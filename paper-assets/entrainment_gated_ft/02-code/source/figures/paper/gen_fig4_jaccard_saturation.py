import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os
from palette import BLUE, CORAL, TEAL, AMBER, GRAY, DARK, LIGHT, RCPARAMS

plt.rcParams.update(RCPARAMS)

ratios = [0.04, 0.077, 0.143, 0.25]
ratio_labels = ['4%', '7.7%', '14.3%', '25%']

data = {
    'LAMBADA': {
        'j_h': [0.0945, 0.0951, 0.0922, 0.1002],
        'j_u': [0.0873, 0.0809, 0.0988, 0.0928],
    },
    'HellaSwag': {
        'j_h': [0.0838, 0.0949, 0.0945, 0.0894],
        'j_u': [0.0846, 0.0668, 0.0867, 0.0833],
    },
    'ARC-Easy': {
        'j_h': [0.0748, 0.0981, 0.0935, 0.1023],
        'j_u': [0.0934, 0.0994, 0.0876, 0.1149],
    },
    'PIQA': {
        'j_h': [0.0852, 0.0862, 0.0807, 0.1122],
        'j_u': [0.0931, 0.1050, 0.0976, 0.0784],
    },
}

mean_j = {}
for bench, vals in data.items():
    mean_j[bench] = [(h + u) / 2 for h, u in zip(vals['j_h'], vals['j_u'])]

colors = {
    'LAMBADA': BLUE,
    'HellaSwag': AMBER,
    'ARC-Easy': GRAY,
    'PIQA': CORAL,
}
markers = {
    'LAMBADA': 'o',
    'HellaSwag': 's',
    'ARC-Easy': 'D',
    'PIQA': '^',
}
linestyles = {
    'LAMBADA': '-',
    'HellaSwag': '-',
    'ARC-Easy': '--',
    'PIQA': '-.',
}

fig, ax = plt.subplots(figsize=(3.3, 2.0))

# Independence baseline reference band
ax.axhspan(0.035, 0.055, color='#F5F5F5', zorder=0)
ax.axhline(y=0.05, color='#CCCCCC', linewidth=0.4, linestyle=':', zorder=1)
ax.text(0.033, 0.048, 'independence baseline', fontsize=4.5, color='#AAAAAA',
        va='top', ha='left', fontstyle='italic')

for bench in ['LAMBADA', 'HellaSwag', 'ARC-Easy', 'PIQA']:
    ax.plot(ratios, mean_j[bench], marker=markers[bench], color=colors[bench],
            linestyle=linestyles[bench],
            markersize=3.5, linewidth=0.9, zorder=3,
            markeredgecolor='white', markeredgewidth=0.3)

label_offsets = {
    'LAMBADA':  (0.007, 0.002),
    'HellaSwag': (0.007, -0.005),
    'ARC-Easy': (0.007, 0.004),
    'PIQA':     (0.007, -0.002),
}

for bench in ['LAMBADA', 'HellaSwag', 'ARC-Easy', 'PIQA']:
    last_x = ratios[-1]
    last_y = mean_j[bench][-1]
    ox, oy = label_offsets[bench]
    t = ax.text(last_x + ox, last_y + oy, bench, fontsize=5.5,
                color=colors[bench], va='center', fontweight='medium')
    t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])

ax.set_xlabel('Attention ratio')
ax.set_ylabel('Mean pairwise Jaccard $\\bar{J}$')
ax.set_xticks(ratios)
ax.set_xticklabels(ratio_labels)
ax.set_ylim(0.035, 0.125)
ax.set_xlim(0.025, 0.32)
ax.grid(axis='y', alpha=0.08, linewidth=0.3, zorder=0, color='#AAAAAA')

out_dir = os.path.dirname(os.path.abspath(__file__))
paper_fig_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures'
os.makedirs(paper_fig_dir, exist_ok=True)

for d in [out_dir, paper_fig_dir]:
    fig.savefig(os.path.join(d, 'fig4_jaccard_saturation.pdf'))
    fig.savefig(os.path.join(d, 'fig4_jaccard_saturation.png'), dpi=300)
plt.close()
print('Saved fig4_jaccard_saturation')
