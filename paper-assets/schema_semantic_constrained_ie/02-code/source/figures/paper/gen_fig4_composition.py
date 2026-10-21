import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

C_VERY_LIGHT = '#BAD4F0'
C_LIGHT      = '#8BAED4'
C_MEDIUM     = '#5B7FAD'
C_DEEP       = '#2B4C7E'
C_TEXT        = '#333333'

modes = ['Unconstr.', 'Grammar\nonly', 'Semantic\nonly', 'S1\n(both)']
dr_reduction = [0, 3, 24, 94]
colors = [C_VERY_LIGHT, C_LIGHT, C_MEDIUM, C_DEEP]

fig, ax = plt.subplots(figsize=(3.5, 2.8))

bars = ax.bar(range(4), dr_reduction, width=0.6, color=colors,
              edgecolor='white', linewidth=0.8)

additive_pred = 3 + 24
ax.axhline(y=additive_pred, color='#D4A574', linestyle='--', linewidth=1.2,
           zorder=0, label=f'Additive prediction ({additive_pred}%)')
ax.text(-0.35, additive_pred + 1.5, f'{additive_pred}%', color='#D4A574',
        fontsize=8, ha='left', va='bottom')

label_offsets = {0: 4, 1: 6, 2: 3, 3: 2}
for i, v in enumerate(dr_reduction):
    if v > 0:
        ax.text(i, v + label_offsets[i], f'{v}%', ha='center', va='bottom',
                fontsize=10, fontweight='bold', color=C_TEXT)

ax.annotate('', xy=(3, 91), xytext=(3, additive_pred + 5),
            arrowprops=dict(arrowstyle='<->', color='#888888', lw=1.0))
ax.text(3.35, (91 + additive_pred + 5) / 2, '3.5×',
        fontsize=8, color='#555555', ha='left', va='center')

ax.set_xticks(range(4))
ax.set_xticklabels(modes, fontsize=8.5)
ax.set_ylabel('DR Reduction (%)')
ax.set_ylim(0, 110)
ax.legend(fontsize=7.5, loc='upper left', framealpha=0.9, edgecolor='#E0E0E0')

plt.tight_layout()

out_path = '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/figures/fig_composition_interaction'
fig.savefig(out_path + '.pdf')
fig.savefig(out_path + '.png')
plt.close()
print('Done')
