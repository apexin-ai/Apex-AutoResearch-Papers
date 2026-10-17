import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

depth_pairs = ['d0→d1', 'd1→d2', 'd2→d3', 'd3→d4', 'd4→d5']
x = np.arange(len(depth_pairs))

binary_pairwise = [0.999, 0.9250, 0.8225, 0.7837, 0.6832]
fourclass_pipeline = [0.9975, 0.8607, 0.8005, None, None]
sixclass_pipeline = [0.9962, 0.8231, 0.6878, 0.6809, 0.6948]

thresholds = [0.65, 0.70, 0.75, 0.80]

# Okabe-Ito colors
c_blue = '#0072B2'
c_orange = '#E69F00'
c_green = '#009E73'

fig, ax = plt.subplots(figsize=(6, 4))

# Binary pairwise
ax.plot(x, binary_pairwise, '-o', color=c_blue, label='Binary pairwise RF',
        markersize=7, zorder=5)

# 4-class pipeline (only first 3 points)
fc_x = [0, 1, 2]
fc_y = [fourclass_pipeline[i] for i in fc_x]
ax.plot(fc_x, fc_y, '--^', color=c_orange, label='4-class pipeline',
        markersize=7, zorder=5)

# 6-class pipeline
ax.plot(x, sixclass_pipeline, ':s', color=c_green, label='6-class pipeline',
        markersize=7, zorder=5)

# Threshold lines
for t in thresholds:
    ax.axhline(y=t, color='#888888', linestyle='--', linewidth=0.8, alpha=0.5)
    ax.text(len(depth_pairs) - 0.5, t + 0.005, f'T={t:.2f}',
            fontsize=8, color='#666666', ha='right', va='bottom')

# EDD shaded region
ax.axvspan(3.5, 4.5, alpha=0.08, color='red', zorder=0)
ax.axvline(x=3.5, color='#CC0000', linestyle='--', linewidth=1.2, alpha=0.7)

# EDD annotation
ax.annotate('EDD = 4',
            xy=(3.5, 0.73), xytext=(2.6, 0.58),
            fontsize=11, fontweight='bold', color='#CC0000',
            arrowprops=dict(arrowstyle='->', color='#CC0000', lw=1.5),
            ha='center', va='top')

# Grid
ax.grid(True, alpha=0.3, color='#CCCCCC', linewidth=0.5)
ax.set_axisbelow(True)

ax.set_xticks(x)
ax.set_xticklabels(depth_pairs)
ax.set_xlabel('Adjacent Depth Pair')
ax.set_ylabel('Pairwise AUC')
ax.set_ylim(0.5, 1.05)
ax.set_xlim(-0.3, 4.5)

ax.legend(loc='upper right', frameon=True, framealpha=0.9, edgecolor='#CCCCCC')

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper'
fig.savefig(f'{out_dir}/fig_auc_decay.pdf')
fig.savefig(f'{out_dir}/fig_auc_decay.png')
plt.close(fig)
print('Done.')
