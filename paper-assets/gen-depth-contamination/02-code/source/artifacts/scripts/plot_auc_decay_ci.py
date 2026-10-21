#!/usr/bin/env python3
"""AUC decay curves with bootstrap confidence interval bands.

Input:  artifacts/exp*_bootstrap_ci.json, results_*/bootstrap_ci.json,
        results_*/pairwise_auc.json (per_fold → approximate CI)
Output: artifacts/figures/fig_s1_auc_decay_ci.pdf
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

TABLEAU_COLORS = [
    "#4e79a7", "#e15759", "#76b7b2", "#59a14f",
    "#b07aa1", "#ff9da7", "#9c755f", "#bab0ac",
    "#edc948", "#f28e2b",
]
MARKERS = ["o", "s", "^", "D", "v", "P", "X", "*", "h", "<"]
PAIR_KEYS = ["0v1", "1v2", "2v3", "3v4", "4v5"]
X_LABELS = ["0 vs 1", "1 vs 2", "2 vs 3", "3 vs 4", "4 vs 5"]


def infer_label(source_path, metadata=None):
    """Infer model label from file path or JSON metadata."""
    if metadata and "experiment" in metadata:
        exp = metadata["experiment"].lower()
    else:
        exp = str(source_path).lower()
    patterns = [
        (r"qwen.*rw|qwen.*rewrite", "Qwen-rw"),
        (r"qwen.*base", "Qwen-base"),
        (r"qwen.*7b", "Qwen-7B"),
        (r"qwen.*cont|qwen(?!.*rw|.*rewrite|.*base|.*7b)", "Qwen-cont"),
        (r"pythia.*greedy", "Pythia-greedy"),
        (r"pythia.*nuc", "Pythia-nuc0.9"),
        (r"pythia.*t07|pythia.*t0\.7", "Pythia-T0.7"),
        (r"pythia.*t12|pythia.*t1\.2", "Pythia-T1.2"),
        (r"pythia", "Pythia"),
        (r"olmo", "OLMo"),
        (r"mistral", "Mistral-7B"),
        (r"llama.*8b", "LLaMA-8B"),
        (r"length.?128", "Length-128"),
        (r"length.?256", "Length-256"),
        (r"length.?512", "Length-512"),
    ]
    for pat, label in patterns:
        if re.search(pat, exp, re.IGNORECASE):
            return label
    name = source_path.stem if source_path.is_file() else source_path.name
    name = re.sub(r"^exp\d+_", "", name).replace("bootstrap_ci", "").replace("pairwise_auc", "").strip("_")
    return name or source_path.parent.name


def discover_ci_sources(root):
    """Find bootstrap CI JSONs and pairwise_auc.json with per_fold data."""
    ci_patterns = [
        "artifacts/*bootstrap*ci*.json",
        "artifacts/exp*_bootstrap_ci.json",
        "results_*/*bootstrap*ci*.json",
        "results/*/*bootstrap*ci*.json",
    ]
    auc_patterns = [
        "results_*/pairwise_auc.json",
        "results/*/pairwise_auc.json",
    ]
    files = set()
    for pat in ci_patterns:
        files.update(root.glob(pat))
    ci_files = sorted(files)

    auc_files_set = set()
    for pat in auc_patterns:
        auc_files_set.update(root.glob(pat))
    auc_files = sorted(auc_files_set)

    return ci_files, auc_files


def load_bootstrap_ci(json_path):
    """Load from bootstrap CI JSON. Returns {pair: {mean, ci_lower, ci_upper}}."""
    with open(json_path) as f:
        raw = json.load(f)

    result = {}
    pairs_data = raw.get("pairs", raw)
    for k in PAIR_KEYS:
        if k in pairs_data:
            entry = pairs_data[k]
            if isinstance(entry, dict) and "ci_lower" in entry:
                result[k] = {
                    "mean": entry.get("boot_mean", entry.get("auc", entry.get("auc_mean_folds"))),
                    "ci_lower": entry["ci_lower"],
                    "ci_upper": entry["ci_upper"],
                }
    return result if result else None, raw


def load_pairwise_auc_ci(json_path):
    """Compute approximate CI from per-fold AUCs (mean ± 1.96*SE)."""
    with open(json_path) as f:
        raw = json.load(f)

    per_fold = raw.get("per_fold")
    mean_data = raw.get("mean")
    if not per_fold or not mean_data:
        return None, raw

    result = {}
    for k in PAIR_KEYS:
        if k in per_fold and k in mean_data:
            folds = np.array(per_fold[k])
            m = mean_data[k]
            se = np.std(folds, ddof=1) / np.sqrt(len(folds))
            result[k] = {
                "mean": m,
                "ci_lower": m - 1.96 * se,
                "ci_upper": m + 1.96 * se,
            }
    return result if result else None, raw


def parse_args():
    parser = argparse.ArgumentParser(description="Plot AUC decay with confidence bands")
    parser.add_argument("--results-dir", type=Path,
                        default=Path(__file__).resolve().parent.parent.parent,
                        help="Root directory to scan")
    parser.add_argument("--output", type=Path, default=None,
                        help="Output PDF path")
    parser.add_argument("--filter", type=str, default=None,
                        help="Filter models by substring")
    return parser.parse_args()


def main():
    args = parse_args()
    root = args.results_dir

    ci_files, auc_files = discover_ci_sources(root)
    if not ci_files and not auc_files:
        print(f"No CI or pairwise_auc files found under {root}")
        return

    models = {}

    for fp in ci_files:
        data, metadata = load_bootstrap_ci(fp)
        if data is None:
            continue
        label = infer_label(fp, metadata)
        if args.filter and args.filter.lower() not in label.lower():
            continue
        label = label + " (bootstrap)"
        models[label] = data

    for fp in auc_files:
        data, metadata = load_pairwise_auc_ci(fp)
        if data is None:
            continue
        label = infer_label(fp, metadata)
        if args.filter and args.filter.lower() not in label.lower():
            continue
        if any(label.split(" (")[0] in k for k in models):
            continue
        models[label] = data

    if not models:
        print("No valid CI data found after filtering")
        return

    x = np.arange(len(PAIR_KEYS))

    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.linewidth": 0.8,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
    })

    fig, ax = plt.subplots(figsize=(7, 4.5), constrained_layout=True)

    ax.axhline(0.60, color="grey", ls="--", lw=0.8, zorder=1)
    ax.text(len(PAIR_KEYS) - 0.45, 0.608, r"$\theta = 0.60$",
            fontsize=8.5, color="grey", va="bottom", ha="right")
    ax.axhline(0.50, color="lightgrey", ls="--", lw=0.8, zorder=1)
    ax.text(len(PAIR_KEYS) - 0.45, 0.508, "chance",
            fontsize=8.5, color="silver", va="bottom", ha="right")

    handles = []
    for i, (label, ci_data) in enumerate(models.items()):
        color = TABLEAU_COLORS[i % len(TABLEAU_COLORS)]
        marker = MARKERS[i % len(MARKERS)]

        means = [ci_data.get(k, {}).get("mean", float("nan")) for k in PAIR_KEYS]
        lowers = [ci_data.get(k, {}).get("ci_lower", float("nan")) for k in PAIR_KEYS]
        uppers = [ci_data.get(k, {}).get("ci_upper", float("nan")) for k in PAIR_KEYS]

        ax.fill_between(x, lowers, uppers, color=color, alpha=0.15, zorder=2)
        line, = ax.plot(x, means, "-", color=color, lw=1.8, marker=marker,
                        markersize=5, label=label, zorder=3)
        handles.append(line)

    ax.set_xticks(x)
    ax.set_xticklabels(X_LABELS)
    ax.set_xlabel("Depth Pair")
    ax.set_ylabel("Pairwise AUC")
    ax.set_ylim(0.45, 1.05)
    ax.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)
    ax.tick_params(direction="in")

    ax.legend(handles=handles, fontsize=8.5, loc="upper right",
              bbox_to_anchor=(1.0, 0.98), framealpha=0.9, edgecolor="0.8")

    if args.output:
        out_path = args.output
    else:
        out_dir = Path(__file__).resolve().parent.parent / "figures"
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "fig_s1_auc_decay_ci.pdf"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    png_path = out_path.with_suffix(".png")
    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    pdf_size = out_path.stat().st_size
    png_size = png_path.stat().st_size
    print(f"Discovered {len(models)} configs: {list(models.keys())}")
    print(f"PDF: {pdf_size/1024:.1f} KB | PNG: {png_size/1024:.1f} KB")
    assert pdf_size > 3 * 1024, f"PDF too small: {pdf_size}"
    print("OK")


if __name__ == "__main__":
    main()
