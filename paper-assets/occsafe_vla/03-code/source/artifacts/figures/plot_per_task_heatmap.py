"""Per-task CAR heatmap: 4 factorial conditions × 10 tasks.
Cell 1/3/Vanilla: v2 real data. Cell 2/4: PLACEHOLDER until Wave 1."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
})

# Rows: 4 factorial cells (v2 data, mean across seeds)
# Columns: T0..T9
# fmt: condition_name: [T0, T1, T2, T3, T4, T5, T6, T7, T8, T9]
data = {
    'Full OCC (BN)':   [0.97, 0.97, 0.89, 0.19, 0.98, 0.15, 0.34, 0.82, 0.99, 0.94],  # Cell 1 — v2 real (3 seeds)
    'Full OCC (LN)':   [0.98, 0.92, 0.92, 0.38, 0.98, 0.07, 0.57, 0.97, 1.00, 1.00],  # Cell 2 — PLACEHOLDER (update Wave 1)
    'Detach (BN)':     [0.98, 0.92, 0.93, 0.36, 0.95, 0.08, 0.50, 0.97, 1.00, 1.00],  # Cell 3 — v2 real (4 seeds)
    'Detach (LN)':     [0.97, 0.78, 0.90, 0.44, 0.96, 0.12, 0.36, 1.00, 0.99, 1.00],  # Cell 4 — PLACEHOLDER (update Wave 1)
}
vanilla = [0.98, 0.93, 0.94, 0.34, 0.96, 0.04, 0.39, 0.91, 1.00, 0.96]  # v2 real (3 seeds)

task_labels = [f'T{i}' for i in range(10)]
task_difficulty = ['E', 'E', 'E', 'H', 'E', 'H', 'H', 'E', 'E', 'E']
condition_labels = list(data.keys())

mat = np.array(list(data.values()))

fig, ax = plt.subplots(figsize=(8.5, 3.2))

cmap = plt.cm.RdYlGn
im = ax.imshow(mat, cmap=cmap, aspect='auto', vmin=0.0, vmax=1.0, interpolation='nearest')

for i in range(mat.shape[0]):
    for j in range(mat.shape[1]):
        val = mat[i, j]
        text_color = 'white' if val < 0.35 else 'black'
        fontweight = 'bold' if val < 0.20 or val > 0.95 else 'normal'
        ax.text(j, i, f'{val:.2f}', ha='center', va='center',
                fontsize=8.5, color=text_color, fontweight=fontweight)

ax.set_xticks(np.arange(len(task_labels)))
ax.set_xticklabels([f'{t}\n({d})' for t, d in zip(task_labels, task_difficulty)])
ax.set_yticks(np.arange(len(condition_labels)))
ax.set_yticklabels(condition_labels)

ax.set_xlabel('Task (E=Easy, H=Hard)')

# Vanilla reference line annotations
for j in range(len(vanilla)):
    v = vanilla[j]
    ax.plot([j - 0.45, j + 0.45], [-0.55, -0.55], color='#555555', linewidth=1.5, clip_on=False)
    ax.text(j, -0.55, f'{v:.2f}', ha='center', va='center', fontsize=7, color='#555555')

ax.text(-1.8, -0.55, 'Vanilla', ha='right', va='center', fontsize=9, color='#555555', fontstyle='italic')

cbar = fig.colorbar(im, ax=ax, shrink=0.85, pad=0.02)
cbar.set_label('CAR', rotation=270, labelpad=12)

ax.set_title('Per-Task Collision Avoidance Rate by Factorial Cell', pad=10, fontsize=12)

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/figures'
fig.savefig(f'{out_dir}/per_task_heatmap.pdf')
fig.savefig(f'{out_dir}/per_task_heatmap.png')
print(f'Saved to {out_dir}/per_task_heatmap.pdf and .png')
plt.close()
