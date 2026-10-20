"""
exp-008: Signal Survival — AUC computation, bootstrap CI, heatmap visualization.

Core analysis module for the signal survival experiment. Computes:
  - AUC matrix: signal × regime AUROC for contamination detection
  - Bootstrap confidence intervals for each AUC
  - Heatmap visualization (signal × regime)
  - Signal trajectory plots across regimes

Input:  regime_signals = OrderedDict{regime_name: {signal_key: [records]}}, labels = {index: 0|1}
Output: AUC matrix, CI matrix, PDF figures, JSON report

Dependencies: numpy, scipy, sklearn, matplotlib
"""

import json
import logging
from collections import OrderedDict
from pathlib import Path

import numpy as np
from sklearn.metrics import roc_auc_score

logger = logging.getLogger(__name__)

SIGNAL_KEYS = ["s1_embedding", "s2_minkpp", "s3_constat", "s4_selfcritique"]
SIGNAL_LABELS = {
    "s1_embedding": "Embedding",
    "s2_minkpp": "Min-K%++",
    "s3_constat": "ConStat",
    "s4_selfcritique": "Self-Critique",
}


# ── AUC computation ──

def extract_signal_values(
    records: list[dict], signal_key: str, labels: dict[int, int],
) -> tuple[np.ndarray, np.ndarray]:
    """Extract aligned (signal_value, label) arrays from records."""
    values, labs = [], []
    for r in records:
        idx = r["index"]
        val = r.get(signal_key)
        if val is None or idx not in labels:
            continue
        values.append(float(val))
        labs.append(labels[idx])
    return np.array(values), np.array(labs)


def compute_auc(values: np.ndarray, labels: np.ndarray) -> float | None:
    """Compute AUROC, handling edge cases."""
    mask = ~(np.isnan(values) | np.isnan(labels))
    v, lab = values[mask], labels[mask].astype(int)
    if lab.sum() == 0 or lab.sum() == len(lab):
        return None
    if len(v) < 10:
        return None
    try:
        return float(roc_auc_score(lab, v))
    except ValueError:
        return None


def compute_auc_matrix(
    regime_signals: OrderedDict,
    labels: dict[int, int],
    regime_names: list[str],
) -> dict[str, dict[str, float | None]]:
    """Compute signal × regime AUC matrix.

    Returns: {signal_key: {regime_name: auc_value}}
    """
    matrix = {}
    for sig_key in SIGNAL_KEYS:
        matrix[sig_key] = {}
        for rname in regime_names:
            rsigs = regime_signals.get(rname, {})
            records = rsigs.get(sig_key, [])
            if not records:
                matrix[sig_key][rname] = None
                continue
            values, labs = extract_signal_values(records, sig_key, labels)
            auc = compute_auc(values, labs)
            matrix[sig_key][rname] = round(auc, 4) if auc is not None else None
    return matrix


def compute_bootstrap_ci(
    regime_signals: OrderedDict,
    labels: dict[int, int],
    regime_names: list[str],
    n_bootstrap: int = 1000,
    ci_level: float = 0.95,
    max_items: int | None = None,
    seed: int = 42,
) -> dict[str, dict[str, tuple[float, float] | None]]:
    """Bootstrap confidence intervals for each signal × regime AUC.

    Returns: {signal_key: {regime_name: (ci_low, ci_high)}}
    """
    rng = np.random.RandomState(seed)
    alpha = (1 - ci_level) / 2

    ci_matrix = {}
    for sig_key in SIGNAL_KEYS:
        ci_matrix[sig_key] = {}
        for rname in regime_names:
            rsigs = regime_signals.get(rname, {})
            records = rsigs.get(sig_key, [])
            if not records:
                ci_matrix[sig_key][rname] = None
                continue

            values, labs = extract_signal_values(records, sig_key, labels)
            if max_items and len(values) > max_items:
                values = values[:max_items]
                labs = labs[:max_items]

            if labs.sum() == 0 or labs.sum() == len(labs) or len(values) < 10:
                ci_matrix[sig_key][rname] = None
                continue

            aucs = []
            n = len(values)
            for _ in range(n_bootstrap):
                idx = rng.randint(0, n, size=n)
                v_boot = values[idx]
                l_boot = labs[idx]
                if l_boot.sum() == 0 or l_boot.sum() == len(l_boot):
                    continue
                try:
                    aucs.append(roc_auc_score(l_boot, v_boot))
                except ValueError:
                    continue

            if len(aucs) < n_bootstrap * 0.5:
                ci_matrix[sig_key][rname] = None
            else:
                ci_matrix[sig_key][rname] = (
                    round(float(np.percentile(aucs, 100 * alpha)), 4),
                    round(float(np.percentile(aucs, 100 * (1 - alpha))), 4),
                )
    return ci_matrix


# ── Visualization ──

def plot_auc_heatmap(
    auc_matrix: dict,
    ci_matrix: dict | None,
    regime_names: list[str],
    output_path: Path,
    title_suffix: str = "",
):
    """Signal × regime AUC heatmap with optional CI annotations."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    signals = [k for k in SIGNAL_KEYS if k in auc_matrix]
    if not signals:
        logger.warning("No signals to plot")
        return

    clean_names = [r.replace("\n", " ") for r in regime_names]
    sig_labels = [SIGNAL_LABELS[k] for k in signals]

    data = np.array([
        [auc_matrix[s].get(r) if auc_matrix[s].get(r) is not None else float("nan")
         for r in regime_names]
        for s in signals
    ], dtype=float)

    fig, ax = plt.subplots(
        figsize=(max(4, 2.0 * len(regime_names)), max(2.5, 0.9 * len(signals)))
    )

    cmap = plt.cm.YlOrRd
    im = ax.imshow(data, cmap=cmap, vmin=0.4, vmax=1.0, aspect="auto")

    ax.set_xticks(range(len(clean_names)))
    ax.set_xticklabels(clean_names, fontsize=9, ha="center")
    ax.set_yticks(range(len(sig_labels)))
    ax.set_yticklabels(sig_labels, fontsize=10)

    for i in range(len(signals)):
        for j in range(len(regime_names)):
            v = data[i, j]
            if np.isnan(v):
                txt = "N/A"
                color = "gray"
            else:
                txt = f"{v:.3f}"
                if ci_matrix and signals[i] in ci_matrix:
                    ci = ci_matrix[signals[i]].get(regime_names[j])
                    if ci:
                        txt += f"\n[{ci[0]:.2f},{ci[1]:.2f}]"
                color = "white" if v > 0.72 else "black"
            ax.text(j, i, txt, ha="center", va="center", fontsize=8, color=color)

    fig.colorbar(im, ax=ax, label="AUROC", shrink=0.8, pad=0.02)
    ax.set_title(f"Signal × Regime AUROC{title_suffix}", fontsize=11, pad=8)

    for edge in ["top", "bottom", "left", "right"]:
        ax.spines[edge].set_visible(False)

    fig.tight_layout()
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    logger.info("Heatmap saved to %s", output_path)


def plot_signal_trajectory(
    auc_matrix: dict,
    regime_names: list[str],
    output_path: Path,
):
    """Line plot of AUC trajectories across regimes for each signal."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    signals = [k for k in SIGNAL_KEYS if k in auc_matrix]
    if not signals:
        return

    clean_names = [r.replace("\n", " ") for r in regime_names]
    colors = {"s1_embedding": "#4C72B0", "s2_minkpp": "#DD8452",
              "s3_constat": "#55A868", "s4_selfcritique": "#C44E52"}
    markers = {"s1_embedding": "o", "s2_minkpp": "s",
               "s3_constat": "D", "s4_selfcritique": "^"}

    fig, ax = plt.subplots(figsize=(max(4, 1.5 * len(regime_names)), 3.5))

    x = np.arange(len(regime_names))
    for sig_key in signals:
        vals = [auc_matrix[sig_key].get(r) for r in regime_names]
        y = [v if v is not None else float("nan") for v in vals]
        ax.plot(
            x, y,
            marker=markers.get(sig_key, "o"),
            color=colors.get(sig_key, "gray"),
            label=SIGNAL_LABELS[sig_key],
            linewidth=2, markersize=7,
        )

    ax.axhline(0.5, color="gray", linestyle="--", linewidth=0.8, alpha=0.6)
    ax.set_xticks(x)
    ax.set_xticklabels(clean_names, fontsize=9)
    ax.set_ylabel("AUROC", fontsize=10)
    ax.set_ylim(0.35, 1.05)
    ax.set_title("Signal AUC Trajectory across Regimes", fontsize=11)
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    logger.info("Trajectory plot saved to %s", output_path)


# ── Report I/O ──

def save_analysis_report(report: dict, output_dir: Path | str):
    """Save full analysis report as JSON."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    def convert(obj):
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, tuple):
            return list(obj)
        raise TypeError(f"Object of type {type(obj)} not serializable")

    out_path = output_dir / "survival_report.json"
    with open(out_path, "w") as f:
        json.dump(report, f, indent=2, default=convert)
    logger.info("Report saved to %s", out_path)

    # Also save a concise AUC-only summary
    summary = {
        "regime_names": report["regime_names"],
        "benchmarks": report["benchmarks"],
    }
    for bench in report["benchmarks"]:
        summary[bench] = {}
        auc_data = report["auc_results"].get(bench, {})
        for sig_key in SIGNAL_KEYS:
            if sig_key in auc_data:
                summary[bench][sig_key] = auc_data[sig_key]

    summary_path = output_dir / "auc_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2, default=convert)
    logger.info("AUC summary saved to %s", summary_path)


# ── Standalone CLI ──

def main():
    """Standalone analysis on pre-computed signals."""
    import argparse

    parser = argparse.ArgumentParser(
        description="exp-008: Analyze signal survival from pre-computed data"
    )
    parser.add_argument("--report-file", type=str,
                        help="Path to survival_report.json for re-plotting")
    parser.add_argument("--output-dir", type=str, default="./exp008_output")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.report_file:
        with open(args.report_file) as f:
            report = json.load(f)

        regime_names = report["regime_names"]
        auc_results = report["auc_results"]
        ci_results = report.get("bootstrap_ci", {})

        for bench in report["benchmarks"]:
            if bench in auc_results:
                ci = ci_results.get(bench, {})
                plot_auc_heatmap(
                    auc_results[bench], ci, regime_names,
                    output_dir / f"auc_heatmap_{bench}.pdf",
                    title_suffix=f" ({bench})",
                )

        # Aggregate
        benchmarks = report["benchmarks"]
        agg_auc = {}
        for sig_key in SIGNAL_KEYS:
            agg_auc[sig_key] = {}
            for rname in regime_names:
                vals = [
                    auc_results[b][sig_key][rname]
                    for b in benchmarks
                    if sig_key in auc_results.get(b, {})
                    and rname in auc_results[b].get(sig_key, {})
                    and auc_results[b][sig_key][rname] is not None
                ]
                agg_auc[sig_key][rname] = round(float(np.mean(vals)), 4) if vals else None

        plot_auc_heatmap(agg_auc, {}, regime_names, output_dir / "survival_auc_heatmap.pdf")
        plot_signal_trajectory(agg_auc, regime_names, output_dir / "signal_trajectory.pdf")

    elif args.dry_run:
        from run_signal_survival import generate_mock_data
        all_data, all_labels, regime_names = generate_mock_data(n_items=200)

        for bench in all_data:
            auc = compute_auc_matrix(all_data[bench], all_labels[bench], regime_names)
            ci = compute_bootstrap_ci(
                all_data[bench], all_labels[bench], regime_names, n_bootstrap=500,
            )
            plot_auc_heatmap(
                auc, ci, regime_names,
                output_dir / f"auc_heatmap_{bench}.pdf",
                title_suffix=f" ({bench}, mock)",
            )
            print(f"\n{bench}:")
            for sig_key in SIGNAL_KEYS:
                if sig_key not in auc:
                    continue
                vals = " | ".join(
                    f"{r}: {auc[sig_key].get(r, 'N/A')}"
                    for r in regime_names
                )
                print(f"  {SIGNAL_LABELS[sig_key]}: {vals}")

        logger.info("Dry-run complete. Outputs in %s", output_dir)

    else:
        parser.error("Provide --report-file or --dry-run")


if __name__ == "__main__":
    main()
