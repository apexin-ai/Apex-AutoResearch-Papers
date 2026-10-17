import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.10,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

OUTDIR = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper'

C_GREEN_BG, C_GREEN_BD, C_GREEN_TXT = '#D5F5E3', '#27AE60', '#1E8449'
C_YELLOW_BG, C_YELLOW_BD, C_YELLOW_TXT = '#FCF3CF', '#F39C12', '#B7950B'
C_ORANGE_BG, C_ORANGE_BD, C_ORANGE_TXT = '#FDEBD0', '#E67E22', '#CA6F1E'
C_RED_BG, C_RED_BD, C_RED_TXT = '#FADBD8', '#E74C3C', '#C0392B'
C_BLUE_BG, C_BLUE_BD = '#D6EAF8', '#3498DB'
C_DARK, C_GRAY, C_LGRAY = '#2C3E50', '#7F8C8D', '#BDC3C7'

SHADOW = [pe.withSimplePatchShadow(offset=(1.2, -1.2), shadow_rgbFace='#bbbbbb', alpha=0.10)]


def rbox(ax, x, y, w, h, fc, ec, lw=0.6, text=None, sub=None,
         fs=11, sfs=8, tc=C_DARK, shadow=True, zorder=2):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.015",
                         facecolor=fc, edgecolor=ec, linewidth=lw, zorder=zorder)
    if shadow:
        box.set_path_effects(SHADOW)
    ax.add_patch(box)
    if text:
        ty = y + h * 0.60 if sub else y + h * 0.50
        ax.text(x + w/2, ty, text, fontsize=fs, fontweight='bold',
                ha='center', va='center', color=tc, zorder=zorder+1)
    if sub:
        ax.text(x + w/2, y + h * 0.28, sub, fontsize=sfs, ha='center',
                va='center', color=C_GRAY, fontstyle='italic', zorder=zorder+1)


def farrow(ax, s, e, color='#AAAAAA', lw=0.8, style='->', ms=9, zorder=3):
    a = FancyArrowPatch(s, e, arrowstyle=style, color=color, linewidth=lw,
                        mutation_scale=ms, zorder=zorder)
    ax.add_patch(a)


fig = plt.figure(figsize=(16.5, 4.5))
gs = fig.add_gridspec(1, 3, width_ratios=[1.0, 1.15, 1.0], wspace=0.28)

# ================================================================
# Panel (a): The Puzzle
# ================================================================
ax = fig.add_subplot(gs[0])
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.08, 1.08)
ax.axis('off')

ax.text(-0.03, 1.06, '(a)', fontsize=13, fontweight='bold', color=C_DARK,
        transform=ax.transAxes, va='top')
ax.text(0.07, 1.06, 'The Puzzle', fontsize=11, fontstyle='italic', color=C_GRAY,
        transform=ax.transAxes, va='top')

# Observation box
obs_cx, obs_cy = 0.50, 0.94
obs_w, obs_h = 0.30, 0.06
ob = FancyBboxPatch((obs_cx - obs_w/2, obs_cy - obs_h/2), obs_w, obs_h,
                     boxstyle="round,pad=0.008", facecolor='#F7F9F9',
                     edgecolor=C_LGRAY, linewidth=0.7, zorder=2)
ob.set_path_effects(SHADOW)
ax.add_patch(ob)
ax.text(obs_cx, obs_cy, 'Robot Observation', fontsize=8.5, ha='center',
        va='center', color=C_GRAY)

# Branches
branches = [
    {'name': 'Linear Projection', 'x': 0.14, 'border': '#7DCEA0', 'fill': '#82C99B',
     'cv': 'CV = 0.055', 'pattern': 'uniform'},
    {'name': 'MLP Projector', 'x': 0.50, 'border': '#F0B27A', 'fill': '#E69F00',
     'cv': 'CV = 0.215', 'pattern': 'gradient'},
    {'name': 'Pixel-Shuffle', 'x': 0.86, 'border': '#EC7063', 'fill': '#D55E00',
     'cv': 'CV = 0.314', 'pattern': 'heterogeneous'},
]

conn_cy = 0.72
conn_w, conn_h = 0.22, 0.075
sq_cy = 0.42
sq_size = 0.055
sq_gap = 0.007
n_sq = 8

for b in branches:
    bx = b['x']

    farrow(ax, (obs_cx, obs_cy - obs_h/2 - 0.005),
           (bx, conn_cy + conn_h/2 + 0.008),
           color=C_LGRAY, lw=0.6, style='->', ms=7)

    cbox = FancyBboxPatch((bx - conn_w/2, conn_cy - conn_h/2), conn_w, conn_h,
                           boxstyle="round,pad=0.010", facecolor='white',
                           edgecolor=b['border'], linewidth=1.0, zorder=2)
    cbox.set_path_effects(SHADOW)
    ax.add_patch(cbox)
    ax.text(bx, conn_cy, b['name'], fontsize=8, ha='center', va='center',
            color=C_DARK, fontweight='bold', zorder=3)

    farrow(ax, (bx, conn_cy - conn_h/2 - 0.005),
           (bx, sq_cy + sq_size/2 + 0.015),
           color=b['border'], lw=0.5, style='->', ms=7)

    total_w = n_sq * sq_size + (n_sq - 1) * sq_gap
    sx_start = bx - total_w / 2

    for i in range(n_sq):
        sx = sx_start + i * (sq_size + sq_gap)
        sy = sq_cy - sq_size / 2

        if b['pattern'] == 'uniform':
            a = 0.52 + 0.03 * np.sin(i * 0.7)
        elif b['pattern'] == 'gradient':
            a = 0.95 - i * 0.095
        else:
            a = [1.0, 0.12, 0.88, 0.10, 0.95, 0.14, 0.82, 0.08][i]

        r = FancyBboxPatch((sx, sy), sq_size, sq_size,
                            boxstyle="round,pad=0.002",
                            facecolor=b['fill'], edgecolor='#e0e0e0',
                            alpha=a, linewidth=0.3, zorder=2)
        ax.add_patch(r)

    ax.text(bx, sq_cy - sq_size/2 - 0.03, b['cv'],
            fontsize=8, ha='center', va='top', color=C_GRAY,
            family='serif')

# Bracket
bk_top = sq_cy - sq_size/2 - 0.06
bk_bot = bk_top - 0.035
ax.plot([0.02, 0.02, 0.50], [bk_top, bk_bot, bk_bot - 0.012],
        color=C_LGRAY, lw=0.6, solid_capstyle='round')
ax.plot([0.98, 0.98, 0.50], [bk_top, bk_bot, bk_bot - 0.012],
        color=C_LGRAY, lw=0.6, solid_capstyle='round')
ax.text(0.50, bk_bot - 0.04, 'Same input, different compressibility',
        fontsize=9, ha='center', va='top', color=C_GRAY, fontstyle='italic')

# ================================================================
# Panel (b): Two-Axis Framework
# ================================================================
ax = fig.add_subplot(gs[1])
ax.set_xlim(-0.18, 1.18)
ax.set_ylim(-0.14, 1.08)
ax.axis('off')

ax.text(-0.06, 1.06, '(b)', fontsize=13, fontweight='bold', color=C_DARK,
        transform=ax.transAxes, va='top')
ax.text(0.02, 1.06, 'Two-Axis Framework', fontsize=11, fontstyle='italic',
        color=C_GRAY, transform=ax.transAxes, va='top')

# Grid cells — shifted right to leave room for axis labels
gx0, gy0 = 0.25, 0.15
gw, gh = 0.30, 0.34
ggap = 0.04

cells = [
    (0, 0, C_GREEN_BG, C_GREEN_BD, '≥98% SR', C_GREEN_TXT, 'Tolerant', False),
    (0, 1, C_YELLOW_BG, C_YELLOW_BD, '~89% SR', C_YELLOW_TXT, 'Moderate loss', False),
    (1, 0, C_ORANGE_BG, C_ORANGE_BD, 'Cliff at k≤0.7', C_ORANGE_TXT, 'Threshold', False),
    (1, 1, C_RED_BG, C_RED_BD, '0–48% SR', C_RED_TXT, 'Catastrophic', True),
]

for col, row, bg, bd, main, mc, sub, hatch in cells:
    cx = gx0 + col * (gw + ggap)
    cy = gy0 + row * (gh + ggap)

    box = FancyBboxPatch((cx, cy), gw, gh, boxstyle="round,pad=0.012",
                          facecolor=bg, edgecolor=bd, linewidth=0.6, zorder=2)
    box.set_path_effects(SHADOW)
    ax.add_patch(box)

    if hatch:
        hb = FancyBboxPatch((cx, cy), gw, gh, boxstyle="round,pad=0.012",
                             facecolor='none', edgecolor='none',
                             hatch='///', alpha=0.12, zorder=2.5)
        ax.add_patch(hb)

    fs = 11 if len(main) <= 10 else 9.5
    ax.text(cx + gw/2, cy + gh * 0.58, main, fontsize=fs, fontweight='bold',
            ha='center', va='center', color=mc, zorder=3)
    ax.text(cx + gw/2, cy + gh * 0.30, sub, fontsize=8.5, ha='center',
            va='center', color=C_GRAY, fontstyle='italic', zorder=3)

# X-axis: Token Coupling (below grid)
mid_x = gx0 + gw + ggap/2
ax.text(mid_x, gy0 - 0.10, 'Token Coupling', fontsize=11, ha='center',
        va='top', fontweight='bold', color=C_DARK)
ax.annotate('', xy=(gx0 + 2*gw + ggap, gy0 - 0.045),
            xytext=(gx0, gy0 - 0.045),
            arrowprops=dict(arrowstyle='->', color=C_LGRAY, lw=0.8))
ax.text(gx0 + gw * 0.4, gy0 - 0.025, 'Independent', fontsize=8, ha='center',
        va='top', color=C_GRAY)
ax.text(gx0 + gw + ggap + gw * 0.6, gy0 - 0.025, 'Entangling', fontsize=8,
        ha='center', va='top', color=C_GRAY)

# Y-axis: Task Complexity — horizontal labels at arrow endpoints
y_ax = gx0 - 0.06
ax.annotate('', xy=(y_ax, gy0 + 2*gh + ggap + 0.01),
            xytext=(y_ax, gy0 - 0.01),
            arrowprops=dict(arrowstyle='->', color=C_LGRAY, lw=0.8))
ax.text(y_ax, gy0 - 0.025, 'Simple', fontsize=8, ha='right', va='top', color=C_GRAY)
ax.text(y_ax, gy0 + 2*gh + ggap + 0.035, 'Complex', fontsize=8, ha='center',
        va='bottom', color=C_GRAY)
ax.text(y_ax - 0.055, gy0 + gh + ggap/2, 'Task\nComplexity', fontsize=10,
        ha='center', va='center', fontweight='bold', color=C_DARK, rotation=90,
        linespacing=1.2)

# Diagonal risk arrow (right side)
ar_x = gx0 + 2*gw + ggap + 0.06
ar_y0, ar_y1 = gy0, gy0 + 2 * gh + ggap
farrow(ax, (ar_x, ar_y0), (ar_x, ar_y1), color=C_RED_BD, lw=1.3, style='->', ms=11)
for frac, c in [(0.0, C_GREEN_BD), (0.33, C_YELLOW_BD), (0.66, C_ORANGE_BD)]:
    ax.plot(ar_x, ar_y0 + frac * (ar_y1 - ar_y0), 'o', color=c, markersize=3.5, zorder=4)
ax.text(ar_x + 0.04, (ar_y0 + ar_y1)/2, 'Increasing\npruning risk',
        fontsize=7.5, ha='left', va='center', color=C_GRAY,
        fontstyle='italic', rotation=90, linespacing=1.3)

# ================================================================
# Panel (c): Diagnose-then-Compress
# ================================================================
ax = fig.add_subplot(gs[2])
ax.set_xlim(-0.14, 1.14)
ax.set_ylim(-0.05, 1.08)
ax.axis('off')

ax.text(-0.04, 1.06, '(c)', fontsize=13, fontweight='bold', color=C_DARK,
        transform=ax.transAxes, va='top')
ax.text(0.06, 1.06, 'Diagnose-then-Compress', fontsize=11, fontstyle='italic',
        color=C_GRAY, transform=ax.transAxes, va='top')

# CV Diagnostic box
dw, dh = 0.52, 0.14
dx = 0.50 - dw/2
dy = 0.78
rbox(ax, dx, dy, dw, dh, C_BLUE_BG, C_BLUE_BD, lw=0.9,
     text='CV Diagnostic', sub='One forward pass', fs=12, sfs=9, tc=C_DARK)

# Three outcome branches
outs = [
    {'x': 0.17, 'label': 'CV < 0.1', 'name': 'Uniform', 'meth': 'L2-norm pruning',
     'bg': C_GREEN_BG, 'bd': C_GREEN_BD, 'tc': C_GREEN_TXT},
    {'x': 0.50, 'label': '0.15 – 0.22', 'name': 'Graded', 'meth': 'Attention scoring',
     'bg': C_YELLOW_BG, 'bd': C_YELLOW_BD, 'tc': C_YELLOW_TXT},
    {'x': 0.83, 'label': 'CV > 0.3', 'name': 'Catastrophic', 'meth': 'VTR re-encoding',
     'bg': C_RED_BG, 'bd': C_RED_BD, 'tc': C_RED_TXT},
]

ow, oh = 0.25, 0.20
oy = 0.18

for o in outs:
    asx = 0.50 + (o['x'] - 0.50) * 0.4
    asy = dy - 0.005
    aey = oy + oh + 0.008

    farrow(ax, (asx, asy), (o['x'], aey), color='#B0B0B0', lw=0.8, style='->', ms=9)

    lx = (asx + o['x']) / 2
    ly = (asy + aey) / 2 + 0.02
    dx_off = -0.06 if o['x'] < 0.3 else (0.06 if o['x'] > 0.7 else 0.0)
    ax.text(lx + dx_off, ly, o['label'], fontsize=7.5, ha='center', va='center',
            color=C_GRAY,
            bbox=dict(facecolor='white', edgecolor='none', pad=2, alpha=0.9),
            zorder=4)

    rbox(ax, o['x'] - ow/2, oy, ow, oh, o['bg'], o['bd'], lw=0.7,
         text=o['name'], sub=o['meth'], fs=10.5, sfs=7, tc=o['tc'])

# ================================================================
fig.savefig(f'{OUTDIR}/fig_hero_overview.png')
fig.savefig(f'{OUTDIR}/fig_hero_overview.pdf')
plt.close()
print('Saved fig_hero_overview.png and fig_hero_overview.pdf')
