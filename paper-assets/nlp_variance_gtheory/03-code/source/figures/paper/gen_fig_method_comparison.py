"""Method comparison: prior work vs ours on facets × benchmarks coverage."""
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

fig, ax = plt.subplots(figsize=(3.4, 2.0))

studies = ['Bouthillier\net al. 2021', 'Messing\n2026', 'Ours']
facets = [4, 5, 7]
benchmarks = [3, 1, 5]

x = np.arange(len(studies))
w = 0.3

b1 = ax.bar(x - w/2, facets, w, label='Facets crossed', color='#2c3e50',
            edgecolor='white', linewidth=0.5)
b2 = ax.bar(x + w/2, benchmarks, w, label='Benchmarks', color='#e74c3c',
            edgecolor='white', linewidth=0.5)

for bars in [b1, b2]:
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h + 0.15,
                f'{int(h)}', ha='center', va='bottom', fontsize=7.5,
                fontweight='bold')

# D-study marker for "Ours" only
ax.annotate('+ D-study\nbudgets', xy=(2, 7.3), fontsize=6,
            ha='center', va='bottom', color='#27ae60', fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(studies, fontsize=7.5)
ax.set_ylabel('Count', fontsize=8)
ax.set_ylim(0, 9.5)
ax.legend(fontsize=7, loc='upper left', framealpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='x', length=0)

plt.tight_layout()
out = Path(__file__).parent
plt.savefig(out / 'fig_method_comparison.pdf', bbox_inches='tight', dpi=300)
plt.savefig(out / 'fig_method_comparison.png', bbox_inches='tight', dpi=200)
plt.close()
print("Saved fig_method_comparison.pdf/png")
