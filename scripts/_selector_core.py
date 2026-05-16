from __future__ import annotations

import csv
import http.client
import json
import os
import re
import ssl
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path


RETRYABLE_API_ERRORS = (
    urllib.error.URLError,
    urllib.error.HTTPError,
    TimeoutError,
    ConnectionResetError,
    ConnectionAbortedError,
    http.client.RemoteDisconnected,
    ssl.SSLError,
)


@dataclass
class ReferenceItem:
    emotion: str
    rank: int
    sample_id: str
    wav_path: str
    text_path: str
    duration_sec: float
    reference_score: int
    intensity: int
    text: str
    reason: str


@dataclass
class StylePlan:
    emotion: str
    intensity: int
    pace: str
    confidence: float
    reason: str
    alternate_emotions: list[str]
    backend: str


def resolve_api_key(explicit_key: str, primary_env: str) -> str:
    if explicit_key:
        return explicit_key
    for env_name in (primary_env, "SELECTOR_API_KEY", "EMOTION_API_KEY", "OPENAI_API_KEY", "DASHSCOPE_API_KEY"):
        value = os.environ.get(env_name, "").strip()
        if value:
            return value
    return ""


def load_reference_bank(index_path: Path) -> list[ReferenceItem]:
    items: list[ReferenceItem] = []
    with index_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            items.append(
                ReferenceItem(
                    emotion=row["emotion"].strip(),
                    rank=int(row["rank"]),
                    sample_id=row["sample_id"].strip(),
                    wav_path=row["wav_path"].strip(),
                    text_path=row["text_path"].strip(),
                    duration_sec=float(row["duration_sec"]),
                    reference_score=int(row["reference_score"]),
                    intensity=int(row["intensity"]),
                    text=row["text"].strip(),
                    reason=row.get("reason", "").strip(),
                )
            )
    if not items:
        raise ValueError(f"No reference items found in {index_path}")
    return items


def extract_json_payload(content: str) -> dict:
    text = content.strip()
    if text.startswith("```"):
        match = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
        if match:
            text = match.group(1).strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError(f"Could not locate JSON object in model output: {content}")
    return json.loads(text[start : end + 1])


def post_chat_completion(api_base: str, api_key: str, model: str, messages: list[dict[str, str]]) -> str:
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.1,
        "top_p": 0.9,
    }
    url = api_base.rstrip("/") + "/chat/completions"
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        body = response.read().decode("utf-8")
    data = json.loads(body)
    return data["choices"][0]["message"]["content"]


def build_api_messages(target_text: str, target_language: str, labels: list[str]) -> list[dict[str, str]]:
    instructions = f"""
You are selecting the speaking style for a character-voice reference bank.
Return strict JSON only:
{{
  "emotion": "one of {labels}",
  "intensity": 1,
  "pace": "slow|medium|fast",
  "confidence": 0.0,
  "reason": "short explanation",
  "alternate_emotions": ["optional secondary labels"]
}}
"""
    user_payload = {
        "target_language": target_language,
        "target_text": target_text,
        "available_emotions": labels,
    }
    return [
        {"role": "system", "content": "You are a careful prosody planner for character voice synthesis."},
        {"role": "user", "content": instructions + "\n\n" + json.dumps(user_payload, ensure_ascii=False, indent=2)},
    ]


def clamp_intensity(raw: object) -> int:
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return 3
    return max(1, min(5, value))


def clamp_confidence(raw: object) -> float:
    try:
        value = float(raw)
    except (TypeError, ValueError):
        return 0.5
    return max(0.0, min(1.0, value))


def normalize_pace(raw: object) -> str:
    value = str(raw or "").strip().lower()
    if value in {"slow", "medium", "fast"}:
        return value
    return "medium"


def normalize_emotion(raw: object, labels: list[str]) -> str:
    value = str(raw or "").strip().lower()
    if value in labels:
        return value
    return "neutral" if "neutral" in labels else labels[0]


def parse_plan(payload: dict, labels: list[str], backend: str) -> StylePlan:
    primary = normalize_emotion(payload.get("emotion"), labels)
    alternates = []
    for item in payload.get("alternate_emotions", []):
        normalized = normalize_emotion(item, labels)
        if normalized != primary:
            alternates.append(normalized)
    return StylePlan(
        emotion=primary,
        intensity=clamp_intensity(payload.get("intensity")),
        pace=normalize_pace(payload.get("pace")),
        confidence=clamp_confidence(payload.get("confidence")),
        reason=str(payload.get("reason", "")).strip() or "No reason provided.",
        alternate_emotions=list(dict.fromkeys(alternates)),
        backend=backend,
    )


def heuristic_emotion(text: str, labels: list[str]) -> tuple[str, int, str, list[str]]:
    lowered = text.strip().lower()
    patterns = [
        ("sad", [r"悲しい", r"行かないで", r"やだ", r"cry", r"难过", r"别走"], 4, "slow", ["gentle"]),
        ("gentle", [r"大好き", r"元気出して", r"お帰り", r"どうした", r"亲爱的", r"好久不见"], 3, "slow", ["neutral"]),
        ("excited", [r"!+", r"わあ", r"すごい", r"太棒", r"哇"], 4, "fast", ["happy"]),
        ("happy", [r"幸せ", r"かわいい", r"えへへ", r"开心", r"可爱"], 4, "medium", ["gentle"]),
        ("teasing", [r"へへ", r"胡散臭い", r"だめだよ", r"逗", r"坏"], 3, "medium", ["neutral"]),
        ("worried", [r"大丈夫", r"心配", r"どうする", r"担心"], 3, "medium", ["gentle"]),
        ("serious", [r"第三次世界大戦", r"しないで", r"重要", r"必须"], 4, "medium", ["neutral"]),
        ("embarrassed", [r"恥ずかしい", r"あうう", r"害羞"], 3, "medium", ["gentle"]),
    ]
    for emotion, regexes, intensity, pace, alternates in patterns:
        if emotion not in labels:
            continue
        if any(re.search(regex, lowered, re.I) for regex in regexes):
            return emotion, intensity, pace, alternates
    if "?" in text or "？" in text:
        fallback = "gentle" if "gentle" in labels else labels[0]
        return fallback, 2, "medium", ["neutral"] if "neutral" in labels else []
    fallback = "neutral" if "neutral" in labels else labels[0]
    return fallback, 2, "medium", []


def plan_with_heuristic(target_text: str, labels: list[str]) -> StylePlan:
    emotion, intensity, pace, alternates = heuristic_emotion(target_text, labels)
    return StylePlan(
        emotion=emotion,
        intensity=intensity,
        pace=pace,
        confidence=0.42,
        reason="Selected by built-in heuristic rules.",
        alternate_emotions=alternates,
        backend="heuristic",
    )


def plan_with_api(
    target_text: str,
    target_language: str,
    labels: list[str],
    api_base: str,
    api_key: str,
    model: str,
    max_retries: int,
    sleep: float,
) -> StylePlan:
    messages = build_api_messages(target_text, target_language, labels)
    last_error: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            content = post_chat_completion(api_base, api_key, model, messages)
            payload = extract_json_payload(content)
            return parse_plan(payload, labels, "api")
        except RETRYABLE_API_ERRORS as exc:
            last_error = exc
            if attempt == max_retries:
                break
            time.sleep(sleep * attempt)
    assert last_error is not None
    raise last_error


def preferred_duration(pace: str) -> float:
    if pace == "slow":
        return 5.6
    if pace == "fast":
        return 3.9
    return 4.7


def score_reference(item: ReferenceItem, plan: StylePlan) -> float:
    score = 0.0
    if item.emotion == plan.emotion:
        score += 50.0
    elif item.emotion in plan.alternate_emotions:
        score += 30.0
    elif item.emotion == "neutral":
        score += 10.0
    score += max(0.0, 20.0 - abs(item.intensity - plan.intensity) * 5.0)
    score += item.reference_score * 5.0
    score += max(0.0, 8.0 - (item.rank - 1) * 1.5)
    score += max(0.0, 8.0 - abs(item.duration_sec - preferred_duration(plan.pace)) * 2.2)
    return score


def select_references(items: list[ReferenceItem], plan: StylePlan, top_k: int, asset_root: Path | None) -> list[dict]:
    ranked = []
    for item in items:
        record = {
            "sample_id": item.sample_id,
            "emotion": item.emotion,
            "rank": item.rank,
            "intensity": item.intensity,
            "reference_score": item.reference_score,
            "duration_sec": item.duration_sec,
            "wav_path": item.wav_path,
            "text_path": item.text_path,
            "text": item.text,
            "reason": item.reason,
            "selector_score": round(score_reference(item, plan), 3),
        }
        if asset_root is not None:
            record["wav_abspath"] = str((asset_root / item.wav_path).resolve())
            record["text_abspath"] = str((asset_root / item.text_path).resolve())
        ranked.append(record)
    ranked.sort(key=lambda record: (-record["selector_score"], record["rank"], record["sample_id"]))
    return ranked[: max(1, top_k)]


def select_reference_from_text(
    *,
    refs_index: Path,
    asset_root: Path | None,
    target_text: str,
    target_language: str,
    backend: str,
    api_base: str = "",
    api_key: str = "",
    api_key_env: str = "SELECTOR_API_KEY",
    model: str = "",
    local_model: str = "",
    top_k: int = 5,
    max_retries: int = 3,
    sleep: float = 1.5,
) -> dict:
    items = load_reference_bank(refs_index)
    labels = sorted({item.emotion for item in items})

    if backend == "api":
        resolved_key = resolve_api_key(api_key, api_key_env)
        if not api_base:
            raise ValueError("API backend selected but api_base is empty.")
        if not model:
            raise ValueError("API backend selected but model is empty.")
        if not resolved_key:
            raise ValueError(f"API backend selected but no API key found in {api_key_env}.")
        plan = plan_with_api(target_text, target_language, labels, api_base, resolved_key, model, max_retries, sleep)
    elif backend == "local":
        raise NotImplementedError(
            "Local selector backend is reserved but not implemented yet. Use backend='api' or backend='heuristic'."
        )
    else:
        plan = plan_with_heuristic(target_text, labels)

    top_candidates = select_references(items, plan, top_k, asset_root)
    return {
        "target_text": target_text,
        "target_language": target_language,
        "plan": asdict(plan),
        "selection": top_candidates[0],
        "alternatives": top_candidates[1:],
        "labels": labels,
        "local_model": local_model,
    }
