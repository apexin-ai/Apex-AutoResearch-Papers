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


def detect_available_signals(items: list[dict], candidates: list[str] = None) -> list[str]:
    """Auto-detect which signals have non-trivial values (not all null/zero)."""
    if candidates is None:
        candidates = SIGNAL_KEYS
    available = []
    for sig in candidates:
        vals = [item.get(sig) for item in items]
        if any(v is not None and v != 0.0 for v in vals):
            available.append(sig)
    return available


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
        signals = detect_available_signals(items)
        if not signals:
            logger.warning("No signals with non-trivial values found")
            return []

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
        signals = detect_available_signals(items)
        if not signals:
            return []

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



def generate_exposure_json(signal_dir: str, benchmarks: list[str],
                           dosage_filter: str = None,
                           k: int = RRF_K,
                           normalize: bool = True) -> dict:
    """
    Generate exposure_scores.json for exp-006 IRT calibration.

    Scans signal_dir for merged signal files, computes RRF per benchmark,
    and returns {benchmark: [tau_per_item]} dict.

    Args:
        signal_dir: Root of exp-002 signal outputs (contains model_dosage_seed/ subdirs)
        benchmarks: List of benchmark names
        dosage_filter: If set, only use signals from this dosage (e.g. "d100")
        k: RRF k parameter
        normalize: If True, min-max normalize tau to [0, 1]
    """
    signal_path = Path(signal_dir)
    exposure = {}

    for bench in benchmarks:
        # Collect all merged signal files for this benchmark
        merged_files = sorted(signal_path.glob(f"*/signals_merged_{bench}.json"))

        if dosage_filter:
            merged_files = [f for f in merged_files if dosage_filter in f.parent.name]

        if not merged_files:
            # Try individual signal files
            sig_files = sorted(signal_path.glob(f"*/signal_*_{bench}.json"))
            if dosage_filter:
                sig_files = [f for f in sig_files if dosage_filter in f.parent.name]
            if not sig_files:
                logger.warning("No signal files found for benchmark %s", bench)
                continue
            items = load_signal_data([str(f) for f in sig_files])
        else:
            # Use merged file (prefer highest dosage for strongest signal)
            items = load_signal_data([str(merged_files[-1])])

        if not items:
            logger.warning("No items loaded for benchmark %s", bench)
            continue

        rrf_results = rrf_aggregate(items, k=k)
        if not rrf_results:
            continue

        # Sort by index to ensure correct ordering
        rrf_results.sort(key=lambda r: r["index"])
        tau = [r["rrf_score"] for r in rrf_results]

        if normalize and tau:
            mn, mx = min(tau), max(tau)
            if mx > mn:
                tau = [(v - mn) / (mx - mn) for v in tau]

        exposure[bench] = tau
        logger.info("Benchmark %s: %d items, tau range [%.4f, %.4f]",
                     bench, len(tau), min(tau), max(tau))

    return exposure


def main():
    parser = argparse.ArgumentParser(description="RRF aggregation of contamination signals")
    parser.add_argument("--signal-files", type=str, nargs="+", default=None,
                        help="JSON files with per-item signal scores (or merged signal file)")
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--k", type=int, default=RRF_K,
                        help="RRF k parameter (default: 60)")
    parser.add_argument("--labels-file", type=str, default=None,
                        help="JSON file with ground-truth contamination labels (list of 0/1)")
    parser.add_argument("--model-name", type=str, default="unknown",
                        help="Model identifier for output naming")
    parser.add_argument("--benchmark", type=str, default=None)
    parser.add_argument("--generate-exposure", action="store_true",
                        help="Generate exposure_scores.json for exp-006 IRT calibration")
    parser.add_argument("--signal-dir", type=str, default=None,
                        help="Root signal output dir (for --generate-exposure mode)")
    parser.add_argument("--benchmarks", type=str, nargs="+",
                        default=["mmlu", "gsm8k", "arc_challenge"],
                        help="Benchmarks to include in exposure scores")
    parser.add_argument("--dosage-filter", type=str, default=None,
                        help="Only use signals from this dosage (e.g. d100)")
    parser.add_argument("--normalize", action="store_true", default=True,
                        help="Min-max normalize tau to [0, 1]")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Mode: generate exposure_scores.json for exp-006
    if args.generate_exposure:
        if not args.signal_dir:
            parser.error("--signal-dir required with --generate-exposure")
        exposure = generate_exposure_json(
            args.signal_dir, args.benchmarks,
            dosage_filter=args.dosage_filter, k=args.k,
            normalize=args.normalize,
        )
        out_file = output_dir / "exposure_scores.json"
        with open(out_file, "w") as f:
            json.dump(exposure, f, indent=2)
        logger.info("Exposure scores saved to %s", out_file)
        for bench, tau in exposure.items():
            logger.info("  %s: %d items", bench, len(tau))
        return

    # Load signals
    if not args.signal_files:
        parser.error("--signal-files required (or use --generate-exposure)")
    items = load_signal_data(args.signal_files)
    logger.info("Loaded %d items with signals", len(items))
    active_signals = detect_available_signals(items)
    logger.info("Active signals: %s", active_signals)

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
