import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'serif'],
    'mathtext.fontset': 'cm',
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

C = {
    'd0_bg': '#D8DEE9', 'd0_bd': '#B8C4D4',
    'd1_bg': '#EAE0D4', 'd1_bd': '#C8B8A4',
    'd2_bg': '#E0CEB0', 'd2_bd': '#C0A888',
    'dk_bg': '#C4A47A', 'dk_bd': '#A08050',
    'arrow':  '#A8B0BA',
    'main':   '#3B4A5C',
    'sub':    '#9099A4',
    'red':    '#8899B0',
    'cls_bg': '#EEF1F5', 'cls_bd': '#8899B0',
    'accent': '#8899B0',
    'bar_label': '#B8956A',
    'binary': '#AAAAAA',
    'ours_bg': '#F5F0EA', 'ours_bd': '#C4A47A',
    'ours_text': '#5B4A30',
    'ours_sub': '#8B7B60',
    'panel':  '#F7F8FA',
    'panel_bd': '#E8ECF0',
}

W, H = 7.0, 2.60
fig = plt.figure(figsize=(W, H))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(-0.08, H + 0.02)
ax.axis('off')


def rbox(ax, x, y, w, h, bg, bd, lw=0.7, zorder=3, shadow=True):
    if shadow:
        for dx, dy, a in [(0.012, -0.012, 0.045), (0.024, -0.024, 0.02)]:
            ax.add_patch(FancyBboxPatch(
                (x+dx, y+dy), w, h,
                boxstyle='round,pad=0.03,rounding_size=0.06',
                fc='#000000', ec='none', alpha=a, zorder=zorder-2))
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle='round,pad=0.03,rounding_size=0.06',
        fc=bg, ec=bd, lw=lw, zorder=zorder))


def doc_icon(ax, cx, cy, s=0.10, c='#6B7B8D', zorder=5):
    px = [cx-s, cx-s, cx+s*0.5, cx+s, cx+s, cx-s]
    py = [cy-s*1.2, cy+s*1.2, cy+s*1.2, cy+s*0.65, cy-s*1.2, cy-s*1.2]
    ax.fill(px, py, fc='white', ec=c, lw=0.5, zorder=zorder)
    fx = [cx+s*0.5, cx+s*0.5, cx+s]
    fy = [cy+s*1.2, cy+s*0.65, cy+s*0.65]
    ax.fill(fx, fy, fc='#E8ECF0', ec=c, lw=0.35, zorder=zorder+1)
    for frac in [0.50, 0.15, -0.20, -0.55]:
        lw_l = s * (1.2 if frac > 0.3 else (1.0 if frac > -0.3 else 0.6))
        ax.plot([cx-s*0.6, cx-s*0.6+lw_l], [cy+s*frac]*2,
                c=c, lw=0.35, alpha=0.38, zorder=zorder+1)


def thin_arrow(ax, xy1, xy2, **kw):
    defaults = dict(arrowstyle='->', color=C['arrow'], lw=0.7,
                    mutation_scale=7, zorder=4,
                    connectionstyle='arc3,rad=0')
    defaults.update(kw)
    ax.add_patch(FancyArrowPatch(xy1, xy2, **defaults))


# ═══════════════════════════════════════════════
# LAYER 1 — Recursive Generation Chain
# ═══════════════════════════════════════════════
bw, bh = 0.72, 0.56
by = 1.48
ay = by + bh/2

chain_bg_y = by - 0.06
chain_bg_h = bh + 0.12

ax.add_patch(FancyBboxPatch(
    (0.16, chain_bg_y), 6.68, chain_bg_h,
    boxstyle='round,pad=0.02,rounding_size=0.06',
    fc=C['panel'], ec=C['panel_bd'], lw=0.35, zorder=1))

ax.text(3.50, chain_bg_y + chain_bg_h + 0.12,
        'Recursive Generation Chain',
        fontsize=10, fontweight='bold', color=C['main'], ha='center')

nodes = [
    (0.50,  r'$\mathcal{D}_0$', 'Human',    C['d0_bg'], C['d0_bd']),
    (1.72,  r'$\mathcal{D}_1$', 'Gen-1',    C['d1_bg'], C['d1_bd']),
    (2.94,  r'$\mathcal{D}_2$', 'Gen-2',    C['d2_bg'], C['d2_bd']),
    (5.58,  r'$\mathcal{D}_K$', r'Gen-$K$', C['dk_bg'], C['dk_bd']),
]

for nx, lab, sub, bg, bd in nodes:
    rbox(ax, nx, by, bw, bh, bg, bd, lw=0.8)
    doc_icon(ax, nx+bw/2, by+bh*0.66, s=0.09, c=bd)
    ax.text(nx+bw/2, by+bh*0.24, lab, fontsize=10, fontweight='bold',
            color=C['main'], ha='center', va='center', zorder=6)
    sub_color = '#F0E8DC' if bg == C['dk_bg'] else C['sub']
    ax.text(nx+bw/2, by+bh*0.05, sub, fontsize=5.5, color=sub_color,
            ha='center', va='center', zorder=6)

for i in range(2):
    x1 = nodes[i][0] + bw + 0.04
    x2 = nodes[i+1][0] - 0.04
    thin_arrow(ax, (x1, ay), (x2, ay))
    ax.text((x1+x2)/2, ay-0.14, 'LoRA ft + sample',
            fontsize=5, color=C['sub'], fontstyle='italic',
            ha='center', va='top', zorder=6)

thin_arrow(ax, (4.82, ay), (nodes[3][0]-0.04, ay))
ax.text((4.82+nodes[3][0]-0.04)/2, ay-0.14, 'LoRA ft + sample',
        fontsize=5, color=C['sub'], fontstyle='italic',
        ha='center', va='top', zorder=6)

for dx in [-0.15, 0, 0.15]:
    ax.plot(4.40+dx, ay, '.', color=C['sub'], markersize=3.5, zorder=6)


# ═══════════════════════════════════════════════
# LAYER 2 — Depth Estimation Query
# ═══════════════════════════════════════════════
qy = 0.56

ax.annotate('', xy=(0.87, qy+0.22), xytext=(0.87, by-0.03),
            arrowprops=dict(arrowstyle='->', color=C['arrow'],
                            ls='dashed', lw=0.5, mutation_scale=6), zorder=4)

doc_icon(ax, 0.68, qy+0.04, s=0.11, c=C['d1_bd'], zorder=5)
ax.text(0.68, qy-0.19, r'Text passage $\mathbf{x}$',
        fontsize=7.5, color=C['main'], ha='center', zorder=6)
ax.text(0.68, qy-0.31, r'depth $d$ = ?',
        fontsize=6.5, color=C['red'], fontstyle='italic', ha='center', zorder=6)

thin_arrow(ax, (1.14, qy), (1.94, qy))

cw, ch = 1.10, 0.38
cx = 1.96
rbox(ax, cx, qy-ch/2, cw, ch, C['cls_bg'], C['cls_bd'], lw=0.7)
ax.text(cx+cw/2, qy+0.05, 'Depth Classifier',
        fontsize=7.5, fontweight='bold', color=C['main'], ha='center', zorder=6)
ax.text(cx+cw/2, qy-0.08, '(Statistical Features + RF)',
        fontsize=5.5, color='#7B8898', ha='center', zorder=6)

thin_arrow(ax, (cx+cw+0.03, qy), (3.80, qy), arrowstyle='-|>')

# ── Bar chart ──
bx0 = 3.88
bw_total = 2.52
bh_max = 0.48
b_base = qy - 0.18

ax.text(bx0+bw_total/2, qy+0.34, 'Estimated Depth Output',
        fontsize=7, fontweight='bold', color=C['main'], ha='center', zorder=6)

ax.add_patch(FancyBboxPatch(
    (bx0-0.06, b_base-0.05), bw_total+0.12, bh_max+0.18,
    boxstyle='round,pad=0.02,rounding_size=0.04',
    fc='#FAFBFC', ec='#E4E8EC', lw=0.3, zorder=2))

bars = [
    (r'$d{=}0$', 0.08, '#D8DEE9'),
    (r'$d{=}1$', 0.70, '#C4A47A'),
    (r'$d{=}2$', 0.15, '#D4B896'),
    (r'$d{=}K$', 0.05, '#A08050'),
]

sp = bw_total / len(bars)
bwi = sp * 0.48

for i, (lbl, val, col) in enumerate(bars):
    bxi = bx0 + i*sp + (sp-bwi)/2
    h = val * bh_max
    ax.add_patch(FancyBboxPatch(
        (bxi, b_base), bwi, h,
        boxstyle='round,pad=0,rounding_size=0.012',
        fc=col, ec='none', alpha=0.85, zorder=5))
    ax.text(bxi+bwi/2, b_base-0.055, lbl,
            fontsize=6, color=C['main'], ha='center', va='top', zorder=6)
    if val >= 0.10:
        ax.text(bxi+bwi/2, b_base+h+0.015, f'{int(val*100)}%',
                fontsize=6, fontweight='bold', color=C['bar_label'],
                ha='center', va='bottom', zorder=6)
ax.plot([bx0-0.02, bx0+bw_total+0.02], [b_base, b_base],
        color='#CCD0D8', lw=0.35, zorder=5)

ax.text(bx0+bw_total/2, b_base-0.25, r'$\hat{d} = 1$',
        fontsize=8, fontweight='bold', color=C['accent'], ha='center', zorder=6)


# ═══════════════════════════════════════════════
# LAYER 3 — Task Comparison
# ═══════════════════════════════════════════════
ty = -0.02

ax.text(1.55, ty, 'Binary:  real vs. synthetic',
        fontsize=6, color=C['binary'], fontstyle='italic', ha='center', zorder=6)

ax.text(2.60, ty, 'vs.', fontsize=5.5, color='#BBBBBB', ha='center', zorder=6)

ax.add_patch(FancyBboxPatch(
    (2.90, ty-0.09), 3.80, 0.18,
    boxstyle='round,pad=0.02,rounding_size=0.08',
    fc=C['ours_bg'], ec=C['ours_bd'], lw=0.5, zorder=3))

ax.text(3.02, ty, r'Ours:  $\hat{d} \in \{0, 1, \ldots, K\}$',
        fontsize=7, fontweight='bold', color=C['ours_text'], ha='left', zorder=6)
ax.text(5.02, ty, '(ordinal depth estimation)',
        fontsize=5.5, color=C['ours_sub'], fontstyle='italic', ha='left', zorder=6)

# ── Save ──
out = '/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/figures'
fig.savefig(f'{out}/fig_problem_illustration.png', dpi=300, facecolor='white')
fig.savefig(f'{out}/fig_problem_illustration.pdf', facecolor='white')
plt.close()
print('DONE: fig_problem_illustration.png + .pdf')
