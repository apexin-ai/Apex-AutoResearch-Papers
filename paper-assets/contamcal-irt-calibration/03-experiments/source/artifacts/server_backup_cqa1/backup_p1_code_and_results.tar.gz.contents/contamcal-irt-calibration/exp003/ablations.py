"""
exp-003 Ablation Variants for RRF Aggregation.

(a) Equal-weight rank averaging
(b) Single-signal only (x4 baselines)
(c) Calibration-based weighted RRF (oracle, learns weights from ground truth)
(d) FP injection robustness (5%, 10%, 20% false positive rates)
(e) Degraded 2-signal mode (ConStat + Self-Critique only, closed-weight scenario)
"""

import argparse
import json
import logging
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from rrf_aggregation import (
    load_signal_files, detect_available_signals, compute_ranks,
    rrf_fuse, normalize_minmax, SIGNAL_KEYS, DEFAULT_K,
    SIGNAL_ROOT, LABELS_ROOT, BENCHMARKS,
)

logger = logging.getLogger(__name__)


def load_labels(labels_dir: str, benchmark: str, dosage: str) -> np.ndarray:
    """Load ground truth contamination labels (0/1 per item)."""
    label_file = Path(labels_dir) / f"contamination_labels_{benchmark}_{dosage}.json"
    if not label_file.exists():
        raise FileNotFoundError(f"Labels not found: {label_file}")
    with open(label_file) as f:
        data = json.load(f)
    return np.array(data["labels"], dtype=int)


# --- (a) Equal-weight rank averaging ---

def equal_weight_rank_avg(items: list[dict], signals: list[str] = None) -> np.ndarray:
    """Average normalized ranks across signals. Lower avg rank = more suspicious."""
    if signals is None:
        signals = detect_available_signals(items)
    n = len(items)
    if n == 0:
        return np.array([])

    avg_rank = np.zeros(n)
    for sig in signals:
        vals = np.array([item.get(sig, 0.0) or 0.0 for item in items], dtype=float)
        avg_rank += compute_ranks(vals)
    avg_rank /= len(signals)

    # Lower rank = more suspicious -> higher score
    if n > 1:
        scores = 1.0 - (avg_rank - 1) / (n - 1)
    else:
        scores = np.array([0.5])
    return scores


# --- (b) Single-signal baselines ---

def single_signal_scores(items: list[dict]) -> dict:
    """Normalize each signal independently to [0,1]."""
    results = {}
    for sig in SIGNAL_KEYS:
        vals = np.array([item.get(sig, 0.0) or 0.0 for item in items], dtype=float)
        if np.any(vals != 0):
            results[sig] = normalize_minmax(vals)
    return results


# --- (c) Calibration-based weighted RRF (oracle) ---

def calibrated_weighted_rrf(items: list[dict], labels: np.ndarray,
                            k: int = DEFAULT_K,
                            signals: list[str] = None) -> tuple:
    """Learn signal weights from ground truth via logistic regression.

    Oracle baseline -- uses labels unavailable in practice.
    Returns (exposure_scores, learned_weights_dict).
    """
    from sklearn.linear_model import LogisticRegression

    if signals is None:
        signals = detect_available_signals(items)

    n = len(items)

    # Build RRF feature matrix: each column = 1/(k + rank_s)
    rank_features = np.zeros((n, len(signals)))
    for j, sig in enumerate(signals):
        vals = np.array([item.get(sig, 0.0) or 0.0 for item in items], dtype=float)
        rank_features[:, j] = 1.0 / (k + compute_ranks(vals))

    y = labels[:n] if len(labels) >= n else np.pad(labels, (0, n - len(labels)))

    lr = LogisticRegression(max_iter=1000, class_weight="balanced")
    lr.fit(rank_features, y)

    raw_weights = lr.coef_[0]
    pos_weights = np.maximum(raw_weights, 0)
    if pos_weights.sum() > 0:
        pos_weights = pos_weights / pos_weights.sum()
    else:
        pos_weights = np.ones(len(signals)) / len(signals)

    weights = {sig: float(w) for sig, w in zip(signals, pos_weights)}

    scores = np.zeros(n)
    for j, sig in enumerate(signals):
        scores += pos_weights[j] * rank_features[:, j]
    scores = normalize_minmax(scores)

    return scores, weights


# --- (d) FP injection robustness ---

def inject_false_positives(items: list[dict], labels: np.ndarray,
                           fp_rate: float, signals: list[str] = None,
                           seed: int = 42) -> list[dict]:
    """Inject false positives by boosting clean items' scores to contaminated p95."""
    if signals is None:
        signals = detect_available_signals(items)

    rng = np.random.RandomState(seed)
    n = min(len(items), len(labels))

    clean_indices = [i for i in range(n) if labels[i] == 0]
    contam_indices = [i for i in range(n) if labels[i] == 1]
    n_inject = int(len(clean_indices) * fp_rate)
    if n_inject == 0:
        return list(items)
    inject_indices = set(rng.choice(clean_indices, size=n_inject, replace=False))

    # 95th percentile of contaminated items per signal
    p95 = {}
    for sig in signals:
        contam_vals = [items[i].get(sig, 0.0) or 0.0 for i in contam_indices]
        p95[sig] = float(np.percentile(contam_vals, 95)) if contam_vals else 1.0

    modified = []
    for i, item in enumerate(items):
        rec = dict(item)
        if i in inject_indices:
            target_sig = rng.choice(signals)
            rec[target_sig] = p95[target_sig]
        modified.append(rec)

    return modified


def fp_robustness_test(items: list[dict], labels: np.ndarray,
                       k: int = DEFAULT_K,
                       fp_rates: list = None) -> dict:
    """Test RRF and single-signal robustness under FP injection.

    Returns {fp_rate_key: {method_name: list_of_scores}}.
    """
    if fp_rates is None:
        fp_rates = [0.05, 0.10, 0.20]

    signals = detect_available_signals(items)
    results = {}

    for rate in fp_rates:
        modified = inject_false_positives(items, labels, rate, signals)
        rate_key = f"fp_{int(rate * 100):02d}pct"
        results[rate_key] = {}

        rrf_scores = rrf_fuse(modified, k=k, signals=signals)
        results[rate_key]["rrf"] = normalize_minmax(rrf_scores).tolist()

        results[rate_key]["rank_avg"] = equal_weight_rank_avg(modified, signals).tolist()

        for sig in signals:
            vals = np.array([item.get(sig, 0.0) or 0.0 for item in modified], dtype=float)
            if np.any(vals != 0):
                results[rate_key][sig] = normalize_minmax(vals).tolist()

    return results


# --- (e) Degraded 2-signal mode ---

def degraded_2signal(items: list[dict], k: int = DEFAULT_K) -> np.ndarray:
    """RRF with only ConStat + Self-Critique (closed-weight scenario)."""
    closed_signals = ["s3_constat", "s4_selfcritique"]
    available = [s for s in closed_signals if s in detect_available_signals(items)]
    if not available:
        logger.warning("Neither ConStat nor Self-Critique available for degraded mode")
        return np.full(len(items), 0.5)

    scores = rrf_fuse(items, k=k, signals=available)
    return normalize_minmax(scores)


# --- Run all ---

def run_all_ablations(signal_dir: str, benchmark: str, labels: np.ndarray,
                      k: int = DEFAULT_K) -> dict:
    """Run all ablation variants, return {method_name: np.ndarray of exposure scores}."""
    items = load_signal_files(signal_dir, benchmark)
    if not items:
        return {}

    signals = detect_available_signals(items)
    n = len(items)
    results = {}

    # Main RRF
    results["rrf"] = normalize_minmax(rrf_fuse(items, k=k, signals=signals))

    # (a) Equal-weight rank averaging
    results["rank_avg"] = equal_weight_rank_avg(items, signals)

    # (b) Single-signal baselines
    for sig, scores in single_signal_scores(items).items():
        results[f"single_{sig}"] = scores

    # (c) Calibrated weighted RRF
    if labels is not None and len(labels) >= n:
        try:
            cal_scores, cal_weights = calibrated_weighted_rrf(
                items, labels, k=k, signals=signals
            )
            results["calibrated_rrf"] = cal_scores
            logger.info("Calibrated weights: %s", cal_weights)
        except Exception as e:
            logger.warning("Calibrated RRF failed: %s", e)

    # (d) FP robustness (only when labels available)
    if labels is not None:
        fp_results = fp_robustness_test(items, labels, k=k)
        for rate_key, method_scores in fp_results.items():
            for method, scores in method_scores.items():
                results[f"{rate_key}_{method}"] = np.array(scores)

    # (e) Degraded 2-signal
    results["degraded_2sig"] = degraded_2signal(items, k=k)

    return results


def run_all_ablations_from_items(items: list[dict], labels: np.ndarray,
                                 k: int = DEFAULT_K) -> dict:
    """Same as run_all_ablations but takes pre-loaded items directly."""
    if not items:
        return {}

    signals = detect_available_signals(items)
    n = len(items)
    results = {}

    results["rrf"] = normalize_minmax(rrf_fuse(items, k=k, signals=signals))
    results["rank_avg"] = equal_weight_rank_avg(items, signals)

    for sig, scores in single_signal_scores(items).items():
        results[f"single_{sig}"] = scores

    if labels is not None and len(labels) >= n:
        try:
            cal_scores, cal_weights = calibrated_weighted_rrf(
                items, labels, k=k, signals=signals
            )
            results["calibrated_rrf"] = cal_scores
            logger.info("Calibrated weights: %s", cal_weights)
        except Exception as e:
            logger.warning("Calibrated RRF failed: %s", e)

    if labels is not None:
        fp_results = fp_robustness_test(items, labels, k=k)
        for rate_key, method_scores in fp_results.items():
            for method, scores in method_scores.items():
                results[f"{rate_key}_{method}"] = np.array(scores)

    results["degraded_2sig"] = degraded_2signal(items, k=k)

    return results


def main():
    parser = argparse.ArgumentParser(
        description="exp-003 ablation variants for RRF aggregation"
    )
    parser.add_argument("--signal-dir", type=str, required=True,
                        help="Signal output dir for one model-dosage")
    parser.add_argument("--benchmark", type=str, required=True,
                        choices=BENCHMARKS)
    parser.add_argument("--labels-file", type=str, default=None,
                        help="Ground truth labels JSON (overrides --dosage)")
    parser.add_argument("--labels-dir", type=str, default=LABELS_ROOT)
    parser.add_argument("--dosage", type=str, default=None,
                        help="Dosage key for auto-loading labels (e.g. d005)")
    parser.add_argument("--k", type=int, default=DEFAULT_K)
    parser.add_argument("--output-dir", type=str, required=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    labels = None
    if args.labels_file:
        with open(args.labels_file) as f:
            data = json.load(f)
        labels = np.array(data["labels"], dtype=int)
    elif args.dosage:
        labels = load_labels(args.labels_dir, args.benchmark, args.dosage)

    results = run_all_ablations(args.signal_dir, args.benchmark, labels, k=args.k)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    model_id = Path(args.signal_dir).name
    for method, scores in results.items():
        out_data = [
            {"index": i, "benchmark": args.benchmark, "exposure": float(s)}
            for i, s in enumerate(scores)
        ]
        out_file = output_dir / f"ablation_{method}_{model_id}_{args.benchmark}.json"
        with open(out_file, "w") as f:
            json.dump(out_data, f, indent=2)

    logger.info("Saved %d ablation results to %s", len(results), output_dir)

    summary = {}
    for method, scores in results.items():
        summary[method] = {
            "mean": float(np.mean(scores)),
            "std": float(np.std(scores)),
            "min": float(np.min(scores)),
            "max": float(np.max(scores)),
        }
    summary_file = output_dir / f"ablation_summary_{model_id}_{args.benchmark}.json"
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)
    logger.info("Summary:\n%s", json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
