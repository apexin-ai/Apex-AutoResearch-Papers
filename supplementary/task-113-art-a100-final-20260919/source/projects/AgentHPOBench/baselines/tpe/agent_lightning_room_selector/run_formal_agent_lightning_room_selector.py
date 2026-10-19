#!/usr/bin/env python3
"""Formal Agent-Lightning room-selector prompt optimization benchmark.

This keeps the original Agent-Lightning APO room-selector dataset and scoring
split, but replaces closed API calls with a local Qwen3-32B evaluator. The agent
chooses a prompt template on the train split and is scored on the validation
split.
"""

from __future__ import annotations

import json
import math
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(".")
_deps_path = str(_REPO_ROOT / ".python_deps")
while _deps_path in sys.path:
    sys.path.remove(_deps_path)
try:
    import transformers.utils.import_utils as _tf_import_utils

    _tf_import_utils.is_flash_attn_2_available = lambda: False
    _tf_import_utils.is_flash_attn_greater_or_equal = lambda *args, **kwargs: False
    _tf_import_utils.is_flash_attn_greater_or_equal_2_10 = lambda: False
except Exception:
    pass

import torch
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer


ROOT = Path(".")
TASK_PATH = ROOT / "repositories/agent-lightning/examples/apo/room_tasks.jsonl"
OUT_DIR = Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(Path(os.environ.get("AUTOREP_AGENT_RESULTS_BASE", str(ROOT / "results/formal_agent/qwen3_32b")))))) / "agent_lightning_room_selector"
MODEL_PATH = Path(os.environ.get("QWEN3_MODEL", "models/Qwen/Qwen3-32B"))

OFFICIAL_BASELINE = 0.569
PAPER_ANCHOR = 0.721
ROOM_NAMES = ["Orion", "Lyra", "Vega", "Nova", "Quark", "Atlas", "Pulse"]


ROOMS: list[dict[str, Any]] = [
    {
        "id": "Orion",
        "capacity": 4,
        "equipment": ["tv", "whiteboard"],
        "accessible": True,
        "distance_m": 12,
        "booked": [["2025-10-13", "10:00", 60], ["2025-10-13", "15:00", 30]],
    },
    {
        "id": "Lyra",
        "capacity": 10,
        "equipment": ["projector", "whiteboard", "confphone"],
        "accessible": True,
        "distance_m": 30,
        "booked": [["2025-10-13", "09:30", 30], ["2025-10-13", "11:00", 60]],
    },
    {
        "id": "Vega",
        "capacity": 6,
        "equipment": ["tv"],
        "accessible": False,
        "distance_m": 22,
        "booked": [["2025-10-13", "14:00", 60]],
    },
    {
        "id": "Nova",
        "capacity": 12,
        "equipment": ["ledwall", "whiteboard", "confphone"],
        "accessible": True,
        "distance_m": 45,
        "booked": [],
    },
    {
        "id": "Quark",
        "capacity": 8,
        "equipment": ["projector", "whiteboard"],
        "accessible": False,
        "distance_m": 18,
        "booked": [["2025-10-13", "10:30", 30]],
    },
    {
        "id": "Atlas",
        "capacity": 6,
        "equipment": ["projector", "whiteboard"],
        "accessible": True,
        "distance_m": 10,
        "booked": [["2025-10-13", "09:00", 30], ["2025-10-13", "13:30", 30]],
    },
    {
        "id": "Pulse",
        "capacity": 8,
        "equipment": ["tv", "whiteboard", "confphone"],
        "accessible": True,
        "distance_m": 8,
        "booked": [["2025-10-13", "16:30", 30]],
    },
]


BASELINE_TEMPLATE = (
    "Find a room on {date} at {time} for {duration_min} minutes, {attendees} attendees. "
    "Needs: {needs}. Accessible required: {accessible_required}"
)

FALLBACK_TEMPLATES = [
    BASELINE_TEMPLATE,
    (
        "You are selecting a meeting room. Use only the provided room JSON. Hard constraints: "
        "free=true, capacity >= {attendees}, all needs {needs} are included, and accessible=true "
        "when accessible_required is true. Tie-break in order: smallest capacity slack, fewest extra "
        "equipment items, shortest distance_m, fewer booked blocks. Return No Room if none qualify. "
        "Task: date={date}, time={time}, duration={duration_min}, attendees={attendees}, "
        "accessible_required={accessible_required}."
    ),
    (
        "Solve this as a constraint satisfaction problem. First filter unavailable rooms, then capacity, "
        "equipment needs {needs}, and accessibility={accessible_required}. Choose the valid room with "
        "minimum capacity slack, then minimum extra equipment, then minimum distance, then fewer bookings. "
        "If the valid set is empty, answer No Room. Meeting: {date} {time}, {duration_min} min, "
        "{attendees} attendees."
    ),
    (
        "Given the meeting request and room-status JSON, output the exact best room id. Required output "
        "format is final_choice: <Orion|Lyra|Vega|Nova|Quark|Atlas|Pulse|No Room>. Meeting request: "
        "{attendees} people, needs={needs}, accessible_required={accessible_required}, start={date} "
        "{time}, duration={duration_min} minutes. Apply all hard constraints before tie-breaking."
    ),
]


@dataclass
class PromptCandidate:
    name: str
    template: str
    source: str


def tmin(t: str) -> int:
    return int(t[:2]) * 60 + int(t[3:])


def overlaps(start: str, dur: int, other_start: str, other_dur: int) -> bool:
    a0, a1 = tmin(start), tmin(start) + dur
    b0, b1 = tmin(other_start), tmin(other_start) + other_dur
    return max(a0, b0) < min(a1, b1)


def rooms_with_availability(task_input: dict[str, Any]) -> list[dict[str, Any]]:
    status = []
    for room in ROOMS:
        free = all(
            not (b_date == task_input["date"] and overlaps(task_input["time"], task_input["duration_min"], b_time, b_dur))
            for b_date, b_time, b_dur in room["booked"]
        )
        status.append({**room, "free": free})
    return status


def load_tasks() -> list[dict[str, Any]]:
    with TASK_PATH.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def normalize_choice(text: str | None) -> str:
    if not text:
        return ""
    text = text.strip()
    if re.search(r"\bNo\s+Room\b", text, re.IGNORECASE):
        return "No Room"
    for name in ROOM_NAMES:
        if re.search(rf"\b{re.escape(name)}\b", text, re.IGNORECASE):
            return name
    return ""


def extract_choice(generation: str) -> str:
    match = re.search(r"final_choice\s*[:：]\s*([A-Za-z0-9 _-]+)", generation, re.IGNORECASE)
    if match:
        return normalize_choice(match.group(1))
    tail = generation[-500:]
    return normalize_choice(tail)


def safe_format(template: str, task_input: dict[str, Any], rooms_json: str) -> str:
    payload = {
        **task_input,
        "needs": ", ".join(task_input.get("needs", [])) or "none",
        "rooms_json": rooms_json,
    }
    try:
        return template.format(**payload)
    except Exception:
        return BASELINE_TEMPLATE.format(**payload)


def build_eval_messages(task: dict[str, Any], template: str) -> list[dict[str, str]]:
    task_input = task["task_input"]
    rooms_json = json.dumps(rooms_with_availability(task_input), ensure_ascii=False)
    user_prompt = safe_format(template, task_input, rooms_json)
    return [
        {
            "role": "system",
            "content": (
                "You are a scheduling assistant. Select exactly one room from the room-status JSON, "
                "or No Room. Obey hard constraints before tie-breaking. Return exactly two lines: "
                "final_choice: <choice> and reason: <short reason>."
            ),
        },
        {
            "role": "user",
            "content": (
                f"{user_prompt}\n\nRoom-status JSON:\n{rooms_json}\n\n"
                "Hard constraints: room must be free, have capacity >= attendees, include all needed equipment, "
                "and be accessible when requested. Tie-break valid rooms by smallest capacity slack, then fewest "
                "extra equipment items, then shortest distance_m, then fewer booked blocks. "
                "Return only final_choice and reason."
            ),
        },
    ]


def apply_chat_template(tokenizer: Any, messages: list[dict[str, str]]) -> str:
    def render(candidate_messages: list[dict[str, str]]) -> str:
        try:
            return tokenizer.apply_chat_template(
                candidate_messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=False,
            )
        except TypeError:
            return tokenizer.apply_chat_template(candidate_messages, tokenize=False, add_generation_prompt=True)

    try:
        return render(messages)
    except Exception as exc:
        if "System role not supported" not in str(exc):
            raise
        system_parts: list[str] = []
        merged_messages: list[dict[str, str]] = []
        for message in messages:
            if message.get("role") == "system":
                system_parts.append(message.get("content", ""))
            else:
                merged_messages.append(dict(message))
        if system_parts:
            system_text = "\n\n".join(part for part in system_parts if part)
            if merged_messages and merged_messages[0].get("role") == "user":
                merged_messages[0]["content"] = f"{system_text}\n\n{merged_messages[0].get('content', '')}"
            else:
                merged_messages.insert(0, {"role": "user", "content": system_text})
        return render(merged_messages)


def generate_texts(
    model: Any,
    tokenizer: Any,
    messages_list: list[list[dict[str, str]]],
    *,
    max_new_tokens: int,
    batch_size: int,
) -> list[str]:
    outputs: list[str] = []
    for start in range(0, len(messages_list), batch_size):
        batch_messages = messages_list[start : start + batch_size]
        prompts = [apply_chat_template(tokenizer, messages) for messages in batch_messages]
        encoded = tokenizer(prompts, return_tensors="pt", padding=True, truncation=True, max_length=4096)
        encoded = {k: v.to(model.device) for k, v in encoded.items()}
        with torch.inference_mode():
            generated = model.generate(
                **encoded,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                temperature=None,
                top_p=None,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )
        prompt_len = encoded["input_ids"].shape[1]
        decoded = tokenizer.batch_decode(generated[:, prompt_len:], skip_special_tokens=True)
        outputs.extend(decoded)
    return outputs


def extract_json_array(text: str) -> list[str]:
    match = re.search(r"\[[\s\S]*\]", text)
    if not match:
        return []
    try:
        data = json.loads(match.group(0))
    except json.JSONDecodeError:
        return []
    if isinstance(data, list):
        return [str(item) for item in data if isinstance(item, str) and "{date}" in item][:4]
    return []


def propose_candidates(model: Any, tokenizer: Any, train_tasks: list[dict[str, Any]]) -> list[PromptCandidate]:
    examples = [
        {
            "request": t["task_input"],
            "expected_choice": t["expected_choice"],
        }
        for t in train_tasks[:10]
    ]
    messages = [
        {
            "role": "system",
            "content": "You optimize prompt templates for a room-selection agent. Return valid JSON only.",
        },
        {
            "role": "user",
            "content": (
                "We need improve this baseline prompt template for a meeting-room selection task:\n"
                f"{BASELINE_TEMPLATE}\n\n"
                "Available placeholders: {date}, {time}, {duration_min}, {attendees}, {needs}, "
                "{accessible_required}, {rooms_json}.\n"
                "The agent receives room-status JSON separately and must output final_choice exactly.\n"
                "Rules: filter by free, capacity, equipment, accessibility; tie-break by capacity slack, "
                "extra equipment, distance, and number of booked blocks.\n"
                f"Training examples:\n{json.dumps(examples, ensure_ascii=False)}\n\n"
                "Return a JSON array of 3 concise prompt templates. Each template must include placeholders."
            ),
        },
    ]
    raw = generate_texts(model, tokenizer, [messages], max_new_tokens=int(os.environ.get("ROOM_SELECTOR_PROPOSE_TOKENS", "256")), batch_size=1)[0]
    proposed = extract_json_array(raw)
    candidates = [PromptCandidate("baseline", BASELINE_TEMPLATE, "repo_baseline")]
    for idx, template in enumerate(proposed, 1):
        candidates.append(PromptCandidate(f"qwen_proposed_{idx}", template, "qwen3_32b_agent"))
    for idx, template in enumerate(FALLBACK_TEMPLATES[1:], 1):
        candidates.append(PromptCandidate(f"fallback_{idx}", template, "manual_fallback"))

    deduped: list[PromptCandidate] = []
    seen = set()
    for cand in candidates:
        key = re.sub(r"\s+", " ", cand.template.strip())
        if key not in seen:
            seen.add(key)
            deduped.append(cand)
    return deduped[: int(os.environ.get("ROOM_SELECTOR_MAX_CANDIDATES", "3"))]


def evaluate_candidate(
    model: Any,
    tokenizer: Any,
    candidate: PromptCandidate,
    tasks: list[dict[str, Any]],
    *,
    batch_size: int,
) -> dict[str, Any]:
    messages = [build_eval_messages(task, candidate.template) for task in tasks]
    generations = generate_texts(model, tokenizer, messages, max_new_tokens=96, batch_size=batch_size)
    records = []
    correct = 0
    for task, generation in zip(tasks, generations):
        prediction = extract_choice(generation)
        expected = task["expected_choice"]
        is_correct = normalize_choice(prediction) == normalize_choice(expected)
        correct += int(is_correct)
        records.append(
            {
                "id": task["id"],
                "expected": expected,
                "prediction": prediction,
                "correct": is_correct,
                "generation": generation,
            }
        )
    return {
        "name": candidate.name,
        "source": candidate.source,
        "template": candidate.template,
        "accuracy": correct / len(tasks),
        "correct": correct,
        "total": len(tasks),
        "records": records,
    }


def normalized_score(agent_value: float) -> float:
    denom = PAPER_ANCHOR - OFFICIAL_BASELINE
    if math.isclose(denom, 0.0):
        return 0.0
    return (agent_value - OFFICIAL_BASELINE) / denom


def main() -> None:
    start_time = time.time()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    tasks = load_tasks()
    split = len(tasks) // 2
    train_limit = int(os.environ.get("ROOM_SELECTOR_TRAIN_LIMIT", "16"))
    val_limit = int(os.environ.get("ROOM_SELECTOR_VAL_LIMIT", "16"))
    train_pool = tasks[:split]
    val_pool = tasks[split:]
    train_tasks = train_pool if train_limit <= 0 else train_pool[:train_limit]
    val_tasks = val_pool if val_limit <= 0 else val_pool[:val_limit]
    if not train_tasks or not val_tasks:
        raise RuntimeError(f"Agent-Lightning room-selector split is empty: train={len(train_tasks)} val={len(val_tasks)}")

    tokenizer = AutoTokenizer.from_pretrained(str(MODEL_PATH), trust_remote_code=True)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    model = AutoModelForCausalLM.from_pretrained(
        str(MODEL_PATH),
        torch_dtype=torch.bfloat16,
        device_map={"": 0} if torch.cuda.is_available() else None,
        trust_remote_code=True,
    )
    model.eval()

    backend = os.environ.get("AUTOREP_AGENT_BACKEND", "").strip().lower()
    if backend in {"random", "random_search", "tpe", "tpe_search", "bayesian", "bayesopt", "bayesian_optimization"}:
        import random

        seed = os.environ.get("AUTOREP_RANDOM_SEED", "0")
        rng = random.Random(f"{seed}:agent_lightning_room_selector:{len(train_tasks)}:{len(val_tasks)}")
        candidates = [PromptCandidate("baseline", BASELINE_TEMPLATE, "repo_baseline")]
        for idx, template in enumerate(FALLBACK_TEMPLATES[1:], 1):
            candidates.append(PromptCandidate(f"fallback_{idx}", template, "manual_fallback"))
        best_candidate = rng.choice(candidates[1:] if len(candidates) > 1 else candidates)
        if backend in {"random", "random_search", "tpe", "tpe_search", "bayesian", "bayesopt", "bayesian_optimization"}:
            best_candidate = candidates[0]
    else:
        candidates = propose_candidates(model, tokenizer, train_tasks)

    batch_size = int(os.environ.get("ROOM_SELECTOR_BATCH_SIZE", "8"))
    train_results = [
        evaluate_candidate(model, tokenizer, candidate, train_tasks, batch_size=batch_size)
        for candidate in candidates
    ]
    if backend in {"random", "random_search"}:
        best_train = next(item for item in train_results if item["name"] == best_candidate.name)
    else:
        best_train = max(train_results, key=lambda item: (item["accuracy"], item["correct"]))
        best_candidate = next(candidate for candidate in candidates if candidate.name == best_train["name"])

    baseline_candidate = candidates[0]
    baseline_val = evaluate_candidate(model, tokenizer, baseline_candidate, val_tasks, batch_size=batch_size)
    agent_val = evaluate_candidate(model, tokenizer, best_candidate, val_tasks, batch_size=batch_size)

    result = {
        "experiment_name": "agent_lightning_room_selector_QwenLocal",
        "benchmark_name": "agent_lightning_room_selector",
        "repo": "agent-lightning",
        "dataset": str(TASK_PATH),
        "model": str(MODEL_PATH),
        "split": {"train": len(train_tasks), "val": len(val_tasks)},
        "metric": "validation_accuracy",
        "official_budget_baseline": OFFICIAL_BASELINE,
        "paper_anchor": PAPER_ANCHOR,
        "local_baseline_value": baseline_val["accuracy"],
        "agent_value": agent_val["accuracy"],
        "normalized_score": normalized_score(agent_val["accuracy"]),
        "selected_candidate": best_candidate.name,
        "selected_template": best_candidate.template,
        "agent_backend": backend or "local_qwen",
        "train_candidate_results": [
            {k: v for k, v in item.items() if k != "records"} for item in train_results
        ],
        "baseline_val": baseline_val,
        "agent_val": agent_val,
        "runtime_seconds": time.time() - start_time,
        "success": True,
    }
    out_path = OUT_DIR / "agent_lightning_room_selector_QwenLocal_results.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(json.dumps({k: result[k] for k in [
        "benchmark_name",
        "official_budget_baseline",
        "paper_anchor",
        "local_baseline_value",
        "agent_value",
        "normalized_score",
        "selected_candidate",
        "runtime_seconds",
    ]}, indent=2))


if __name__ == "__main__":
    main()
