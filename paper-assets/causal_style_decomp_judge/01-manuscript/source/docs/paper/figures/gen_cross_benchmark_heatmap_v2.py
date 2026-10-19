"""
Optimized cross-benchmark heatmap: BT win probability significance matrix.
Narrative: Style bias is reproducible across benchmarks; Claude shows
benchmark-dependent (quality-driven) sensitivity.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# Data (rows: judges, cols: benchmark×axis)
# Rows: GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash, Claude Sonnet 4
# Cols: LLMBar-Form, LLMBar-Verb, LLMBar-Reg, AEval-Form, AEval-Verb, MTB-Form
bt_values = [
    [0.630, 0.760, 0.570, 0.727, None,  0.692],
    [0.665, 0.773, 0.553, 0.657, 0.841, 0.712],
    [0.695, 0.735, 0.635, 0.756, None,  None ],
    [0.574, 0.708, None,  None,  None,  None ],
    [0.562, 0.541, None,  0.698, 0.683, 0.733],
]

# Significance levels: 3=p<.001, 2=p<.01, 1=p<.05, 0=NS, -1=not tested
sig_levels = [
    [3, 3, 1, 3, -1, 3],
    [3, 3, 0, 3, 3,  3],
    [3, 3, 2, 3, -1, -1],
    [1, 3, -1, -1, -1, -1],
    [0, 0, -1, 3, 3, 3],
]

row_labels = ['GPT-4o', 'Qwen3-32B', 'Llama-3.3-70B', 'Gemini-2.5-Flash', 'Claude Sonnet 4']
col_labels = ['LLMBar\nForm.', 'LLMBar\nVerb.', 'LLMBar\nReg.', 'AEval\nForm.', 'AEval\nVerb.', 'MTB\nForm.']

nrows = len(row_labels)
ncols = len(col_labels)

# Color scheme: significance → blue intensity
color_map = {
    3:  '#1B4F72',   # p<.001 — dark blue
    2:  '#2874A6',   # p<.01
    1:  '#7FB3D8',   # p<.05
    0:  '#EBF5FB',   # NS
    -1: '#E5E8E8',   # not tested
}

fig, ax = plt.subplots(figsize=(4.6, 2.1))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

cell_gap = 0.06

for i in range(nrows):
    for j in range(ncols):
        sig = sig_levels[i][j]
        bt = bt_values[i][j]
        color = color_map[sig]

        x0 = j + cell_gap / 2
        y0 = (nrows - 1 - i) + cell_gap / 2
        w = 1 - cell_gap
        h = 1 - cell_gap

        rect = mpatches.FancyBboxPatch(
            (x0, y0), w, h,
            boxstyle='round,pad=0.02,rounding_size=0.08',
            facecolor=color, edgecolor='white', linewidth=0.8,
            zorder=2)
        ax.add_patch(rect)

        if sig == -1:
            cx, cy = j + 0.5, nrows - 1 - i + 0.5
            ax.plot([j + 0.22, j + 0.78], [nrows - 1 - i + 0.22, nrows - 1 - i + 0.78],
                    color='#B0B0B0', lw=0.8, zorder=3)
            ax.plot([j + 0.22, j + 0.78], [nrows - 1 - i + 0.78, nrows - 1 - i + 0.22],
                    color='#B0B0B0', lw=0.8, zorder=3)
            continue

        text_color = 'white' if sig >= 2 else '#2C3E50'
        fw = 'bold' if sig >= 2 else 'normal'
        ax.text(j + 0.5, nrows - 1 - i + 0.5,
                f'.{int(bt * 1000):03d}',
                ha='center', va='center',
                fontsize=8.5, fontfamily='sans-serif',
                fontweight=fw, color=text_color, zorder=4)

ax.set_xlim(0, ncols)
ax.set_ylim(0, nrows)
ax.set_xticks([j + 0.5 for j in range(ncols)])
ax.set_xticklabels(col_labels, fontsize=7.5, ha='center')
ax.set_yticks([nrows - 1 - i + 0.5 for i in range(nrows)])
ax.set_yticklabels(row_labels, fontsize=8)
ax.tick_params(axis='both', which='both', length=0, pad=4)
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')

for spine in ax.spines.values():
    spine.set_visible(False)

legend_elements = [
    mpatches.Patch(facecolor=color_map[3],  edgecolor='#CCC', linewidth=0.4, label='$p<.001$'),
    mpatches.Patch(facecolor=color_map[2],  edgecolor='#CCC', linewidth=0.4, label='$p<.01$'),
    mpatches.Patch(facecolor=color_map[1],  edgecolor='#CCC', linewidth=0.4, label='$p<.05$'),
    mpatches.Patch(facecolor=color_map[0],  edgecolor='#CCC', linewidth=0.4, label='NS'),
    mpatches.Patch(facecolor=color_map[-1], edgecolor='#CCC', linewidth=0.4, label='N/A'),
]

leg = ax.legend(handles=legend_elements, loc='upper center',
                bbox_to_anchor=(0.5, -0.03), ncol=5,
                fontsize=7, frameon=False, handlelength=1.0,
                handletextpad=0.3, columnspacing=1.0)

plt.tight_layout(rect=[0, 0.08, 1, 1])

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/figures'
fig.savefig(f'{out_dir}/cross_benchmark_heatmap.pdf', dpi=300,
            bbox_inches='tight', facecolor='white', edgecolor='none', pad_inches=0.05)
fig.savefig(f'{out_dir}/cross_benchmark_heatmap.png', dpi=300,
            bbox_inches='tight', facecolor='white', edgecolor='none', pad_inches=0.05)
plt.close()
print('Saved: cross_benchmark_heatmap.pdf + .png')
