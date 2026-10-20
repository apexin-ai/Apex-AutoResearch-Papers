#!/usr/bin/env python3
"""Filtering strategy comparison: bar chart of downstream MMLU under different curation methods.

Input:  artifacts/*filter*.json, results_*/*filter*.json, or embedded paper data (exp-006)
Output: artifacts/figures/fig_filtering_strategies.pdf
Deps:   matplotlib, numpy
"""

import argparse
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

TABLEAU_COLORS = [
    "#4e79a7", "#e15759", "#76b7b2", "#59a14f",
    "#b07aa1", "#ff9da7", "#9c755f", "#bab0ac",
    "#edc948", "#f28e2b",
]

EMBEDDED_FILTERING = {
    "experiment": "exp-006 K*-aware data curation",
    "metric": "MMLU (5-shot)",
    "strategies": [
        {"name": "No filter", "score": 0.5865, "std": 0.0010, "category": "baseline"},
        {"name": "DSIR", "score": 0.5869, "std": 0.0003, "category": "baseline"},
        {"name": "Surprisal\nselection", "score": 0.5894, "std": 0.0009, "category": "alternative"},
        {"name": "Graduated\nweighting", "score": 0.5892, "std": 0.0008, "category": "alternative"},
        {"name": "Binary\nDrayson", "score": 0.5913, "std": 0.0009, "category": "alternative"},
        {"name": r"Binary $K^*$" + "\nfiltering", "score": 0.5941, "std": 0.0008, "category": "ours"},
    ],
}


def discover_filtering_files(root):
    """Find filtering experiment JSON files."""
    patterns = [
        "artifacts/*filter*.json",
        "artifacts/*curation*.json",
        "results_*/*filter*.json",
        "results/*filter*.json",
        "results_*/*curation*.json",
    ]
    files = set()
    for pat in patterns:
        files.update(root.glob(pat))
    return sorted(files)


def load_filtering_data(json_path):
    """Load filtering comparison data from JSON."""
    with open(json_path) as f:
        raw = json.load(f)
    if "strategies" in raw:
        return raw
    return None


def parse_args():
    parser = argparse.ArgumentParser(description="Plot filtering strategy comparison")
    parser.add_argument("--data-dir", type=Path,
                        default=Path(__file__).resolve().parent.parent.parent,
                        help="Root directory to scan for filtering data")
    parser.add_argument("--output", type=Path, default=None,
                        help="Output PDF path")
    parser.add_argument("--use-embedded", action="store_true",
                        help="Force use of embedded paper data")
    return parser.parse_args()


def main():
    args = parse_args()
    root = args.data_dir

    data = None
    if not args.use_embedded:
        filter_files = discover_filtering_files(root)
        for fp in filter_files:
            data = load_filtering_data(fp)
            if data is not None:
                print(f"Loaded filtering data from {fp}")
                break

    if data is None:
        print("No filtering JSON found on disk — using embedded paper data")
        data = EMBEDDED_FILTERING

    strategies = data["strategies"]
    metric_label = data.get("metric", "MMLU (5-shot)")

    names = [s["name"] for s in strategies]
    scores = np.array([s["score"] for s in strategies])
    stds = np.array([s.get("std", 0) for s in strategies])
    categories = [s.get("category", "other") for s in strategies]

    category_colors = {
        "baseline": "#bab0ac",
        "alternative": "#4e79a7",
        "ours": "#e15759",
        "other": "#76b7b2",
    }
    colors = [category_colors.get(c, "#76b7b2") for c in categories]

    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.linewidth": 0.8,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
    })

    fig, ax = plt.subplots(figsize=(6, 4), constrained_layout=True)

    x = np.arange(len(names))
    bar_width = 0.6
    bars = ax.bar(x, scores, bar_width, color=colors, edgecolor="white",
                  linewidth=0.8, zorder=3)

    if np.any(stds > 0):
        ax.errorbar(x, scores, yerr=1.96 * stds, fmt="none", ecolor="#333333",
                    elinewidth=1.0, capsize=3, capthick=1.0, zorder=4)

    for i, (bar, score) in enumerate(zip(bars, scores)):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.0008,
                f"{score:.4f}", ha="center", va="bottom", fontsize=9,
                fontweight="bold" if categories[i] == "ours" else "normal")

    best_idx = np.argmax(scores)
    bars[best_idx].set_edgecolor("#333333")
    bars[best_idx].set_linewidth(1.5)

    y_min = min(scores) - 0.006
    y_max = max(scores) + 0.005
    ax.set_ylim(y_min, y_max)

    no_filter_score = next((s["score"] for s in strategies if "no filter" in s["name"].lower()), None)
    if no_filter_score is not None:
        ax.axhline(no_filter_score, color="#bab0ac", ls="--", lw=0.8, zorder=1)
        ax.text(len(names) - 0.5, no_filter_score + 0.0003, "no-filter baseline",
                fontsize=8, color="#999999", ha="right", va="bottom")

    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=9.5)
    ax.set_ylabel(metric_label)
    ax.tick_params(direction="in")
    ax.grid(axis="y", color="#e0e0e0", linewidth=0.5, zorder=0)

    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#bab0ac", edgecolor="white", label="Baseline"),
        Patch(facecolor="#4e79a7", edgecolor="white", label="Alternative"),
        Patch(facecolor="#e15759", edgecolor="white", label="Ours"),
    ]
    ax.legend(handles=legend_elements, fontsize=9, loc="upper left",
              framealpha=0.9, edgecolor="0.8")

    if args.output:
        out_path = args.output
    else:
        out_dir = Path(__file__).resolve().parent.parent / "figures"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "fig_filtering_strategies.pdf"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    png_path = out_path.with_suffix(".png")
    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    pdf_size = out_path.stat().st_size
    png_size = png_path.stat().st_size
    print(f"Strategies: {names}")
    print(f"PDF: {pdf_size/1024:.1f} KB | PNG: {png_size/1024:.1f} KB")
    assert pdf_size > 3 * 1024, f"PDF too small: {pdf_size}"
    print("OK")


if __name__ == "__main__":
    main()
