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
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
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

COL_BENEFIT = '#E8A838'
COL_COST = '#E8A838'

models = ['Qwen3\n1.7B', 'Qwen3\n4B', 'Qwen3\n8B', 'LLaMA\n3.1-8B', 'Qwen3\n14B']
tax_values = [-5.01, 1.65, -0.91, -1.46, 0.12]
tax_errors = [0.59, 0.29, 0.74, 0.40, 0.64]

colors = [COL_BENEFIT if v < 0 else COL_COST for v in tax_values]
edge_colors = ['#BA862D' for v in tax_values]

fig, ax = plt.subplots(figsize=(5.8, 3.2), dpi=300)

ax.axhspan(-8, 0, color='#F5FAFE', alpha=0.5, zorder=0)
ax.axhspan(0, 5, color='#FFFAF0', alpha=0.5, zorder=0)

ax.text(4.7, -3.8, 'evidence\nbenefits', fontsize=7, color='#4A8BBF', alpha=0.8,
        ha='center', va='center', fontstyle='italic', linespacing=0.9)
ax.text(4.7, 2.5, 'evidence\ncosts', fontsize=7, color='#B8862D', alpha=0.8,
        ha='center', va='center', fontstyle='italic', linespacing=0.9)

x = np.arange(len(models))
bars = ax.bar(x, tax_values, width=0.55, color=colors, edgecolor=edge_colors,
              linewidth=0.5, zorder=3, alpha=0.88)

for i, (val, err) in enumerate(zip(tax_values, tax_errors)):
    ax.errorbar(i, val, yerr=err, fmt='none', ecolor='black', capsize=3.5,
                capthick=0.8, linewidth=0.8, zorder=4, alpha=0.7)

ax.axhline(y=0, color='#666666', linestyle='-', linewidth=0.6, alpha=0.6, zorder=2)

for i, (val, err) in enumerate(zip(tax_values, tax_errors)):
    sign = '+' if val > 0 else ''
    label = f'{sign}{val:.2f}pp'
    if val >= 0:
        y_pos = val + err + 0.2
        va = 'bottom'
    else:
        y_pos = val - err - 0.2
        va = 'top'
    t = ax.text(i, y_pos, label, ha='center', va=va, fontsize=8, fontweight='bold',
                color='#333333')
    t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=9)
ax.set_ylabel('Evidence Tax (pp)', fontsize=11)
ax.set_ylim(-7.0, 3.8)
ax.grid(axis='y', alpha=0.12, color='#999999', linestyle='-', linewidth=0.3, zorder=1)

from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=COL_BENEFIT, edgecolor='#BA862D', linewidth=0.5,
          alpha=0.88, label='Evidence helps (negative tax)'),
    Patch(facecolor=COL_COST, edgecolor='#BA862D', linewidth=0.5,
          alpha=0.88, label='Evidence hurts (positive tax)'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=7.5,
          framealpha=0.95, edgecolor='#e0e0e0', borderpad=0.5)

fig.tight_layout()
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper'
fig.savefig(f'{out_dir}/fig_evidence_tax.pdf', bbox_inches='tight', dpi=300)
fig.savefig(f'{out_dir}/fig_evidence_tax.png', bbox_inches='tight', dpi=300)
print('Done. fig_evidence_tax PDF and PNG saved.')
