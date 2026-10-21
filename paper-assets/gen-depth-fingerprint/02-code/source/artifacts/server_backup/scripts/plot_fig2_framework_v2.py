"""Figure 2: Framework overview -- Gen-Depth Fingerprint (v3).
Three-panel: Chain Construction | Feature Extraction | Classification & DDR
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# ── Palette ──
BG       = '#F5F7FA'
BLUE     = '#2171B5'
BLUE_LT  = '#D6E8F5'
ORANGE   = '#E6550D'
ORANGE_LT= '#FDE8D0'
GRAY     = '#999999'
GRAY_LT  = '#EEEEEE'
DARK     = '#333333'
WHITE    = '#FFFFFF'
DEPTH    = ['#F7FBFF','#BDD7E7','#6BAED6','#2171B5','#08519C']
DEPTH_EC = ['#9ECAE1','#6BAED6','#3182BD','#08519C','#063E78']

fig, ax = plt.subplots(figsize=(6.75, 3.0))
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
T = ax.transAxes
S1, S2 = 0.345, 0.67

# ── Helpers ──
def rbox(x, y, w, h, fc, ec='#CCC', lw=0.6, zorder=2):
    ax.add_patch(FancyBboxPatch((x,y), w, h, boxstyle="round,pad=0.005",
        fc=fc, ec=ec, lw=lw, zorder=zorder, transform=T, clip_on=False))

def tx(x, y, s, **kw):
    d = dict(ha='center', va='center', fontsize=7, color=DARK, zorder=5, transform=T)
    d.update(kw); return ax.text(x, y, s, **d)

def arr(x0, y0, x1, y1, c='#555', lw=0.8, cs=None, hw=5, hl=5):
    props = dict(arrowstyle=f'->,head_width={hw/72*2},head_length={hl/72*2}',
                 color=c, lw=lw)
    if cs: props['connectionstyle'] = cs
    ax.annotate('', xy=(x1,y1), xytext=(x0,y0), arrowprops=props,
        xycoords='axes fraction', textcoords='axes fraction', zorder=3)

def bigarr(x0, y0, x1, y1, c=DARK, lw=1.5):
    """Prominent cross-panel arrow."""
    ax.annotate('', xy=(x1,y1), xytext=(x0,y0),
        arrowprops=dict(arrowstyle='->,head_width=0.15,head_length=0.1',
                        color=c, lw=lw),
        xycoords='axes fraction', textcoords='axes fraction', zorder=4)

# ── Background panels + titles ──
for x0, x1, title in [
    (0.005, S1-0.005, 'Chain Construction'),
    (S1+0.005, S2-0.005, 'Feature Extraction'),
    (S2+0.005, 0.995, 'Classification & DDR')]:
    rbox(x0, 0.01, x1-x0, 0.96, BG, '#D0D4DA', 0.8, zorder=0)
    tx((x0+x1)/2, 0.96, title, fontsize=9, fontweight='bold', va='top')

for sx in [S1, S2]:
    ax.plot([sx,sx], [0.03,0.93], color='#C0C4CA', lw=0.5, ls='--',
        transform=T, clip_on=False, zorder=1)

# ═══════════════════════════════════════
# SECTION 1: Chain Construction
# ═══════════════════════════════════════
ml = S1/2

# Seed text box
sw, sh = 0.22, 0.055
rbox(ml-sw/2, 0.86, sw, sh, DEPTH[0], DEPTH_EC[0], 0.7)
tx(ml, 0.888, 'Seed text (gen-0)', fontsize=6.5, fontweight='bold')

arr(ml, 0.855, ml, 0.81, c=DARK, lw=1.0)

# Generator G box
gw, gh = 0.19, 0.06
gy = 0.745
rbox(ml-gw/2, gy, gw, gh, '#FFF3E0', '#E6550D', 0.8)
tx(ml, gy+gh/2, 'Generator $G$', fontsize=7.5, fontweight='bold', color='#BF360C')

# Prominent loop arrow using manual path
loop_x = ml + gw/2 + 0.015
loop_bot = gy + 0.01
loop_top = gy + gh - 0.01
# Draw a visible loop: exit right from bottom, curve right, re-enter top
ax.annotate('', xy=(loop_x-0.008, loop_top), xytext=(loop_x-0.008, loop_bot),
    arrowprops=dict(arrowstyle='->,head_width=0.08,head_length=0.06',
                    connectionstyle='arc3,rad=-3.5', color='#D84315', lw=1.0),
    xycoords='axes fraction', textcoords='axes fraction', zorder=4)
tx(loop_x+0.045, gy+gh/2, r'$\times 4$', fontsize=7, color='#D84315', fontweight='bold')

arr(ml, gy, ml, 0.68, c=DARK, lw=1.0)

# Depth gradient strip
bw, bgap = 0.05, 0.004
total_w = 5*bw + 4*bgap
sx0 = ml - total_w/2
strip_y, strip_h = 0.61, 0.06
for i in range(5):
    bx = sx0 + i*(bw+bgap)
    tc = WHITE if i >= 3 else DARK
    rbox(bx, strip_y, bw, strip_h, DEPTH[i], DEPTH_EC[i], 0.5)
    tx(bx+bw/2, strip_y+strip_h/2, f'gen-{i}', fontsize=6, color=tc, fontweight='medium')

tx(ml, strip_y-0.025, 'Generation depth $d$', fontsize=6, color='#666', fontstyle='italic')

# Annotation area
aw = 0.28
rbox(ml-aw/2, 0.06, aw, 0.44, WHITE, '#BCC2CC', 0.4)
tx(ml, 0.455, '8 base models, 5 families', fontsize=6.2, color='#444', fontweight='bold')
tx(ml, 0.41, '0.6B–8B parameters', fontsize=6, color='#555')
tx(ml, 0.34, '3 prompt types:', fontsize=6.2, color='#444', fontweight='bold')
tx(ml, 0.29, 'continuation', fontsize=6, color='#555')
tx(ml, 0.245, 'elaboration', fontsize=6, color='#555')
tx(ml, 0.20, 'rewriting', fontsize=6, color='#555')
tx(ml, 0.13, r'$\tau$=0.7, top-$p$=0.9', fontsize=5.5, color='#888')
tx(ml, 0.09, 'max 256 tokens', fontsize=5.5, color='#888')

# Cross-panel arrow
bigarr(S1-0.01, 0.65, S1+0.015, 0.65)

# ═══════════════════════════════════════
# SECTION 2: Feature Extraction
# ═══════════════════════════════════════
mm = (S1+S2)/2

# Pythia-410M
pw, ph = 0.17, 0.055
rbox(mm-pw/2, 0.86, pw, ph, '#D4E8D4', '#4A8C4A', 0.7)
tx(mm, 0.888, 'Pythia-410M', fontsize=7, fontweight='bold', color='#2D5A2D')

arr(mm, 0.855, mm, 0.825, c='#4A8C4A', lw=0.7)

# NLL distribution curve
nw, nh = 0.22, 0.09
nx = mm - nw/2
ny = 0.725
rbox(nx, ny, nw, nh, WHITE, '#BBB', 0.4)
tx(mm, ny+nh+0.012, 'Token NLL Distribution', fontsize=5.8, color='#666')

cxs = np.linspace(nx+0.012, nx+nw-0.012, 60)
t = np.linspace(-3, 3, 60)
cys = ny + 0.015 + 0.06 * np.exp(-t**2/2)
ax.plot(cxs, cys, color=BLUE, lw=0.9, transform=T, clip_on=False, zorder=4)
ax.fill_between(cxs, ny+0.015, cys, color=BLUE, alpha=0.12, transform=T, zorder=3)

arr(mm, ny, mm, 0.67, c='#666', lw=0.7)

# Feature groups
fl = S1 + 0.018
fr = S2 - 0.018
cg = 0.008
fw = (fr-fl-cg)/2
fh = 0.055

# Drifting (blue)
dy = 0.625
tx(fl+0.005, dy, r'Drifting  $|\rho|>0.4$', fontsize=6, color=BLUE,
   fontweight='bold', ha='left')
for j, f in enumerate(['entropy_mean','entropy_min','TTR','hapax_ratio']):
    r, c = j//2, j%2
    bx = fl + c*(fw+cg)
    by = dy - 0.05 - r*(fh+0.01)
    rbox(bx, by, fw, fh, BLUE_LT, BLUE, 0.5)
    tx(bx+fw/2, by+fh/2, f, fontsize=5.8, color=BLUE)

# Stationary (orange)
ssy = dy - 0.05 - 2*(fh+0.01) - 0.02
tx(fl+0.005, ssy, r'Stationary  $|\rho|<0.10$', fontsize=6, color=ORANGE,
   fontweight='bold', ha='left')
for j, f in enumerate(['entropy_max','tail_decay']):
    bx = fl + j*(fw+cg)
    by = ssy - 0.05
    rbox(bx, by, fw, fh, ORANGE_LT, ORANGE, 0.5)
    tx(bx+fw/2, by+fh/2, f, fontsize=5.8, color='#B8860B')

# Intermediate (gray)
iy = ssy - 0.05 - fh - 0.02
tx(fl+0.005, iy, 'Intermediate', fontsize=6, color=GRAY, fontweight='bold', ha='left')
by_i = iy - 0.05
rbox(fl, by_i, fw, fh, GRAY_LT, GRAY, 0.5)
tx(fl+fw/2, by_i+fh/2, 'entropy_std', fontsize=5.8, color='#555')

# Cross-panel arrow
bigarr(S2-0.01, 0.65, S2+0.015, 0.65)

# ═══════════════════════════════════════
# SECTION 3: Classification & DDR
# ═══════════════════════════════════════
mr = (S2+1)/2

# XGBoost
xw, xh = 0.20, 0.06
rbox(mr-xw/2, 0.855, xw, xh, '#E8D4E8', '#6A3D6A', 0.7)
tx(mr, 0.885, 'XGBoost (LOGO-CV)', fontsize=6.5, fontweight='bold', color='#4A2D4A')

arr(mr, 0.85, mr, 0.805, c='#555', lw=0.8)

# 3-class output boxes
cw_, ch_ = 0.06, 0.06
cg_ = 0.008
ct_ = 3*cw_ + 2*cg_
cx0 = mr - ct_/2
cy_ = 0.735
for k, (cls, col, tc) in enumerate([
    ('gen-0', DEPTH[0], DARK),
    ('gen-1', DEPTH[1], DARK),
    ('gen-2+', DEPTH[3], WHITE)]):
    cx = cx0 + k*(cw_+cg_)
    rbox(cx, cy_, cw_, ch_, col, '#666', 0.5)
    tx(cx+cw_/2, cy_+ch_/2, cls, fontsize=6, color=tc, fontweight='medium')

tx(mr, cy_-0.025, '3-class output', fontsize=5.5, color='#666')

# ── DDR subplot ──
ddx = S2 + 0.018
ddy = 0.05
ddw = 0.97 - ddx
ddh = 0.56

rbox(ddx, ddy, ddw, ddh, WHITE, '#BBB', 0.5)
tx(ddx+ddw/2, ddy+ddh-0.022, 'Differential Depth Response', fontsize=6.5, fontweight='bold')

pl = ddx + 0.055
pr = ddx + ddw - 0.02
pb = ddy + 0.10
pt = ddy + ddh - 0.09

# Axes
ax.plot([pl,pr], [pb,pb], color='#999', lw=0.4, transform=T, clip_on=False, zorder=2)
ax.plot([pl,pl], [pb,pt], color='#999', lw=0.4, transform=T, clip_on=False, zorder=2)

for i in range(5):
    xt = pl + i*(pr-pl)/4
    ax.plot([xt,xt], [pb-0.012,pb], color='#999', lw=0.3, transform=T, clip_on=False, zorder=2)
    tx(xt, pb-0.032, str(i), fontsize=6, color='#666')

tx((pl+pr)/2, pb-0.062, 'depth', fontsize=6, color='#555')
tx(pl-0.032, (pb+pt)/2, 'value', fontsize=5.5, color='#555', rotation=90)

# Data
xs = np.array([pl + i*(pr-pl)/4 for i in range(5)])

yd = pb + np.array([0.92, 0.72, 0.50, 0.40, 0.34])*(pt-pb)
ax.plot(xs, yd, color=BLUE, lw=1.3, marker='o', ms=3, zorder=4, transform=T, clip_on=False)

ys2 = pb + np.array([0.50, 0.52, 0.49, 0.51, 0.50])*(pt-pb)
ax.plot(xs, ys2, color=ORANGE, lw=1.3, marker='s', ms=3, zorder=4, transform=T, clip_on=False)

yi2 = pb + np.array([0.72, 0.62, 0.55, 0.50, 0.47])*(pt-pb)
ax.plot(xs, yi2, color=GRAY, lw=1.0, marker='^', ms=2.5, ls='--', zorder=4, transform=T, clip_on=False)

# Labels (spread vertically)
lbl = pr + 0.008
tx(lbl, yd[-1]+0.015, 'Drifting', fontsize=5.5, color=BLUE, ha='left')

# Stationary: offset up
stat_lbl_y = ys2[-1] + 0.03
ax.plot([pr+0.001, lbl-0.002], [ys2[-1], stat_lbl_y], color=ORANGE, lw=0.4, ls=':',
    transform=T, clip_on=False, zorder=3)
tx(lbl, stat_lbl_y, 'Stationary', fontsize=5.5, color=ORANGE, ha='left')

# Intermediate: offset down
intm_lbl_y = yi2[-1] - 0.03
ax.plot([pr+0.001, lbl-0.002], [yi2[-1], intm_lbl_y], color=GRAY, lw=0.4, ls=':',
    transform=T, clip_on=False, zorder=3)
tx(lbl, intm_lbl_y, 'Interm.', fontsize=5.5, color=GRAY, ha='left')

# ── Save ──
out = '/root/gen-depth-fingerprint/paper/figures'
fig.savefig(f'{out}/fig2_framework.pdf', format='pdf')
fig.savefig(f'{out}/fig2_framework.png', format='png')
print(f"Saved: {out}/fig2_framework.pdf + .png")
