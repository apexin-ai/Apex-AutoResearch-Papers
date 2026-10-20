#!/usr/bin/env python3
"""Pairwise AUC decay curves: auto-discovers experiment JSONs and plots all configs.

Input:  results_*/pairwise_auc.json, results/*/pairwise_auc.json, data_*/pairwise_auc.json
Output: artifacts/figures/fig2_auc_decay.pdf
Deps:   matplotlib, numpy
"""

import argparse
import json
import re
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ── Color/style rotation ──
TABLEAU_COLORS = [
    "#4e79a7", "#e15759", "#76b7b2", "#59a14f",
    "#b07aa1", "#ff9da7", "#9c755f", "#bab0ac",
    "#edc948", "#f28e2b",
]
MARKERS = ["o", "s", "^", "D", "v", "P", "X", "*", "h", "<"]
LINESTYLES_SOLID = ["-", "-", "-", "-", "-", "-", "-", "-"]
LINESTYLES_DASHED = ["--", "--", "--", "--", "--", "--", "--", "--"]


def infer_label(dir_path: Path) -> tuple[str, str]:
    """Infer display label and group (model/decode) from directory name."""
    name = dir_path.name

    decode_patterns = {
        "greedy": "Greedy", "nuc09": "Nuc p=0.9", "nuc0.9": "Nuc p=0.9",
        "t07": "T=0.7", "t0.7": "T=0.7", "t12": "T=1.2", "t1.2": "T=1.2",
    }
    for pat, label in decode_patterns.items():
        if pat in name.lower():
            return label, "decode"

    model_patterns = [
        (r"qwen.*rw|qwen.*rewrite", "Qwen-rewrite"),
        (r"qwen.*base", "Qwen-base"),
        (r"qwen.*7b", "Qwen-7B"),
        (r"qwen.*cont|qwen(?!.*rw|.*rewrite|.*base|.*7b)", "Qwen-cont"),
        (r"pythia", "Pythia-cont"),
        (r"olmo", "OLMo-cont"),
        (r"mistral.*7b", "Mistral-7B"),
        (r"llama.*8b", "LLaMA-8B"),
    ]
    for pat, label in model_patterns:
        if re.search(pat, name, re.IGNORECASE):
            return label, "model"

    clean = name.replace("results_", "").replace("results", "").replace("data_", "")
    clean = re.sub(r"^exp\d+_?", "", clean).strip("_") or name
    return clean, "model"


def discover_auc_files(root: Path) -> list[Path]:
    """Find all pairwise_auc.json under results_*/, results/*/, data_*/."""
    patterns = [
        "results_*/pairwise_auc.json",
        "results/*/pairwise_auc.json",
        "data_*/pairwise_auc.json",
    ]
    files = []
    for pat in patterns:
        files.extend(sorted(root.glob(pat)))
    return files


def load_auc_data(json_path: Path) -> dict[str, float] | None:
    """Load pairwise AUC from JSON. Returns {pair: auc} dict or None."""
    with open(json_path) as f:
        raw = json.load(f)
    if "mean" in raw:
        return raw["mean"]
    pairs = {}
    for key in ["0v1", "1v2", "2v3", "3v4", "4v5"]:
        if key in raw:
            val = raw[key]
            if isinstance(val, dict):
                pairs[key] = val.get("auc", val.get("mean"))
            else:
                pairs[key] = val
    return pairs if pairs else None


def parse_args():
    parser = argparse.ArgumentParser(description="Plot pairwise AUC decay curves")
    parser.add_argument("--results-dir", type=Path,
                        default=Path(__file__).resolve().parent.parent.parent,
                        help="Root directory to scan for results")
    parser.add_argument("--output", type=Path, default=None,
                        help="Output PDF path (default: artifacts/figures/fig2_auc_decay.pdf)")
    parser.add_argument("--filter", type=str, default=None,
                        help="Filter models by substring (case-insensitive)")
    return parser.parse_args()


def main():
    args = parse_args()
    root = args.results_dir

    auc_files = discover_auc_files(root)
    if not auc_files:
        print(f"No pairwise_auc.json found under {root}")
        return

    models = {}  # label -> {group, data}
    for fp in auc_files:
        parent = fp.parent
        label, group = infer_label(parent)
        data = load_auc_data(fp)
        if data is None:
            continue
        if args.filter and args.filter.lower() not in label.lower():
            continue
        models[label] = {"group": group, "data": data}

    if not models:
        print("No valid AUC data found after filtering")
        return

    model_items = [(k, v) for k, v in models.items() if v["group"] == "model"]
    decode_items = [(k, v) for k, v in models.items() if v["group"] == "decode"]

    x_labels = ["0 vs 1", "1 vs 2", "2 vs 3", "3 vs 4", "4 vs 5"]
    pair_keys = ["0v1", "1v2", "2v3", "3v4", "4v5"]
    x = np.arange(len(x_labels))

    # ── Style ──
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.linewidth": 0.8,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
    })

    fig, ax = plt.subplots(figsize=(7, 4), constrained_layout=True)

    ax.axvspan(0.5, 1.5, color="#fff9c4", alpha=0.55, zorder=0)
    ax.text(1.0, 1.02, r"$K^*$ boundary", ha="center", va="bottom", fontsize=9,
            fontstyle="italic", color="#8d6e00")

    ax.axhline(0.60, color="grey", ls="--", lw=0.8, zorder=1)
    ax.text(4.55, 0.608, r"$\theta = 0.60$", fontsize=8.5, color="grey", va="bottom", ha="right")
    ax.axhline(0.50, color="lightgrey", ls="--", lw=0.8, zorder=1)
    ax.text(4.55, 0.508, "chance", fontsize=8.5, color="silver", va="bottom", ha="right")

    model_handles = []
    for i, (label, info) in enumerate(model_items):
        color = TABLEAU_COLORS[i % len(TABLEAU_COLORS)]
        marker = MARKERS[i % len(MARKERS)]
        y = [info["data"].get(k, np.nan) for k in pair_keys]
        line, = ax.plot(x, y, "-", color=color, lw=1.8, marker=marker,
                        markersize=5, label=label, zorder=3)
        model_handles.append(line)

    decode_handles = []
    for i, (label, info) in enumerate(decode_items):
        color = TABLEAU_COLORS[(len(model_items) + i) % len(TABLEAU_COLORS)]
        marker = MARKERS[(len(model_items) + i) % len(MARKERS)]
        y = [info["data"].get(k, np.nan) for k in pair_keys]
        line, = ax.plot(x, y, "--", color=color, lw=1.8, marker=marker,
                        markersize=5, label=label, zorder=3)
        decode_handles.append(line)

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    ax.set_xlabel("Depth Pair")
    ax.set_ylabel("Pairwise AUC (5-fold CV)")
    ax.set_ylim(0.45, 1.05)
    ax.set_xlim(-0.25, len(x_labels) - 0.75)
    ax.tick_params(direction="in")

    if model_handles:
        leg1 = ax.legend(handles=model_handles, title="Models", title_fontsize=9,
                         fontsize=8.5, loc="upper right", bbox_to_anchor=(1.0, 0.98),
                         framealpha=0.9, edgecolor="0.8")
        ax.add_artist(leg1)
    if decode_handles:
        ax.legend(handles=decode_handles, title="Decoding", title_fontsize=9,
                  fontsize=8.5, loc="center right", bbox_to_anchor=(1.0, 0.58),
                  framealpha=0.9, edgecolor="0.8")
    elif model_handles:
        ax.legend(handles=model_handles, title="Models", title_fontsize=9,
                  fontsize=8.5, loc="upper right", bbox_to_anchor=(1.0, 0.98),
                  framealpha=0.9, edgecolor="0.8")

    # ── Save ──
    if args.output:
        out_path = args.output
    else:
        out_dir = Path(__file__).resolve().parent.parent / "figures"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "fig2_auc_decay.pdf"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    png_path = out_path.with_suffix(".png")
    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    pdf_size = out_path.stat().st_size
    png_size = png_path.stat().st_size
    print(f"Discovered {len(models)} configs: {list(models.keys())}")
    print(f"PDF: {pdf_size/1024:.1f} KB | PNG: {png_size/1024:.1f} KB")
    assert pdf_size > 5 * 1024, f"PDF too small: {pdf_size}"
    print("OK")


if __name__ == "__main__":
    main()
