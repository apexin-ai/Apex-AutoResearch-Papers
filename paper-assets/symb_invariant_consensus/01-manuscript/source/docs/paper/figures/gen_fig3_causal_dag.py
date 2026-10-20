"""Figure 3: Causal DAG — Information bottleneck in self-extracted constraints.
M→T→A→C→S with exogenous truth Y. Red bottleneck arrow (A→C) shows
constraints derived from answer, establishing C⊥⊥Y|A.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.colors as mcolors
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Serif',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

OUTDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures'


def draw_3d_box(ax, x, y, w, h, fill_top, fill_bottom, border_color, border_width=2,
                shadow_offset=(0.006, -0.008), shadow_alpha=0.35, corner_radius=0.015):
    """Draw a 3D raised box with gradient fill, shadow, and highlight."""
    # 1. Shadow
    shadow = FancyBboxPatch((x + shadow_offset[0], y + shadow_offset[1]), w, h,
                             boxstyle=f'round,pad=0,rounding_size={corner_radius}',
                             facecolor='#222222', alpha=shadow_alpha, edgecolor='none',
                             transform=ax.transAxes, zorder=1)
    ax.add_patch(shadow)

    # 2. Main box with bottom color
    box = FancyBboxPatch((x, y), w, h,
                          boxstyle=f'round,pad=0,rounding_size={corner_radius}',
                          facecolor=fill_bottom, edgecolor=border_color,
                          linewidth=border_width, transform=ax.transAxes, zorder=2)
    ax.add_patch(box)

    # 3. Gradient overlay using imshow clipped to box
    gradient = np.linspace(1, 0, 256).reshape(-1, 1)
    top_rgb = np.array(mcolors.to_rgb(fill_top))
    bot_rgb = np.array(mcolors.to_rgb(fill_bottom))
    colors = np.zeros((256, 1, 4))
    for i in range(256):
        t = gradient[i, 0]
        colors[i, 0, :3] = top_rgb * t + bot_rgb * (1 - t)
        colors[i, 0, 3] = 0.9
    img = ax.imshow(colors, extent=[x, x + w, y, y + h], aspect='auto',
                    transform=ax.transAxes, zorder=3, interpolation='bicubic')
    clip_box = FancyBboxPatch((x, y), w, h,
                               boxstyle=f'round,pad=0,rounding_size={corner_radius}',
                               transform=ax.transAxes)
    img.set_clip_path(clip_box)

    # 4. Top highlight
    hl_y = y + h - 0.015
    highlight = FancyBboxPatch((x + 0.008, hl_y), w - 0.016, 0.010,
                                boxstyle=f'round,pad=0,rounding_size={corner_radius * 0.4}',
                                facecolor='white', alpha=0.35, edgecolor='none',
                                transform=ax.transAxes, zorder=4)
    ax.add_patch(highlight)

    # 5. Border on top (crisp edge)
    border = FancyBboxPatch((x, y), w, h,
                             boxstyle=f'round,pad=0,rounding_size={corner_radius}',
                             facecolor='none', edgecolor=border_color,
                             linewidth=border_width, transform=ax.transAxes, zorder=5)
    ax.add_patch(border)


def edge_point(node, direction):
    """Get the edge midpoint of a node in given direction."""
    x, y = node['pos']
    w, h = node['size']
    cx, cy = x + w / 2, y + h / 2
    if direction == 'right':
        return (x + w, cy)
    if direction == 'left':
        return (x, cy)
    if direction == 'top':
        return (cx, y + h)
    if direction == 'bottom':
        return (cx, y)


# ── Node definitions ──
nodes = {
    'Y': {'pos': (0.45, 0.78), 'size': (0.10, 0.14), 'label': 'Y', 'sub': 'Truth',
           'fill': '#F7DC6F', 'fill_dark': '#D4AC0D', 'border': '#B7950B', 'text_color': '#7D6608',
           'border_width': 2.5, 'shadow_alpha': 0.32},
    'M': {'pos': (0.04, 0.44), 'size': (0.10, 0.14), 'label': 'M', 'sub': 'Model',
           'fill': '#D5D8DC', 'fill_dark': '#ABB2B9', 'border': '#808B96', 'text_color': '#2C3E50'},
    'T': {'pos': (0.22, 0.44), 'size': (0.10, 0.14), 'label': 'T', 'sub': 'Trace',
           'fill': '#D5D8DC', 'fill_dark': '#ABB2B9', 'border': '#808B96', 'text_color': '#2C3E50'},
    'A': {'pos': (0.40, 0.44), 'size': (0.11, 0.15), 'label': 'A', 'sub': 'Answer',
           'fill': '#AED6F1', 'fill_dark': '#5DADE2', 'border': '#1A5276', 'text_color': '#154360',
           'border_width': 2.5, 'shadow_alpha': 0.32},
    'C': {'pos': (0.58, 0.44), 'size': (0.10, 0.14), 'label': 'C', 'sub': 'Constr.',
           'fill': '#F5B7B1', 'fill_dark': '#E74C3C', 'border': '#922B21', 'text_color': '#78281F'},
    'S': {'pos': (0.76, 0.44), 'size': (0.10, 0.14), 'label': 'S', 'sub': 'Output',
           'fill': '#A2D9CE', 'fill_dark': '#45B39D', 'border': '#148F77', 'text_color': '#0E6251'},
}

# ── Build figure ──
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
fig.patch.set_facecolor('white')

# Draw nodes
for key, nd in nodes.items():
    x, y = nd['pos']
    w, h = nd['size']
    bw = nd.get('border_width', 2)
    sa = nd.get('shadow_alpha', 0.35)
    draw_3d_box(ax, x, y, w, h, nd['fill'], nd['fill_dark'], nd['border'],
                border_width=bw, shadow_alpha=sa)
    cx, cy = x + w / 2, y + h / 2
    ax.text(cx, cy + 0.012, f'$\\mathit{{{nd["label"]}}}$',
            fontsize=18, fontweight='bold', ha='center', va='center',
            fontfamily='serif', color=nd['text_color'],
            transform=ax.transAxes, zorder=6)
    ax.text(cx, cy - 0.028, nd['sub'],
            fontsize=8, ha='center', va='center',
            fontfamily='sans-serif', color='#7F8C8D',
            transform=ax.transAxes, zorder=6)

# ── Edges ──

def draw_arrow(p0, p1, color='#7F8C8D', lw=1.8, hl=8, hw=5,
               dashed=False, conn='arc3,rad=0', zorder=5):
    style = f'->,head_length={hl},head_width={hw}'
    ls = (0, (5, 3.5)) if dashed else '-'
    arrow = FancyArrowPatch(
        p0, p1,
        arrowstyle=style,
        connectionstyle=conn,
        color=color, linewidth=lw,
        linestyle=ls,
        mutation_scale=1.0,
        shrinkA=0, shrinkB=0,
        zorder=zorder, clip_on=False,
        transform=ax.transAxes,
    )
    ax.add_patch(arrow)


# M → T
draw_arrow(edge_point(nodes['M'], 'right'), edge_point(nodes['T'], 'left'))

# T → A
draw_arrow(edge_point(nodes['T'], 'right'), edge_point(nodes['A'], 'left'))

# A → C  (bottleneck — red, thick)
draw_arrow(edge_point(nodes['A'], 'right'), edge_point(nodes['C'], 'left'),
           color='#C0392B', lw=3.0, hl=10, hw=7)

# C → S
draw_arrow(edge_point(nodes['C'], 'right'), edge_point(nodes['S'], 'left'))

# Y → A  (gold dashed)
draw_arrow(edge_point(nodes['Y'], 'bottom'), edge_point(nodes['A'], 'top'),
           color='#B7950B', lw=1.5, dashed=True, hl=6, hw=4)

# Y → C  (blocked — faint gray dashed)
y_bottom = edge_point(nodes['Y'], 'bottom')
c_top = edge_point(nodes['C'], 'top')
yc_start = (y_bottom[0] + 0.03, y_bottom[1])
yc_end = (c_top[0] - 0.01, c_top[1])
draw_arrow(yc_start, yc_end,
           color='#CCCCCC', lw=0.8, dashed=True, hl=3, hw=2, zorder=3)

# Red ✗ on blocked path
bx = (yc_start[0] + yc_end[0]) / 2 + 0.015
by = (yc_start[1] + yc_end[1]) / 2
ax.text(bx, by, r'$\times$', fontsize=16, fontweight='bold',
        color='#C0392B', ha='center', va='center',
        transform=ax.transAxes, zorder=12)

# M → S  (curved arc below)
m_right = edge_point(nodes['M'], 'right')
s_left = edge_point(nodes['S'], 'left')
m_arc_start = (m_right[0], m_right[1] - 0.02)
s_arc_end = (s_left[0], s_left[1] - 0.02)
draw_arrow(m_arc_start, s_arc_end,
           color='#BDC3C7', lw=1.0, conn='arc3,rad=-0.35', zorder=3, hl=5, hw=3)

# ── Annotations ──

# "bottleneck" above A→C
ac_mid_x = (edge_point(nodes['A'], 'right')[0] + edge_point(nodes['C'], 'left')[0]) / 2
ac_mid_y = edge_point(nodes['A'], 'right')[1]
ax.text(ac_mid_x, ac_mid_y + 0.055, 'bottleneck',
        fontsize=11, fontstyle='italic', fontweight='bold',
        color='#C0392B', ha='center', va='center',
        fontfamily='sans-serif', transform=ax.transAxes, zorder=10)

# "C = f(T, A)" below A→C
ax.text(ac_mid_x, ac_mid_y - 0.055, '$C = f\\,(T, A)$',
        fontsize=9, fontstyle='italic', color='#888888',
        ha='center', va='center', fontfamily='serif',
        transform=ax.transAxes, zorder=10)

# ── Conditional independence box ──
ci_x, ci_y = 0.33, 0.05
ci_w, ci_h = 0.24, 0.12
draw_3d_box(ax, ci_x, ci_y, ci_w, ci_h,
            '#FDF6E3', '#F5E6C8', '#D5DBDB',
            border_width=1.0, shadow_alpha=0.20, corner_radius=0.012)
ci_cx = ci_x + ci_w / 2
ci_cy = ci_y + ci_h / 2
ax.text(ci_cx, ci_cy + 0.012, r'$C \perp\!\!\!\perp Y \mid A$',
        fontsize=14, ha='center', va='center',
        fontfamily='serif', transform=ax.transAxes, zorder=6)
ax.text(ci_cx, ci_cy - 0.022, 'conditional independence',
        fontsize=9, fontstyle='italic', ha='center', va='center',
        fontfamily='sans-serif', color='#7F8C8D',
        transform=ax.transAxes, zorder=6)

# ── Save ──
fig.savefig(f'{OUTDIR}/fig3_causal_dag.png', facecolor='white')
fig.savefig(f'{OUTDIR}/fig3_causal_dag.pdf', facecolor='white')
plt.close()
print('Done: fig3_causal_dag')
