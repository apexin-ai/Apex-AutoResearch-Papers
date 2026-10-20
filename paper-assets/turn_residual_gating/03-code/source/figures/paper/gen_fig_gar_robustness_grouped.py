import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

strategies = ['Last\n(ours)', 'All\ntokens', 'First\ntoken', 'Goal-\nonly']
conditions = ['Base', 'TG', 'SS']
cond_colors = [C_BASE, C_TG, C_SS]

mid_turn_gar = {
    'Base': [0.0152, 0.0152, 0.0224, 0.0049],
    'TG':   [0.3254, 0.0253, 0.0392, 0.3103],
    'SS':   [0.4582, 0.3658, 0.4118, 0.4435],
}

turn1_gar = {
    'Base': [0.0858, 0.1152, 0.2987, 0.0110],
    'TG':   [0.3938, 0.1275, 0.3225, 0.3313],
    'SS':   [0.5274, 0.5043, 0.7549, 0.4528],
}

x = np.arange(len(strategies))
width = 0.22

fig, axes = plt.subplots(2, 1, figsize=(3.5, 4.5), sharey=False)

for ax, data, title in [(axes[0], mid_turn_gar, 'Mid-turn GAR'),
                         (axes[1], turn1_gar, 'Turn-1 GAR')]:
    for i, (cond, color) in enumerate(zip(conditions, cond_colors)):
        offset = (i - 1) * width
        bars = ax.bar(x + offset, data[cond], width, label=cond, color=color,
                      edgecolor='white', linewidth=0.3, alpha=0.85)
    ax.set_xticks(x)
    ax.set_xticklabels(strategies, fontsize=7)
    ax.set_title(title, fontsize=9, fontweight='bold')
    ax.set_ylabel('GAR')

axes[0].legend(frameon=False, ncol=3, loc='upper center', fontsize=7,
               bbox_to_anchor=(0.5, 1.02))

fig.tight_layout(h_pad=2.0)
save_fig(fig, 'fig_gar_robustness_grouped')
