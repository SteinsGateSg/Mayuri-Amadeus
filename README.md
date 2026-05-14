# Mayuri-Amadeus

中文文档： [README_ZH.md](README_ZH.md)

Project homepage: [docs/index.html](docs/index.html)

`Mayuri-Amadeus` is a standalone Shiina Mayuri character-instance repository prepared for GitHub publication.

This repository contains:

- project documentation and landing page
- curated reference clips grouped by emotion
- character profile and final model metadata
- thin wrapper scripts for `Persona-Forge`
- dataset metadata and training-manifest statistics

Large assets are intentionally published outside this repository:

- final model weights: Hugging Face model repo
- full audio dataset: Hugging Face dataset repo
- local training outputs: not tracked in git

## External Repositories

- GitHub character repo:
  `https://github.com/SteinsGateSg/Mayuri-Amadeus`
- Hugging Face model:
  `https://huggingface.co/SteinsGateSg/mayuri-voice`
- Hugging Face dataset:
  `https://huggingface.co/datasets/SteinsGateSg/mayuri-voice-dataset`

## Repository Layout

```text
Mayuri-Amadeus/
  configs/
    mayuri_v2.env.example
  data/
    meta/
      mayuri_asr_raw.csv
    manifests/
      mayuri_ja_filtered.stats.json
      mayuri_ja_filtered.rejects.csv
      README.md
    raw/
      README.md
  docs/
    index.html
    assets/
  metadata/
    reference_bank/
      emotion_labels.csv
      emotion_labels.jsonl
      emotion_summary.json
      reference_shortlist.csv
  models/
    README.md
    gpt/
    sovits/
  profiles/
    mayuri.yaml
  refs/
    index.csv
    ...
  scripts/
    build_manifest.py
    label_reference_emotions.py
    synthesize.py
    train_gpt_sovits.py
  weights/
    final_model_combo.json
    README.md
```

## What Is Included

Included in git:

- final selected reference bank
- dataset transcript CSV
- filtering stats and rejects report
- emotion-label metadata
- role-specific docs and wrappers

Not included in git:

- full `data/raw/wav/` training audio
- final GPT / SoVITS weight files
- generated manifest `.list`
- local preview outputs
- Hugging Face upload staging folders

## Framework Dependency

This repository depends on the generic framework repo:

- `Persona-Forge`

Recommended local development install:

```bash
pip install -e /path/to/Persona-Forge
```

After the framework repo is public, you can also install it from GitHub:

```bash
pip install git+https://github.com/SteinsGateSg/Persona-Forge.git
```

If you prefer not to install it globally, you can place a clone at:

```text
third_party/Persona-Forge
```

inside this repository.

## Quick Start

### 1. Clone this repository

```bash
git clone https://github.com/SteinsGateSg/Mayuri-Amadeus.git
cd Mayuri-Amadeus
```

### 2. Install the framework

```bash
pip install -e /path/to/Persona-Forge
```

### 3. Prepare local model files

Download the final published weights from the Hugging Face model repo into:

```text
models/gpt/mayuri_v2-e8.ckpt
models/sovits/mayuri_v2_e20.pth
```

### 4. Run synthesis

```bash
python scripts/synthesize.py \
  --ref-id MAY_0053 \
  --target-text "おかりん、今日は何をしているの？" \
  --target-language 日文 \
  --output-dir outputs/preview/latest
```

This wrapper uses:

- `refs/index.csv` for reference lookup
- `models/gpt/mayuri_v2-e8.ckpt` by default
- `models/sovits/mayuri_v2_e20.pth` by default

### 5. Prepare for training

Download the full dataset from the Hugging Face dataset repo and place WAV files in:

```text
data/raw/wav/
```

Then rebuild the local manifest:

```bash
python scripts/build_manifest.py
```

After that, run:

```bash
python scripts/train_gpt_sovits.py doctor
```

## Training Notes

- This repository is the character repo, not the generic framework repo.
- The reusable training logic lives in `Persona-Forge`.
- The generated `.list` manifest is intentionally not tracked because it depends on the local clone path.
- The bundled reference bank is small enough for GitHub and is intended for inference and demos.

## Final Model Pair

- SoVITS: `e20`
- GPT: `e8`

See:

- [profiles/mayuri.yaml](profiles/mayuri.yaml)
- [weights/final_model_combo.json](weights/final_model_combo.json)
- [weights/README.md](weights/README.md)
