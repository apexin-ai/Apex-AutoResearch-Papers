"""
Generate Figure A.5: Treatment-dependent misclassification sensitivity.
Three-panel line plot: |Bias|, RMSE, Coverage vs gamma_T.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# ── Style ──────────────────────────────────────────────────────────────────
mpl.rcParams.update({
    "font.family": "serif",
    "mathtext.fontset": "cm",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.labelsize": 7.5,
    "ytick.labelsize": 7.5,
    "axes.labelsize": 8.5,
    "axes.titlesize": 8.5,
    "figure.dpi": 300,
})

# ── Data ───────────────────────────────────────────────────────────────────
DATA_PATH = "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/treatment_dep_misclass_summary.csv"
df = pd.read_csv(DATA_PATH)

# Method config: label, color, marker, linestyle
METHOD_CFG = {
    "naive":            ("Naive",        "#0072B2", "o", "-"),
    "global_corrected": ("Global Corr.", "#D55E00", "s", "--"),
    "hb_ec_hte":        ("EC-HTE",      "#009E73", "^", "-"),
}

# Per-panel vertical offsets (points) for direct labels to avoid overlap.
# Tuned manually based on the endpoint values:
#   mean_abs_bias @ 0.20: naive=0.186, global=0.182, ec-hte=0.195
#   rmse @ 0.20:          naive=0.202, global=0.210, ec-hte=0.224
#   coverage @ 0.20:      naive=0.200, global=0.415, ec-hte=0.370
LABEL_OFFSETS = {
    "mean_abs_bias": {"naive": -8, "global_corrected": 1, "hb_ec_hte": 8},
    "rmse":          {"naive": -8, "global_corrected": 1, "hb_ec_hte": 8},
    "coverage":      {"naive": -6, "global_corrected": 7, "hb_ec_hte": -6},
}

# ── Figure ─────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(7.5, 2.6), sharex=True)

panels = [
    ("mean_abs_bias", r"|Bias|",    r"(a) Bias grows with $\gamma_T$"),
    ("rmse",          "RMSE",       r"(b) RMSE tracks bias pattern"),
    ("coverage",      "Coverage",   r"(c) Coverage drops below 95\%"),
]

for ax, (col, ylabel, title) in zip(axes, panels):
    for method, (label, color, marker, ls) in METHOD_CFG.items():
        sub = df[df["method"] == method].sort_values("gamma_T")
        ax.plot(
            sub["gamma_T"], sub[col],
            color=color, marker=marker, markersize=4,
            linestyle=ls, linewidth=1.3, label=label,
            markeredgewidth=0.4, markeredgecolor="white",
            clip_on=False, zorder=3,
        )
        # Direct label at end of line
        x_end = sub["gamma_T"].iloc[-1]
        y_end = sub[col].iloc[-1]
        y_off = LABEL_OFFSETS[col][method]
        ax.annotate(
            label,
            xy=(x_end, y_end),
            xytext=(5, y_off),
            textcoords="offset points",
            fontsize=6.2,
            fontweight="bold",
            color=color,
            va="center",
            clip_on=False,
        )

    # 95% reference line for coverage panel
    if col == "coverage":
        ax.axhline(0.95, color="#999999", linestyle=":", linewidth=0.7, zorder=0)
        # Place "95%" label inside the plot area, aligned left
        ax.text(
            0.20, 0.95, " 95%", fontsize=6, color="#999999",
            va="bottom", ha="right",
        )

    ax.set_title(title, fontsize=8, fontweight="bold", pad=6, loc="left")
    ax.set_ylabel(ylabel)
    ax.set_xlabel(r"$\gamma_T$")

    # Light horizontal grid
    ax.yaxis.grid(True, linewidth=0.25, alpha=0.5, color="#cccccc")
    ax.set_axisbelow(True)

# x-ticks
for ax in axes:
    ax.set_xticks([0.0, 0.05, 0.10, 0.15, 0.20])
    ax.set_xticklabels(["0", "0.05", "0.10", "0.15", "0.20"])
    ax.set_xlim(-0.01, 0.215)

plt.tight_layout(w_pad=1.8)
# Extra right margin for direct labels
fig.subplots_adjust(right=0.86)

# ── Save ───────────────────────────────────────────────────────────────────
OUT_DIR = "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/figures"
fig.savefig(f"{OUT_DIR}/treatment_dep_misclass.pdf", bbox_inches="tight", dpi=300)
fig.savefig(f"{OUT_DIR}/treatment_dep_misclass.png", bbox_inches="tight", dpi=300)
plt.close()
print("Done: treatment_dep_misclass.pdf/.png")
