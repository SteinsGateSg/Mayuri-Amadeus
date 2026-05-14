# Mayuri-Amadeus

English documentation: [README.md](README.md)

项目主页： [docs/index.html](docs/index.html)

`Mayuri-Amadeus` 是一个面向 GitHub 发布整理过的椎名真由理角色实例仓库。

这个仓库主要包含：

- 项目文档和主页
- 按情绪分组整理好的参考音频库
- 角色 profile 与最终模型组合说明
- 面向 `Persona-Forge` 的薄封装脚本
- 数据集元数据与训练筛选统计

大资产不直接放在这个 GitHub 仓库里：

- 最终模型权重：放在 Hugging Face model repo
- 全量训练音频：放在 Hugging Face dataset repo
- 本地训练输出：不纳入 git

## 外部仓库

- GitHub 角色仓库：
  `https://github.com/SteinsGateSg/Mayuri-Amadeus`
- Hugging Face 模型仓库：
  `https://huggingface.co/SteinsGateSg/mayuri-voice`
- Hugging Face 数据集仓库：
  `https://huggingface.co/datasets/SteinsGateSg/mayuri-voice-dataset`

## 仓库结构

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

## 仓库中包含什么

纳入 git 的内容：

- 最终整理好的参考音频库
- 数据集转写 CSV
- 过滤统计与 rejects 报告
- 情绪标注元数据
- 角色专属文档与脚本封装

不纳入 git 的内容：

- 全量 `data/raw/wav/` 训练音频
- 最终 GPT / SoVITS 权重文件
- 生成出来的 `.list` manifest
- 本地试听输出
- Hugging Face 上传 staging 目录

## 框架依赖

这个仓库依赖通用训练框架仓库：

- `Persona-Forge`

本地开发推荐这样安装：

```bash
pip install -e /path/to/Persona-Forge
```

等框架仓库公开后，也可以直接从 GitHub 安装：

```bash
pip install git+https://github.com/SteinsGateSg/Persona-Forge.git
```

如果你不想全局安装，也可以把框架仓库克隆到：

```text
third_party/Persona-Forge
```

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/SteinsGateSg/Mayuri-Amadeus.git
cd Mayuri-Amadeus
```

### 2. 安装框架

```bash
pip install -e /path/to/Persona-Forge
```

### 3. 准备本地模型文件

从 Hugging Face 模型仓库下载最终权重，并放到：

```text
models/gpt/mayuri_v2-e8.ckpt
models/sovits/mayuri_v2_e20.pth
```

### 4. 直接推理

```bash
python scripts/synthesize.py \
  --ref-id MAY_0053 \
  --target-text "おかりん、今日は何をしているの？" \
  --target-language 日文 \
  --output-dir outputs/preview/latest
```

这个封装默认使用：

- `refs/index.csv` 里的参考索引
- `models/gpt/mayuri_v2-e8.ckpt`
- `models/sovits/mayuri_v2_e20.pth`

### 5. 准备训练

先从 Hugging Face 数据集仓库下载全量音频，放到：

```text
data/raw/wav/
```

然后重建本地 manifest：

```bash
python scripts/build_manifest.py
```

之后执行：

```bash
python scripts/train_gpt_sovits.py doctor
```

## 训练说明

- 这个仓库是角色实例仓库，不是通用训练框架仓库
- 可复用的训练逻辑在 `Persona-Forge`
- `.list` manifest 不纳入 git，因为它依赖本地克隆路径
- 精选参考音频库体积较小，保留在 GitHub 仓库里，方便试听和 demo

## 最终模型组合

- SoVITS：`e20`
- GPT：`e8`

详细信息见：

- [profiles/mayuri.yaml](profiles/mayuri.yaml)
- [weights/final_model_combo.json](weights/final_model_combo.json)
- [weights/README.md](weights/README.md)
