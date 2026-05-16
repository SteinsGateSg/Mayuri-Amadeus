<div align="center">

# ✦ Mayuri-Amadeus ✦

<p><em>Shiina Mayuri Voice Release · Character Repository for GPT-SoVITS</em></p>

<p>
  <a href="https://steinsgatesg.github.io/Mayuri-Amadeus/">
    <img src="https://img.shields.io/badge/🌆%20Homepage-4a2f23?style=for-the-badge&logoColor=fff7f2" alt="Homepage" />
  </a>
  <a href="https://github.com/SteinsGateSg/Mayuri-Amadeus">
    <img src="https://img.shields.io/badge/🐙%20GitHub-181717?style=for-the-badge&logo=github&logoColor=ffffff" alt="GitHub repository" />
  </a>
  <a href="https://huggingface.co/SteinsGateSg/mayuri-voice">
    <img src="https://img.shields.io/badge/🤗%20HF%20Model-fcd34d?style=for-the-badge&logoColor=2b1d13" alt="Hugging Face model" />
  </a>
  <a href="https://huggingface.co/datasets/SteinsGateSg/mayuri-voice-dataset">
    <img src="https://img.shields.io/badge/📚%20HF%20Dataset-f59e0b?style=for-the-badge&logoColor=2b1d13" alt="Hugging Face dataset" />
  </a>
</p>

<p>
  <img src="https://img.shields.io/badge/Voice-Shiina%20Mayuri-b0463c?style=flat-square" alt="Voice" />
  <img src="https://img.shields.io/badge/SoVITS-e20-8b5e3c?style=flat-square" alt="SoVITS e20" />
  <img src="https://img.shields.io/badge/GPT-e8-6f8aa1?style=flat-square" alt="GPT e8" />
  <img src="https://img.shields.io/badge/Reference%20Bank-10%20moods-c97a54?style=flat-square" alt="Reference Bank" />
</p>

English · <a href="README_ZH.md">简体中文</a>

</div>

`Mayuri-Amadeus` is a character repository centered on one public Shiina Mayuri voice release: curated references, model metadata, demo assets, and standalone local inference.

## What Lives Here

- curated reference clips grouped by mood
- character profile and final model-pair metadata
- standalone selector and synthesis entrypoints
- dataset metadata, filtering stats, and emotion labels
- project homepage and release documents

## Inference Path

Local inference in this repository does **not** depend on `Persona-Forge`.

Required local files:

```text
models/gpt/mayuri_v2-e8.ckpt
models/sovits/mayuri_v2_e20.pth
data/raw/wav/          # optional for training only
```

Select a reference automatically:

```bash
python scripts/select_reference.py \
  --target-text "亲爱的你啊，好久不见。" \
  --target-language 中文 \
  --backend heuristic \
  --format json
```

Run synthesis with automatic reference selection:

```bash
python scripts/synthesize.py \
  --auto-select \
  --target-text "おかりん、今日は何をしているの？" \
  --target-language 日文 \
  --output-dir outputs/preview/latest
```

Run synthesis with a fixed reference:

```bash
python scripts/synthesize.py \
  --ref-id MAY_0053 \
  --target-text "おかりん、今日は何をしているの？" \
  --target-language 日文 \
  --output-dir outputs/preview/latest
```

## API Selector

The selector supports an OpenAI-compatible API backend and keeps a reserved local-model interface for later expansion.

```bash
export SELECTOR_API_BASE="https://dashscope.aliyuncs.com/compatible-mode/v1"
export SELECTOR_API_KEY="your_key"
export SELECTOR_MODEL="qwen3.6-plus"

python scripts/select_reference.py \
  --target-text "元気出してほしいよ。" \
  --target-language 日文 \
  --backend api \
  --format json
```

## Training Path

Training wrappers still use the generic framework repository:

- `Persona-Forge`

Recommended install:

```bash
pip install -e /path/to/Persona-Forge
```

Then:

```bash
python scripts/build_manifest.py
python scripts/train_gpt_sovits.py doctor
```

## Repository Layout

```text
Mayuri-Amadeus/
  data/
    meta/
    manifests/
    raw/
  docs/
    index.html
    assets/
  metadata/
    reference_bank/
  models/
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
    select_reference.py
    synthesize.py
    train_gpt_sovits.py
  weights/
    final_model_combo.json
```

## Assets

Tracked in git:

- selected reference bank
- transcript CSV
- filtering stats and rejects
- emotion-label metadata
- docs and lightweight wrappers

Not tracked in git:

- full `data/raw/wav/`
- final large weight files
- generated `.list` manifests
- local preview outputs
- Hugging Face upload staging folders

## Final Pair

- SoVITS: `e20`
- GPT: `e8`

See:

- [profiles/mayuri.yaml](profiles/mayuri.yaml)
- [weights/final_model_combo.json](weights/final_model_combo.json)
- [weights/README.md](weights/README.md)
