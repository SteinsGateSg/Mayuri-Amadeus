#!/usr/bin/env python3
from __future__ import annotations

import sys

from _framework import (
    PROJECT_ROOT,
    add_default_args,
    bootstrap_framework,
    default_gpt_root,
    default_pretrained_root,
)


def main(argv: list[str] | None = None) -> int:
    bootstrap_framework()
    from character_voice_lab import gpt_sovits

    args = list(sys.argv[1:] if argv is None else argv)
    defaults = {
        "--manifest": str(PROJECT_ROOT / "data" / "manifests" / "mayuri_ja_filtered.list"),
        "--exp-name": "mayuri_v2",
        "--version": "v2",
        "--gpt-sovits-root": default_gpt_root(),
        "--pretrained-root": default_pretrained_root(),
    }
    return gpt_sovits.main(add_default_args(args, defaults))


if __name__ == "__main__":
    raise SystemExit(main())
