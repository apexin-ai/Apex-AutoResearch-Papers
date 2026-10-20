"""
RRF (Reciprocal Rank Fusion) aggregation of contamination signals.

Fuses 4 per-item signal scores into a single exposure score using RRF
(Cormack et al. 2009). Also implements ablation variants: equal-weight
rank averaging and single-signal baselines.

Input:  Per-item signal scores (JSON from compute_signals.py)
Output: Per-model-item fused exposure scores + signal survival AUC matrix
"""

import argparse
import json
import logging
from pathlib import Path

import numpy as np

logger = logging.getLogger(__name__)

SIGNAL_KEYS = ["s1_embedding", "s2_minkpp", "s3_constat", "s4_selfcritique"]
RRF_K = 60


def load_signal_data(signal_files: list[str]) -> list[dict]:
    """Load and merge signal files. Each file contains a list of per-item dicts."""
    merged = {}
    for fpath in signal_files:
        with open(fpath) as f:
            data = json.load(f)
        for item in data:
            idx = item["index"]
            if idx not in merged:
                merged[idx] = {"index": idx, "benchmark": item.get("benchmark", "")}
            merged[idx].update(item)
    return [merged[k] for k in sorted(merged)]


def compute_ranks(scores: np.ndarray) -> np.ndarray:
    """Rank items from 1 (highest score = most suspicious) to N."""
    order = np.argsort(-scores)  # descending
    ranks = np.empty_like(order)
    ranks[order] = np.arange(1, len(scores) + 1)
    return ranks


def rrf_aggregate(items: list[dict], k: int = RRF_K,
                  signals: list[str] = None) -> list[dict]:
    """
    RRF fusion: score_j = sum_s 1/(k + rank_s(j))

    All signals are oriented so higher = more suspicious.
    """
    if signals is None:
        signals = SIGNAL_KEYS

    n = len(items)
    if n == 0:
        return []

    # Extract score vectors
    score_matrix = {}
    for sig in signals:
        vals = np.array([item.get(sig, 0.0) or 0.0 for item in items], dtype=float)
        score_matrix[sig] = vals

    # Compute ranks for each signal
    rank_matrix = {}
    for sig in signals:
        rank_matrix[sig] = compute_ranks(score_matrix[sig])

    # RRF fusion
    rrf_scores = np.zeros(n)
    for sig in signals:
        rrf_scores += 1.0 / (k + rank_matrix[sig])

    # Build output
    results = []
    for i, item in enumerate(items):
        record = {
            "index": item["index"],
            "benchmark": item.get("benchmark", ""),
            "rrf_score": float(rrf_scores[i]),
        }
        for sig in signals:
            record[f"rank_{sig}"] = int(rank_matrix[sig][i])
        results.append(record)

    return results


def rank_average_aggregate(items: list[dict],
                           signals: list[str] = None) -> list[dict]:
    """Equal-weight rank averaging (ablation baseline)."""
    if signals is None:
        signals = SIGNAL_KEYS

    n = len(items)
    if n == 0:
        return []

    rank_matrix = {}
    for sig in signals:
        vals = np.array([item.get(sig, 0.0) or 0.0 for item in items], dtype=float)
        rank_matrix[sig] = compute_ranks(vals)

    avg_ranks = np.zeros(n)
    for sig in signals:
        avg_ranks += rank_matrix[sig]
    avg_ranks /= len(signals)

    # Lower average rank = more suspicious, so score = -avg_rank for consistent ordering
    results = []
    for i, item in enumerate(items):
        results.append({
            "index": item["index"],
            "benchmark": item.get("benchmark", ""),
            "rank_avg_score": float(-avg_ranks[i]),
            "mean_rank": float(avg_ranks[i]),
        })
    return results


def single_signal_scores(items: list[dict]) -> dict[str, list[dict]]:
    """Single-signal ablation: each signal alone as the exposure score."""
    results = {}
    for sig in SIGNAL_KEYS:
        vals = [{"index": item["index"], "benchmark": item.get("benchmark", ""),
                 f"single_{sig}": item.get(sig, 0.0) or 0.0} for item in items]
        results[sig] = vals
    return results


def compute_signal_auc(items: list[dict], labels: list[int]) -> dict:
    """
    Compute per-signal AUC if ground-truth contamination labels are available.
    Returns signal survival AUC matrix.
    """
    from sklearn.metrics import roc_auc_score

    labels_arr = np.array(labels)
    if len(np.unique(labels_arr)) < 2:
        logger.warning("Cannot compute AUC: labels have only one class")
        return {}

    auc_results = {}
    for sig in SIGNAL_KEYS:
        scores = np.array([item.get(sig, 0.0) or 0.0 for item in items])
        try:
            auc = roc_auc_score(labels_arr, scores)
            auc_results[sig] = float(auc)
        except ValueError as e:
            logger.warning("AUC computation failed for %s: %s", sig, e)
            auc_results[sig] = None

    # Also compute AUC for RRF fused score
    rrf_results = rrf_aggregate(items)
    rrf_scores = np.array([r["rrf_score"] for r in rrf_results])
    try:
        auc_results["rrf_fused"] = float(roc_auc_score(labels_arr, rrf_scores))
    except ValueError:
        auc_results["rrf_fused"] = None

    return auc_results


def main():
    parser = argparse.ArgumentParser(description="RRF aggregation of contamination signals")
    parser.add_argument("--signal-files", type=str, nargs="+", required=True,
                        help="JSON files with per-item signal scores (or merged signal file)")
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--k", type=int, default=RRF_K,
                        help="RRF k parameter (default: 60)")
    parser.add_argument("--labels-file", type=str, default=None,
                        help="JSON file with ground-truth contamination labels (list of 0/1)")
    parser.add_argument("--model-name", type=str, default="unknown",
                        help="Model identifier for output naming")
    parser.add_argument("--benchmark", type=str, default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load signals
    items = load_signal_data(args.signal_files)
    logger.info("Loaded %d items with signals", len(items))

    # RRF aggregation
    rrf_results = rrf_aggregate(items, k=args.k)
    rrf_file = output_dir / f"rrf_scores_{args.model_name}.json"
    with open(rrf_file, "w") as f:
        json.dump(rrf_results, f, indent=2)
    logger.info("RRF scores saved to %s", rrf_file)

    # Ablation: rank averaging
    ra_results = rank_average_aggregate(items)
    ra_file = output_dir / f"rank_avg_scores_{args.model_name}.json"
    with open(ra_file, "w") as f:
        json.dump(ra_results, f, indent=2)

    # Ablation: single signal
    ss_results = single_signal_scores(items)
    ss_file = output_dir / f"single_signal_scores_{args.model_name}.json"
    with open(ss_file, "w") as f:
        json.dump({k: v for k, v in ss_results.items()}, f, indent=2)

    # AUC matrix (if labels available)
    if args.labels_file:
        with open(args.labels_file) as f:
            labels = json.load(f)
        auc_results = compute_signal_auc(items, labels)
        auc_file = output_dir / f"signal_auc_{args.model_name}.json"
        with open(auc_file, "w") as f:
            json.dump(auc_results, f, indent=2)
        logger.info("Signal AUC matrix: %s", json.dumps(auc_results, indent=2))

    # Summary statistics
    rrf_scores = [r["rrf_score"] for r in rrf_results]
    logger.info("RRF score range: [%.6f, %.6f], mean=%.6f",
                min(rrf_scores), max(rrf_scores), np.mean(rrf_scores))


if __name__ == "__main__":
    main()
