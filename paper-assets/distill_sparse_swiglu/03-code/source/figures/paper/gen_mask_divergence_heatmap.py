"""Figure A.5: Per-layer Jaccard distance between KL and magnitude masks (30% + 50%)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.linewidth': 0.6,
    'mathtext.fontset': 'cm',
})

OUT = '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/figures/paper'

jd_30 = np.array([
    0.4095, 0.4315, 0.4602, 0.435, 0.4381, 0.4409, 0.4349, 0.4696,
    0.4858, 0.4763, 0.4856, 0.4881, 0.4575, 0.4405, 0.419, 0.3882,
    0.3689, 0.3842, 0.3785, 0.4167, 0.433, 0.448, 0.4893, 0.5091,
    0.5539, 0.573, 0.593, 0.6001, 0.5962, 0.5383, 0.399, 0.3614,
])

jd_50 = np.array([
    0.627, 0.7411, 0.7193, 0.6907, 0.6739, 0.6776, 0.6799, 0.7112,
    0.7088, 0.7271, 0.7173, 0.695, 0.6921, 0.6988, 0.646, 0.61,
    0.6112, 0.6154, 0.6371, 0.6582, 0.6693, 0.6746, 0.6998, 0.7188,
    0.7338, 0.7471, 0.7517, 0.7437, 0.729, 0.6998, 0.6079, 0.5234,
])

data = np.vstack([jd_30, jd_50])

fig, ax = plt.subplots(figsize=(6.5, 1.5))

cmap = plt.cm.YlOrRd
im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=0.3, vmax=0.8)

ax.set_yticks([0, 1])
ax.set_yticklabels(['30%', '50%'])
ax.set_xticks(np.arange(0, 32, 4))
ax.set_xticklabels([str(i) for i in range(0, 32, 4)])
ax.set_xlabel('Layer index')
ax.set_ylabel('Sparsity')

for i in range(2):
    for j in range(32):
        val = data[i, j]
        color = 'white' if val > 0.60 else '#333333'
        if j % 4 == 0:
            ax.text(j, i, f'{val:.2f}', ha='center', va='center',
                    fontsize=5.5, color=color, fontweight='bold')

cbar = plt.colorbar(im, ax=ax, fraction=0.02, pad=0.04, aspect=12)
cbar.set_label('Jaccard distance', fontsize=8)
cbar.ax.tick_params(labelsize=7)

mean_30 = np.mean(jd_30)
mean_50 = np.mean(jd_50)
ax.axhline(y=0.5, color='white', linewidth=1.5, zorder=5)

ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['top'].set_linewidth(0.4)
ax.spines['right'].set_linewidth(0.4)
ax.spines['bottom'].set_linewidth(0.4)
ax.spines['left'].set_linewidth(0.4)

fig.tight_layout()
fig.savefig(f'{OUT}/mask_divergence_heatmap.pdf')
fig.savefig(f'{OUT}/mask_divergence_heatmap.png')
print('Saved mask_divergence_heatmap.pdf/.png')
plt.close()
