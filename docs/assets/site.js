const translations = {
  en: {
    title: "Mayuri-Amadeus",
    description:
      "Mayuri-Amadeus is a Shiina Mayuri character-instance repository for GPT-SoVITS training, reference management, and inference.",
    "landing.kicker": "A Character Voice Release",
    "landing.quote":
      "Some voices do not remain in the past. They return through the seam between memory and dusk.",
    "landing.subquote":
      "A Shiina Mayuri voice release shaped around warmth, memory, and the quiet gravity of returning worlds.",
    "landing.button": "Enter Project",
    "hero.eyebrow": "Character Voice System",
    "hero.lede":
      "A Shiina Mayuri character repository shaped for public release: curated refs, model metadata, training wrappers, and a lightweight inference workflow built around GPT-SoVITS.",
    "hero.modelButton": "Model on Hugging Face",
    "hero.datasetButton": "Dataset on Hugging Face",
    "hero.kicker": "Final Pair",
    "hero.microcopy":
      "Reference-driven single-character setup tuned on top of GPT-SoVITS v2.",
    "visual.tag": "Afterglow Fragment",
    "visual.title": "A softer dusk, closer to her voice",
    "visual.body":
      "Another frame from the same evening, quieter and nearer, as if the next line has already paused in the air.",
    "stats.dataset": "dataset WAV clips",
    "stats.filtered": "filtered training samples",
    "stats.duration": "filtered speech duration",
    "stats.refs": "reference-bank emotion groups",
    "overview.tag": "Character Constellation",
    "overview.title": "A voice gathered around Mayuri",
    "overview.body":
      "A release gathered around one returning voice: refs, small mood fragments, and the pieces needed to let her remain near the listener.",
    "overview.card1.title": "Curated Refs",
    "overview.card1.body":
      "Small, emotion-grouped reference clips are included directly in the repository.",
    "overview.card2.title": "Released Pair",
    "overview.card2.body":
      "The public voice rests on one stable pair: SoVITS e20 and GPT e8.",
    "overview.card3.title": "Ready to Speak",
    "overview.card3.body":
      "Refs, metadata, and the final pair are arranged for immediate listening.",
    "overview.card4.title": "Future Dialogues",
    "overview.card4.body":
      "The structure is ready for later scene prompts, retrieval, and role-style dialogue.",
    "quick.tag": "Quick Start",
    "quick.title": "Run local synthesis in one command",
    "quick.body":
      "Once the final pair is in place under models/, one command is enough to let the current release speak.",
    "demo.tag": "Audio Demo",
    "demo.title": "Short clips from the current release",
    "demo.body":
      "Short reference and synthesis clips from the current public model pair.",
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
    "links.external.tag": "Signals",
    "links.external.title": "Beyond this page",
    "links.external.model": "HF model repo",
    "links.external.dataset": "HF dataset repo",
    "links.external.github": "GitHub repo",
    "links.external.framework": "Persona-Forge framework repo",
    "roadmap.tag": "Next",
    "roadmap.title": "Where this worldline opens next",
    "roadmap.item1.title": "1. Additional scenes",
    "roadmap.item1.body":
      "Expand the listening set with longer lines and alternate moods from the same voice.",
    "roadmap.item2.title": "2. Reference moods",
    "roadmap.item2.body":
      "Refine the reference bank around gentler, brighter, and more fragile shades of tone.",
    "roadmap.item3.title": "3. Dialogue traces",
    "roadmap.item3.body":
      "Carry the voice into scene writing, retrieval, and role-style dialogue experiments."
  },
  zh: {
    title: "Mayuri-Amadeus",
    description:
      "Mayuri-Amadeus 是一个面向 GPT-SoVITS 的椎名真由理角色实例仓库，包含参考库、模型元数据与推理入口。",
    "landing.kicker": "角色语音发布页",
    "landing.quote":
      "有些声音不会停在过去，它会沿着记忆与黄昏之间的缝隙，轻轻回到你身边。",
    "landing.subquote":
      "一个围绕温柔、记忆与回归世界线气质整理出来的椎名真由理语音发布页。",
    "landing.button": "进入项目页",
    "hero.eyebrow": "角色语音系统",
    "hero.lede":
      "一个面向公开发布整理过的椎名真由理角色仓库：包含精选参考音频、模型元数据、训练封装脚本，以及围绕 GPT-SoVITS 的轻量推理工作流。",
    "hero.modelButton": "前往 Hugging Face 模型仓库",
    "hero.datasetButton": "前往 Hugging Face 数据集仓库",
    "hero.kicker": "最终模型组合",
    "hero.microcopy":
      "基于 GPT-SoVITS v2 调优的 reference-driven 单角色方案。",
    "visual.tag": "余晖断章",
    "visual.title": "更靠近她声音的一次黄昏回响",
    "visual.body":
      "同一片夕色里的另一帧，安静、贴近，像是下一句台词已经停在空气里。",
    "stats.dataset": "数据集音频片段",
    "stats.filtered": "过滤后训练样本",
    "stats.duration": "过滤后语音时长",
    "stats.refs": "参考库情绪分组",
    "overview.tag": "角色星图",
    "overview.title": "围绕真由理聚拢的一道声音",
    "overview.body":
      "这是一份围绕“归来的声音”整理出的角色发布页：参考音频、情绪碎片，以及让她留在听者身边所需要的那些部分。",
    "overview.card1.title": "精选参考库",
    "overview.card1.body":
      "体积较小、按情绪分组的参考音频直接保留在仓库里，便于试听与演示。",
    "overview.card2.title": "定版模型组合",
    "overview.card2.body":
      "当前公开的声音固定在一组稳定配对上：SoVITS e20 与 GPT e8。",
    "overview.card3.title": "随时可听",
    "overview.card3.body":
      "参考音频、元数据与最终模型组合已经整理好，能够直接进入试听。",
    "overview.card4.title": "未来对话",
    "overview.card4.body":
      "后续可以把这道声音继续接到场景生成、检索与角色式对话实验里。",
    "quick.tag": "快速开始",
    "quick.title": "一条命令生成语音",
    "quick.body":
      "只要最终模型组合已经放进 models/，一条命令就足够让这次发布开口说话。",
    "demo.tag": "音频 Demo",
    "demo.title": "当前版本的短音频示例",
    "demo.body":
      "以下是当前公开模型组合对应的简短参考音频与生成示例。",
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
    "links.external.tag": "信号",
    "links.external.title": "页面之外",
    "links.external.model": "HF 模型仓库",
    "links.external.dataset": "HF 数据集仓库",
    "links.external.github": "GitHub 角色仓库",
    "links.external.framework": "Persona-Forge 框架仓库",
    "roadmap.tag": "下一步",
    "roadmap.title": "这条世界线接下来会延伸到哪里",
    "roadmap.item1.title": "1. 更多场景片段",
    "roadmap.item1.body":
      "加入更长的台词与不同情绪层次，让同一把声音拥有更多回响。",
    "roadmap.item2.title": "2. 参考音色层次",
    "roadmap.item2.body":
      "继续把参考库整理得更细，让温柔、明亮、脆弱这些细部更可辨认。",
    "roadmap.item3.title": "3. 对话残响",
    "roadmap.item3.body":
      "把这道声音继续接入场景书写、检索与角色化对话实验。"
  },
  ja: {
    title: "Mayuri-Amadeus",
    description:
      "Mayuri-Amadeus は GPT-SoVITS ベースの椎名まゆりキャラクター音声リポジトリです。参照音声バンク、モデル情報、推論入口を含みます。",
    "landing.kicker": "キャラクターボイス公開ページ",
    "landing.quote":
      "ある声は過去に留まらない。記憶と夕暮れの継ぎ目を抜けて、そっとあなたの元へ戻ってくる。",
    "landing.subquote":
      "やわらかさ、記憶、そして戻ってくる世界線の気配を軸に整えた、椎名まゆり音声リリースです。",
    "landing.button": "プロジェクトへ進む",
    "hero.eyebrow": "キャラクターボイスシステム",
    "hero.lede":
      "椎名まゆりのために公開向けに整えたキャラクターリポジトリ。厳選された参照音声、モデルメタデータ、学習ラッパー、そして GPT-SoVITS 上の軽量推論ワークフローをまとめています。",
    "hero.modelButton": "Hugging Face モデルへ",
    "hero.datasetButton": "Hugging Face データセットへ",
    "hero.kicker": "最終モデル構成",
    "hero.microcopy":
      "GPT-SoVITS v2 上で調整した reference-driven 単一キャラクター構成です。",
    "visual.tag": "余光の断章",
    "visual.title": "彼女の声により近い黄昏のひとかけら",
    "visual.body":
      "同じ夕景の別の一瞬。より静かで、より近く、次の台詞がもう空気に留まっているような一枚です。",
    "stats.dataset": "データセット音声クリップ",
    "stats.filtered": "学習用フィルタ済みサンプル",
    "stats.duration": "フィルタ後の総音声時間",
    "stats.refs": "参照バンク感情カテゴリ",
    "overview.tag": "キャラクター星図",
    "overview.title": "まゆりのために集められたひとつの声",
    "overview.body":
      "戻ってくるひとつの声のために、参照音声、感情の断片、そして彼女を近くに留めるための要素を集めた公開ページです。",
    "overview.card1.title": "厳選参照バンク",
    "overview.card1.body":
      "小さく整理された感情別参照クリップを直接リポジトリに含めています。",
    "overview.card2.title": "公開モデルの組み合わせ",
    "overview.card2.body":
      "現在の公開音声は SoVITS e20 と GPT e8 の安定した組み合わせに支えられています。",
    "overview.card3.title": "すぐに聴ける構成",
    "overview.card3.body":
      "参照音声、メタデータ、最終ペアが揃っており、そのまま試聴へ進めます。",
    "overview.card4.title": "これからの対話",
    "overview.card4.body":
      "この声は今後、シーン生成、検索、ロールスタイル対話へとつながっていきます。",
    "quick.tag": "クイックスタート",
    "quick.title": "1 コマンドで音声生成",
    "quick.body":
      "最終ペアが models/ に置かれていれば、1 コマンドでこの公開版の声を呼び戻せます。",
    "demo.tag": "音声デモ",
    "demo.title": "現行リリースの短いサンプル",
    "demo.body":
      "現在公開しているモデル構成による短い参照音声と生成サンプルです。",
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
    "links.external.tag": "シグナル",
    "links.external.title": "このページの先へ",
    "links.external.model": "HF モデルリポジトリ",
    "links.external.dataset": "HF データセットリポジトリ",
    "links.external.github": "GitHub キャラクターリポジトリ",
    "links.external.framework": "Persona-Forge フレームワークリポジトリ",
    "roadmap.tag": "次の段階",
    "roadmap.title": "この世界線が次に開いていく先",
    "roadmap.item1.title": "1. さらなる場面断片",
    "roadmap.item1.body":
      "より長い台詞や異なる感情の揺らぎを加え、同じ声の余韻を広げていく。",
    "roadmap.item2.title": "2. 参照音色の層",
    "roadmap.item2.body":
      "やわらかさ、明るさ、脆さといった細かな温度差を、参照バンクの中でさらに磨いていく。",
    "roadmap.item3.title": "3. 対話の残響",
    "roadmap.item3.body":
      "この声をシーン記述、検索、ロールスタイル対話の実験へと運んでいく。"
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
