import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

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
})

models = ['Qwen3-8B', 'Llama-3.1-8B', 'Mistral-7B']
datasets = ['SciERC', 'DocRED']

dr_reduction = np.array([
    [94, 45],   # Qwen
    [99, 90],   # Llama
    [76, 42],   # Mistral
])

cmap = LinearSegmentedColormap.from_list('blue_mono',
    ['#BAD4F0', '#8BAED4', '#5B7FAD', '#2B4C7E', '#1B2A4A'])

fig, ax = plt.subplots(figsize=(3.5, 3.0))

im = ax.imshow(dr_reduction, cmap=cmap, vmin=30, vmax=100, aspect='auto')

for i in range(3):
    for j in range(2):
        val = dr_reduction[i, j]
        text_color = 'white' if val >= 70 else '#333333'
        ax.text(j, i, f'{val}%', ha='center', va='center',
                fontsize=13, fontweight='bold', color=text_color)

ax.set_xticks(range(2))
ax.set_xticklabels(datasets, fontsize=10)
ax.set_yticks(range(3))
ax.set_yticklabels(models, fontsize=9)

ax.set_xlabel('')
ax.set_ylabel('')

cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.08)
cbar.set_label('DR Reduction (%)', fontsize=9)
cbar.ax.tick_params(labelsize=8)

ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
for spine in ax.spines.values():
    spine.set_linewidth(0.5)
    spine.set_color('#CCCCCC')

plt.tight_layout()

out_path = '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/figures/fig_crossmodel_heatmap'
fig.savefig(out_path + '.pdf')
fig.savefig(out_path + '.png')
plt.close()
print('Done')
