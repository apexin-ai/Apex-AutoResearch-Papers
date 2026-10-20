# plot_fig2_framework.py  -- Framework overview (Figure 2)
# Three-panel: Chain Construction | Feature Extraction | Classification + DDR

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

BLUE   = '#0072B2'
ORANGE = '#E69F00'
GRAY   = '#888888'
LGRAY  = '#F5F5F5'
MGRAY  = '#DDDDDD'
DARK   = '#333333'
WHITE  = '#FFFFFF'
DEPTH  = ['#FFFFFF', '#ACCBE1', '#5A9ECF', '#2171B5', '#08306B']

fig, ax = plt.subplots(figsize=(6.1, 2.7))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
T = ax.transAxes

def rbox(x, y, w, h, fc, ec, lw=0.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.003",
                                fc=fc, ec=ec, lw=lw, zorder=2,
                                transform=T, clip_on=False))

def tx(x, y, s, **kw):
    d = dict(ha='center', va='center', fontsize=7, color=DARK, zorder=5, transform=T)
    d.update(kw); ax.text(x, y, s, **d)

def arr(x0, y0, x1, y1, c='#555', lw=0.8):
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color=c, lw=lw),
                xycoords='axes fraction', textcoords='axes fraction', zorder=3)

# ── Section panels ──
S1, S2 = 0.335, 0.67
for x0, x1, lab in [(0.005, S1-0.005, 'Chain Construction'),
                     (S1+0.005, S2-0.005, 'Feature Extraction'),
                     (S2+0.005, 0.995, 'Classification + DDR')]:
    rbox(x0, 0.01, x1-x0, 0.96, LGRAY, MGRAY, 0.6)
    tx((x0+x1)/2, 0.96, lab, fontsize=7.5, fontweight='bold', va='top')

# ════════ SECTION 1 ════════
bw, bh = 0.055, 0.075
cy, gap = 0.74, 0.008
for i in range(5):
    bx = 0.012 + i*(bw+gap)
    rbox(bx, cy-bh/2, bw, bh, DEPTH[i], '#666', 0.5)
    tc = WHITE if i >= 3 else DARK
    tx(bx+bw/2, cy, f'gen-{i}', fontsize=5.5, color=tc, fontweight='medium')
    if i < 4:
        arr(bx+bw+0.001, cy, bx+bw+gap-0.001, cy, '#777', 0.5)

tx(0.012+2*(bw+gap)+bw/2, cy+0.11, 'Generator $G$',
   fontsize=6.5, fontstyle='italic', color='#555')
ax.annotate('', xy=(0.012+3.5*(bw+gap)+bw/2, cy+0.075),
            xytext=(0.012+0.5*(bw+gap)+bw/2, cy+0.075),
            arrowprops=dict(arrowstyle='->', color='#aaa', lw=0.4,
                           connectionstyle='arc3,rad=-0.15'),
            xycoords='axes fraction', textcoords='axes fraction', zorder=2)

tx(S1/2, 0.45, '8 generators, 5 families (0.6B–8B)', fontsize=6, color='#555')
tx(S1/2, 0.35, '3 prompts: continuation,', fontsize=5.5, color='#555')
tx(S1/2, 0.27, 'elaboration, rewriting', fontsize=5.5, color='#555')
tx(S1/2, 0.16, r'$\tau$=0.7, top-$p$=0.9, max 256 tok.', fontsize=5.5, color='#555')

for i in range(5):
    lx = 0.04 + i*0.052
    ax.add_patch(Rectangle((lx, 0.05), 0.042, 0.06, fc=DEPTH[i], ec='#aaa', lw=0.3,
                            zorder=2, transform=T, clip_on=False))
    tc = WHITE if i >= 3 else DARK
    tx(lx+0.021, 0.08, str(i), fontsize=5.5, color=tc)
tx(0.04+2*0.052+0.021, 0.02, 'depth', fontsize=5.5, color='#666')

# ════════ SECTION 2 ════════
mid = (S1+S2)/2
rw = 0.14
rbox(mid-rw/2, 0.85, rw, 0.07, '#D4E8D4', '#4A8C4A', 0.7)
tx(mid, 0.885, 'Pythia-410M', fontsize=6.5, color='#2D5A2D', fontweight='bold')
arr(mid, 0.85, mid, 0.81, '#4A8C4A', 0.7)

fx_l, fx_r = S1+0.013, S2-0.013
col_gap = 0.007
box_w = (fx_r-fx_l-col_gap)/2
box_h = 0.06

# Drifting
dy = 0.76
tx(fx_l, dy, 'Drifting  |$\\rho$| > 0.4', fontsize=6, color=BLUE,
   fontweight='bold', ha='left')
for j, f in enumerate(['entropy_mean', 'entropy_min', 'TTR', 'hapax_ratio']):
    r, c = j//2, j%2
    bx = fx_l + c*(box_w+col_gap)
    by = dy - 0.07 - r*(box_h+0.015)
    rbox(bx, by, box_w, box_h, '#D6E8F5', BLUE, 0.5)
    tx(bx+box_w/2, by+box_h/2, f, fontsize=5.8, color=BLUE)

# Shape
sy = dy - 0.07 - 2*(box_h+0.015) - 0.015
tx(fx_l, sy, 'Shape  |$\\rho$| < 0.10', fontsize=6, color=ORANGE,
   fontweight='bold', ha='left')
for j, f in enumerate(['entropy_max', 'tail_decay']):
    bx = fx_l + j*(box_w+col_gap)
    by = sy - 0.07
    rbox(bx, by, box_w, box_h, '#FDF0D5', ORANGE, 0.5)
    tx(bx+box_w/2, by+box_h/2, f, fontsize=5.8, color='#B8860B')

# Intermediate
iy = sy - 0.07 - box_h - 0.025
tx(fx_l, iy, 'Intermediate', fontsize=6, color=GRAY, fontweight='bold', ha='left')
by = iy - 0.07
rbox(fx_l, by, box_w, box_h, '#EEEEEE', GRAY, 0.5)
tx(fx_l+box_w/2, by+box_h/2, 'entropy_std', fontsize=5.8, color='#555')

arr(S1-0.01, 0.72, S1+0.012, 0.72, '#444', 1.0)

# ════════ SECTION 3 ════════
arr(S2-0.01, 0.72, S2+0.012, 0.72, '#444', 1.0)
s3m = (S2+1)/2

xw = 0.17
rbox(s3m-xw/2, 0.84, xw, 0.08, '#E8D4E8', '#6A3D6A', 0.7)
tx(s3m, 0.88, 'XGBoost (LOGO CV)', fontsize=6.5, color='#4A2D4A', fontweight='bold')
arr(s3m, 0.84, s3m, 0.79, '#555')

cw, cgap = 0.058, 0.008
cx_start = s3m - (3*cw+2*cgap)/2
for k, (cls, col, tc) in enumerate([('gen-0', DEPTH[0], DARK),
                                     ('gen-1', DEPTH[1], DARK),
                                     ('gen-2+', DEPTH[3], WHITE)]):
    cx = cx_start + k*(cw+cgap)
    rbox(cx, 0.67, cw, 0.08, col, '#666', 0.5)
    tx(cx+cw/2, 0.71, cls, fontsize=6, color=tc, fontweight='medium')

# ── DDR plot ──
ddx, ddy, ddw, ddh = S2+0.012, 0.03, 0.99-S2-0.012, 0.58
rbox(ddx, ddy, ddw, ddh, WHITE, '#BBB', 0.5)
tx(ddx+ddw/2, ddy+ddh-0.02, 'Differential Depth Response',
   fontsize=6, fontweight='bold')

pl, pr = ddx+0.055, ddx+ddw-0.015
pb, pt = ddy+0.10, ddy+ddh-0.10

ax.plot([pl, pr], [pb, pb], color='#999', lw=0.4, zorder=2, transform=T, clip_on=False)
ax.plot([pl, pl], [pb, pt], color='#999', lw=0.4, zorder=2, transform=T, clip_on=False)

for i in range(5):
    tx_ = pl + i*(pr-pl)/4
    ax.plot([tx_, tx_], [pb-0.012, pb], color='#999', lw=0.3, zorder=2,
            transform=T, clip_on=False)
    tx(tx_, pb-0.032, str(i), fontsize=6, color='#666')
tx((pl+pr)/2, pb-0.065, 'depth', fontsize=6, color='#555')
tx(pl-0.03, (pb+pt)/2, 'value', fontsize=5.5, color='#555', rotation=90)

xs = np.array([pl + i*(pr-pl)/4 for i in range(5)])

yd = pb + np.array([0.92, 0.75, 0.58, 0.48, 0.42])*(pt-pb)
ax.plot(xs, yd, color=BLUE, lw=1.2, marker='o', ms=2.5, zorder=4,
        transform=T, clip_on=False)

ys = pb + np.array([0.50, 0.52, 0.49, 0.51, 0.50])*(pt-pb)
ax.plot(xs, ys, color=ORANGE, lw=1.2, marker='s', ms=2.5, zorder=4,
        transform=T, clip_on=False)

yi = pb + np.array([0.72, 0.64, 0.57, 0.53, 0.50])*(pt-pb)
ax.plot(xs, yi, color=GRAY, lw=0.9, marker='^', ms=2, ls='--', zorder=4,
        transform=T, clip_on=False)

# Endpoint labels with vertical spread to avoid overlap
label_x = pr + 0.006
# Spread labels vertically: use fixed offsets from top of plot
label_positions = [
    ('Drifting', BLUE, yd[-1], pt - 0.06),
    ('Shape', ORANGE, ys[-1], (pb+pt)/2 + 0.02),
    ('Interm.', GRAY, yi[-1], (pb+pt)/2 - 0.06),
]
for lab, col, y_data, y_label in label_positions:
    # Small connecting line from data point to label
    ax.plot([pr, label_x-0.002], [y_data, y_label], color=col, lw=0.4,
            ls=':', transform=T, clip_on=False, zorder=3)
    tx(label_x, y_label, lab, fontsize=5.5, color=col, ha='left', va='center')

out = '/root/gen-depth-fingerprint/paper/figures'
fig.savefig(f'{out}/fig2_framework.pdf', format='pdf')
fig.savefig(f'{out}/fig2_framework.png', format='png')
print(f"Saved: {out}/fig2_framework.pdf + .png")
