"""Cohen's |d| effect-size heatmap (Figure 3).

Compact single-column heatmap: 3 models × 6 conditions.
Output: fig_heatmap.{pdf,png}
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import shutil
from pathlib import Path

import sys; sys.path.insert(0, str(Path(__file__).resolve().parent))
import palette
palette.apply()

PROJ = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam')

models = ['Qwen', 'Llama', 'Mistral']
col_labels = ['5%', '15%', '25%', '50%', '15%', '50%']

d_vals = np.array([
    [4.15, 5.36, 7.44, 5.08, 3.16, 5.30],
    [2.57, 2.80, 2.56, 2.30, np.nan, np.nan],
    [3.83, 3.37, np.nan, 4.09, np.nan, np.nan],
])

ci_text = [
    ['[2.7, 9.9]', '±1.10', '±1.86', '±3.02', '[2.0, 9.5]', '[3.6, 15.2]'],
    ['±0.99', '±0.60', '±0.52', '±0.30', '', ''],
    ['±1.42', '±0.68', '', '±0.53', '', ''],
]

n_rows, n_cols = d_vals.shape

cmap = mcolors.LinearSegmentedColormap.from_list(
    'd_cmap', ['#FFFFFF', '#C8D6E5', '#7B9CC7', palette.QWEN], N=256)
norm = mcolors.Normalize(vmin=0, vmax=8.0)

fig, ax = plt.subplots(figsize=(4.2, 1.85))
fig.subplots_adjust(left=0.13, right=0.88, top=0.85, bottom=0.18)

d_display = np.where(np.isnan(d_vals), 0, d_vals)
im = ax.imshow(d_display, cmap=cmap, norm=norm, aspect='auto')

# Missing cells with hatching
for i in range(n_rows):
    for j in range(n_cols):
        if np.isnan(d_vals[i, j]):
            ax.add_patch(plt.Rectangle(
                (j - 0.5, i - 0.5), 1, 1,
                facecolor='#F8F8F8', edgecolor='white', linewidth=1.2,
                hatch='///', zorder=2))
            ax.patches[-1].set_edgecolor('#E0E0E0')

# White grid
for i in range(n_rows + 1):
    ax.axhline(y=i - 0.5, color='white', linewidth=1.2, zorder=3)
for j in range(n_cols + 1):
    ax.axvline(x=j - 0.5, color='white', linewidth=1.2, zorder=3)
ax.axvline(x=3.5, color='white', linewidth=3.0, zorder=4)

# Cell text
for i in range(n_rows):
    for j in range(n_cols):
        val = d_vals[i, j]
        if np.isnan(val):
            ax.text(j, i, '—', ha='center', va='center',
                    fontsize=8, color='#CCCCCC', zorder=5)
        else:
            r, g, b, _ = cmap(norm(val))
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            txt_color = 'white' if lum < 0.55 else palette.TEXT

            ax.text(j, i - 0.12, f'{val:.2f}',
                    ha='center', va='center', fontsize=8,
                    color=txt_color, fontweight='bold', zorder=5)
            if ci_text[i][j]:
                ci_alpha = 0.80 if lum < 0.55 else 0.65
                ax.text(j, i + 0.18, ci_text[i][j],
                        ha='center', va='center', fontsize=5.5,
                        color=txt_color, alpha=ci_alpha, zorder=5)

# Axes
ax.set_xticks(range(n_cols))
ax.set_xticklabels(col_labels, fontsize=7)
ax.xaxis.set_ticks_position('bottom')
ax.set_yticks(range(n_rows))
ax.set_yticklabels(models, fontsize=7.5, fontweight='bold')

for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(length=0)

# Benchmark group labels
trans = ax.get_xaxis_transform()
ax.text(1.5, -0.25, 'MMLU', ha='center', va='top',
        fontsize=7, fontweight='bold', color=palette.TEXT, transform=trans)
ax.text(4.5, -0.25, 'ARC-C', ha='center', va='top',
        fontsize=7, fontweight='bold', color=palette.TEXT, transform=trans)

# Colorbar
cbar = fig.colorbar(im, ax=ax, shrink=0.75, pad=0.03, aspect=12)
cbar.set_label("Cohen's |$d$|", fontsize=7, labelpad=3)
cbar.ax.tick_params(labelsize=6)
cbar.outline.set_linewidth(0.3)

# Save
out = Path(__file__).resolve().parent
fig.savefig(out / 'fig_heatmap.pdf', format='pdf')
fig.savefig(out / 'fig_heatmap.png', format='png')
plt.close()

for tgt in [PROJ / 'paper' / 'paper']:
    shutil.copy2(str(out / 'fig_heatmap.pdf'), str(tgt / 'fig_heatmap.pdf'))
print("Done: fig_heatmap.pdf/png")
