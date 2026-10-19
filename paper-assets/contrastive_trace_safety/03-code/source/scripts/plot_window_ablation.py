#!/usr/bin/env python3
"""Generate window ablation figure (Figure 4).

3-panel line plot: Balanced Accuracy, Precision, Step-level FPR
comparing HS probe vs Text probe on R1-8B across W=1,3,5,10,15,20,25.

Data source: appendix tables tab:window_full (HS) and tab:text_window (Text).
Output: docs/paper/figures/fig2_temporal_improvement.{pdf,png}
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

# ── Unified rcParams ──────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Times'],
    'mathtext.fontset': 'dejavuserif',
    'font.size': 8,
    'axes.titlesize': 8,
    'axes.labelsize': 7,
    'xtick.labelsize': 5.5,
    'ytick.labelsize': 5.5,
    'legend.fontsize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.5,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.0,
})

# ── Data ──────────────────────────────────────────────────────────
WINDOWS = [1, 3, 5, 10, 15, 20, 25]

HS_BAL_ACC   = [77.8, 79.0, 78.1, 79.3, 80.2, 80.7, 81.0]
HS_PRECISION = [69.3, 72.3, 72.6, 74.3, 77.7, 78.6, 82.2]
HS_FPR       = [9.65, 8.50, 8.09, 7.61, 6.39, 6.12, 4.83]

TEXT_BAL_ACC   = [64.7, 66.9, 69.2, 72.1, 74.3, 75.8, 76.7]
TEXT_PRECISION = [41.6, 44.8, 48.5, 54.3, 58.9, 62.1, 64.8]
TEXT_FPR       = [25.8, 23.1, 20.4, 16.7, 14.2, 12.5, 11.8]

# ── Panel config ──────────────────────────────────────────────────
# subtitle_pos: (x, y, va, ha) in axes coords -- placed where data is sparse
PANELS = [
    {
        "ylabel": "Bal. Acc. (%)",
        "hs": HS_BAL_ACC,
        "text": TEXT_BAL_ACC,
        "subtitle": "(a) Both improve",
        "subtitle_pos": (0.03, 0.03, "bottom", "left"),  # bottom-left (data sparse)
    },
    {
        "ylabel": "Precision (%)",
        "hs": HS_PRECISION,
        "text": TEXT_PRECISION,
        "subtitle": "(b) HS +17pp lead",
        "subtitle_pos": (0.97, 0.03, "bottom", "right"),  # bottom-right
    },
    {
        "ylabel": "Step FPR (%)",
        "hs": HS_FPR,
        "text": TEXT_FPR,
        "subtitle": "(c) FPR halves",
        "subtitle_pos": (0.5, 0.55, "center", "center"),  # center, between curves
    },
]

C_HS   = "#0072B2"
C_TEXT = "#E69F00"

# ── Figure ────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(7.0, 1.8), sharey=False)
plt.subplots_adjust(wspace=0.35)

XTICK_SHOW = [1, 5, 15, 25]

for idx, (ax, panel) in enumerate(zip(axes, PANELS)):
    hs_data = panel["hs"]
    text_data = panel["text"]

    # Fill between to show HS-Text gap
    ax.fill_between(WINDOWS, hs_data, text_data,
                    alpha=0.07, color="#555555", zorder=1, label="_nolegend_")

    # Lines -- HS solid blue, Text dashed orange
    ax.plot(WINDOWS, hs_data, "-o", color=C_HS, linewidth=0.9, markersize=1.8,
            markeredgewidth=0, zorder=3, label="HS probe")
    ax.plot(WINDOWS, text_data, "--s", color=C_TEXT, linewidth=0.9, markersize=1.8,
            markeredgewidth=0, markerfacecolor=C_TEXT, zorder=3, label="Text probe")

    ax.set_xlabel("Window $W$", fontsize=5.5, labelpad=1)
    ax.set_ylabel(panel["ylabel"], fontsize=5.5, labelpad=2)

    # Insight subtitle inside plot at data-sparse location
    sx, sy, sva, sha = panel["subtitle_pos"]
    t = ax.text(sx, sy, panel["subtitle"],
                transform=ax.transAxes, fontsize=5.5,
                va=sva, ha=sha, fontstyle="italic",
                color="0.35")
    t.set_path_effects([pe.withStroke(linewidth=1.5, foreground="white")])

    # X-axis: reduced ticks, extend xlim for endpoint labels
    ax.set_xticks(XTICK_SHOW)
    ax.set_xticklabels([str(w) for w in XTICK_SHOW])
    ax.set_xlim(-1, 30)

    ax.grid(True, alpha=0.18, linewidth=0.3)
    ax.tick_params(axis="both", which="both", length=1.5, width=0.4, pad=1)

    # Direct label endpoints
    hs_end = hs_data[-1]
    text_end = text_data[-1]

    # Vertical offset for close values
    gap = abs(hs_end - text_end)
    if gap < 6:
        hs_va_offset = 1.2
        text_va_offset = -1.2
    else:
        hs_va_offset = 0
        text_va_offset = 0

    t1 = ax.text(26.5, hs_end + hs_va_offset,
                 f"{hs_end:.0f}",
                 fontsize=4.5, color=C_HS, va="center", ha="left", weight="bold")
    t1.set_path_effects([pe.withStroke(linewidth=1.2, foreground="white")])
    t2 = ax.text(26.5, text_end + text_va_offset,
                 f"{text_end:.0f}",
                 fontsize=4.5, color=C_TEXT, va="center", ha="left", weight="bold")
    t2.set_path_effects([pe.withStroke(linewidth=1.2, foreground="white")])

# Compact legend on center panel
handles = axes[1].get_legend_handles_labels()[0]
axes[1].legend(
    [handles[0], handles[1]], ["HS probe", "Text probe"],
    fontsize=5.5, framealpha=0.9, edgecolor="0.85",
    loc="upper center", bbox_to_anchor=(0.5, 1.22),
    borderpad=0.2, ncol=2, columnspacing=0.8,
    handlelength=1.3, handletextpad=0.3,
)

# ── Save ──────────────────────────────────────────────────────────
import os
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dir = os.path.join(base, "docs", "paper", "figures")
os.makedirs(out_dir, exist_ok=True)

out_pdf = os.path.join(out_dir, "fig2_temporal_improvement.pdf")
out_png = out_pdf.replace(".pdf", ".png")
fig.savefig(out_pdf, bbox_inches="tight", dpi=300)
fig.savefig(out_png, bbox_inches="tight", dpi=300)
print(f"Saved: {out_pdf}")
print(f"Saved: {out_png}")
