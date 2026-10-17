"""
Cross-benchmark heatmap: BT win probability significance across judges, benchmarks, and style axes.
Output: cross_benchmark_heatmap.pdf (publication-quality, column-width figure)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

# ── Data ──────────────────────────────────────────────────────────────────────
# Rows: GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash, Claude Sonnet 4
# Cols: LLMBar-Form, LLMBar-Verb, LLMBar-Reg, AEval-Form, AEval-Verb, MTB-Form
# None = not tested

bt_values = [
    # GPT-4o
    [0.630, 0.760, 0.570, 0.727, None,  0.692],
    # Qwen3-32B
    [0.665, 0.773, 0.553, 0.657, 0.841, 0.712],
    # Llama-3.3-70B
    [0.695, 0.735, 0.635, 0.756, None,  None ],
    # Gemini-2.5-Flash
    [0.574, 0.708, None,  None,  None,  None ],
    # Claude Sonnet 4
    [0.562, 0.541, None,  0.698, 0.683, 0.733],
]

# Significance levels: 3=p<.001, 2=p<.01, 1=p<.05, 0=NS, -1=not tested
sig_levels = [
    # GPT-4o
    [3, 3, 1, 3, -1, 3],
    # Qwen3-32B
    [3, 3, 0, 3, 3,  3],
    # Llama-3.3-70B
    [3, 3, 2, 3, -1, -1],
    # Gemini-2.5-Flash
    [1, 3, -1, -1, -1, -1],
    # Claude Sonnet 4
    [0, 0, -1, 3, 3, 3],
]

row_labels = ['GPT-4o', 'Qwen3-32B', 'Llama-3.3-70B', 'Gemini-2.5-Flash', 'Claude Sonnet 4']
col_labels = ['LLMBar\nForm.', 'LLMBar\nVerb.', 'LLMBar\nReg.', 'AEval\nForm.', 'AEval\nVerb.', 'MTB\nForm.']

nrows = len(row_labels)
ncols = len(col_labels)

# ── Color mapping ────────────────────────────────────────────────────────────
# Map significance level to color
# Using a blue palette: dark → strong significance
color_map = {
    3:  '#1a5276',   # p<.001 — dark teal-blue
    2:  '#2e86c1',   # p<.01  — medium blue
    1:  '#85c1e9',   # p<.05  — light blue
    0:  '#eaf2f8',   # NS     — very light blue / near-white
    -1: '#d5d8dc',   # not tested — light gray
}

# ── Figure ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(4.5, 2.0))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

for i in range(nrows):
    for j in range(ncols):
        sig = sig_levels[i][j]
        bt = bt_values[i][j]
        color = color_map[sig]

        # Draw cell
        rect = plt.Rectangle((j, nrows - 1 - i), 1, 1,
                              facecolor=color, edgecolor='white', linewidth=1.2)
        ax.add_patch(rect)

        # Not-tested cells: draw diagonal cross
        if sig == -1:
            cx, cy = j + 0.5, nrows - 1 - i + 0.5
            ax.plot([j + 0.2, j + 0.8], [nrows - 1 - i + 0.2, nrows - 1 - i + 0.8],
                    color='#95a5a6', lw=0.8, zorder=2)
            ax.plot([j + 0.2, j + 0.8], [nrows - 1 - i + 0.8, nrows - 1 - i + 0.2],
                    color='#95a5a6', lw=0.8, zorder=2)
            continue

        # BT value text
        text_color = 'white' if sig >= 2 else '#2c3e50'
        ax.text(j + 0.5, nrows - 1 - i + 0.5,
                f'.{int(bt * 1000):03d}',
                ha='center', va='center',
                fontsize=8, fontfamily='sans-serif',
                fontweight='bold' if sig >= 3 else 'normal',
                color=text_color, zorder=3)

# Axis configuration
ax.set_xlim(0, ncols)
ax.set_ylim(0, nrows)
ax.set_xticks([j + 0.5 for j in range(ncols)])
ax.set_xticklabels(col_labels, fontsize=7.5, fontfamily='sans-serif', ha='center')
ax.set_yticks([nrows - 1 - i + 0.5 for i in range(nrows)])
ax.set_yticklabels(row_labels, fontsize=8, fontfamily='sans-serif')
ax.tick_params(axis='both', which='both', length=0, pad=4)
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')

# Remove spines
for spine in ax.spines.values():
    spine.set_visible(False)

# ── Legend (below the heatmap) ────────────────────────────────────────────────
legend_elements = [
    mpatches.Patch(facecolor=color_map[3],  edgecolor='#aaa', linewidth=0.5, label='$p<.001$'),
    mpatches.Patch(facecolor=color_map[2],  edgecolor='#aaa', linewidth=0.5, label='$p<.01$'),
    mpatches.Patch(facecolor=color_map[1],  edgecolor='#aaa', linewidth=0.5, label='$p<.05$'),
    mpatches.Patch(facecolor=color_map[0],  edgecolor='#aaa', linewidth=0.5, label='NS'),
    mpatches.Patch(facecolor=color_map[-1], edgecolor='#aaa', linewidth=0.5, label='N/A'),
]

leg = ax.legend(handles=legend_elements, loc='upper center',
                bbox_to_anchor=(0.5, -0.04), ncol=5,
                fontsize=7, frameon=False, handlelength=1.0, handletextpad=0.3,
                columnspacing=1.0)

plt.tight_layout(rect=[0, 0.08, 1, 1])

out_path = '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/figures/cross_benchmark_heatmap.pdf'
fig.savefig(out_path, dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none', pad_inches=0.05)
print(f'Saved: {out_path}')

# Also save PNG for quick preview
png_path = out_path.replace('.pdf', '.png')
fig.savefig(png_path, dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none', pad_inches=0.05)
print(f'Saved: {png_path}')
plt.close()
