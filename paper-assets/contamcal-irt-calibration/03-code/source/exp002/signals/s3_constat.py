import json
import logging
from pathlib import Path

import numpy as np

logger = logging.getLogger(__name__)


def _load_per_item_correctness(eval_results_path: str, benchmark: str) -> list[bool]:
    with open(eval_results_path) as f:
        data = json.load(f)

    bench_data = data.get("benchmarks", {}).get(benchmark)
    if bench_data is None:
        raise ValueError(f"Benchmark '{benchmark}' not found in {eval_results_path}")

    return [item["correct"] for item in bench_data["per_item"]]


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

    n_items = len(orig_seeds[0])
    for vec in orig_seeds + para_seeds:
        if len(vec) != n_items:
            raise ValueError(f"Item count mismatch: expected {n_items}, got {len(vec)}")

    orig_matrix = np.array(orig_seeds, dtype=float)
    para_matrix = np.array(para_seeds, dtype=float)

    orig_mean = orig_matrix.mean(axis=0)
    para_mean = para_matrix.mean(axis=0)
    gap = orig_mean - para_mean

    results = []
    for i in range(n_items):
        results.append({
            "item_id": make_item_id(benchmark, i),
            "signal": "s3_constat",
            "score": float(gap[i]),
            "metadata": {
                "orig_accuracy": float(orig_mean[i]),
                "para_accuracy": float(para_mean[i]),
                "n_seeds": len(orig_seeds),
            },
        })

    return results
