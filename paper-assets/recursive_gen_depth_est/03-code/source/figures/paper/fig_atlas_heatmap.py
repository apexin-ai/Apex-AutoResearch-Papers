import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
})

with open('/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/atlas_v2/feature_importance_9cell.json') as f:
    data = json.load(f)

per_cell = data['per_cell']

cell_keys = [
    'pythia_nucleus095', 'pythia_temp09', 'pythia_topk50',
    'olmo_nucleus095', 'olmo_temp09', 'olmo_topk50',
    'gpt2xl_nucleus095', 'gpt2xl_temp09', 'gpt2xl_topk50',
]

features = ['p90_ppl', 'var_surprisal', 'mean_ppl', 'p75_ppl', 'mean_surprisal', 'var_ppl', 'type_token_ratio']
universal_top2 = {'p90_ppl', 'var_surprisal'}

imp_matrix = np.zeros((len(features), len(cell_keys)))
for j, ck in enumerate(cell_keys):
    cell = per_cell[ck]
    for i, feat in enumerate(features):
        imp_matrix[i, j] = cell['importances'][feat]

fig, ax = plt.subplots(figsize=(3.45, 2.0))

im = ax.imshow(imp_matrix, cmap='YlOrRd', aspect='auto', vmin=0, vmax=imp_matrix.max())

for i in range(len(features)):
    for j in range(len(cell_keys)):
        val = imp_matrix[i, j]
        color = 'white' if val > 0.16 else 'black'
        ax.text(j, i, f'.{int(val*1000):03d}', ha='center', va='center', fontsize=5,
                color=color, fontweight='bold' if val > 0.12 else 'normal')

ylabels = []
for feat in features:
    label = f'★ {feat}' if feat in universal_top2 else f'  {feat}'
    ylabels.append(label)
ax.set_yticks(range(len(features)))
ax.set_yticklabels(ylabels, fontsize=6)

strategy_labels = ['nuc', 'tmp', 'topk'] * 3
ax.set_xticks(range(len(cell_keys)))
ax.set_xticklabels(strategy_labels, fontsize=5.5)

model_names = ['Pythia-1.4B', 'OLMo-1B', 'GPT-2 XL']
for g, name in enumerate(model_names):
    center = g * 3 + 1
    ax.text(center, -0.7, name, ha='center', va='bottom', fontsize=7, fontweight='bold',
            transform=ax.get_xaxis_transform())

for x in [2.5, 5.5]:
    ax.axvline(x, color='white', linewidth=2)

for x in [0.5, 1.5, 3.5, 4.5, 6.5, 7.5]:
    ax.axvline(x, color='white', linewidth=0.4, alpha=0.5)
for y in [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]:
    ax.axhline(y, color='white', linewidth=0.4, alpha=0.5)

cbar = fig.colorbar(im, ax=ax, shrink=0.85, pad=0.02)
cbar.set_label('Importance', fontsize=6)
cbar.ax.tick_params(labelsize=5)

ax.tick_params(top=False, bottom=True, labeltop=False, labelbottom=True, length=2)

plt.tight_layout()

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/figures/fig_atlas_heatmap'
fig.savefig(f'{out_base}.pdf')
fig.savefig(f'{out_base}.png')
plt.close()

import os
for ext in ['pdf', 'png']:
    p = f'{out_base}.{ext}'
    sz = os.path.getsize(p)
    print(f'{p}: {sz} bytes')
