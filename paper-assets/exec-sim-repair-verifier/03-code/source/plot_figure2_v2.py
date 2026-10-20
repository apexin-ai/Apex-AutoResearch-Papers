#!/usr/bin/env python3
# Figure 2: CLS/CWM/TRAJ accuracy across two models and two granularities.
# Shows gap amplification from function to repo level with multi-seed error bars.

import argparse
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --- Data from Tables 1 & 3 ---
# Function-level: Qwen3-4B (5 seeds), DeepSeek-6.7B (2 seeds)
# Repo-level: Qwen3-8B (3 seeds CLS/TRAJ), DeepSeek-6.7B (2-3 seeds)
# n_seeds tracks seed count for each cell; 1 = single-seed placeholder
DATA = {
    "func": {
        "CLS":  {"qwen": {"mean": 88.43, "std": 0.78, "n_seeds": 5},
                 "deepseek": {"mean": 86.85, "std": 0.11, "n_seeds": 2}},
        "CWM":  {"qwen": {"mean": 87.19, "std": 0.37, "n_seeds": 5},
                 "deepseek": {"mean": 86.83, "std": 1.49, "n_seeds": 2}},
        "TRAJ": {"qwen": {"mean": 86.30, "std": 0.97, "n_seeds": 5},
                 "deepseek": {"mean": 84.16, "std": 1.30, "n_seeds": 2}},
    },
    "repo": {
        "CLS":  {"qwen": {"mean": 84.83, "std": 0.67, "n_seeds": 3},
                 "deepseek": {"mean": 84.38, "std": 2.50, "n_seeds": 2}},
        "CWM":  {"qwen": {"mean": 66.48, "std": 1.15, "n_seeds": 3},
                 "deepseek": {"mean": 58.30, "std": 2.82, "n_seeds": 3}},
        "TRAJ": {"qwen": {"mean": 72.91, "std": 3.61, "n_seeds": 3},
                 "deepseek": {"mean": 77.08, "std": 3.61, "n_seeds": 3}},
    },
}

FORMULATIONS = ["CLS", "CWM", "TRAJ"]
PANELS = [
    ("func", "(a) Function-level"),
    ("repo", "(b) Repo-level"),
]

COLOR_QWEN = "#4878A8"
COLOR_DEEPSEEK = "#E8853A"
HATCH_SINGLE_SEED = "///"


def setup_style():
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "DejaVu Serif"],
        "font.size": 10,
        "axes.labelsize": 11,
        "axes.titlesize": 11,
        "axes.linewidth": 0.8,
        "axes.edgecolor": "#333333",
        "xtick.labelsize": 10,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.05,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })


def plot_panel(ax, panel_key, panel_title):
    x = np.arange(len(FORMULATIONS))
    width = 0.32

    qwen_means = [DATA[panel_key][f]["qwen"]["mean"] for f in FORMULATIONS]
    qwen_stds = [DATA[panel_key][f]["qwen"]["std"] for f in FORMULATIONS]
    qwen_seeds = [DATA[panel_key][f]["qwen"]["n_seeds"] for f in FORMULATIONS]

    ds_means = [DATA[panel_key][f]["deepseek"]["mean"] for f in FORMULATIONS]
    ds_stds = [DATA[panel_key][f]["deepseek"]["std"] for f in FORMULATIONS]
    ds_seeds = [DATA[panel_key][f]["deepseek"]["n_seeds"] for f in FORMULATIONS]

    # Only show error bars when n_seeds > 1
    qwen_yerr = [s if n > 1 else 0.0 for s, n in zip(qwen_stds, qwen_seeds)]
    ds_yerr = [s if n > 1 else 0.0 for s, n in zip(ds_stds, ds_seeds)]

    bars_q = ax.bar(
        x - width / 2, qwen_means, width,
        yerr=qwen_yerr, capsize=3,
        color=COLOR_QWEN, edgecolor="black", linewidth=0.5,
        label="Qwen3", error_kw={"linewidth": 0.8},
    )
    bars_d = ax.bar(
        x + width / 2, ds_means, width,
        yerr=ds_yerr, capsize=3,
        color=COLOR_DEEPSEEK, edgecolor="black", linewidth=0.5,
        label="DeepSeek", error_kw={"linewidth": 0.8},
    )

    # Hatch single-seed bars to visually distinguish placeholders
    for i, (bq, bd) in enumerate(zip(bars_q, bars_d)):
        if qwen_seeds[i] == 1:
            bq.set_hatch(HATCH_SINGLE_SEED)
            bq.set_alpha(0.7)
        if ds_seeds[i] == 1:
            bd.set_hatch(HATCH_SINGLE_SEED)
            bd.set_alpha(0.7)

    # Value labels above bars
    for bars, stds, seeds in [(bars_q, qwen_stds, qwen_seeds),
                               (bars_d, ds_stds, ds_seeds)]:
        for bar, std, n in zip(bars, stds, seeds):
            h = bar.get_height()
            if h > 0:
                offset = std + 1.5 if n > 1 else 1.2
                label_text = f"{h:.1f}"
                if n == 1:
                    label_text += "*"
                ax.text(
                    bar.get_x() + bar.get_width() / 2, h + offset,
                    label_text, ha="center", va="bottom", fontsize=7.5,
                )

    ax.set_xticks(x)
    ax.set_xticklabels(FORMULATIONS)
    ax.set_xlabel("Formulation")
    ax.set_ylabel("Accuracy (%)")
    ax.set_title(panel_title, fontweight="medium")

    # Majority baseline (repo-level only)
    if panel_key == "repo":
        ax.axhline(y=72.96, color="#888888", linestyle="--", linewidth=0.9,
                    zorder=1)
        ax.text(len(FORMULATIONS) - 0.5, 73.8, "Majority baseline",
                ha="right", va="bottom", fontsize=7.5, color="#666666",
                fontstyle="italic")

    ax.set_ylim(0, 105)
    ax.yaxis.set_major_locator(plt.MultipleLocator(20))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(10))
    ax.grid(axis="y", linewidth=0.3, color="#cccccc", zorder=0)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def main():
    parser = argparse.ArgumentParser(
        description="Plot Figure 2: gap amplification from function to repo level."
    )
    parser.add_argument("--output_dir", default="artifacts/",
                        help="Output directory (default: artifacts/)")
    parser.add_argument("--format", choices=["pdf", "png", "both"],
                        default="both", help="Output format (default: both)")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    setup_style()

    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

    for ax, (key, title) in zip(axes, PANELS):
        plot_panel(ax, key, title)

    axes[0].legend(loc="upper right", frameon=True, fancybox=False,
                   edgecolor="#999999")
    axes[1].set_ylabel("")

    # Footnote for single-seed markers
    has_single = any(
        DATA[pk][f][m]["n_seeds"] == 1
        for pk in DATA for f in FORMULATIONS for m in ["qwen", "deepseek"]
    )
    if has_single:
        fig.text(0.5, -0.02, "* single seed (awaiting multi-seed replication); "
                 "hatched bars = no error bar available",
                 ha="center", fontsize=8, fontstyle="italic", color="#666666")

    fig.tight_layout(w_pad=2.5)

    stem = os.path.join(args.output_dir, "figure2_v2")
    if args.format in ("pdf", "both"):
        fig.savefig(f"{stem}.pdf")
        print(f"Saved {stem}.pdf")
    if args.format in ("png", "both"):
        fig.savefig(f"{stem}.png")
        print(f"Saved {stem}.png")
    plt.close(fig)


if __name__ == "__main__":
    main()
