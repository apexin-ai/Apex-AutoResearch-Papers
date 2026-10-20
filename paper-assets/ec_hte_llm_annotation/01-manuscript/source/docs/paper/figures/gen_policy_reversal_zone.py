"""
Generate Figure A.6: Policy Reversal Zone (two-panel figure).
Panel (A): Line plot of sign reversal probability vs True CATE for different configs.
Panel (B): Heatmap of reversal probability with tau_z0 on x-axis, delta_misclass on y-axis.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

# ─── Style setup ───────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "serif",
    "mathtext.fontset": "cm",
    "font.size": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 6.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 300,
})

# ─── Project palette ──────────────────────────────────────────────────────────
C_DANGER = "#D55E00"   # orange-red (global correction)
C_SAFE   = "#AAAAAA"   # gray (naive)
C_BLUE   = "#0072B2"   # blue (delta_misclass variants)

# ─── Load data ─────────────────────────────────────────────────────────────────
DATA_PATH = "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/policy_reversal_zone.csv"
df = pd.read_csv(DATA_PATH)

# ─── Panel A: Line plot ────────────────────────────────────────────────────────
# For the line plot, we show reversal probability averaged over delta_cate
# for different "configurations":
#   - "All configs (global)": average over all delta_misclass and delta_cate for each tau_z0
#   - "All configs (naive)": baseline at 0 (naive has no reversal since no correction)
#   - "High δ_misclass (≥0.15)": only high misclass values
#   - "Low δ_misclass (<0.05)": only low misclass values

# Aggregate for line plot
all_global = df.groupby("tau_z0")["pct_rev_global"].mean().reset_index()
all_global.columns = ["tau_z0", "pct"]

high_delta = df[df["delta_misclass"] >= 0.15].groupby("tau_z0")["pct_rev_global"].mean().reset_index()
high_delta.columns = ["tau_z0", "pct"]

low_delta = df[df["delta_misclass"] < 0.05].groupby("tau_z0")["pct_rev_global"].mean().reset_index()
low_delta.columns = ["tau_z0", "pct"]

# ─── Panel B: Heatmap ──────────────────────────────────────────────────────────
# Aggregate over delta_cate for (tau_z0, delta_misclass) pairs
heatmap_df = df.groupby(["tau_z0", "delta_misclass"])["pct_rev_global"].mean().reset_index()
heatmap_pivot = heatmap_df.pivot(index="delta_misclass", columns="tau_z0", values="pct_rev_global")

# Subsample for readability: select every other row for delta_misclass
delta_vals = sorted(heatmap_pivot.index)
# Select subset: 0, 0.05, 0.10, 0.15, 0.20, 0.25
delta_subset = [d for d in delta_vals if d in [0.0, 0.05, 0.10, 0.15, 0.20, 0.25]]
heatmap_sub = heatmap_pivot.loc[delta_subset]

# ─── Create figure ─────────────────────────────────────────────────────────────
fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7.5, 2.8),
                                  gridspec_kw={"width_ratios": [1, 1.2], "wspace": 0.35})

# ═══ Panel (A): Line plot ═══════════════════════════════════════════════════════
# Danger zone background band (light red, where reversal > 0 is concerning)
ax_a.axhspan(5, 50, color=C_DANGER, alpha=0.07, zorder=0)
ax_a.text(0.195, 37, "danger\nzone", fontsize=6.5, color=C_DANGER, alpha=0.65,
          fontstyle="italic", ha="right", va="center", linespacing=1.1)

# Naive baseline (always 0)
ax_a.axhline(0, color=C_SAFE, linewidth=1.2, linestyle="--", label="No correction (naive)", zorder=2)

# All configs global
ax_a.plot(all_global["tau_z0"], all_global["pct"], color=C_DANGER,
          linewidth=1.8, marker="o", markersize=4, label="All configs (global)", zorder=3)

# High delta_misclass
ax_a.plot(high_delta["tau_z0"], high_delta["pct"], color=C_DANGER,
          linewidth=1.2, marker="s", markersize=3.5, linestyle="--",
          alpha=0.7, label=r"High $\delta_{\mathrm{misclass}} \geq 0.15$", zorder=3)

# Low delta_misclass
ax_a.plot(low_delta["tau_z0"], low_delta["pct"], color=C_BLUE,
          linewidth=1.2, marker="^", markersize=3.5, linestyle="-",
          label=r"Low $\delta_{\mathrm{misclass}} < 0.05$", zorder=3)

ax_a.set_xlabel(r"True CATE $\tau(0)$")
ax_a.set_ylabel("Sign reversal probability (%)")
ax_a.set_xlim(-0.005, 0.21)
ax_a.set_ylim(-2, 50)
ax_a.legend(loc="upper right", framealpha=0.95, edgecolor="#CCCCCC",
            fancybox=False, borderpad=0.4, handlelength=1.8)

# Panel label
ax_a.text(-0.12, 1.05, "(A)", transform=ax_a.transAxes, fontsize=10, fontweight="bold", va="top")

# ═══ Panel (B): Heatmap ════════════════════════════════════════════════════════
# Custom colormap: white -> light orange -> dark orange-red
cmap_colors = ["#FFFFFF", "#FEE8D6", "#FDBE85", "#E6550D", "#A63603"]
cmap = LinearSegmentedColormap.from_list("reversal", cmap_colors, N=256)

im = ax_b.imshow(heatmap_sub.values, aspect="auto", cmap=cmap,
                 vmin=0, vmax=45, origin="lower", interpolation="nearest")

# Axis labels
tau_labels = [f"{v:.2f}" for v in heatmap_sub.columns]
delta_labels = [f"{v:.2f}" for v in heatmap_sub.index]

ax_b.set_xticks(range(len(tau_labels)))
ax_b.set_xticklabels(tau_labels, rotation=0)  # HORIZONTAL!
ax_b.set_yticks(range(len(delta_labels)))
ax_b.set_yticklabels(delta_labels)

ax_b.set_xlabel(r"True CATE $\tau(0)$")
ax_b.set_ylabel(r"$\delta_{\mathrm{misclass}}$")

# Cell annotations
for i in range(heatmap_sub.shape[0]):
    for j in range(heatmap_sub.shape[1]):
        val = heatmap_sub.values[i, j]
        # Use white text on dark cells, black on light
        text_color = "white" if val > 25 else "#333333"
        ax_b.text(j, i, f"{val:.0f}", ha="center", va="center",
                  fontsize=7, color=text_color)

# Colorbar
cbar = fig.colorbar(im, ax=ax_b, fraction=0.046, pad=0.04)
cbar.set_label("Reversal probability (%)", fontsize=7)
cbar.ax.tick_params(labelsize=6.5)
cbar.outline.set_linewidth(0.5)
cbar.outline.set_edgecolor("#888888")

# Re-enable spines for heatmap (looks better with frame)
for spine in ax_b.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(0.5)
    spine.set_color("#888888")

# Panel label
ax_b.text(-0.18, 1.05, "(B)", transform=ax_b.transAxes, fontsize=10, fontweight="bold", va="top")

# ─── Save ──────────────────────────────────────────────────────────────────────
OUT_DIR = "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/figures"
fig.savefig(f"{OUT_DIR}/policy_reversal_zone.pdf", bbox_inches="tight", dpi=300)
fig.savefig(f"{OUT_DIR}/policy_reversal_zone.png", bbox_inches="tight", dpi=300)
plt.close()
print("Done: saved policy_reversal_zone.pdf and .png")
