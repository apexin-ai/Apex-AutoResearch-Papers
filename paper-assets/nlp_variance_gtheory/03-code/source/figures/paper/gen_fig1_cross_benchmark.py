"""Generate Figure 3: Cross-benchmark variance decomposition (stacked bar chart).
Data source: Table 3 in paper (8-model Henderson Method I results).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],
    'font.size': 11,
    'axes.labelsize': 11,
    'xtick.labelsize': 10.5,
    'ytick.labelsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

benchmarks = ['MMLU', 'ARC', 'HellaSwag', 'GSM8K', 'MATH']

data = {
    'Item':        [37.9, 37.9, 34.3, 16.9, 24.0],
    'Model×Item':  [30.2, 33.7, 36.0, 14.6, 17.3],
    'Model':       [ 2.8,  3.1,  5.4, 10.7,  8.5],
    'Prompt':      [ 0.9,  1.4,  2.1,  5.4,  0.8],
    'Residual':    [25.0, 15.4, 21.4, 39.9, 43.9],
    'Other':       [ 3.2,  8.5,  0.8, 12.5,  5.5],
}

components = ['Item', 'Model×Item', 'Model', 'Prompt', 'Residual', 'Other']

colors = {
    'Item':       '#2166ac',
    'Model×Item': '#67a9cf',
    'Model':      '#ef8a62',
    'Prompt':     '#b2182b',
    'Residual':   '#999999',
    'Other':      '#d9d9d9',
}

hatches = {
    'Item':       '///',
    'Model×Item': '\\\\\\',
    'Model':      '|||',
    'Prompt':     '---',
    'Residual':   '...',
    'Other':      'xxx',
}

# Layout: MC group x=[0, 1.0, 2.0], FF group x=[3.3, 4.3]
x_positions = [0, 1.0, 2.0, 3.3, 4.3]
bar_width = 0.55

fig, ax = plt.subplots(figsize=(8.5, 6.5))

bottoms = np.zeros(5)
for comp in components:
    values = data[comp]
    ax.bar(x_positions, values, bar_width, bottom=bottoms,
           color=colors[comp], edgecolor='white', linewidth=0.3,
           hatch=hatches[comp], label=comp)
    for i, (v, b) in enumerate(zip(values, bottoms)):
        if v > 12:
            ax.text(x_positions[i], b + v/2, f'{v:.0f}%',
                    ha='center', va='center', fontsize=7, color='white', fontweight='bold')
    bottoms += values

# Regime separator
ax.axvline(x=2.65, color='black', linestyle='--', linewidth=0.8, alpha=0.5)

# Group labels
ax.text(1.0, 103, 'Multiple-Choice', ha='center', va='bottom', fontsize=9, fontstyle='italic')
ax.text(3.8, 103, 'Free-Form', ha='center', va='bottom', fontsize=9, fontstyle='italic')

ax.set_xticks(x_positions)
ax.set_xticklabels(benchmarks, fontsize=9)
ax.set_xlim(-0.5, 4.8)
ax.set_ylim(0, 108)
ax.set_ylabel('Variance Share (%)', fontsize=10)
ax.spines['left'].set_linewidth(0.8)
ax.spines['bottom'].set_linewidth(0.8)

handles = [mpatches.Patch(facecolor=colors[c], edgecolor='white', hatch=hatches[c], label=c) for c in components]
ax.legend(handles=handles, bbox_to_anchor=(0.5, -0.10), loc='upper center',
          fontsize=7.5, ncol=6, framealpha=0.9, edgecolor='none')

plt.tight_layout()

out_dir = Path(__file__).parent
plt.savefig(out_dir / 'fig1_cross_benchmark.pdf', bbox_inches='tight', dpi=300)
plt.savefig(out_dir / 'fig1_cross_benchmark.png', bbox_inches='tight', dpi=200)
plt.close()

print("Saved fig1_cross_benchmark.pdf and .png")
for i, bm in enumerate(benchmarks):
    total = sum(data[c][i] for c in components)
    print(f'  {bm}: {total:.1f}%')
