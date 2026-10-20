"""
fig1_overview.py — Hero figure for CoRL 2026.
Three-panel overview: (a) Training setup, (b) Factorial design, (c) Key result.
All data from v2 codebase (Table 1 in paper).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

# === Paper color palette (semantic, consistent across all figures) ===
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
    'encoder_fill': '#EBF0F7',
    'encoder_edge': '#4C72B0',
    'llm_fill':     '#F5F0E8',
    'llm_edge':     '#937860',
    'head_fill':    '#FFF3E0',
    'head_edge':    '#E69F00',
    'action_fill':  '#E8F5E9',
    'action_edge':  '#55A868',
    'grid':         '#DEE2E6',
}

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 14,
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

ax_a = fig.add_axes([0.015, 0.06, 0.30, 0.86])
ax_b = fig.add_axes([0.34, 0.06, 0.24, 0.86])
ax_c = fig.add_axes([0.635, 0.12, 0.345, 0.72])

for ax in [ax_a, ax_b]:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')


def draw_box(ax, xy, w, h, label, sublabel=None, fill='white', edge='#333',
             fontsize=13, lw=1.8, radius=0.18):
    box = FancyBboxPatch(xy, w, h, boxstyle=f"round,pad=0,rounding_size={radius}",
                         facecolor=fill, edgecolor=edge, linewidth=lw, zorder=3)
    ax.add_patch(box)
    cx, cy = xy[0] + w/2, xy[1] + h/2
    if sublabel:
        ax.text(cx, cy + 0.22, label, ha='center', va='center', fontsize=fontsize,
                fontweight='bold', color=UI['text'], zorder=4)
        ax.text(cx, cy - 0.28, sublabel, ha='center', va='center', fontsize=11,
                color=UI['subtle'], zorder=4, style='italic')
    else:
        ax.text(cx, cy, label, ha='center', va='center', fontsize=fontsize,
                fontweight='bold', color=UI['text'], zorder=4)


def draw_arrow(ax, start, end, color='#555', lw=1.6, style='->', mutation=13):
    arrow = FancyArrowPatch(start, end, arrowstyle=style, color=color,
                            linewidth=lw, mutation_scale=mutation, zorder=2)
    ax.add_patch(arrow)


# ============================================================
# PANEL (a): Training Architecture
# ============================================================
ax_a.text(0.1, 9.6, '(a) Training Setup', fontsize=15, fontweight='bold',
          va='top', color=UI['text'])

draw_box(ax_a, (3.2, 0.3), 3.6, 1.1, 'RGB Observation', fill='#F0F4F8',
         edge=UI['subtle'], fontsize=11.5)
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
ax_a.text(5.0, 3.75, 'concat (2176-d)', fontsize=11, ha='center',
          color=UI['subtle'], style='italic')

draw_box(ax_a, (1.5, 6.0), 3.0, 1.0, 'Action Head', sublabel='7-DoF tokens',
         fill=UI['action_fill'], edge=UI['action_edge'])
draw_arrow(ax_a, (3.5, 5.2), (3.0, 6.0), color=UI['action_edge'], lw=1.8)
ax_a.text(1.5, 7.3, r'$\mathcal{L}_{\mathrm{action}}$', fontsize=14,
          ha='center', color=UI['action_edge'], fontweight='bold')
draw_arrow(ax_a, (2.2, 7.2), (2.5, 7.0), color=UI['action_edge'], lw=1.3)

draw_box(ax_a, (6.0, 6.0), 3.0, 1.0, 'Aux Head', sublabel='BEV / Depth',
         fill=UI['head_fill'], edge=UI['head_edge'])
draw_arrow(ax_a, (6.5, 5.2), (7.5, 6.0), color=UI['head_edge'], lw=1.8)
ax_a.text(8.7, 7.3, r'$\lambda(t) \cdot \mathcal{L}_{\mathrm{aux}}$',
          fontsize=14, ha='center', color=UI['head_edge'], fontweight='bold')
draw_arrow(ax_a, (8.3, 7.2), (8.0, 7.0), color=UI['head_edge'], lw=1.3)

ax_a.text(9.25, 6.15, 'BN/LN', fontsize=11, ha='center',
          color=COLORS['full_occ_bn'], fontweight='bold',
          bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                    edgecolor=COLORS['full_occ_bn'], lw=1.3))

ax_a.annotate('', xy=(7.2, 3.5), xytext=(7.5, 5.95),
              arrowprops=dict(arrowstyle='->', color=COLORS['full_occ_bn'],
                              lw=2.2, linestyle=(0, (4, 3)),
                              connectionstyle='arc3,rad=-0.12'))
ax_a.text(8.8, 4.5, 'gradient\nflow?', fontsize=12, ha='center',
          color=COLORS['full_occ_bn'], fontweight='bold', style='italic',
          bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF0F0',
                    edgecolor=COLORS['full_occ_bn'], lw=1.0, alpha=0.85))

ax_a.text(7.5, 8.4, 'discarded at inference', fontsize=11.5,
          ha='center', color='#7F8C8D', style='italic',
          bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF8E1',
                    edgecolor='#BDC3C7', lw=0.8, alpha=0.9))
draw_arrow(ax_a, (7.5, 8.1), (7.5, 7.0), color=UI['subtle'],
           lw=0.7, style='->')


# ============================================================
# PANEL (b): 2x2 Factorial Design
# ============================================================
ax_b.text(0.1, 9.6, '(b) Factorial Design', fontsize=15, fontweight='bold',
          va='top', color=UI['text'])

mx, my = 1.5, 4.0
mw, mh = 7.0, 4.4
cell_w, cell_h = mw / 2, mh / 2

ax_b.text(mx + cell_w * 0.5, my + mh + 0.5, 'Gradient ON',
          ha='center', fontsize=13, fontweight='bold', color=COLORS['full_occ_bn'])
ax_b.text(mx + cell_w * 1.5, my + mh + 0.5, 'Gradient OFF',
          ha='center', fontsize=13, fontweight='bold', color=COLORS['detach_bn'])
ax_b.text(mx - 0.2, my + cell_h * 1.5, 'BN',
          ha='right', va='center', fontsize=13, fontweight='bold', color=UI['text'])
ax_b.text(mx - 0.2, my + cell_h * 0.5, 'LN',
          ha='right', va='center', fontsize=13, fontweight='bold', color=UI['text'])

cells_b = [
    (0, 1, 'Full OCC',      'full_occ_bn', '#FDECEA'),
    (1, 1, 'Detach OCC',    'detach_bn',   '#EEEBF5'),
    (0, 0, 'Full OCC+LN',   'full_occ_ln', '#FFF5E0'),
    (1, 0, 'Detach+LN',     'detach_ln',   '#F3EDE6'),
]

border = FancyBboxPatch((mx, my), mw, mh, boxstyle="round,pad=0,rounding_size=0.2",
                         facecolor='none', edgecolor='#BDC3C7', linewidth=1.0, zorder=2)
ax_b.add_patch(border)
ax_b.plot([mx, mx + mw], [my + cell_h, my + cell_h],
          color=UI['grid'], lw=0.8, zorder=1)
ax_b.plot([mx + cell_w, mx + cell_w], [my, my + mh],
          color=UI['grid'], lw=0.8, zorder=1)

for col, row, name, ckey, bg in cells_b:
    x = mx + col * cell_w
    y = my + row * cell_h
    box = FancyBboxPatch((x + 0.1, y + 0.1), cell_w - 0.2, cell_h - 0.2,
                         boxstyle="round,pad=0,rounding_size=0.15",
                         facecolor=bg, edgecolor=COLORS[ckey],
                         linewidth=1.2, zorder=3)
    ax_b.add_patch(box)
    ax_b.text(x + cell_w/2, y + cell_h/2, name,
              ha='center', va='center', fontsize=13, fontweight='bold',
              color=COLORS[ckey], zorder=4)

ax_b.text(mx, my - 0.5, 'Additional:', fontsize=11.5,
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
    ax_b.text(cx + 0.4, cy, name, fontsize=10.5, va='center', color=UI['text'])

ax_b.text(mx + mw/2, my - 2.55,
          '5 factors across 12 conditions:\ngradient flow / label content / normalization\n'
          'reference frame / temporal extent',
          ha='center', fontsize=10, color=UI['subtle'], style='italic',
          linespacing=1.3)


# ============================================================
# PANEL (c): Key Result — v2 data from Table 1
# ============================================================
# CORRECTED v2 data (Table 1), grouped by normalization type
cdata = [
    {'name': 'Full OCC\n(BN, Grad ON)',     'car': 0.725, 'sd': 0.064,
     'color': COLORS['full_occ_bn'], 'n_seeds': 3},
    {'name': 'Detach OCC\n(BN, Grad OFF)',   'car': 0.767, 'sd': 0.024,
     'color': COLORS['detach_bn'],   'n_seeds': 4},
    {'name': 'Full OCC+LN\n(LN, Grad ON)',  'car': 0.773, 'sd': 0.027,
     'color': COLORS['full_occ_ln'], 'n_seeds': 4},
    {'name': 'Detach+LN\n(LN, Grad OFF)',   'car': 0.802, 'sd': 0.024,
     'color': COLORS['detach_ln'],   'n_seeds': 3},
]
vanilla_car = 0.745

ax_c.set_xlim(0.655, 0.87)
ax_c.set_ylim(-0.8, len(cdata) - 0.2)
ax_c.invert_yaxis()
ax_c.spines['top'].set_visible(False)
ax_c.spines['right'].set_visible(False)
ax_c.spines['left'].set_visible(False)
ax_c.set_xlabel('Collision Avoidance Rate (CAR)', fontsize=13, fontweight='bold', labelpad=6)

ax_c.set_title('(c) Only BN + gradient flow falls below Vanilla',
               fontsize=15, fontweight='bold', color=UI['text'],
               loc='left', pad=16)

# Group background bands
ax_c.axhspan(-0.5, 1.5, alpha=0.02, color=COLORS['full_occ_bn'], zorder=0)
ax_c.axhspan(1.5, 3.5, alpha=0.02, color=COLORS['full_occ_ln'], zorder=0)
ax_c.text(0.865, 0.5, 'BN', fontsize=11, color=COLORS['full_occ_bn'], ha='center', va='center',
          fontweight='bold', alpha=0.35,
          bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))
ax_c.text(0.865, 2.5, 'LN', fontsize=11, color=COLORS['full_occ_ln'], ha='center', va='center',
          fontweight='bold', alpha=0.35,
          bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))

# Vanilla reference
ax_c.axvline(x=vanilla_car, color=COLORS['vanilla'], linestyle='--',
             linewidth=1.8, alpha=0.7, zorder=1)
ax_c.text(vanilla_car + 0.003, -0.55, f'Vanilla  {vanilla_car:.3f}',
          fontsize=11.5, color=COLORS['vanilla'], va='top', ha='left',
          fontweight='bold',
          path_effects=[pe.withStroke(linewidth=3, foreground='white')])

# Below-baseline shading
ax_c.axvspan(0.655, vanilla_car, alpha=0.04, color=COLORS['full_occ_bn'], zorder=0)

# Connecting lines: BN pair (y=0 Full OCC → y=1 Detach OCC) — adjacent!
ax_c.plot([0.725, 0.767], [0, 1], color=COLORS['full_occ_bn'],
          lw=1.3, linestyle=':', alpha=0.5, zorder=1)
ax_c.text(0.730, 0.55, '$-$4.2 pp', fontsize=11,
          color=COLORS['full_occ_bn'], ha='left', va='center',
          fontweight='bold', alpha=0.8,
          path_effects=[pe.withStroke(linewidth=3, foreground='white')])

# LN pair (y=2 Full OCC+LN → y=3 Detach+LN) — adjacent!
ax_c.plot([0.773, 0.802], [2, 3], color=COLORS['full_occ_ln'],
          lw=1.3, linestyle=':', alpha=0.5, zorder=1)
ax_c.text(0.778, 2.55, '$-$2.9 pp', fontsize=11,
          color=COLORS['full_occ_ln'], ha='left', va='center',
          fontweight='bold', alpha=0.8,
          path_effects=[pe.withStroke(linewidth=3, foreground='white')])

# Plot data
for i, d in enumerate(cdata):
    ax_c.plot(d['car'], i, 'o', color=d['color'], markersize=11,
              markeredgecolor='white', markeredgewidth=1.0, zorder=5)

    if d['sd'] is not None:
        ax_c.errorbar(d['car'], i, xerr=d['sd'], fmt='none', ecolor=d['color'],
                      elinewidth=2.2, capsize=5, capthick=1.6, zorder=4,
                      alpha=0.7)

    right_x = d['car'] + (d['sd'] if d['sd'] else 0) + 0.006
    label_text = f'{d["car"]:.3f} ± {d["sd"]:.3f}' if d['sd'] else f'{d["car"]:.3f}'

    ax_c.text(right_x, i + 0.02, label_text, fontsize=11, ha='left',
              va='center', color=d['color'], fontweight='bold',
              path_effects=[pe.withStroke(linewidth=3, foreground='white')])

ax_c.set_yticks(list(range(len(cdata))))
ax_c.set_yticklabels([d['name'] for d in cdata], fontsize=10.5, linespacing=1.1)
ax_c.tick_params(axis='y', length=0, pad=6)
ax_c.tick_params(axis='x', labelsize=12)
ax_c.grid(axis='x', alpha=0.10, color='#999', zorder=0)
ax_c.set_xticks([0.68, 0.70, 0.72, 0.74, 0.76, 0.78, 0.80, 0.82, 0.84, 0.86])

# Save
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'
fig.savefig(f'{out_dir}/fig1_overview.png', dpi=300, bbox_inches='tight',
            pad_inches=0.05, facecolor='white')
fig.savefig(f'{out_dir}/fig1_overview.pdf', dpi=300, bbox_inches='tight',
            pad_inches=0.05, facecolor='white')
plt.close()
print("Saved fig1_overview.png and fig1_overview.pdf")
