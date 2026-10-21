"""Generate Figure 4: Bias vs Confounding Level (optimized for EMNLP).

Data extracted from exp-012 synthetic validation (N=50, I=100, J=8, 50 seeds).
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

OUT_DIR = "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper"

COLORS = {
    'baseline': '#0072B2',
    'treatment': '#E69F00',
    'collapse': '#D55E00',
    'safe': '#009E73',
    'neutral': '#999999',
}

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Times'],
    'mathtext.fontset': 'cm',
    'font.size': 10,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.5,
})

rho = np.array([0.0, 0.3, 0.6, 0.9])

seq_mean = np.array([0.200, 0.197, 0.192, 0.187])
seq_std = np.array([0.015, 0.012, 0.012, 0.015])

gmfrm_mean = np.array([0.058, 0.057, 0.059, 0.066])
gmfrm_std = np.array([0.008, 0.008, 0.007, 0.010])

fig, ax = plt.subplots(figsize=(3.3, 2.8))

# Fill between to show the gap
ax.fill_between(rho, seq_mean, gmfrm_mean, alpha=0.06, color='#555555', zorder=1)

# Sequential line
ax.errorbar(rho, seq_mean, yerr=seq_std, fmt='o-', color=COLORS['baseline'],
            markersize=5, linewidth=1.5, capsize=3.5, capthick=1.0,
            markeredgecolor='white', markeredgewidth=0.8,
            label='Sequential', zorder=5)

# G-MFRM line
ax.errorbar(rho, gmfrm_mean, yerr=gmfrm_std, fmt='s-', color=COLORS['treatment'],
            markersize=5, linewidth=1.5, capsize=3.5, capthick=1.0,
            markeredgecolor='white', markeredgewidth=0.8,
            label='Joint G-MFRM', zorder=5)

# Zero reference
ax.axhline(0, color=COLORS['neutral'], linestyle='--', linewidth=0.5, alpha=0.4, zorder=0)

# Narrative annotation: bias reduction
mid_y = (seq_mean.mean() + gmfrm_mean.mean()) / 2
reduction = (1 - gmfrm_mean.mean() / seq_mean.mean()) * 100
t = ax.annotate(f'~{reduction:.0f}% bias\nreduction',
                xy=(0.45, mid_y), fontsize=7, color='#555555',
                style='italic', ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                          edgecolor='#CCCCCC', alpha=0.85, linewidth=0.4))

ax.set_xlabel(r'Confounding correlation $\rho$', fontsize=9.5)
ax.set_ylabel('Bias slope', fontsize=9.5)
ax.set_xlim(-0.05, 0.95)
ax.set_ylim(-0.01, 0.28)
ax.set_xticks(rho)

ax.legend(fontsize=8, loc='upper right', framealpha=0.85,
          edgecolor='#DDDDDD', borderpad=0.4, handlelength=1.8)

# Minimal grid
ax.grid(True, alpha=0.12, axis='y', zorder=0)

fig.tight_layout(pad=0.3)
fig.savefig(f"{OUT_DIR}/fig4_bias_vs_rho.pdf", bbox_inches="tight", dpi=300)
fig.savefig(f"{OUT_DIR}/fig4_bias_vs_rho.png", bbox_inches="tight", dpi=300)
plt.close(fig)
print("Saved fig4_bias_vs_rho")
