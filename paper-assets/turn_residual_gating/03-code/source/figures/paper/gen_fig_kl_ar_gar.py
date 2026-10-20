"""Generate appendix figure: Per-turn AR GAR curves + mid-turn bar chart."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

turns = np.arange(1, 6)
data = {
    'Base':      ([0.0853, 0.0319, 0.0206, 0.0125, 0.0042], C_BASE, 's', '--'),
    'LoRA-only': ([0.1072, 0.0586, 0.0304, 0.0489, 0.0397], C_LO, 'D', '-'),
    'PCGrad':    ([0.0903, 0.0382, 0.0276, 0.0292, 0.0267], C_PC,  '^', '-'),
    'UG':        ([0.1130, 0.0564, 0.0328, 0.0198, 0.0160], C_UG,   'v', '-'),
    'TG':        ([0.1297, 0.0725, 0.0591, 0.0428, 0.0664], C_TG,   'o', '-'),
    'SS':        ([0.5264, 0.4494, 0.4380, 0.3996, 0.3909], C_SS,   'P', '-'),
}

bar_data = {
    'Base':      0.0186,
    'LoRA-only': 0.0373,
    'PCGrad':    0.0301,
    'UG':        0.0333,
    'TG':        0.0641,
    'SS':        0.4231,
}

# Plot 1: Per-turn AR GAR curves
fig, ax = plt.subplots(figsize=(4.0, 2.8))

for name, (vals, col, mk, ls) in data.items():
    ax.plot(turns, vals, linestyle=ls, marker=mk, color=col,
            markersize=5, markerfacecolor=col, markeredgecolor='white',
            markeredgewidth=0.6, label=name, zorder=3)

ax.set_xlabel('Turn')
ax.set_ylabel('AR Goal Attention Ratio (GAR)')
ax.set_xticks(turns)
ax.set_xlim(0.6, 5.4)
ax.set_ylim(-0.01, 0.58)
ax.legend(loc='center right',
          handletextpad=0.4, borderpad=0.4, ncol=1, columnspacing=1.0, fontsize=6.5)
ax.grid(axis='y', alpha=0.2, linewidth=0.5)

fig.tight_layout()
save_fig(fig, 'fig_kl_ar_gar_curves')

# Plot 2: Mid-turn AR GAR bar chart
fig, ax = plt.subplots(figsize=(4.0, 2.4))

names = list(bar_data.keys())
vals = [bar_data[n] for n in names]
bar_colors = [data[n][1] if n in data else C_BASE for n in names]

bars = ax.bar(names, vals, color=bar_colors, edgecolor='white', linewidth=0.6,
              width=0.6, zorder=3)

for bar, v in zip(bars, vals):
    ax.text(bar.get_x() + bar.get_width()/2, v + 0.008,
            f'{v:.3f}', ha='center', va='bottom', fontsize=7, color='#444444')

ax.set_ylabel('Mid-turn AR GAR')
ax.set_ylim(0, 0.50)
ax.grid(axis='y', alpha=0.2, linewidth=0.5)

fig.tight_layout()
save_fig(fig, 'fig_kl_ar_gar_bar')
