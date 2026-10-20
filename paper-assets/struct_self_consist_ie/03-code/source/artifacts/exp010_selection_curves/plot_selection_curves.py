#!/usr/bin/env python3
"""Standalone plotting for exp-010 selection curves. Reads exp010_metrics.json."""

import json
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, MultipleLocator

METRICS_PATH = sys.argv[1] if len(sys.argv) > 1 else "exp010_metrics.json"
OUT_DIR = sys.argv[2] if len(sys.argv) > 2 else "figures"

with open(METRICS_PATH) as f:
    data = json.load(f)

# ── Style ──────────────────────────────────────────────────────────

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
    "font.size": 11,
    "axes.labelsize": 13,
    "axes.titlesize": 14,
    "legend.fontsize": 10,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
    "axes.linewidth": 0.8,
    "grid.linewidth": 0.5,
    "lines.linewidth": 2.0,
})

STYLES = {
    "SJ":          {"color": "#1b6ec2", "marker": "o", "ls": "-",  "lw": 2.2, "ms": 8,  "zorder": 10},
    "FK":          {"color": "#e67e22", "marker": "s", "ls": "-",  "lw": 2.0, "ms": 7,  "zorder": 9},
    "logprob":     {"color": "#27ae60", "marker": "^", "ls": "-",  "lw": 2.2, "ms": 8,  "zorder": 8},
    "voting_conf": {"color": "#c0392b", "marker": "D", "ls": "-",  "lw": 2.0, "ms": 6.5,"zorder": 7},
    "EM":          {"color": "#8e44ad", "marker": "v", "ls": "-",  "lw": 1.8, "ms": 7,  "zorder": 6},
    "random":      {"color": "#95a5a6", "marker": "+", "ls": "--", "lw": 1.5, "ms": 8,  "zorder": 4},
    "oracle":      {"color": "#2c3e50", "marker": "*", "ls": "--", "lw": 1.6, "ms": 10, "zorder": 5},
    "greedy":      {"color": "#7f8c8d", "marker": "",  "ls": ":",  "lw": 2.0, "ms": 0,  "zorder": 3},
}

LABELS = {
    "SJ": "Soft Jaccard",
    "FK": "Fleiss' $\\kappa$",
    "logprob": "Log-prob",
    "voting_conf": "Voting Conf.",
    "EM": "Exact Match",
    "random": "Random",
    "oracle": "Oracle",
    "greedy": "Greedy ($T$=0)",
}

PLOT_ORDER = ["oracle", "SJ", "FK", "voting_conf", "logprob", "EM", "random", "greedy"]

DATASET_ORDER = [
    ("scierc_ner", "(a) NER — SciERC"),
    ("scierc_re",  "(b) RE — SciERC"),
    ("conll_ner",  "(c) NER — CoNLL-2003"),
]

# ── Plot ───────────────────────────────────────────────────────────

fig, axes = plt.subplots(1, 3, figsize=(16, 5.2))
plt.subplots_adjust(left=0.06, right=0.98, top=0.90, bottom=0.22, wspace=0.28)

for ax_idx, (ds_key, title) in enumerate(DATASET_ORDER):
    ax = axes[ax_idx]
    ds = data[ds_key]
    n_vals = ds["n_values"]
    results = ds["results"]
    results_std = ds["results_std"]

    for sig in PLOT_ORDER:
        st = STYLES[sig]
        ys = [results[str(n)][sig] for n in n_vals]

        if sig == "greedy":
            ax.axhline(y=ys[0], color=st["color"], ls=st["ls"], lw=st["lw"],
                        label=LABELS[sig], zorder=st["zorder"], alpha=0.8)
        else:
            stds = [results_std[str(n)].get(sig, 0) for n in n_vals]
            has_err = any(s > 0 for s in stds)
            if has_err:
                ys_arr = np.array(ys)
                stds_arr = np.array(stds)
                ax.fill_between(n_vals, ys_arr - stds_arr, ys_arr + stds_arr,
                                color=st["color"], alpha=0.08, zorder=1)
            ax.plot(n_vals, ys, color=st["color"], marker=st["marker"],
                    ls=st["ls"], lw=st["lw"], ms=st["ms"],
                    label=LABELS[sig], zorder=st["zorder"],
                    markeredgecolor="white", markeredgewidth=0.7,
                    clip_on=False)

    ax.set_xscale("log", base=2)
    ax.set_xticks(n_vals)
    ax.xaxis.set_major_formatter(ScalarFormatter())
    ax.set_xlabel("$N$ (number of samples)")
    if ax_idx == 0:
        ax.set_ylabel("Macro F1")

    ax.set_title(title, fontweight="bold", pad=8)
    ax.grid(True, alpha=0.25, ls="--", zorder=0)
    ax.set_xlim(0.85, n_vals[-1] * 1.15)

    # Y-axis: tight range with small padding
    all_ys = []
    for sig in PLOT_ORDER:
        all_ys.extend(results[str(n)][sig] for n in n_vals)
    y_min = min(all_ys)
    y_max = max(all_ys)
    pad = (y_max - y_min) * 0.06
    ax.set_ylim(y_min - pad, y_max + pad)

    # Minor ticks for Y
    y_range = y_max - y_min
    if y_range < 0.15:
        ax.yaxis.set_minor_locator(MultipleLocator(0.01))
    else:
        ax.yaxis.set_minor_locator(MultipleLocator(0.02))
    ax.tick_params(which="minor", length=2)

    # Annotate instance count
    ax.text(0.97, 0.03, f"$n$={ds['n_instances']}", transform=ax.transAxes,
            fontsize=9, ha="right", va="bottom", color="#666666")

# Shared legend at bottom
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=4, fontsize=10.5,
           bbox_to_anchor=(0.52, -0.01), frameon=True,
           edgecolor="#cccccc", fancybox=False,
           handlelength=2.5, columnspacing=1.8)

os.makedirs(OUT_DIR, exist_ok=True)
pdf_path = os.path.join(OUT_DIR, "fig_selection_curves.pdf")
png_path = os.path.join(OUT_DIR, "fig_selection_curves.png")
fig.savefig(pdf_path, dpi=300, bbox_inches="tight")
fig.savefig(png_path, dpi=300, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {pdf_path}")
print(f"Saved: {png_path}")
