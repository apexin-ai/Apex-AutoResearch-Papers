"""
Optimized forest plot: BT win probability across 4 judges × 2-3 style axes.
Narrative: Verbosity is the strongest, most consistent bias; formality is universal
but weaker; register is judge-dependent.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.lines import Line2D
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

AXIS_COLORS = {
    'Verbosity': '#E15759',
    'Formality': '#4E79A7',
    'Register':  '#76B7B2',
}

# Data grouped by judge: (axis, bt, ci_lo, ci_hi, p_str, significant)
judges = {
    'GPT-4o': [
        ('Verbosity', 0.760, 0.686, 0.826, 'p<.001', True),
        ('Formality', 0.630, 0.558, 0.703, 'p<.001', True),
        ('Register',  0.570, 0.489, 0.649, 'p=.038', True),
    ],
    'Qwen3-32B': [
        ('Verbosity', 0.773, 0.703, 0.843, 'p<.0001', True),
        ('Formality', 0.665, 0.585, 0.739, 'p<.0001', True),
        ('Register',  0.553, 0.473, 0.630, 'p=.092', False),
    ],
    'Llama-3.3-70B': [
        ('Verbosity', 0.735, 0.660, 0.805, 'p<.0001', True),
        ('Formality', 0.695, 0.618, 0.765, 'p<.0001', True),
        ('Register',  0.635, 0.555, 0.712, 'p=.0014', True),
    ],
    'Gemini-2.5-Flash': [
        ('Verbosity', 0.708, 0.637, 0.772, 'p<.0001', True),
        ('Formality', 0.574, 0.500, 0.642, 'p=.031', True),
    ],
}

fig, ax = plt.subplots(figsize=(4.0, 3.2))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Build y positions: judge header rows (no data) + axis data rows
all_rows = []  # (type, judge_name, data_or_None, y)
y = 0
judge_groups = list(judges.items())

for ji, (judge_name, axes_data) in enumerate(reversed(judge_groups)):
    group_data_start = y
    for ai, row in enumerate(reversed(axes_data)):
        all_rows.append(('data', judge_name, row, y))
        y += 1
    group_data_end = y - 1
    all_rows.append(('header', judge_name, (group_data_start, group_data_end), y + 0.05))
    y += 1.1  # gap for next group (header space + padding)

all_rows = list(reversed(all_rows))
max_y = y - 0.5

# Draw judge group backgrounds (alternating)
judge_idx = 0
for item in all_rows:
    if item[0] == 'header':
        _, judge_name, (gs, ge), yh = item
        if judge_idx % 2 == 0:
            ax.axhspan(gs - 0.42, yh + 0.15, color='#F7F7F7', zorder=0, linewidth=0)
        judge_idx += 1

# Vertical reference line at 0.50
ax.axvline(x=0.50, color='#AAAAAA', linestyle='--', linewidth=0.9, zorder=1)

# Plot each row
for item in all_rows:
    if item[0] == 'header':
        _, judge_name, (gs, ge), yh = item
        ax.text(0.44, yh, judge_name, ha='right', va='center',
                fontsize=10, fontweight='bold', color='#222222')
        continue

    _, judge_name, (axis_name, bt, ci_lo, ci_hi, p_str, sig), yval = item
    color = AXIS_COLORS[axis_name]

    # CI whisker
    ax.plot([ci_lo, ci_hi], [yval, yval], color=color, linewidth=1.5,
            solid_capstyle='round', zorder=2)

    # Diamond marker (filled if significant, open if not)
    if sig:
        ax.scatter(bt, yval, marker='D', s=40, color=color,
                   edgecolors='white', linewidths=0.5, zorder=4)
    else:
        ax.scatter(bt, yval, marker='D', s=40, facecolors='white',
                   edgecolors=color, linewidths=1.5, zorder=4)

    # Axis label (left of plot, indented)
    ax.text(0.44, yval, f'{axis_name}', ha='right', va='center',
            fontsize=9, color='#555555')

# Axis configuration
ax.set_xlim(0.45, 0.90)
ax.set_ylim(-0.6, max_y + 2.2)
ax.set_yticks([])
ax.set_xlabel('P(style-preferred wins)', fontsize=10)
ax.spines['left'].set_visible(False)

# Axis color legend (top, horizontal)
axis_patches = [
    Line2D([0], [0], color=AXIS_COLORS['Verbosity'], linewidth=2.5, label='Verbosity'),
    Line2D([0], [0], color=AXIS_COLORS['Formality'], linewidth=2.5, label='Formality'),
    Line2D([0], [0], color=AXIS_COLORS['Register'], linewidth=2.5, label='Register'),
]
leg_top = ax.legend(handles=axis_patches, loc='upper right',
                    fontsize=8, frameon=True, framealpha=0.95,
                    edgecolor='#DDDDDD', borderpad=0.4, ncol=3,
                    columnspacing=1.0, handlelength=1.5)
leg_top.get_frame().set_linewidth(0.5)

# Diamond legend (lower right, well separated from color legend above)
diamond_elements = [
    Line2D([0], [0], marker='D', color='w', markerfacecolor='#888888',
           markeredgecolor='#888888', markersize=6.5, label='Sig. ($p<.05$)'),
    Line2D([0], [0], marker='D', color='w', markerfacecolor='white',
           markeredgecolor='#888888', markersize=6.5, markeredgewidth=1.5,
           label='Not sig.'),
]
leg_bot = ax.legend(handles=diamond_elements, loc='upper right',
                    bbox_to_anchor=(1.0, -0.18),
                    fontsize=8, frameon=True, framealpha=0.95,
                    edgecolor='#DDDDDD', borderpad=0.4, ncol=2,
                    columnspacing=0.8, handlelength=1.2)
leg_bot.get_frame().set_linewidth(0.5)
ax.add_artist(leg_top)

plt.tight_layout()
fig.subplots_adjust(bottom=0.24)

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/figures'
fig.savefig(f'{out_dir}/forest_plot.pdf', facecolor='white', edgecolor='none')
fig.savefig(f'{out_dir}/forest_plot.png', facecolor='white', edgecolor='none')
plt.close()
print('Saved: forest_plot.pdf + .png')
