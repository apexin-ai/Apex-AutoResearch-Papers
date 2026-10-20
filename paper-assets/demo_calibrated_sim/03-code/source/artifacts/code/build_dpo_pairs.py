"""Build DPO training pairs from calibrated and uncalibrated τ-Bench traces.

Aligns traces by task_id, pairs calibrated (chosen) vs uncalibrated (rejected)
user responses at each turn. Supports cross-pairing when multiple trials exist
per task.

Input:  calibrated traces JSON (from generate_synthetic_corpus.py)
        uncalibrated traces JSON (from MVP baseline or same format)
Output: JSONL with {"prompt", "chosen", "rejected"} per line

Dependencies: none (stdlib only)
"""

from __future__ import annotations

import argparse
import json
import logging
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("build_dpo_pairs")


# ---------------------------------------------------------------------------
# Trace loading
# ---------------------------------------------------------------------------

def load_traces(path: str) -> List[dict]:
    """Load traces from either corpus format or raw tau-bench checkpoint format.

    Supported formats:
    1. Corpus format (from generate_synthetic_corpus.py):
       {"metadata": ..., "traces": [{"task_id", "trace", ...}, ...]}
    2. Raw checkpoint format (list of EnvRunResult dicts):
       [{"task_id", "traj", "reward", "trial"}, ...]
    """
    with open(path) as f:
        data = json.load(f)

    if isinstance(data, dict) and "traces" in data:
        return data["traces"]

    if isinstance(data, list):
        records = []
        for item in data:
            traj = item.get("traj", [])
            trace = []
            for msg in traj:
                role = msg.get("role", "")
                content = msg.get("content", "")
                if role in ("user", "assistant"):
                    trace.append({"role": role, "content": content or ""})
            if trace:
                records.append({
                    "task_id": item.get("task_id"),
                    "trial": item.get("trial", 0),
                    "trace": trace,
                })
        return records

    raise ValueError(f"Unrecognized trace format in {path}")


def group_by_task(records: List[dict]) -> Dict[int, List[List[dict]]]:
    """Group trace records by task_id, returning {task_id: [trace, trace, ...]}."""
    groups: Dict[int, List[List[dict]]] = defaultdict(list)
    for rec in records:
        tid = rec.get("task_id")
        if tid is not None and rec.get("trace"):
            groups[tid].append(rec["trace"])
    return dict(groups)


# ---------------------------------------------------------------------------
# DPO pair construction
# ---------------------------------------------------------------------------

def extract_user_turns_with_context(trace: List[dict]) -> List[Tuple[str, str]]:
    """Extract (context_up_to_turn, user_response) pairs from a trace.

    For each user turn, context = all messages before that turn (system + prior
    dialogue), and response = the user's message at that turn.
    """
    pairs = []
    for i, msg in enumerate(trace):
        if msg["role"] != "user":
            continue
        context_messages = trace[:i]
        if not context_messages:
            continue
        context = format_context(context_messages)
        response = msg["content"].strip()
        if response:
            pairs.append((context, response))
    return pairs


def format_context(messages: List[dict]) -> str:
    """Format conversation history as a prompt string for DPO."""
    parts = []
    for msg in messages:
        role = msg["role"]
        content = msg["content"].strip()
        if not content:
            continue
        if role == "user":
            parts.append(f"Customer: {content}")
        elif role == "assistant":
            parts.append(f"Agent: {content}")
        else:
            parts.append(f"{role}: {content}")
    return "\n".join(parts)


def build_pairs_for_task(
    calibrated_traces: List[List[dict]],
    uncalibrated_traces: List[List[dict]],
    min_turn_length: int = 10,
) -> List[dict]:
    """Build DPO pairs by cross-pairing calibrated and uncalibrated traces.

    For each (calibrated_trace, uncalibrated_trace) combination, align user
    turns by position index and create a pair where calibrated = chosen.
    """
    pairs = []

    for cal_trace in calibrated_traces:
        cal_turns = extract_user_turns_with_context(cal_trace)
        for uncal_trace in uncalibrated_traces:
            uncal_turns = extract_user_turns_with_context(uncal_trace)

            n_pairs = min(len(cal_turns), len(uncal_turns))
            for idx in range(n_pairs):
                cal_ctx, cal_resp = cal_turns[idx]
                uncal_ctx, uncal_resp = uncal_turns[idx]

                if len(cal_resp) < min_turn_length or len(uncal_resp) < min_turn_length:
                    continue

                if cal_resp.strip() == uncal_resp.strip():
                    continue

                if "###STOP###" in cal_resp or "###STOP###" in uncal_resp:
                    continue

                # Use calibrated trace's context as the prompt
                pairs.append({
                    "prompt": cal_ctx,
                    "chosen": cal_resp,
                    "rejected": uncal_resp,
                })

    return pairs


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def build_dpo_dataset(args: argparse.Namespace) -> int:
    log.info("Loading calibrated traces from %s", args.calibrated_traces)
    cal_records = load_traces(args.calibrated_traces)
    log.info("Loaded %d calibrated trace records", len(cal_records))

    log.info("Loading uncalibrated traces from %s", args.uncalibrated_traces)
    uncal_records = load_traces(args.uncalibrated_traces)
    log.info("Loaded %d uncalibrated trace records", len(uncal_records))

    cal_groups = group_by_task(cal_records)
    uncal_groups = group_by_task(uncal_records)

    common_tasks = set(cal_groups.keys()) & set(uncal_groups.keys())
    log.info(
        "Task alignment: %d calibrated tasks, %d uncalibrated tasks, %d in common",
        len(cal_groups), len(uncal_groups), len(common_tasks),
    )

    if not common_tasks:
        log.error("No overlapping task_ids between calibrated and uncalibrated traces")
        return 0

    all_pairs = []
    for tid in sorted(common_tasks):
        task_pairs = build_pairs_for_task(
            cal_groups[tid],
            uncal_groups[tid],
            min_turn_length=args.min_turn_length,
        )
        all_pairs.extend(task_pairs)
        if task_pairs:
            log.info("Task %d: %d DPO pairs", tid, len(task_pairs))

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        for pair in all_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    log.info("Wrote %d DPO pairs to %s", len(all_pairs), output_path)

    if all_pairs:
        avg_prompt_len = sum(len(p["prompt"]) for p in all_pairs) / len(all_pairs)
        avg_chosen_len = sum(len(p["chosen"]) for p in all_pairs) / len(all_pairs)
        avg_rejected_len = sum(len(p["rejected"]) for p in all_pairs) / len(all_pairs)
        log.info(
            "Stats: avg_prompt=%.0f chars, avg_chosen=%.0f chars, avg_rejected=%.0f chars",
            avg_prompt_len, avg_chosen_len, avg_rejected_len,
        )

    return len(all_pairs)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Build DPO pairs from calibrated and uncalibrated τ-Bench traces"
    )
    p.add_argument(
        "--calibrated-traces", required=True,
        help="Path to calibrated traces JSON (from generate_synthetic_corpus.py)",
    )
    p.add_argument(
        "--uncalibrated-traces", required=True,
        help="Path to uncalibrated traces JSON (MVP baseline or tau-bench checkpoint)",
    )
    p.add_argument(
        "--output", default="/root/democalib/data/dpo_pairs.jsonl",
        help="Output JSONL path (default: /root/democalib/data/dpo_pairs.jsonl)",
    )
    p.add_argument(
        "--min-turn-length", type=int, default=10,
        help="Minimum character length for user turns to include (default: 10)",
    )
    return p.parse_args()


if __name__ == "__main__":
    n = build_dpo_dataset(parse_args())
    if n == 0:
        log.warning("No DPO pairs generated — check trace alignment and filtering")
