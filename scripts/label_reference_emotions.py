#!/usr/bin/env python3
from __future__ import annotations

import sys

from _framework import PROJECT_ROOT, add_default_args, bootstrap_framework


def main(argv: list[str] | None = None) -> int:
    bootstrap_framework()
    from character_voice_lab import reference_bank

    args = list(sys.argv[1:] if argv is None else argv)
    defaults = {
        "--manifest": str(PROJECT_ROOT / "data" / "manifests" / "mayuri_ja_filtered.list"),
        "--output-dir": str(PROJECT_ROOT / "outputs" / "reference_bank"),
    }
    return reference_bank.main(add_default_args(args, defaults))


if __name__ == "__main__":
    raise SystemExit(main())
