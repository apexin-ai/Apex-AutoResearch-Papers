"""
exp-003: RRF Ablation Analysis

Evaluates RRF aggregation against ablation variants using ground-truth
contamination labels from exp-001.

Input:
  - Per-model signal files (JSON from exp-002, with keys s1_embedding,
    s2_minkpp, s3_constat, s4_selfcritique)
  - Ground-truth contamination labels (JSON, list of 0/1)

Output (to --output-dir):
  - rrf_ablation_results.json — full AUC-ROC results per method/benchmark
  - rrf_ablation_table.tex    — LaTeX table for paper
"""

import argparse
import json
import logging
import os
import sys
from itertools import combinations
from pathlib import Path

import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

SIGNAL_KEYS = ["s1_embedding", "s2_minkpp", "s3_constat", "s4_selfcritique"]
SIGNAL_NAMES = {
    "s1_embedding": "Embedding",
    "s2_minkpp": "Min-K++",
    "s3_constat": "ConStat",
    "s4_selfcritique": "SelfCritique",
}
K_VALUES = [20, 40, 60, 80, 100]
DEFAULT_K = 60


def load_signal_data(signal_files: list[str]) -> list[dict]:
    """Load and merge signal files."""
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


def load_labels(labels_file: str) -> np.ndarray:
    with open(labels_file) as f:
        labels = json.load(f)
    return np.array(labels, dtype=int)


def compute_ranks(scores: np.ndarray) -> np.ndarray:
    order = np.argsort(-scores)
    ranks = np.empty_like(order)
    ranks[order] = np.arange(1, len(scores) + 1)
    return ranks


def rrf_scores(items: list[dict], k: int, signals: list[str]) -> np.ndarray:
    n = len(items)
    fused = np.zeros(n)
    for sig in signals:
        vals = np.array([item.get(sig, 0.0) or 0.0 for item in items], dtype=float)
        ranks = compute_ranks(vals)
        fused += 1.0 / (k + ranks)
    return fused


def logistic_regression_scores(items: list[dict], labels: np.ndarray,
                               signals: list[str]) -> np.ndarray:
    """5-fold cross-validated logistic regression probabilities."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.preprocessing import StandardScaler

    n = len(items)
    X = np.column_stack([
        np.array([item.get(sig, 0.0) or 0.0 for item in items], dtype=float)
        for sig in signals
    ])

    probs = np.zeros(n)
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    for train_idx, test_idx in skf.split(X, labels):
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X[train_idx])
        X_test = scaler.transform(X[test_idx])

        clf = LogisticRegression(max_iter=1000, random_state=42)
        clf.fit(X_train, labels[train_idx])
        probs[test_idx] = clf.predict_proba(X_test)[:, 1]

    return probs


def safe_auc(labels: np.ndarray, scores: np.ndarray) -> "float | None":
    from sklearn.metrics import roc_auc_score

    if len(np.unique(labels)) < 2:
        return None
    try:
        return float(roc_auc_score(labels, scores))
    except ValueError:
        return None


def inject_false_positives(labels: np.ndarray, fp_rate: float, rng) -> np.ndarray:
    """Inject false positives into clean items (0→1) at given rate."""
    noisy = labels.copy()
    clean_idx = np.where(labels == 0)[0]
    n_flip = max(1, int(len(clean_idx) * fp_rate))
    flip_idx = rng.choice(clean_idx, size=min(n_flip, len(clean_idx)), replace=False)
    noisy[flip_idx] = 1
    return noisy


def run_ablation(items: list[dict], labels: np.ndarray) -> dict:
    """Run all ablation variants and return AUC-ROC results."""
    results = {}

    # 1. Full RRF at default k
    scores = rrf_scores(items, DEFAULT_K, SIGNAL_KEYS)
    results["rrf_full"] = safe_auc(labels, scores)

    # 2. Single-signal baselines
    for sig in SIGNAL_KEYS:
        vals = np.array([item.get(sig, 0.0) or 0.0 for item in items], dtype=float)
        results[f"single_{sig}"] = safe_auc(labels, vals)

    # 3. Drop-one-signal
    for sig in SIGNAL_KEYS:
        remaining = [s for s in SIGNAL_KEYS if s != sig]
        scores = rrf_scores(items, DEFAULT_K, remaining)
        results[f"drop_{sig}"] = safe_auc(labels, scores)

    # 4. Logistic regression
    lr_probs = logistic_regression_scores(items, labels, SIGNAL_KEYS)
    results["logistic_regression"] = safe_auc(labels, lr_probs)

    # 5. RRF k sensitivity
    k_results = {}
    for k in K_VALUES:
        scores = rrf_scores(items, k, SIGNAL_KEYS)
        k_results[k] = safe_auc(labels, scores)
    results["rrf_k_sensitivity"] = k_results

    # 6. All subsets of size 2 and 3
    subset_results = {}
    for size in [2, 3]:
        for combo in combinations(SIGNAL_KEYS, size):
            key = "+".join(combo)
            scores = rrf_scores(items, DEFAULT_K, list(combo))
            subset_results[key] = safe_auc(labels, scores)
    results["signal_subsets"] = subset_results

    # 7. FP injection robustness: measure AUC degradation under noisy labels
    fp_results = {}
    rng = np.random.default_rng(42)
    for fp_rate in [0.05, 0.10, 0.20]:
        rate_runs = []
        for trial in range(10):
            noisy_labels = inject_false_positives(labels, fp_rate, rng)
            auc = safe_auc(noisy_labels, scores)
            rate_runs.append(auc)
        rate_runs = [v for v in rate_runs if v is not None]
        fp_results[f"fp_{int(fp_rate*100):02d}pct"] = {
            "mean_auc": round(float(np.mean(rate_runs)), 4) if rate_runs else None,
            "std_auc": round(float(np.std(rate_runs)), 4) if rate_runs else None,
            "n_trials": len(rate_runs),
        }
    results["fp_injection_robustness"] = fp_results

    # 8. 2-signal degraded mode: ConStat + SelfCritique only (closed-weight applicable)
    closed_weight_signals = ["s3_constat", "s4_selfcritique"]
    cw_scores = rrf_scores(items, DEFAULT_K, closed_weight_signals)
    results["closed_weight_2signal"] = safe_auc(labels, cw_scores)
    results["closed_weight_2signal_signals"] = closed_weight_signals

    return results


def format_latex_table(all_results: dict) -> str:
    """Generate a LaTeX table: methods × benchmarks."""
    benchmarks = sorted(all_results.keys())
    n_bench = len(benchmarks)

    # Collect all method rows
    rows = []

    # Full RRF
    row = [r"RRF (full, $k{=}60$)"]
    for bench in benchmarks:
        v = all_results[bench].get("rrf_full")
        row.append(f"{v:.3f}" if v is not None else "--")
    rows.append(row)

    # Single signals
    for sig in SIGNAL_KEYS:
        name = SIGNAL_NAMES.get(sig, sig)
        row = [f"Single: {name}"]
        for bench in benchmarks:
            v = all_results[bench].get(f"single_{sig}")
            row.append(f"{v:.3f}" if v is not None else "--")
        rows.append(row)

    # Drop-one
    for sig in SIGNAL_KEYS:
        name = SIGNAL_NAMES.get(sig, sig)
        row = [f"Drop: {name}"]
        for bench in benchmarks:
            v = all_results[bench].get(f"drop_{sig}")
            row.append(f"{v:.3f}" if v is not None else "--")
        rows.append(row)

    # Logistic regression
    row = ["Logistic Regression"]
    for bench in benchmarks:
        v = all_results[bench].get("logistic_regression")
        row.append(f"{v:.3f}" if v is not None else "--")
    rows.append(row)

    # k sensitivity
    for k in K_VALUES:
        row = [f"RRF ($k{{=}}{k}$)"]
        for bench in benchmarks:
            ks = all_results[bench].get("rrf_k_sensitivity", {})
            v = ks.get(k) if isinstance(ks, dict) else ks.get(str(k))
            row.append(f"{v:.3f}" if v is not None else "--")
        rows.append(row)

    # Build LaTeX
    col_spec = "l" + "c" * n_bench
    header = " & ".join(["Method"] + [b.replace("_", r"\_") for b in benchmarks])

    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{RRF ablation: AUC-ROC by aggregation method and benchmark.}",
        r"\label{tab:rrf-ablation}",
        rf"\begin{{tabular}}{{{col_spec}}}",
        r"\toprule",
        header + r" \\",
        r"\midrule",
    ]
    for row in rows:
        lines.append(" & ".join(row) + r" \\")
    lines += [
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table}",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="exp-003: RRF aggregation ablation analysis"
    )
    parser.add_argument(
        "--signal-dir", type=str, required=True,
        help="Directory containing per-model signal JSON files "
             "(signal_{model}_{bench}.json)"
    )
    parser.add_argument(
        "--labels-dir", type=str, required=True,
        help="Directory containing ground-truth contamination labels "
             "(contamination_labels_{bench}_d{dosage}.json)"
    )
    parser.add_argument(
        "--output-dir", type=str, required=True,
        help="Output directory for results"
    )
    parser.add_argument(
        "--benchmarks", type=str, nargs="+",
        default=["mmlu", "gsm8k", "arc_challenge", "humaneval"],
        help="Benchmarks to analyze"
    )
    parser.add_argument(
        "--dosage", type=int, default=None,
        help="Dosage level for label file selection (e.g., 50). "
             "If not set, looks for contamination_labels_{bench}.json"
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    signal_dir = Path(args.signal_dir)
    labels_dir = Path(args.labels_dir)

    all_results = {}

    for bench in args.benchmarks:
        log.info("=== Benchmark: %s ===", bench)

        # Find signal files for this benchmark
        signal_files = sorted(signal_dir.glob(f"signal_*_{bench}.json"))
        if not signal_files:
            signal_files = sorted(signal_dir.glob(f"*{bench}*.json"))
        if not signal_files:
            log.warning("No signal files found for %s, skipping", bench)
            continue

        items = load_signal_data([str(f) for f in signal_files])
        log.info("Loaded %d items from %d signal files", len(items), len(signal_files))

        # Find label file
        if args.dosage is not None:
            label_file = labels_dir / f"contamination_labels_{bench}_d{args.dosage}.json"
        else:
            label_file = labels_dir / f"contamination_labels_{bench}.json"

        if not label_file.exists():
            candidates = sorted(labels_dir.glob(f"contamination_labels_{bench}*.json"))
            if candidates:
                label_file = candidates[0]
                log.info("Using label file: %s", label_file)
            else:
                log.warning("No label file found for %s, skipping", bench)
                continue

        labels = load_labels(str(label_file))
        if len(labels) != len(items):
            log.warning(
                "Label count (%d) != item count (%d) for %s, skipping",
                len(labels), len(items), bench,
            )
            continue

        pos_rate = labels.mean()
        log.info("Labels: %d items, %.1f%% positive", len(labels), 100 * pos_rate)

        bench_results = run_ablation(items, labels)
        all_results[bench] = bench_results

        log.info(
            "RRF full AUC=%.4f | LR AUC=%.4f",
            bench_results.get("rrf_full") or 0,
            bench_results.get("logistic_regression") or 0,
        )
        for sig in SIGNAL_KEYS:
            auc = bench_results.get(f"single_{sig}")
            log.info("  Single %s: AUC=%.4f", sig, auc or 0)

    if not all_results:
        log.error("No benchmarks produced results. Check signal/label paths.")
        sys.exit(1)

    # Save JSON results
    results_path = output_dir / "rrf_ablation_results.json"
    with open(results_path, "w") as f:
        json.dump(all_results, f, indent=2)
    log.info("Results saved to %s", results_path)

    # Generate LaTeX table
    latex = format_latex_table(all_results)
    tex_path = output_dir / "rrf_ablation_table.tex"
    with open(tex_path, "w") as f:
        f.write(latex)
    log.info("LaTeX table saved to %s", tex_path)

    # Summary: best method per benchmark
    log.info("=== Summary ===")
    for bench, res in all_results.items():
        flat = {k: v for k, v in res.items()
                if isinstance(v, (int, float)) and v is not None}
        if flat:
            best_method = max(flat, key=flat.get)
            log.info("  %s: best=%s (AUC=%.4f)", bench, best_method, flat[best_method])


if __name__ == "__main__":
    main()
