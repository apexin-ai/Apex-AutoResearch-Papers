import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

df = pd.read_csv(os.path.expanduser('~/spectral_optim_vision_geometry/analysis/deit_spectral_results.csv'))

attn_types = ['attn_proj', 'attn_Q', 'attn_K', 'attn_V']
mlp_types = ['mlp_fc1', 'mlp_fc2']

results = []
for block in range(12):
    for cat, types in [('Attention', attn_types), ('MLP', mlp_types)]:
        muon_sr = df[(df['optimizer'] == 'Muon') & (df['block'] == block) & (df['layer_type'].isin(types))]['stable_rank'].mean()
        adamw_sr = df[(df['optimizer'] == 'AdamW') & (df['block'] == block) & (df['layer_type'].isin(types))]['stable_rank'].mean()
        results.append({'block': block, 'category': cat, 'ratio': muon_sr / adamw_sr})

rdf = pd.DataFrame(results)

fig, ax = plt.subplots(figsize=(8, 4))

x = np.arange(12)
width = 0.35

attn_ratios = rdf[rdf['category'] == 'Attention']['ratio'].values
mlp_ratios = rdf[rdf['category'] == 'MLP']['ratio'].values

bars_attn = ax.bar(x - width/2, attn_ratios, width, label='Attention layers',
                   color='#4C72B0', edgecolor='white', linewidth=0.5, zorder=3)
bars_mlp = ax.bar(x + width/2, mlp_ratios, width, label='MLP layers',
                  color='#DD8452', edgecolor='white', linewidth=0.5, zorder=3)

ax.axhline(y=1.0, color='gray', linestyle='--', linewidth=1.0, alpha=0.7, zorder=2)
ax.text(11.5, 1.05, 'ratio = 1.0', ha='right', va='bottom', fontsize=8, color='gray')

all_ratios = np.concatenate([attn_ratios, mlp_ratios])
block_labels = list(range(12)) * 2
cat_labels = ['Attn'] * 12 + ['MLP'] * 12

max_idx = np.argmax(all_ratios)
min_idx = np.argmin(all_ratios)

max_block = block_labels[max_idx]
max_cat = cat_labels[max_idx]
max_val = all_ratios[max_idx]
min_block = block_labels[min_idx]
min_cat = cat_labels[min_idx]
min_val = all_ratios[min_idx]

# Annotate max (Block 3 Attn)
ax.annotate(f'{max_val:.1f}× ({max_cat})',
            xy=(max_block - width/2, max_val),
            xytext=(max_block + 1.8, max_val + 0.25),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=1.2),
            fontsize=8, fontweight='bold', color='#333333')

# Annotate min (Block 0 Attn) — push annotation to the right to avoid y-axis overlap
ax.annotate(f'{min_val:.1f}× ({min_cat})',
            xy=(min_block + (-width/2 if min_cat == 'Attn' else width/2), min_val),
            xytext=(min_block + 1.8, min_val + 0.5),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=1.2),
            fontsize=8, fontweight='bold', color='#333333')

ax.set_xlabel('Transformer Block Index', fontsize=11)
ax.set_ylabel('Stable Rank Ratio (Muon / AdamW)', fontsize=11)
ax.set_title('DeiT-S Per-Layer Stable Rank Ratio', fontsize=13, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels([str(i) for i in range(12)])
ax.legend(loc='upper right', framealpha=0.9, fontsize=9)
ax.set_ylim(0, max(all_ratios) * 1.2)
ax.grid(axis='y', alpha=0.3, zorder=0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

os.makedirs(os.path.expanduser('~/spectral_optim_vision_geometry/figures'), exist_ok=True)
fig.savefig(os.path.expanduser('~/spectral_optim_vision_geometry/figures/deit_perlayer_sr_ratio.pdf'),
            bbox_inches='tight', dpi=300)
fig.savefig(os.path.expanduser('~/spectral_optim_vision_geometry/figures/deit_perlayer_sr_ratio.png'),
            bbox_inches='tight', dpi=300)
print('Done.')
