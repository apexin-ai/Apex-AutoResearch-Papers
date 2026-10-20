import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe

fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
ax.set_xlim(-0.2, 10.2)
ax.set_ylim(0.2, 5.8)
ax.axis('off')
ax.set_aspect('equal')
fig.patch.set_facecolor('white')

nodes_cfg = {
    'Y': ('Truth',   5.0, 4.95, '#FEF9E7', '#D4AC0D', 1.6),
    'M': ('Model',   1.0, 2.8, '#F5F6FA', '#BDC3C7', 1.2),
    'T': ('Trace',   3.0, 2.8, '#F5F6FA', '#BDC3C7', 1.2),
    'A': ('Answer',  5.0, 2.8, '#EBF5FB', '#2C3E50', 1.6),
    'C': ('Constr.', 7.0, 2.8, '#FDF0EF', '#C0392B', 1.4),
    'S': ('Output',  9.0, 2.8, '#E8F8F5', '#1ABC9C', 1.2),
}

nw, nh = 0.78, 0.78
centers = {}

for lbl, (sub, cx, cy, fill, ecol, ew) in nodes_cfg.items():
    box = FancyBboxPatch(
        (cx - nw/2, cy - nh/2), nw, nh,
        boxstyle="round,pad=0,rounding_size=0.11",
        facecolor=fill, edgecolor=ecol, linewidth=ew, zorder=10
    )
    box.set_path_effects([
        pe.SimplePatchShadow(offset=(0.8, -0.8), shadow_rgbFace='#000000', alpha=0.05),
        pe.Normal()
    ])
    ax.add_patch(box)
    ax.text(cx, cy + 0.06, f'$\\mathit{{{lbl}}}$',
            fontsize=18, fontweight='bold', ha='center', va='center',
            fontfamily='serif', zorder=11)
    ax.text(cx, cy - 0.23, sub,
            fontsize=7.5, ha='center', va='center',
            fontfamily='sans-serif', color='#7F8C8D', zorder=11)
    centers[lbl] = (cx, cy)

def edge(p0, p1, color='#666666', lw=1.1, dashed=False, conn='arc3,rad=0',
         zorder=5, hl=6, hw=3.5):
    a = FancyArrowPatch(
        p0, p1,
        arrowstyle=f'->,head_length={hl},head_width={hw}',
        connectionstyle=conn,
        color=color, linewidth=lw,
        linestyle=(0, (5, 3.5)) if dashed else '-',
        mutation_scale=1.0, shrinkA=0, shrinkB=0,
        zorder=zorder, clip_on=False
    )
    ax.add_patch(a)

gap = nw/2 + 0.08

# Causal chain
edge((centers['M'][0]+gap, centers['M'][1]),
     (centers['T'][0]-gap, centers['T'][1]))
edge((centers['T'][0]+gap, centers['T'][1]),
     (centers['A'][0]-gap, centers['A'][1]))
# A → C bottleneck — crimson, thicker line, proportional head
edge((centers['A'][0]+gap, centers['A'][1]),
     (centers['C'][0]-gap, centers['C'][1]),
     color='#C0392B', lw=1.8, hl=7, hw=4)
edge((centers['C'][0]+gap, centers['C'][1]),
     (centers['S'][0]-gap, centers['S'][1]))

# Y → A dashed gold
edge((centers['Y'][0], centers['Y'][1]-nh/2-0.06),
     (centers['A'][0], centers['A'][1]+nh/2+0.06),
     color='#B8860B', lw=1.1, dashed=True)

# M → S curved arc below
edge((centers['M'][0]+gap, centers['M'][1]-0.18),
     (centers['S'][0]-gap, centers['S'][1]-0.18),
     color='#CCCCCC', lw=0.5, conn='arc3,rad=0.25', zorder=3, hl=4, hw=2.5)

# Blocked path Y → C faint dashed
edge((centers['Y'][0]+0.32, centers['Y'][1]-nh/2-0.06),
     (centers['C'][0]-0.12, centers['C'][1]+nh/2+0.06),
     color='#DDDDDD', lw=0.5, dashed=True, zorder=3, hl=3, hw=2)

# Red × on blocked path
bx = (centers['Y'][0]+0.32 + centers['C'][0]-0.12) / 2 + 0.10
by = (centers['Y'][1]-nh/2-0.06 + centers['C'][1]+nh/2+0.06) / 2
ax.text(bx, by, '×', fontsize=14, fontweight='bold',
        color='#C0392B', ha='center', va='center', zorder=12)

# "bottleneck" — tightly above A→C edge
mid_ac = (centers['A'][0] + centers['C'][0]) / 2
ax.text(mid_ac, centers['A'][1] + 0.44, 'bottleneck',
        fontsize=8.5, fontstyle='italic', fontweight='bold',
        color='#C0392B', ha='center', va='center', fontfamily='sans-serif')

# "C = f(T, A)" — below A→C edge
ax.text(mid_ac, centers['A'][1] - 0.48, '$C = f\\,(T, A)$',
        fontsize=8, color='#666666', ha='center', va='center', fontfamily='serif')

# Conditional independence box
bx_c, by_c = 5.0, 0.78
ci = FancyBboxPatch(
    (bx_c - 1.12, by_c - 0.32), 2.24, 0.64,
    boxstyle="round,pad=0,rounding_size=0.09",
    facecolor='#FDF6E3', edgecolor='#D5DBDB', linewidth=0.8, zorder=10
)
ci.set_path_effects([
    pe.SimplePatchShadow(offset=(0.8, -0.8), shadow_rgbFace='#000000', alpha=0.05),
    pe.Normal()
])
ax.add_patch(ci)
ax.text(bx_c, by_c + 0.07, r'$C \perp\!\!\!\perp Y \mid A$',
        fontsize=12, ha='center', va='center', fontfamily='serif', zorder=11)
ax.text(bx_c, by_c - 0.14, 'conditional independence',
        fontsize=7, fontstyle='italic', ha='center', va='center',
        fontfamily='sans-serif', color='#7F8C8D', zorder=11)

out = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures/fig3_causal_dag_pb_v2.png'
plt.savefig(out, dpi=300, bbox_inches='tight', pad_inches=0.10, facecolor='white')
plt.close()
print(f'Saved: {out}')
