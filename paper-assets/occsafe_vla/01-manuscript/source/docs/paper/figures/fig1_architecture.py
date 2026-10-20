"""
fig1_architecture.py — Panels (a) Training Setup + (b) Factorial Design.
Split from fig1_overview.py; data unchanged.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

COLORS = {
    'vanilla':     '#4C72B0',
    'full_occ_bn': '#C44E52',
    'full_occ_ln': '#E69F00',
    'random_occ':  '#55A868',
    'detach_bn':   '#8172B3',
    'detach_ln':   '#937860',
    'depth':       '#CCB974',
    'cutoff':      '#64B5CD',
}

UI = {
    'text':         '#2C3E50',
    'subtle':       '#95A5A6',
    'encoder_fill': '#EEF2F8',
    'encoder_edge': '#4C72B0',
    'llm_fill':     '#F6F2EC',
    'llm_edge':     '#937860',
    'head_fill':    '#FFF6E8',
    'head_edge':    '#E69F00',
    'action_fill':  '#EDF7EE',
    'action_edge':  '#55A868',
    'grid':         '#DEE2E6',
}

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 15,
    'text.color': UI['text'],
    'axes.labelcolor': UI['text'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'mathtext.fontset': 'cm',
})

fig = plt.figure(figsize=(14.5, 5.5), dpi=300, facecolor='white')

ax_a = fig.add_axes([0.015, 0.06, 0.46, 0.86])
ax_b = fig.add_axes([0.52, 0.06, 0.44, 0.86])

for ax in [ax_a, ax_b]:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')


def draw_box(ax, xy, w, h, label, sublabel=None, fill='white', edge='#333',
             fontsize=15, lw=1.4, radius=0.18, shadow=True):
    if shadow:
        shadow_box = FancyBboxPatch(
            (xy[0] + 0.04, xy[1] - 0.04), w, h,
            boxstyle=f"round,pad=0,rounding_size={radius}",
            facecolor='#00000008', edgecolor='none', linewidth=0, zorder=2)
        ax.add_patch(shadow_box)
    box = FancyBboxPatch(xy, w, h, boxstyle=f"round,pad=0,rounding_size={radius}",
                         facecolor=fill, edgecolor=edge, linewidth=lw, zorder=3)
    ax.add_patch(box)
    cx, cy = xy[0] + w/2, xy[1] + h/2
    if sublabel:
        ax.text(cx, cy + 0.22, label, ha='center', va='center', fontsize=fontsize,
                fontweight='bold', color=UI['text'], zorder=4)
        ax.text(cx, cy - 0.28, sublabel, ha='center', va='center', fontsize=14,
                color=UI['subtle'], zorder=4, style='italic')
    else:
        ax.text(cx, cy, label, ha='center', va='center', fontsize=fontsize,
                fontweight='bold', color=UI['text'], zorder=4)


def draw_arrow(ax, start, end, color='#555', lw=1.2, style='->', mutation=11):
    arrow = FancyArrowPatch(start, end, arrowstyle=style, color=color,
                            linewidth=lw, mutation_scale=mutation, zorder=2)
    ax.add_patch(arrow)


# ============================================================
# PANEL (a): Training Architecture
# ============================================================
ax_a.text(0.1, 9.6, '(a) Training Setup', fontsize=16, fontweight='bold',
          va='top', color=UI['text'])

draw_box(ax_a, (3.2, 0.3), 3.6, 1.1, 'RGB Observation', fill='#F0F4F8',
         edge=UI['subtle'], fontsize=14)
draw_box(ax_a, (1.0, 2.4), 3.0, 1.0, 'DINOv2', sublabel='1024-d patches',
         fill=UI['encoder_fill'], edge=UI['encoder_edge'])
draw_box(ax_a, (5.5, 2.4), 3.0, 1.0, 'SigLIP', sublabel='1152-d patches',
         fill=UI['encoder_fill'], edge=UI['encoder_edge'])
draw_arrow(ax_a, (4.2, 1.4), (2.5, 2.4), color=UI['encoder_edge'])
draw_arrow(ax_a, (5.8, 1.4), (7.0, 2.4), color=UI['encoder_edge'])

draw_box(ax_a, (2.5, 4.2), 5.0, 1.0, 'LLM Backbone', sublabel='Llama-2 7B + LoRA',
         fill=UI['llm_fill'], edge=UI['llm_edge'])
draw_arrow(ax_a, (2.5, 3.4), (4.0, 4.2), color='#666')
draw_arrow(ax_a, (7.0, 3.4), (6.0, 4.2), color='#666')
ax_a.text(5.0, 3.75, 'concat (2176-d)', fontsize=14, ha='center',
          color=UI['subtle'], style='italic')

draw_box(ax_a, (1.5, 6.0), 3.0, 1.0, 'Action Head', sublabel='7-DoF tokens',
         fill=UI['action_fill'], edge=UI['action_edge'])
draw_arrow(ax_a, (3.5, 5.2), (3.0, 6.0), color=UI['action_edge'], lw=1.8)
ax_a.text(1.5, 7.3, r'$\mathcal{L}_{\mathrm{action}}$', fontsize=15,
          ha='center', color=UI['action_edge'], fontweight='bold')
draw_arrow(ax_a, (2.2, 7.2), (2.5, 7.0), color=UI['action_edge'], lw=1.3)

draw_box(ax_a, (6.0, 6.0), 3.0, 1.0, 'Aux Head', sublabel='BEV / Depth',
         fill=UI['head_fill'], edge=UI['head_edge'])
draw_arrow(ax_a, (6.5, 5.2), (7.5, 6.0), color=UI['head_edge'], lw=1.8)
ax_a.text(8.7, 7.3, r'$\lambda(t) \cdot \mathcal{L}_{\mathrm{aux}}$',
          fontsize=15, ha='center', color=UI['head_edge'], fontweight='bold')
draw_arrow(ax_a, (8.3, 7.2), (8.0, 7.0), color=UI['head_edge'], lw=1.3)

ax_a.text(9.25, 6.15, 'BN/LN', fontsize=14, ha='center',
          color=COLORS['full_occ_bn'], fontweight='bold',
          bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                    edgecolor=COLORS['full_occ_bn'], lw=1.3))

ax_a.annotate('', xy=(7.2, 3.5), xytext=(7.5, 5.95),
              arrowprops=dict(arrowstyle='->', color=COLORS['full_occ_bn'],
                              lw=1.8, linestyle=(0, (4, 3)),
                              connectionstyle='arc3,rad=-0.12'))
ax_a.text(8.8, 4.5, 'gradient\nflow?', fontsize=15, ha='center',
          color=COLORS['full_occ_bn'], fontweight='bold', style='italic',
          bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF0F0',
                    edgecolor=COLORS['full_occ_bn'], lw=1.0, alpha=0.85))

ax_a.text(7.5, 8.4, 'discarded at inference', fontsize=14,
          ha='center', color='#7F8C8D', style='italic',
          bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF8E1',
                    edgecolor='#BDC3C7', lw=0.8, alpha=0.9))
draw_arrow(ax_a, (7.5, 8.1), (7.5, 7.0), color=UI['subtle'],
           lw=0.7, style='->')


# ============================================================
# PANEL (b): 2x2 Factorial Design
# ============================================================
ax_b.text(0.1, 9.6, '(b) Factorial Design', fontsize=16, fontweight='bold',
          va='top', color=UI['text'])

mx, my = 1.5, 4.0
mw, mh = 7.0, 4.4
cell_w, cell_h = mw / 2, mh / 2

ax_b.text(mx + cell_w * 0.5, my + mh + 0.5, 'Gradient ON',
          ha='center', fontsize=15, fontweight='bold', color=COLORS['full_occ_bn'])
ax_b.text(mx + cell_w * 1.5, my + mh + 0.5, 'Gradient OFF',
          ha='center', fontsize=15, fontweight='bold', color=COLORS['detach_bn'])
ax_b.text(mx - 0.2, my + cell_h * 1.5, 'BN',
          ha='right', va='center', fontsize=15, fontweight='bold', color=UI['text'])
ax_b.text(mx - 0.2, my + cell_h * 0.5, 'LN',
          ha='right', va='center', fontsize=15, fontweight='bold', color=UI['text'])

cells_b = [
    (0, 1, 'Full OCC',      'full_occ_bn', '#FEF0EE'),
    (1, 1, 'Detach OCC',    'detach_bn',   '#F1EEF7'),
    (0, 0, 'Full OCC+LN',   'full_occ_ln', '#FFF7E8'),
    (1, 0, 'Detach+LN',     'detach_ln',   '#F5F0EB'),
]

border_shadow = FancyBboxPatch((mx + 0.04, my - 0.04), mw, mh,
                               boxstyle="round,pad=0,rounding_size=0.2",
                               facecolor='#00000008', edgecolor='none', linewidth=0, zorder=1)
ax_b.add_patch(border_shadow)
border = FancyBboxPatch((mx, my), mw, mh, boxstyle="round,pad=0,rounding_size=0.2",
                         facecolor='none', edgecolor='#BDC3C7', linewidth=0.9, zorder=2)
ax_b.add_patch(border)
ax_b.plot([mx, mx + mw], [my + cell_h, my + cell_h],
          color=UI['grid'], lw=0.6, zorder=1)
ax_b.plot([mx + cell_w, mx + cell_w], [my, my + mh],
          color=UI['grid'], lw=0.6, zorder=1)

for col, row, name, ckey, bg in cells_b:
    x = mx + col * cell_w
    y = my + row * cell_h
    box = FancyBboxPatch((x + 0.1, y + 0.1), cell_w - 0.2, cell_h - 0.2,
                         boxstyle="round,pad=0,rounding_size=0.15",
                         facecolor=bg, edgecolor=COLORS[ckey],
                         linewidth=1.0, zorder=3)
    ax_b.add_patch(box)
    ax_b.text(x + cell_w/2, y + cell_h/2, name,
              ha='center', va='center', fontsize=15, fontweight='bold',
              color=COLORS[ckey], zorder=4)

ax_b.text(mx, my - 0.5, 'Additional:', fontsize=14,
          fontweight='bold', color=UI['text'])
extras = [
    ('Random OCC', COLORS['random_occ']),
    ('Depth-only', COLORS['depth']),
    ('Cutoff / Reverse', COLORS['cutoff']),
    ('Vanilla (no aux)', COLORS['vanilla']),
]
for i, (name, color) in enumerate(extras):
    cx = mx if i < 2 else mx + 3.6
    cy = my - 1.0 - (i % 2) * 0.50
    ax_b.plot(cx + 0.1, cy, 's', color=color, markersize=4.5, zorder=4)
    ax_b.text(cx + 0.4, cy, name, fontsize=13, va='center', color=UI['text'])

ax_b.text(mx + mw/2, my - 3.05,
          '5 factors across 12 conditions:\ngradient flow / label content / normalization\n'
          'reference frame / temporal extent',
          ha='center', fontsize=13, color=UI['subtle'], style='italic',
          linespacing=1.3)


# Panel separator
sep_x = 0.49
fig.add_artist(plt.Line2D([sep_x, sep_x], [0.08, 0.90], transform=fig.transFigure,
               color='#E8E8E8', linewidth=0.4, zorder=0))

# Save
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'
fig.savefig(f'{out_dir}/fig1_architecture.png', dpi=300, bbox_inches='tight',
            pad_inches=0.05, facecolor='white')
fig.savefig(f'{out_dir}/fig1_architecture.pdf', dpi=300, bbox_inches='tight',
            pad_inches=0.05, facecolor='white')
plt.close()
print("Saved fig1_architecture.png and fig1_architecture.pdf")
