"""Dual-panel Pareto plot: Beam Width vs R-F1 for beam width sweep.

Left: SciERC (Qwen3-8B + Llama-3.1-8B LoRA, 551 docs)
Right: DocRED (Llama-3.1-8B LoRA, 200 docs)

X-axis: beam width k (log2 scale)
Bubble size: total violation rate (DR% + CF% + RV%)
Green ring: zero-violation points

Usage:
    python plot_pareto_dual.py [--output beam_pareto.pdf]
"""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# ---------------------------------------------------------------------------
# Data: {beam_k: {"unc": {...}, "con": {...}}}
# dr/cf/rv in percent
# ---------------------------------------------------------------------------

# SciERC: Qwen3-8B LoRA (complete: k=1,2,4,8 x unc/con)
scierc_qwen = {
    1: {"unc": {"rf1": 42.95, "dr": 2.11, "cf": 0,    "rv": 0},
        "con": {"rf1": 42.95, "dr": 0,    "cf": 0.50, "rv": 0}},
    2: {"unc": {"rf1": 44.75, "dr": 1.54, "cf": 0,    "rv": 0},
        "con": {"rf1": 44.60, "dr": 0,    "cf": 0.11, "rv": 0}},
    4: {"unc": {"rf1": 43.72, "dr": 1.89, "cf": 0,    "rv": 0},
        "con": {"rf1": 43.60, "dr": 0,    "cf": 0,    "rv": 0}},
    8: {"unc": {"rf1": 43.17, "dr": 1.77, "cf": 0,    "rv": 0},
        "con": {"rf1": 43.65, "dr": 0,    "cf": 0,    "rv": 0}},
}

# SciERC: Llama-3.1-8B LoRA (unc: k=1 only; con: k=1,2,4,8)
scierc_llama = {
    1: {"unc": {"rf1": 45.45, "dr": 1.11, "cf": 0,    "rv": 0},
        "con": {"rf1": 45.47, "dr": 0.09, "cf": 0.46, "rv": 0}},
    2: {"unc": None,
        "con": {"rf1": 46.12, "dr": 0,    "cf": 0.17, "rv": 0}},
    4: {"unc": None,
        "con": {"rf1": 46.18, "dr": 0,    "cf": 0,    "rv": 0}},
    8: {"unc": None,
        "con": {"rf1": 44.95, "dr": 0,    "cf": 0,    "rv": 0}},
}

# DocRED: Llama-3.1-8B LoRA (complete: k=1,2,4,8 x unc/con)
docred_llama = {
    1: {"unc": {"rf1": 47.28, "dr": 0.30, "cf": 0.19, "rv": 0.36},
        "con": {"rf1": 47.35, "dr": 0,    "cf": 0.19, "rv": 0}},
    2: {"unc": {"rf1": 51.31, "dr": 0.11, "cf": 0.05, "rv": 0.07},
        "con": {"rf1": 51.17, "dr": 0,    "cf": 0,    "rv": 0}},
    4: {"unc": {"rf1": 52.65, "dr": 0.04, "cf": 0.08, "rv": 0.08},
        "con": {"rf1": 51.89, "dr": 0,    "cf": 0,    "rv": 0}},
    8: {"unc": {"rf1": 51.97, "dr": 0,    "cf": 0.05, "rv": 0.07},
        "con": {"rf1": 51.74, "dr": 0,    "cf": 0,    "rv": 0}},
}

# ---------------------------------------------------------------------------
# Plotting config
# ---------------------------------------------------------------------------

BEAMS = [1, 2, 4, 8]
BUBBLE_SCALE = 200
BUBBLE_ALPHA = 0.25
ZERO_VIOL_COLOR = "#4daf4a"
SWEET_COLOR = "#e31a1c"

# Model-specific styles
QWEN_UNC  = {"color": "#999999", "marker": "o", "ls": "-",  "label": "Qwen unc"}
QWEN_CON  = {"color": "#2166ac", "marker": "s", "ls": "-",  "label": "Qwen con"}
LLAMA_UNC = {"color": "#999999", "marker": "^", "ls": "--", "label": "Llama unc"}
LLAMA_CON = {"color": "#d6604d", "marker": "D", "ls": "--", "label": "Llama con"}

# Single-model styles (DocRED panel)
SINGLE_UNC = {"color": "#999999", "marker": "o", "ls": "-", "label": "Unconstrained"}
SINGLE_CON = {"color": "#2166ac", "marker": "s", "ls": "-", "label": "Constrained"}


def _total_viol(d):
    if d is None:
        return 0
    return d.get("dr", 0) + d.get("cf", 0) + d.get("rv", 0)


def _extract(data, mode):
    xs, ys, viols = [], [], []
    for k in BEAMS:
        entry = data[k].get(mode)
        if entry is not None and entry.get("rf1") is not None:
            xs.append(k)
            ys.append(entry["rf1"])
            viols.append(_total_viol(entry))
    return xs, ys, viols


def _draw_series(ax, data, mode, style, annotate=True, ann_offset_y=6):
    xs, ys, viols = _extract(data, mode)
    if not xs:
        return
    ax.plot(xs, ys, color=style["color"], marker=style["marker"],
            markersize=7, linewidth=1.5, linestyle=style["ls"],
            label=style["label"], zorder=3)
    for x, y, v in zip(xs, ys, viols):
        if v > 0:
            ax.scatter(x, y, s=v * BUBBLE_SCALE, color=style["color"],
                       alpha=BUBBLE_ALPHA, zorder=2, edgecolors="none")
    if annotate:
        for x, y in zip(xs, ys):
            ax.annotate(f"$k$={x}", (x, y), textcoords="offset points",
                        xytext=(8, ann_offset_y), fontsize=7.5,
                        color=style["color"])


def _mark_zero_viols(ax, data):
    for mode in ("unc", "con"):
        for k in BEAMS:
            entry = data[k].get(mode)
            if entry is not None and entry.get("rf1") is not None and _total_viol(entry) == 0:
                ax.scatter(k, entry["rf1"], s=180, facecolors="none",
                           edgecolors=ZERO_VIOL_COLOR, linewidths=2.0,
                           zorder=4)


def _format_axes(ax, title):
    ax.set_title(title, fontsize=11, fontweight="bold")
    ax.set_xlabel("Beam Width ($k$)", fontsize=10)
    ax.set_ylabel("R-F1", fontsize=10)
    ax.set_xscale("log", base=2)
    ax.set_xticks(BEAMS)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.minorticks_off()
    ax.set_xlim(0.75, 11)
    ax.tick_params(labelsize=9)
    ax.grid(True, alpha=0.3, linewidth=0.5)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="beam_pareto.pdf")
    args = parser.parse_args()

    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 10,
        "axes.linewidth": 0.8,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "figure.dpi": 150,
    })

    fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(10, 4),
                                      constrained_layout=True)

    # --- Left panel: SciERC (dual model) ---
    _draw_series(ax_l, scierc_qwen, "unc", QWEN_UNC, annotate=True, ann_offset_y=6)
    _draw_series(ax_l, scierc_qwen, "con", QWEN_CON, annotate=True, ann_offset_y=-14)
    _draw_series(ax_l, scierc_llama, "unc", LLAMA_UNC, annotate=False)
    _draw_series(ax_l, scierc_llama, "con", LLAMA_CON, annotate=True, ann_offset_y=8)
    _mark_zero_viols(ax_l, scierc_qwen)
    _mark_zero_viols(ax_l, scierc_llama)

    # Sweet spot: Qwen k=2 con (best R-F1 with near-zero violations)
    d = scierc_qwen[2]["con"]
    ax_l.scatter(2, d["rf1"], s=220, marker="*", color=SWEET_COLOR,
                 edgecolors="black", linewidths=0.5, zorder=5)

    _format_axes(ax_l, "SciERC (551 docs)")
    ax_l.legend(fontsize=8, loc="lower left", framealpha=0.9, ncol=2)

    # --- Right panel: DocRED (single model) ---
    _draw_series(ax_r, docred_llama, "unc", SINGLE_UNC, annotate=True, ann_offset_y=6)
    _draw_series(ax_r, docred_llama, "con", SINGLE_CON, annotate=True, ann_offset_y=-14)
    _mark_zero_viols(ax_r, docred_llama)

    # Sweet spot: k=2 con (zero violations, good R-F1)
    d = docred_llama[2]["con"]
    ax_r.scatter(2, d["rf1"], s=220, marker="*", color=SWEET_COLOR,
                 edgecolors="black", linewidths=0.5, zorder=5)

    _format_axes(ax_r, "DocRED (Llama-3.1-8B LoRA, 200 docs)")
    ax_r.legend(fontsize=8, loc="lower right", framealpha=0.9)

    # --- Shared legend for special markers ---
    from matplotlib.lines import Line2D
    handles = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor="none",
               markeredgecolor=ZERO_VIOL_COLOR, markeredgewidth=2,
               markersize=10, label="Zero violation"),
        Line2D([0], [0], marker="*", color=SWEET_COLOR,
               markersize=12, linestyle="None", label="Sweet spot"),
    ]
    fig.legend(handles=handles, loc="upper center", ncol=2,
               fontsize=9, bbox_to_anchor=(0.5, 1.02), frameon=False)

    out = Path(args.output)
    fig.savefig(out, bbox_inches="tight")
    fig.savefig(out.with_suffix(".png"), bbox_inches="tight", dpi=300)
    print(f"Saved {out} and {out.with_suffix('.png')}")
    plt.close(fig)


if __name__ == "__main__":
    main()
