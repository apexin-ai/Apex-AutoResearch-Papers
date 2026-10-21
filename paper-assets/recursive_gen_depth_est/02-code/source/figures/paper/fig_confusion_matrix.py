import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 13,
    'axes.titlesize': 14,
    'axes.labelsize': 14,
    'xtick.labelsize': 13,
    'ytick.labelsize': 13,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

cm_best = np.array([
    [99.1,  0.9,  0.0,  0.0],
    [ 0.5, 91.1,  7.7,  0.7],
    [ 0.0,  6.6, 72.9, 20.4],
    [ 0.0,  0.5, 19.3, 80.2],
])

cm_loo = np.array([
    [99.3,  0.7,  0.0,  0.0],
    [ 1.5, 75.5, 17.4,  5.6],
    [ 0.4, 22.1, 43.3, 34.2],
    [ 0.3,  7.8, 33.1, 58.8],
])

labels = ['d0', 'd1', 'd2', 'd3']
panels = [
    (cm_best, 'GPT-2 XL / temp (best, 85.9%)'),
    (cm_loo, 'OLMo holdout (best LOO, 69.2%)'),
]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
fig.subplots_adjust(wspace=0.3)

for ax, (cm, title) in zip(axes, panels):
    im = ax.imshow(cm, cmap='Blues', vmin=0, vmax=100, aspect='equal')

    for i in range(4):
        for j in range(4):
            val = cm[i, j]
            color = 'white' if val > 60 else 'black'
            ax.text(j, i, f'{val:.1f}', ha='center', va='center',
                    fontsize=13, fontweight='bold', color=color)
            if i == j:
                rect = patches.Rectangle(
                    (j - 0.5, i - 0.5), 1, 1,
                    linewidth=2, edgecolor='black', facecolor='none'
                )
                ax.add_patch(rect)

    ax.set_xticks(range(4))
    ax.set_yticks(range(4))
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('True')
    ax.set_title(title)
    ax.tick_params(length=0)

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper/fig_confusion_matrix'
fig.savefig(f'{out_base}.pdf')
fig.savefig(f'{out_base}.png')
plt.close(fig)
print('Done')
