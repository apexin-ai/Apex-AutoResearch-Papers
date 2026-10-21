#!/usr/bin/env python3
"""Item 10: 4-panel per-turn GAR bar charts for β=0/3/5/10."""
import sys, json
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

with open('/tmp/training_data.json') as f:
    all_data = json.load(f)

steering = all_data['steering']

betas = ['beta_0.0', 'beta_3.0', 'beta_5.0', 'beta_10.0']
beta_labels = [r'$\beta = 0$', r'$\beta = 3$', r'$\beta = 5$', r'$\beta = 10$']
turn_labels = ['Turn 1', 'Turn 2']

beta0_gar = steering['beta_0.0']['avg_gar_per_turn']

fig, axes = plt.subplots(4, 1, figsize=(3.5, 5.5))
axes_flat = axes.flatten()

bar_colors = [C_TF, C_AR]

for idx, (bkey, blabel) in enumerate(zip(betas, beta_labels)):
    ax = axes_flat[idx]
    d = steering[bkey]
    gar_values = d['avg_gar_per_turn']
    ppl = d['avg_ppl']

    x = np.arange(len(gar_values))
    bars = ax.bar(x, gar_values, width=0.45, color=bar_colors[:len(gar_values)],
                  edgecolor='white', linewidth=0.5, alpha=0.85)

    for i, ref in enumerate(beta0_gar):
        if bkey != 'beta_0.0':
            ax.plot([x[i] - 0.25, x[i] + 0.25], [ref, ref],
                    color=C_GRAY, linewidth=0.6, linestyle='--', alpha=0.5)

    for bar, val in zip(bars, gar_values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                f'{val:.2f}', ha='center', va='bottom', fontsize=7)

    ax.set_xticks(x)
    ax.set_xticklabels(turn_labels, fontsize=8)
    ax.set_ylabel('GAR', fontsize=8)
    ax.set_ylim(0, 1.15)
    ax.tick_params(axis='y', labelsize=7)

    ppl_str = f'{ppl:.1f}' if ppl < 100 else f'{ppl:.0f}'
    ax.set_title(f'{blabel}  (PPL {ppl_str})', fontsize=9, fontweight='bold')

from matplotlib.lines import Line2D
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=C_TF, alpha=0.85, edgecolor='white', label='Turn 1'),
    Patch(facecolor=C_AR, alpha=0.85, edgecolor='white', label='Turn 2'),
    Line2D([0], [0], color=C_GRAY, linewidth=0.6, linestyle='--', alpha=0.5,
           label=r'$\beta\!=\!0$ ref.'),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=3, fontsize=7,
           frameon=False, bbox_to_anchor=(0.5, -0.02))

fig.tight_layout(rect=[0, 0.02, 1, 1], h_pad=1.5)
save_fig(fig, 'fig_steering_perturn_4panel')
print("Done: fig_steering_perturn_4panel")
