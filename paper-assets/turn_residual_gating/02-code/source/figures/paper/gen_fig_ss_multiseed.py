"""Figure B: Multi-seed Confidence — SS AR GAR at β=0 and β=5."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np
import matplotlib.patheffects as pe

apply_style()

betas = [r'$\beta=0$', r'$\beta=5$']
seeds_b0 = [0.347, 0.423, 0.433]
seeds_b5 = [0.716, 0.717, 0.718]
all_seeds = [seeds_b0, seeds_b5]
means = [np.mean(s) for s in all_seeds]
stds = [np.std(s) for s in all_seeds]

C_COLD = '#7BA7C2'
C_WARM = C_SS
bar_colors = [C_COLD, C_WARM]
edge_colors = ['#5A8CA6', '#9E5E3E']

fig, ax = plt.subplots(figsize=(3.2, 2.8))

x = np.arange(len(betas))
bar_width = 0.45

for i in range(len(betas)):
    ax.bar(x[i], means[i], bar_width,
           color=bar_colors[i], edgecolor=edge_colors[i], linewidth=0.6,
           zorder=2, alpha=0.85)

    ax.errorbar(x[i], means[i], yerr=stds[i], fmt='none', capsize=4,
                ecolor='#666666', elinewidth=0.9, capthick=0.7, zorder=3)

    jitter = np.linspace(-0.06, 0.06, len(all_seeds[i]))
    dc = '#5A8CA6' if i == 0 else '#9E5E3E'
    ec = '#4A7A92' if i == 0 else '#8A4E30'
    ax.scatter(x[i] + jitter, all_seeds[i], s=22,
               color=dc, edgecolor=ec, linewidth=0.6, zorder=4)

    txt = ax.text(x[i], means[i] + stds[i] + 0.030,
                  f'{means[i]:.3f}±{stds[i]:.3f}',
                  ha='center', va='bottom', fontsize=7.5, color='#444444')
    txt.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

# Subtle horizontal grid
ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
ax.set_axisbelow(True)
ax.grid(axis='y', alpha=0.12, linewidth=0.4, color='#888888')

ax.set_xticks(x)
ax.set_xticklabels(betas, fontsize=9)
ax.set_ylabel('AR GAR', fontsize=9)
ax.set_ylim(0, 0.85)
ax.set_xlim(-0.5, 1.5)

save_fig(fig, 'fig_ss_multiseed')
