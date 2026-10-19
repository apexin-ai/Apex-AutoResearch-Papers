"""Generate cosine compression bar chart: shallow vs deep cosine distance for 4 models.
Data source: Tab cosine_volatility (appendix.tex L142-161).
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

models = ['R1-8B', 'OT-7B', 'QwQ-32B', 'R1-32B']
shallow_mean = [0.186, 0.077, 0.037, 0.067]
shallow_std  = [0.097, 0.080, 0.064, 0.050]
deep_mean    = [0.411, 0.206, 0.084, 0.092]
deep_std     = [0.143, 0.091, 0.056, 0.076]
shallow_labels = ['L2', 'L2', 'L2', 'L10']
deep_labels    = ['L14', 'L16', 'L63', 'L63']
ratios = [d/s for d, s in zip(deep_mean, shallow_mean)]

x = np.arange(len(models))
width = 0.32

fig, ax = plt.subplots(figsize=(3.25, 2.2), dpi=300)

BLUE = '#4A90D9'
ORANGE = '#E67E22'

bars_s = ax.bar(x - width/2, shallow_mean, width, yerr=shallow_std,
                color=BLUE, edgecolor='white', linewidth=0.5,
                capsize=2, error_kw={'linewidth': 0.7, 'capthick': 0.7},
                label='Shallow layer', zorder=3)
bars_d = ax.bar(x + width/2, deep_mean, width, yerr=deep_std,
                color=ORANGE, edgecolor='white', linewidth=0.5,
                capsize=2, error_kw={'linewidth': 0.7, 'capthick': 0.7},
                label='Deep layer', zorder=3)

for i, (s, d, r) in enumerate(zip(shallow_mean, deep_mean, ratios)):
    bracket_top = d + deep_std[i] + 0.025
    ax.plot([x[i] - width/2, x[i] - width/2, x[i] + width/2, x[i] + width/2],
            [bracket_top - 0.01, bracket_top, bracket_top, bracket_top - 0.01],
            color='#555555', linewidth=0.6, zorder=4)
    ax.text(x[i], bracket_top + 0.012, f'{r:.1f}×',
            ha='center', va='bottom', fontsize=6.5, fontweight='bold', color='#333333')

for i, (bar, lbl) in enumerate(zip(bars_s, shallow_labels)):
    ax.text(bar.get_x() + bar.get_width()/2, -0.022, lbl,
            ha='center', va='top', fontsize=5, color=BLUE, style='italic')
for i, (bar, lbl) in enumerate(zip(bars_d, deep_labels)):
    ax.text(bar.get_x() + bar.get_width()/2, -0.022, lbl,
            ha='center', va='top', fontsize=5, color=ORANGE, style='italic')

ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=7)
ax.set_ylabel('Mean step-to-step\ncosine distance', fontsize=7)
ax.set_ylim(-0.05, 0.62)
ax.tick_params(axis='y', labelsize=6)
ax.tick_params(axis='x', length=0)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.spines['left'].set_linewidth(0.5)

ax.axhline(y=0, color='#CCCCCC', linewidth=0.4, zorder=1)
ax.yaxis.grid(True, linewidth=0.3, alpha=0.5, zorder=0)

ax.legend(fontsize=6, loc='upper right', framealpha=0.9,
          edgecolor='#CCCCCC', handlelength=1.2, handletextpad=0.4,
          borderpad=0.3, labelspacing=0.3)

plt.tight_layout(pad=0.3)
_dir = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(_dir, 'fig_cosine_compression.pdf'),
            bbox_inches='tight', pad_inches=0.03, facecolor='white')
plt.savefig(os.path.join(_dir, 'fig_cosine_compression.png'), dpi=300,
            bbox_inches='tight', pad_inches=0.03, facecolor='white')
print('Saved: fig_cosine_compression.pdf + fig_cosine_compression.png')
