import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# Okabe-Ito palette
C_BLUE    = '#0072B2'
C_ORANGE  = '#E69F00'
C_GREEN   = '#009E73'
C_RED     = '#D55E00'
C_PURPLE  = '#CC79A7'
C_SKYBLUE = '#56B4E9'
C_GREY    = '#999999'
C_DARKGREY = '#555555'
C_LIGHTGREY = '#E0E0E0'

def draw_rounded_box(ax, x, y, w, h, text, facecolor='#EBF5FB',
                     edgecolor=C_BLUE, fontsize=10, textcolor='black',
                     linewidth=1.2, fontstyle='normal', fontweight='normal',
                     alpha=1.0, zorder=3):
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle="round,pad=0.03",
                          facecolor=facecolor, edgecolor=edgecolor,
                          linewidth=linewidth, alpha=alpha, zorder=zorder)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            color=textcolor, fontstyle=fontstyle, fontweight=fontweight,
            zorder=zorder+1)
    return box

def draw_arrow(ax, x1, y1, x2, y2, color='#333333', linewidth=1.2,
               arrowstyle='->', mutation_scale=12, zorder=2):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                             arrowstyle=arrowstyle,
                             mutation_scale=mutation_scale,
                             color=color, linewidth=linewidth, zorder=zorder)
    ax.add_patch(arrow)
    return arrow

# ── Figure ──
fig = plt.figure(figsize=(6.75, 2.5))

# Manual gridspec for more control
gs = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.55, 0.95], wspace=0.45,
                      left=0.01, right=0.99, top=0.92, bottom=0.04)
ax_a = fig.add_subplot(gs[0])
ax_b = fig.add_subplot(gs[1])
ax_c = fig.add_subplot(gs[2])

for ax in (ax_a, ax_b, ax_c):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

# ═══════════════════════════════════════════════════════
# Panel (a): Formalization Pipeline (vertical layout)
# ═══════════════════════════════════════════════════════
ax_a.set_title('(a) Formalization Pipeline', fontsize=9.5, fontweight='bold', pad=4)

steps_a = [
    ('NL Problem',                '#FFF3E0', C_ORANGE),
    ('LLM Formalizer (Qwen3-4B)', '#E3F2FD', C_BLUE),
    ('Formal Logic (FOL/Prolog)', '#E8F5E9', C_GREEN),
    ('Solver (Prover9/SWI)',     '#F3E5F5', C_PURPLE),
    ('Pass ✓ / Fail ✗',           '#F5F5F5', C_DARKGREY),
]

box_w_a = 8.5
box_h_a = 1.3
x_mid_a = 5.0
y_positions_a = [9.0, 7.2, 5.4, 3.6, 1.8]

for i, (label, fc, ec) in enumerate(steps_a):
    fw = 'bold' if i == len(steps_a) - 1 else 'normal'
    draw_rounded_box(ax_a, x_mid_a, y_positions_a[i], box_w_a, box_h_a, label,
                     facecolor=fc, edgecolor=ec, fontsize=7.5, fontweight=fw)

for i in range(len(y_positions_a) - 1):
    draw_arrow(ax_a, x_mid_a, y_positions_a[i] - box_h_a/2 - 0.08,
               x_mid_a, y_positions_a[i+1] + box_h_a/2 + 0.08,
               color=C_DARKGREY, linewidth=1.5, mutation_scale=14)

# ═══════════════════════════════════════════════════════
# Panel (b): Solver Trace Ablation
# ═══════════════════════════════════════════════════════
ax_b.set_xlim(0, 12)
ax_b.set_ylim(0, 10)
ax_b.set_title('(b) Solver Trace Ablation', fontsize=9.5, fontweight='bold', pad=4)

comp_labels = ['c₁', 'c₂', 'c₃', 'c₄']
ablation_results = [
    ('c₁', True),   # necessary (Fail when removed)
    ('c₂', False),  # redundant (Pass when removed)
    ('c₃', True),   # necessary
    ('c₄', False),  # redundant
]

# -- Left column: Original formalization --
orig_x = 1.0
orig_top = 8.4
row_gap = 1.45
comp_w = 1.4
comp_h = 0.85

ax_b.text(orig_x, 9.45, 'Formalization', ha='center', va='center',
          fontsize=7.5, fontweight='bold', color=C_DARKGREY)

for i, label in enumerate(comp_labels):
    yy = orig_top - i * row_gap
    draw_rounded_box(ax_b, orig_x, yy, comp_w, comp_h, label,
                     facecolor='#E3F2FD', edgecolor=C_BLUE, fontsize=8)

conc_y = orig_top - len(comp_labels) * row_gap
draw_rounded_box(ax_b, orig_x, conc_y, comp_w, comp_h, 'concl.',
                 facecolor='#FFF8E1', edgecolor=C_ORANGE, fontsize=7)

# -- Right column: LOO ablation rows --
abl_start_x = 3.3
mini_w = 0.85
mini_h = 0.75
mini_gap = 1.0
solver_x = 8.0
result_x = 10.7

ax_b.text(6.5, 9.45, 'Leave-One-Out Ablation', ha='center', va='center',
          fontsize=7.5, fontweight='bold', color=C_DARKGREY)

for row_idx, (removed, is_necessary) in enumerate(ablation_results):
    yy = orig_top - row_idx * row_gap

    # Draw mini components
    for ci in range(4):
        cx = abl_start_x + ci * mini_gap
        label = comp_labels[ci]
        if label == removed:
            draw_rounded_box(ax_b, cx, yy, mini_w, mini_h, label,
                             facecolor=C_LIGHTGREY, edgecolor=C_GREY,
                             fontsize=7, textcolor=C_GREY, linewidth=0.7)
            ax_b.plot([cx - mini_w/2 + 0.05, cx + mini_w/2 - 0.05],
                      [yy, yy], color=C_RED, linewidth=1.8, zorder=5)
        else:
            draw_rounded_box(ax_b, cx, yy, mini_w, mini_h, label,
                             facecolor='#E3F2FD', edgecolor=C_BLUE,
                             fontsize=7, linewidth=0.7)

    # Arrow to solver
    last_comp_x = abl_start_x + 3 * mini_gap + mini_w/2
    draw_arrow(ax_b, last_comp_x + 0.15, yy,
               solver_x - 0.65, yy, color=C_DARKGREY, linewidth=0.9,
               mutation_scale=8)

    # Solver box
    draw_rounded_box(ax_b, solver_x, yy, 1.15, mini_h, 'Solver',
                     facecolor='#F3E5F5', edgecolor=C_PURPLE, fontsize=7,
                     linewidth=0.7)

    # Arrow to result
    draw_arrow(ax_b, solver_x + 0.65, yy,
               result_x - 0.55, yy, color=C_DARKGREY, linewidth=0.9,
               mutation_scale=8)

    # Result text
    if is_necessary:
        ax_b.text(result_x, yy + 0.22, '✗ Fail', ha='center', va='center',
                  fontsize=7, color=C_RED, fontweight='bold')
        ax_b.text(result_x, yy - 0.22, 'necessary', ha='center', va='center',
                  fontsize=6.5, color=C_RED, fontstyle='italic')
    else:
        ax_b.text(result_x, yy + 0.22, '✓ Pass', ha='center', va='center',
                  fontsize=7, color=C_GREEN, fontweight='bold')
        ax_b.text(result_x, yy - 0.22, 'redundant', ha='center', va='center',
                  fontsize=6.5, color=C_GREEN, fontstyle='italic')

# ISR formula at bottom
ax_b.text(6.0, 0.7,
          'ISR = $\\frac{n_{\\mathrm{necessary}}}{n_{\\mathrm{total}}}$'
          ' = $\\frac{2}{4}$ = 0.50',
          ha='center', va='center', fontsize=8.5,
          bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF8E1',
                    edgecolor=C_ORANGE, linewidth=1.0),
          zorder=5)

# ═══════════════════════════════════════════════════════
# Panel (c): Diagnostic vs Reward (Goodhart)
# ═══════════════════════════════════════════════════════
ax_c.set_title('(c) Diagnostic → Reward: Goodhart', fontsize=9.5, fontweight='bold', pad=4)

# Upper section: Diagnostic (green)
diag_y = 7.8
draw_rounded_box(ax_c, 5.0, diag_y, 9.5, 1.6, '',
                 facecolor='#E8F5E9', edgecolor=C_GREEN, fontsize=8,
                 linewidth=1.2)
ax_c.text(5.0, diag_y + 0.28, '✓  ISR as Diagnostic', ha='center', va='center',
          fontsize=8, fontweight='bold', color=C_GREEN)
ax_c.text(5.0, diag_y - 0.32, 'Post-hoc quality audit', ha='center',
          va='center', fontsize=7, color=C_DARKGREY)

# Sub-text
ax_c.text(5.0, 6.2, 'Detects hacking invisible to PR',
          ha='center', va='center', fontsize=7, color=C_DARKGREY, fontstyle='italic')

# Goodhart arrow
draw_arrow(ax_c, 5.0, 5.7, 5.0, 4.2,
           color=C_RED, linewidth=2.0, mutation_scale=15, arrowstyle='->')

# "Goodhart's Law" label
ax_c.text(5.0, 5.0, "Goodhart's Law",
          ha='center', va='center', fontsize=7.5, fontweight='bold',
          color=C_RED,
          bbox=dict(boxstyle='round,pad=0.22', facecolor='#FFF0F0',
                    edgecolor=C_RED, linewidth=0.7, alpha=0.95))

# Lower section: Reward (red)
rew_y = 2.8
draw_rounded_box(ax_c, 5.0, rew_y, 9.5, 1.6, '',
                 facecolor='#FBE9E7', edgecolor=C_RED, fontsize=8,
                 linewidth=1.2)
ax_c.text(5.0, rew_y + 0.28, '✗  ISR as Reward Signal', ha='center', va='center',
          fontsize=8, fontweight='bold', color=C_RED)
ax_c.text(5.0, rew_y - 0.32,
          '$r = r_{\\mathrm{exec}} \\cdot (1 + \\beta \\cdot \\mathrm{ISR})$',
          ha='center', va='center', fontsize=8, color=C_DARKGREY)

# Sub-text
ax_c.text(5.0, 1.2, 'Model games ISR (meta-Goodhart)',
          ha='center', va='center', fontsize=7, color=C_RED, fontstyle='italic')

# ── Save ──

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/figures/paper'
canonical = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures'
plt.savefig(f'{outdir}/fig1_sta_overview.pdf')
plt.savefig(f'{outdir}/fig1_sta_overview.png')
plt.savefig(f'{canonical}/fig1_sta_overview.pdf')
plt.savefig(f'{canonical}/fig1_sta_overview.png')
plt.close()

print('Done.')
