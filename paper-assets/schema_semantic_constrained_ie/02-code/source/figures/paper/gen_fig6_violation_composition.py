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

C_DR = '#2B4C7E'
C_CF = '#8BAED4'
C_TEXT = '#333333'

modes = ['Unconstr.', 'Grammar', 'Semantic', 'S1\n(both)']
dr = [15.37, 14.84, 11.65, 0.93]
cf = [0.08, 0.08, 2.71, 9.90]

x = np.arange(len(modes))
w = 0.32

fig, ax = plt.subplots(figsize=(3.5, 2.8))

bars_dr = ax.bar(x - w/2, dr, w, color=C_DR, edgecolor='white', linewidth=0.6,
                 label='DR (irrecoverable)')
bars_cf = ax.bar(x + w/2, cf, w, color=C_CF, edgecolor='white', linewidth=0.6,
                 label='CF (correctable)')

for i, v in enumerate(dr):
    offset = 0.8 if v > 2 else 1.5
    ax.text(x[i] - w/2, v + offset, f'{v:.1f}', ha='center', va='bottom',
            fontsize=8, fontweight='bold', color=C_TEXT)

for i, v in enumerate(cf):
    offset = 0.8 if v > 2 else 1.5
    ax.text(x[i] + w/2, v + offset, f'{v:.1f}', ha='center', va='bottom',
            fontsize=8, fontweight='bold', color=C_TEXT)

ax.set_xticks(x)
ax.set_xticklabels(modes, fontsize=8.5)
ax.set_ylabel('Violation Rate (%)')
ax.set_ylim(0, 21)
ax.legend(fontsize=7.5, loc='upper right', framealpha=0.9, edgecolor='#E0E0E0')

plt.tight_layout()

out_path = '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/figures/fig_violation_composition'
fig.savefig(out_path + '.pdf')
fig.savefig(out_path + '.png')
plt.close()
print('Done')
