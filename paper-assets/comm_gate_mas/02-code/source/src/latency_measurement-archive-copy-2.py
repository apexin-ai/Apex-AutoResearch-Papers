#!/usr/bin/env python3
"""Wall-clock latency measurement: baseline vs ack_only pruning."""

import argparse
import gc
import json
import logging
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pruning_validation import (
    check_answer,
    get_prune_rounds_for_task,
    load_annotations,
    load_traces,
    run_e2e_pruned_pipeline,
)
from trace_collection import build_llm_config, load_config, _raise_fd_limit
from utils import extract_final_answer

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_TRACES_PATH = "outputs/full_scale/qwen_round_robin/traces/traces.jsonl"
DEFAULT_ANN_DIR = "outputs/full_scale/qwen_round_robin/annotations"
DEFAULT_CONFIG_PATH = "configs/full_scale.yaml"
DEFAULT_OUTPUT_PATH = "outputs/v7_analysis/latency_measurement.json"
DEFAULT_N_TASKS = 20


def measure_tasks(tasks, annotations, cfg, llm_config, strategy, n_tasks=20):
    """Run n_tasks with per-task wall-clock timing."""
    ack_types = {"acknowledgment"}
    max_rounds = cfg["trace_collection"].get("max_rounds", 6)
    results = []

    for i, task_rec in enumerate(tasks[:n_tasks]):
        task_id = task_rec["task_id"]
        question = task_rec["question"]
        ground_truth = task_rec["ground_truth"]

        if strategy == "baseline":
            prune_rounds = set()
        else:
            prune_rounds = get_prune_rounds_for_task(task_rec, annotations, ack_types)

        start = time.time()
        try:
            messages = run_e2e_pruned_pipeline(
                question, cfg, llm_config, prune_rounds, max_rounds=max_rounds
            )
        except Exception:
            logger.exception("Failed on %s", task_id)
            results.append({
                "task_id": task_id, "elapsed": None, "correct": False,
                "pruned_rounds": len(prune_rounds),
            })
            gc.collect()
            continue
        elapsed = time.time() - start
        gc.collect()

        final_answer = None
        for msg in reversed(messages):
            final_answer = extract_final_answer(msg.get("content", ""))
            if final_answer is not None:
                break

        is_correct = check_answer(final_answer, ground_truth)
        results.append({
            "task_id": task_id,
            "elapsed": round(elapsed, 3),
            "correct": is_correct,
            "answer": str(final_answer),
            "pruned_rounds": len(prune_rounds),
        })
        logger.info("[%s] %d/%d task=%s %.2fs correct=%s pruned=%d",
                     strategy, i + 1, n_tasks, task_id, elapsed, is_correct,
                     len(prune_rounds))

    valid = [r for r in results if r["elapsed"] is not None]
    latencies = [r["elapsed"] for r in valid]
    correct_count = sum(1 for r in valid if r["correct"])

    return {
        "strategy": strategy,
        "per_task": results,
        "mean_latency": round(sum(latencies) / len(latencies), 3) if latencies else None,
        "median_latency": round(sorted(latencies)[len(latencies) // 2], 3) if latencies else None,
        "total_time": round(sum(latencies), 3),
        "accuracy": round(correct_count / len(valid), 4) if valid else 0,
        "n_tasks": len(valid),
    }


def parse_args():
    parser = argparse.ArgumentParser(description="Latency measurement: baseline vs ack_only")
    parser.add_argument("--traces", default=DEFAULT_TRACES_PATH)
    parser.add_argument("--annotations", default=DEFAULT_ANN_DIR)
    parser.add_argument("--config", default=DEFAULT_CONFIG_PATH)
    parser.add_argument("--output", default=DEFAULT_OUTPUT_PATH)
    parser.add_argument("--model", default=None, help="Override model name in config")
    parser.add_argument("--port", type=int, default=None, help="Override api_base port")
    parser.add_argument("--n-tasks", type=int, default=DEFAULT_N_TASKS)
    return parser.parse_args()


def main():
    args = parse_args()
    _raise_fd_limit()
    cfg = load_config(args.config)

    if args.model:
        cfg["model"]["name"] = args.model
    if args.port:
        cfg["model"]["api_base"] = f"http://localhost:{args.port}/v1"

    llm_config = build_llm_config(cfg)

    all_tasks = load_traces(args.traces)
    annotations = load_annotations(args.annotations)
    logger.info("Loaded %d tasks, %d annotations", len(all_tasks), len(annotations))

    n_tasks = args.n_tasks
    tasks = all_tasks[:n_tasks]

    logger.info("=== Measuring baseline (no pruning) ===")
    baseline = measure_tasks(tasks, annotations, cfg, llm_config, "baseline", n_tasks)
    logger.info("Baseline: mean=%.2fs, accuracy=%.1f%%",
                baseline["mean_latency"] or 0, baseline["accuracy"] * 100)

    logger.info("=== Measuring ack_only pruning ===")
    ack_only = measure_tasks(tasks, annotations, cfg, llm_config, "ack_only", n_tasks)
    logger.info("Ack-only: mean=%.2fs, accuracy=%.1f%%",
                ack_only["mean_latency"] or 0, ack_only["accuracy"] * 100)

    speedup = None
    if baseline["mean_latency"] and ack_only["mean_latency"]:
        speedup = round(baseline["mean_latency"] / ack_only["mean_latency"], 3)
        reduction_pct = round((1 - ack_only["mean_latency"] / baseline["mean_latency"]) * 100, 1)
    else:
        reduction_pct = None

    output = {
        "baseline": baseline,
        "ack_only": ack_only,
        "speedup_ratio": speedup,
        "latency_reduction_pct": reduction_pct,
        "n_tasks": n_tasks,
        "config": {
            "model": cfg["model"]["name"],
            "api_base": cfg["model"]["api_base"],
            "max_rounds": cfg["trace_collection"].get("max_rounds", 6),
        },
    }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info("Results saved to %s", args.output)

    logger.info("=== Summary ===")
    logger.info("Baseline: mean=%.2fs, accuracy=%.1f%%",
                baseline["mean_latency"] or 0, baseline["accuracy"] * 100)
    logger.info("Ack-only: mean=%.2fs, accuracy=%.1f%%",
                ack_only["mean_latency"] or 0, ack_only["accuracy"] * 100)
    if speedup:
        logger.info("Speedup: %.2fx, latency reduction: %.1f%%", speedup, reduction_pct)


if __name__ == "__main__":
    main()
