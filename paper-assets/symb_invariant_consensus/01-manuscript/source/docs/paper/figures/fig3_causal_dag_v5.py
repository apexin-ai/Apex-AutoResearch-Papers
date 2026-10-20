import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.font_manager as fm

fig, ax = plt.subplots(figsize=(7.2, 3.0), dpi=300)
ax.set_xlim(-0.3, 11.3)
ax.set_ylim(0.2, 4.5)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('white')

serif_prop = fm.FontProperties(family='serif')
serif_bold = fm.FontProperties(family='serif', weight='bold')

# Node positions — wider spacing
nodes = {
    'M': {'x': 1.0, 'y': 1.6, 'label': 'Model',
           'fill': '#D6E8F5', 'border': '#5B8DB8', 'text': '#2C5F8A', 'bw': 2.0},
    'T': {'x': 3.2, 'y': 1.6, 'label': 'Trace',
           'fill': '#D8CEE8', 'border': '#8B6FAF', 'text': '#5B3F7E', 'bw': 2.0},
    'A': {'x': 5.4, 'y': 1.6, 'label': 'Answer',
           'fill': '#F5C6C6', 'border': '#C0392B', 'text': '#8B1A1A', 'bw': 2.8},
    'C': {'x': 7.6, 'y': 1.6, 'label': 'Constraints',
           'fill': '#FAE0C8', 'border': '#D4874D', 'text': '#8B5E2B', 'bw': 2.0},
    'S': {'x': 9.8, 'y': 1.6, 'label': 'SICA',
           'fill': '#C8E6E8', 'border': '#3A8B8F', 'text': '#2A6B6F', 'bw': 2.0},
    'Y': {'x': 5.4, 'y': 3.5, 'label': 'Truth',
           'fill': '#D4EDDA', 'border': '#6BAF7B', 'text': '#3A6B44', 'bw': 1.6},
}

nw, nh = 1.05, 0.8
nw_a, nh_a = 1.12, 0.86

def dims(key):
    return (nw_a, nh_a) if key == 'A' else (nw, nh)

# Background groups
pad = 0.35
gen_left = nodes['M']['x'] - nw/2 - pad
gen_bottom = nodes['M']['y'] - nh/2 - pad * 0.7
gen_right = nodes['A']['x'] + nw_a/2 + pad
gen_top = nodes['Y']['y'] + nh/2 + pad
gen_bg = FancyBboxPatch(
    (gen_left, gen_bottom), gen_right - gen_left, gen_top - gen_bottom,
    boxstyle="round,pad=0,rounding_size=0.22",
    facecolor='#F4F5F7', edgecolor='none', zorder=0
)
ax.add_patch(gen_bg)
ax.text((gen_left + gen_right) / 2, gen_top + 0.05,
        'Generation', fontsize=6.5, color='#B0B0B0',
        ha='center', va='bottom', fontfamily='sans-serif')

ver_left = nodes['C']['x'] - nw/2 - pad
ver_bottom = gen_bottom
ver_right = nodes['S']['x'] + nw/2 + pad
ver_top = nodes['C']['y'] + nh/2 + pad
ver_bg = FancyBboxPatch(
    (ver_left, ver_bottom), ver_right - ver_left, ver_top - ver_bottom,
    boxstyle="round,pad=0,rounding_size=0.22",
    facecolor='#F6F5F3', edgecolor='none', zorder=0
)
ax.add_patch(ver_bg)
ax.text((ver_left + ver_right) / 2, ver_top + 0.05,
        'Verification', fontsize=6.5, color='#B0B0B0',
        ha='center', va='bottom', fontfamily='sans-serif')

# Draw nodes
for key, n in nodes.items():
    w, h = dims(key)
    is_y = key == 'Y'

    shadow = FancyBboxPatch(
        (n['x'] - w/2 + 0.02, n['y'] - h/2 - 0.02),
        w, h,
        boxstyle="round,pad=0,rounding_size=0.16",
        facecolor='#00000006', edgecolor='none', zorder=1
    )
    ax.add_patch(shadow)

    box = FancyBboxPatch(
        (n['x'] - w/2, n['y'] - h/2),
        w, h,
        boxstyle="round,pad=0,rounding_size=0.16",
        facecolor=n['fill'], edgecolor=n['border'],
        linewidth=n['bw'],
        linestyle=(0, (5, 3)) if is_y else '-',
        zorder=2
    )
    ax.add_patch(box)

    ax.text(n['x'], n['y'] + 0.08, key,
            fontsize=21, fontweight='bold', color=n['text'],
            ha='center', va='center', fontproperties=serif_bold, zorder=3)
    ax.text(n['x'], n['y'] - 0.23, n['label'],
            fontsize=8.5, color=n['text'],
            ha='center', va='center', fontproperties=serif_prop, zorder=3)

# Arrow helper
def draw_arrow(src, dst, color='#555555', lw=1.5, hw=5, hl=4,
               dashed=False, vertical=False):
    sw, sh = dims(src)
    dw, dh = dims(dst)
    s, d = nodes[src], nodes[dst]
    gap = 0.1

    if vertical:
        sx, sy = s['x'], s['y'] - sh/2 - gap
        dx, dy = d['x'], d['y'] + dh/2 + gap
    else:
        sx, sy = s['x'] + sw/2 + gap, s['y']
        dx, dy = d['x'] - dw/2 - gap, d['y']

    arrow = FancyArrowPatch(
        (sx, sy), (dx, dy),
        arrowstyle=f'-|>,head_width={hw},head_length={hl}',
        color=color, linewidth=lw,
        linestyle='--' if dashed else '-',
        mutation_scale=1, zorder=4
    )
    ax.add_patch(arrow)

# Main chain
draw_arrow('M', 'T', lw=1.5, hw=5, hl=4)
draw_arrow('T', 'A', lw=1.5, hw=5, hl=4)
draw_arrow('C', 'S', lw=1.5, hw=5, hl=4)

# A → C: red bottleneck
draw_arrow('A', 'C', color='#C0392B', lw=2.0, hw=6, hl=5)

# Y → A: dashed gray
draw_arrow('Y', 'A', color='#AAAAAA', lw=1.0, hw=4, hl=3.5,
           dashed=True, vertical=True)

# "bottleneck" label — centered above A→C arrow
ax.text(
    (nodes['A']['x'] + nodes['C']['x']) / 2,
    nodes['A']['y'] + 0.6,
    'bottleneck', fontsize=7.5, fontstyle='italic', color='#C0392B',
    ha='center', va='center', fontproperties=serif_prop, zorder=5
)

# C ⊥⊥ Y | A annotation box
ann_x = (nodes['C']['x'] + nodes['S']['x']) / 2 + 0.3
ann_y = 3.5
ann_w, ann_h = 1.3, 0.42
ann_box = FancyBboxPatch(
    (ann_x - ann_w/2, ann_y - ann_h/2),
    ann_w, ann_h,
    boxstyle="round,pad=0.05,rounding_size=0.07",
    facecolor='#F8F8F8', edgecolor='#D0D0D0',
    linewidth=0.7, linestyle=(0, (4, 3)), zorder=2
)
ax.add_patch(ann_box)
ax.text(ann_x, ann_y, r'$C \perp\!\!\!\perp Y \mid A$',
        fontsize=9.5, color='#555555',
        ha='center', va='center', zorder=3)

out = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures'
plt.savefig(f'{out}/fig3_causal_dag_pb_v5.png', dpi=300, bbox_inches='tight',
            pad_inches=0.08, facecolor='white')
plt.savefig(f'{out}/fig3_causal_dag_pb_v5.pdf', dpi=300, bbox_inches='tight',
            pad_inches=0.08, facecolor='white')
plt.close()
print('Saved PNG + PDF')
