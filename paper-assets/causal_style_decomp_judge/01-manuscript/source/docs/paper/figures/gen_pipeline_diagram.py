"""
CSD Pipeline Diagram (Figure 1, Hero Figure).
Five-stage pipeline with semantic coloring and visual hierarchy.
Designed at 7.0" for \\textwidth (~6.5") in EMNLP two-column format.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'savefig.dpi': 300,
})

# --- Layout ---
fig_w, fig_h = 7.0, 1.58
n_boxes = 5
box_w = 1.14
box_h = 1.20
gap_x = 0.22
total_w = n_boxes * box_w + (n_boxes - 1) * gap_x
x_start = (fig_w - total_w) / 2
y_center = fig_h / 2

# --- Semantic colors (project palette) ---
STAGE = [
    {'fill': '#F2F5F9', 'accent': '#4E79A7', 'border': '#CBD5E1'},  # Source
    {'fill': '#FEF4ED', 'accent': '#E15759', 'border': '#F0CDB0'},  # Generation
    {'fill': '#EBF5EC', 'accent': '#3D9140', 'border': '#A5D6A7'},  # NLI Gate ★
    {'fill': '#F2ECF7', 'accent': '#8E6AAF', 'border': '#C9B4DB'},  # Scoring
    {'fill': '#F2F5F9', 'accent': '#4E79A7', 'border': '#CBD5E1'},  # Analysis
]

boxes_data = [
    ('1', 'Source\nData',               'LLMBar Natural +\nAdversarial',   '$n{=}100$'),
    ('2', 'Counterfactual\nGeneration', 'Qwen3-32B\nstyle rewriter',      'formal $\\leftrightarrow$ casual'),
    ('3', 'NLI Content\nVerification',  'DeBERTa-v3-large',               'threshold $\\geq$ 0.90'),
    ('4', 'Dual Pairwise\nScoring',     'LLM Judge\n(A/B swap)',           '2 trials per pair'),
    ('5', 'Statistical\nAnalysis',      'BT model + GEE\ndecomposition',   '+ Likert comparison'),
]

arrow_labels = ['$n{=}100$', '100 cf.', '88 pass', '173 comp.']

fig, ax = plt.subplots(figsize=(fig_w, fig_h))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, fig_w)
ax.set_ylim(0, fig_h)
ax.axis('off')

# --- Subtle horizontal connector line behind boxes ---
conn_y = y_center
conn_x0 = x_start + box_w / 2
conn_x1 = x_start + (n_boxes - 1) * (box_w + gap_x) + box_w / 2
ax.plot([conn_x0, conn_x1], [conn_y, conn_y],
        color='#E0E0E0', linewidth=1.5, zorder=0,
        solid_capstyle='round')

box_rects = []
for i, (num, title, detail, extra) in enumerate(boxes_data):
    sc = STAGE[i]
    x = x_start + i * (box_w + gap_x)
    y = y_center - box_h / 2
    box_rects.append((x, y, x + box_w, y + box_h))

    is_key = (i == 2)
    lw = 1.4 if is_key else 0.5

    # Two-layer shadow for depth
    for s_off, s_alpha in [(0.012, 0.02), (0.006, 0.012)]:
        shadow = FancyBboxPatch(
            (x + s_off, y - s_off), box_w, box_h,
            boxstyle='round,pad=0.02,rounding_size=0.055',
            facecolor='#000000', edgecolor='none', alpha=s_alpha, zorder=1)
        ax.add_patch(shadow)

    # Main box
    box = FancyBboxPatch(
        (x, y), box_w, box_h,
        boxstyle='round,pad=0.02,rounding_size=0.055',
        facecolor=sc['fill'], edgecolor=sc['border'], linewidth=lw, zorder=2)
    ax.add_patch(box)

    # Accent stripe at top
    accent_y = y + box_h - 0.005
    margin = 0.09
    ax.plot([x + margin, x + box_w - margin], [accent_y, accent_y],
            color=sc['accent'], linewidth=2.0 if is_key else 1.5,
            solid_capstyle='round', zorder=3, clip_on=True)

    # Number badge
    nr = 0.085
    nx = x + 0.14
    ny = y + box_h - 0.065 - nr
    badge = Circle((nx, ny), nr, facecolor=sc['accent'],
                    edgecolor='white', linewidth=0.8, zorder=4)
    ax.add_patch(badge)
    ax.text(nx, ny, num, ha='center', va='center',
            fontsize=6.5, fontweight='bold', color='white', zorder=5)

    # Title
    ax.text(x + box_w / 2, y + box_h * 0.51, title,
            ha='center', va='center', fontsize=8, fontweight='bold',
            color='#1A1A2E', zorder=3, linespacing=0.92)

    # Detail
    ax.text(x + box_w / 2, y + box_h * 0.21, detail,
            ha='center', va='center', fontsize=6.2, color='#5A5A5A',
            zorder=3, linespacing=0.95)

    # Extra
    ax.text(x + box_w / 2, y + box_h * 0.06, extra,
            ha='center', va='center', fontsize=5.5, color='#999999',
            zorder=3, fontstyle='italic')

# Arrows with flow labels
for i in range(n_boxes - 1):
    x1 = box_rects[i][2]
    x2 = box_rects[i + 1][0]
    y_arr = y_center

    arrow = FancyArrowPatch(
        (x1 + 0.015, y_arr), (x2 - 0.015, y_arr),
        arrowstyle='-|>', mutation_scale=7,
        color='#B8B8B8', linewidth=0.7, zorder=5)
    ax.add_patch(arrow)

    # Sample attrition label above arrow
    mid_x = (x1 + x2) / 2
    label_y = y_center + box_h / 2 + 0.04
    t = ax.text(mid_x, label_y, arrow_labels[i],
                ha='center', va='bottom', fontsize=5,
                color='#999999', fontstyle='italic', zorder=6)
    t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/figures'
fig.savefig(f'{out_dir}/pipeline_diagram.pdf', dpi=300,
            bbox_inches='tight', facecolor='white', edgecolor='none', pad_inches=0.02)
fig.savefig(f'{out_dir}/pipeline_diagram.png', dpi=300,
            bbox_inches='tight', facecolor='white', edgecolor='none', pad_inches=0.02)
plt.close()
print('Saved: pipeline_diagram.pdf + .png')
