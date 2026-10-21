#!/usr/bin/env python3
"""exp-003 decoding ablation: 4-config pairwise AUC grouped bar chart + summary table.
Input:  artifacts/exp003_analysis.json (or built-in data)
Output: artifacts/exp003_decoding_ablation.pdf, .png, .tex
"""

import json
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
ARTIFACT_DIR = ROOT / "artifacts"
JSON_PATH = ARTIFACT_DIR / "exp003_analysis.json"

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------
FALLBACK_AUC = {
    "Config1-Greedy":  {"0v1": 0.9797, "1v2": 0.6893, "2v3": 0.5613, "3v4": 0.5404, "4v5": 0.5139},
    "Config2-Nuc09":   {"0v1": 0.9946, "1v2": 0.6866, "2v3": 0.5917, "3v4": 0.5466, "4v5": 0.5068},
    "Config3-T07":     {"0v1": 0.9878, "1v2": 0.6887, "2v3": 0.5902, "3v4": 0.5393, "4v5": 0.5349},
    "Config4-T12":     {"0v1": 0.9982, "1v2": 0.7039, "2v3": 0.5823, "3v4": 0.5293, "4v5": 0.5237},
}

CONFIG_LABELS = {
    "Config1-Greedy": "Greedy",
    "Config2-Nuc09":  "Nuc p=.9, T=1.0",
    "Config3-T07":    "Nuc p=.95, T=0.7",
    "Config4-T12":    "Nuc p=.95, T=1.2",
}

DEPTH_PAIRS = ["0v1", "1v2", "2v3", "3v4", "4v5"]
DEPTH_LABELS = ["0 vs 1", "1 vs 2", "2 vs 3", "3 vs 4", "4 vs 5"]

COLORS_FILL = ["#4E79A7", "#F28E2B", "#59A14F", "#E15759"]
COLORS_EDGE = ["#2B5A83", "#C06A10", "#3B7A32", "#B8393B"]

def load_data():
    if JSON_PATH.exists():
        with open(JSON_PATH) as f:
            blob = json.load(f)
        return blob.get("pairwise_auc_table", FALLBACK_AUC), blob
    return FALLBACK_AUC, {}

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
def plot_grouped_bar(auc_table):
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["DejaVu Serif", "Times New Roman", "Computer Modern Roman"],
        "mathtext.fontset": "cm",
        "font.size": 8,
        "axes.titlesize": 9,
        "axes.labelsize": 8,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 6.5,
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "axes.spines.top": False,
        "axes.spines.right": False,
    })

    configs = list(auc_table.keys())
    n_configs = len(configs)
    n_pairs = len(DEPTH_PAIRS)

    fig, ax = plt.subplots(figsize=(3.5, 2.5))

    bar_width = 0.18
    x = np.arange(n_pairs)

    for ci, cfg in enumerate(configs):
        vals = [auc_table[cfg].get(dp, float("nan")) for dp in DEPTH_PAIRS]
        offset = (ci - (n_configs - 1) / 2) * bar_width
        bars = ax.bar(
            x + offset, vals, bar_width,
            color=COLORS_FILL[ci], edgecolor=COLORS_EDGE[ci],
            linewidth=0.6, alpha=0.85,
            label=CONFIG_LABELS.get(cfg, cfg), zorder=3,
        )

    ax.axhline(0.60, color="#888888", linestyle="--", linewidth=0.7, zorder=2)
    ax.text(n_pairs - 0.5, 0.605, r"$\theta=0.60$", fontsize=6, color="#666666",
            ha="right", va="bottom")

    ax.axhline(0.50, color="#AAAAAA", linestyle=":", linewidth=0.6, zorder=2)
    ax.text(n_pairs - 0.5, 0.505, "chance", fontsize=5.5, color="#999999",
            ha="right", va="bottom")

    ax.set_xticks(x)
    ax.set_xticklabels(DEPTH_LABELS)
    ax.set_xlabel("Depth pair")
    ax.set_ylabel("Pairwise AUC")
    ax.set_ylim(0.47, 1.03)

    ax.legend(loc="upper right", frameon=True, framealpha=0.9,
              edgecolor="#CCCCCC", fancybox=False, handlelength=1.2,
              handletextpad=0.4, borderpad=0.3, labelspacing=0.25)

    ax.set_axisbelow(True)

    pdf_path = ARTIFACT_DIR / "exp003_decoding_ablation.pdf"
    png_path = ARTIFACT_DIR / "exp003_decoding_ablation.png"
    fig.savefig(pdf_path)
    fig.savefig(png_path, dpi=300)
    plt.close(fig)
    print(f"Saved: {pdf_path}")
    print(f"Saved: {png_path}")

# ---------------------------------------------------------------------------
# Table
# ---------------------------------------------------------------------------
def print_and_save_table(auc_table, blob):
    top3 = blob.get("top3_features", {})
    theta_sens = blob.get("theta_sensitivity", {})

    header = f"{'Config':<22} {'Decoding':<22} {'1v2 AUC':>8} {'K*(θ=.60)':>10} {'Top-3 Features'}"
    sep = "-" * len(header)
    lines = [header, sep]

    decoding_map = {
        "Config1-Greedy": "greedy",
        "Config2-Nuc09":  "nucleus p=0.9, T=1.0",
        "Config3-T07":    "nucleus p=0.95, T=0.7",
        "Config4-T12":    "nucleus p=0.95, T=1.2",
    }

    tex_rows = []
    for cfg in auc_table:
        auc_1v2 = auc_table[cfg].get("1v2", float("nan"))
        kstar = theta_sens.get(cfg, {}).get("0.6", "—")
        feats = ", ".join(top3.get(cfg, []))
        dec = decoding_map.get(cfg, cfg)
        line = f"{cfg:<22} {dec:<22} {auc_1v2:>8.4f} {str(kstar):>10} {feats}"
        lines.append(line)
        tex_rows.append(
            f"  {cfg} & {dec} & {auc_1v2:.4f} & {kstar} & {feats} \\\\"
        )

    table_str = "\n".join(lines)
    print("\n" + table_str + "\n")

    tex = (
        "\\begin{table}[t]\n"
        "\\centering\n"
        "\\caption{Decoding ablation summary (exp-003). $K^*$ = max depth with AUC $>\\theta$.}\n"
        "\\label{tab:exp003-decoding}\n"
        "\\small\n"
        "\\begin{tabular}{llccc}\n"
        "\\toprule\n"
        "Config & Decoding & 1v2 AUC & $K^*(\\theta{=}0.60)$ & Top-3 Features \\\\\n"
        "\\midrule\n"
        + "\n".join(tex_rows) + "\n"
        "\\bottomrule\n"
        "\\end{tabular}\n"
        "\\end{table}\n"
    )

    tex_path = ARTIFACT_DIR / "exp003_decoding_ablation.tex"
    tex_path.write_text(tex)
    print(f"Saved: {tex_path}")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    auc_table, blob = load_data()
    plot_grouped_bar(auc_table)
    print_and_save_table(auc_table, blob)
