"""Figure D (Appendix): Instruction Retention — β=0 vs β=3 by category."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

categories = ['Content', 'Count', 'Position', 'Format', 'Overall']
beta0 = [62.5, 78.9, 84.2, 76.9, 75.9]
beta3 = [86.3, 89.5, 89.5, 76.9, 87.0]
deltas = [b3 - b0 for b0, b3 in zip(beta0, beta3)]

fig, ax = plt.subplots(figsize=(5.0, 2.8))

x = np.arange(len(categories))
w = 0.30

c_b0 = C_PURPLE
c_b3 = C_TEAL

bars0 = ax.bar(x - w/2, beta0, w, color=c_b0, alpha=0.65,
               edgecolor='white', linewidth=0.4, label=r'$\beta=0$', zorder=2)
bars3 = ax.bar(x + w/2, beta3, w, color=c_b3, alpha=0.85,
               edgecolor='white', linewidth=0.4, label=r'$\beta=3$', zorder=2)

for i, d in enumerate(deltas):
    if abs(d) > 0.1:
        sign = '+' if d > 0 else ''
        ax.text(x[i] + w/2, beta3[i] + 1.0, f'{sign}{d:.1f}pp',
                ha='center', va='bottom', fontsize=6.5, color='#555555',
                fontweight='bold')
    else:
        ax.text(x[i] + w/2, beta3[i] + 1.0, '—',
                ha='center', va='bottom', fontsize=6.5, color='#AAAAAA')

ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=8)
ax.set_ylabel('Instruction Following Rate (%)', fontsize=9)
ax.set_ylim(50, 100)
ax.set_xlim(-0.6, len(categories) - 0.4)

ax.legend(loc='upper left',
          handletextpad=0.4, borderpad=0.35, fontsize=7)

save_fig(fig, 'fig_instruction_retention')
