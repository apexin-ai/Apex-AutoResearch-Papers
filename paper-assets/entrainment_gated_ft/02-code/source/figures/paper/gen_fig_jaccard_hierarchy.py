import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os
from palette import BLUE, CORAL, TEAL, AMBER, GRAY, DARK, LIGHT, RCPARAMS

plt.rcParams.update(RCPARAMS)

categories = [
    'Independence\nbaseline',
    'Cross-\narchitecture',
    'Pythia 70M\nwithin-seed',
    'Within-\narchitecture',
]

means = [
    0.05,
    (0.096 + 0.091) / 2,
    (0.273 + 0.393) / 2,
    (0.348 + 0.310) / 2,
]

helped = [0.05, 0.096, 0.273, 0.348]
hurt   = [0.05, 0.091, 0.393, 0.310]

colors = [LIGHT, BLUE, AMBER, TEAL]

x = np.arange(len(categories))
width = 0.50

fig, ax = plt.subplots(figsize=(3.3, 2.2))

bars = ax.bar(x, means, width, color=colors, alpha=0.85, zorder=3,
              edgecolor='white', linewidth=0.5)

for i in range(1, len(categories)):
    ax.plot([i, i], [helped[i], hurt[i]], color=DARK,
            linewidth=0.6, zorder=4)
    ax.plot(i, helped[i], '_', color=DARK, markersize=3.5, zorder=4)
    ax.plot(i, hurt[i], '_', color=DARK, markersize=3.5, zorder=4)

for i, (bar, m) in enumerate(zip(bars, means)):
    t = ax.text(bar.get_x() + bar.get_width() / 2, m + 0.012,
                f'{m:.2f}', ha='center', va='bottom', fontsize=6.5,
                fontweight='bold', color=DARK)
    t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])

# Elegant brackets with clean lines
bracket_y1 = 0.37
ax.annotate('', xy=(0, bracket_y1 - 0.06), xytext=(0, bracket_y1 - 0.04),
            arrowprops=dict(arrowstyle='-', color='#BBBBBB', lw=0.5))
ax.plot([0, 0, 1, 1],
        [means[0] + 0.025, bracket_y1 - 0.05, bracket_y1 - 0.05, means[1] + 0.025],
        color='#BBBBBB', lw=0.5, clip_on=False, solid_capstyle='round')
ax.text(0.5, bracket_y1 - 0.045, r'2$\times$', ha='center', fontsize=6,
        color=GRAY)

bracket_y2 = 0.42
ax.plot([1, 1, 3, 3],
        [means[1] + 0.025, bracket_y2, bracket_y2, means[3] + 0.025],
        color='#BBBBBB', lw=0.5, clip_on=False, solid_capstyle='round')
ax.text(2.0, bracket_y2 + 0.005, r'3$\times$', ha='center', fontsize=6,
        color=GRAY)

ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=6)
ax.set_ylabel('Mean pairwise Jaccard $\\bar{J}$')
ax.set_ylim(0, 0.48)
ax.grid(axis='y', alpha=0.08, linewidth=0.3, zorder=0, color='#AAAAAA')

ax.text(0.98, 0.97, 'LAMBADA, 1.3B\n(Pythia: 70M)',
        transform=ax.transAxes, fontsize=5.5, fontstyle='italic',
        color=GRAY, va='top', ha='right')

out_dir = os.path.dirname(os.path.abspath(__file__))
paper_fig_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures'
os.makedirs(paper_fig_dir, exist_ok=True)

for d in [out_dir, paper_fig_dir]:
    fig.savefig(os.path.join(d, 'fig_jaccard_hierarchy.pdf'))
    fig.savefig(os.path.join(d, 'fig_jaccard_hierarchy.png'), dpi=300)
plt.close()
print('Saved fig_jaccard_hierarchy')
