"""Generate fig6_cn_profile.pdf: Two-panel contamination profile figure.
Panel (a): Contamination susceptibility bar chart
Panel (b): Bias absorption scatter plot
"""
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

# exp-019 / exp-003b data
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

names = [d[0] for d in data]
cn    = np.array([d[1] for d in data])
cn_lo = np.array([d[2] for d in data])
cn_hi = np.array([d[3] for d in data])
dtheta = np.array([d[4] for d in data])

order = np.argsort(cn)[::-1]

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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.6, 3.2))

# === Panel (a): Contamination bars ===
y_pos = np.arange(len(names))
colors = ["#D55E00" if cn[i] > 1.5 else "#0072B2" for i in order]

for rank, idx in enumerate(order):
    ax1.barh(rank, cn[idx], color=colors[rank], alpha=0.8, height=0.6, zorder=3)
    ax1.plot([cn_lo[idx], cn_hi[idx]], [rank, rank],
             color="#333333", lw=1.2, solid_capstyle="round", zorder=4)

ax1.set_yticks(y_pos)
ax1.set_yticklabels([DISPLAY[names[i]] for i in order], fontsize=9)
ax1.set_xlabel(r"$\hat{c}_n$ (posterior mean $\pm$ 95% CI)", fontsize=10)
ax1.set_title("(a) Contamination susceptibility", fontsize=10.5, fontweight="bold", pad=8)
ax1.set_xlim(-0.3, 7.5)
ax1.grid(axis="x", alpha=0.2, lw=0.5)
ax1.margins(y=0.06)

# === Panel (b): Bias absorption scatter ===
rho, _ = stats.spearmanr(cn, dtheta)

ax2.scatter(cn, dtheta, c="#2C3E50", s=45, zorder=5, edgecolors="white", linewidth=0.5)

slope, intercept, _, _, _ = stats.linregress(cn, dtheta)
x_fit = np.linspace(-0.2, 6.5, 100)
ax2.plot(x_fit, slope * x_fit + intercept, "--", color="#999999", lw=1.0, zorder=2)
ax2.axhline(0, color="#CCCCCC", lw=0.7, zorder=1)

# Annotations: alternate left/right to avoid overlap
label_offsets = {
    "gpt-3.5-turbo-0125": (-1.5, 0.05),
    "gpt-4-0613":         (-1.2, 0.05),
    "qwen2.5-72b":        (-0.7, 0.08),
    "llama-3.3-70b":      (0.30, 0.08),
    "gemma-2-9b":         (0.30, 0.07),
    "qwen3-8b":           (-0.6, 0.14),
    "gpt-4o-mini":        (0.30, 0.12),
    "gpt-4o":             (0.30, -0.10),
}
for i, name in enumerate(names):
    dx, dy = label_offsets.get(name, (0.15, 0.0))
    ha = "right" if dx < 0 else "left"
    use_arrow = abs(dx) > 0.4 or abs(dy) > 0.08
    ax2.annotate(DISPLAY[name], (cn[i], dtheta[i]),
                 xytext=(cn[i]+dx, dtheta[i]+dy),
                 fontsize=7.5, color="#333333", ha=ha, va="center",
                 arrowprops=dict(arrowstyle="-", color="#AAAAAA", lw=0.4)
                 if use_arrow else None)

ax2.text(0.95, 0.08, f"Spearman $\\rho$ = {rho:.1f}",
         transform=ax2.transAxes, fontsize=9, ha="right",
         bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#CCCCCC",
                   alpha=0.9, lw=0.5))

ax2.set_xlabel(r"$\hat{c}_n$", fontsize=10)
ax2.set_ylabel(r"$\Delta\theta$ (MFRM $-$ G-MFRM)", fontsize=10)
ax2.set_title("(b) Bias absorption in MFRM", fontsize=10.5, fontweight="bold", pad=8)
ax2.set_xlim(-0.5, 7.0)
ax2.set_ylim(-0.65, 1.05)
ax2.grid(alpha=0.15, lw=0.5)

fig.tight_layout(w_pad=2.5)
fig.savefig(f"{OUT_DIR}/fig6_cn_profile.pdf", bbox_inches="tight", dpi=300)
fig.savefig(f"{OUT_DIR}/fig6_cn_profile.png", bbox_inches="tight", dpi=300)
plt.close(fig)
print("Done: fig6_cn_profile.pdf")
