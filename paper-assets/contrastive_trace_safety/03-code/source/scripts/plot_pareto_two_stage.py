#!/usr/bin/env python3
"""Generate Pareto front figure (Appendix Figure A.1).

Precision-coverage Pareto comparison: single-stage vs two-stage adaptive
detection on R1-8B.

Data source: artifacts/exp_pathC_two_stage_summary.md (trace-level metrics).
Output: docs/paper/figures/pareto_two_stage.{pdf,png}
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
    'axes.titlesize': 9,
    'axes.labelsize': 8.5,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.5,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.2,
})

# ── Data ──────────────────────────────────────────────────────────
SS = {
    1:  (0.7037, 0.8462),
    3:  (0.7222, 0.6667),
    5:  (0.7091, 0.6667),
    10: (0.7222, 0.6667),
    15: (0.7091, 0.7692),
    20: (0.7222, 0.7179),
    25: (0.7091, 0.7436),
}

TS_DOMINANT = {
    (3, 15, 1): (0.7222, 0.7692),
    (3, 25, 1): (0.7222, 0.7436),
}

SS_PARETO = [(0.7037, 0.8462), (0.7091, 0.7692), (0.7222, 0.7179)]

C_SS  = "#0072B2"
C_DOM = "#009E73"

# ── Figure ────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(3.4, 2.4))

# SS Pareto frontier line
pareto_sorted = sorted(SS_PARETO, key=lambda x: x[1])
pareto_cov = [p[1] for p in pareto_sorted]
pareto_prec = [p[0] for p in pareto_sorted]
ax.plot(pareto_cov, pareto_prec,
        "--", color=C_SS, alpha=0.4, linewidth=0.9, zorder=2,
        label="_nolegend_")

# Subtle shading: region above Pareto frontier
shade_cov  = pareto_cov + [pareto_cov[-1], pareto_cov[0]]
shade_prec = pareto_prec + [0.728, 0.728]
ax.fill(shade_cov, shade_prec, alpha=0.04, color=C_DOM, zorder=1)

# Single-stage scatter
ss_cov = [v[1] for v in SS.values()]
ss_prec = [v[0] for v in SS.values()]
ax.scatter(ss_cov, ss_prec, c=C_SS, s=28, marker="o", zorder=4,
           label="Single-stage", edgecolors="white", linewidths=0.4)

# Per-point labels
LABEL_CFG = {
    1:  {"text": "$W$=1",     "xytext": (5, -7),  "ha": "left"},
    3:  {"text": "$W$=3,10",  "xytext": (-5, 5),  "ha": "right"},
    5:  {"text": "$W$=5",     "xytext": (-5, -7), "ha": "right"},
    15: {"text": "$W$=15",    "xytext": (5, -7),  "ha": "left"},
    20: {"text": "$W$=20",    "xytext": (-5, 5),  "ha": "right"},
    25: {"text": "$W$=25",    "xytext": (-5, -7), "ha": "right"},
}
for w, (prec, cov) in SS.items():
    if w == 10:
        continue
    cfg = LABEL_CFG[w]
    t = ax.annotate(cfg["text"], (cov, prec), fontsize=6,
                    textcoords="offset points", xytext=cfg["xytext"],
                    ha=cfg["ha"], color="0.35")
    t.set_path_effects([pe.withStroke(linewidth=1.2, foreground="white")])

# Two-stage dominant points
dom_cov = [v[1] for v in TS_DOMINANT.values()]
dom_prec = [v[0] for v in TS_DOMINANT.values()]
ax.scatter(dom_cov, dom_prec, c=C_DOM, s=65, marker="*", zorder=5,
           label="Two-stage (dominant)", edgecolors="white", linewidths=0.3)

# Two-stage labels -- separate offsets to avoid overlap
TS_LABEL_CFG = {
    (3, 15, 1): {"xytext": (6, 5),   "ha": "left"},   # above-right
    (3, 25, 1): {"xytext": (6, -7),  "ha": "left"},   # below-right
}
for (ws, wc, k), (prec, cov) in TS_DOMINANT.items():
    cfg = TS_LABEL_CFG[(ws, wc, k)]
    t = ax.annotate(f"({ws},{wc},{k})", (cov, prec), fontsize=5.5, color=C_DOM,
                    textcoords="offset points", xytext=cfg["xytext"],
                    ha=cfg["ha"], weight="bold")
    t.set_path_effects([pe.withStroke(linewidth=1.2, foreground="white")])

# Small arrow: W=15 single-stage -> (3,15,1) two-stage showing precision gain
# W=15 is at (cov=0.7692, prec=0.7091), (3,15,1) at (cov=0.7692, prec=0.7222)
ax.annotate("", xy=(0.7692, 0.7205), xytext=(0.7692, 0.7108),
            arrowprops=dict(arrowstyle="->", color=C_DOM, lw=0.7),
            zorder=6)
t = ax.text(0.775, 0.7155, "+1.3pp", fontsize=5, color=C_DOM,
            fontstyle="italic", ha="left", va="center")
t.set_path_effects([pe.withStroke(linewidth=1.0, foreground="white")])

ax.set_xlabel("Coverage (early detection rate)", fontsize=8)
ax.set_ylabel("Precision", fontsize=8)
ax.tick_params(axis="both", which="both", length=2, width=0.4, pad=2)
ax.grid(True, alpha=0.18, linewidth=0.3)

ax.set_ylim(0.698, 0.728)
ax.set_xlim(0.62, 0.88)

ax.legend(fontsize=6.5, framealpha=0.9, edgecolor="0.85",
          bbox_to_anchor=(0.0, 1.02), loc="lower left", borderpad=0.3,
          ncol=2, handlelength=1.3, handletextpad=0.3,
          columnspacing=1.0)

# ── Save ──────────────────────────────────────────────────────────
import os
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dir = os.path.join(base, "docs", "paper", "figures")
os.makedirs(out_dir, exist_ok=True)

out_pdf = os.path.join(out_dir, "pareto_two_stage.pdf")
out_png = out_pdf.replace(".pdf", ".png")
fig.savefig(out_pdf, bbox_inches="tight", dpi=300)
fig.savefig(out_png, bbox_inches="tight", dpi=300)
print(f"Saved: {out_pdf}")
print(f"Saved: {out_png}")
