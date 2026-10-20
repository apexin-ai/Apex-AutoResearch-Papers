import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import FancyArrowPatch

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.01,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# --- Data (do not modify values) ---
data = [
    (r'$\pi$0.5',  'Object',  24.2, 0.055),
    (r'$\pi$0.5',  'Spatial', 21.4, 0.055),
    ('X-VLA',       'Object',   0.2, 0.151),
    ('X-VLA',       'Spatial',  1.4, 0.151),
    ('X-VLA',       'Goal',     0.2, 0.151),
]

# Academic muted palette
C_PI = '#c44e52'
C_XV = '#4c72b0'

rows = [
    (r'$\pi$0.5',  'Object',  24.2, C_PI),
    (r'$\pi$0.5',  'Spatial', 21.4, C_PI),
    ('X-VLA',       'Spatial',  1.4, C_XV),
    ('X-VLA',       'Object',   0.2, C_XV),
    ('X-VLA',       'Goal',     0.2, C_XV),
]

ypos = [4.2, 3.2, 1.6, 0.8, 0.0]

fig, ax = plt.subplots(figsize=(3.5, 2.1))

for (model, suite, val, color), yi in zip(rows, ypos):
    ax.hlines(yi, 0, val, color=color, linewidth=1.5, zorder=2)
    ax.plot(val, yi, 'o', color=color, markersize=6,
            markeredgecolor='white', markeredgewidth=0.6, zorder=3)
    ax.text(val + 0.5, yi, f'{val:.1f}', ha='left', va='center',
            fontsize=8, color='#444444')

sep_y = (ypos[1] + ypos[2]) / 2
ax.axhline(sep_y, color='#dddddd', linewidth=0.5, zorder=0)

ax.set_yticks(ypos)
ax.set_yticklabels([f'{m} · {s}' for m, s, _, _ in rows])
ax.tick_params(axis='y', length=0, pad=3)
for i, (_, _, _, c) in enumerate(rows):
    ax.get_yticklabels()[i].set_color(c)

ax.spines['left'].set_visible(False)

# 17x bracket with refined thin arrows
by = ypos[0] + 0.55
ax.annotate('', xy=(24.2, by), xytext=(1.4, by),
            arrowprops=dict(arrowstyle='<|-|>', color='#888888', lw=0.6,
                            mutation_scale=6))
ax.text((24.2 + 1.4) / 2, by + 0.08, r'17$\times$',
        ha='center', va='bottom', fontsize=9, fontweight='bold', color=C_PI)

ax.set_xlabel('Method gap |SR(L2) − SR(Random)| (pp)')
ax.set_xlim(-0.3, 27.5)
ax.set_ylim(-0.5, by + 0.75)
ax.grid(axis='x', alpha=0.12, zorder=0)

plt.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper'
artdir = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/_project/chart'
os.makedirs(outdir, exist_ok=True)
os.makedirs(artdir, exist_ok=True)
for d in [outdir, artdir]:
    plt.savefig(f'{d}/fig_method_gap.pdf')
    plt.savefig(f'{d}/fig_method_gap.png')
plt.close()
print('Done')
