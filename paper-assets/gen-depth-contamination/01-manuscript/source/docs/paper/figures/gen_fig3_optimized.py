#!/usr/bin/env python3
"""Figure 3: K*(theta) — two-panel, full textwidth.
Data source: Table 1 (tab:kstar_ci) + extended table. Qwen cross-scored."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.lines import Line2D

PAIR_KEYS = ["0v1", "1v2", "2v3", "3v4", "4v5"]

# Data updated to match paper tables (Qwen cross-scored)
MODELS = {
    "Qwen-rw": {
        "mean":     [0.9956, 0.6955, 0.5893, 0.5435, 0.5340],
        "ci_lower": [0.993, 0.686, 0.580, 0.534, 0.524],
        "ci_upper": [0.998, 0.704, 0.599, 0.553, 0.544],
    },
    "Pythia": {
        "mean":     [0.9722, 0.6074, 0.5440, 0.5051, 0.5079],
        "ci_lower": [0.967, 0.598, 0.534, 0.495, 0.498],
        "ci_upper": [0.977, 0.617, 0.554, 0.515, 0.518],
    },
    "OLMo": {
        "mean":     [0.9861, 0.5001, 0.4973, 0.5034, 0.4971],
        "ci_lower": [0.984, 0.496, 0.486, 0.492, 0.484],
        "ci_upper": [0.989, 0.519, 0.509, 0.513, 0.505],
    },
    "Qwen-cont": {
        "mean":     [0.9971, 0.6112, 0.5609, 0.5409, 0.5141],
        "ci_lower": [0.996, 0.602, 0.551, 0.531, 0.504],
        "ci_upper": [0.999, 0.621, 0.571, 0.551, 0.524],
    },
    "Qwen-7B": {
        "mean":     [0.9644, 0.6178, 0.5492, 0.5276, 0.5085],
        "ci_lower": [0.961, 0.608, 0.539, 0.518, 0.499],
        "ci_upper": [0.967, 0.626, 0.559, 0.537, 0.519],
    },
}

COLORS = {
    "Qwen-rw":   "#0072B2",
    "Pythia":    "#D55E00",
    "OLMo":      "#BBBBBB",
    "Qwen-cont": "#009E73",
    "Qwen-7B":   "#CC79A7",
}
MARKERS = {"Qwen-rw": "o", "Pythia": "s", "OLMo": "x", "Qwen-cont": "^", "Qwen-7B": "D"}


def compute_kstar(means, theta):
    k = 0
    for v in means:
        if v > theta:
            k += 1
        else:
            break
    return k


plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.linewidth": 0.5,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.03,
})

fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7, 2.6),
                                  gridspec_kw={"width_ratios": [1, 1.2], "wspace": 0.35})

x = np.arange(len(PAIR_KEYS))

# ═══════════════════════════════════════════════════════════════
# Panel (a): AUC profile
# ═══════════════════════════════════════════════════════════════

# Discriminable zone
ax_a.axhspan(0.60, 1.05, color="#F0F7F0", alpha=0.4, zorder=0, lw=0)

# K*=2 depth region highlight
ax_a.axvspan(0.5, 1.5, color="#E3F2FD", alpha=0.35, zorder=0, lw=0)
t_k = ax_a.text(1.0, 0.65, r"$K^*{=}2$", ha="center", fontsize=7.5,
                color="#0072B2", alpha=0.6, fontweight="bold")

# θ reference
ax_a.axhline(0.60, color="#888888", ls="--", lw=0.7, zorder=1)
t = ax_a.text(4.3, 0.607, r"$\theta{=}0.60$", fontsize=6.5, color="#666666",
              va="bottom", ha="right")
t.set_path_effects([pe.withStroke(linewidth=1.8, foreground="white")])

for name, data in MODELS.items():
    c, m = COLORS[name], MARKERS[name]
    means = np.array(data["mean"])
    lo, hi = np.array(data["ci_lower"]), np.array(data["ci_upper"])

    is_olmo = name == "OLMo"
    ls = "--" if is_olmo else "-"
    lw = 0.8 if is_olmo else 1.3
    alpha = 0.6 if is_olmo else 1.0

    ax_a.fill_between(x, lo, hi, color=c, alpha=0.06 if is_olmo else 0.10, zorder=2, lw=0)
    ax_a.plot(x, means, ls, color=c, lw=lw, marker=m, markersize=3.5,
              markeredgewidth=0.3, markeredgecolor="white" if not is_olmo else c,
              label=name, zorder=4 if not is_olmo else 3, alpha=alpha,
              solid_capstyle="round")

ax_a.set_xticks(x)
ax_a.set_xticklabels(PAIR_KEYS, fontsize=7.5)
ax_a.set_xlabel("Depth pair", fontsize=8.5)
ax_a.set_ylabel("Pairwise AUC", fontsize=8.5)
ax_a.set_ylim(0.47, 1.02)
ax_a.set_xlim(-0.2, len(PAIR_KEYS) - 0.7)
ax_a.tick_params(direction="in", labelsize=7, length=2.5)
ax_a.legend(fontsize=6, loc="center right", framealpha=0.95, edgecolor="#DDDDDD",
            fancybox=True, handlelength=1.5, borderpad=0.3, labelspacing=0.15)
ax_a.set_title(r"$\mathbf{(a)}$ Pairwise AUC profile", fontsize=8.5, loc="left", pad=4)

# ═══════════════════════════════════════════════════════════════
# Panel (b): K*(theta) step functions
# ═══════════════════════════════════════════════════════════════
thetas = np.arange(0.50, 0.751, 0.005)

all_kstar = {}
for name, data in MODELS.items():
    ks = [compute_kstar(data["mean"], t) for t in thetas]
    all_kstar[name] = ks

kstar_arr = np.array(list(all_kstar.values()))
k_min = kstar_arr.min(axis=0)
k_max = kstar_arr.max(axis=0)

# Consensus K*=2 bands
mask_all2 = (k_min == 2) & (k_max == 2)
for j in range(len(thetas)):
    if mask_all2[j]:
        ax_b.axvspan(thetas[j] - 0.0025, thetas[j] + 0.0025,
                     color="#E3F2FD", alpha=0.5, linewidth=0, zorder=0)

for name, ks in all_kstar.items():
    c = COLORS[name]
    lw = 0.8 if name == "OLMo" else 1.3
    alpha = 0.6 if name == "OLMo" else 1.0
    ax_b.step(thetas, ks, where="post", color=c, linewidth=lw, label=name,
              zorder=3, alpha=alpha)

ax_b.axvline(x=0.60, color="#888888", ls="--", lw=0.7, alpha=0.7, zorder=1)
t2 = ax_b.text(0.603, 3.3, r"$\theta{=}0.60$", color="#666666", fontsize=6.5, va="top")
t2.set_path_effects([pe.withStroke(linewidth=1.8, foreground="white")])

# "Plateau" annotation
ax_b.annotate("stable plateau", xy=(0.585, 2), xytext=(0.655, 2.6),
              fontsize=6, color="#555555", fontstyle="italic",
              arrowprops=dict(arrowstyle="->", color="#AAAAAA", lw=0.6,
                              connectionstyle="arc3,rad=-0.15"))

consensus_patch = mpatches.Patch(color="#E3F2FD", alpha=0.5,
                                  label=r"$K^*{=}2$ (all models)")
model_lines = [Line2D([0], [0], color=COLORS[n], lw=1.3, label=n,
                       alpha=0.6 if n == "OLMo" else 1.0)
               for n in all_kstar.keys()]
ax_b.legend(handles=[consensus_patch] + model_lines, fontsize=6,
            loc="upper right", framealpha=0.95, edgecolor="#DDDDDD",
            fancybox=True, handlelength=1.5, borderpad=0.3, labelspacing=0.15)

ax_b.set_xlabel(r"Threshold $\theta$", fontsize=8.5)
ax_b.set_ylabel(r"$K^*(\theta)$", fontsize=8.5)
ax_b.set_xlim(0.495, 0.72)
ax_b.set_ylim(-0.15, 3.8)
ax_b.set_yticks([0, 1, 2, 3])
ax_b.tick_params(direction="in", labelsize=7, length=2.5)
ax_b.set_title(r"$\mathbf{(b)}$ $K^*(\theta)$ sensitivity", fontsize=8.5, loc="left", pad=4)

fig.subplots_adjust(left=0.08, right=0.97, top=0.92, bottom=0.16, wspace=0.35)

out = "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures"
fig.savefig(f"{out}/fig_kstar_theta.pdf")
fig.savefig(f"{out}/fig_kstar_theta.png")
plt.close(fig)
print("OK fig3")
