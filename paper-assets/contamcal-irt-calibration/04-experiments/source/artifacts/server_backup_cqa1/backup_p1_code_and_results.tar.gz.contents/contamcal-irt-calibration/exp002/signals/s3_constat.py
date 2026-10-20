# Fix: use all original indices as base, not orig∩para intersection.
# Items without paraphrase data get score=0.0 (no contamination evidence).
import json
import logging
from pathlib import Path

import numpy as np

logger = logging.getLogger(__name__)


def _load_per_item_correctness(eval_results_path: str, benchmark: str) -> dict[int, bool]:
    with open(eval_results_path) as f:
        data = json.load(f)

    bench_data = data.get("benchmarks", {}).get(benchmark)
    if bench_data is None:
        raise ValueError(f"Benchmark '{benchmark}' not found in {eval_results_path}")

    return {item["index"]: item["correct"] for item in bench_data["per_item"]}


def compute(
    benchmark: str,
    model_path: str = None,
    adapter_path: str = None,
    output_dir: str = None,
    cache_dir: str = None,
    batch_size: int = 8,
    original_eval_paths: list[str] = None,
    paraphrase_eval_paths: list[str] = None,
    **kwargs,
) -> list[dict]:
    from utils import make_item_id

    if not original_eval_paths or not paraphrase_eval_paths:
        logger.warning("S3 ConStat requires --original-eval-paths and --paraphrase-eval-paths; skipping")
        return []

    if len(original_eval_paths) != len(paraphrase_eval_paths):
        raise ValueError(
            f"Mismatched seed counts: {len(original_eval_paths)} original vs "
            f"{len(paraphrase_eval_paths)} paraphrased"
        )

    orig_seeds = [_load_per_item_correctness(p, benchmark) for p in original_eval_paths]
    para_seeds = [_load_per_item_correctness(p, benchmark) for p in paraphrase_eval_paths]

    # Use union of all original seed indices as the full item set
    all_orig_indices = set()
    for d in orig_seeds:
        all_orig_indices |= set(d.keys())
    all_orig_indices = sorted(all_orig_indices)

    # Indices that have paraphrase data across all seeds
    para_covered = set(para_seeds[0].keys())
    for d in para_seeds[1:]:
        para_covered &= set(d.keys())

    n_with_para = len(para_covered)
    n_total = len(all_orig_indices)

    if not all_orig_indices:
        logger.warning("No original items for %s; skipping", benchmark)
        return []

    logger.info(
        "S3 ConStat %s: %d total items, %d with paraphrase data (%.1f%% coverage)",
        benchmark, n_total, n_with_para,
        100.0 * n_with_para / n_total if n_total else 0,
    )

    results = []
    for idx in all_orig_indices:
        if idx in para_covered:
            orig_vals = [seed.get(idx, 0) for seed in orig_seeds]
            para_vals = [seed.get(idx, 0) for seed in para_seeds]
            orig_acc = float(np.mean(orig_vals))
            para_acc = float(np.mean(para_vals))
            gap = orig_acc - para_acc
            has_para = True
        else:
            orig_vals = [seed.get(idx, 0) for seed in orig_seeds]
            orig_acc = float(np.mean(orig_vals))
            para_acc = 0.0
            gap = 0.0
            has_para = False

        results.append({
            "item_id": make_item_id(benchmark, idx),
            "signal": "s3_constat",
            "score": gap,
            "metadata": {
                "orig_accuracy": orig_acc,
                "para_accuracy": para_acc if has_para else None,
                "n_seeds": len(orig_seeds),
                "original_index": idx,
                "has_paraphrase": has_para,
            },
        })

    return results
