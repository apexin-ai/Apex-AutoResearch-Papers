import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Data
conditions = [
    "Bypass\n(baseline, k=1.0)",
    "ACIS\n(learned, k=0.5)",
    "ACIS\n(learned, k=0.7)",
    "ACIS\n(learned, k=0.9)",
    "Random\n(random, k=0.5)",
    "True-removal\n(learned, k=0.5)",
    "Merge\n(learned, k=0.5)",
]
sr = [44.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
ci_lo = [40.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
ci_hi = [49.2, 1.3, 0.76, 0.76, 0.76, 0.8, 0.76]

err_lo = [s - lo for s, lo in zip(sr, ci_lo)]
err_hi = [hi - s for s, hi in zip(sr, ci_hi)]

# Colors: Okabe-Ito
color_baseline = '#0072B2'
color_pruning = '#D55E00'  # muted orange-red for all pruning conditions

colors = [color_baseline] + [color_pruning] * 6
alphas = [1.0] + [0.55] * 6

fig, ax = plt.subplots(figsize=(8, 3.5))

x = np.arange(len(conditions))
bar_width = 0.62

bars = ax.bar(x, sr, width=bar_width, color=colors, edgecolor='white', linewidth=0.5, zorder=3)
for bar, a in zip(bars, alphas):
    bar.set_alpha(a)

# Error bars
ax.errorbar(x, sr, yerr=[err_lo, err_hi], fmt='none', ecolor='#333333',
            elinewidth=1.2, capsize=3.5, capthick=1.2, zorder=4)

# Y axis
ax.set_ylim(0, 55)
ax.set_yticks([0, 10, 20, 30, 40, 50])
ax.set_ylabel('Success Rate (%)')

# X axis
ax.set_xticks(x)
ax.set_xticklabels(conditions, rotation=25, ha='right', fontsize=8.5)
ax.set_xlim(-0.6, len(conditions) - 0.4)

# Baseline annotation
ax.annotate('44.8%', xy=(0, 44.8), xytext=(0, 48.5),
            ha='center', va='bottom', fontsize=11, fontweight='bold',
            color=color_baseline)

# 0% annotations for pruning conditions
for i in range(1, len(conditions)):
    ax.annotate('0%', xy=(i, 0), xytext=(i, 2.0),
                ha='center', va='bottom', fontsize=8.5, color='#555555')

# Cliff-edge annotation: bracket + arrow from baseline to pruning zone
ax.annotate('',
            xy=(3.0, 42), xycoords='data',
            xytext=(0.55, 42), textcoords='data',
            arrowprops=dict(arrowstyle='->', color='#CC0000', lw=2.0,
                            connectionstyle='arc3,rad=0'))

ax.text(1.75, 44.5, 'Cliff Edge', ha='center', va='bottom',
        fontsize=11, fontweight='bold', color='#CC0000',
        fontstyle='italic')

# Dashed separator line between baseline and pruning
ax.axvline(x=0.5, color='#999999', linestyle='--', linewidth=1.0, alpha=0.7, zorder=1)

# Light grid on y axis
ax.yaxis.grid(True, linestyle=':', alpha=0.4, zorder=0)
ax.set_axisbelow(True)

# Legend for ablation dimensions (bottom)
legend_elements = [
    mpatches.Patch(facecolor=color_baseline, alpha=1.0, label='Baseline (no pruning)'),
    mpatches.Patch(facecolor=color_pruning, alpha=0.55, label='Token pruning (all variants)'),
]

# Dimension markers as text annotations below
dim_text = (
    r'$\mathbf{Ablation\ dimensions}$: '
    r'Scoring $\in$ {learned, random}  |  '
    r'Retain ratio $k \in$ {0.5, 0.7, 0.9}  |  '
    r'Mechanism $\in$ {zero-mask, true-removal, merge}'
)

ax.legend(handles=legend_elements, loc='upper right', frameon=True,
          fancybox=False, edgecolor='#cccccc', framealpha=0.9)

fig.text(0.5, -0.02, dim_text, ha='center', va='top', fontsize=8.5,
         color='#444444')

plt.tight_layout()

out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig_cliff_edge.pdf', format='pdf')
fig.savefig(out_dir / 'fig_cliff_edge.png', format='png')
plt.close()
print("Done.")
