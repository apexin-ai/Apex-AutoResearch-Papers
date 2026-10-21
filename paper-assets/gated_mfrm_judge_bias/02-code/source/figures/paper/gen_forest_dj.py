"""Generate forest_dj.pdf: Judge severity estimates with 95% CI."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT_DIR = "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper"

# d_j data from exp-003b (posterior mean, 95% CI)
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

order = np.argsort(means)

PROP_COLOR = "#2171B5"
OPEN_COLOR = "#CB181D"
proprietary = {"Claude Opus 4.7", "GPT-5.5", "Claude Sonnet 4.6",
               "DeepSeek-V4-Pro", "Gemini-2.5-Pro"}

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Times New Roman", "Times"],
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

fig, ax = plt.subplots(figsize=(3.4, 2.8))
y_pos = np.arange(len(names))

for rank, idx in enumerate(order):
    color = PROP_COLOR if names[idx] in proprietary else OPEN_COLOR
    ax.plot([ci_lo[idx], ci_hi[idx]], [rank, rank],
            color=color, lw=2.8, solid_capstyle="round", alpha=0.75)
    ax.plot(means[idx], rank, "o", color="#222222", markersize=4.5, zorder=5)

ax.axvline(0, color="#999999", ls="--", lw=0.7, alpha=0.5)
ax.grid(axis="x", alpha=0.2, lw=0.5)

ax.set_yticks(y_pos)
ax.set_yticklabels([names[i] for i in order], fontsize=8.5)
ax.set_xlabel(r"$d_j$ (judge severity)", fontsize=10)
ax.set_xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
ax.set_xlim(-1.25, 1.05)
ax.margins(y=0.06)

from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color=PROP_COLOR, lw=2.5, label="Proprietary"),
    Line2D([0], [0], color=OPEN_COLOR, lw=2.5, label="Open-source"),
]
ax.legend(handles=legend_elements, loc="lower right", fontsize=7.5,
          framealpha=0.85, edgecolor="#CCCCCC")

fig.tight_layout(pad=0.3)
fig.savefig(f"{OUT_DIR}/forest_dj.pdf", bbox_inches="tight", dpi=300)
fig.savefig(f"{OUT_DIR}/forest_dj.png", bbox_inches="tight", dpi=300)
plt.close(fig)
print("Done: forest_dj.pdf + forest_dj.png")
