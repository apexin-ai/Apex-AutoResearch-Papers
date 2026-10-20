import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

out_dir = "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/figures"

C = {
    'baseline':  '#4A90D9',   # steel blue — Adaptive b* / primary data / ours
    'treatment': '#E8913A',   # warm amber — ESS-only / contrast methods
    'collapse':  '#C75C5C',   # muted coral — Random / degradation / failure
    'safe':      '#43A888',   # sage green — Grid-best / Oracle / D&R / good outcome
    'neutral':   '#90A4AE',   # blue-gray — Uniform baseline / reference
}

# Data
tau =     [0.5,    0.6,    0.7,    0.8,    0.9,    0.95]
ppl =     [17.688, 17.681, 17.679, 17.653, 17.712, 17.723]
uniform_baseline = 17.694
grid_best = 17.651

# ── Premium rcParams (publication-grade, PaperBanana-equivalent) ──
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'dejavuserif',
    'font.size': 9,
    'axes.titlesize': 9.5,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'axes.linewidth': 0.8,
    'axes.edgecolor': 'black',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.axisbelow': True,
    'xtick.major.width': 0.5,  'ytick.major.width': 0.5,
    'xtick.minor.width': 0.3,  'ytick.minor.width': 0.3,
    'xtick.major.size': 3.5,   'ytick.major.size': 3.5,
    'xtick.minor.size': 2.0,   'ytick.minor.size': 2.0,
    'xtick.direction': 'out',  'ytick.direction': 'out',
    'xtick.major.pad': 4,      'ytick.major.pad': 4,
    'lines.linewidth': 1.5,
    'lines.markersize': 5,
    'legend.frameon': False,
    'legend.borderpad': 0.3,
    'legend.handlelength': 1.5,
    'legend.handletextpad': 0.5,
    'grid.linewidth': 0.5,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'grid.color': '#CCCCCC',
    'figure.dpi': 300,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'savefig.facecolor': 'white',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

fig, ax = plt.subplots(figsize=(3.5, 2.5))

# Safe range shading [0.5, 0.8]
ax.axvspan(0.5, 0.8, alpha=0.10, color=C['safe'], zorder=0)
ax.text(0.65, 17.730, 'safe range', ha='center', va='top',
        fontsize=6.5, color=C['safe'], fontstyle='italic')

# Reference lines
ax.axhline(y=uniform_baseline, color=C['neutral'], linestyle='--', linewidth=0.8, zorder=1)
ax.text(0.96, uniform_baseline + 0.001, f'Uniform = {uniform_baseline}',
        ha='right', va='bottom', fontsize=6.5, color=C['neutral'])

ax.axhline(y=grid_best, color=C['safe'], linestyle='--', linewidth=0.8, zorder=1)
ax.text(0.51, grid_best - 0.001, f'Grid-best = {grid_best}',
        ha='left', va='top', fontsize=6.5, color=C['safe'])

# Main curve (Adaptive)
ax.plot(tau, ppl, 'o-', color=C['baseline'], markerfacecolor=C['baseline'],
        markeredgecolor='white', markeredgewidth=0.6, zorder=3)

# Highlight optimal τ=0.8
best_idx = 3  # τ=0.8
ax.plot(tau[best_idx], ppl[best_idx], '*', color=C['safe'], markersize=12,
        markeredgecolor='white', markeredgewidth=0.4, zorder=4)
ax.annotate(f'τ*=0.8 (PPL={ppl[best_idx]:.3f})',
            xy=(tau[best_idx], ppl[best_idx]),
            xytext=(tau[best_idx] - 0.22, ppl[best_idx] + 0.012),
            fontsize=6.5, color=C['safe'], fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=C['safe'], lw=0.8,
                            connectionstyle='arc3,rad=-0.2'),
            ha='left', va='bottom')

# Axes
ax.set_xlabel(r'Temperature threshold $\tau$')
ax.set_ylabel('Held-out PPL')
ax.set_xlim(0.45, 0.99)
ax.set_ylim(17.638, 17.735)
ax.set_xticks(tau)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.02))

ax.grid(axis='y', lw=0.5, alpha=0.3, color='#CCCCCC', linestyle='--')

plt.tight_layout(pad=0.4)

fig.savefig(f'{out_dir}/tau_sweep_rho04.pdf', dpi=300, bbox_inches='tight')
fig.savefig(f'{out_dir}/tau_sweep_rho04.png', dpi=300, bbox_inches='tight')
print('Saved PDF and PNG.')
