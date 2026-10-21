import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
import numpy as np
import json
import seaborn as sns

with open('/root/gen-depth-fingerprint/results/cross_temp_transfer.json') as f:
    data = json.load(f)

generators = ['Pythia-2.8B', 'Pythia-1B', 'Qwen3-1.7B', 'Llama-3.2-3B', 'OLMo-2-1B', 'Qwen3-8B', 'Qwen3-0.6B', 'Mistral-7B']
three_class_f1 = [0.798, 0.806, 0.772, 0.775, 0.781, 0.714, 0.780, 0.682]
binary_f1 = [0.724, 0.718, 0.709, 0.697, 0.695, 0.692, 0.691, 0.633]

gen6_3class = data['results']['0.7_to_0.7']['per_generator_3class']
gen6_binary = data['results']['0.7_to_0.7']['per_generator_binary']

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

ax = axes[0]
sorted_idx = np.argsort(binary_f1)[::-1]
sorted_gen = [generators[i] for i in sorted_idx]
sorted_f1 = [binary_f1[i] for i in sorted_idx]
sorted_3cl = [three_class_f1[i] for i in sorted_idx]

y = np.arange(len(generators))
width = 0.35
bars1 = ax.barh(y + width/2, sorted_3cl, width, label='3-class F1', color='#0072B2', edgecolor='white')
bars2 = ax.barh(y - width/2, sorted_f1, width, label='Binary F1', color='#D55E00', edgecolor='white')
ax.set_yticks(y)
ax.set_yticklabels(sorted_gen, fontsize=9)
ax.set_xlabel('Macro F1', fontsize=10)
ax.set_title('(a) Per-Generator LOGO F1', fontsize=11, fontweight='bold')
ax.set_xlim(0.55, 0.85)
ax.axvline(x=0.762, color='#0072B2', linestyle='--', alpha=0.5, linewidth=0.8)
ax.axvline(x=0.694, color='#D55E00', linestyle='--', alpha=0.5, linewidth=0.8)
ax.legend(fontsize=8, loc='lower right')

for bar in bars1:
    ax.text(bar.get_width() + 0.003, bar.get_y() + bar.get_height()/2,
            f'{bar.get_width():.3f}', ha='left', va='center', fontsize=7)
for bar in bars2:
    ax.text(bar.get_width() + 0.003, bar.get_y() + bar.get_height()/2,
            f'{bar.get_width():.3f}', ha='left', va='center', fontsize=7)

ax = axes[1]
gen6_names = ['OLMo-2-1B', 'Pythia-1B', 'Pythia-2.8B', 'Qwen3-0.6B', 'Qwen3-1.7B', 'Qwen3-8B']
gen6_keys = ['olmo-2-1b', 'pythia-1b', 'pythia-2.8b', 'qwen3-0.6b', 'qwen3-1.7b', 'qwen3-8b']
matrix = np.array([[gen6_3class[k] for k in gen6_keys],
                   [gen6_binary[k] for k in gen6_keys]]).T
sns.heatmap(matrix, annot=True, fmt='.3f', cmap='RdYlGn', ax=ax,
            xticklabels=['3-class F1', 'Binary F1'],
            yticklabels=gen6_names,
            vmin=0.6, vmax=1.0, linewidths=0.5, cbar_kws={'label': 'F1 Score'})
ax.set_title('(b) 6-Gen LOGO Detail', fontsize=11, fontweight='bold')
ax.tick_params(labelsize=9)

plt.tight_layout(pad=2.0)
plt.savefig('/root/gen-depth-fingerprint/chart/fig_appendix_per_gen.pdf', bbox_inches='tight', dpi=300)
print("Saved fig_appendix_per_gen.pdf")
