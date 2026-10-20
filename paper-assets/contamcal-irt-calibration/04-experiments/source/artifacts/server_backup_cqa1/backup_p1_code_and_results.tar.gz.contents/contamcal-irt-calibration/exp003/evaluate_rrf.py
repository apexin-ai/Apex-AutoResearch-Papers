"""
exp-003 Evaluation: Compare RRF vs Ablation Methods.

Computes AUC-ROC, Average Precision, precision@k for all aggregation
methods. Generates ROC curves, score distribution plots, and FP
robustness degradation curves.

Supports --mock mode for testing with synthetic data.
"""

import argparse
import json
import logging
import sys
from pathlib import Path

import numpy as np
from sklearn.metrics import roc_auc_score, average_precision_score, roc_curve

sys.path.insert(0, str(Path(__file__).parent))
from rrf_aggregation import (
    load_signal_files, detect_available_signals, rrf_fuse,
    normalize_minmax, SIGNAL_KEYS, DEFAULT_K,
    SIGNAL_ROOT, LABELS_ROOT, BENCHMARKS,
)
from ablations import (
    load_labels, equal_weight_rank_avg, single_signal_scores,
    calibrated_weighted_rrf, degraded_2signal,
    run_all_ablations, run_all_ablations_from_items,
    fp_robustness_test,
)

logger = logging.getLogger(__name__)


def compute_metrics(scores: np.ndarray, labels: np.ndarray) -> dict:
    """Compute AUC-ROC, Average Precision, and precision@k."""
    n = min(len(scores), len(labels))
    scores, labels = scores[:n], labels[:n]

    if len(np.unique(labels)) < 2:
        return {"auc_roc": float("nan"), "avg_precision": float("nan"),
                "precision_at_100": float("nan"), "precision_at_500": float("nan")}

    auc = roc_auc_score(labels, scores)
    ap = average_precision_score(labels, scores)

    sorted_idx = np.argsort(-scores)
    p100 = float(labels[sorted_idx[:100]].mean()) if n >= 100 else float("nan")
    p500 = float(labels[sorted_idx[:500]].mean()) if n >= 500 else float("nan")

    return {
        "auc_roc": float(auc),
        "avg_precision": float(ap),
        "precision_at_100": p100,
        "precision_at_500": p500,
    }


def plot_roc_curves(method_scores: dict, labels: np.ndarray,
                    output_path: str, title: str = "ROC Curves"):
    """Plot ROC curves for main methods (excludes FP variants)."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        logger.warning("matplotlib unavailable, skipping ROC plot")
        return

    n = min(min(len(s) for s in method_scores.values()), len(labels))
    labels_n = labels[:n]
    if len(np.unique(labels_n)) < 2:
        logger.warning("Single-class labels, skipping ROC plot")
        return

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    main_methods = [m for m in method_scores if not m.startswith("fp_")]

    for method in sorted(main_methods):
        scores = method_scores[method][:n]
        fpr, tpr, _ = roc_curve(labels_n, scores)
        auc = roc_auc_score(labels_n, scores)
        ax.plot(fpr, tpr, label=f"{method} (AUC={auc:.3f})")

    ax.plot([0, 1], [0, 1], "k--", alpha=0.3)
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title(title)
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    logger.info("ROC plot saved to %s", output_path)


def plot_score_distributions(method_scores: dict, labels: np.ndarray,
                             output_path: str, title: str = "Score Distributions"):
    """Histogram of exposure scores split by clean/contaminated."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        logger.warning("matplotlib unavailable, skipping distribution plot")
        return

    main_methods = sorted(m for m in method_scores if not m.startswith("fp_"))
    n_methods = len(main_methods)
    if n_methods == 0:
        return

    ncols = min(3, n_methods)
    nrows = (n_methods + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(5 * ncols, 4 * nrows))
    if n_methods == 1:
        axes = np.array([axes])
    axes = np.atleast_1d(axes).flatten()

    n = min(min(len(s) for s in method_scores.values()), len(labels))
    labels_n = labels[:n]
    clean_mask = labels_n == 0
    contam_mask = labels_n == 1

    for i, method in enumerate(main_methods):
        ax = axes[i]
        scores = method_scores[method][:n]
        bins = np.linspace(0, 1, 50)
        if np.any(clean_mask):
            ax.hist(scores[clean_mask], bins=bins, alpha=0.6,
                    label="Clean", color="steelblue")
        if np.any(contam_mask):
            ax.hist(scores[contam_mask], bins=bins, alpha=0.6,
                    label="Contaminated", color="tomato")
        ax.set_title(method, fontsize=10)
        ax.set_xlabel("Exposure Score")
        ax.set_ylabel("Count")
        ax.legend(fontsize=8)

    for i in range(n_methods, len(axes)):
        axes[i].set_visible(False)

    fig.suptitle(title, fontsize=12)
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    logger.info("Distribution plot saved to %s", output_path)


def plot_fp_robustness(method_scores: dict, labels: np.ndarray,
                       output_path: str):
    """AUC degradation curve under increasing FP injection rates."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        return

    n = min(min(len(s) for s in method_scores.values()), len(labels))
    labels_n = labels[:n]
    if len(np.unique(labels_n)) < 2:
        return

    # Parse fp_{rate}pct_{method} keys
    fp_data = {}
    for key, scores in method_scores.items():
        if not key.startswith("fp_"):
            continue
        parts = key.split("_", 3)  # fp, 05pct, method...
        rate = int(parts[1].replace("pct", ""))
        method = "_".join(parts[2:])
        if method not in fp_data:
            fp_data[method] = {}
        fp_data[method][rate] = roc_auc_score(labels_n, np.array(scores[:n]))

    if not fp_data:
        return

    # Add 0% baseline
    for key, scores in method_scores.items():
        if key.startswith("fp_"):
            continue
        if key in fp_data:
            fp_data[key][0] = roc_auc_score(labels_n, np.array(scores[:n]))

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    for method, rate_aucs in sorted(fp_data.items()):
        rates = sorted(rate_aucs.keys())
        aucs = [rate_aucs[r] for r in rates]
        ax.plot(rates, aucs, "o-", label=method)

    ax.set_xlabel("FP Injection Rate (%)")
    ax.set_ylabel("AUC-ROC")
    ax.set_title("Robustness to False Positive Injection")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    logger.info("FP robustness plot saved to %s", output_path)


def format_metrics_table(all_metrics: dict) -> str:
    """Format metrics as a markdown table."""
    lines = [
        "| Method | AUC-ROC | Avg Precision | P@100 | P@500 |",
        "|--------|---------|---------------|-------|-------|",
    ]
    for method in sorted(all_metrics):
        m = all_metrics[method]
        def fmt(v):
            return f"{v:.4f}" if not np.isnan(v) else "N/A"
        lines.append(
            f"| {method} | {fmt(m['auc_roc'])} | {fmt(m['avg_precision'])} "
            f"| {fmt(m['precision_at_100'])} | {fmt(m['precision_at_500'])} |"
        )
    return "\n".join(lines)


def generate_mock_data(n_items: int = 1000, n_contaminated: int = 100,
                       seed: int = 42) -> tuple:
    """Generate synthetic signal data for pipeline testing."""
    rng = np.random.RandomState(seed)
    labels = np.zeros(n_items, dtype=int)
    contam_idx = rng.choice(n_items, size=n_contaminated, replace=False)
    labels[contam_idx] = 1

    items = []
    for i in range(n_items):
        base = 0.3 if labels[i] == 0 else 0.7
        items.append({
            "index": i,
            "benchmark": "mock",
            "s1_embedding": float(np.clip(rng.normal(base, 0.15), 0, 1)),
            "s2_minkpp": float(np.clip(rng.normal(base + 0.05, 0.2), 0, 1)),
            "s3_constat": float(np.clip(rng.normal(base - 0.05, 0.18), 0, 1)),
            "s4_selfcritique": float(np.clip(rng.normal(base + 0.1, 0.22), 0, 1)),
        })

    return items, labels


def run_mock_evaluation(output_dir: str):
    """Full evaluation pipeline on synthetic mock data."""
    logger.info("=== Mock Evaluation ===")
    items, labels = generate_mock_data()
    logger.info("Generated %d items (%d contaminated)", len(items), int(labels.sum()))

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = run_all_ablations_from_items(items, labels)

    # Compute metrics
    metrics = {}
    for method, scores in results.items():
        metrics[method] = compute_metrics(scores, labels)

    table = format_metrics_table(metrics)
    logger.info("\n%s", table)

    with open(output_dir / "mock_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    # Plots
    plot_roc_curves(results, labels,
                    str(output_dir / "mock_roc_curves.png"),
                    "Mock Data: ROC Curves")
    plot_score_distributions(results, labels,
                             str(output_dir / "mock_score_dist.png"),
                             "Mock Data: Score Distributions")
    plot_fp_robustness(results, labels,
                       str(output_dir / "mock_fp_robustness.png"))

    logger.info("Mock evaluation complete. Results in %s", output_dir)


def main():
    parser = argparse.ArgumentParser(
        description="exp-003: Evaluate RRF aggregation methods"
    )
    parser.add_argument("--mock", action="store_true",
                        help="Run evaluation on synthetic mock data")
    parser.add_argument("--signal-root", type=str, default=SIGNAL_ROOT)
    parser.add_argument("--labels-dir", type=str, default=LABELS_ROOT)
    parser.add_argument("--signal-dir", type=str, default=None,
                        help="Single model signal dir")
    parser.add_argument("--benchmark", type=str, default=None,
                        choices=BENCHMARKS)
    parser.add_argument("--dosage", type=str, default=None)
    parser.add_argument("--k", type=int, default=DEFAULT_K)
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--all", action="store_true",
                        help="Evaluate all model-dosage-benchmark combos")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    if args.mock:
        run_mock_evaluation(args.output_dir)
        return

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.all:
        signal_root = Path(args.signal_root)
        all_metrics = {}

        for model_dir in sorted(signal_root.iterdir()):
            if not model_dir.is_dir():
                continue
            model_id = model_dir.name
            parts = model_id.split("_")
            dosage = next(
                (p for p in parts if p.startswith("d") and p[1:].isdigit()), None
            )
            if not dosage or dosage == "d000":
                continue

            for bench in BENCHMARKS:
                try:
                    labels = load_labels(args.labels_dir, bench, dosage)
                except FileNotFoundError:
                    continue

                items = load_signal_files(str(model_dir), bench)
                if not items:
                    continue

                key = f"{model_id}/{bench}"
                logger.info("Evaluating %s ...", key)

                results = run_all_ablations(str(model_dir), bench, labels, k=args.k)
                metrics = {}
                for method, scores in results.items():
                    metrics[method] = compute_metrics(scores, labels)
                all_metrics[key] = metrics

                combo_dir = output_dir / model_id / bench
                combo_dir.mkdir(parents=True, exist_ok=True)
                plot_roc_curves(results, labels,
                                str(combo_dir / "roc_curves.png"),
                                f"ROC: {model_id} / {bench}")
                plot_score_distributions(results, labels,
                                         str(combo_dir / "score_dist.png"),
                                         f"Dist: {model_id} / {bench}")
                plot_fp_robustness(results, labels,
                                   str(combo_dir / "fp_robustness.png"))

        with open(output_dir / "all_metrics.json", "w") as f:
            json.dump(all_metrics, f, indent=2)

        for key, metrics in all_metrics.items():
            logger.info("\n=== %s ===", key)
            logger.info("\n%s", format_metrics_table(metrics))
        return

    # Single evaluation mode
    if not args.signal_dir or not args.benchmark or not args.dosage:
        parser.error("Need --signal-dir, --benchmark, --dosage (or use --mock / --all)")

    labels = load_labels(args.labels_dir, args.benchmark, args.dosage)
    results = run_all_ablations(args.signal_dir, args.benchmark, labels, k=args.k)

    metrics = {}
    for method, scores in results.items():
        metrics[method] = compute_metrics(scores, labels)

    table = format_metrics_table(metrics)
    logger.info("\n%s", table)

    model_id = Path(args.signal_dir).name
    with open(output_dir / f"metrics_{model_id}_{args.benchmark}.json", "w") as f:
        json.dump(metrics, f, indent=2)

    plot_roc_curves(results, labels,
                    str(output_dir / f"roc_{model_id}_{args.benchmark}.png"),
                    f"ROC: {model_id} / {args.benchmark}")
    plot_score_distributions(results, labels,
                             str(output_dir / f"dist_{model_id}_{args.benchmark}.png"),
                             f"Dist: {model_id} / {args.benchmark}")
    plot_fp_robustness(results, labels,
                       str(output_dir / f"fp_robust_{model_id}_{args.benchmark}.png"))


if __name__ == "__main__":
    main()
