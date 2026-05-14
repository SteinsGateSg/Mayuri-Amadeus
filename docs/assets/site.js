const translations = {
  en: {
    title: "Mayuri-Amadeus",
    description:
      "Mayuri-Amadeus is a Shiina Mayuri character-instance repository for GPT-SoVITS training, reference management, and inference.",
    "hero.eyebrow": "Character Voice System",
    "hero.lede":
      "A Shiina Mayuri character repository shaped for public release: curated refs, model metadata, training wrappers, and a lightweight inference workflow built around GPT-SoVITS.",
    "hero.modelButton": "Model on Hugging Face",
    "hero.datasetButton": "Dataset on Hugging Face",
    "hero.kicker": "Final Pair",
    "hero.microcopy":
      "Reference-driven single-character setup tuned on top of GPT-SoVITS v2.",
    "stats.dataset": "dataset WAV clips",
    "stats.filtered": "filtered training samples",
    "stats.duration": "filtered speech duration",
    "stats.refs": "reference-bank emotion groups",
    "overview.tag": "What This Repo Is",
    "overview.title": "Character repo, not framework repo",
    "overview.body":
      "Mayuri-Amadeus is the character-instance side of a two-repo split. It keeps Mayuri-specific assets and metadata, while reusable workflow code lives in Persona-Forge.",
    "overview.card1.title": "Curated Refs",
    "overview.card1.body":
      "Small, emotion-grouped reference clips are included directly in the repository.",
    "overview.card2.title": "HF-Backed Assets",
    "overview.card2.body":
      "Large model files and the full dataset are published on Hugging Face instead of git.",
    "overview.card3.title": "Inference-Ready",
    "overview.card3.body":
      "A thin wrapper resolves the final GPT + SoVITS pair once you download them into models/.",
    "overview.card4.title": "LLM-Friendly",
    "overview.card4.body":
      "The repository is structured as a reusable character asset for later dialogue and retrieval demos.",
    "quick.tag": "Quick Start",
    "quick.title": "Run local synthesis in one command",
    "quick.body":
      "After downloading the final weights from Hugging Face into models/, you can generate Mayuri speech directly with the bundled reference bank.",
    "demo.tag": "Audio Demo",
    "demo.title": "Short clips from the current release",
    "demo.body":
      "These samples are kept intentionally short so the homepage feels like a real release page rather than a raw experiment log.",
    "demo.ref.badge": "Reference",
    "demo.ref.title": "Neutral reference clip",
    "demo.ref.body":
      "One curated line from the reference bank used to anchor tone and pacing.",
    "demo.jp.badge": "Japanese",
    "demo.jp.title": "Japanese synthesis",
    "demo.jp.body":
      "Local inference using the final public pair: SoVITS e20 plus GPT e8.",
    "demo.zh.badge": "Chinese",
    "demo.zh.title": "Cross-lingual synthesis",
    "demo.zh.body":
      "A simple Chinese line, kept here to show the model pair beyond same-language playback.",
    "demo.lineLabel": "Line",
    "links.repo.tag": "Repository",
    "links.repo.title": "Core Documents",
    "links.assets.tag": "Assets",
    "links.assets.title": "What is inside",
    "links.external.tag": "External",
    "links.external.title": "Published endpoints",
    "links.external.model": "HF model repo",
    "links.external.dataset": "HF dataset repo",
    "links.external.github": "GitHub repo",
    "links.external.framework": "Persona-Forge framework repo",
    "roadmap.tag": "Next",
    "roadmap.title": "Where this repository is headed",
    "roadmap.item1.title": "1. Character release",
    "roadmap.item1.body":
      "Ship a clean public GitHub repo linked to HF weights and dataset.",
    "roadmap.item2.title": "2. Reference workflows",
    "roadmap.item2.body":
      "Improve emotion-aware reference selection and publish better demo comparisons.",
    "roadmap.item3.title": "3. LLM playground",
    "roadmap.item3.body":
      "Connect the voice system to role-style generation, retrieval, and dialogue planning."
  },
  zh: {
    title: "Mayuri-Amadeus",
    description:
      "Mayuri-Amadeus 是一个面向 GPT-SoVITS 的椎名真由理角色实例仓库，包含参考库、模型元数据与推理入口。",
    "hero.eyebrow": "角色语音系统",
    "hero.lede":
      "一个面向公开发布整理过的椎名真由理角色仓库：包含精选参考音频、模型元数据、训练封装脚本，以及围绕 GPT-SoVITS 的轻量推理工作流。",
    "hero.modelButton": "前往 Hugging Face 模型仓库",
    "hero.datasetButton": "前往 Hugging Face 数据集仓库",
    "hero.kicker": "最终模型组合",
    "hero.microcopy":
      "基于 GPT-SoVITS v2 调优的 reference-driven 单角色方案。",
    "stats.dataset": "数据集音频片段",
    "stats.filtered": "过滤后训练样本",
    "stats.duration": "过滤后语音时长",
    "stats.refs": "参考库情绪分组",
    "overview.tag": "仓库定位",
    "overview.title": "这是角色仓库，不是框架仓库",
    "overview.body":
      "Mayuri-Amadeus 是“两仓库拆分”里的角色实例侧。它保存真由理专属的数据、参考库和模型元数据，而可复用工作流放在 Persona-Forge 中。",
    "overview.card1.title": "精选参考库",
    "overview.card1.body":
      "体积较小、按情绪分组的参考音频直接保留在仓库里，便于试听与演示。",
    "overview.card2.title": "HF 承载大资产",
    "overview.card2.body":
      "大模型文件和全量数据集都放在 Hugging Face，而不是直接塞进 git。",
    "overview.card3.title": "可直接推理",
    "overview.card3.body":
      "只要把最终 GPT 与 SoVITS 权重下载到 models/ 下，这个仓库就能直接跑本地推理。",
    "overview.card4.title": "适合接入 LLM",
    "overview.card4.body":
      "整体结构被设计成一个可复用的角色语音资产，后续可以接到对话、检索和角色扮演 playground 上。",
    "quick.tag": "快速开始",
    "quick.title": "一条命令生成语音",
    "quick.body":
      "把最终权重从 Hugging Face 下载到 models/ 后，就可以直接结合内置参考库生成真由理语音。",
    "demo.tag": "音频 Demo",
    "demo.title": "当前版本的短音频示例",
    "demo.body":
      "这些样例刻意保持简短，让首页更像正式发布页，而不是原始实验日志。",
    "demo.ref.badge": "参考音频",
    "demo.ref.title": "中性参考句",
    "demo.ref.body":
      "来自参考库的一条精选台词，用来作为语气和节奏锚点。",
    "demo.jp.badge": "日文生成",
    "demo.jp.title": "日文推理示例",
    "demo.jp.body":
      "使用公开定版组合本地生成：SoVITS e20 + GPT e8。",
    "demo.zh.badge": "中文生成",
    "demo.zh.title": "跨语种推理示例",
    "demo.zh.body":
      "保留一句简短中文样例，用来展示这套模型组合不只限于同语种复述。",
    "demo.lineLabel": "台词",
    "links.repo.tag": "仓库内容",
    "links.repo.title": "核心文档",
    "links.assets.tag": "资产",
    "links.assets.title": "仓库里有什么",
    "links.external.tag": "外部链接",
    "links.external.title": "公开发布入口",
    "links.external.model": "HF 模型仓库",
    "links.external.dataset": "HF 数据集仓库",
    "links.external.github": "GitHub 角色仓库",
    "links.external.framework": "Persona-Forge 框架仓库",
    "roadmap.tag": "下一步",
    "roadmap.title": "这个仓库接下来会做什么",
    "roadmap.item1.title": "1. 角色仓库发布",
    "roadmap.item1.body":
      "把它整理成一个干净的公开 GitHub 仓库，并链接到 HF 上的模型与数据集。",
    "roadmap.item2.title": "2. 参考库工作流",
    "roadmap.item2.body":
      "继续改进情绪参考选择流程，并发布更规范的试听对比。",
    "roadmap.item3.title": "3. LLM Playground",
    "roadmap.item3.body":
      "把这套语音系统接到角色风格生成、检索和对话规划上。"
  },
  ja: {
    title: "Mayuri-Amadeus",
    description:
      "Mayuri-Amadeus は GPT-SoVITS ベースの椎名まゆりキャラクター音声リポジトリです。参照音声バンク、モデル情報、推論入口を含みます。",
    "hero.eyebrow": "キャラクターボイスシステム",
    "hero.lede":
      "椎名まゆりのために公開向けに整えたキャラクターリポジトリ。厳選された参照音声、モデルメタデータ、学習ラッパー、そして GPT-SoVITS 上の軽量推論ワークフローをまとめています。",
    "hero.modelButton": "Hugging Face モデルへ",
    "hero.datasetButton": "Hugging Face データセットへ",
    "hero.kicker": "最終モデル構成",
    "hero.microcopy":
      "GPT-SoVITS v2 上で調整した reference-driven 単一キャラクター構成です。",
    "stats.dataset": "データセット音声クリップ",
    "stats.filtered": "学習用フィルタ済みサンプル",
    "stats.duration": "フィルタ後の総音声時間",
    "stats.refs": "参照バンク感情カテゴリ",
    "overview.tag": "このリポジトリについて",
    "overview.title": "これはキャラクター側であり、フレームワーク側ではない",
    "overview.body":
      "Mayuri-Amadeus は二分割構成のキャラクター側です。まゆり固有のデータ、参照バンク、モデルメタデータを保持し、再利用可能なワークフローは Persona-Forge に分離されています。",
    "overview.card1.title": "厳選参照バンク",
    "overview.card1.body":
      "小さく整理された感情別参照クリップを直接リポジトリに含めています。",
    "overview.card2.title": "大きな資産は HF へ",
    "overview.card2.body":
      "大きなモデルとフルデータセットは git ではなく Hugging Face 側で配布します。",
    "overview.card3.title": "推論しやすい構成",
    "overview.card3.body":
      "最終 GPT と SoVITS を models/ に置くだけでローカル推論が動くようになっています。",
    "overview.card4.title": "LLM 連携向け",
    "overview.card4.body":
      "対話、検索、ロールプレイ用 playground に接続しやすいキャラクター音声資産として構成しています。",
    "quick.tag": "クイックスタート",
    "quick.title": "1 コマンドで音声生成",
    "quick.body":
      "Hugging Face から最終重みを models/ に置けば、同梱の参照バンクでそのまままゆり音声を生成できます。",
    "demo.tag": "音声デモ",
    "demo.title": "現行リリースの短いサンプル",
    "demo.body":
      "トップページを実験ログではなく公開ページらしく見せるため、短いサンプルだけを置いています。",
    "demo.ref.badge": "参照音声",
    "demo.ref.title": "ニュートラル参照クリップ",
    "demo.ref.body":
      "話し方とテンポのアンカーとして使う、参照バンク中の代表的な 1 行です。",
    "demo.jp.badge": "日本語生成",
    "demo.jp.title": "日本語推論サンプル",
    "demo.jp.body":
      "公開用の最終組み合わせ、SoVITS e20 と GPT e8 を使ったローカル推論です。",
    "demo.zh.badge": "中国語生成",
    "demo.zh.title": "クロスリンガル推論サンプル",
    "demo.zh.body":
      "同言語再生だけでなく、簡単な中国語文にも対応できることを示す短いサンプルです。",
    "demo.lineLabel": "台詞",
    "links.repo.tag": "リポジトリ",
    "links.repo.title": "主要ドキュメント",
    "links.assets.tag": "アセット",
    "links.assets.title": "含まれているもの",
    "links.external.tag": "外部リンク",
    "links.external.title": "公開先",
    "links.external.model": "HF モデルリポジトリ",
    "links.external.dataset": "HF データセットリポジトリ",
    "links.external.github": "GitHub キャラクターリポジトリ",
    "links.external.framework": "Persona-Forge フレームワークリポジトリ",
    "roadmap.tag": "次の段階",
    "roadmap.title": "このリポジトリの次の展開",
    "roadmap.item1.title": "1. キャラクターリリース",
    "roadmap.item1.body":
      "HF のモデルとデータセットを参照する、整った公開 GitHub リポジトリとして仕上げる。",
    "roadmap.item2.title": "2. 参照ワークフロー",
    "roadmap.item2.body":
      "感情ベースの参照選択を改善し、より整った試聴比較を公開する。",
    "roadmap.item3.title": "3. LLM Playground",
    "roadmap.item3.body":
      "ロールスタイル生成、検索、対話計画とこの音声システムをつなぐ。"
  }
};

function applyLanguage(lang) {
  const locale = translations[lang] || translations.en;
  document.documentElement.lang = lang;
  document.title = locale.title;
  const meta = document.querySelector('meta[name="description"]');
  if (meta) meta.setAttribute("content", locale.description);
  document.querySelectorAll("[data-i18n]").forEach((node) => {
    const key = node.getAttribute("data-i18n");
    if (locale[key]) {
      node.textContent = locale[key];
    }
  });
  document.querySelectorAll(".lang-chip").forEach((button) => {
    button.classList.toggle("is-active", button.dataset.lang === lang);
  });
  localStorage.setItem("mayuri-amadeus-lang", lang);
}

const preferred = localStorage.getItem("mayuri-amadeus-lang");
const browserLang = navigator.language.startsWith("zh")
  ? "zh"
  : navigator.language.startsWith("ja")
    ? "ja"
    : "en";
const initialLang = preferred || browserLang;

document.querySelectorAll(".lang-chip").forEach((button) => {
  button.addEventListener("click", () => applyLanguage(button.dataset.lang));
});

applyLanguage(initialLang);
