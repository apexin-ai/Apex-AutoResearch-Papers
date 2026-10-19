#!/usr/bin/env python3
"""Generate fig2_sparsity_sweep: PPL vs Sparsity for KL Predictor, Vanilla TEAL, WINA."""

import json
import pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
DATA_PATH = HERE / "fig2_data.json"
OUT_PDF = HERE / "fig2_sparsity_sweep.pdf"
OUT_PNG = HERE / "fig2_sparsity_sweep.png"

with open(DATA_PATH) as f:
    data = json.load(f)

sparsity = data["sparsity"]
dense_ppl = data["dense_baseline"]
methods = data["methods"]

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "mathtext.fontset": "stix",
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

fig, ax = plt.subplots(figsize=(5.0, 3.8))

ax.set_yscale("log")

ax.axhline(y=dense_ppl, color="grey", linestyle="--", linewidth=1.0, alpha=0.7, zorder=1)
ax.text(sparsity[0] - 1.5, dense_ppl * 0.88, f"Dense ({dense_ppl})",
        fontsize=9, color="grey", ha="left", va="top")

for name, m in methods.items():
    ax.plot(sparsity, m["ppl"],
            color=m["color"], linestyle=m["linestyle"], marker=m["marker"],
            markersize=7, linewidth=2.0, label=m["label"], zorder=3)

# Annotate KL vs TEAL gap at each sparsity level
kl_ppl = methods["KL Predictor"]["ppl"]
teal_ppl = methods["Vanilla TEAL"]["ppl"]
kl_color = methods["KL Predictor"]["color"]
teal_color = methods["Vanilla TEAL"]["color"]
wina_color = methods["WINA"]["color"]

# 30% gap annotation
gap_30 = teal_ppl[0] - kl_ppl[0]
ax.annotate(f"Δ={gap_30:.2f}",
            xy=(sparsity[0], np.sqrt(kl_ppl[0] * teal_ppl[0])),
            xytext=(sparsity[0] - 5.5, np.sqrt(kl_ppl[0] * teal_ppl[0]) * 1.15),
            fontsize=8, color="#555555", fontweight="bold",
            ha="center", va="bottom")

# 50% gap annotation
gap_50 = teal_ppl[1] - kl_ppl[1]
ax.annotate(f"Δ={gap_50:.1f}",
            xy=(sparsity[1], np.sqrt(kl_ppl[1] * teal_ppl[1])),
            xytext=(sparsity[1] + 0.5, np.sqrt(kl_ppl[1] * teal_ppl[1]) * 1.2),
            fontsize=8, color="#555555", fontweight="bold",
            ha="center", va="bottom")

# 70% annotations with values
kl_70 = kl_ppl[2]
teal_70 = teal_ppl[2]
wina_70 = methods["WINA"]["ppl"][2]

ax.annotate(f"{kl_70:.1f}",
            xy=(70, kl_70), xytext=(72.5, kl_70 * 0.72),
            fontsize=8.5, color=kl_color, fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=kl_color, lw=0.8, alpha=0.6),
            ha="left", va="center")

ax.annotate(f"{teal_70:.1f}",
            xy=(70, teal_70), xytext=(72.5, teal_70),
            fontsize=8.5, color=teal_color, fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=teal_color, lw=0.8, alpha=0.6),
            ha="left", va="center")

ax.annotate(f"{wina_70:.1f}",
            xy=(70, wina_70), xytext=(72.5, wina_70 * 1.15),
            fontsize=8.5, color=wina_color, fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=wina_color, lw=0.8, alpha=0.6),
            ha="left", va="center")

# Bracket showing gap at 70%
bracket_x = 68.2
ax.annotate("", xy=(bracket_x, kl_70), xytext=(bracket_x, wina_70),
            arrowprops=dict(arrowstyle="<->", color="#555555", lw=1.2))
gap_mid = np.sqrt(kl_70 * wina_70)
ax.text(bracket_x - 1.5, gap_mid, f"{wina_70/kl_70:.1f}×\n(WINA vs Ours)",
        fontsize=8.5, color="#555555", ha="right", va="center", fontweight="bold")

ax.set_xlabel("Sparsity (%)")
ax.set_ylabel("Perplexity (log scale)")
ax.set_xticks(sparsity)
ax.set_xticklabels([f"{s:.0f}%" if s == int(s) else f"{s}%" for s in sparsity])
ax.set_xlim(22, 80)

ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
ax.yaxis.set_minor_formatter(ticker.NullFormatter())
ax.set_yticks([6, 10, 20, 50, 100, 140])
ax.get_yaxis().set_major_formatter(ticker.ScalarFormatter())
ax.ticklabel_format(axis="y", style="plain")

ax.legend(loc="upper left", frameon=True, fancybox=False, edgecolor="#cccccc",
          framealpha=0.95)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.25, which="major")

fig.savefig(OUT_PDF, format="pdf")
fig.savefig(OUT_PNG, format="png")
plt.close(fig)

print(f"Saved: {OUT_PDF}")
print(f"Saved: {OUT_PNG}")
