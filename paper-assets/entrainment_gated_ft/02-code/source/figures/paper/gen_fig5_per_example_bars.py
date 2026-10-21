import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os
from palette import BLUE, CORAL, TEAL, AMBER, GRAY, DARK, LIGHT, RCPARAMS

plt.rcParams.update(RCPARAMS)

archs = ['GDN', 'RetNet', 'HGRN2']
helped = [462, 426, 548]
hurt = [615, 495, 395]
net = [-153, -69, 153]

x = np.arange(len(archs))
width = 0.30

fig, ax = plt.subplots(figsize=(3.3, 2.2))

bars_h = ax.bar(x - width/2, helped, width, label='Helped', color=BLUE,
                alpha=0.85, zorder=3, edgecolor='white', linewidth=0.5)
bars_u = ax.bar(x + width/2, hurt, width, label='Hurt', color=CORAL,
                alpha=0.85, zorder=3, edgecolor='white', linewidth=0.5)

for i, (h, u, n) in enumerate(zip(helped, hurt, net)):
    y_max = max(h, u) + 18
    sign = '+' if n > 0 else ''
    color = TEAL if n > 0 else CORAL
    t = ax.text(i, y_max, f'net {sign}{n}', ha='center', va='bottom',
                fontsize=6, fontweight='bold', color=color)
    t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])

ax.set_xticks(x)
ax.set_xticklabels(archs)
ax.set_ylabel('Number of examples')
ax.set_ylim(0, 700)
ax.legend(loc='upper center', frameon=False, ncol=2,
          bbox_to_anchor=(0.5, 1.0), columnspacing=1.5)

ax.grid(axis='y', alpha=0.08, linewidth=0.3, zorder=0, color='#AAAAAA')

ax.text(0.98, 0.03, 'LAMBADA, $N = 5{,}153$, 1.3B',
        transform=ax.transAxes, fontsize=5.5, fontstyle='italic',
        color=GRAY, va='bottom', ha='right')

out_dir = os.path.dirname(os.path.abspath(__file__))
paper_fig_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures'
os.makedirs(paper_fig_dir, exist_ok=True)

for d in [out_dir, paper_fig_dir]:
    fig.savefig(os.path.join(d, 'fig5_per_example_bars.pdf'))
    fig.savefig(os.path.join(d, 'fig5_per_example_bars.png'), dpi=300)
    fig.savefig(os.path.join(d, 'fig_per_example_bars.pdf'))
    fig.savefig(os.path.join(d, 'fig_per_example_bars.png'), dpi=300)
plt.close()
print('Saved fig_per_example_bars')
