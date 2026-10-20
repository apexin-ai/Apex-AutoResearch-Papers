"""Dual-panel Pareto plot: Beam Width vs R-F1 for beam width sweep (v2).

Left: SciERC (Qwen3-8B + Llama-3.1-8B LoRA, 551 docs)
Right: DocRED (Llama-3.1-8B LoRA, 200 docs)

X-axis: beam width k (log2 scale)
Bubble size: total violation rate (DR% + CF% + RV%)
Green ring: zero-violation points
Star: Pareto-optimal (k=2)

v2 changes:
- Remove per-point k= labels (x-axis already shows beam width)
- Move "Zero violation" and "Sweet spot" into per-panel legends
- Color palette aligned with Figure 1 v6 style
- Cleaner visual style with serif axis labels
"""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.lines import Line2D

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

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
# Color palette (aligned with Figure 1 v6)
# ---------------------------------------------------------------------------
C_DEEP_BLUE   = "#2B4C7E"   # Constrained series (深蓝)
C_MEDIUM_BLUE = "#5B7FAD"   # Llama constrained accent (中蓝)
C_LIGHT_BLUE  = "#8BAED4"   # Unconstrained series (浅蓝)
C_GOLD        = "#D4A574"   # Pareto-optimal star
C_DEEP_INDIGO = "#1B2A4A"   # Title text
C_GRID        = "#F0F0F0"   # Grid lines
C_ZERO_RING   = "#2B4C7E"   # Zero-violation ring (深蓝)

BEAMS = [1, 2, 4, 8]
BUBBLE_SCALE = 300
BUBBLE_ALPHA = 0.25

# Model-specific styles (SciERC panel — two models)
QWEN_UNC  = {"color": C_LIGHT_BLUE,  "marker": "o", "ls": "-",  "label": "Qwen3 unconstrained"}
QWEN_CON  = {"color": C_DEEP_BLUE,  "marker": "s", "ls": "-",  "label": "Qwen3 constrained"}
LLAMA_UNC = {"color": C_LIGHT_BLUE, "marker": "^", "ls": "--", "label": "Llama unconstrained"}
LLAMA_CON = {"color": C_MEDIUM_BLUE,"marker": "D", "ls": "--", "label": "Llama constrained"}

# Single-model styles (DocRED panel)
SINGLE_UNC = {"color": C_LIGHT_BLUE, "marker": "o", "ls": "-", "label": "Unconstrained"}
SINGLE_CON = {"color": C_DEEP_BLUE,  "marker": "s", "ls": "-", "label": "Constrained"}


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


def _draw_series(ax, data, mode, style):
    xs, ys, viols = _extract(data, mode)
    if not xs:
        return
    ax.plot(xs, ys, color=style["color"], marker=style["marker"],
            markersize=6.5, linewidth=1.4, linestyle=style["ls"],
            label=style["label"], zorder=3, markeredgecolor="white",
            markeredgewidth=0.6)
    for x, y, v in zip(xs, ys, viols):
        if v > 0:
            ax.scatter(x, y, s=v * BUBBLE_SCALE, color=style["color"],
                       alpha=BUBBLE_ALPHA, zorder=2, edgecolors="none")


def _mark_zero_viols(ax, data):
    for mode in ("unc", "con"):
        for k in BEAMS:
            entry = data[k].get(mode)
            if entry is not None and entry.get("rf1") is not None and _total_viol(entry) == 0:
                ax.scatter(k, entry["rf1"], s=160, facecolors="none",
                           edgecolors=C_ZERO_RING, linewidths=1.8,
                           zorder=4)


def _format_axes(ax, title):
    ax.set_title(title, fontsize=11, fontweight="bold", color=C_DEEP_INDIGO,
                 pad=8, fontfamily="serif")
    ax.set_xlabel("Beam Width ($k$)", fontsize=10, fontfamily="serif")
    ax.set_ylabel("R-F1", fontsize=10, fontfamily="serif")
    ax.set_xscale("log", base=2)
    ax.set_xticks(BEAMS)
    ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    ax.minorticks_off()
    ax.set_xlim(0.75, 11)
    ax.tick_params(labelsize=9)
    ax.grid(True, color=C_GRID, linewidth=0.6, zorder=0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_linewidth(0.6)
        spine.set_color("#CCCCCC")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def _add_special_legend(ax, loc="lower left"):
    handles = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor="none",
               markeredgecolor=C_ZERO_RING, markeredgewidth=1.8,
               markersize=9, label="Zero violation"),
        Line2D([0], [0], marker="*", color=C_GOLD, markeredgecolor="#6B5B4A",
               markeredgewidth=0.4,
               markersize=11, linestyle="None", label="Pareto-optimal ($k$=2)"),
    ]
    return handles


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="beam_pareto.pdf")
    args = parser.parse_args()

    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 10,
        "axes.linewidth": 0.6,
        "xtick.major.width": 0.5,
        "ytick.major.width": 0.5,
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.05,
        "mathtext.fontset": "cm",
    })

    fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(9.5, 3.8),
                                      constrained_layout=True)

    # --- Left panel: SciERC (dual model) ---
    _draw_series(ax_l, scierc_qwen, "unc", QWEN_UNC)
    _draw_series(ax_l, scierc_qwen, "con", QWEN_CON)
    _draw_series(ax_l, scierc_llama, "unc", LLAMA_UNC)
    _draw_series(ax_l, scierc_llama, "con", LLAMA_CON)
    _mark_zero_viols(ax_l, scierc_qwen)
    _mark_zero_viols(ax_l, scierc_llama)

    # Pareto-optimal: Qwen k=2 con — white halo then gold star
    d = scierc_qwen[2]["con"]
    ax_l.scatter(2, d["rf1"], s=400, marker="*", color="white",
                 edgecolors="none", zorder=5)
    ax_l.scatter(2, d["rf1"], s=320, marker="*", color=C_GOLD,
                 edgecolors="#6B5B4A", linewidths=0.6, zorder=6)

    _format_axes(ax_l, "SciERC (551 docs)")

    # Combined legend for left panel
    series_handles, series_labels = ax_l.get_legend_handles_labels()
    special_handles = _add_special_legend(ax_l)
    all_handles = series_handles + special_handles
    all_labels = series_labels + [h.get_label() for h in special_handles]
    ax_l.legend(all_handles, all_labels, fontsize=7, loc="lower left",
                framealpha=0.95, edgecolor="#E0E0E0", ncol=3,
                handlelength=1.8, columnspacing=0.8, handletextpad=0.4,
                labelspacing=0.3)

    # --- Right panel: DocRED (single model) ---
    _draw_series(ax_r, docred_llama, "unc", SINGLE_UNC)
    _draw_series(ax_r, docred_llama, "con", SINGLE_CON)
    _mark_zero_viols(ax_r, docred_llama)

    # Pareto-optimal: k=2 con — white halo then gold star
    d = docred_llama[2]["con"]
    ax_r.scatter(2, d["rf1"], s=400, marker="*", color="white",
                 edgecolors="none", zorder=5)
    ax_r.scatter(2, d["rf1"], s=320, marker="*", color=C_GOLD,
                 edgecolors="#6B5B4A", linewidths=0.6, zorder=6)

    _format_axes(ax_r, "DocRED (200 docs)")

    # Combined legend for right panel
    series_handles, series_labels = ax_r.get_legend_handles_labels()
    special_handles = _add_special_legend(ax_r)
    all_handles = series_handles + special_handles
    all_labels = series_labels + [h.get_label() for h in special_handles]
    ax_r.legend(all_handles, all_labels, fontsize=7.5, loc="lower right",
                framealpha=0.95, edgecolor="#E0E0E0",
                handlelength=2.0, handletextpad=0.5)

    out = Path(args.output)
    fig.savefig(out, bbox_inches="tight")
    fig.savefig(out.with_suffix(".png"), bbox_inches="tight", dpi=300)
    print(f"Saved {out} and {out.with_suffix('.png')}")
    plt.close(fig)


if __name__ == "__main__":
    main()
