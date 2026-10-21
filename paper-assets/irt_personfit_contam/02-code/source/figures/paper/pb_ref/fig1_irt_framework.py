"""
Figure 1: IRT Person-Fit Framework for LLM Benchmark Contamination Detection
=============================================================================
2x2 composite figure for EMNLP 2026 paper.

Panels:
  (a) 4PL Item Characteristic Curve (ICC) with clean vs contaminated θ markers
  (b) ℓz* person-fit statistic distribution for clean vs contaminated seeds
  (c) θ-shift absorption: free-θ vs fixed-θ Cohen's |d| comparison
  (d) Dose-response trajectory across contamination levels

Style: Nature Publishing Group academic palette, minimal design.
Output: PDF + PNG at 300 DPI.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.stats import norm

# ---------------------------------------------------------------------------
# Style constants (Nature Publishing Group palette)
# ---------------------------------------------------------------------------
NAVY   = "#3C5488"
RED    = "#E64B35"
TEAL   = "#00A087"
GRAY   = "#999999"
LGRAY  = "#E5E5E5"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 8,
    "axes.labelsize": 9,
    "axes.titlesize": 9,
    "xtick.labelsize": 7.5,
    "ytick.labelsize": 7.5,
    "legend.fontsize": 7,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "lines.linewidth": 1.4,
    "axes.facecolor": "white",
    "figure.facecolor": "white",
    "axes.grid": True,
    "grid.color": LGRAY,
    "grid.linewidth": 0.4,
    "grid.alpha": 0.7,
})


def icc_4pl(theta, a=1.5, b=-0.5, c=0.25, d=0.92):
    """4-Parameter Logistic Item Characteristic Curve."""
    return c + (d - c) / (1 + np.exp(-a * (theta - b)))


# ---------------------------------------------------------------------------
# Create figure
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(7.2, 5.4), constrained_layout=True)

# ========================== Panel (a) ======================================
ax = axes[0, 0]
theta = np.linspace(-3, 3, 500)
p_theta = icc_4pl(theta)

ax.plot(theta, p_theta, color=NAVY, lw=2, zorder=5)

# Asymptotes
ax.axhline(0.25, color=GRAY, ls="--", lw=0.8, zorder=2)
ax.axhline(0.92, color=GRAY, ls="--", lw=0.8, zorder=2)
ax.text(2.6, 0.27, r"$c_i$ (guessing)", fontsize=6.5, color=GRAY, ha="right", va="bottom")
ax.text(2.6, 0.89, r"$d_i$ (upper asymp.)", fontsize=6.5, color=GRAY, ha="right", va="top")

# Clean model marker
theta_clean = 0.20
p_clean = icc_4pl(theta_clean)
ax.axvline(theta_clean, color=TEAL, ls="--", lw=1.0, zorder=3)
ax.plot(theta_clean, p_clean, "o", color=TEAL, ms=5, zorder=6)
ax.text(theta_clean + 0.15, 0.50, r"Clean" + "\n" + r"$\theta\!=\!+0.20$",
        fontsize=6, color=TEAL, va="center", ha="left",
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.8, pad=1))

# Contaminated model marker
theta_contam = -2.22
p_contam = icc_4pl(theta_contam)
ax.axvline(theta_contam, color=RED, ls="--", lw=1.0, zorder=3)
ax.plot(theta_contam, p_contam, "o", color=RED, ms=5, zorder=6)
ax.text(theta_contam - 0.15, 0.50, r"Contam." + "\n" + r"$\theta\!=\!-2.22$",
        fontsize=6, color=RED, va="center", ha="right",
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.8, pad=1))

ax.set_xlim(-3, 3)
ax.set_ylim(0, 1.02)
ax.set_xlabel(r"$\theta$ (Ability)")
ax.set_ylabel(r"$P$(correct)")
ax.set_title(r"$\mathbf{(a)}$ 4PL Item Response Model", loc="left", fontsize=9)

# ========================== Panel (b) ======================================
ax = axes[0, 1]

# Simulated ℓz* distributions
x_range = np.linspace(-5, 4, 500)
# Clean: centered ~+0.20, moderate spread
clean_pdf = norm.pdf(x_range, loc=0.20, scale=0.65)
# Contaminated: centered ~-2.22, slightly wider
contam_pdf = norm.pdf(x_range, loc=-2.22, scale=0.70)

ax.fill_between(x_range, clean_pdf, alpha=0.30, color=NAVY, zorder=3)
ax.plot(x_range, clean_pdf, color=NAVY, lw=1.5, zorder=4, label="Clean seeds (N=10)")
ax.fill_between(x_range, contam_pdf, alpha=0.30, color=RED, zorder=3)
ax.plot(x_range, contam_pdf, color=RED, lw=1.5, zorder=4, label="Contaminated")

# Delta arrow between peaks
y_arrow = max(max(clean_pdf), max(contam_pdf)) * 0.60
ax.annotate("", xy=(0.20, y_arrow), xytext=(-2.22, y_arrow),
            arrowprops=dict(arrowstyle="<->", color="k", lw=1.2), zorder=6)
ax.text((-2.22 + 0.20) / 2, y_arrow + 0.02,
        r"$\Delta\ell_z^* = 2.4$", fontsize=7.5,
        ha="center", va="bottom", fontweight="bold", zorder=6)

ax.set_xlim(-4.5, 3)
ax.set_ylim(0, None)
ax.set_xlabel(r"$\ell_z^*$ (Person-Fit Statistic)")
ax.set_ylabel("Density")
ax.set_title(r"$\mathbf{(b)}$ $\ell_z^*$ Detection Signal", loc="left", fontsize=9)
ax.legend(loc="upper right", frameon=True, framealpha=0.9, edgecolor=LGRAY)

# ========================== Panel (c) ======================================
ax = axes[1, 0]

labels = [r"Free-$\theta$", r"Fixed-$\theta$"]
values = [5.08, 12.32]
colors = [NAVY, TEAL]

bars = ax.bar(labels, values, width=0.55, color=colors, edgecolor="white", lw=0.5, zorder=4)

# Value labels on top
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.25,
            f"{val:.2f}", ha="center", va="bottom", fontsize=8, fontweight="bold")

# Amplification annotation (bracket with arrow)
x0 = bars[0].get_x() + bars[0].get_width() / 2
x1 = bars[1].get_x() + bars[1].get_width() / 2
y_top = 13.2
ax.annotate("", xy=(x1, y_top), xytext=(x0, y_top),
            arrowprops=dict(arrowstyle="->", color="k", lw=1.2), zorder=6)
ax.text((x0 + x1) / 2, y_top + 0.25, r"$2.4\times$", fontsize=8,
        ha="center", va="bottom", fontweight="bold", zorder=6)

ax.set_ylim(0, 15)
ax.set_ylabel(r"Cohen's $|d|$")
ax.set_title(r"$\mathbf{(c)}$ $\theta$-Shift Absorption", loc="left", fontsize=9)

# ========================== Panel (d) ======================================
ax = axes[1, 1]

contam_levels = [5, 15, 25, 50]
qwen_d = [4.15, 5.36, 7.44, 5.08]
llama_d = [2.57, 2.80, 2.56, 2.30]

ax.plot(contam_levels, qwen_d, "o-", color=NAVY, ms=6, lw=1.8,
        label="Qwen-2.5-7B", zorder=5)
ax.plot(contam_levels, llama_d, "s--", color=RED, ms=5, lw=1.5,
        label="Llama-3.1-8B", zorder=5)

# Annotate peak at 25%
peak_idx = 2  # 25%
ax.annotate("peak", xy=(contam_levels[peak_idx], qwen_d[peak_idx]),
            xytext=(contam_levels[peak_idx] + 5, qwen_d[peak_idx] + 0.8),
            fontsize=7, color=NAVY, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.8),
            zorder=6)

ax.set_xlim(0, 55)
ax.set_ylim(0, 9)
ax.set_xlabel("Contamination Level (%)")
ax.set_ylabel(r"Cohen's $|d|$")
ax.set_xticks(contam_levels)
ax.set_title(r"$\mathbf{(d)}$ Dose-Response (Free-$\theta$)", loc="left", fontsize=9)
ax.legend(loc="upper left", frameon=True, framealpha=0.9, edgecolor=LGRAY)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
import os
out_dir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(out_dir, "fig1_irt_framework.png"), dpi=300, bbox_inches="tight")
fig.savefig(os.path.join(out_dir, "fig1_irt_framework.pdf"), bbox_inches="tight")
print(f"Saved to {out_dir}/fig1_irt_framework.png and .pdf")
plt.close(fig)
