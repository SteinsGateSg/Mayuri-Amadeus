<div align="center">

# ✦ Mayuri-Amadeus ✦

<p><em>椎名真由理语音发布页 · 面向 GPT-SoVITS 的角色仓库</em></p>

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
  <img src="https://img.shields.io/badge/Voice-椎名真由理-b0463c?style=flat-square" alt="Voice" />
  <img src="https://img.shields.io/badge/SoVITS-e20-8b5e3c?style=flat-square" alt="SoVITS e20" />
  <img src="https://img.shields.io/badge/GPT-e8-6f8aa1?style=flat-square" alt="GPT e8" />
  <img src="https://img.shields.io/badge/Reference%20Bank-10%20moods-c97a54?style=flat-square" alt="Reference Bank" />
</p>

简体中文 · <a href="README.md">English</a>

</div>

`Mayuri-Amadeus` 是围绕一套公开椎名真由理语音版本整理出来的角色仓库：包含参考音频库、模型元数据、demo 资产，以及独立的本地推理入口。

## 仓库内容

- 按情绪分组整理好的参考音频库
- 角色 profile 与最终模型组合元数据
- 独立的 selector 与推理入口
- 数据集元数据、过滤统计与情感标注结果
- 项目主页与发布文档

## 推理链路

这个仓库里的本地推理 **不依赖** `Persona-Forge`。

本地需要准备：

```text
models/gpt/mayuri_v2-e8.ckpt
models/sovits/mayuri_v2_e20.pth
data/raw/wav/          # 仅训练时需要
```

自动选择参考音频：

```bash
python scripts/select_reference.py \
  --target-text "亲爱的你啊，好久不见。" \
  --target-language 中文 \
  --backend heuristic \
  --format json
```

自动选择参考并直接推理：

```bash
python scripts/synthesize.py \
  --auto-select \
  --target-text "おかりん、今日は何をしているの？" \
  --target-language 日文 \
  --output-dir outputs/preview/latest
```

指定固定参考音频推理：

```bash
python scripts/synthesize.py \
  --ref-id MAY_0053 \
  --target-text "おかりん、今日は何をしているの？" \
  --target-language 日文 \
  --output-dir outputs/preview/latest
```

## API Selector

selector 支持 OpenAI 兼容接口，同时保留了本地模型接口位置，后续可以直接补上。

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

## 训练链路

训练封装仍然使用通用框架仓库：

- `Persona-Forge`

推荐安装方式：

```bash
pip install -e /path/to/Persona-Forge
```

之后执行：

```bash
python scripts/build_manifest.py
python scripts/train_gpt_sovits.py doctor
```

## 仓库结构

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

## 资产边界

纳入 git：

- 最终参考音频库
- 转写 CSV
- 过滤统计与 rejects
- 情绪标注元数据
- 文档与轻量脚本

不纳入 git：

- 全量 `data/raw/wav/`
- 最终大模型权重
- 生成出来的 `.list` manifest
- 本地试听输出
- Hugging Face 上传 staging 目录

## 最终模型组合

- SoVITS：`e20`
- GPT：`e8`

详见：

- [profiles/mayuri.yaml](profiles/mayuri.yaml)
- [weights/final_model_combo.json](weights/final_model_combo.json)
- [weights/README.md](weights/README.md)
