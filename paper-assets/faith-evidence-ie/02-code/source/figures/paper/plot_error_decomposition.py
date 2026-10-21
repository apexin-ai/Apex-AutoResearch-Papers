import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 10,
    'axes.labelsize': 11,
    'xtick.labelsize': 9.5,
    'ytick.labelsize': 9.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

COL_1_7B = '#5B9BD5'
COL_4B   = '#E8A838'
COL_8B   = '#009E73'
COL_1_7B_E = '#497CAA'
COL_4B_E   = '#BA862D'
COL_8B_E   = '#1A7A5A'

categories = ['Truncation FN', 'Hallucinated FP', 'Duplicates', 'FN: other']
scale_1_7B = [-22, -8, -20, +13]
scale_4B = [-16, -6, -11, +15]
scale_8B = [-18, -12, -14, +14]

x = np.arange(len(categories))
width = 0.23
gap = 0.02

fig, ax = plt.subplots(figsize=(6, 3.5))

bars1 = ax.bar(x - width - gap, scale_1_7B, width, label='1.7B',
               color=COL_1_7B, edgecolor=COL_1_7B_E, linewidth=0.4, zorder=3, alpha=0.88)
bars2 = ax.bar(x, scale_4B, width, label='4B',
               color=COL_4B, edgecolor=COL_4B_E, linewidth=0.4, zorder=3, alpha=0.88)
bars3 = ax.bar(x + width + gap, scale_8B, width, label='8B+LLaMA',
               color=COL_8B, edgecolor=COL_8B_E, linewidth=0.4, zorder=3, alpha=0.88)

for bars in [bars1, bars2, bars3]:
    for bar in bars:
        h = bar.get_height()
        if h < 0:
            y_pos = h - 0.6
            va = 'top'
        else:
            y_pos = h + 0.5
            va = 'bottom'
        t = ax.text(bar.get_x() + bar.get_width()/2, y_pos, f'{h:+d}',
                    ha='center', va=va, fontsize=7.5, fontweight='bold', color='#333333')
        t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])

ax.axhline(y=0, color='#666666', linestyle='-', linewidth=0.6, alpha=0.6, zorder=2)
ax.set_ylabel('Relative Change (%)')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.grid(axis='y', alpha=0.12, color='#999999', linestyle='-', linewidth=0.3, zorder=0)

from matplotlib.patches import Patch
handles = [
    Patch(facecolor=COL_1_7B, edgecolor=COL_1_7B_E, linewidth=0.4, alpha=0.88, label='1.7B'),
    Patch(facecolor=COL_4B,   edgecolor=COL_4B_E,   linewidth=0.4, alpha=0.88, label='4B'),
    Patch(facecolor=COL_8B,   edgecolor=COL_8B_E,   linewidth=0.4, alpha=0.88, label='8B+LLaMA'),
]
ax.legend(handles=handles, loc='upper left', fontsize=8, framealpha=0.95,
          edgecolor='#e0e0e0', borderpad=0.5, frameon=True)

fig.tight_layout()
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper'
fig.savefig(f'{out_dir}/fig_error_decomposition.pdf', bbox_inches='tight', dpi=300)
fig.savefig(f'{out_dir}/fig_error_decomposition.png', bbox_inches='tight', dpi=300)
plt.close()
print('Done: fig_error_decomposition.pdf/png')
