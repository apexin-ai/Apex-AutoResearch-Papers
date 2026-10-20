"""Generate appendix Figure 9: Gate value distributions (violin plots)."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

tg_gates = np.array([
    .883, .793, .996, .988, .984, .797, .961, .918,
    .965, .934, .969, .918, .926, .941, .930, .965,
    .941, .910, .961, .965, .973, .988, .969, .980,
    .980, .984, .988, 1.00
])

ug_gates = np.array([
    .875, .918, .953, .777, .961, .812, .949, .934,
    .957, .945, .961, .949, .953, .957, .953, .965,
    .957, .949, .969, .969, .977, .984, .973, .984,
    .988, .988, .992, 1.00
])

pcgrad_gates = np.array([
    .891, .813, .988, .980, .977, .816, .953, .926,
    .957, .941, .965, .930, .934, .945, .938, .961,
    .945, .918, .957, .961, .969, .984, .965, .977,
    .977, .980, .984, .996
])

fig, ax = plt.subplots(figsize=(3.5, 2.8))

data = [tg_gates, ug_gates, pcgrad_gates]
colors = [C_TG, C_UG, C_PC]
labels = ['TG', 'UG', 'TG+PCGrad']

parts = ax.violinplot(data, positions=[1, 2, 3], showmeans=True,
                       showmedians=False, showextrema=False)

for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_alpha(0.7)
    pc.set_edgecolor('white')
    pc.set_linewidth(0.5)

parts['cmeans'].set_color('#333333')
parts['cmeans'].set_linewidth(1.2)

for i, d in enumerate(data):
    ax.scatter(np.full_like(d, i + 1) + np.random.uniform(-0.08, 0.08, len(d)),
               d, s=12, color=colors[i], alpha=0.6, edgecolors='white',
               linewidths=0.3, zorder=3)

for i, d in enumerate(data):
    ax.text(i + 1, 0.73, f'μ={d.mean():.3f}\nσ={d.std():.3f}',
            ha='center', va='top', fontsize=7, color='#555555')

ax.set_xticks([1, 2, 3])
ax.set_xticklabels(labels)
ax.set_ylabel('Gate value $g$')
ax.set_ylim(0.68, 1.03)
ax.axhline(1.0, color='#cccccc', linestyle=':', linewidth=0.8, zorder=1)
ax.set_title('Gate Value Distribution (Qwen, 28L)',
             fontsize=8, fontweight='bold', pad=6)
ax.grid(axis='y', alpha=0.15, zorder=0)

plt.tight_layout()
save_fig(fig, 'fig_gate_distribution')
