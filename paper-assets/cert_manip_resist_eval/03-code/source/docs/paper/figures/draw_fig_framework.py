"""Figure 1: The Shifting Bottleneck — concept figure for EMNLP 2026."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse
import matplotlib.patheffects as pe
import matplotlib.colors as mcolors
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
    'font.size': 11,
    'figure.dpi': 300, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42, 'ps.fonttype': 42,
})
SANS = {'fontfamily': 'sans-serif'}

C_BLUE = '#0072B2'; C_RED = '#D55E00'; C_TEAL = '#009E73'
C_ORANGE = '#E69F00'; C_PURPLE = '#7B2D8E'; C_PINK = '#CC79A7'
C_DARK = '#2A2A2A'
FILL_BLUE = '#C5DFF0'; FILL_RED = '#F4CCCC'; FILL_TEAL = '#B2DFDB'
FILL_ORANGE = '#FFE0B2'; FILL_PURPLE = '#E1BEE7'; FILL_PINK = '#F8BBD0'
BOX_BG = '#F5F5F5'; BOX_EC = '#DDDDDD'; PANEL_EC = '#DDDDDD'
BG_A = '#FDF0EF'   # panel (a): light warm red — η_max dominates
BG_B = '#F3EDF7'   # panel (b): light lavender — transition
BG_C = '#EDF4FB'   # panel (c): light cool blue — K_eff dominates

FIG_W, FIG_H = 16, 5.5
L_FRAC, C_FRAC, R_FRAC = 0.355, 0.22, 0.355
H_FRAC = 0.96
GAP = 0.025

def get_asp(frac_w):
    return (H_FRAC * FIG_H) / (frac_w * FIG_W)

def circ(ax, x, y, r, fill, edge, label, asp, lw=1.5, fs=15):
    w, h = 2*r/asp, 2*r
    ax.add_patch(Ellipse((x+0.003, y-0.003), w, h,
                         fc='#00000008', ec='none', transform=ax.transAxes, zorder=1))
    ax.add_patch(Ellipse((x, y), w, h,
                         fc=fill, ec=edge, lw=lw, transform=ax.transAxes, zorder=2))
    ax.text(x, y, label, ha='center', va='center', fontsize=fs,
            color=C_DARK, transform=ax.transAxes, zorder=3)

def edge_pt(x, y, r, asp, tx, ty):
    dx = (tx - x) * asp; dy = ty - y
    a = np.arctan2(dy, dx)
    return x + r/asp * np.cos(a), y + r * np.sin(a)

def diam(ax, x, y, s, color, asp, label_text='Adversary', label_pos='above'):
    sx = s / asp * 0.7
    vs = [(x, y+s), (x+sx, y), (x, y-s), (x-sx, y)]
    ax.add_patch(plt.Polygon([(v[0]+0.002, v[1]-0.002) for v in vs],
                             fc='#00000008', ec='none', transform=ax.transAxes, zorder=1))
    ax.add_patch(plt.Polygon(vs, fc=color, ec='#B34A00', lw=1.0,
                             transform=ax.transAxes, zorder=2))
    if label_pos == 'above':
        ax.text(x, y+s+0.018, label_text, ha='center', va='bottom',
                fontsize=8, color=C_RED, fontstyle='italic',
                transform=ax.transAxes, zorder=3, **SANS)
    elif label_pos == 'right':
        ax.text(x+sx+0.015, y, label_text, ha='left', va='center',
                fontsize=8, color=C_RED, fontstyle='italic',
                transform=ax.transAxes, zorder=3, **SANS)

def rbox(ax, cx, cy, w, h, lines, bg=BOX_BG, ec=BOX_EC):
    ax.add_patch(FancyBboxPatch((cx-w/2, cy-h/2), w, h,
                 boxstyle='round,pad=0.005,rounding_size=0.012',
                 fc=bg, ec=ec, lw=0.7, transform=ax.transAxes, zorder=2))
    n = len(lines)
    for i, (txt, kw) in enumerate(lines):
        dy = (n-1)*0.018 - i*0.036 if n > 1 else 0
        ax.text(cx, cy+dy, txt, ha='center', va='center',
                transform=ax.transAxes, zorder=3, **kw)

def ln(ax, x1, y1, x2, y2, c='#CCCCCC', lw=0.6, ls='-', alpha=1):
    ax.plot([x1,x2], [y1,y2], color=c, lw=lw, ls=ls, alpha=alpha,
            transform=ax.transAxes, zorder=1, clip_on=False)

def arr(ax, x1, y1, x2, y2, c=C_RED, lw=2, ls='-', alpha=1, ms=10):
    a = FancyArrowPatch((x1,y1), (x2,y2),
        arrowstyle='->,head_length=4,head_width=2.5',
        color=c, lw=lw, linestyle=ls, alpha=alpha,
        mutation_scale=ms, shrinkA=0, shrinkB=0,
        transform=ax.transAxes, zorder=4, clip_on=False)
    ax.add_patch(a)


# ── figure layout ──
fig = plt.figure(figsize=(FIG_W, FIG_H))
y0 = (1 - H_FRAC) / 2
x0_l = 0.02
x0_c = x0_l + L_FRAC + GAP
x0_r = x0_c + C_FRAC + GAP

ax_l = fig.add_axes([x0_l, y0, L_FRAC, H_FRAC])
ax_c = fig.add_axes([x0_c, y0, C_FRAC, H_FRAC])
ax_r = fig.add_axes([x0_r, y0, R_FRAC, H_FRAC])

for ax in [ax_l, ax_c, ax_r]:
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')

asp_lr = get_asp(L_FRAC)
asp_c  = get_asp(C_FRAC)
R = 0.078

# ═══════════════════════════════════════════════════════════════════
# Panel (a): K = 3
# ═══════════════════════════════════════════════════════════════════
ax = ax_l; asp = asp_lr

ax.add_patch(FancyBboxPatch((0.02, 0.02), 0.96, 0.96,
    boxstyle='round,pad=0,rounding_size=0.020',
    fc=BG_A, ec=PANEL_EC, lw=0.6, transform=ax.transAxes, zorder=0))

ax.text(0.06, 0.96, '(a)', fontsize=15, fontweight='bold', color=C_DARK,
        va='top', transform=ax.transAxes)
ax.text(0.17, 0.96, '$K = 3$', fontsize=12, color=C_DARK,
        va='top', transform=ax.transAxes)

j1 = (0.26, 0.78)
j2 = (0.10, 0.48)
j3 = (0.42, 0.48)

circ(ax, *j1, R, FILL_BLUE, C_BLUE, '$J_1$', asp)
circ(ax, *j2, R, FILL_BLUE, C_BLUE, '$J_2$', asp)
circ(ax, *j3, R, FILL_RED, C_RED, '$J_3$', asp, lw=2.5)

for a, b in [(j1,j2), (j2,j3), (j1,j3)]:
    ln(ax, a[0], a[1], b[0], b[1], c='#D0D0D0', lw=0.7)

# adversary
ADV_S = 0.055
adv = (0.70, 0.78)
diam(ax, *adv, ADV_S, C_RED, asp)

# thick attack arrow
a_end = edge_pt(j3[0], j3[1], R, asp, adv[0], adv[1])
arr(ax, adv[0]-0.015, adv[1]-ADV_S, a_end[0], a_end[1],
    c=C_RED, lw=3.5, alpha=0.85, ms=15)

ax.text(0.57, 0.73, 'attack', fontsize=8.5, color=C_RED, fontstyle='italic',
        ha='center', va='bottom', transform=ax.transAxes, zorder=5, **SANS,
        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

# annotation
ax.text(0.66, 0.38, '1 flip =\nmajority\ncompromised', fontsize=7, ha='center',
        va='center', color='#AAAAAA', fontstyle='italic',
        transform=ax.transAxes, **SANS, linespacing=1.2)

# dashed line J₃ → majority vote
ln(ax, j3[0]-0.02, j3[1]-R-0.005, 0.30, 0.315, c='#CCCCCC', lw=0.5, ls='--')

# majority vote box
rbox(ax, 0.30, 0.28, 0.35, 0.055,
     [('Majority vote: $t = 2$', {'fontsize': 10.5, 'color': C_DARK})],
     bg='#FAFAFA', ec='#D0D0D0')

# bottleneck
rbox(ax, 0.50, 0.085, 0.70, 0.10,
     [('Bottleneck: $\\eta_{\\max}$',
       {'fontsize': 13, 'fontweight': 'bold', 'color': C_DARK}),
      ('(individual weakness)',
       {'fontsize': 9.5, 'fontstyle': 'italic', 'color': '#999999'})])


# ═══════════════════════════════════════════════════════════════════
# Panel (b): Transition
# ═══════════════════════════════════════════════════════════════════
ax = ax_c

ax.add_patch(FancyBboxPatch((0.03, 0.02), 0.94, 0.96,
    boxstyle='round,pad=0,rounding_size=0.020',
    fc=BG_B, ec=PANEL_EC, lw=0.6, transform=ax.transAxes, zorder=0))

ax.text(0.10, 0.96, '(b)', fontsize=15, fontweight='bold', color=C_DARK,
        va='top', transform=ax.transAxes, zorder=6)
ax.text(0.10, 0.88, 'Transition', fontsize=11, fontweight='bold', color=C_DARK,
        va='top', transform=ax.transAxes, zorder=6)

ln(ax, 0.5, 0.12, 0.5, 0.82, c='#D0D0D0', lw=0.7, ls='--')

ax.text(0.50, 0.50, '$K^* \\in (3,\\, 5)$', fontsize=18, ha='center', va='center',
        fontstyle='italic', color=C_DARK, transform=ax.transAxes, zorder=6)

arr(ax, 0.10, 0.72, 0.90, 0.72, c='#BBBBBB', lw=1.0, alpha=0.6, ms=8)
ax.text(0.50, 0.755, '$\\eta_{\\max}$ attenuates', fontsize=9, ha='center',
        va='bottom', fontstyle='italic', color='#AAAAAA',
        transform=ax.transAxes, zorder=6, **SANS)

arr(ax, 0.10, 0.30, 0.90, 0.30, c=C_BLUE, lw=1.0, alpha=0.6, ms=8)
ax.text(0.50, 0.335, '$K_{\\mathrm{eff}}$ emerges', fontsize=9, ha='center',
        va='bottom', fontstyle='italic', color=C_BLUE,
        transform=ax.transAxes, zorder=6, **SANS)


# ═══════════════════════════════════════════════════════════════════
# Panel (c): K ≥ 5
# ═══════════════════════════════════════════════════════════════════
ax = ax_r; asp = asp_lr

ax.add_patch(FancyBboxPatch((0.02, 0.02), 0.96, 0.96,
    boxstyle='round,pad=0,rounding_size=0.020',
    fc=BG_C, ec=PANEL_EC, lw=0.6, transform=ax.transAxes, zorder=0))

ax.text(0.06, 0.96, '(c)', fontsize=15, fontweight='bold', color=C_DARK,
        va='top', transform=ax.transAxes)
ax.text(0.17, 0.96, '$K \\geq 5$', fontsize=12, color=C_DARK,
        va='top', transform=ax.transAxes)

# pentagon
pcx, pcy = 0.35, 0.57
pr_x = 0.21; pr_y = pr_x * asp
angles_deg = [90, 162, 234, 306, 18]
judge_info = [
    ('$J_1$', FILL_TEAL, C_TEAL),
    ('$J_2$', FILL_BLUE, C_BLUE),
    ('$J_3$', FILL_ORANGE, C_ORANGE),
    ('$J_4$', FILL_PURPLE, C_PURPLE),
    ('$J_5$', FILL_PINK, C_PINK),
]

jpos = []
for deg in angles_deg:
    rad = np.radians(deg)
    jpos.append((pcx + pr_x*np.cos(rad), pcy + pr_y*np.sin(rad)))

# MI connections (subtle)
mi_pairs = [(0,1,0.4), (0,4,0.35), (1,2,0.3), (2,3,0.35), (3,4,0.25),
            (0,2,0.12), (1,3,0.15), (2,4,0.12)]
for i, j, a in mi_pairs:
    ln(ax, jpos[i][0], jpos[i][1], jpos[j][0], jpos[j][1],
       c='#D5D5D5', lw=0.4, ls='--', alpha=a)

for (jx, jy), (lbl, fill, edge) in zip(jpos, judge_info):
    circ(ax, jx, jy, R, fill, edge, lbl, asp)

# adversary
adv = (0.84, 0.57)
diam(ax, *adv, ADV_S, C_RED, asp, label_pos='right')

# fan-out dashed arrows (edge to edge)
for jx, jy in jpos:
    ax0, ay0 = edge_pt(adv[0], adv[1], ADV_S, asp, jx, jy)
    ax1, ay1 = edge_pt(jx, jy, R, asp, adv[0], adv[1])
    arr(ax, ax0, ay0, ax1, ay1,
        c=C_RED, lw=1.0, ls=(0,(4,3)), alpha=0.4, ms=7)

ax.text(adv[0]-0.01, adv[1]-ADV_S-0.03, 'must flip $\\geq\\!3$',
        fontsize=8.5, ha='center', va='top', color=C_RED, fontstyle='italic',
        transform=ax.transAxes, zorder=5, **SANS)

# bottleneck
rbox(ax, 0.50, 0.085, 0.70, 0.10,
     [('Bottleneck: $K_{\\mathrm{eff}}$',
       {'fontsize': 13, 'fontweight': 'bold', 'color': C_DARK}),
      ('(structural diversity)',
       {'fontsize': 9.5, 'fontstyle': 'italic', 'color': '#999999'})])

# ── save ──
OUT = '/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/figures'
fig.savefig(f'{OUT}/fig_framework.png', dpi=300, facecolor='white')
fig.savefig(f'{OUT}/fig_framework.pdf', dpi=300, facecolor='white')
plt.close()
print('Done')
