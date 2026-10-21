"""Generate forest_dj.pdf: Dot-and-whisker judge severity plot."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_DIR = "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper"

# d_j data from exp-003b (posterior mean, 95% CI lower, 95% CI upper)
data = [
    ("Claude Opus 4.7",    0.60,  0.43,   0.76),
    ("GPT-5.5",            0.53,  0.37,   0.70),
    ("DeepSeek-V4-Pro",    0.31,  0.073,  0.54),
    ("Claude Sonnet 4.6",  0.14, -0.037,  0.31),
    ("Gemini-2.5-Pro",    -0.036,-0.27,   0.19),
    ("Qwen3-235B",        -0.038,-0.24,   0.16),
    ("Qwen2.5-72B",       -0.35, -0.64,  -0.066),
    ("LLaMA-3.3-70B",     -0.42, -0.66,  -0.18),
    ("Mistral-Large-2",   -0.74, -1.1,   -0.37),
]

names  = [d[0] for d in data]
means  = np.array([d[1] for d in data])
ci_lo  = np.array([d[2] for d in data])
ci_hi  = np.array([d[3] for d in data])

order = np.argsort(means)[::-1]  # descending by d_j

PROP_COLOR = "#2166ac"
OPEN_COLOR = "#b2182b"
proprietary = {"Claude Opus 4.7", "GPT-5.5", "Claude Sonnet 4.6",
               "DeepSeek-V4-Pro", "Gemini-2.5-Pro"}

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif", "Times"],
    "mathtext.fontset": "cm",
    "font.size": 10,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
})

fig, ax = plt.subplots(figsize=(3.4, 2.6))
n = len(names)

for rank, idx in enumerate(order):
    color = PROP_COLOR if names[idx] in proprietary else OPEN_COLOR
    y = n - 1 - rank

    # alternating background stripes
    if rank % 2 == 0:
        ax.axhspan(y - 0.4, y + 0.4, color="#f5f5f5", zorder=0)

    # CI whisker line
    ax.plot([ci_lo[idx], ci_hi[idx]], [y, y],
            color=color, lw=1.0, solid_capstyle="round", alpha=0.85, zorder=3)

    # point estimate dot
    ax.plot(means[idx], y, "o", color=color, markersize=5.5,
            markeredgecolor="white", markeredgewidth=0.5, zorder=5)

    # value annotation
    ax.text(ci_hi[idx] + 0.06, y, f"{means[idx]:+.1f}",
            fontsize=7, va="center", ha="left", color="#444444")

# zero reference line
ax.axvline(0, color="#888888", ls="--", lw=0.7, alpha=0.6, zorder=1)

ax.set_yticks(range(n))
ax.set_yticklabels([names[order[n - 1 - i]] for i in range(n)], fontsize=8)
ax.set_xlabel(r"$d_j$ (judge severity)", fontsize=10)
ax.set_xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
ax.set_xlim(-1.25, 1.15)
ax.set_ylim(-0.5, n - 0.5)

from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker="o", color="w", markerfacecolor=PROP_COLOR,
           markersize=6, label="Proprietary"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor=OPEN_COLOR,
           markersize=6, label="Open-source"),
]
ax.legend(handles=legend_elements, loc="lower right", fontsize=7,
          frameon=False, handletextpad=0.3)

fig.tight_layout(pad=0.3)
fig.savefig(f"{OUT_DIR}/forest_dj.pdf", bbox_inches="tight", dpi=300)
fig.savefig(f"{OUT_DIR}/forest_dj.png", bbox_inches="tight", dpi=300)
plt.close(fig)
print("Done: forest_dj.pdf + forest_dj.png")
