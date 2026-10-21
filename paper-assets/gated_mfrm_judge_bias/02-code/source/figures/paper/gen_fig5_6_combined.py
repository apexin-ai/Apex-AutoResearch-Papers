"""Generate fig5_6_combined.pdf: Two-panel figure* combining contamination
susceptibility (a) and bias absorption (b) as paired lollipop charts."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

OUT_DIR = "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper"

DISPLAY = {
    "gemma-2-9b": "Gemma-2-9B",
    "gpt-3.5-turbo-0125": "GPT-3.5-Turbo",
    "gpt-4-0613": "GPT-4-0613",
    "gpt-4o": "GPT-4o",
    "gpt-4o-mini": "GPT-4o-mini",
    "llama-3.3-70b": "LLaMA-3.3-70B",
    "qwen2.5-72b": "Qwen2.5-72B",
    "qwen3-8b": "Qwen3-8B",
}

PROPRIETARY = {"gpt-3.5-turbo-0125", "gpt-4-0613", "gpt-4o", "gpt-4o-mini"}

data = [
    ("gemma-2-9b",        1.6536, 0.3565, 2.9143, -0.1611),
    ("gpt-3.5-turbo-0125",5.5871, 4.4174, 6.7825,  0.7864),
    ("gpt-4-0613",        4.1681, 3.1019, 5.2684,  0.4311),
    ("gpt-4o",            0.8805, 0.0516, 2.2113, -0.3967),
    ("gpt-4o-mini",       0.9345, 0.0590, 2.2139, -0.3678),
    ("llama-3.3-70b",     2.4780, 1.0878, 3.9163, -0.0217),
    ("qwen2.5-72b",       2.9610, 1.4025, 4.5926,  0.0350),
    ("qwen3-8b",          1.1782, 0.1391, 2.4994, -0.3053),
]

names  = [d[0] for d in data]
cn     = np.array([d[1] for d in data])
cn_lo  = np.array([d[2] for d in data])
cn_hi  = np.array([d[3] for d in data])
dtheta = np.array([d[4] for d in data])

order = np.argsort(cn)[::-1]  # descending by c_n

rho, _ = stats.spearmanr(cn, dtheta)

PROP_COLOR = "#0072B2"
OPEN_COLOR = "#D55E00"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif", "Times"],
    "mathtext.fontset": "cm",
    "font.size": 10,
    "axes.labelsize": 10,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(7.0, 2.2),
                                gridspec_kw={"width_ratios": [1, 1.2]})
n = len(names)

for rank, idx in enumerate(order):
    y = n - 1 - rank
    color = PROP_COLOR if names[idx] in PROPRIETARY else OPEN_COLOR

    # alternating row background
    if rank % 2 == 0:
        for ax in (ax1, ax2):
            ax.axhspan(y - 0.4, y + 0.4, color="#f5f5f5", zorder=0)

    # --- Panel (a): c_n lollipop with CI ---
    ax1.plot([0, cn[idx]], [y, y], color=color, lw=1.2,
             solid_capstyle="round", zorder=2)
    ax1.plot(cn[idx], y, "o", color=color, markersize=5.5,
             markeredgecolor="white", markeredgewidth=0.4, zorder=4)
    ax1.plot([cn_lo[idx], cn_hi[idx]], [y, y],
             color=color, lw=0.6, solid_capstyle="round", alpha=0.5, zorder=3)

    # --- Panel (b): Δθ lollipop ---
    ax2.plot([0, dtheta[idx]], [y, y], color=color, lw=1.2,
             solid_capstyle="round", zorder=2)
    ax2.plot(dtheta[idx], y, "o", color=color, markersize=5.5,
             markeredgecolor="white", markeredgewidth=0.4, zorder=4)
    sign = "+" if dtheta[idx] > 0 else ""
    nudge = 0.04 if dtheta[idx] >= 0 else -0.04
    ha = "left" if dtheta[idx] >= 0 else "right"
    ax2.text(dtheta[idx] + nudge, y, f"{sign}{dtheta[idx]:.2f}",
             fontsize=6.5, va="center", ha=ha, color="#555555")

# y-axis labels
ax1.set_yticks(range(n))
ax1.set_yticklabels([DISPLAY[names[order[n - 1 - i]]] for i in range(n)],
                    fontsize=8)
ax1.set_ylim(-0.5, n - 0.5)

# panel (a) styling
ax1.axvline(0, color="#CCCCCC", lw=0.5, zorder=1)
ax1.set_xlabel(r"$\hat{c}_n$ (posterior mean $\pm$ 95% CI)", fontsize=9)
ax1.set_xlim(-0.3, 7.5)
ax1.grid(axis="x", alpha=0.15, lw=0.4)

# panel (b) styling
ax2.axvline(0, color="#888888", ls="--", lw=0.7, alpha=0.6, zorder=1)
ax2.set_xlabel(r"$\Delta\theta$ (MFRM $-$ G-MFRM)", fontsize=9)
ax2.set_xlim(-0.65, 1.1)
ax2.grid(axis="x", alpha=0.15, lw=0.4)

# panel labels as titles (outside axes, no overlap with data)
ax1.set_title("(a)", loc="left", fontsize=9, fontweight="bold", pad=4)
ax2.set_title("(b)", loc="left", fontsize=9, fontweight="bold", pad=4)

# Spearman rho annotation in panel (b)
ax2.text(0.95, 0.08, f"Spearman $\\rho$ = {rho:.1f}",
         transform=ax2.transAxes, fontsize=7.5, ha="right",
         bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#CCCCCC",
                   alpha=0.9, lw=0.5), zorder=5)

# legend in panel (a)
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker="o", color="w", markerfacecolor=PROP_COLOR,
           markersize=5, label="Proprietary"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor=OPEN_COLOR,
           markersize=5, label="Open-source"),
]
ax1.legend(handles=legend_elements, loc="lower right", fontsize=6.5,
           framealpha=0.9, edgecolor="#CCCCCC", handletextpad=0.3)

fig.tight_layout(w_pad=1.5, pad=0.3)
fig.savefig(f"{OUT_DIR}/fig5_6_combined.pdf", bbox_inches="tight", dpi=300)
fig.savefig(f"{OUT_DIR}/fig5_6_combined.png", bbox_inches="tight", dpi=300)
plt.close(fig)
print("Done: fig5_6_combined.pdf + fig5_6_combined.png")
