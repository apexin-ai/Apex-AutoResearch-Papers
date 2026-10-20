import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# Okabe-Ito palette
OI_GREEN  = '#009E73'
OI_BLUE   = '#0072B2'
OI_GRAY   = '#999999'
OI_ORANGE = '#E69F00'
OI_VERMIL = '#D55E00'
OI_PURPLE = '#CC79A7'
OI_SKYBLUE = '#56B4E9'
OI_BLACK  = '#000000'

BG_PART1 = '#F5F5F0'
BG_PART2 = '#F0F4F5'
BG_PART3 = '#F5F0F0'

fig, ax = plt.subplots(figsize=(14, 6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_aspect('equal')

def draw_box(ax, xy, w, h, text, fc='white', ec='#444444', lw=1.2, fontsize=10,
             fontweight='normal', text_color='black', style='round,pad=0.1', zorder=3):
    box = FancyBboxPatch(xy, w, h, boxstyle=style, facecolor=fc, edgecolor=ec,
                         linewidth=lw, zorder=zorder, mutation_scale=0.3)
    ax.add_patch(box)
    cx = xy[0] + w / 2
    cy = xy[1] + h / 2
    ax.text(cx, cy, text, ha='center', va='center', fontsize=fontsize,
            fontweight=fontweight, color=text_color, zorder=zorder + 1)
    return box

def draw_arrow(ax, posA, posB, color='#555555', lw=1.5, style='->', zorder=2,
               connectionstyle='arc3,rad=0.0', shrinkA=3, shrinkB=3):
    arrow = FancyArrowPatch(posA, posB, arrowstyle=style, color=color,
                            linewidth=lw, connectionstyle=connectionstyle,
                            shrinkA=shrinkA, shrinkB=shrinkB, zorder=zorder,
                            mutation_scale=14)
    ax.add_patch(arrow)
    return arrow

def draw_section_bg(ax, xy, w, h, fc, label, label_y_offset=0.15):
    bg = FancyBboxPatch(xy, w, h, boxstyle='round,pad=0.15', facecolor=fc,
                        edgecolor='#CCCCCC', linewidth=0.8, zorder=0, alpha=0.7)
    ax.add_patch(bg)
    ax.text(xy[0] + w / 2, xy[1] + h - label_y_offset, label,
            ha='center', va='top', fontsize=9, fontweight='bold', color='#666666', zorder=1)

# ── Section backgrounds ──
draw_section_bg(ax, (0.15, 0.2), 3.4, 5.5, BG_PART1, 'Data Preparation')
draw_section_bg(ax, (3.75, 0.2), 4.3, 5.5, BG_PART2, 'Weak Supervision')
draw_section_bg(ax, (8.25, 0.2), 5.55, 5.5, BG_PART3, 'Detection Methods')

# ════════════════════════════════════════════════
# PART 1: Data Preparation
# ════════════════════════════════════════════════

# Agent Trajectory box
draw_box(ax, (0.4, 3.7), 2.9, 0.9, '', fc='white', ec='#555555', lw=1.3)
ax.text(1.85, 4.4, 'Agent Trajectory', ha='center', va='center', fontsize=10.5,
        fontweight='bold', color=OI_BLACK, zorder=4)
ax.text(1.85, 3.95, r'$(a_1, a_2, \ldots, a_n)$', ha='center', va='center',
        fontsize=10, color='#444444', zorder=4, style='italic')

# Arrow down
draw_arrow(ax, (1.85, 3.7), (1.85, 3.1), color='#555555', lw=1.3)

# Sliding Window box
draw_box(ax, (0.5, 2.2), 2.7, 0.9, '', fc='white', ec='#555555', lw=1.3)
ax.text(1.85, 2.85, 'Sliding Window', ha='center', va='center', fontsize=10.5,
        fontweight='bold', color=OI_BLACK, zorder=4)
ax.text(1.85, 2.45, r'$k = 5$ steps', ha='center', va='center',
        fontsize=9.5, color='#666666', zorder=4)

# Small illustration of sliding window (5 mini-boxes)
for i in range(7):
    x0 = 0.7 + i * 0.32
    fc = OI_SKYBLUE if 1 <= i <= 5 else '#E8E8E8'
    ec_c = OI_BLUE if 1 <= i <= 5 else '#BBBBBB'
    rect = FancyBboxPatch((x0, 1.15), 0.28, 0.55, boxstyle='round,pad=0.04',
                          facecolor=fc, edgecolor=ec_c, linewidth=0.8, zorder=3, alpha=0.7)
    ax.add_patch(rect)
    ax.text(x0 + 0.14, 1.42, f'$a_{{{i+1}}}$', ha='center', va='center',
            fontsize=7.5, color='#333333', zorder=4)

# Bracket under sliding window selection
ax.annotate('', xy=(1.02, 1.05), xytext=(2.78, 1.05),
            arrowprops=dict(arrowstyle='-', color=OI_BLUE, lw=1.0))
ax.plot([1.02, 1.02], [1.05, 1.12], color=OI_BLUE, lw=1.0, zorder=3)
ax.plot([2.78, 2.78], [1.05, 1.12], color=OI_BLUE, lw=1.0, zorder=3)
ax.text(1.9, 0.92, 'window', ha='center', va='center', fontsize=8,
        color=OI_BLUE, zorder=4)

# Arrow from Part1 to Part2
draw_arrow(ax, (3.3, 2.65), (4.1, 3.25), color='#555555', lw=1.3,
           connectionstyle='arc3,rad=-0.1')

# ════════════════════════════════════════════════
# PART 2: Weak Supervision
# ════════════════════════════════════════════════

lf_x = 4.1
lf_w = 2.7
lf_h = 0.65
lf_gap = 0.15

lf_labels = [
    (r'$\lambda_1$: Command Repetition', OI_ORANGE),
    (r'$\lambda_2$: File Diff Delta', OI_VERMIL),
    (r'$\lambda_3$: Outcome Backprop.', OI_PURPLE),
]

lf_centers = []
for i, (label, color) in enumerate(lf_labels):
    y = 4.2 - i * (lf_h + lf_gap)
    draw_box(ax, (lf_x, y), lf_w, lf_h, '', fc='white', ec=color, lw=1.5)
    ax.text(lf_x + lf_w / 2, y + lf_h / 2, label, ha='center', va='center',
            fontsize=9.5, color='#333333', zorder=4)
    lf_centers.append((lf_x + lf_w, y + lf_h / 2))

# "Labeling Functions" title
ax.text(lf_x + lf_w / 2, 5.05, 'Labeling Functions', ha='center', va='center',
        fontsize=10, fontweight='bold', color='#555555', zorder=4)

# Majority Vote box
mv_x = 4.6
mv_y = 1.5
mv_w = 1.7
mv_h = 0.7
draw_box(ax, (mv_x, mv_y), mv_w, mv_h, '', fc='#FAFAFA', ec='#555555', lw=1.3)
ax.text(mv_x + mv_w / 2, mv_y + mv_h / 2 + 0.1, 'Majority Vote', ha='center',
        va='center', fontsize=9.5, fontweight='bold', color=OI_BLACK, zorder=4)
ax.text(mv_x + mv_w / 2, mv_y + mv_h / 2 - 0.15, '→ Silver Labels', ha='center',
        va='center', fontsize=8.5, color='#666666', zorder=4)

# Arrows from LFs to Majority Vote
for cx, cy in lf_centers:
    draw_arrow(ax, (cx - 0.05, cy), (mv_x + mv_w / 2, mv_y + mv_h),
               color='#888888', lw=1.0, connectionstyle='arc3,rad=0.0')

# Confidence annotation
ax.text(mv_x + mv_w / 2, mv_y - 0.15, 'confidence ∈ {1, 2, 3}', ha='center',
        va='center', fontsize=8, color='#888888', style='italic', zorder=4)

# Arrow from Part2 to Part3
draw_arrow(ax, (mv_x + mv_w, mv_y + mv_h / 2), (8.6, mv_y + mv_h / 2),
           color='#555555', lw=1.3)

# ════════════════════════════════════════════════
# PART 3: Detection Methods
# ════════════════════════════════════════════════

method_x = 8.6
method_w = 3.0
method_h = 0.55
result_x = 11.9
result_w = 1.6

methods = [
    {
        'name': 'Structural Features',
        'detail': '30-dim → RF / GB',
        'result': 'F1: 0.995',
        'color': OI_GREEN,
        'lw': 2.8,
        'y': 4.4,
    },
    {
        'name': 'NL Embedding Probe',
        'detail': 'GRU → Binary clf.',
        'result': 'F1: 0.906',
        'color': OI_BLUE,
        'lw': 2.0,
        'y': 3.0,
    },
    {
        'name': 'LLM-as-Judge',
        'detail': 'Claude → Zero-shot',
        'result': 'F1: 0.663',
        'color': OI_GRAY,
        'lw': 1.2,
        'y': 1.6,
    },
]

for m in methods:
    y = m['y']
    c = m['color']
    lw = m['lw']

    # Method box
    draw_box(ax, (method_x, y), method_w, method_h * 1.6, '', fc='white', ec=c, lw=lw)
    ax.text(method_x + method_w / 2, y + method_h * 1.6 / 2 + 0.12, m['name'],
            ha='center', va='center', fontsize=10, fontweight='bold', color='#333333', zorder=4)
    ax.text(method_x + method_w / 2, y + method_h * 1.6 / 2 - 0.14, m['detail'],
            ha='center', va='center', fontsize=8.5, color='#666666', zorder=4)

    # Arrow to result
    draw_arrow(ax, (method_x + method_w, y + method_h * 1.6 / 2),
               (result_x, y + method_h * 1.6 / 2),
               color=c, lw=lw * 0.7, style='->')

    # Result box
    draw_box(ax, (result_x, y + 0.08), result_w, method_h * 1.2, m['result'],
             fc='white', ec=c, lw=lw, fontsize=10.5, fontweight='bold', text_color=c)

# Arrow from silver labels into each method (branching)
branch_start = (8.45, mv_y + mv_h / 2)
for i, m in enumerate(methods):
    y = m['y'] + method_h * 1.6 / 2
    if m['name'] == 'LLM-as-Judge':
        # Dashed arrow for LLM-as-Judge (eval only, not trained on silver labels)
        arrow = FancyArrowPatch(branch_start, (method_x, y), arrowstyle='->',
                                color='#AAAAAA', linewidth=1.0,
                                connectionstyle='arc3,rad=0.0',
                                linestyle='--', shrinkA=3, shrinkB=3,
                                zorder=2, mutation_scale=14)
        ax.add_patch(arrow)
        # "eval only" annotation
        mid_x = (branch_start[0] + method_x) / 2 - 0.1
        mid_y = (branch_start[1] + y) / 2
        ax.text(mid_x, mid_y - 0.25, 'eval only', ha='center', va='center',
                fontsize=7.5, color='#888888', style='italic', zorder=4)
    else:
        draw_arrow(ax, branch_start, (method_x, y), color='#AAAAAA', lw=1.0,
                   connectionstyle='arc3,rad=0.0', style='->')

# ── Save ──
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/figures/paper'
fig.savefig(f'{out_dir}/fig_pipeline.pdf', format='pdf')
fig.savefig(f'{out_dir}/fig_pipeline.png', format='png')
plt.close(fig)
print('Done.')
