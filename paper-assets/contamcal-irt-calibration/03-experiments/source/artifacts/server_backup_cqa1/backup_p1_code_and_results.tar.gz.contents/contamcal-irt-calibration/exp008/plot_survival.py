"""
exp-008 Signal Survival — visualization.
v2: Extended to N regimes; primary output is AUC heatmap (paper Figure 2).

Generates:
  1. AUC heatmap: signal x regime AUROC matrix
  2. Pairwise delta-AUC heatmap: AUC change between adjacent regime pairs

Input:  survival_report.json (from run_signal_survival.py)
Output: PDF files in output directory

Dependencies: matplotlib, seaborn (optional fallback to imshow), numpy
"""

import argparse
import json
import logging
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

logger = logging.getLogger(__name__)

SIGNAL_KEYS = ["s1_embedding", "s2_minkpp", "s3_constat", "s4_selfcritique"]
SIGNAL_LABELS = {
    "s1_embedding": "Embedding",
    "s2_minkpp": "Min-K%++",
    "s3_constat": "ConStat",
    "s4_selfcritique": "Self-Critique",
}


def _try_import_seaborn():
    try:
        import seaborn as sns
        return sns
    except ImportError:
        logger.warning("seaborn not available, falling back to matplotlib imshow")
        return None


def plot_auc_heatmap(report: dict, output_path: Path):
    """Signal x regime AUC heatmap (paper Figure 2 format)."""
    sns = _try_import_seaborn()

    auc_matrix = report["auc_matrix"]
    regime_names = report["regime_names"]

    signals = [k for k in SIGNAL_KEYS if k in auc_matrix]
    if not signals:
        logger.warning("No signals to plot")
        return

    sig_labels = [SIGNAL_LABELS[k] for k in signals]
    data = np.array([
        [auc_matrix[s].get(r, float("nan")) for r in regime_names]
        for s in signals
    ])

    fig, ax = plt.subplots(
        figsize=(max(3.5, 1.5 * len(regime_names)), max(3, 0.8 * len(signals)))
    )

    if sns is not None:
        sns.heatmap(
            data, annot=True, fmt=".3f", cmap="YlOrRd",
            xticklabels=regime_names, yticklabels=sig_labels,
            vmin=0.4, vmax=1.0, linewidths=0.5, linecolor="white",
            cbar_kws={"label": "AUROC", "shrink": 0.8},
            ax=ax,
        )
    else:
        im = ax.imshow(data, cmap="YlOrRd", vmin=0.4, vmax=1.0, aspect="auto")
        ax.set_xticks(range(len(regime_names)))
        ax.set_xticklabels(regime_names)
        ax.set_yticks(range(len(sig_labels)))
        ax.set_yticklabels(sig_labels)
        for i in range(len(signals)):
            for j in range(len(regime_names)):
                v = data[i, j]
                color = "white" if v > 0.75 else "black"
                ax.text(
                    j, i, f"{v:.3f}", ha="center", va="center",
                    fontsize=10, color=color,
                )
        fig.colorbar(im, ax=ax, label="AUROC", shrink=0.8)

    ax.set_title("Contamination Signal AUROC across Regimes", fontsize=12, pad=10)
    ax.tick_params(labelsize=10)
    ax.set_xlabel("")
    ax.set_ylabel("")

    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    logger.info("AUC heatmap saved to %s", output_path)


def plot_delta_auc_heatmap(report: dict, output_path: Path):
    """Pairwise delta-AUC heatmap between adjacent regime pairs."""
    sns = _try_import_seaborn()

    pairwise_tests = report.get("pairwise_tests", {})
    if not pairwise_tests:
        logger.warning("No pairwise tests to plot")
        return

    pair_keys = list(pairwise_tests.keys())
    signals = [k for k in SIGNAL_KEYS if k in next(iter(pairwise_tests.values()))]
    if not signals:
        logger.warning("No signals in pairwise tests")
        return

    sig_labels = [SIGNAL_LABELS[k] for k in signals]
    pair_labels = [k.replace("_vs_", " → ") for k in pair_keys]

    data = np.array([
        [
            (pairwise_tests[pk][s].get("auc_b", 0) or 0)
            - (pairwise_tests[pk][s].get("auc_a", 0) or 0)
            if s in pairwise_tests[pk]
            else float("nan")
            for pk in pair_keys
        ]
        for s in signals
    ])

    vmax = max(0.15, float(np.nanmax(np.abs(data))))
    fig, ax = plt.subplots(
        figsize=(max(3.5, 1.8 * len(pair_keys)), max(3, 0.8 * len(signals)))
    )

    if sns is not None:
        sns.heatmap(
            data, annot=True, fmt="+.3f", cmap="RdBu_r",
            xticklabels=pair_labels, yticklabels=sig_labels,
            vmin=-vmax, vmax=vmax, center=0,
            linewidths=0.5, linecolor="white",
            cbar_kws={"label": "Δ AUROC", "shrink": 0.8},
            ax=ax,
        )
    else:
        im = ax.imshow(
            data, cmap="RdBu_r", vmin=-vmax, vmax=vmax, aspect="auto",
        )
        ax.set_xticks(range(len(pair_labels)))
        ax.set_xticklabels(pair_labels)
        ax.set_yticks(range(len(sig_labels)))
        ax.set_yticklabels(sig_labels)
        for i in range(len(signals)):
            for j in range(len(pair_keys)):
                v = data[i, j]
                ax.text(
                    j, i, f"{v:+.3f}", ha="center", va="center", fontsize=10,
                )
        fig.colorbar(im, ax=ax, label="Δ AUROC", shrink=0.8)

    ax.set_title(
        "Signal AUROC Change between Adjacent Regimes", fontsize=12, pad=10,
    )
    ax.tick_params(labelsize=10)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    logger.info("Delta AUC heatmap saved to %s", output_path)


def main():
    parser = argparse.ArgumentParser(
        description="exp-008: Plot signal survival figures"
    )
    parser.add_argument("--report-file", type=str,
                        help="Path to survival_report.json")
    parser.add_argument("--output-dir", type=str, default="./exp008_output")
    parser.add_argument("--dry-run", action="store_true",
                        help="Generate report from mock data first")
    parser.add_argument("--max-items", type=int, default=None)
    parser.add_argument("--regime-names", nargs="+", default=None,
                        help="Regime names for dry-run (default: SFT RL)")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        from run_signal_survival import generate_mock_data
        from signal_survival_analysis import run_survival_analysis, save_report

        regime_names = args.regime_names or ["SFT", "RL"]
        max_items = args.max_items or 100
        regime_signals, labels = generate_mock_data(
            n_items=max_items, regime_names=regime_names,
        )
        report = run_survival_analysis(regime_signals, labels)
        save_report(report, output_dir)
    else:
        if not args.report_file:
            parser.error("--report-file required (unless --dry-run)")
        with open(args.report_file) as f:
            report = json.load(f)

    plot_auc_heatmap(report, output_dir / "survival_auc_heatmap.pdf")
    plot_delta_auc_heatmap(report, output_dir / "survival_delta_auc.pdf")

    logger.info("Plots saved to %s", output_dir)


if __name__ == "__main__":
    main()
