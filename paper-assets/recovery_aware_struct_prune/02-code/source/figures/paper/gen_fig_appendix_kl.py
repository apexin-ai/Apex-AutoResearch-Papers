import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 11,
    'axes.titleweight': 'bold',
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# All data verified from W&B or server logs (2026-05-18)
methods = {
    'CKA-only': {
        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'kl': [0.001206, 0.001232, 0.001671, 0.001500, 0.001567, 0.001579, 0.001558, 0.001701, 0.001508, 0.001609],
        'color': '#009E73', 'ls': '-',
    },
    'Random': {
        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90],
        'kl': [0.0042, 0.0047, 0.0046, 0.0044, 0.0045, 0.0043, 0.0046, 0.0045, 0.0044],
        'color': '#E69F00', 'ls': '--',
    },
    'Standard': {
        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'kl': [0.002187, 0.002394, 0.002652, 0.002662, 0.002266, 0.002454, 0.002444, 0.002470, 0.002462, 0.003229],
        'color': '#CC79A7', 'ls': '-',
    },
    'RASP': {
        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'kl': [0.0008379, 0.0009728, 0.001022, 0.0007673, 0.001035, 0.000894, 0.001119, 0.0008899, 0.001043, 0.0008991],
        'color': '#D55E00', 'ls': '-',
    },
}

fig, ax = plt.subplots(figsize=(5.5, 3.5))

for name, d in methods.items():
    ax.plot(d['steps'], d['kl'], color=d['color'], linestyle=d['ls'],
            marker='o', markersize=4, linewidth=1.8, label=name, zorder=3)

ax.set_xlabel('Training Step')
ax.set_ylabel('KL Divergence')
ax.set_xlim(0, 105)
ax.set_xticks(np.arange(0, 110, 20))
ax.grid(True, axis='y', alpha=0.3, color='#cccccc', zorder=0)
ax.legend(loc='upper right', frameon=False)

plt.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper'
fig.savefig(f'{outdir}/fig_appendix_kl.pdf')
fig.savefig(f'{outdir}/fig_appendix_kl.png')
plt.close()
print('KL appendix figure saved.')
