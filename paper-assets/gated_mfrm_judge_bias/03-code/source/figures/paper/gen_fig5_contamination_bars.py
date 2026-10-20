"""Generate fig5_contamination_bars.pdf: Lollipop chart of contamination susceptibility."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

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
    ("gemma-2-9b",        1.6536, 0.3565, 2.9143),
    ("gpt-3.5-turbo-0125",5.5871, 4.4174, 6.7825),
    ("gpt-4-0613",        4.1681, 3.1019, 5.2684),
    ("gpt-4o",            0.8805, 0.0516, 2.2113),
    ("gpt-4o-mini",       0.9345, 0.0590, 2.2139),
    ("llama-3.3-70b",     2.4780, 1.0878, 3.9163),
    ("qwen2.5-72b",       2.9610, 1.4025, 4.5926),
    ("qwen3-8b",          1.1782, 0.1391, 2.4994),
]

names = [d[0] for d in data]
cn    = np.array([d[1] for d in data])
cn_lo = np.array([d[2] for d in data])
cn_hi = np.array([d[3] for d in data])

order = np.argsort(cn)[::-1]

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

fig, ax = plt.subplots(figsize=(5.0, 2.2))
n = len(names)

for rank, idx in enumerate(order):
    y = n - 1 - rank
    color = PROP_COLOR if names[idx] in PROPRIETARY else OPEN_COLOR

    # lollipop stem: thin line from x=0 to point estimate
    ax.plot([0, cn[idx]], [y, y], color=color, lw=1.2, solid_capstyle="round", zorder=2)

    # lollipop head: filled circle at point estimate
    ax.plot(cn[idx], y, "o", color=color, markersize=6,
            markeredgecolor="white", markeredgewidth=0.4, zorder=4)

    # CI whisker: thinner line
    ax.plot([cn_lo[idx], cn_hi[idx]], [y, y],
            color=color, lw=0.6, solid_capstyle="round", alpha=0.5, zorder=3)

ax.set_yticks(range(n))
ax.set_yticklabels([DISPLAY[names[order[n - 1 - i]]] for i in range(n)], fontsize=8)
ax.set_xlabel(r"$\hat{c}_n$ (posterior mean $\pm$ 95% CI)", fontsize=9)
ax.set_xlim(-0.3, 7.5)
ax.set_ylim(-0.5, n - 0.5)
ax.grid(axis="x", alpha=0.15, lw=0.4)
ax.axvline(0, color="#CCCCCC", lw=0.5, zorder=0)

from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker="o", color="w", markerfacecolor=PROP_COLOR,
           markersize=5, label="Proprietary"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor=OPEN_COLOR,
           markersize=5, label="Open-source"),
]
ax.legend(handles=legend_elements, loc="lower right", fontsize=7,
          framealpha=0.9, edgecolor="#CCCCCC", handletextpad=0.3)

fig.tight_layout(pad=0.3)
fig.savefig(f"{OUT_DIR}/fig5_contamination_bars.pdf", bbox_inches="tight", dpi=300)
fig.savefig(f"{OUT_DIR}/fig5_contamination_bars.png", bbox_inches="tight", dpi=300)
plt.close(fig)
print("Done: fig5_contamination_bars.pdf + fig5_contamination_bars.png")
