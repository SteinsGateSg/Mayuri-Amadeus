#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import os
import subprocess
import sys
from pathlib import Path

from _framework import PROJECT_ROOT, default_gpt_root
from _selector_core import select_reference_from_text


DEFAULT_GPT_MODEL = PROJECT_ROOT / "models" / "gpt" / "mayuri_v2-e8.ckpt"
DEFAULT_SOVITS_MODEL = PROJECT_ROOT / "models" / "sovits" / "mayuri_v2_e20.pth"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "outputs" / "preview" / "latest"
DEFAULT_REFS_INDEX = PROJECT_ROOT / "refs" / "index.csv"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Synthesize Mayuri voice using the final selected model pair.")
    parser.add_argument("--ref-id", default="", help="Reference sample id from refs/index.csv, e.g. MAY_0053")
    parser.add_argument("--ref-audio", default="", help="Override reference audio path")
    parser.add_argument("--ref-text-file", default="", help="Override reference text file path")
    parser.add_argument("--ref-text", default="", help="Override reference text content")
    parser.add_argument("--target-text-file", default="", help="Path to target text file")
    parser.add_argument("--target-text", default="", help="Target text content")
    parser.add_argument("--ref-language", default="日文")
    parser.add_argument("--target-language", default="日文")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--gpt-model", default=str(DEFAULT_GPT_MODEL))
    parser.add_argument("--sovits-model", default=str(DEFAULT_SOVITS_MODEL))
    parser.add_argument("--gpt-sovits-root", default=default_gpt_root())
    parser.add_argument("--auto-select", action="store_true", help="Automatically select a reference clip from refs/index.csv")
    parser.add_argument("--selector-backend", choices=["api", "heuristic", "local"], default="heuristic")
    parser.add_argument("--selector-api-base", default="", help="OpenAI-compatible base URL for selector")
    parser.add_argument("--selector-api-key", default="", help="Explicit selector API key")
    parser.add_argument("--selector-api-key-env", default="SELECTOR_API_KEY", help="Environment variable name for selector API key lookup")
    parser.add_argument("--selector-model", default="", help="Selector API model name")
    parser.add_argument("--selector-local-model", default="", help="Reserved selector local-model placeholder")
    parser.add_argument("--selector-top-k", type=int, default=5)
    parser.add_argument("--selector-max-retries", type=int, default=3)
    parser.add_argument("--selector-sleep", type=float, default=1.5)
    return parser.parse_args(argv)


def resolve_path(path: str | Path) -> Path:
    return Path(path).expanduser().resolve()


def require_exists(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"{label} not found: {path}")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def extend_pythonpath(env: dict[str, str], gpt_root: Path) -> dict[str, str]:
    extra_paths = [
        str(gpt_root),
        str(gpt_root / "GPT_SoVITS"),
        str(gpt_root / "GPT_SoVITS" / "BigVGAN"),
        str(gpt_root / "tools"),
        str(gpt_root / "tools" / "asr"),
        str(gpt_root / "tools" / "uvr5"),
    ]
    current = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = os.pathsep.join(extra_paths + ([current] if current else []))
    return env


def print_command(cmd: list[str], cwd: Path) -> None:
    print(f"[run] (cwd={cwd}) {' '.join(cmd)}")


def materialize_text(path: str | None, text: str | None, output_dir: Path, filename: str) -> Path:
    if path:
        resolved = resolve_path(path)
        require_exists(resolved, filename)
        return resolved
    assert text is not None
    ensure_dir(output_dir)
    temp_path = output_dir / filename
    temp_path.write_text(text.strip() + "\n", encoding="utf-8")
    return temp_path


def read_target_text(args: argparse.Namespace) -> str:
    if args.target_text:
        return args.target_text.strip()
    if args.target_text_file:
        return Path(args.target_text_file).expanduser().read_text(encoding="utf-8").strip()
    raise SystemExit("Either --target-text or --target-text-file is required.")


def resolve_ref_from_index(sample_id: str) -> tuple[Path, Path]:
    with DEFAULT_REFS_INDEX.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["sample_id"].strip() == sample_id:
                wav_path = PROJECT_ROOT / row["wav_path"]
                text_path = PROJECT_ROOT / row["text_path"]
                return wav_path, text_path
    raise FileNotFoundError(f"Reference sample id not found in refs/index.csv: {sample_id}")


def pick_reference(args: argparse.Namespace, target_text: str) -> tuple[Path, Path, str | None]:
    if args.ref_id:
        ref_audio, ref_text_file = resolve_ref_from_index(args.ref_id)
        return ref_audio, ref_text_file, args.ref_id

    if args.ref_audio:
        ref_audio = resolve_path(args.ref_audio)
        ref_text_file = resolve_path(args.ref_text_file) if args.ref_text_file else None
        if ref_text_file is None and not args.ref_text:
            raise SystemExit("When --ref-audio is provided, also provide --ref-text-file or --ref-text.")
        return ref_audio, ref_text_file, None

    if args.auto_select:
        selection = select_reference_from_text(
            refs_index=DEFAULT_REFS_INDEX,
            asset_root=PROJECT_ROOT,
            target_text=target_text,
            target_language=args.target_language,
            backend=args.selector_backend,
            api_base=args.selector_api_base,
            api_key=args.selector_api_key,
            api_key_env=args.selector_api_key_env,
            model=args.selector_model,
            local_model=args.selector_local_model,
            top_k=args.selector_top_k,
            max_retries=args.selector_max_retries,
            sleep=args.selector_sleep,
        )
        ref_id = selection["selection"]["sample_id"]
        ref_audio, ref_text_file = resolve_ref_from_index(ref_id)
        print(f"[selected] ref_id={ref_id} emotion={selection['selection']['emotion']} score={selection['selection']['selector_score']}")
        return ref_audio, ref_text_file, ref_id

    raise SystemExit("Provide --ref-id, or --ref-audio with text, or use --auto-select.")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    gpt_root = resolve_path(args.gpt_sovits_root)
    gpt_model = resolve_path(args.gpt_model)
    sovits_model = resolve_path(args.sovits_model)
    output_dir = resolve_path(args.output_dir)
    target_text = read_target_text(args)

    ref_audio, ref_text_file, _ = pick_reference(args, target_text)

    require_exists(gpt_root, "GPT-SoVITS root")
    require_exists(gpt_model, "GPT model")
    require_exists(sovits_model, "SoVITS model")
    require_exists(ref_audio, "reference audio")
    ensure_dir(output_dir)

    ref_text_path = materialize_text(str(ref_text_file) if ref_text_file else None, args.ref_text, output_dir, "reference.txt")
    target_text_path = materialize_text(args.target_text_file, args.target_text, output_dir, "target.txt")

    env = extend_pythonpath(os.environ.copy(), gpt_root)
    cmd = [
        sys.executable,
        "-m",
        "GPT_SoVITS.inference_cli",
        "--gpt_model",
        str(gpt_model),
        "--sovits_model",
        str(sovits_model),
        "--ref_audio",
        str(ref_audio),
        "--ref_text",
        str(ref_text_path),
        "--ref_language",
        args.ref_language,
        "--target_text",
        str(target_text_path),
        "--target_language",
        args.target_language,
        "--output_path",
        str(output_dir),
    ]
    print_command(cmd, gpt_root)
    subprocess.run(cmd, cwd=gpt_root, env=env, check=True)
    print(f"[done] synthesized audio under {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
