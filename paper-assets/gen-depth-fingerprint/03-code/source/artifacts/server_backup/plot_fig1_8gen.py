import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

with open('/root/gen-depth-fingerprint/results/8gen_per_gen_spearman.json') as f:
    data = json.load(f)

features = ['hapax_ratio', 'ttr', 'entropy_mean', 'entropy_min', 'entropy_max', 'entropy_std', 'tail_decay']
feature_labels = ['hapax_ratio', 'ttr', 'entropy_mean', 'entropy_min', 'entropy_max', 'entropy_std', 'tail_decay']

generators = data['_generators']
median_vals = data['_median']

family_colors = {
    'pythia-1b': '#2171B5', 'pythia-2.8b': '#2171B5',
    'olmo-2-1b': '#238B45',
    'qwen3-0.6b': '#E6550D', 'qwen3-1.7b': '#E6550D', 'qwen3-8b': '#E6550D',
    'llama-3.2-3b': '#CB181D',
    'mistral-7b-v0.3': '#6A51A3',
}

family_names = {
    'Pythia': '#2171B5',
    'OLMo': '#238B45',
    'Qwen': '#E6550D',
    'Llama': '#CB181D',
    'Mistral': '#6A51A3',
}

fig, ax = plt.subplots(figsize=(7, 3.5))

# Three-zone shading
ax.axhspan(0.4, 0.85, color='#FFCCCC', alpha=0.3, zorder=0)
ax.axhspan(-0.85, -0.4, color='#FFCCCC', alpha=0.3, zorder=0)
ax.axhspan(0.1, 0.4, color='#FFF3CD', alpha=0.3, zorder=0)
ax.axhspan(-0.4, -0.1, color='#FFF3CD', alpha=0.3, zorder=0)
ax.axhspan(-0.1, 0.1, color='#D4EDDA', alpha=0.3, zorder=0)

# Zone labels on right side
ax.text(len(features) - 0.5, 0.55, 'Strong drift', fontsize=7.5, color='#8B0000', ha='right', style='italic', alpha=0.8)
ax.text(len(features) - 0.5, -0.55, 'Strong drift', fontsize=7.5, color='#8B0000', ha='right', style='italic', alpha=0.8)
ax.text(len(features) - 0.5, 0.25, 'Moderate', fontsize=7.5, color='#856404', ha='right', style='italic', alpha=0.8)
ax.text(len(features) - 0.5, -0.25, 'Moderate', fontsize=7.5, color='#856404', ha='right', style='italic', alpha=0.8)
ax.text(len(features) - 0.5, 0.0, 'Near-stationary', fontsize=7.5, color='#155724', ha='right', style='italic', alpha=0.8)

# Zone boundary lines
for y in [0.4, -0.4, 0.1, -0.1]:
    ax.axhline(y=y, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)

# y=0 reference line
ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)

# Plot per-generator dots with jitter
np.random.seed(42)
for i, feat in enumerate(features):
    for gen in generators:
        val = data[gen][feat]
        jitter = np.random.uniform(-0.15, 0.15)
        color = family_colors[gen]
        ax.scatter(i + jitter, val, c=color, s=45, alpha=0.8, edgecolors='white', linewidths=0.3, zorder=3)
    
    # Overall median as black X
    ax.scatter(i, median_vals[feat], c='black', s=70, marker='X', zorder=4, linewidths=0.8)

ax.set_xticks(range(len(features)))
ax.set_xticklabels(feature_labels, fontsize=9, rotation=20, ha='right')
ax.set_ylabel('Spearman ρ with depth', fontsize=10.5)
ax.set_ylim(-0.85, 0.25)
ax.set_xlim(-0.5, len(features) - 0.5)
ax.tick_params(axis='y', labelsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Legend
legend_handles = []
for name, color in family_names.items():
    legend_handles.append(mpatches.Patch(color=color, label=name))
legend_handles.append(plt.Line2D([0], [0], marker='X', color='w', markerfacecolor='black', markersize=8, label='Overall (median)'))

ax.legend(handles=legend_handles, loc='lower left', fontsize=8, framealpha=0.9, ncol=3, columnspacing=1.0)

plt.tight_layout()
plt.savefig('/root/gen-depth-fingerprint/fig1_differential_response.pdf', bbox_inches='tight', dpi=300)
plt.savefig('/root/gen-depth-fingerprint/fig1_differential_response.png', bbox_inches='tight', dpi=200)
plt.close()
print("Done. Saved PDF and PNG.")
