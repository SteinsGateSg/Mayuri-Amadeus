from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def framework_candidates() -> list[Path]:
    env_root = os.environ.get("CHARACTER_VOICE_LAB_ROOT", "").strip()
    candidates: list[Path] = []
    if env_root:
        candidates.append(Path(env_root).expanduser())
    candidates.extend(
        [
            PROJECT_ROOT.parent / "Persona-Forge",
            PROJECT_ROOT.parent / "character-voice-lab",
            PROJECT_ROOT / "third_party" / "Persona-Forge",
            PROJECT_ROOT / "third_party" / "character-voice-lab",
        ]
    )
    return candidates


def bootstrap_framework() -> Path:
    try:
        module = importlib.import_module("character_voice_lab")
        return Path(module.__file__).resolve().parents[1]
    except ModuleNotFoundError:
        pass

    for candidate in framework_candidates():
        package_dir = candidate / "character_voice_lab"
        if package_dir.exists():
            candidate_str = str(candidate.resolve())
            if candidate_str not in sys.path:
                sys.path.insert(0, candidate_str)
            return candidate.resolve()
    searched = "\n".join(str(path) for path in framework_candidates())
    raise RuntimeError(
        "Persona-Forge not found. Install it into the current environment, "
        "set CHARACTER_VOICE_LAB_ROOT, or place a clone at:\n"
        f"{searched}"
    )


def add_default_args(argv: list[str], defaults: dict[str, str]) -> list[str]:
    args = list(argv)
    present = set(arg for arg in args if arg.startswith("--"))
    for flag, value in defaults.items():
        if flag in present or value == "":
            continue
        args.extend([flag, value])
    return args


def default_gpt_root() -> str:
    env_root = os.environ.get("GPT_SOVITS_ROOT", "").strip()
    if env_root:
        return str(Path(env_root).expanduser())
    candidates = [
        PROJECT_ROOT / "third_party" / "GPT-SoVITS",
        PROJECT_ROOT.parent / "GPT-SoVITS",
        PROJECT_ROOT.parent / "amadeus-project" / "sovits" / "GPT-SoVITS",
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate.resolve())
    return ""


def default_pretrained_root() -> str:
    env_root = os.environ.get("GPT_SOVITS_MODEL_ROOT", "").strip()
    if env_root:
        return str(Path(env_root).expanduser())
    candidates = [
        PROJECT_ROOT / "third_party" / "GPT-SoVITS-models",
        PROJECT_ROOT / "models" / "GPT-SoVITS",
        PROJECT_ROOT.parent / "models" / "GPT-SoVITS",
        Path.home() / "models" / "GPT-SoVITS",
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate.resolve())
    return ""
