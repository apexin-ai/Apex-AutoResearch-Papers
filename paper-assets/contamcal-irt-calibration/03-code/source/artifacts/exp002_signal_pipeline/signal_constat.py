"""
Signal 3: ConStat performance gap (original vs paraphrased).

Computes per-item accuracy gap between original and paraphrased benchmark
versions from exp-001 evaluation results. No additional model inference needed.

Input:  exp-001 eval_results.json for original + paraphrased items (across seeds)
Output: JSON with per-item accuracy gap scores
"""

import argparse
import json
import logging
from pathlib import Path

import numpy as np

logger = logging.getLogger(__name__)


def load_per_item_correctness(eval_results_path: str, benchmark: str) -> list[bool]:
    """Load per-item correctness from an eval_results.json file."""
    with open(eval_results_path) as f:
        data = json.load(f)

    bench_data = data.get("benchmarks", {}).get(benchmark)
    if bench_data is None:
        raise ValueError(f"Benchmark '{benchmark}' not found in {eval_results_path}")

    return [item["correct"] for item in bench_data["per_item"]]


def compute_constat_signal(
    benchmark: str,
    original_eval_paths: list[str],
    paraphrase_eval_paths: list[str],
) -> list[dict]:
    """
    Compute per-item accuracy gap across seeds.

    Each path corresponds to one seed. Per-item accuracy is averaged over seeds
    (3 seeds → possible values: 0, 0.33, 0.67, 1.0).
    Gap = mean(original) - mean(paraphrased).
    """
    if len(original_eval_paths) != len(paraphrase_eval_paths):
        raise ValueError(
            f"Mismatched seed counts: {len(original_eval_paths)} original vs "
            f"{len(paraphrase_eval_paths)} paraphrased"
        )

    # Load correctness vectors for all seeds
    orig_seeds = []
    for path in original_eval_paths:
        orig_seeds.append(load_per_item_correctness(path, benchmark))

    para_seeds = []
    for path in paraphrase_eval_paths:
        para_seeds.append(load_per_item_correctness(path, benchmark))

    n_items = len(orig_seeds[0])
    for i, vec in enumerate(orig_seeds + para_seeds):
        if len(vec) != n_items:
            raise ValueError(f"Item count mismatch: expected {n_items}, got {len(vec)}")

    orig_matrix = np.array(orig_seeds, dtype=float)  # (n_seeds, n_items)
    para_matrix = np.array(para_seeds, dtype=float)

    orig_mean = orig_matrix.mean(axis=0)  # (n_items,)
    para_mean = para_matrix.mean(axis=0)
    gap = orig_mean - para_mean

    results = []
    for i in range(n_items):
        results.append({
            "index": i,
            "benchmark": benchmark,
            "s3_constat": float(gap[i]),
            "s3_orig_accuracy": float(orig_mean[i]),
            "s3_para_accuracy": float(para_mean[i]),
        })

    return results


def main():
    parser = argparse.ArgumentParser(description="Signal 3: ConStat performance gap")
    parser.add_argument("--benchmark", type=str, required=True,
                        choices=["mmlu", "gsm8k", "arc_challenge", "humaneval"])
    parser.add_argument("--original-eval-paths", type=str, nargs="+", required=True,
                        help="Paths to eval_results.json for original items (one per seed)")
    parser.add_argument("--paraphrase-eval-paths", type=str, nargs="+", required=True,
                        help="Paths to eval_results.json for paraphrased items (one per seed)")
    parser.add_argument("--output-dir", type=str, required=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = compute_constat_signal(
        benchmark=args.benchmark,
        original_eval_paths=args.original_eval_paths,
        paraphrase_eval_paths=args.paraphrase_eval_paths,
    )

    out_file = output_dir / f"signal_constat_{args.benchmark}.json"
    with open(out_file, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved %d items to %s", len(results), out_file)


if __name__ == "__main__":
    main()
