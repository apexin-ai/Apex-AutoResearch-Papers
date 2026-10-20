import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
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
})

methods = ['EAP-IG', 'EP', 'ACDC']

panels = {
    '(a) IOI': np.array([
        [1.00, 0.31, 0.10],
        [0.31, 1.00, 0.09],
        [0.10, 0.09, 1.00],
    ]),
    '(b) Arithmetic': np.array([
        [1.00, 0.695, 0.17],
        [0.695, 1.00, 0.17],
        [0.17, 0.17, 1.00],
    ]),
    '(c) SVA': np.array([
        [1.00, 0.65, 0.32],
        [0.65, 1.00, 0.42],
        [0.32, 0.42, 1.00],
    ]),
    '(d) Factual Recall': np.array([
        [1.00, 0.82, 0.15],
        [0.82, 1.00, 0.15],
        [0.15, 0.15, 1.00],
    ]),
}

fig, axes = plt.subplots(1, 4, figsize=(14, 3.5))

cmap = plt.cm.YlOrRd
norm = mcolors.Normalize(vmin=0, vmax=1)

for ax, (title, matrix) in zip(axes, panels.items()):
    masked = np.ma.array(matrix, mask=np.eye(3, dtype=bool))
    im = ax.imshow(masked, cmap=cmap, norm=norm, aspect='equal')

    for i in range(3):
        for j in range(3):
            if i == j:
                ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1,
                             fill=True, facecolor='#E8E8E8', edgecolor='white', linewidth=1.5))
                ax.text(j, i, '1.00', ha='center', va='center',
                        fontsize=11, color='#888888', fontweight='normal')
            else:
                val = matrix[i, j]
                color = 'white' if val > 0.55 else 'black'
                ax.text(j, i, f'{val:.2f}', ha='center', va='center',
                        fontsize=11, color=color, fontweight='bold')

    ax.set_xticks(range(3))
    ax.set_yticks(range(3))
    ax.set_xticklabels(methods, rotation=30, ha='right')
    if ax == axes[0]:
        ax.set_yticklabels(methods)
    else:
        ax.set_yticklabels([])
    ax.set_title(title, fontsize=12, pad=8)

    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(2.5, -0.5)

    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('#CCCCCC')
        spine.set_linewidth(0.8)
    ax.tick_params(length=0)

cbar_ax = fig.add_axes([0.93, 0.18, 0.012, 0.65])
cbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cbar_ax)
cbar.set_label('Jaccard Similarity', fontsize=11)
cbar.ax.tick_params(labelsize=9)

plt.subplots_adjust(left=0.06, right=0.91, wspace=0.15, bottom=0.15, top=0.88)

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper'
fig.savefig(f'{outdir}/fig3_jaccard_heatmap.pdf')
fig.savefig(f'{outdir}/fig3_jaccard_heatmap.png')
plt.close()
print('Saved fig3_jaccard_heatmap.pdf and .png')
