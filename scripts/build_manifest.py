#!/usr/bin/env python3
from __future__ import annotations

import sys

from _framework import PROJECT_ROOT, add_default_args, bootstrap_framework


def main(argv: list[str] | None = None) -> int:
    bootstrap_framework()
    from character_voice_lab import manifest

    args = list(sys.argv[1:] if argv is None else argv)
    defaults = {
        "--csv": str(PROJECT_ROOT / "data" / "meta" / "mayuri_asr_raw.csv"),
        "--wav-dir": str(PROJECT_ROOT / "data" / "raw" / "wav"),
        "--output-list": str(PROJECT_ROOT / "data" / "manifests" / "mayuri_ja_filtered.list"),
        "--stats-json": str(PROJECT_ROOT / "data" / "manifests" / "mayuri_ja_filtered.stats.json"),
        "--rejects-csv": str(PROJECT_ROOT / "data" / "manifests" / "mayuri_ja_filtered.rejects.csv"),
        "--speaker": "shiina_mayuri",
        "--language": "ja",
    }
    return manifest.main(add_default_args(args, defaults))


if __name__ == "__main__":
    raise SystemExit(main())
