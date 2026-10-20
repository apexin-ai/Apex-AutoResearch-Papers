"""Figure 4: Cross-benchmark transfer heatmap — 6 models x 3 benchmarks."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent / 'figures' / 'paper'))
from paper_style import *

apply_style()

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# ── Data ─────────────────────────────────────────────────────────────
model_names = ['OLMo-2 7B', 'Falcon3 7B', 'Gemma-2 9B',
               'Qwen2.5-7B', 'Phi-4 14B', 'Qwen2.5-14B']
benchmarks = ['MMLU', 'ARC', 'GSM8K']

data = np.array([
    [+3.21, +3.92, +2.10],
    [+4.19, +4.01, +1.29],
    [+3.76, -1.20, +1.33],
    [-1.78, -2.90, +9.38],
    [-0.17, +0.60, -0.50],
    [-9.37, -3.40, +13.09],
])

# ── Figure ───────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=figsize_column(aspect=0.54))

vmax = 16.5
norm = mcolors.TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)
masked = np.ma.masked_invalid(data)
im = ax.imshow(masked, cmap=DIVERGING_CMAP, norm=norm, aspect='auto')

# Cell annotations with auto black/white text
na_mask = np.isnan(data)
for i in range(len(model_names)):
    for j in range(len(benchmarks)):
        if na_mask[i, j]:
            ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1,
                         fill=True, facecolor=COLORS['grid'],
                         edgecolor=COLORS['separator'], linewidth=0.5, zorder=1))
            ax.text(j, i, 'N/A', ha='center', va='center',
                    fontsize=8, color=COLORS['nonsignificant'], fontstyle='italic')
        else:
            val = data[i, j]
            rgba = DIVERGING_CMAP(norm(val))
            luminance = 0.299 * rgba[0] + 0.587 * rgba[1] + 0.114 * rgba[2]
            text_color = 'white' if luminance < 0.55 else COLORS['text']
            sign = '+' if val > 0 else ''
            ax.text(j, i, f'{sign}{val:.1f}', ha='center', va='center',
                    fontsize=10, color=text_color, fontweight='bold')

ax.set_xticks(range(len(benchmarks)))
ax.set_yticks(range(len(model_names)))
ax.set_xticklabels(benchmarks)
ax.set_yticklabels(model_names)

ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)

for spine in ax.spines.values():
    spine.set_visible(False)

# White grid separators
ax.set_xticks(np.arange(len(benchmarks)+1)-.5, minor=True)
ax.set_yticks(np.arange(len(model_names)+1)-.5, minor=True)
ax.grid(which="minor", color="white", linestyle='-', linewidth=2)
ax.tick_params(which="minor", bottom=False, left=False)

cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04, shrink=0.85)
cbar.set_label('$\\Delta$acc (pp)', fontsize=9)
cbar.ax.tick_params(labelsize=8)

# ── Save ─────────────────────────────────────────────────────────────
out = str(Path(__file__).parent / 'fig_cross_benchmark_heatmap')
plt.savefig(out + '.pdf', facecolor='white', edgecolor='none')
plt.savefig(out + '.png', facecolor='white', edgecolor='none')
plt.close()
print(f'Saved: {out}.pdf')
