#!/usr/bin/env python3
"""Cross-model transfer heatmap: classifier trained on model A, tested on model B.

Input:  artifacts/*transfer*.json, results_*/*transfer*.json, or embedded paper data
Output: artifacts/figures/fig3_transfer_heatmap.pdf
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

EMBEDDED_TRANSFER = {
    "pair": "1v2",
    "description": "Cross-model transfer AUC (1v2) from paper exp-013",
    "models": ["Qwen-rw", "Qwen-cont", "Pythia", "OLMo"],
    "matrix": [
        [0.6955, 0.6194, 0.5863, 0.5791],
        [0.6081, 0.6112, 0.5556, 0.5493],
        [0.5917, 0.5632, 0.6539, 0.5988],
        [0.5836, 0.5514, 0.5901, 0.6145],
    ],
}


def discover_transfer_files(root):
    """Find transfer matrix JSON files."""
    patterns = [
        "artifacts/*transfer*.json",
        "artifacts/*cross_scorer*.json",
        "results_*/*transfer*.json",
        "results/*transfer*.json",
    ]
    files = set()
    for pat in patterns:
        files.update(root.glob(pat))
    return sorted(files)


def load_transfer_data(json_path):
    """Load transfer matrix from JSON."""
    with open(json_path) as f:
        raw = json.load(f)
    if "matrix" in raw and "models" in raw:
        return raw["models"], np.array(raw["matrix"]), raw.get("pair", "1v2")
    if "transfer_matrix" in raw:
        tm = raw["transfer_matrix"]
        models = list(tm.keys())
        matrix = np.array([[tm[r].get(c, float("nan")) for c in models] for r in models])
        return models, matrix, raw.get("pair", "1v2")
    return None, None, None


def parse_args():
    parser = argparse.ArgumentParser(description="Plot cross-model transfer heatmap")
    parser.add_argument("--data-dir", type=Path,
                        default=Path(__file__).resolve().parent.parent.parent,
                        help="Root directory to scan for transfer data")
    parser.add_argument("--output", type=Path, default=None,
                        help="Output PDF path")
    parser.add_argument("--use-embedded", action="store_true",
                        help="Force use of embedded paper data")
    return parser.parse_args()


def main():
    args = parse_args()
    root = args.data_dir

    models, matrix, pair = None, None, None
    if not args.use_embedded:
        transfer_files = discover_transfer_files(root)
        for fp in transfer_files:
            models, matrix, pair = load_transfer_data(fp)
            if models is not None:
                print(f"Loaded transfer data from {fp}")
                break

    if models is None:
        print("No transfer JSON found on disk — using embedded paper data")
        models = EMBEDDED_TRANSFER["models"]
        matrix = np.array(EMBEDDED_TRANSFER["matrix"])
        pair = EMBEDDED_TRANSFER["pair"]

    n = len(models)

    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.linewidth": 0.8,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
    })

    fig, ax = plt.subplots(figsize=(5.5, 4.5), constrained_layout=True)

    cmap = plt.cm.viridis
    vmin, vmax = 0.50, max(0.75, np.nanmax(matrix) + 0.02)
    im = ax.imshow(matrix, cmap=cmap, vmin=vmin, vmax=vmax, aspect="equal")

    for i in range(n):
        for j in range(n):
            val = matrix[i, j]
            if np.isnan(val):
                continue
            color = "white" if val > (vmin + vmax) / 2 else "black"
            weight = "bold" if i == j else "normal"
            ax.text(j, i, f"{val:.3f}", ha="center", va="center",
                    fontsize=10, color=color, fontweight=weight)

    for i in range(n):
        rect = plt.Rectangle((i - 0.5, i - 0.5), 1, 1, linewidth=2.0,
                              edgecolor="#333333", facecolor="none", zorder=5)
        ax.add_patch(rect)

    ax.set_xticks(range(n))
    ax.set_xticklabels(models, fontsize=10)
    ax.set_yticks(range(n))
    ax.set_yticklabels(models, fontsize=10)
    ax.set_xlabel("Test model", fontsize=11)
    ax.set_ylabel("Train model", fontsize=11)
    ax.tick_params(direction="in", length=0)

    cbar = fig.colorbar(im, ax=ax, shrink=0.82, pad=0.02)
    cbar.set_label(f"AUC ({pair})", fontsize=10)
    cbar.ax.tick_params(labelsize=9)

    if args.output:
        out_path = args.output
    else:
        out_dir = Path(__file__).resolve().parent.parent / "figures"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "fig3_transfer_heatmap.pdf"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    png_path = out_path.with_suffix(".png")
    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    pdf_size = out_path.stat().st_size
    png_size = png_path.stat().st_size
    print(f"Models: {models}")
    print(f"PDF: {pdf_size/1024:.1f} KB | PNG: {png_size/1024:.1f} KB")
    assert pdf_size > 3 * 1024, f"PDF too small: {pdf_size}"
    print("OK")


if __name__ == "__main__":
    main()
