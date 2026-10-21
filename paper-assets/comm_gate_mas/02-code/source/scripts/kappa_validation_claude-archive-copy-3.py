"""Cohen's κ validation: Claude Sonnet vs GPT-4o AND vs Human annotators.

Two comparisons in one run:
  Part 1 (claude-vs-gpt4o): 100 Qwen messages from oracle_qwen_10run,
    compute 5-class and binary κ between Claude and GPT-4o.
  Part 2 (claude-vs-human): 225 messages from human annotation sheet,
    compute 5-class and binary κ between Claude and human annotator.

Decision gate (D191): κ_binary > 0.8 → Plan A (Claude as Llama oracle).

Usage:
  OPENROUTER_API_KEY=[REDACTED] python scripts/kappa_validation_claude.py
  python scripts/kappa_validation_claude.py --dry-run
  python scripts/kappa_validation_claude.py --mode oracle   # GPT-4o only
  python scripts/kappa_validation_claude.py --mode human    # Human only
"""
from __future__ import annotations

import argparse
import csv
import json
import logging
import os
import random
import sys
import time
from collections import Counter

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

VALID_TYPES = {"information_provision", "reasoning_guidance", "verification",
               "coordination", "acknowledgment"}

MODEL = "anthropic/claude-sonnet-4"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Anthropic Sonnet pricing (USD per 1M tokens, 2025)
PRICE_INPUT_PER_M = 3.00
PRICE_OUTPUT_PER_M = 15.00


def classify_message(client: OpenAI, prev_text: str, msg_text: str,
                     sender: str, task_id: str, token_tracker: dict) -> dict:
    user_prompt = f"""## Context

Task: {task_id}

### Previous message (for context):
{prev_text[:2000] if prev_text else '[conversation start]'}

### Current message to classify (sent by {sender}):
{msg_text[:3000]}

Classify the function of the current message."""

    for attempt in range(4):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                max_tokens=256,
                temperature=0,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
            )
            if resp.usage:
                token_tracker["input_tokens"] += resp.usage.prompt_tokens or 0
                token_tracker["output_tokens"] += resp.usage.completion_tokens or 0
            token_tracker["api_calls"] += 1

            raw = resp.choices[0].message.content or "{}"
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
            result = json.loads(raw)
            if result.get("type") not in VALID_TYPES:
                logger.warning("Invalid type %r, retrying", result.get("type"))
                continue
            return result
        except json.JSONDecodeError:
            logger.warning("Attempt %d JSON parse failed for %s", attempt + 1, task_id)
            time.sleep(1)
        except Exception as e:
            err_str = str(e).lower()
            if "rate" in err_str or "429" in err_str:
                backoff = 15 * (2 ** min(attempt, 3))
                logger.warning("Rate limit (attempt %d), backing off %ds", attempt + 1, backoff)
                time.sleep(backoff)
            else:
                logger.warning("Attempt %d failed: %s", attempt + 1, e)
                if attempt < 3:
                    time.sleep(2 ** attempt)
    return {"type": "unknown", "confidence": 0.0, "reasoning": "all attempts failed"}


# ── Statistics ──────────────────────────────────────────────────────

def compute_cohens_kappa(labels1: list[str], labels2: list[str]) -> float:
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


def compute_per_category(labels_ref: list[str], labels_pred: list[str],
                         ref_name: str = "ref", pred_name: str = "pred") -> dict:
    categories = sorted(set(labels_ref) | set(labels_pred))
    result = {}
    for cat in categories:
        tp = sum(1 for a, b in zip(labels_ref, labels_pred) if a == cat and b == cat)
        fn = sum(1 for a, b in zip(labels_ref, labels_pred) if a == cat and b != cat)
        fp = sum(1 for a, b in zip(labels_ref, labels_pred) if a != cat and b == cat)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        result[cat] = {"precision": round(precision, 4), "recall": round(recall, 4),
                       "f1": round(f1, 4),
                       f"support_{ref_name}": tp + fn,
                       f"support_{pred_name}": tp + fp}
    return result


def build_confusion_matrix(labels1: list[str], labels2: list[str]) -> dict:
    categories = sorted(set(labels1) | set(labels2))
    matrix = {cat: {c: 0 for c in categories} for cat in categories}
    for a, b in zip(labels1, labels2):
        matrix[a][b] += 1
    return matrix


def compute_kappa_report(ref_labels: list[str], pred_labels: list[str],
                         ref_name: str, pred_name: str) -> dict:
    kappa_5 = compute_cohens_kappa(ref_labels, pred_labels)
    agree_5 = sum(1 for a, b in zip(ref_labels, pred_labels) if a == b) / len(ref_labels)

    ref_bin = ["ack" if l == "acknowledgment" else "non-ack" for l in ref_labels]
    pred_bin = ["ack" if l == "acknowledgment" else "non-ack" for l in pred_labels]
    kappa_bin = compute_cohens_kappa(ref_bin, pred_bin)
    agree_bin = sum(1 for a, b in zip(ref_bin, pred_bin) if a == b) / len(ref_bin)

    return {
        "kappa_5class": round(kappa_5, 4),
        "kappa_binary_ack": round(kappa_bin, 4),
        "agreement_5class": round(agree_5, 4),
        "agreement_binary": round(agree_bin, 4),
        "n": len(ref_labels),
        "per_category": compute_per_category(ref_labels, pred_labels, ref_name, pred_name),
        "confusion_matrix": build_confusion_matrix(ref_labels, pred_labels),
        "distribution": {
            ref_name: dict(Counter(ref_labels).most_common()),
            pred_name: dict(Counter(pred_labels).most_common()),
        },
    }


# ── Data Loading ────────────────────────────────────────────────────

def load_oracle_data(traces_path: str, oracle_path: str) -> list[dict]:
    with open(traces_path) as f:
        traces = {}
        for line in f:
            if line.strip():
                t = json.loads(line)
                traces[t["task_id"]] = t

    with open(oracle_path) as f:
        oracle = json.load(f)

    samples = []
    for task_entry in oracle["per_task"]:
        task_id = task_entry["task_id"]
        if task_id not in traces:
            continue
        trace_msgs = traces[task_id]["messages"]
        round_to_msg = {m["round"]: m for m in trace_msgs}

        for decision in task_entry["oracle_decisions"]:
            r = decision["round"]
            if r not in round_to_msg:
                continue
            msg = round_to_msg[r]
            prev_round = r - 1
            prev_text = round_to_msg[prev_round]["content"] if prev_round in round_to_msg else ""

            samples.append({
                "source": "oracle",
                "msg_id": f"{task_id}_r{r}",
                "task_id": task_id,
                "round": r,
                "sender": msg["sender"],
                "content": msg["content"],
                "prev_content": prev_text,
                "ref_label": decision["function_type"],
                "ref_is_ack": decision["is_ack"],
            })
    return samples


def load_human_data(full_path: str, completed_path: str) -> list[dict]:
    with open(full_path) as f:
        full_rows = {r["msg_id"]: r for r in csv.DictReader(f)}

    with open(completed_path) as f:
        human_rows = list(csv.DictReader(f))

    samples = []
    for hr in human_rows:
        mid = hr["msg_id"]
        human_label = hr.get("human_label", "").strip()
        if not human_label or human_label not in VALID_TYPES:
            continue
        fr = full_rows.get(mid, hr)
        samples.append({
            "source": "human",
            "msg_id": mid,
            "task_id": hr.get("task_id", ""),
            "round": int(hr.get("round", 0)),
            "sender": hr.get("sender", ""),
            "content": fr.get("message_text", hr.get("message_text", "")),
            "prev_content": fr.get("prev_message_text", hr.get("prev_message_text", "")),
            "ref_label": human_label,
            "ref_is_ack": human_label == "acknowledgment",
            "backbone": hr.get("backbone", ""),
        })
    return samples


def stratified_sample(samples: list[dict], n: int, seed: int = 42) -> list[dict]:
    rng = random.Random(seed)
    by_type = {}
    for s in samples:
        by_type.setdefault(s["ref_label"], []).append(s)

    result = []
    n_types = len(by_type)
    min_per_type = max(5, n // (n_types * 2))

    for typ, items in by_type.items():
        rng.shuffle(items)
        take = min(min_per_type, len(items))
        result.extend(items[:take])

    remaining_pool = [s for s in samples if s not in result]
    rng.shuffle(remaining_pool)
    need = n - len(result)
    if need > 0:
        result.extend(remaining_pool[:need])

    rng.shuffle(result)
    return result[:n]


# ── Batch Classification ───────────────────────────────────────────

def classify_batch(client: OpenAI | None, samples: list[dict],
                   token_tracker: dict, label: str, dry_run: bool = False) -> list[dict]:
    logger.info("── %s: classifying %d messages ──", label, len(samples))

    if dry_run:
        dist = Counter(s["ref_label"] for s in samples)
        logger.info("  Ref distribution: %s", dict(dist.most_common()))
        for s in samples[:3]:
            logger.info("  %s round=%d ref=%s content=%s...",
                        s["task_id"], s["round"], s["ref_label"], s["content"][:60])
        est_tokens = len(samples) * 900
        est_cost = est_tokens / 1e6 * PRICE_INPUT_PER_M + (len(samples) * 60) / 1e6 * PRICE_OUTPUT_PER_M
        logger.info("  Estimated cost: ~$%.3f", est_cost)
        return samples

    for i, s in enumerate(samples):
        logger.info("[%d/%d] %s r%d (ref=%s)",
                    i + 1, len(samples), s["task_id"], s["round"], s["ref_label"])
        result = classify_message(
            client, s["prev_content"], s["content"],
            s["sender"], s["task_id"], token_tracker,
        )
        s["claude_type"] = result.get("type", "unknown")
        s["claude_confidence"] = result.get("confidence", 0.0)
        s["claude_reasoning"] = result.get("reasoning", "")

        if (i + 1) % 25 == 0:
            done_tokens = token_tracker["input_tokens"] + token_tracker["output_tokens"]
            logger.info("  Progress: %d/%d, tokens: %d", i + 1, len(samples), done_tokens)
        time.sleep(0.5)

    return samples


# ── Main ────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="κ validation: Claude Sonnet vs GPT-4o + Human")
    parser.add_argument("--api-key", help="OpenRouter API key (or OPENROUTER_API_KEY env)")
    parser.add_argument("--mode", choices=["all", "oracle", "human"], default="all",
                        help="Which comparisons to run (default: all)")
    parser.add_argument("--traces", default="outputs/full_scale/qwen_round_robin/traces/traces.jsonl")
    parser.add_argument("--oracle", default="outputs/oracle_qwen_10run/seed_42.json")
    parser.add_argument("--human-full", default="data/human_annotation/annotation_sheet_full.csv")
    parser.add_argument("--human-completed", default="data/human_annotation/annotation_sheet_completed.csv")
    parser.add_argument("--output", default="outputs/kappa_validation/claude_kappa_results.json")
    parser.add_argument("--n-oracle", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    run_oracle = args.mode in ("all", "oracle")
    run_human = args.mode in ("all", "human")

    # ── Load data ──
    oracle_samples, human_samples = [], []
    if run_oracle:
        logger.info("Loading oracle data (Qwen GPT-4o labels)...")
        all_oracle = load_oracle_data(args.traces, args.oracle)
        logger.info("Oracle: %d aligned messages", len(all_oracle))
        oracle_samples = stratified_sample(all_oracle, args.n_oracle, args.seed)
        logger.info("Sampled %d oracle messages", len(oracle_samples))

    if run_human:
        logger.info("Loading human annotation data...")
        human_samples = load_human_data(args.human_full, args.human_completed)
        logger.info("Human: %d annotated messages", len(human_samples))

    total_api_calls = len(oracle_samples) + len(human_samples)
    est_cost = total_api_calls * 900 / 1e6 * PRICE_INPUT_PER_M + total_api_calls * 60 / 1e6 * PRICE_OUTPUT_PER_M
    logger.info("Total messages to classify: %d (est. cost ~$%.2f)", total_api_calls, est_cost)

    if args.dry_run:
        logger.info("=== DRY RUN ===")
        if run_oracle:
            classify_batch(None, oracle_samples, {}, "Claude vs GPT-4o", dry_run=True)
        if run_human:
            classify_batch(None, human_samples, {}, "Claude vs Human", dry_run=True)
        return

    # ── Init client (OpenRouter) ──
    api_key = [REDACTED] or os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        logger.error("Set OPENROUTER_API_KEY or pass --api-key")
        sys.exit(1)

    client = OpenAI(
        base_url=OPENROUTER_BASE_URL,
        api_key=[REDACTED],
        default_headers={
            "HTTP-Referer": "https://github.com/comm-gate-mas",
            "X-Title": "kappa-validation",
        },
    )
    token_tracker = {"input_tokens": 0, "output_tokens": 0, "api_calls": 0}

    # ── Classify ──
    if run_oracle:
        oracle_samples = classify_batch(client, oracle_samples, token_tracker, "Claude vs GPT-4o")
    if run_human:
        human_samples = classify_batch(client, human_samples, token_tracker, "Claude vs Human")

    # ── Compute κ ──
    results = {"model": MODEL, "seed": args.seed, "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")}

    if run_oracle:
        valid = [s for s in oracle_samples if s.get("claude_type") and s["claude_type"] != "unknown"]
        ref = [s["ref_label"] for s in valid]
        pred = [s["claude_type"] for s in valid]
        report = compute_kappa_report(ref, pred, "gpt4o", "claude")
        report["n_total"] = len(oracle_samples)
        report["n_valid"] = len(valid)
        report["per_message"] = [{
            "msg_id": s["msg_id"], "task_id": s["task_id"], "round": s["round"],
            "gpt4o": s["ref_label"], "claude": s["claude_type"],
            "agree_5class": s["ref_label"] == s["claude_type"],
            "agree_binary": s["ref_is_ack"] == (s["claude_type"] == "acknowledgment"),
        } for s in valid]
        results["claude_vs_gpt4o"] = report

        logger.info("═══ Claude vs GPT-4o ═══")
        logger.info("  5-class κ = %.4f (agreement %.1f%%)", report["kappa_5class"], report["agreement_5class"] * 100)
        logger.info("  Binary  κ = %.4f (agreement %.1f%%)", report["kappa_binary_ack"], report["agreement_binary"] * 100)

    if run_human:
        valid = [s for s in human_samples if s.get("claude_type") and s["claude_type"] != "unknown"]
        ref = [s["ref_label"] for s in valid]
        pred = [s["claude_type"] for s in valid]
        report = compute_kappa_report(ref, pred, "human", "claude")
        report["n_total"] = len(human_samples)
        report["n_valid"] = len(valid)

        # Per-backbone breakdown
        per_bb = {}
        for bb in sorted(set(s.get("backbone", "") for s in valid)):
            if not bb:
                continue
            bb_valid = [s for s in valid if s.get("backbone") == bb]
            bb_ref = [s["ref_label"] for s in bb_valid]
            bb_pred = [s["claude_type"] for s in bb_valid]
            bb_kappa = compute_cohens_kappa(bb_ref, bb_pred)
            bb_ref_bin = ["ack" if l == "acknowledgment" else "non-ack" for l in bb_ref]
            bb_pred_bin = ["ack" if l == "acknowledgment" else "non-ack" for l in bb_pred]
            bb_kappa_bin = compute_cohens_kappa(bb_ref_bin, bb_pred_bin)
            per_bb[bb] = {"kappa_5class": round(bb_kappa, 4),
                          "kappa_binary": round(bb_kappa_bin, 4),
                          "n": len(bb_valid)}
        report["per_backbone"] = per_bb

        report["per_message"] = [{
            "msg_id": s["msg_id"], "task_id": s["task_id"], "round": s["round"],
            "backbone": s.get("backbone", ""),
            "human": s["ref_label"], "claude": s["claude_type"],
            "agree_5class": s["ref_label"] == s["claude_type"],
            "agree_binary": s["ref_is_ack"] == (s["claude_type"] == "acknowledgment"),
        } for s in valid]
        results["claude_vs_human"] = report

        logger.info("═══ Claude vs Human ═══")
        logger.info("  5-class κ = %.4f (agreement %.1f%%)", report["kappa_5class"], report["agreement_5class"] * 100)
        logger.info("  Binary  κ = %.4f (agreement %.1f%%)", report["kappa_binary_ack"], report["agreement_binary"] * 100)
        for bb, s in per_bb.items():
            logger.info("    %s: 5c κ=%.4f, bin κ=%.4f (n=%d)", bb, s["kappa_5class"], s["kappa_binary"], s["n"])

    # ── Decision gate ──
    oracle_bin_k = results.get("claude_vs_gpt4o", {}).get("kappa_binary_ack", 0)
    oracle_5c_k = results.get("claude_vs_gpt4o", {}).get("kappa_5class", 0)
    human_bin_k = results.get("claude_vs_human", {}).get("kappa_binary_ack", 0)

    if oracle_bin_k > 0.8 or oracle_5c_k > 0.8:
        decision = "PASS_A"
        reason = f"κ_binary={oracle_bin_k:.4f}, κ_5class={oracle_5c_k:.4f} — at least one > 0.8"
    else:
        decision = "FAIL_C"
        reason = f"κ_binary={oracle_bin_k:.4f}, κ_5class={oracle_5c_k:.4f} — both ≤ 0.8"

    results["decision"] = {
        "gate": decision,
        "reason": reason,
        "rule": "κ_binary > 0.8 OR κ_5class > 0.8 → Plan A (Claude oracle); else → Plan C",
        "human_kappa_binary": human_bin_k,
    }

    # ── Token usage ──
    total_tokens = token_tracker["input_tokens"] + token_tracker["output_tokens"]
    cost_in = token_tracker["input_tokens"] / 1e6 * PRICE_INPUT_PER_M
    cost_out = token_tracker["output_tokens"] / 1e6 * PRICE_OUTPUT_PER_M
    results["token_usage"] = {
        "input_tokens": token_tracker["input_tokens"],
        "output_tokens": token_tracker["output_tokens"],
        "total_tokens": total_tokens,
        "api_calls": token_tracker["api_calls"],
        "cost_usd": round(cost_in + cost_out, 4),
    }

    # ── Save ──
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    logger.info("")
    logger.info("═══ DECISION GATE (D191) ═══")
    logger.info("  %s: %s", decision, reason)
    if human_bin_k:
        logger.info("  (Claude vs Human binary κ = %.4f — for paper reporting)", human_bin_k)
    logger.info("")
    logger.info("Cost: $%.4f (%d tokens, %d calls)", cost_in + cost_out, total_tokens, token_tracker["api_calls"])
    logger.info("Saved to %s", args.output)


if __name__ == "__main__":
    main()
