"""Single-model variance decomposition bar chart (§4.1 results)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# Data from §4.1 single-model baseline (Llama-3.1-8B-Instruct, MMLU)
components = [
    'item',
    'resid.',
    'prmpt\n×item',
    'seed\n×item',
    'prec.\n×item',
    'temp.\n×item',
    'prec.',
    'ord.\n×item',
    'other',
]
values = [58.4, 23.1, 5.5, 4.7, 3.3, 2.9, 0.9, 0.8, 0.4]

colors = [
    '#2c3e50',  # item_id - dark (dominant)
    '#95a5a6',  # residual - grey
    '#3498db',  # prompt×item
    '#2ecc71',  # seed×item
    '#9b59b6',  # precision×item
    '#f39c12',  # temp×item
    '#e74c3c',  # precision main
    '#1abc9c',  # ordering×item
    '#bdc3c7',  # others
]

fig, ax = plt.subplots(figsize=(3.4, 2.4))

bars = ax.bar(range(len(values)), values, color=colors, width=0.7,
              edgecolor='white', linewidth=0.5)

# Value labels
for i, (bar, val) in enumerate(zip(bars, values)):
    if val >= 3:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.8,
                f'{val}%', ha='center', va='bottom', fontsize=6,
                fontweight='bold')
    else:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.8,
                f'{val}', ha='center', va='bottom', fontsize=5.5,
                color='#666666')

ax.set_xticks(range(len(components)))
ax.set_xticklabels(components, fontsize=6, rotation=0)
ax.set_ylabel('Variance share (%)', fontsize=8)
ax.set_ylim(0, 68)

# Bracket for "item-conditional interactions"
ax.annotate('', xy=(1.7, 62), xytext=(7.3, 62),
            arrowprops=dict(arrowstyle='-', color='#e74c3c', lw=0.8))
ax.plot([1.7, 1.7], [61, 62], color='#e74c3c', lw=0.8)
ax.plot([7.3, 7.3], [61, 62], color='#e74c3c', lw=0.8)
ax.text(4.5, 63, 'item-conditional interactions (17.2%)',
        ha='center', fontsize=5.5, color='#e74c3c', fontstyle='italic')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='x', length=0)

plt.tight_layout()
out = Path(__file__).parent
plt.savefig(out / 'fig_single_model_variance.pdf', bbox_inches='tight', dpi=300)
plt.savefig(out / 'fig_single_model_variance.png', bbox_inches='tight', dpi=200)
plt.close()
print("Saved fig_single_model_variance.pdf/png")
