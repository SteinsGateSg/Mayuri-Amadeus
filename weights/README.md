# Weights

This repository does not check large model files into git.

The final selected combination is:

- SoVITS: `mayuri_v2_e20`
- GPT: `mayuri_v2-e8`

Expected local layout after downloading from Hugging Face:

```text
models/
  gpt/
    mayuri_v2-e8.ckpt
  sovits/
    mayuri_v2_e20.pth
```

Hugging Face sources:

- Model repo:
  `https://huggingface.co/SteinsGateSg/mayuri-voice`
- Dataset repo:
  `https://huggingface.co/datasets/SteinsGateSg/mayuri-voice-dataset`

This repository is the character-instance repo. The generic reusable workflow lives in `Persona-Forge`.
