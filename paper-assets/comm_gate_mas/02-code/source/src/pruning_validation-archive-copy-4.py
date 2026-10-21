"""Pruning validation with two modes: offline simulation and true end-to-end.

Offline (--mode simulate): Remove messages from existing traces, re-extract answers.
  Fast but assumes message independence (upper bound on accuracy retention).

End-to-end (--mode e2e): Re-run the multi-agent pipeline with AG2 reply hooks that
  replace pruned messages with placeholders. Downstream agents generate responses
  based on reduced context. Requires running vLLM instance.

Three pruning strategies compared:
  - function_guided: prune reasoning_guidance + information_provision + verification
  - ack_only: prune acknowledgment messages
  - random: prune same number of rounds randomly (per-task)
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import json
import logging
import os
import random
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

import yaml

_src_dir = os.path.dirname(os.path.abspath(__file__))
if _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)

try:
    from autogen import AssistantAgent, GroupChat, GroupChatManager
except ImportError:
    AssistantAgent = GroupChat = GroupChatManager = None

from utils import extract_final_answer
from arc_utils import extract_arc_answer, arc_answers_equal, format_arc_question
from strategyqa_utils import extract_strategyqa_answer, strategyqa_answers_equal, format_strategyqa_question
from trace_collection import (
    build_llm_config, load_config, load_dataset_from_config,
    _build_agents, _get_agent_names, _extract_messages_from_groupchat, _raise_fd_limit,
    extract_ground_truth,
)
from heuristic_ack_detector import heuristic_is_ack, heuristic_is_ack_llama

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

PLACEHOLDER = "I acknowledge the previous message."

_INFRA_EXCEPTION_NAMES = frozenset({
    "APIConnectionError", "ConnectError", "ConnectionError",
    "NotFoundError", "RemoteProtocolError",
})


def _is_infra_error(exc: Exception) -> bool:
    exc_name = type(exc).__name__
    return any(n in exc_name for n in _INFRA_EXCEPTION_NAMES)

# ---------------------------------------------------------------------------
# Oracle label cache for precomputed annotations
# ---------------------------------------------------------------------------
_oracle_cache: dict = {}
_cache_miss_log = None


def compute_oracle_cache_key(task_id: str, text: str, prev_text: str) -> str:
    prev_norm = prev_text[:2000] if prev_text else ""
    text_norm = text[:3000]
    return hashlib.sha256(f"{task_id}\n{prev_norm}\n{text_norm}".encode()).hexdigest()


def load_oracle_cache(path: str) -> dict:
    with open(path) as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Oracle (GPT-4o) binary ack classifier for online pruning
# ---------------------------------------------------------------------------

# Simplified from the 5-class SYSTEM_PROMPT in gpt4o_annotation.py.
# Binary decision only: ack vs substantive.  Keeps the key priority rule
# (confirm-with-explanation = substantive) to avoid over-suppression.
ORACLE_ACK_SYSTEM_PROMPT = """\
Classify whether this message in a multi-agent math conversation is an \
acknowledgment or substantive.

Acknowledgment: simple confirmation, repetition, or agreement that adds \
no new information, calculations, or reasoning. Restating what was already \
said without extending it.

Substantive: provides new calculations, reasoning steps, error corrections, \
verification with explanation, or extends the solution in any way.

Key rule: if a message confirms correctness WITH a substantive explanation \
or adds new work, classify as substantive.

Respond with ONLY a JSON object (no markdown, no extra text):
{"is_ack": true, "confidence": 0.9}"""


def oracle_is_ack(
    client,
    model: str,
    text: str,
    prev_text: str,
    task_id: str = "",
    round_idx: int = 0,
) -> dict:
    """Binary ack classification via GPT-4o oracle.

    Returns dict with keys: round, is_ack, confidence, tokens.
    Defaults to non-ack (conservative) on failure.
    """
    user_prompt = (
        f"### Previous message:\n{prev_text[:2000] if prev_text else '[start]'}"
        f"\n\n### Current message to classify:\n{text[:3000]}"
    )

    for attempt in range(4):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": ORACLE_ACK_SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0,
                max_tokens=64,
                timeout=120,
            )
            raw = resp.choices[0].message.content or "{}"
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
            result = json.loads(raw)
            return {
                "round": round_idx,
                "is_ack": bool(result.get("is_ack", False)),
                "confidence": float(result.get("confidence", 0.5)),
                "tokens": resp.usage.total_tokens if resp.usage else 0,
            }
        except json.JSONDecodeError:
            logger.warning("Oracle JSON parse fail (attempt %d) task=%s r=%d",
                           attempt + 1, task_id, round_idx)
            time.sleep(1)
        except Exception as e:
            err_str = str(e).lower()
            if "rate" in err_str or "429" in err_str:
                backoff = 15 * (2 ** min(attempt, 3))
                logger.warning("Oracle rate limit (attempt %d), backoff %ds",
                               attempt + 1, backoff)
                time.sleep(backoff)
            else:
                logger.warning("Oracle error (attempt %d) task=%s: %s",
                               attempt + 1, task_id, e)
                time.sleep(2 ** attempt)

    return {
        "round": round_idx,
        "is_ack": False,
        "confidence": 0.0,
        "tokens": 0,
        "error": "all_attempts_failed",
    }


def oracle_5class_is_ack(
    client,
    model: str,
    text: str,
    prev_text: str,
    task_id: str = "",
    round_idx: int = 0,
) -> dict:
    """5-class GPT-4o annotation → binary ack label.

    Uses the same 5-class prompt as gpt4o_annotation.py.
    type=="acknowledgment" → is_ack=True, all others → False.
    Checks _oracle_cache first when loaded; logs misses to _cache_miss_log.
    """
    global _cache_miss_log

    if _oracle_cache:
        cache_key = compute_oracle_cache_key(task_id, text, prev_text)
        if cache_key in _oracle_cache:
            cached = _oracle_cache[cache_key]
            return {
                "round": round_idx,
                "is_ack": cached["is_ack"],
                "confidence": cached.get("confidence", 0.5),
                "tokens": 0,
                "function_type": cached["function_type"],
                "cached": True,
            }
        if _cache_miss_log is not None:
            _cache_miss_log.write(json.dumps({
                "task_id": task_id, "round": round_idx,
                "text": text, "prev_text": prev_text,
                "cache_key": cache_key,
            }) + "\n")
            _cache_miss_log.flush()
        if client is None:
            return {
                "round": round_idx, "is_ack": False, "confidence": 0.0,
                "tokens": 0, "function_type": "cache_miss",
            }

    from gpt4o_annotation import SYSTEM_PROMPT as FIVECLASS_PROMPT

    user_prompt = (
        f"## Context\n\nTask: {task_id}\n\n"
        f"### Previous message (for context):\n"
        f"{prev_text[:2000] if prev_text else '[conversation start]'}\n\n"
        f"### Current message to classify (sent by agent):\n{text[:3000]}\n\n"
        f"Classify the function of the current message."
    )

    for attempt in range(4):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": FIVECLASS_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0,
                max_tokens=256,
                timeout=120,
            )
            raw = resp.choices[0].message.content or "{}"
            raw = raw.strip()
            if raw.startswith("```"):
                raw = raw.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
            result = json.loads(raw)
            func_type = result.get("type", "unknown")
            return {
                "round": round_idx,
                "is_ack": func_type == "acknowledgment",
                "confidence": float(result.get("confidence", 0.5)),
                "tokens": resp.usage.total_tokens if resp.usage else 0,
                "function_type": func_type,
            }
        except json.JSONDecodeError:
            logger.warning("Oracle 5-class JSON parse fail (attempt %d) task=%s r=%d",
                           attempt + 1, task_id, round_idx)
            time.sleep(1)
        except Exception as e:
            err_str = str(e).lower()
            if "rate" in err_str or "429" in err_str:
                backoff = 15 * (2 ** min(attempt, 3))
                logger.warning("Oracle 5-class rate limit (attempt %d), backoff %ds",
                               attempt + 1, backoff)
                time.sleep(backoff)
            else:
                logger.warning("Oracle 5-class error (attempt %d) task=%s: %s",
                               attempt + 1, task_id, e)
                time.sleep(2 ** attempt)

    return {
        "round": round_idx,
        "is_ack": False,
        "confidence": 0.0,
        "tokens": 0,
        "function_type": "unknown",
        "error": "all_attempts_failed",
    }


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def load_annotations(ann_dir: str) -> dict[str, str]:
    """Load function annotations: msg_key -> function_type.

    Supports two formats:
      - Flat (actual output of functional_annotation.py): one record per message,
        fields: task_id, message_index, annotation_a.type (cross-model) or annotation.type
      - Nested (legacy): one record per task with messages array
    """
    ann_file = os.path.join(ann_dir, "annotations.jsonl")
    if not os.path.exists(ann_file):
        return {}
    labels = {}
    with open(ann_file) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            task_id = rec.get("task_id", "")

            if "message_index" in rec:
                # Flat format: message_index is 0-based index of agent messages (round > 0)
                # Round = message_index + 1 (round 0 is the initial question)
                msg_idx = rec["message_index"]
                rnd = msg_idx + 1
                key = f"{task_id}_r{rnd}"
                ann_a = rec.get("annotation_a", {})
                ann_single = rec.get("annotation", {})
                fn_type = ann_a.get("type") or ann_single.get("type") or "unknown"
                labels[key] = fn_type
            elif "messages" in rec:
                # Nested format (legacy)
                for msg in rec["messages"]:
                    key = f"{task_id}_r{msg.get('round', 0)}"
                    labels[key] = msg.get("function_type", msg.get("label", "unknown"))
    return labels


def load_traces(traces_path: str) -> list[dict]:
    """Load all task records from a traces JSONL file."""
    tasks = []
    with open(traces_path) as f:
        for line in f:
            if line.strip():
                tasks.append(json.loads(line))
    return tasks


def check_answer(final_answer, ground_truth) -> bool:
    if final_answer is None:
        return False
    try:
        return abs(float(final_answer) - float(ground_truth)) < 1e-6
    except ValueError:
        return str(final_answer).strip() == str(ground_truth).strip()


def get_prune_rounds_for_task(task_rec: dict, annotations: dict[str, str],
                               prune_types: set[str]) -> set[int]:
    """Determine which rounds to prune for a task based on function annotations."""
    task_id = task_rec["task_id"]
    prune_rounds = set()
    for msg in task_rec.get("messages", []):
        rnd = msg.get("round", 0)
        if rnd == 0:
            continue
        key = f"{task_id}_r{rnd}"
        fn_type = annotations.get(key, "unknown")
        if fn_type in prune_types:
            prune_rounds.add(rnd)
    return prune_rounds


# ---------------------------------------------------------------------------
# End-to-end pruning via AG2 reply hooks
# ---------------------------------------------------------------------------

def run_e2e_pruned_pipeline(
    question: str,
    cfg: dict,
    llm_config: dict,
    prune_rounds: set[int],
    max_rounds: int = 6,
) -> list[dict]:
    """Run round_robin pipeline with real message pruning.

    Uses AG2's register_reply to intercept agent responses at pruned rounds.
    When a round is pruned, the agent returns PLACEHOLDER instead of calling
    the LLM, so downstream agents see reduced context and must generate
    responses accordingly.
    """
    agents = _build_agents(cfg, llm_config)
    agent_names = _get_agent_names(cfg)

    groupchat = GroupChat(
        agents=agents, messages=[], max_round=max_rounds,
        speaker_selection_method="round_robin",
    )
    manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    if not prune_rounds:
        agents[0].initiate_chat(manager, message=question)
        return _extract_messages_from_groupchat(groupchat, agent_names)

    def pruning_hook(recipient, messages, sender, config):
        current_round = len(groupchat.messages)
        if current_round in prune_rounds:
            return True, PLACEHOLDER
        return False, None

    for agent in agents:
        agent.register_reply([GroupChatManager], pruning_hook, position=0)

    agents[0].initiate_chat(manager, message=question)
    return _extract_messages_from_groupchat(groupchat, agent_names)


def _format_question_for_domain(item: dict, domain: str) -> str:
    if domain == "arc":
        return format_arc_question(item)
    elif domain == "strategyqa":
        return item["question"]
    return item["question"]


def _extract_answer_for_domain(text: str, domain: str) -> str | None:
    if domain == "arc":
        return extract_arc_answer(text)
    elif domain == "strategyqa":
        return extract_strategyqa_answer(text)
    return extract_final_answer(text)


def _check_answer_for_domain(final_answer, ground_truth, domain: str) -> bool:
    if domain == "arc":
        return arc_answers_equal(final_answer, ground_truth)
    elif domain == "strategyqa":
        return strategyqa_answers_equal(final_answer, ground_truth)
    return check_answer(final_answer, ground_truth)


def compute_ack_position_weights(
    tasks: list[dict],
    annotations: dict[str, str],
) -> dict[int, float]:
    """Compute global ack frequency at each round position across all tasks."""
    from collections import Counter
    counts: Counter = Counter()
    for task_rec in tasks:
        task_id = task_rec["task_id"]
        for msg in task_rec.get("messages", []):
            rnd = msg.get("round", 0)
            if rnd == 0:
                continue
            key = f"{task_id}_r{rnd}"
            if annotations.get(key) == "acknowledgment":
                counts[rnd] += 1
    total = sum(counts.values())
    if total == 0:
        return {}
    return {rnd: cnt / total for rnd, cnt in counts.items()}


def run_e2e_strategy(
    tasks: list[dict],
    annotations: dict[str, str],
    prune_types: set[str],
    cfg: dict,
    llm_config: dict,
    strategy_name: str,
    random_seed: int | None = None,
    domain: str = "gsm8k",
    position_weights: dict[int, float] | None = None,
) -> dict:
    """Run e2e pruning for a list of tasks under one strategy.

    For 'random' strategy, pass random_seed to randomize which rounds to prune
    (same count as function_guided would prune per task).
    If position_weights is provided, use weighted sampling matching ack position distribution.
    """
    import numpy as np

    max_rounds = cfg["trace_collection"].get("max_rounds", 6)
    correct = 0
    total = 0
    total_pruned_rounds = 0
    total_rounds = 0
    per_task_results = []

    for idx, task_rec in enumerate(tasks):
        task_id = task_rec["task_id"]
        question = task_rec["question"]
        ground_truth = task_rec["ground_truth"]
        total += 1

        # Determine which rounds to prune
        if random_seed is not None:
            # Random strategy: prune same count as function_guided would
            fg_rounds = get_prune_rounds_for_task(task_rec, annotations, prune_types)
            all_rounds = sorted({msg["round"] for msg in task_rec.get("messages", [])
                                 if msg.get("round", 0) > 0})
            n_to_prune = min(len(fg_rounds), len(all_rounds))

            if position_weights and n_to_prune > 0:
                weights = np.array([position_weights.get(r, 1e-6) for r in all_rounds])
                weights /= weights.sum()
                rng_np = np.random.RandomState(random_seed + idx)
                chosen = rng_np.choice(len(all_rounds), size=n_to_prune,
                                       replace=False, p=weights)
                prune_rounds = {all_rounds[i] for i in chosen}
            else:
                rng = random.Random(random_seed + idx)
                prune_rounds = set(rng.sample(all_rounds, n_to_prune))
        else:
            prune_rounds = get_prune_rounds_for_task(task_rec, annotations, prune_types)

        task_total_rounds = len([m for m in task_rec.get("messages", [])
                                 if m.get("round", 0) > 0])
        total_pruned_rounds += len(prune_rounds)
        total_rounds += task_total_rounds

        try:
            messages = run_e2e_pruned_pipeline(
                question, cfg, llm_config, prune_rounds, max_rounds=max_rounds
            )
        except Exception:
            logger.exception("E2E failed on %s", task_id)
            continue
        finally:
            gc.collect()

        final_answer = None
        for msg in reversed(messages):
            final_answer = _extract_answer_for_domain(msg.get("content", ""), domain)
            if final_answer is not None:
                break

        is_correct = _check_answer_for_domain(final_answer, ground_truth, domain)
        if is_correct:
            correct += 1
        per_task_results.append({"task_id": task_id, "correct": is_correct})

        logger.info("[%s] %d/%d task=%s prune=%d/%d correct=%s answer=%s",
                    strategy_name, idx + 1, len(tasks), task_id,
                    len(prune_rounds), task_total_rounds, is_correct, final_answer)

    accuracy = correct / total if total > 0 else 0
    prune_pct = total_pruned_rounds / total_rounds * 100 if total_rounds > 0 else 0

    return {
        "strategy": strategy_name,
        "correct": correct,
        "total": total,
        "accuracy": round(accuracy, 4),
        "total_pruned_rounds": total_pruned_rounds,
        "total_rounds": total_rounds,
        "prune_pct": round(prune_pct, 2),
        "per_task": per_task_results,
    }


def e2e_main(args):
    """End-to-end pruning validation main."""
    _raise_fd_limit()

    cfg = load_config(args.config)
    llm_config = build_llm_config(cfg)
    domain = cfg.get("data", {}).get("source", "gsm8k")

    traces_path = os.path.join(args.traces_dir, "traces.jsonl")
    annotations = load_annotations(args.annotations_dir)
    logger.info("Loaded %d annotation labels", len(annotations))

    all_tasks = load_traces(traces_path)
    if args.task_offset:
        all_tasks = all_tasks[args.task_offset:]
    if args.num_tasks and args.num_tasks < len(all_tasks):
        all_tasks = all_tasks[:args.num_tasks]
    logger.info("Using %d tasks for e2e validation (offset=%d, domain=%s)",
                len(all_tasks), args.task_offset, domain)

    # Baseline accuracy from existing traces
    baseline_correct = sum(1 for t in all_tasks if t.get("is_correct"))
    baseline = {
        "correct": baseline_correct,
        "total": len(all_tasks),
        "accuracy": round(baseline_correct / len(all_tasks), 4) if all_tasks else 0,
    }
    logger.info("Baseline accuracy: %d/%d = %.1f%%",
                baseline["correct"], baseline["total"], baseline["accuracy"] * 100)

    fg_types = {"reasoning_guidance", "information_provision", "verification"}
    ack_types = {"acknowledgment"}

    strategy = getattr(args, "strategy", "all")
    strategies = {}

    if strategy in ("all", "function_guided"):
        fg_result = run_e2e_strategy(
            all_tasks, annotations, fg_types, cfg, llm_config, "function_guided",
            domain=domain,
        )
        logger.info("Function-guided: accuracy=%.1f%%, prune=%.1f%%",
                     fg_result["accuracy"] * 100, fg_result["prune_pct"])
        strategies["function_guided"] = fg_result

    if strategy in ("all", "ack_only"):
        ack_result = run_e2e_strategy(
            all_tasks, annotations, ack_types, cfg, llm_config, "ack_only",
            domain=domain,
        )
        logger.info("Ack-only: accuracy=%.1f%%, prune=%.1f%%",
                     ack_result["accuracy"] * 100, ack_result["prune_pct"])
        strategies["ack_only"] = ack_result

    if strategy in ("all", "random"):
        # Random should match ack_only's prune count for fair comparison (Table 1)
        if "ack_only" in strategies:
            ref_types = ack_types
        elif "function_guided" in strategies:
            ref_types = fg_types
        else:
            ref_types = ack_types
        random_result = run_e2e_strategy(
            all_tasks, annotations, ref_types, cfg, llm_config, "random",
            random_seed=42, domain=domain,
        )
        logger.info("Random: accuracy=%.1f%%, prune=%.1f%%",
                     random_result["accuracy"] * 100, random_result["prune_pct"])
        strategies["random"] = random_result

    output = {
        "mode": "e2e",
        "strategy_filter": strategy,
        "num_tasks": len(all_tasks),
        "baseline": baseline,
        "strategies": strategies,
        "comparison": {},
        "config": {
            "model": cfg["model"]["name"],
            "api_base": cfg["model"]["api_base"],
            "max_rounds": cfg["trace_collection"].get("max_rounds", 6),
            "placeholder": PLACEHOLDER,
        },
    }

    if "function_guided" in strategies and "ack_only" in strategies:
        fg_result = strategies["function_guided"]
        ack_result = strategies["ack_only"]
        output["comparison"]["fg_vs_baseline_delta_pp"] = round(
            (fg_result["accuracy"] - baseline["accuracy"]) * 100, 2)
        output["comparison"]["ack_vs_baseline_delta_pp"] = round(
            (ack_result["accuracy"] - baseline["accuracy"]) * 100, 2)
    for s_name, s_result in strategies.items():
        output["comparison"][f"{s_name}_vs_baseline_delta_pp"] = round(
            (s_result["accuracy"] - baseline["accuracy"]) * 100, 2)
    if "function_guided" in strategies and "random" in strategies:
        output["comparison"]["fg_vs_random_delta_pp"] = round(
            (strategies["function_guided"]["accuracy"] - strategies["random"]["accuracy"]) * 100, 2)
        output["comparison"]["fg_dominates_random"] = (
            strategies["function_guided"]["accuracy"] >= strategies["random"]["accuracy"])

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info("E2E results saved to %s", args.output)


# ---------------------------------------------------------------------------
# Multi-trial random + McNemar test
# ---------------------------------------------------------------------------

def mcnemar_test(fg_per_task: list[dict], rand_per_task: list[dict]) -> dict:
    """McNemar's test comparing two strategies on per-task correctness.

    Returns contingency table counts and p-value (exact binomial).
    """
    try:
        from scipy.stats import binomtest
        def _binom_pvalue(x, n, p):
            return binomtest(x, n, p).pvalue
    except ImportError:
        from scipy.stats import binom_test as _binom_pvalue
    fg_map = {r["task_id"]: r["correct"] for r in fg_per_task}
    rand_map = {r["task_id"]: r["correct"] for r in rand_per_task}
    common = set(fg_map) & set(rand_map)

    # b = fg correct, rand wrong; c = fg wrong, rand correct
    a = b = c = d = 0
    for tid in common:
        fg_ok, rand_ok = fg_map[tid], rand_map[tid]
        if fg_ok and rand_ok:
            a += 1
        elif fg_ok and not rand_ok:
            b += 1
        elif not fg_ok and rand_ok:
            c += 1
        else:
            d += 1

    n_discordant = b + c
    if n_discordant == 0:
        p_value = 1.0
    else:
        p_value = float(_binom_pvalue(min(b, c), n_discordant, 0.5))

    return {
        "a_both_correct": a, "b_fg_only": b,
        "c_rand_only": c, "d_both_wrong": d,
        "n_discordant": n_discordant, "p_value": round(p_value, 6),
        "significant_005": p_value < 0.05,
    }


def e2e_random_multi_main(args):
    """Run random e2e pruning with multiple seeds + McNemar vs function_guided."""
    import numpy as np
    _raise_fd_limit()

    cfg = load_config(args.config)
    llm_config = build_llm_config(cfg)
    domain = cfg.get("data", {}).get("source", "gsm8k")

    traces_path = os.path.join(args.traces_dir, "traces.jsonl")
    annotations = load_annotations(args.annotations_dir)
    logger.info("Loaded %d annotation labels", len(annotations))

    all_tasks = load_traces(traces_path)
    if args.task_offset:
        all_tasks = all_tasks[args.task_offset:]
    if args.num_tasks and args.num_tasks < len(all_tasks):
        all_tasks = all_tasks[:args.num_tasks]
    logger.info("Using %d tasks (offset=%d, domain=%s)",
                len(all_tasks), args.task_offset, domain)

    baseline_correct = sum(1 for t in all_tasks if t.get("is_correct"))
    baseline = {
        "correct": baseline_correct, "total": len(all_tasks),
        "accuracy": round(baseline_correct / len(all_tasks), 4) if all_tasks else 0,
    }

    fg_types = {"reasoning_guidance", "information_provision", "verification"}
    ack_types = {"acknowledgment"}

    random_only = getattr(args, "random_only", False)
    fg_result = None
    ack_result = None

    if not random_only:
        # Run function_guided once (for McNemar comparison)
        logger.info("Running function_guided strategy...")
        fg_result = run_e2e_strategy(
            all_tasks, annotations, fg_types, cfg, llm_config, "function_guided",
            domain=domain,
        )
        logger.info("Function-guided: %.1f%%", fg_result["accuracy"] * 100)

        # Run ack_only once (for McNemar comparison)
        logger.info("Running ack_only strategy...")
        ack_result = run_e2e_strategy(
            all_tasks, annotations, ack_types, cfg, llm_config, "ack_only",
            domain=domain,
        )
        logger.info("Ack-only: %.1f%%", ack_result["accuracy"] * 100)
    else:
        logger.info("--random-only: skipping function_guided and ack_only")

    # Run random with multiple seeds
    # --random-ref controls whether random prune count matches fg or ack
    random_ref = getattr(args, "random_ref", "fg")
    random_ref_types = ack_types if random_ref == "ack" else fg_types
    logger.info("Random reference strategy: %s", random_ref)

    n_trials = args.random_trials
    seed_base = args.random_seed_start if args.random_seed_start is not None else 100
    trial_results = []
    mcnemar_fg_vs_rand = []
    mcnemar_ack_vs_rand = []

    for trial in range(n_trials):
        seed = seed_base + trial
        logger.info("Random trial %d/%d (seed=%d)...", trial + 1, n_trials, seed)
        rand_result = run_e2e_strategy(
            all_tasks, annotations, random_ref_types, cfg, llm_config,
            f"random_seed{seed}", random_seed=seed, domain=domain,
        )
        trial_results.append(rand_result)

        if fg_result and ack_result:
            mc_fg = mcnemar_test(fg_result["per_task"], rand_result["per_task"])
            mc_ack = mcnemar_test(ack_result["per_task"], rand_result["per_task"])
            mcnemar_fg_vs_rand.append(mc_fg)
            mcnemar_ack_vs_rand.append(mc_ack)
            logger.info("  accuracy=%.1f%%, McNemar fg p=%.4f, ack p=%.4f",
                        rand_result["accuracy"] * 100, mc_fg["p_value"], mc_ack["p_value"])
        else:
            logger.info("  accuracy=%.1f%%", rand_result["accuracy"] * 100)

    mcnemar_fg_vs_ack = None
    if fg_result and ack_result:
        mcnemar_fg_vs_ack = mcnemar_test(fg_result["per_task"], ack_result["per_task"])
        logger.info("McNemar fg vs ack: p=%.4f", mcnemar_fg_vs_ack["p_value"])

    accs = [r["accuracy"] for r in trial_results]
    mean_acc = float(np.mean(accs))
    std_acc = float(np.std(accs, ddof=1)) if n_trials > 1 else 0.0
    ci_95 = 1.96 * std_acc / np.sqrt(n_trials) if n_trials > 1 else 0.0
    fg_p_values = [m["p_value"] for m in mcnemar_fg_vs_rand]
    ack_p_values = [m["p_value"] for m in mcnemar_ack_vs_rand]

    output = {
        "mode": "e2e_random_multi",
        "num_tasks": len(all_tasks),
        "n_trials": n_trials,
        "seed_base": seed_base,
        "baseline": baseline,
    }

    if fg_result:
        output["function_guided"] = {
            "accuracy": fg_result["accuracy"],
            "correct": fg_result["correct"],
            "total": fg_result["total"],
            "prune_pct": fg_result["prune_pct"],
        }
    if ack_result:
        output["ack_only"] = {
            "accuracy": ack_result["accuracy"],
            "correct": ack_result["correct"],
            "total": ack_result["total"],
            "prune_pct": ack_result["prune_pct"],
        }

    output["random_multi"] = {
        "seeds": [seed_base + i for i in range(n_trials)],
        "accuracies": [round(a, 4) for a in accs],
        "mean_accuracy": round(mean_acc, 4),
        "std_accuracy": round(std_acc, 4),
        "ci_95_lower": round(mean_acc - ci_95, 4),
        "ci_95_upper": round(mean_acc + ci_95, 4),
    }

    if mcnemar_fg_vs_rand:
        output["mcnemar_fg_vs_random"] = {
            "per_trial": mcnemar_fg_vs_rand,
            "p_values": [round(p, 6) for p in fg_p_values],
            "any_significant_005": any(p < 0.05 for p in fg_p_values),
            "mean_p_value": round(float(np.mean(fg_p_values)), 6),
        }
    if mcnemar_ack_vs_rand:
        output["mcnemar_ack_vs_random"] = {
            "per_trial": mcnemar_ack_vs_rand,
            "p_values": [round(p, 6) for p in ack_p_values],
            "any_significant_005": any(p < 0.05 for p in ack_p_values),
            "mean_p_value": round(float(np.mean(ack_p_values)), 6),
        }
    if mcnemar_fg_vs_ack:
        output["mcnemar_fg_vs_ack"] = mcnemar_fg_vs_ack

    summary = {"random_mean": round(mean_acc, 4)}
    if fg_result:
        summary["fg_accuracy"] = fg_result["accuracy"]
        summary["fg_vs_random_delta_pp"] = round((fg_result["accuracy"] - mean_acc) * 100, 2)
    if ack_result:
        summary["ack_accuracy"] = ack_result["accuracy"]
        summary["ack_vs_random_delta_pp"] = round((ack_result["accuracy"] - mean_acc) * 100, 2)
    if fg_result and ack_result:
        summary["fg_vs_ack_delta_pp"] = round((fg_result["accuracy"] - ack_result["accuracy"]) * 100, 2)
        summary["fg_dominates_random"] = fg_result["accuracy"] > mean_acc
        summary["ack_dominates_random"] = ack_result["accuracy"] > mean_acc

    output["summary"] = summary
    output["config"] = {
        "model": cfg["model"]["name"],
        "api_base": cfg["model"]["api_base"],
        "max_rounds": cfg["trace_collection"].get("max_rounds", 6),
        "placeholder": PLACEHOLDER,
    }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info("Multi-trial results saved to %s", args.output)


def e2e_pos_matched_main(args):
    """Position-matched random: random sampling weighted by ack position distribution."""
    import numpy as np
    _raise_fd_limit()

    cfg = load_config(args.config)
    llm_config = build_llm_config(cfg)
    domain = cfg.get("data", {}).get("source", "gsm8k")

    traces_path = os.path.join(args.traces_dir, "traces.jsonl")
    annotations = load_annotations(args.annotations_dir)
    logger.info("Loaded %d annotation labels", len(annotations))

    all_tasks = load_traces(traces_path)
    if args.task_offset:
        all_tasks = all_tasks[args.task_offset:]
    if args.num_tasks and args.num_tasks < len(all_tasks):
        all_tasks = all_tasks[:args.num_tasks]
    logger.info("Using %d tasks (offset=%d, domain=%s)",
                len(all_tasks), args.task_offset, domain)

    baseline_correct = sum(1 for t in all_tasks if t.get("is_correct"))
    baseline = {
        "correct": baseline_correct, "total": len(all_tasks),
        "accuracy": round(baseline_correct / len(all_tasks), 4) if all_tasks else 0,
    }

    ack_types = {"acknowledgment"}

    # Compute position weights from ack annotations
    pos_weights = compute_ack_position_weights(all_tasks, annotations)
    logger.info("Ack position weights: %s", pos_weights)

    # Run ack_only once
    logger.info("Running ack_only strategy...")
    ack_result = run_e2e_strategy(
        all_tasks, annotations, ack_types, cfg, llm_config, "ack_only",
        domain=domain,
    )
    logger.info("Ack-only: %.1f%%", ack_result["accuracy"] * 100)

    # Run position-matched random with multiple seeds
    n_trials = args.random_trials
    seed_base = 200
    trial_results = []
    mcnemar_ack_vs_rand = []

    for trial in range(n_trials):
        seed = seed_base + trial
        logger.info("Pos-matched random trial %d/%d (seed=%d)...", trial + 1, n_trials, seed)
        rand_result = run_e2e_strategy(
            all_tasks, annotations, ack_types, cfg, llm_config,
            f"pos_matched_seed{seed}", random_seed=seed, domain=domain,
            position_weights=pos_weights,
        )
        trial_results.append(rand_result)

        mc_ack = mcnemar_test(ack_result["per_task"], rand_result["per_task"])
        mcnemar_ack_vs_rand.append(mc_ack)
        logger.info("  accuracy=%.1f%%, McNemar ack vs pos_matched p=%.4f",
                    rand_result["accuracy"] * 100, mc_ack["p_value"])

    accs = [r["accuracy"] for r in trial_results]
    mean_acc = float(np.mean(accs))
    std_acc = float(np.std(accs, ddof=1)) if n_trials > 1 else 0.0
    ci_95 = 1.96 * std_acc / np.sqrt(n_trials) if n_trials > 1 else 0.0
    ack_p_values = [m["p_value"] for m in mcnemar_ack_vs_rand]

    output = {
        "mode": "e2e_pos_matched",
        "num_tasks": len(all_tasks),
        "n_trials": n_trials,
        "baseline": baseline,
        "ack_position_weights": {str(k): round(v, 4) for k, v in sorted(pos_weights.items())},
        "ack_only": {
            "accuracy": ack_result["accuracy"],
            "correct": ack_result["correct"],
            "total": ack_result["total"],
            "prune_pct": ack_result["prune_pct"],
        },
        "pos_matched_random": {
            "seeds": [seed_base + i for i in range(n_trials)],
            "accuracies": [round(a, 4) for a in accs],
            "mean_accuracy": round(mean_acc, 4),
            "std_accuracy": round(std_acc, 4),
            "ci_95_lower": round(mean_acc - ci_95, 4),
            "ci_95_upper": round(mean_acc + ci_95, 4),
        },
        "mcnemar_ack_vs_pos_matched": {
            "per_trial": mcnemar_ack_vs_rand,
            "p_values": [round(p, 6) for p in ack_p_values],
            "any_significant_005": any(p < 0.05 for p in ack_p_values),
            "mean_p_value": round(float(np.mean(ack_p_values)), 6),
        },
        "summary": {
            "ack_accuracy": ack_result["accuracy"],
            "pos_matched_random_mean": round(mean_acc, 4),
            "ack_vs_pos_matched_delta_pp": round((ack_result["accuracy"] - mean_acc) * 100, 2),
            "ack_dominates_pos_matched": ack_result["accuracy"] > mean_acc,
        },
        "config": {
            "model": cfg["model"]["name"],
            "api_base": cfg["model"]["api_base"],
            "max_rounds": cfg["trace_collection"].get("max_rounds", 6),
            "placeholder": PLACEHOLDER,
        },
    }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info("Position-matched results saved to %s", args.output)


# ---------------------------------------------------------------------------
# Offline simulation (original functionality, kept as upper-bound reference)
# ---------------------------------------------------------------------------

def evaluate_accuracy(traces_path: str, domain: str = "gsm8k") -> dict:
    """Compute accuracy from a traces JSONL file."""
    correct = 0
    total = 0
    with open(traces_path) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            total += 1
            if rec.get("is_correct"):
                correct += 1
    return {"correct": correct, "total": total, "accuracy": correct / total if total > 0 else 0}


def compute_token_stats(traces_path: str, annotations: dict[str, str]) -> dict:
    """Compute per-function token stats from traces + annotations."""
    stats = defaultdict(lambda: {"msg_count": 0, "total_words": 0})
    total_words = 0

    with open(traces_path) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            task_id = rec["task_id"]
            for msg in rec.get("messages", []):
                rnd = msg.get("round", 0)
                if rnd == 0:
                    continue
                key = f"{task_id}_r{rnd}"
                fn_type = annotations.get(key, "unknown")
                words = len(msg.get("content", "").split())
                stats[fn_type]["msg_count"] += 1
                stats[fn_type]["total_words"] += words
                total_words += words

    result = {}
    for fn_type, s in stats.items():
        result[fn_type] = {
            "msg_count": s["msg_count"],
            "total_words": s["total_words"],
            "est_tokens": int(s["total_words"] * 1.3),
            "word_share_pct": round(s["total_words"] / total_words * 100, 2) if total_words > 0 else 0,
        }
    result["_total_words"] = total_words
    result["_total_est_tokens"] = int(total_words * 1.3)
    return result


def simulate_function_pruning(traces_path: str, annotations: dict[str, str],
                               prune_types: list[str], domain: str = "gsm8k") -> dict:
    """Simulate pruning by removing messages of given types and re-extracting answers."""
    correct = 0
    total = 0
    pruned_words = 0
    total_words = 0

    with open(traces_path) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            task_id = rec["task_id"]
            ground_truth = rec["ground_truth"]
            total += 1

            remaining_msgs = []
            for msg in rec.get("messages", []):
                rnd = msg.get("round", 0)
                content = msg.get("content", "")
                words = len(content.split())
                total_words += words

                if rnd == 0:
                    remaining_msgs.append(msg)
                    continue

                key = f"{task_id}_r{rnd}"
                fn_type = annotations.get(key, "unknown")
                if fn_type in prune_types:
                    pruned_words += words
                else:
                    remaining_msgs.append(msg)

            final_answer = None
            for msg in reversed(remaining_msgs):
                final_answer = _extract_answer_for_domain(msg.get("content", ""), domain)
                if final_answer is not None:
                    break

            if _check_answer_for_domain(final_answer, ground_truth, domain):
                correct += 1

    accuracy = correct / total if total > 0 else 0
    token_savings = pruned_words / total_words * 100 if total_words > 0 else 0

    return {
        "pruned_types": prune_types,
        "correct": correct,
        "total": total,
        "accuracy": round(accuracy, 4),
        "pruned_words": pruned_words,
        "total_words": total_words,
        "token_savings_pct": round(token_savings, 2),
    }


def simulate_random_pruning(traces_path: str, annotations: dict[str, str],
                             target_prune_pct: float, n_trials: int = 10,
                             seed_base: int = 42, domain: str = "gsm8k") -> dict:
    """Simulate random pruning at a target percentage, averaged over n_trials."""
    all_msg_keys = []
    with open(traces_path) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            task_id = rec["task_id"]
            for msg in rec.get("messages", []):
                rnd = msg.get("round", 0)
                if rnd > 0:
                    all_msg_keys.append(f"{task_id}_r{rnd}")

    n_to_prune = int(len(all_msg_keys) * target_prune_pct / 100)

    trial_results = []
    for trial in range(n_trials):
        rng = random.Random(seed_base + trial)
        pruned_keys = set(rng.sample(all_msg_keys, min(n_to_prune, len(all_msg_keys))))

        correct = 0
        total = 0
        pruned_words = 0
        total_words = 0

        with open(traces_path) as f:
            for line in f:
                if not line.strip():
                    continue
                rec = json.loads(line)
                task_id = rec["task_id"]
                ground_truth = rec["ground_truth"]
                total += 1

                remaining_msgs = []
                for msg in rec.get("messages", []):
                    rnd = msg.get("round", 0)
                    content = msg.get("content", "")
                    words = len(content.split())
                    total_words += words

                    if rnd == 0:
                        remaining_msgs.append(msg)
                        continue

                    key = f"{task_id}_r{rnd}"
                    if key in pruned_keys:
                        pruned_words += words
                    else:
                        remaining_msgs.append(msg)

                final_answer = None
                for msg in reversed(remaining_msgs):
                    final_answer = _extract_answer_for_domain(msg.get("content", ""), domain)
                    if final_answer is not None:
                        break

                if _check_answer_for_domain(final_answer, ground_truth, domain):
                    correct += 1

        accuracy = correct / total if total > 0 else 0
        token_savings = pruned_words / total_words * 100 if total_words > 0 else 0
        trial_results.append({"accuracy": accuracy, "token_savings_pct": token_savings})

    import numpy as np
    accs = [t["accuracy"] for t in trial_results]
    savings = [t["token_savings_pct"] for t in trial_results]

    return {
        "target_prune_pct": target_prune_pct,
        "n_trials": n_trials,
        "accuracy_mean": round(float(np.mean(accs)), 4),
        "accuracy_std": round(float(np.std(accs)), 4),
        "token_savings_mean": round(float(np.mean(savings)), 2),
        "token_savings_std": round(float(np.std(savings)), 2),
    }


def simulate_main(args):
    """Offline simulation main (original functionality)."""
    traces_path = os.path.join(args.traces_dir, "traces.jsonl")
    annotations = load_annotations(args.annotations_dir)
    domain = getattr(args, "domain", "gsm8k")
    logger.info("Loaded %d annotation labels (domain=%s)", len(annotations), domain)

    baseline = evaluate_accuracy(traces_path)
    logger.info("Baseline accuracy: %d/%d = %.1f%%",
                baseline["correct"], baseline["total"], baseline["accuracy"] * 100)

    token_stats = compute_token_stats(traces_path, annotations)

    function_types = ["acknowledgment", "information_provision", "reasoning_guidance",
                      "verification", "coordination"]

    single_prune = {}
    for fn in function_types:
        result = simulate_function_pruning(traces_path, annotations, [fn], domain=domain)
        single_prune[fn] = result
        logger.info("Prune %s: accuracy=%.1f%% (Δ=%.1f%%), savings=%.1f%%",
                    fn, result["accuracy"] * 100,
                    (result["accuracy"] - baseline["accuracy"]) * 100,
                    result["token_savings_pct"])

    combo_scenarios = [
        ["information_provision", "verification"],
        ["information_provision", "reasoning_guidance"],
        ["information_provision", "coordination"],
        ["acknowledgment", "information_provision"],
        ["reasoning_guidance", "information_provision", "verification"],
        ["acknowledgment", "information_provision", "reasoning_guidance"],
    ]
    combo_prune = {}
    for combo in combo_scenarios:
        key = "+".join(sorted(combo))
        result = simulate_function_pruning(traces_path, annotations, combo, domain=domain)
        combo_prune[key] = result

    all_fn_savings = {fn: single_prune[fn]["token_savings_pct"] for fn in function_types}
    random_results = {}
    for pct in sorted(set([10, 20, 30, 40, 50] +
                          [round(v) for v in all_fn_savings.values() if v > 0])):
        if pct <= 0 or pct > 90:
            continue
        result = simulate_random_pruning(traces_path, annotations, pct,
                                          n_trials=args.random_trials, domain=domain)
        random_results[str(pct)] = result

    output = {
        "mode": "simulate",
        "baseline": baseline,
        "token_stats": token_stats,
        "function_guided": {"single_type": single_prune, "combinations": combo_prune},
        "random_baseline": random_results,
        "dominance_analysis": {},
    }

    for fn in function_types:
        fn_savings = single_prune[fn]["token_savings_pct"]
        fn_acc = single_prune[fn]["accuracy"]
        closest_random_pct = str(min(
            [int(k) for k in random_results.keys()],
            key=lambda x: abs(x - fn_savings),
        )) if random_results else None

        if closest_random_pct and closest_random_pct in random_results:
            rand_acc = random_results[closest_random_pct]["accuracy_mean"]
            output["dominance_analysis"][fn] = {
                "fn_savings_pct": fn_savings,
                "fn_accuracy": fn_acc,
                "random_savings_pct": random_results[closest_random_pct]["token_savings_mean"],
                "random_accuracy": rand_acc,
                "function_advantage_pp": round((fn_acc - rand_acc) * 100, 2),
                "dominates_random": fn_acc >= rand_acc,
            }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info("Simulation results saved to %s", args.output)


# ---------------------------------------------------------------------------
# Online pruning: real-time ack detection during live conversation
# ---------------------------------------------------------------------------


def _load_distilbert_for_online(checkpoint_path: str):
    """Load DistilBERT ack classifier for online pruning.

    Args:
        checkpoint_path: Path to fine-tuned checkpoint directory.

    Returns:
        Tuple of (model, tokenizer, device) or None if loading fails.
    """
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer

    tokenizer_path = checkpoint_path
    if not os.path.exists(os.path.join(checkpoint_path, "tokenizer_config.json")):
        tokenizer_path = os.path.dirname(checkpoint_path.rstrip("/"))
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
    model = AutoModelForSequenceClassification.from_pretrained(checkpoint_path)
    model.eval()
    device = "cpu"
    model.to(device)
    logger.info("DistilBERT loaded from %s (tokenizer=%s, device=%s)",
                checkpoint_path, tokenizer_path, device)
    return (model, tokenizer, device)


def _distilbert_is_ack(distilbert_model, content: str) -> bool:
    """Classify a single message as ack (1) or non-ack (0) using DistilBERT.

    Args:
        distilbert_model: Tuple of (model, tokenizer, device).
        content: Message text.

    Returns:
        True if the message is classified as ack.
    """
    import torch
    model, tokenizer, device = distilbert_model
    inputs = tokenizer(
        content, padding=True, truncation=True,
        max_length=256, return_tensors="pt",
    ).to(device)
    with torch.no_grad():
        logits = model(**inputs).logits
    return torch.argmax(logits, dim=-1).item() == 1


def run_online_pruned_pipeline(
    question: str,
    cfg: dict,
    char_threshold: int = 30,
    max_rounds: int = 6,
    backbone: str = "qwen",
    pruning_mode: str = "skip",
    detection_mode: str = "heuristic",
    oracle_client=None,
    oracle_model: str = "gpt-4o",
    task_id: str = "",
    random_suppress_rate: float = 0.0,
    distilbert_model=None,
    ack_prune_rate: float = 1.0,
) -> tuple[list[dict], list[int], list[dict]]:
    """Run round_robin pipeline with real-time ack suppression.

    Uses direct LLM API calls to implement true online pruning: each agent
    generates normally, and if its output is detected as ack (heuristic_is_ack),
    the message is NOT added to the conversation context for subsequent agents.

    Returns (all_messages, suppressed_rounds, oracle_decisions).
    """
    from openai import OpenAI
    import httpx as _httpx_local

    agents_cfg = cfg["agents"]
    if isinstance(agents_cfg, list):
        agent_list = agents_cfg
    else:
        agent_list = list(agents_cfg.values())

    model_cfg = cfg["model"]
    _http_timeout = float(model_cfg.get("timeout", 60))
    client = OpenAI(base_url=model_cfg["api_base"], api_key=[REDACTED]"api_key"],
                    timeout=_httpx_local.Timeout(_http_timeout, connect=10.0))

    agent_names = [a["name"] for a in agent_list]
    n_agents = len(agent_list)

    all_messages = [{
        "sender": agent_names[0],
        "receiver": agent_names[1 % n_agents],
        "content": question,
        "round": 0,
    }]
    visible_msgs = []
    suppressed_rounds = []
    oracle_decisions = []

    extra_body = {}
    if "stop" in model_cfg:
        extra_body["stop"] = model_cfg["stop"]

    for round_idx in range(1, max_rounds):
        agent_idx = round_idx % n_agents
        agent = agent_list[agent_idx]

        oai_messages = [{"role": "system", "content": agent["system_message"]}]
        oai_messages.append({"role": "user", "content": question})
        for vm in visible_msgs:
            role = "assistant" if vm["sender"] == agent["name"] else "user"
            oai_messages.append({"role": role, "content": vm["content"]})

        response = client.chat.completions.create(
            model=model_cfg["name"],
            messages=oai_messages,
            temperature=model_cfg.get("temperature", 0),
            top_p=model_cfg.get("top_p", 1.0),
            max_tokens=model_cfg.get("max_tokens", 2048),
            extra_body=extra_body if extra_body else None,
            timeout=_http_timeout,
        )
        content = response.choices[0].message.content or ""

        receiver_idx = (agent_idx + 1) % n_agents
        msg = {
            "sender": agent_names[agent_idx],
            "receiver": agent_names[receiver_idx],
            "content": content,
            "round": round_idx,
        }
        all_messages.append(msg)

        prev_content = visible_msgs[-1]["content"] if visible_msgs else ""
        if pruning_mode == "none":
            is_ack = False
        elif detection_mode == "random":
            import random as _rnd
            is_ack = _rnd.random() < random_suppress_rate
        elif detection_mode == "oracle_fg" and oracle_client is not None:
            decision = oracle_5class_is_ack(
                oracle_client, oracle_model, content, prev_content,
                task_id=task_id, round_idx=round_idx,
            )
            is_ack = decision.get("function_type", "") in ("reasoning_guidance", "verification")
            oracle_decisions.append(decision)
        elif detection_mode == "oracle_5class" and oracle_client is not None:
            decision = oracle_5class_is_ack(
                oracle_client, oracle_model, content, prev_content,
                task_id=task_id, round_idx=round_idx,
            )
            is_ack = decision["is_ack"]
            oracle_decisions.append(decision)
        elif detection_mode == "oracle" and oracle_client is not None:
            decision = oracle_is_ack(
                oracle_client, oracle_model, content, prev_content,
                task_id=task_id, round_idx=round_idx,
            )
            is_ack = decision["is_ack"]
            oracle_decisions.append(decision)
        elif detection_mode == "length_only":
            is_ack = len(content.strip()) < char_threshold
        elif detection_mode == "distilbert" and distilbert_model is not None:
            is_ack = _distilbert_is_ack(distilbert_model, content)
        elif backbone == "llama":
            is_ack = heuristic_is_ack_llama(content, prev_content)
        else:
            is_ack = heuristic_is_ack(content, char_threshold)

        if is_ack:
            do_suppress = (ack_prune_rate >= 1.0 or
                           (ack_prune_rate > 0 and
                            hash(f"{task_id}_{round_idx}_prune") % 10000 / 10000.0 < ack_prune_rate))
            if do_suppress:
                suppressed_rounds.append(round_idx)
                if pruning_mode == "detect_only":
                    visible_msgs.append(msg)
                elif pruning_mode == "placeholder":
                    placeholder_msg = dict(msg, content=PLACEHOLDER)
                    visible_msgs.append(placeholder_msg)
            else:
                visible_msgs.append(msg)
        else:
            visible_msgs.append(msg)

    return all_messages, suppressed_rounds, oracle_decisions


def online_main(args):
    """Online pruning: run live conversations with real-time ack suppression."""
    import time as _time
    _raise_fd_limit()

    # Load precomputed oracle cache if provided
    global _oracle_cache
    oracle_cache_path = getattr(args, "oracle_cache", None)
    if oracle_cache_path:
        _oracle_cache = load_oracle_cache(oracle_cache_path)
        logger.info("Loaded oracle cache: %d entries from %s", len(_oracle_cache), oracle_cache_path)

    cfg = load_config(args.config)
    if getattr(args, "data_seed", None) is not None:
        cfg["data"]["seed"] = args.data_seed
    domain = cfg.get("data", {}).get("source", "gsm8k")
    max_rounds = cfg["trace_collection"].get("max_rounds", 6)
    char_threshold = getattr(args, "char_threshold", 30)
    pruning_mode = getattr(args, "pruning_mode", "skip")
    model_name = cfg["model"]["name"].lower()
    backbone = "llama" if "llama" in model_name else "qwen"
    detection_mode = getattr(args, "detection_mode", "heuristic")

    distilbert_model = None
    if detection_mode == "distilbert":
        ckpt = getattr(args, "distilbert_checkpoint",
                        "artifacts/classifier/distilbert_ack/checkpoint-810")
        distilbert_model = _load_distilbert_for_online(ckpt)

    oracle_client = None
    oracle_model_name = os.environ.get("ORACLE_MODEL") or getattr(args, "openai_model", "gpt-4o")
    if detection_mode in ("oracle", "oracle_5class"):
        api_key = [REDACTED], "openai_api_key", None) or os.environ.get("OPENAI_API_KEY")
        if not api_key and not oracle_cache_path:
            raise SystemExit("--openai-api-key or OPENAI_API_KEY env var required for oracle/oracle_5class mode (or use --oracle-cache)")
        if api_key:
            from openai import OpenAI as _OracleOpenAI
            import httpx as _httpx
            _oracle_timeout = float(os.environ.get("ORACLE_TIMEOUT", 120))
            _oracle_base = os.environ.get("ORACLE_BASE_URL")
            _client_kw = {"api_key": [REDACTED], "timeout": _httpx.Timeout(_oracle_timeout, connect=10.0)}
            if _oracle_base:
                _client_kw["base_url"] = _oracle_base
            oracle_client = _OracleOpenAI(**_client_kw)

    if args.traces_dir:
        traces_path = os.path.join(args.traces_dir, "traces.jsonl")
        all_tasks = load_traces(traces_path)
        if args.task_offset:
            all_tasks = all_tasks[args.task_offset:]
        if args.num_tasks and args.num_tasks < len(all_tasks):
            all_tasks = all_tasks[:args.num_tasks]
    else:
        num = args.num_tasks or cfg["data"].get("num_tasks", 100)
        cfg_copy = json.loads(json.dumps(cfg))
        cfg_copy["data"]["num_tasks"] = num
        raw_tasks, _ = load_dataset_from_config(cfg_copy)
        all_tasks = []
        for idx, item in enumerate(raw_tasks[:num]):
            all_tasks.append({
                "task_id": f"{domain}_{idx:04d}",
                "question": _format_question_for_domain(item, domain),
                "ground_truth": extract_ground_truth(item["answer"]) if domain == "gsm8k" else item.get("ground_truth", item.get("answer", "")),
            })
    logger.info("Online pruning: %d tasks, domain=%s, char_threshold=%d, pruning_mode=%s, detection=%s",
                len(all_tasks), domain, char_threshold, pruning_mode, detection_mode)

    baseline_correct = 0
    pruned_correct = 0
    total = 0
    total_suppressed = 0
    total_agent_rounds = 0
    per_task = []
    t_start = _time.time()

    for idx, task_rec in enumerate(all_tasks):
        task_id = task_rec["task_id"]
        question = task_rec["question"]
        ground_truth = task_rec["ground_truth"]
        total += 1

        # --- Baseline run (no suppression) ---
        try:
            bl_msgs, _, _ = run_online_pruned_pipeline(
                question, cfg,
                char_threshold=char_threshold, max_rounds=max_rounds,
                pruning_mode="none",
                backbone=backbone,
                task_id=task_id,
            )
        except Exception as exc:
            if _is_infra_error(exc):
                logger.warning("Infrastructure error on %s (skipped): %s", task_id, exc)
                per_task.append({"task_id": task_id, "skipped": True, "infra_error": True, "skip_reason": type(exc).__name__})
                continue
            logger.exception("Baseline failed on %s", task_id)
            per_task.append({"task_id": task_id, "baseline_correct": False,
                             "pruned_correct": False, "suppressed": 0})
            continue
        finally:
            gc.collect()

        bl_answer = None
        for msg in reversed(bl_msgs):
            content = msg.get("content", "")
            bl_answer = _extract_answer_for_domain(content, domain)
            if bl_answer is not None:
                break
        bl_is_correct = _check_answer_for_domain(bl_answer, ground_truth, domain)
        if bl_is_correct:
            baseline_correct += 1

        # --- Pruned run ---
        try:
            messages, suppressed_rounds, task_oracle_decs = run_online_pruned_pipeline(
                question, cfg,
                char_threshold=char_threshold, max_rounds=max_rounds,
                pruning_mode=pruning_mode,
                backbone=backbone,
                detection_mode=detection_mode,
                oracle_client=oracle_client,
                oracle_model=oracle_model_name,
                task_id=task_id,
                distilbert_model=distilbert_model,
                ack_prune_rate=getattr(args, 'ack_prune_rate', 1.0),
            )
        except Exception as exc:
            if _is_infra_error(exc):
                logger.warning("Infrastructure error on %s (skipped): %s", task_id, exc)
                per_task.append({"task_id": task_id, "skipped": True, "infra_error": True, "skip_reason": type(exc).__name__})
                continue
            logger.exception("Online pruning failed on %s", task_id)
            per_task.append({"task_id": task_id, "baseline_correct": bl_is_correct,
                             "pruned_correct": False, "suppressed": 0})
            continue
        finally:
            gc.collect()

        agent_msgs = [m for m in messages if m.get("round", 0) > 0]
        n_suppressed = len(suppressed_rounds)
        total_suppressed += n_suppressed
        total_agent_rounds += len(agent_msgs)

        final_answer = None
        for msg in reversed(messages):
            content = msg.get("content", "")
            if content == PLACEHOLDER:
                continue
            final_answer = _extract_answer_for_domain(content, domain)
            if final_answer is not None:
                break

        is_correct = _check_answer_for_domain(final_answer, ground_truth, domain)
        if is_correct:
            pruned_correct += 1
        task_result = {
            "task_id": task_id,
            "baseline_correct": bl_is_correct,
            "pruned_correct": is_correct,
            "suppressed": n_suppressed,
            "suppressed_rounds": suppressed_rounds,
            "total_agent_msgs": len(agent_msgs),
            "final_answer": str(final_answer),
            "baseline_answer": str(bl_answer),
        }
        if task_oracle_decs:
            task_result["oracle_decisions"] = task_oracle_decs
        per_task.append(task_result)

        logger.info("[online] %d/%d task=%s baseline=%s pruned=%s suppressed=%d/%d",
                    idx + 1, len(all_tasks), task_id,
                    bl_is_correct, is_correct,
                    n_suppressed, len(agent_msgs))

    elapsed = _time.time() - t_start
    completed_tasks = [t for t in per_task if not t.get("skipped")]
    skipped_tasks = [t for t in per_task if t.get("skipped")]
    infra_error_tasks = [t for t in per_task if t.get("infra_error")]
    total_completed = len(completed_tasks)
    total_skipped = len(skipped_tasks)
    total_infra_errors = len(infra_error_tasks)
    bl_accuracy = baseline_correct / total_completed if total_completed > 0 else 0
    pr_accuracy = pruned_correct / total_completed if total_completed > 0 else 0
    suppress_pct = total_suppressed / total_agent_rounds * 100 if total_agent_rounds > 0 else 0

    output = {
        "mode": "online_pruning",
        "pruning_mode": pruning_mode,
        "detection_mode": detection_mode,
        "char_threshold": char_threshold,
        "ack_prune_rate": getattr(args, "ack_prune_rate", 1.0),
        "num_tasks": len(all_tasks),
        "total_attempted": len(per_task),
        "total_completed": total_completed,
        "total_skipped": total_skipped,
        "total_infra_errors": total_infra_errors,
        "baseline": {
            "correct": baseline_correct,
            "total": total_completed,
            "accuracy": round(bl_accuracy, 4),
        },
        "online_pruned": {
            "correct": pruned_correct,
            "total": total_completed,
            "accuracy": round(pr_accuracy, 4),
            "total_suppressed_msgs": total_suppressed,
            "total_agent_rounds": total_agent_rounds,
            "suppress_pct": round(suppress_pct, 2),
        },
        "delta_pp": round((pr_accuracy - bl_accuracy) * 100, 2),
        "elapsed_seconds": round(elapsed, 1),
        "per_task": per_task,
        "config": {
            "model": cfg["model"]["name"],
            "api_base": cfg["model"]["api_base"],
            "max_rounds": max_rounds,
        },
    }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info("Online pruning results saved to %s", args.output)
    logger.info("Completed: %d/%d (skipped: %d, infra_errors: %d) | Baseline: %.1f%% | Online-pruned: %.1f%% | Delta: %+.1fpp | Suppress: %.1f%% | Time: %.0fs",
                total_completed, len(per_task), total_skipped, total_infra_errors,
                bl_accuracy * 100, pr_accuracy * 100,
                (pr_accuracy - bl_accuracy) * 100, suppress_pct, elapsed)


def online_oracle_main(args):
    """Paired baseline + oracle-pruned experiment.

    For each task, runs both:
      1. Baseline (pruning_mode=none) — no suppression
      2. Oracle-pruned (detection_mode=oracle_5class, pruning_mode=skip)
    Produces paired per-task results and McNemar test.
    """
    if getattr(args, "detection_mode", "heuristic") == "heuristic":
        args.detection_mode = "oracle_5class"
        logger.info("online_oracle mode: detection_mode defaulted to oracle_5class")
    _raise_fd_limit()

    # Load precomputed oracle cache if provided
    global _oracle_cache
    oracle_cache_path = getattr(args, "oracle_cache", None)
    if oracle_cache_path:
        _oracle_cache = load_oracle_cache(oracle_cache_path)
        logger.info("Loaded oracle cache: %d entries from %s", len(_oracle_cache), oracle_cache_path)

    cfg = load_config(args.config)
    if getattr(args, "data_seed", None) is not None:
        cfg["data"]["seed"] = args.data_seed
    domain = cfg.get("data", {}).get("source", "gsm8k")
    max_rounds = cfg["trace_collection"].get("max_rounds", 6)
    model_name = cfg["model"]["name"].lower()
    backbone = "llama" if "llama" in model_name else "qwen"

    # Oracle client setup (optional when cache is loaded)
    oracle_client = None
    oracle_base_url = getattr(args, "oracle_base_url", None) or os.environ.get("ORACLE_BASE_URL")
    api_key = [REDACTED], "openai_api_key", None) or os.environ.get("OPENAI_API_KEY")
    if not api_key and not oracle_base_url and not oracle_cache_path:
        raise SystemExit("--openai-api-key or OPENAI_API_KEY env var required for online_oracle mode (or use --oracle-base-url for local vLLM, or --oracle-cache for precomputed labels)")
    if api_key or oracle_base_url:
        from openai import OpenAI as _OracleOpenAI
        import httpx as _httpx
        _oracle_timeout = float(os.environ.get("ORACLE_TIMEOUT", 120))
        client_kwargs = {"api_key": [REDACTED] or "dummy", "timeout": _httpx.Timeout(_oracle_timeout, connect=10.0)}
        if oracle_base_url:
            client_kwargs["base_url"] = oracle_base_url
        oracle_client = _OracleOpenAI(**client_kwargs)
    oracle_model_name = os.environ.get("ORACLE_MODEL") or getattr(args, "openai_model", "gpt-4o")

    # Load tasks
    if args.traces_dir:
        traces_path = os.path.join(args.traces_dir, "traces.jsonl")
        all_tasks = load_traces(traces_path)
        if args.task_offset:
            all_tasks = all_tasks[args.task_offset:]
        if args.num_tasks and args.num_tasks < len(all_tasks):
            all_tasks = all_tasks[:args.num_tasks]
    else:
        num = args.num_tasks or cfg["data"].get("num_tasks", 100)
        total_needed = num + (args.task_offset or 0)
        cfg_copy = json.loads(json.dumps(cfg))
        cfg_copy["data"]["num_tasks"] = total_needed
        raw_tasks, _ = load_dataset_from_config(cfg_copy)
        all_tasks = []
        for idx, item in enumerate(raw_tasks[:total_needed]):
            all_tasks.append({
                "task_id": f"{domain}_{idx:04d}",
                "question": _format_question_for_domain(item, domain),
                "ground_truth": extract_ground_truth(item["answer"]) if domain == "gsm8k" else item.get("ground_truth", item.get("answer", "")),
            })
        if args.task_offset:
            all_tasks = all_tasks[args.task_offset:]
        if args.num_tasks and args.num_tasks < len(all_tasks):
            all_tasks = all_tasks[:args.num_tasks]

    logger.info("Online oracle: %d tasks, domain=%s, backbone=%s, oracle_model=%s",
                len(all_tasks), domain, backbone, oracle_model_name)

    partial_path = args.output.replace(".json", "_partial.json")
    baseline_correct = 0
    oracle_correct = 0
    total = 0
    total_suppressed = 0
    total_agent_rounds = 0
    total_oracle_tokens = 0
    per_task = []
    completed_task_ids = set()

    if os.path.exists(partial_path):
        with open(partial_path) as _pf:
            _partial = json.load(_pf)
        per_task = _partial.get("per_task", [])
        completed_task_ids = {r["task_id"] for r in per_task}
        baseline_correct = _partial.get("baseline_correct", 0)
        oracle_correct = _partial.get("oracle_correct", 0)
        total = _partial.get("total", 0)
        total_suppressed = _partial.get("total_suppressed", 0)
        total_agent_rounds = _partial.get("total_agent_rounds", 0)
        total_oracle_tokens = _partial.get("total_oracle_tokens", 0)
        logger.info("Resuming from checkpoint: %d tasks completed", len(completed_task_ids))

    t_start = time.time()

    import signal as _signal
    _task_timeout_s = int(cfg.get("model", {}).get("timeout", 60)) * 5

    class _TaskTimeout(Exception):
        pass

    def _task_alarm(signum, frame):
        raise _TaskTimeout()

    _signal.signal(_signal.SIGALRM, _task_alarm)

    for idx, task_rec in enumerate(all_tasks):
        task_id = task_rec["task_id"]
        question = task_rec["question"]
        ground_truth = task_rec["ground_truth"]

        if task_id in completed_task_ids:
            logger.info("[oracle] %d/%d task=%s SKIPPED (checkpoint)", idx + 1, len(all_tasks), task_id)
            continue

        task_success = False
        task_error = None
        task_is_infra = False
        bl_is_correct = False
        bl_answer = None
        or_is_correct = False
        or_answer = None
        or_msgs = []
        suppressed_rounds = []
        oracle_decs = []

        for _attempt in range(2):
            try:
                _signal.alarm(_task_timeout_s)

                # --- Baseline run (no suppression) ---
                try:
                    bl_msgs, _, _ = run_online_pruned_pipeline(
                        question, cfg,
                        max_rounds=max_rounds, backbone=backbone,
                        pruning_mode="none", task_id=task_id,
                    )
                finally:
                    gc.collect()

                bl_answer = None
                for msg in reversed(bl_msgs):
                    bl_answer = _extract_answer_for_domain(msg.get("content", ""), domain)
                    if bl_answer is not None:
                        break
                bl_is_correct = _check_answer_for_domain(bl_answer, ground_truth, domain)

                # --- Oracle-pruned run ---
                det_mode = getattr(args, "detection_mode", "oracle")
                try:
                    or_msgs, suppressed_rounds, oracle_decs = run_online_pruned_pipeline(
                        question, cfg,
                        max_rounds=max_rounds, backbone=backbone,
                        pruning_mode="skip",
                        detection_mode=det_mode,
                        oracle_client=oracle_client,
                        oracle_model=oracle_model_name,
                        task_id=task_id,
                    )
                finally:
                    gc.collect()

                or_answer = None
                for msg in reversed(or_msgs):
                    content = msg.get("content", "")
                    if content == PLACEHOLDER:
                        continue
                    or_answer = _extract_answer_for_domain(content, domain)
                    if or_answer is not None:
                        break
                or_is_correct = _check_answer_for_domain(or_answer, ground_truth, domain)

                _signal.alarm(0)
                task_success = True
                break
            except _TaskTimeout:
                _signal.alarm(0)
                if _attempt == 0:
                    logger.warning("[oracle] task=%s timeout after %ds, retrying", task_id, _task_timeout_s)
                    continue
                else:
                    logger.error("[oracle] task=%s timeout after retry, skipping", task_id)
                    task_error = "timeout"
                    break
            except Exception as _e:
                _signal.alarm(0)
                task_is_infra = _is_infra_error(_e)
                logger.exception("[oracle] task=%s failed (%s): %s",
                                 task_id, "infra" if task_is_infra else "task", _e)
                task_error = str(_e)
                break

        total += 1

        if not task_success:
            per_task.append({
                "task_id": task_id,
                "baseline_correct": False,
                "oracle_pruned_correct": False,
                "messages_suppressed": 0,
                "total_messages": 0,
                "oracle_decisions": [],
                "skipped": True,
                "infra_error": task_is_infra,
                "skip_reason": task_error,
            })
            logger.info("[oracle] %d/%d task=%s SKIPPED (%s)",
                        idx + 1, len(all_tasks), task_id, task_error)
        else:
            if bl_is_correct:
                baseline_correct += 1
            if or_is_correct:
                oracle_correct += 1

            agent_msgs = [m for m in or_msgs if m.get("round", 0) > 0]
            n_suppressed = len(suppressed_rounds)
            total_suppressed += n_suppressed
            total_agent_rounds += len(agent_msgs)
            total_oracle_tokens += sum(d.get("tokens", 0) for d in oracle_decs)

            per_task.append({
                "task_id": task_id,
                "question": question[:200],
                "ground_truth": str(ground_truth),
                "baseline_correct": bl_is_correct,
                "baseline_answer": str(bl_answer),
                "oracle_pruned_correct": or_is_correct,
                "oracle_pruned_answer": str(or_answer),
                "messages_suppressed": n_suppressed,
                "total_messages": len(agent_msgs),
                "oracle_decisions": oracle_decs,
            })

            logger.info("[oracle] %d/%d task=%s bl=%s oracle=%s suppressed=%d/%d",
                        idx + 1, len(all_tasks), task_id,
                        bl_is_correct, or_is_correct,
                        n_suppressed, len(agent_msgs))

        _ckpt = {
            "baseline_correct": baseline_correct, "oracle_correct": oracle_correct,
            "total": total, "total_suppressed": total_suppressed,
            "total_agent_rounds": total_agent_rounds, "total_oracle_tokens": total_oracle_tokens,
            "per_task": per_task,
        }
        os.makedirs(os.path.dirname(partial_path) or ".", exist_ok=True)
        with open(partial_path, "w") as _pf:
            json.dump(_ckpt, _pf, indent=2, ensure_ascii=False)
        logger.info("Checkpoint saved: %d tasks → %s", total, partial_path)

    _signal.alarm(0)
    _signal.signal(_signal.SIGALRM, _signal.SIG_DFL)

    elapsed = time.time() - t_start

    # --- McNemar test (exclude skipped tasks) ---
    valid_tasks = [r for r in per_task if not r.get("skipped", False)]
    n_skipped = len(per_task) - len(valid_tasks)
    n_infra_errors = sum(1 for r in per_task if r.get("infra_error"))
    n_valid = len(valid_tasks)

    a = b = c = d = 0
    for r in valid_tasks:
        bl_ok = r.get("baseline_correct", False)
        or_ok = r.get("oracle_pruned_correct", False)
        if bl_ok and or_ok:
            a += 1
        elif not bl_ok and or_ok:
            b += 1
        elif bl_ok and not or_ok:
            c += 1
        else:
            d += 1

    n_discordant = b + c
    if n_discordant == 0:
        chi2_cc = 0.0
        p_value = 1.0
    else:
        chi2_cc = (abs(b - c) - 1) ** 2 / (b + c)
        from scipy.stats import chi2 as _chi2_dist
        p_value = float(1 - _chi2_dist.cdf(chi2_cc, df=1))

    bl_acc = baseline_correct / n_valid if n_valid > 0 else 0
    or_acc = oracle_correct / n_valid if n_valid > 0 else 0
    suppress_rate = total_suppressed / total_agent_rounds * 100 if total_agent_rounds > 0 else 0

    output = {
        "mode": "online_oracle",
        "num_tasks": n_valid,
        "num_skipped": n_skipped,
        "num_infra_errors": n_infra_errors,
        "elapsed_seconds": round(elapsed, 1),
        "baseline": {
            "correct": baseline_correct,
            "total": n_valid,
            "accuracy": round(bl_acc, 4),
        },
        "oracle_pruned": {
            "correct": oracle_correct,
            "total": n_valid,
            "accuracy": round(or_acc, 4),
            "total_suppressed": total_suppressed,
            "total_agent_rounds": total_agent_rounds,
            "suppression_rate": round(suppress_rate, 2),
        },
        "delta_pp": round((or_acc - bl_acc) * 100, 2),
        "mcnemar": {
            "a_both_correct": a,
            "b_oracle_only": b,
            "c_baseline_only": c,
            "d_both_wrong": d,
            "n_discordant": n_discordant,
            "chi2_cc": round(chi2_cc, 4),
            "p_value": round(p_value, 6),
            "method": "mcnemar_chi2_cc",
            "significant_005": p_value < 0.05,
        },
        "oracle_stats": {
            "total_api_calls": sum(1 for r in per_task for _ in r.get("oracle_decisions", [])),
            "total_tokens": total_oracle_tokens,
            "avg_confidence": round(
                sum(d.get("confidence", 0) for r in per_task for d in r.get("oracle_decisions", []))
                / max(1, sum(1 for r in per_task for _ in r.get("oracle_decisions", []))),
                4,
            ),
            "oracle_model": oracle_model_name,
        },
        "per_task": per_task,
        "config": {
            "model": cfg["model"]["name"],
            "api_base": cfg["model"]["api_base"],
            "max_rounds": max_rounds,
            "backbone": backbone,
        },
    }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info("Oracle results saved to %s", args.output)
    if os.path.exists(partial_path):
        os.remove(partial_path)
        logger.info("Removed checkpoint file %s", partial_path)
    logger.info("Baseline: %.1f%% | Oracle: %.1f%% | Δ: %+.1fpp | Suppress: %.1f%% | McNemar p=%.4f | N=%d (skipped=%d) | Time: %.0fs",
                bl_acc * 100, or_acc * 100, (or_acc - bl_acc) * 100,
                suppress_rate, p_value, n_valid, n_skipped, elapsed)


# ---------------------------------------------------------------------------
# Online random token-matched pruning
# ---------------------------------------------------------------------------

def online_random_token_matched_main(args):
    """Paired baseline + random token-matched suppression experiment.

    For each task, runs:
      1. Baseline (pruning_mode=none) — no suppression
      2. Random-suppressed (detection_mode=random) — suppress messages with
         probability --random-suppress-rate (default 0.106, derived from oracle
         ack stats: 56.32% ack rate × 12/64 token ratio)

    No GPT-4o API required. Uses --data-seed for reproducibility.
    """
    _raise_fd_limit()
    import random as _rnd
    _rnd.seed(args.data_seed or 42)

    cfg = load_config(args.config)
    if getattr(args, "data_seed", None) is not None:
        cfg["data"]["seed"] = args.data_seed
    domain = cfg.get("data", {}).get("source", "gsm8k")
    max_rounds = cfg["trace_collection"].get("max_rounds", 6)
    model_name = cfg["model"]["name"].lower()
    backbone = "llama" if "llama" in model_name else "qwen"
    suppress_rate = getattr(args, "random_suppress_rate", 0.106)

    # Load tasks
    if args.traces_dir:
        traces_path = os.path.join(args.traces_dir, "traces.jsonl")
        all_tasks = load_traces(traces_path)
        if args.task_offset:
            all_tasks = all_tasks[args.task_offset:]
        if args.num_tasks and args.num_tasks < len(all_tasks):
            all_tasks = all_tasks[:args.num_tasks]
    else:
        num = args.num_tasks or cfg["data"].get("num_tasks", 100)
        total_needed = num + (args.task_offset or 0)
        cfg_copy = json.loads(json.dumps(cfg))
        cfg_copy["data"]["num_tasks"] = total_needed
        raw_tasks, _ = load_dataset_from_config(cfg_copy)
        all_tasks = []
        for idx, item in enumerate(raw_tasks[:total_needed]):
            all_tasks.append({
                "task_id": f"{domain}_{idx:04d}",
                "question": _format_question_for_domain(item, domain),
                "ground_truth": extract_ground_truth(item["answer"]) if domain == "gsm8k" else item.get("ground_truth", item.get("answer", "")),
            })
        if args.task_offset:
            all_tasks = all_tasks[args.task_offset:]
        if args.num_tasks and args.num_tasks < len(all_tasks):
            all_tasks = all_tasks[:args.num_tasks]

    logger.info("Online random token-matched: %d tasks, domain=%s, backbone=%s, suppress_rate=%.4f",
                len(all_tasks), domain, backbone, suppress_rate)

    partial_path = args.output.replace(".json", "_partial.json")
    baseline_correct = 0
    random_correct = 0
    total = 0
    total_suppressed = 0
    total_agent_rounds = 0
    per_task = []
    completed_task_ids = set()

    if os.path.exists(partial_path):
        with open(partial_path) as _pf:
            _partial = json.load(_pf)
        per_task = _partial.get("per_task", [])
        completed_task_ids = {r["task_id"] for r in per_task}
        baseline_correct = _partial.get("baseline_correct", 0)
        random_correct = _partial.get("random_correct", 0)
        total = _partial.get("total", 0)
        total_suppressed = _partial.get("total_suppressed", 0)
        total_agent_rounds = _partial.get("total_agent_rounds", 0)
        logger.info("Resuming from checkpoint: %d tasks completed", len(completed_task_ids))

    t_start = time.time()

    for idx, task_rec in enumerate(all_tasks):
        task_id = task_rec["task_id"]
        question = task_rec["question"]
        ground_truth = task_rec["ground_truth"]

        if task_id in completed_task_ids:
            logger.info("[random] %d/%d task=%s SKIPPED (checkpoint)", idx + 1, len(all_tasks), task_id)
            continue

        total += 1

        # --- Baseline run ---
        try:
            bl_msgs, _, _ = run_online_pruned_pipeline(
                question, cfg,
                max_rounds=max_rounds, backbone=backbone,
                pruning_mode="none", task_id=task_id,
            )
        except Exception as exc:
            if _is_infra_error(exc):
                logger.warning("Infrastructure error on %s (skipped): %s", task_id, exc)
                per_task.append({"task_id": task_id, "skipped": True, "infra_error": True, "skip_reason": type(exc).__name__})
                continue
            logger.exception("Baseline failed on %s", task_id)
            per_task.append({"task_id": task_id, "baseline_correct": False,
                             "random_pruned_correct": False, "messages_suppressed": 0,
                             "total_messages": 0})
            continue
        finally:
            gc.collect()

        bl_answer = None
        for msg in reversed(bl_msgs):
            bl_answer = _extract_answer_for_domain(msg.get("content", ""), domain)
            if bl_answer is not None:
                break
        bl_is_correct = _check_answer_for_domain(bl_answer, ground_truth, domain)
        if bl_is_correct:
            baseline_correct += 1

        # --- Random-suppressed run ---
        try:
            rnd_msgs, suppressed_rounds, _ = run_online_pruned_pipeline(
                question, cfg,
                max_rounds=max_rounds, backbone=backbone,
                pruning_mode="skip",
                detection_mode="random",
                random_suppress_rate=suppress_rate,
                task_id=task_id,
            )
        except Exception as exc:
            if _is_infra_error(exc):
                logger.warning("Infrastructure error on %s (skipped): %s", task_id, exc)
                per_task.append({"task_id": task_id, "skipped": True, "infra_error": True, "skip_reason": type(exc).__name__})
                continue
            logger.exception("Random-suppressed run failed on %s", task_id)
            per_task.append({"task_id": task_id, "baseline_correct": bl_is_correct,
                             "random_pruned_correct": False, "messages_suppressed": 0,
                             "total_messages": 0})
            continue
        finally:
            gc.collect()

        rnd_answer = None
        for msg in reversed(rnd_msgs):
            content = msg.get("content", "")
            if content == PLACEHOLDER:
                continue
            rnd_answer = _extract_answer_for_domain(content, domain)
            if rnd_answer is not None:
                break
        rnd_is_correct = _check_answer_for_domain(rnd_answer, ground_truth, domain)
        if rnd_is_correct:
            random_correct += 1

        agent_msgs = [m for m in rnd_msgs if m.get("round", 0) > 0]
        n_suppressed = len(suppressed_rounds)
        total_suppressed += n_suppressed
        total_agent_rounds += len(agent_msgs)

        per_task.append({
            "task_id": task_id,
            "question": question[:200],
            "ground_truth": str(ground_truth),
            "baseline_correct": bl_is_correct,
            "baseline_answer": str(bl_answer),
            "random_pruned_correct": rnd_is_correct,
            "random_pruned_answer": str(rnd_answer),
            "messages_suppressed": n_suppressed,
            "total_messages": len(agent_msgs),
        })

        logger.info("[random] %d/%d task=%s bl=%s random=%s suppressed=%d/%d",
                    idx + 1, len(all_tasks), task_id,
                    bl_is_correct, rnd_is_correct,
                    n_suppressed, len(agent_msgs))

        if total % 50 == 0:
            _ckpt = {
                "baseline_correct": baseline_correct, "random_correct": random_correct,
                "total": total, "total_suppressed": total_suppressed,
                "total_agent_rounds": total_agent_rounds,
                "per_task": per_task,
            }
            os.makedirs(os.path.dirname(partial_path) or ".", exist_ok=True)
            with open(partial_path, "w") as _pf:
                json.dump(_ckpt, _pf, indent=2, ensure_ascii=False)
            logger.info("Checkpoint saved: %d tasks → %s", total, partial_path)

    elapsed = time.time() - t_start

    # --- McNemar test (exclude skipped tasks) ---
    valid_tasks = [r for r in per_task if not r.get("skipped")]
    n_skipped = len(per_task) - len(valid_tasks)
    n_infra_errors = sum(1 for r in per_task if r.get("infra_error"))
    n_valid = len(valid_tasks)

    a = b = c = d = 0
    for r in valid_tasks:
        bl_ok = r.get("baseline_correct", False)
        rnd_ok = r.get("random_pruned_correct", False)
        if bl_ok and rnd_ok:
            a += 1
        elif not bl_ok and rnd_ok:
            b += 1
        elif bl_ok and not rnd_ok:
            c += 1
        else:
            d += 1

    n_discordant = b + c
    if n_discordant == 0:
        chi2_cc = 0.0
        p_value = 1.0
    else:
        chi2_cc = (abs(b - c) - 1) ** 2 / (b + c)
        from scipy.stats import chi2 as _chi2_dist
        p_value = float(1 - _chi2_dist.cdf(chi2_cc, df=1))

    bl_acc = baseline_correct / n_valid if n_valid > 0 else 0
    rnd_acc = random_correct / n_valid if n_valid > 0 else 0
    suppress_pct = total_suppressed / total_agent_rounds * 100 if total_agent_rounds > 0 else 0

    output = {
        "mode": "online_random_token_matched",
        "random_suppress_rate": suppress_rate,
        "num_tasks": n_valid,
        "num_skipped": n_skipped,
        "num_infra_errors": n_infra_errors,
        "elapsed_seconds": round(elapsed, 1),
        "baseline": {
            "correct": baseline_correct,
            "total": n_valid,
            "accuracy": round(bl_acc, 4),
        },
        "random_pruned": {
            "correct": random_correct,
            "total": n_valid,
            "accuracy": round(rnd_acc, 4),
            "total_suppressed": total_suppressed,
            "total_agent_rounds": total_agent_rounds,
            "suppression_rate": round(suppress_pct, 2),
        },
        "delta_pp": round((rnd_acc - bl_acc) * 100, 2),
        "mcnemar": {
            "a_both_correct": a,
            "b_random_only": b,
            "c_baseline_only": c,
            "d_both_wrong": d,
            "n_discordant": n_discordant,
            "chi2_cc": round(chi2_cc, 4),
            "p_value": round(p_value, 6),
            "method": "mcnemar_chi2_cc",
            "significant_005": p_value < 0.05,
        },
        "per_task": per_task,
        "config": {
            "model": cfg["model"]["name"],
            "api_base": cfg["model"]["api_base"],
            "max_rounds": max_rounds,
            "backbone": backbone,
            "data_seed": args.data_seed or 42,
        },
    }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info("Random token-matched results saved to %s", args.output)
    if os.path.exists(partial_path):
        os.remove(partial_path)
        logger.info("Removed checkpoint file %s", partial_path)
    logger.info("Baseline: %.1f%% | Random: %.1f%% | Δ: %+.1fpp | Suppress: %.1f%% | McNemar p=%.4f | Time: %.0fs",
                bl_acc * 100, rnd_acc * 100, (rnd_acc - bl_acc) * 100,
                suppress_pct, p_value, elapsed)


# ---------------------------------------------------------------------------
# Online function-guided pruning
# ---------------------------------------------------------------------------

def online_fg_main(args):
    """Paired baseline + function-guided (FG) pruning experiment.

    For each task, runs:
      1. Baseline (pruning_mode=none) — no suppression
      2. FG-pruned (detection_mode=oracle_fg) — suppress messages classified as
         reasoning_guidance or verification by GPT-4o 5-class oracle

    Requires GPT-4o API access (--openai-api-key or OPENAI_API_KEY).
    """
    _raise_fd_limit()

    cfg = load_config(args.config)
    if getattr(args, "data_seed", None) is not None:
        cfg["data"]["seed"] = args.data_seed
    domain = cfg.get("data", {}).get("source", "gsm8k")
    max_rounds = cfg["trace_collection"].get("max_rounds", 6)
    model_name = cfg["model"]["name"].lower()
    backbone = "llama" if "llama" in model_name else "qwen"

    # Oracle client setup
    from openai import OpenAI as _OracleOpenAI
    import httpx as _httpx
    oracle_base_url = getattr(args, "oracle_base_url", None) or os.environ.get("ORACLE_BASE_URL")
    api_key = [REDACTED], "openai_api_key", None) or os.environ.get("OPENAI_API_KEY")
    if not api_key and not oracle_base_url:
        raise SystemExit("--openai-api-key or OPENAI_API_KEY env var required for online_fg mode (or use --oracle-base-url for local vLLM)")
    _oracle_timeout = float(os.environ.get("ORACLE_TIMEOUT", 120))
    client_kwargs = {"api_key": [REDACTED] or "dummy", "timeout": _httpx.Timeout(_oracle_timeout, connect=10.0)}
    if oracle_base_url:
        client_kwargs["base_url"] = oracle_base_url
    oracle_client = _OracleOpenAI(**client_kwargs)
    oracle_model_name = os.environ.get("ORACLE_MODEL") or getattr(args, "openai_model", "gpt-4o")

    # Load tasks
    if args.traces_dir:
        traces_path = os.path.join(args.traces_dir, "traces.jsonl")
        all_tasks = load_traces(traces_path)
        if args.task_offset:
            all_tasks = all_tasks[args.task_offset:]
        if args.num_tasks and args.num_tasks < len(all_tasks):
            all_tasks = all_tasks[:args.num_tasks]
    else:
        num = args.num_tasks or cfg["data"].get("num_tasks", 100)
        total_needed = num + (args.task_offset or 0)
        cfg_copy = json.loads(json.dumps(cfg))
        cfg_copy["data"]["num_tasks"] = total_needed
        raw_tasks, _ = load_dataset_from_config(cfg_copy)
        all_tasks = []
        for idx, item in enumerate(raw_tasks[:total_needed]):
            all_tasks.append({
                "task_id": f"{domain}_{idx:04d}",
                "question": _format_question_for_domain(item, domain),
                "ground_truth": extract_ground_truth(item["answer"]) if domain == "gsm8k" else item.get("ground_truth", item.get("answer", "")),
            })
        if args.task_offset:
            all_tasks = all_tasks[args.task_offset:]
        if args.num_tasks and args.num_tasks < len(all_tasks):
            all_tasks = all_tasks[:args.num_tasks]

    logger.info("Online FG pruning: %d tasks, domain=%s, backbone=%s, oracle_model=%s",
                len(all_tasks), domain, backbone, oracle_model_name)

    partial_path = args.output.replace(".json", "_partial.json")
    baseline_correct = 0
    fg_correct = 0
    total = 0
    total_suppressed = 0
    total_agent_rounds = 0
    total_oracle_tokens = 0
    per_task = []
    completed_task_ids = set()

    if os.path.exists(partial_path):
        with open(partial_path) as _pf:
            _partial = json.load(_pf)
        per_task = _partial.get("per_task", [])
        completed_task_ids = {r["task_id"] for r in per_task}
        baseline_correct = _partial.get("baseline_correct", 0)
        fg_correct = _partial.get("fg_correct", 0)
        total = _partial.get("total", 0)
        total_suppressed = _partial.get("total_suppressed", 0)
        total_agent_rounds = _partial.get("total_agent_rounds", 0)
        total_oracle_tokens = _partial.get("total_oracle_tokens", 0)
        logger.info("Resuming from checkpoint: %d tasks completed", len(completed_task_ids))

    t_start = time.time()

    for idx, task_rec in enumerate(all_tasks):
        task_id = task_rec["task_id"]
        question = task_rec["question"]
        ground_truth = task_rec["ground_truth"]

        if task_id in completed_task_ids:
            logger.info("[fg] %d/%d task=%s SKIPPED (checkpoint)", idx + 1, len(all_tasks), task_id)
            continue

        total += 1

        # --- Baseline run ---
        try:
            bl_msgs, _, _ = run_online_pruned_pipeline(
                question, cfg,
                max_rounds=max_rounds, backbone=backbone,
                pruning_mode="none", task_id=task_id,
            )
        except Exception:
            logger.exception("Baseline failed on %s", task_id)
            per_task.append({"task_id": task_id, "baseline_correct": False,
                             "fg_pruned_correct": False, "messages_suppressed": 0,
                             "total_messages": 0, "oracle_decisions": []})
            continue
        finally:
            gc.collect()

        bl_answer = None
        for msg in reversed(bl_msgs):
            bl_answer = _extract_answer_for_domain(msg.get("content", ""), domain)
            if bl_answer is not None:
                break
        bl_is_correct = _check_answer_for_domain(bl_answer, ground_truth, domain)
        if bl_is_correct:
            baseline_correct += 1

        # --- FG-pruned run ---
        try:
            fg_msgs, suppressed_rounds, oracle_decs = run_online_pruned_pipeline(
                question, cfg,
                max_rounds=max_rounds, backbone=backbone,
                pruning_mode="skip",
                detection_mode="oracle_fg",
                oracle_client=oracle_client,
                oracle_model=oracle_model_name,
                task_id=task_id,
            )
        except Exception:
            logger.exception("FG run failed on %s", task_id)
            per_task.append({"task_id": task_id, "baseline_correct": bl_is_correct,
                             "fg_pruned_correct": False, "messages_suppressed": 0,
                             "total_messages": 0, "oracle_decisions": []})
            continue
        finally:
            gc.collect()

        fg_answer = None
        for msg in reversed(fg_msgs):
            content = msg.get("content", "")
            if content == PLACEHOLDER:
                continue
            fg_answer = _extract_answer_for_domain(content, domain)
            if fg_answer is not None:
                break
        fg_is_correct = _check_answer_for_domain(fg_answer, ground_truth, domain)
        if fg_is_correct:
            fg_correct += 1

        agent_msgs = [m for m in fg_msgs if m.get("round", 0) > 0]
        n_suppressed = len(suppressed_rounds)
        total_suppressed += n_suppressed
        total_agent_rounds += len(agent_msgs)
        total_oracle_tokens += sum(d.get("tokens", 0) for d in oracle_decs)

        per_task.append({
            "task_id": task_id,
            "question": question[:200],
            "ground_truth": str(ground_truth),
            "baseline_correct": bl_is_correct,
            "baseline_answer": str(bl_answer),
            "fg_pruned_correct": fg_is_correct,
            "fg_pruned_answer": str(fg_answer),
            "messages_suppressed": n_suppressed,
            "total_messages": len(agent_msgs),
            "oracle_decisions": oracle_decs,
        })

        logger.info("[fg] %d/%d task=%s bl=%s fg=%s suppressed=%d/%d",
                    idx + 1, len(all_tasks), task_id,
                    bl_is_correct, fg_is_correct,
                    n_suppressed, len(agent_msgs))

        if total % 50 == 0:
            _ckpt = {
                "baseline_correct": baseline_correct, "fg_correct": fg_correct,
                "total": total, "total_suppressed": total_suppressed,
                "total_agent_rounds": total_agent_rounds, "total_oracle_tokens": total_oracle_tokens,
                "per_task": per_task,
            }
            os.makedirs(os.path.dirname(partial_path) or ".", exist_ok=True)
            with open(partial_path, "w") as _pf:
                json.dump(_ckpt, _pf, indent=2, ensure_ascii=False)
            logger.info("Checkpoint saved: %d tasks → %s", total, partial_path)

    elapsed = time.time() - t_start

    # --- McNemar test ---
    a = b = c = d = 0
    for r in per_task:
        bl_ok = r.get("baseline_correct", False)
        fg_ok = r.get("fg_pruned_correct", False)
        if bl_ok and fg_ok:
            a += 1
        elif not bl_ok and fg_ok:
            b += 1
        elif bl_ok and not fg_ok:
            c += 1
        else:
            d += 1

    n_discordant = b + c
    if n_discordant == 0:
        chi2_cc = 0.0
        p_value = 1.0
    else:
        chi2_cc = (abs(b - c) - 1) ** 2 / (b + c)
        from scipy.stats import chi2 as _chi2_dist
        p_value = float(1 - _chi2_dist.cdf(chi2_cc, df=1))

    bl_acc = baseline_correct / total if total > 0 else 0
    fg_acc = fg_correct / total if total > 0 else 0
    suppress_pct = total_suppressed / total_agent_rounds * 100 if total_agent_rounds > 0 else 0

    output = {
        "mode": "online_fg",
        "num_tasks": total,
        "elapsed_seconds": round(elapsed, 1),
        "baseline": {
            "correct": baseline_correct,
            "total": total,
            "accuracy": round(bl_acc, 4),
        },
        "fg_pruned": {
            "correct": fg_correct,
            "total": total,
            "accuracy": round(fg_acc, 4),
            "total_suppressed": total_suppressed,
            "total_agent_rounds": total_agent_rounds,
            "suppression_rate": round(suppress_pct, 2),
        },
        "delta_pp": round((fg_acc - bl_acc) * 100, 2),
        "mcnemar": {
            "a_both_correct": a,
            "b_fg_only": b,
            "c_baseline_only": c,
            "d_both_wrong": d,
            "n_discordant": n_discordant,
            "chi2_cc": round(chi2_cc, 4),
            "p_value": round(p_value, 6),
            "method": "mcnemar_chi2_cc",
            "significant_005": p_value < 0.05,
        },
        "oracle_stats": {
            "total_api_calls": sum(1 for r in per_task for _ in r.get("oracle_decisions", [])),
            "total_tokens": total_oracle_tokens,
            "avg_confidence": round(
                sum(d.get("confidence", 0) for r in per_task for d in r.get("oracle_decisions", []))
                / max(1, sum(1 for r in per_task for _ in r.get("oracle_decisions", []))),
                4,
            ),
            "oracle_model": oracle_model_name,
        },
        "per_task": per_task,
        "config": {
            "model": cfg["model"]["name"],
            "api_base": cfg["model"]["api_base"],
            "max_rounds": max_rounds,
            "backbone": backbone,
        },
    }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info("FG pruning results saved to %s", args.output)
    if os.path.exists(partial_path):
        os.remove(partial_path)
        logger.info("Removed checkpoint file %s", partial_path)
    logger.info("Baseline: %.1f%% | FG: %.1f%% | Δ: %+.1fpp | Suppress: %.1f%% | McNemar p=%.4f | Time: %.0fs",
                bl_acc * 100, fg_acc * 100, (fg_acc - bl_acc) * 100,
                suppress_pct, p_value, elapsed)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Pruning validation (simulate or e2e)")
    parser.add_argument("--mode", choices=["simulate", "e2e", "e2e_random_multi", "e2e_pos_matched", "online_pruning", "online_oracle", "online_random_token_matched", "online_fg"],
                        default="simulate",
                        help="simulate=offline, e2e=full pipeline, e2e_random_multi=multi-seed, e2e_pos_matched=position-matched, online_pruning=live ack gating, online_oracle=paired baseline+oracle, online_random_token_matched=random token-matched, online_fg=function-guided pruning")
    parser.add_argument("--config", type=str, default=None,
                        help="Config YAML (required for e2e/online modes)")
    parser.add_argument("--traces-dir", default=None,
                        help="Directory containing traces.jsonl")
    parser.add_argument("--annotations-dir", default=None,
                        help="Directory containing annotations.jsonl")
    parser.add_argument("--output", default="outputs/v7_analysis/pruning_validation.json")
    parser.add_argument("--num-tasks", type=int, default=None,
                        help="Limit number of tasks (e2e mode)")
    parser.add_argument("--task-offset", type=int, default=0,
                        help="Skip first N tasks before applying --num-tasks")
    parser.add_argument("--random-trials", type=int, default=10,
                        help="Number of random trials (simulate mode)")
    parser.add_argument("--strategy",
                        choices=["all", "function_guided", "ack_only", "random"],
                        default="all",
                        help="Which e2e strategy to run (default: all)")
    parser.add_argument("--random-ref", choices=["fg", "ack"], default="fg",
                        help="Random prune count matches fg or ack (default: fg)")
    parser.add_argument("--random-seed-start", type=int, default=None,
                        help="Override seed_base for e2e_random_multi (default: 100)")
    parser.add_argument("--random-only", action="store_true",
                        help="Skip baseline/fg/ack, only run random seeds (e2e_random_multi)")
    parser.add_argument("--char-threshold", type=int, default=30,
                        help="Heuristic ack char threshold (online_pruning mode, default: 30)")
    parser.add_argument("--pruning-mode", choices=["skip", "placeholder", "none", "detect_only"], default="skip",
                        help="Online pruning mode: skip=remove ack, placeholder=replace with generic text, none=no suppression, detect_only=detect but keep msg (default: skip)")
    parser.add_argument("--detection-mode", choices=["heuristic", "oracle", "oracle_5class", "random", "oracle_fg", "length_only", "distilbert"], default="heuristic",
                        help="Ack detection method: heuristic=rule-based, oracle=GPT-4o binary, oracle_5class=GPT-4o 5-class, random=probabilistic, oracle_fg=FG pruning, length_only=pure length filter, distilbert=learned classifier (default: heuristic)")
    parser.add_argument("--distilbert-checkpoint", type=str,
                        default="artifacts/classifier/distilbert_ack/checkpoint-810",
                        help="Path to fine-tuned DistilBERT checkpoint for distilbert detection mode")
    parser.add_argument("--openai-api-key", type=str, default=None,
                        help="OpenAI API key for oracle mode (or set OPENAI_API_KEY env var)")
    parser.add_argument("--openai-model", type=str, default="gpt-4o",
                        help="OpenAI model for oracle classification (default: gpt-4o)")
    parser.add_argument("--oracle-base-url", type=str, default=None,
                        help="Custom base URL for oracle API (e.g. http://localhost:8000/v1 for local vLLM)")
    parser.add_argument("--oracle-cache", type=str, default=None,
                        help="Path to precomputed oracle labels JSON (skips API calls for cached keys)")
    parser.add_argument("--data-seed", type=int, default=None,
                        help="Override config data.seed for dataset shuffling")
    parser.add_argument("--random-suppress-rate", type=float, default=0.106,
                        help="Per-message suppression probability for online_random_token_matched (default: 0.106)")
    parser.add_argument("--random-token-budget", type=int, default=None,
                        help="If set, suppress by token budget instead of probability (online_random_token_matched)")
    parser.add_argument("--domain", type=str, default="gsm8k",
                        choices=["gsm8k", "arc", "strategyqa"],
                        help="Task domain for answer extraction (default: gsm8k)")
    parser.add_argument("--ack-prune-rate", type=float, default=1.0,
                        help="Fraction of detected ack messages to actually prune (0.0=none, 1.0=all)")
    args = parser.parse_args()

    needs_traces = args.mode not in ("online_pruning", "online_oracle", "online_random_token_matched", "online_fg")
    if needs_traces and not args.traces_dir:
        parser.error("--traces-dir is required for %s mode" % args.mode)
    if needs_traces and not args.annotations_dir:
        parser.error("--annotations-dir is required for %s mode" % args.mode)

    if args.mode == "e2e":
        if not args.config:
            parser.error("--config is required for e2e mode")
        e2e_main(args)
    elif args.mode == "e2e_random_multi":
        if not args.config:
            parser.error("--config is required for e2e_random_multi mode")
        e2e_random_multi_main(args)
    elif args.mode == "e2e_pos_matched":
        if not args.config:
            parser.error("--config is required for e2e_pos_matched mode")
        e2e_pos_matched_main(args)
    elif args.mode == "online_pruning":
        if not args.config:
            parser.error("--config is required for online_pruning mode")
        online_main(args)
    elif args.mode == "online_oracle":
        if not args.config:
            parser.error("--config is required for online_oracle mode")
        online_oracle_main(args)
    elif args.mode == "online_random_token_matched":
        if not args.config:
            parser.error("--config is required for online_random_token_matched mode")
        online_random_token_matched_main(args)
    elif args.mode == "online_fg":
        if not args.config:
            parser.error("--config is required for online_fg mode")
        online_fg_main(args)
    else:
        simulate_main(args)


if __name__ == "__main__":
    main()
