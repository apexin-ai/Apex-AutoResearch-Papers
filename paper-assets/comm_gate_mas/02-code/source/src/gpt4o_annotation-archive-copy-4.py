"""GPT-4o annotation of inter-agent messages.

Two modes:
  1. csv (default): Reads annotation_sheet_full.csv, annotates with GPT-4o,
     outputs CSV + Cohen's κ statistics.
  2. oracle-precompute: Reads traces JSONL from e2e experiments, classifies
     each message as ack/non-ack, outputs oracle cache JSON compatible with
     pruning_validation.py's _oracle_cache format.

Usage:
  # CSV annotation mode (existing)
  python src/gpt4o_annotation.py --api-key $KEY

  # Oracle precompute mode
  python src/gpt4o_annotation.py oracle-precompute \\
      --input outputs/e2e_llama_n300_clean/traces/traces.jsonl \\
      --output outputs/oracle_labels/llama_n300_oracle.json \\
      [--checkpoint outputs/oracle_labels/llama_n300_oracle.json.ckpt] \\
      [--dry-run]
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import logging
import os
import sys
import time

from openai import OpenAI

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a communication analyst for multi-agent systems. Your task is to classify the function of a message in a multi-agent math problem-solving conversation.

## Function Types

1. **information_provision**: Provides facts, data, intermediate calculations, or partial results that advance the solution. Includes reporting computed values, stating known quantities, or presenting new numerical results.

2. **reasoning_guidance**: Provides reasoning direction, problem decomposition, step-by-step plans, or conceptual frameworks. Includes breaking the problem into sub-problems, suggesting solution strategies, or outlining multi-step approaches.

3. **verification**: Checks, corrects, or confirms the correctness of previous work. Includes identifying errors, validating results, pointing out mistakes, or confirming a step is correct with a specific reason.

4. **coordination**: Manages the flow of the conversation, assigns tasks, requests clarification, or controls turn-taking. Includes delegating sub-tasks, asking for more information, or directing the problem-solving process.

5. **acknowledgment**: Simple confirmation, repetition, or agreement that adds no new information or reasoning. Includes restating what was already said without extending it.

## Priority Rules (when a message fits multiple categories)

Priority: coordination > verification > reasoning_guidance > information_provision > acknowledgment

- If a message both provides new results AND checks previous work, classify as **verification**.
- If a message provides a reasoning plan AND new results, classify as **reasoning_guidance**.
- If a message confirms correctness WITH a substantive explanation of why, classify as **verification** (not acknowledgment).
- If a message simply agrees or restates without adding new information, classify as **acknowledgment**.

## Output Format

Respond with ONLY a JSON object (no markdown, no extra text):
{"type": "<function_type>", "confidence": <0.0-1.0>, "reasoning": "<brief explanation>"}
"""

VALID_TYPES = {"information_provision", "reasoning_guidance", "verification", "coordination", "acknowledgment"}


def annotate_single(client: OpenAI, model: str, prev_text: str, msg_text: str,
                    sender: str, task_id: str, token_tracker: dict | None = None) -> dict:
    user_prompt = f"""## Context

Task: {task_id}

### Previous message (for context):
{prev_text[:2000] if prev_text else '[conversation start]'}

### Current message to classify (sent by {sender}):
{msg_text[:3000]}

Classify the function of the current message."""

    for attempt in range(6):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0,
                max_tokens=256,
            )
            if token_tracker is not None and resp.usage:
                token_tracker["prompt_tokens"] += resp.usage.prompt_tokens
                token_tracker["completion_tokens"] += resp.usage.completion_tokens
                token_tracker["api_calls"] += 1
            raw = resp.choices[0].message.content or "{}"
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
            result = json.loads(raw)
            if result.get("type") not in VALID_TYPES:
                logger.warning("Invalid type %r for %s, retrying", result.get("type"), task_id)
                continue
            return result
        except json.JSONDecodeError:
            logger.warning("Attempt %d JSON parse failed for %s", attempt + 1, task_id)
            time.sleep(2)
        except Exception as e:
            err_str = str(e).lower()
            if "rate" in err_str or "429" in err_str or "quota" in err_str:
                backoff = 30 * (2 ** min(attempt, 3))
                logger.warning("Rate limit hit (attempt %d) for %s, backing off %ds", attempt + 1, task_id, backoff)
                time.sleep(backoff)
            else:
                logger.warning("Attempt %d failed for %s: %s", attempt + 1, task_id, e)
                if attempt < 5:
                    time.sleep(2 ** attempt)
    return {"type": "unknown", "confidence": 0.0, "reasoning": "all attempts failed"}


def compute_cohens_kappa(labels1: list[str], labels2: list[str]) -> float:
    from collections import Counter
    assert len(labels1) == len(labels2)
    n = len(labels1)
    if n == 0:
        return 0.0
    agree = sum(1 for a, b in zip(labels1, labels2) if a == b)
    p_o = agree / n
    counts1 = Counter(labels1)
    counts2 = Counter(labels2)
    all_labels = set(labels1) | set(labels2)
    p_e = sum((counts1[l] / n) * (counts2[l] / n) for l in all_labels)
    if p_e >= 1.0:
        return 1.0
    return (p_o - p_e) / (1 - p_e)


def compute_per_category_agreement(labels1: list[str], labels2: list[str]) -> dict:
    categories = sorted(set(labels1) | set(labels2))
    result = {}
    for cat in categories:
        tp = sum(1 for a, b in zip(labels1, labels2) if a == cat and b == cat)
        fn = sum(1 for a, b in zip(labels1, labels2) if a == cat and b != cat)
        fp = sum(1 for a, b in zip(labels1, labels2) if a != cat and b == cat)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        result[cat] = {"precision": round(precision, 4), "recall": round(recall, 4),
                       "f1": round(f1, 4), "support_llm": tp + fn, "support_gpt4o": tp + fp}
    return result


def build_confusion_matrix(labels1: list[str], labels2: list[str]) -> dict:
    categories = sorted(set(labels1) | set(labels2))
    matrix = {cat: {c: 0 for c in categories} for cat in categories}
    for a, b in zip(labels1, labels2):
        matrix[a][b] += 1
    return matrix


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/human_annotation/annotation_sheet_full.csv")
    parser.add_argument("--output", default="outputs/gpt4o_annotation")
    parser.add_argument("--api-key", required=True)
    parser.add_argument("--model", default="gpt-4o")
    parser.add_argument("--resume", action="store_true", help="Resume from partial results")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    client = OpenAI(api_key=[REDACTED]

    rows = []
    with open(args.input, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    logger.info("Loaded %d messages from %s", len(rows), args.input)

    result_csv = os.path.join(args.output, "gpt4o_annotations.csv")
    done_ids = set()
    partial_results = []
    if args.resume and os.path.exists(result_csv):
        with open(result_csv, newline="") as f:
            reader = csv.DictReader(f)
            partial_results = [r for r in reader if r.get("gpt4o_label") != "unknown"]
            done_ids = {r["msg_id"] for r in partial_results}
        logger.info("Resuming: %d valid done, retrying unknown", len(done_ids))

    token_tracker = {"prompt_tokens": 0, "completion_tokens": 0, "api_calls": 0}

    results = list(partial_results)
    for i, row in enumerate(rows):
        if row["msg_id"] in done_ids:
            continue
        logger.info("[%d/%d] Annotating %s", i + 1, len(rows), row["msg_id"])
        ann = annotate_single(
            client, args.model,
            prev_text=row.get("prev_message_text", ""),
            msg_text=row["message_text"],
            sender=row["sender"],
            task_id=row["task_id"],
            token_tracker=token_tracker,
        )
        results.append({
            "msg_id": row["msg_id"],
            "backbone": row["backbone"],
            "topology": row["topology"],
            "task_id": row["task_id"],
            "sender": row["sender"],
            "llm_label": row["llm_label"],
            "gpt4o_label": ann.get("type", "unknown"),
            "gpt4o_confidence": ann.get("confidence", 0),
            "gpt4o_reasoning": ann.get("reasoning", ""),
        })
        time.sleep(2.5)
        if (i + 1) % 25 == 0:
            _save_csv(result_csv, results)
            logger.info("Checkpoint saved at %d/%d", i + 1, len(rows))

    _save_csv(result_csv, results)

    # --- Compute statistics ---
    valid = [r for r in results if r["gpt4o_label"] != "unknown"]
    llm_labels = [r["llm_label"] for r in valid]
    gpt4o_labels = [r["gpt4o_label"] for r in valid]

    kappa = compute_cohens_kappa(llm_labels, gpt4o_labels)
    agreement = sum(1 for a, b in zip(llm_labels, gpt4o_labels) if a == b) / len(llm_labels)
    per_cat = compute_per_category_agreement(llm_labels, gpt4o_labels)
    confusion = build_confusion_matrix(llm_labels, gpt4o_labels)

    # Per-backbone kappa
    per_backbone = {}
    for bb in sorted(set(r["backbone"] for r in valid)):
        bb_rows = [r for r in valid if r["backbone"] == bb]
        bb_llm = [r["llm_label"] for r in bb_rows]
        bb_gpt = [r["gpt4o_label"] for r in bb_rows]
        bb_kappa = compute_cohens_kappa(bb_llm, bb_gpt)
        bb_agree = sum(1 for a, b in zip(bb_llm, bb_gpt) if a == b) / len(bb_llm)
        per_backbone[bb] = {"kappa": round(bb_kappa, 4), "agreement": round(bb_agree, 4), "n": len(bb_rows)}

    # GPT-4o pricing (USD per 1M tokens, as of 2025)
    PRICE_INPUT_PER_M = 2.50
    PRICE_OUTPUT_PER_M = 10.00
    prompt_cost = token_tracker["prompt_tokens"] / 1_000_000 * PRICE_INPUT_PER_M
    completion_cost = token_tracker["completion_tokens"] / 1_000_000 * PRICE_OUTPUT_PER_M
    total_cost = prompt_cost + completion_cost
    total_tokens = token_tracker["prompt_tokens"] + token_tracker["completion_tokens"]
    avg_tokens_per_msg = total_tokens / token_tracker["api_calls"] if token_tracker["api_calls"] > 0 else 0

    token_stats = {
        "prompt_tokens": token_tracker["prompt_tokens"],
        "completion_tokens": token_tracker["completion_tokens"],
        "total_tokens": total_tokens,
        "api_calls": token_tracker["api_calls"],
        "avg_tokens_per_message": round(avg_tokens_per_msg, 1),
        "cost_usd": {
            "input": round(prompt_cost, 4),
            "output": round(completion_cost, 4),
            "total": round(total_cost, 4),
        },
        "pricing_note": "GPT-4o: $2.50/M input, $10.00/M output",
    }

    stats = {
        "overall": {
            "cohens_kappa": round(kappa, 4),
            "percent_agreement": round(agreement, 4),
            "n_total": len(valid),
            "n_unknown": len(results) - len(valid),
        },
        "per_backbone": per_backbone,
        "per_category": per_cat,
        "confusion_matrix": confusion,
        "token_usage": token_stats,
    }

    stats_path = os.path.join(args.output, "gpt4o_kappa_stats.json")
    with open(stats_path, "w") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    logger.info("=== GPT-4o Annotation Results ===")
    logger.info("Overall κ=%.4f, agreement=%.1f%%, n=%d", kappa, agreement * 100, len(valid))
    for bb, s in per_backbone.items():
        logger.info("  %s: κ=%.4f, agreement=%.1f%%", bb, s["kappa"], s["agreement"] * 100)
    logger.info("=== Token Usage ===")
    logger.info("Prompt tokens: %d, Completion tokens: %d, Total: %d",
                token_tracker["prompt_tokens"], token_tracker["completion_tokens"], total_tokens)
    logger.info("Avg tokens/message: %.1f", avg_tokens_per_msg)
    logger.info("Cost: input=$%.4f + output=$%.4f = total=$%.4f USD",
                prompt_cost, completion_cost, total_cost)
    logger.info("Stats saved to %s", stats_path)
    logger.info("Annotations saved to %s", result_csv)


def _save_csv(path: str, rows: list[dict]):
    if not rows:
        return
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def _save_json(path: str, data: dict):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


def compute_oracle_cache_key(task_id: str, text: str, prev_text: str) -> str:
    """Matches pruning_validation.compute_oracle_cache_key exactly."""
    prev_norm = prev_text[:2000] if prev_text else ""
    text_norm = text[:3000]
    return hashlib.sha256(f"{task_id}\n{prev_norm}\n{text_norm}".encode()).hexdigest()


def oracle_precompute(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(
        description="Precompute oracle ack/non-ack labels from traces JSONL",
    )
    parser.add_argument("--input", required=True,
                        help="Traces JSONL file (one JSON object per line)")
    parser.add_argument("--output", required=True,
                        help="Output oracle cache JSON path")
    parser.add_argument("--checkpoint",
                        help="Checkpoint path (default: <output>.ckpt)")
    parser.add_argument("--api-key",
                        help="OpenAI API key (or set OPENAI_API_KEY env var)")
    parser.add_argument("--model", default="gpt-4o")
    parser.add_argument("--dry-run", action="store_true",
                        help="Count messages without calling the API")
    args = parser.parse_args(argv)

    if not args.checkpoint:
        args.checkpoint = args.output + ".ckpt"

    api_key = [REDACTED] or os.environ.get("OPENAI_API_KEY")
    if not api_key and not args.dry_run:
        raise SystemExit("Set OPENAI_API_KEY or pass --api-key")

    tasks = []
    with open(args.input) as f:
        for line in f:
            line = line.strip()
            if line:
                tasks.append(json.loads(line))
    logger.info("Loaded %d tasks from %s", len(tasks), args.input)

    cache: dict[str, dict] = {}
    if os.path.exists(args.checkpoint):
        with open(args.checkpoint) as f:
            cache = json.load(f)
        logger.info("Resumed %d cached labels from %s", len(cache), args.checkpoint)

    total_msgs = 0
    pending_msgs = 0
    for task in tasks:
        msgs = task["messages"]
        for i, msg in enumerate(msgs):
            total_msgs += 1
            prev_text = msgs[i - 1]["content"] if i > 0 else ""
            key = compute_oracle_cache_key(task["task_id"], msg["content"], prev_text)
            if key not in cache:
                pending_msgs += 1

    logger.info("Messages: %d total, %d cached, %d pending",
                total_msgs, total_msgs - pending_msgs, pending_msgs)

    if args.dry_run:
        est_tokens = pending_msgs * 800
        est_cost = est_tokens / 1_000_000 * 2.50 + (pending_msgs * 50) / 1_000_000 * 10.00
        logger.info("Estimated cost: ~$%.2f (%.0fK tokens @ GPT-4o rates)", est_cost, est_tokens / 1000)
        return

    client = OpenAI(api_key=[REDACTED]
    token_tracker = {"prompt_tokens": 0, "completion_tokens": 0, "api_calls": 0}
    newly_done = 0

    for task in tasks:
        task_id = task["task_id"]
        msgs = task["messages"]
        for i, msg in enumerate(msgs):
            prev_text = msgs[i - 1]["content"] if i > 0 else ""
            key = compute_oracle_cache_key(task_id, msg["content"], prev_text)
            if key in cache:
                continue

            ann = annotate_single(
                client, args.model,
                prev_text=prev_text,
                msg_text=msg["content"],
                sender=msg["sender"],
                task_id=task_id,
                token_tracker=token_tracker,
            )

            func_type = ann.get("type", "unknown")
            cache[key] = {
                "is_ack": func_type == "acknowledgment",
                "confidence": ann.get("confidence", 0.0),
                "function_type": func_type,
                "task_id": task_id,
                "round": msg.get("round", i),
                "sender": msg["sender"],
            }

            newly_done += 1
            if newly_done % 10 == 0:
                _save_json(args.checkpoint, cache)
                logger.info("[%d/%d] checkpoint saved (%d total cached)",
                            newly_done, pending_msgs, len(cache))

            time.sleep(2.5)

    _save_json(args.checkpoint, cache)
    _save_json(args.output, cache)

    total_tokens = token_tracker["prompt_tokens"] + token_tracker["completion_tokens"]
    cost_in = token_tracker["prompt_tokens"] / 1_000_000 * 2.50
    cost_out = token_tracker["completion_tokens"] / 1_000_000 * 10.00
    logger.info("Done. %d labels → %s", len(cache), args.output)
    logger.info("API: %d calls, %d tokens, $%.4f",
                token_tracker["api_calls"], total_tokens, cost_in + cost_out)

    n_ack = sum(1 for v in cache.values() if v["is_ack"])
    logger.info("Label distribution: %d ack, %d non-ack (%.1f%% ack)",
                n_ack, len(cache) - n_ack,
                100 * n_ack / len(cache) if cache else 0)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "oracle-precompute":
        oracle_precompute(sys.argv[2:])
    else:
        main()
