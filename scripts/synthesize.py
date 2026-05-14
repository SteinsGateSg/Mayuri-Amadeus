#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from pathlib import Path

from _framework import PROJECT_ROOT, add_default_args, bootstrap_framework, default_gpt_root


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
    return parser.parse_args(argv)


def resolve_ref_from_index(sample_id: str) -> tuple[Path, Path]:
    with DEFAULT_REFS_INDEX.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["sample_id"].strip() == sample_id:
                wav_path = PROJECT_ROOT / row["wav_path"]
                text_path = PROJECT_ROOT / row["text_path"]
                return wav_path, text_path
    raise FileNotFoundError(f"Reference sample id not found in refs/index.csv: {sample_id}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    bootstrap_framework()
    from character_voice_lab import synthesize

    if args.ref_id:
        ref_audio, ref_text_file = resolve_ref_from_index(args.ref_id)
    else:
        ref_audio = Path(args.ref_audio).expanduser().resolve() if args.ref_audio else None
        ref_text_file = Path(args.ref_text_file).expanduser().resolve() if args.ref_text_file else None

    defaults = {
        "--gpt-sovits-root": args.gpt_sovits_root,
        "--gpt-model": args.gpt_model,
        "--sovits-model": args.sovits_model,
        "--output-dir": args.output_dir,
        "--ref-language": args.ref_language,
        "--target-language": args.target_language,
    }

    if ref_audio is not None:
        defaults["--ref-audio"] = str(ref_audio)
    if ref_text_file is not None:
        defaults["--ref-text-file"] = str(ref_text_file)
    elif args.ref_text:
        defaults["--ref-text"] = args.ref_text

    if args.target_text_file:
        defaults["--target-text-file"] = args.target_text_file
    elif args.target_text:
        defaults["--target-text"] = args.target_text

    return synthesize.main(add_default_args([], defaults))


if __name__ == "__main__":
    raise SystemExit(main())
