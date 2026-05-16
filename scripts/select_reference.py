#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from _framework import PROJECT_ROOT
from _selector_core import select_reference_from_text


DEFAULT_REFS_INDEX = PROJECT_ROOT / "refs" / "index.csv"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Select a Mayuri reference clip from the curated reference bank."
    )
    parser.add_argument("--target-text", default="", help="Target text content")
    parser.add_argument("--target-text-file", default="", help="Path to target text file")
    parser.add_argument("--target-language", default="日文")
    parser.add_argument("--backend", choices=["api", "heuristic", "local"], default="heuristic")
    parser.add_argument("--api-base", default="", help="OpenAI-compatible base URL")
    parser.add_argument("--api-key", default="", help="Explicit API key")
    parser.add_argument("--api-key-env", default="SELECTOR_API_KEY", help="Environment variable name for API key lookup")
    parser.add_argument("--model", default="", help="API model name")
    parser.add_argument("--local-model", default="", help="Reserved local-model path placeholder")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--format", choices=["json", "ref-id", "shell"], default="json")
    parser.add_argument("--max-retries", type=int, default=3)
    parser.add_argument("--sleep", type=float, default=1.5)
    return parser.parse_args(argv)


def read_target_text(args: argparse.Namespace) -> str:
    if args.target_text:
        return args.target_text.strip()
    if args.target_text_file:
        return Path(args.target_text_file).expanduser().read_text(encoding="utf-8").strip()
    raise SystemExit("Either --target-text or --target-text-file is required.")


def emit_result(fmt: str, result: dict) -> int:
    selection = result["selection"]
    if fmt == "ref-id":
        print(selection["sample_id"])
        return 0
    if fmt == "shell":
        print(f'REF_ID="{selection["sample_id"]}"')
        return 0
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    result = select_reference_from_text(
        refs_index=DEFAULT_REFS_INDEX,
        asset_root=PROJECT_ROOT,
        target_text=read_target_text(args),
        target_language=args.target_language,
        backend=args.backend,
        api_base=args.api_base,
        api_key=args.api_key,
        api_key_env=args.api_key_env,
        model=args.model,
        local_model=args.local_model,
        top_k=args.top_k,
        max_retries=args.max_retries,
        sleep=args.sleep,
    )
    return emit_result(args.format, result)


if __name__ == "__main__":
    raise SystemExit(main())
