"""Method framework v3: Three-panel icon-heavy visual storytelling concept figure.
(a) The Problem — training vs inference attention gap
(b) Diagnosis — systematic elimination → exposure bias
(c) The Fix — scheduled sampling bridges the gap
"""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

apply_style()
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'DejaVu Sans', 'Arial'],
    'font.size': 9,
})

BLUE = '#6BAED6'; ORANGE = '#FDAE6B'; GREEN = '#8DC98D'; ROSE = '#E6A8A1'
GRAY = '#BDBDBD'; LGRAY = '#E8E8E8'; DARK = '#333333'; MUTED = '#999999'
BLUE_D = '#4A90B8'; ORANGE_D = '#D4874A'; GREEN_D = '#5DAA5D'; ROSE_D = '#C07070'
PANEL_BG = '#FAFAFA'; PANEL_BORDER = '#E0E0E0'

fig = plt.figure(figsize=(14, 5.5), facecolor='white')
ax_a = fig.add_axes([0.01, 0.02, 0.315, 0.94])
ax_b = fig.add_axes([0.34, 0.02, 0.305, 0.94])
ax_c = fig.add_axes([0.66, 0.02, 0.33, 0.94])

for ax in [ax_a, ax_b, ax_c]:
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
    ax.add_patch(FancyBboxPatch((0.15, 0.1), 9.7, 9.65,
                 boxstyle="round,pad=0,rounding_size=0.2",
                 fc=PANEL_BG, ec=PANEL_BORDER, lw=0.8, zorder=0))


def rbox(ax, x, y, w, h, fill='white', edge=PANEL_BORDER, lw=0.7, r=0.15, alpha=1.0, zorder=2):
    b = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                        fc=fill, ec=edge, lw=lw, alpha=alpha, zorder=zorder)
    ax.add_patch(b); return b


def bubble(ax, x, y, w, h, fill, edge=None, right=False, zorder=3):
    if edge is None: edge = fill
    bx = x - w if right else x
    ax.add_patch(FancyBboxPatch((bx, y), w, h, boxstyle="round,pad=0,rounding_size=0.1",
                 fc=fill, ec=edge, lw=0.5, zorder=zorder))
    # Two thin "text" lines inside
    lx = bx + 0.15
    for dy in [h*0.6, h*0.3]:
        line_w = w * 0.6 if dy == h*0.6 else w * 0.4
        ax.plot([lx, lx + line_w], [y + dy, y + dy], color=edge if edge != fill else '#CCCCCC',
                lw=0.3, alpha=0.4, zorder=zorder+1)


def checkmark(ax, cx, cy, s=0.4, color=GREEN_D, lw=2.5, zorder=10):
    ax.plot([cx-s*0.5, cx-s*0.05, cx+s*0.55], [cy, cy-s*0.4, cy+s*0.45],
            color=color, lw=lw, solid_capstyle='round', solid_joinstyle='round', zorder=zorder)


def cross(ax, cx, cy, s=0.35, color=ROSE_D, lw=2.5, zorder=10):
    ax.plot([cx-s, cx+s], [cy-s, cy+s], color=color, lw=lw, solid_capstyle='round', zorder=zorder)
    ax.plot([cx-s, cx+s], [cy+s, cy-s], color=color, lw=lw, solid_capstyle='round', zorder=zorder)


# ═══════════════ PANEL (a): The Problem ═══════════════
ax_a.text(0.5, 9.55, '(a)', fontsize=11, fontweight='bold', color=DARK, va='top')
ax_a.text(1.3, 9.55, 'The Problem', fontsize=10.5, fontweight='bold', color=DARK, va='top')

# -- Training scene --
rbox(ax_a, 0.4, 5.55, 9.0, 4.0, fill='#F4FAF4', edge='#B8D8B8', lw=0.7, r=0.18, alpha=0.8)
ax_a.text(0.7, 9.3, 'Training', fontsize=8.5, color=GREEN_D, fontweight='bold', va='top')

# User bubbles (blue fill), model bubbles (gray), more opaque
user_fill = BLUE + '40'
model_fill = '#E8E8E8'
specs = [
    (1.0, 8.6, 3.6, 0.35, user_fill, False),
    (8.8, 8.05, 3.0, 0.35, model_fill, True),
    (1.0, 7.5, 2.8, 0.35, user_fill, False),
    (8.8, 6.95, 3.4, 0.35, model_fill, True),
    (1.0, 6.4, 3.2, 0.35, user_fill, False),
]
for bx, by, bw, bh, bf, is_r in specs:
    bubble(ax_a, bx, by, bw, bh, fill=bf, right=is_r)

# Target (warm glow)
bubble(ax_a, 8.8, 5.78, 3.6, 0.42, fill=ORANGE + '55', edge=ORANGE_D, right=True, zorder=4)

# Attention arrows (thick dashed, clearly visible)
for sy, rad in [(8.75, -0.22), (7.65, -0.15), (6.55, -0.08)]:
    ax_a.annotate('', xy=(5.9, 5.95), xytext=(3.2, sy),
                  arrowprops=dict(arrowstyle='->', color=BLUE_D, lw=1.5,
                                  linestyle=(0, (4, 2)), alpha=0.7,
                                  connectionstyle=f'arc3,rad={rad}'), zorder=5)

checkmark(ax_a, 8.8, 9.0, s=0.5, color=GREEN_D, lw=3.5)

# -- Cracked arrow --
ax_a.annotate('', xy=(4.5, 4.55), xytext=(4.5, 5.45),
              arrowprops=dict(arrowstyle='->', color='#AAAAAA', lw=3.0, mutation_scale=18), zorder=5)
bolt = [(0, 0.22), (0.13, 0.06), (-0.07, -0.03), (0.09, -0.22)]
bx0, by0 = 5.1, 5.0
ax_a.plot([bx0+p[0] for p in bolt], [by0+p[1] for p in bolt],
          color=ROSE_D, lw=2.2, solid_capstyle='round', zorder=7)
ax_a.text(5.7, 5.0, '8–17×', fontsize=10.5, color=ROSE_D, fontweight='bold',
          fontstyle='italic', ha='left', va='center')

# -- Inference scene --
rbox(ax_a, 0.4, 0.35, 9.0, 3.95, fill='#FAF4F4', edge='#D8B8B8', lw=0.7, r=0.18, alpha=0.8)
ax_a.text(0.7, 4.05, 'Inference', fontsize=8.5, color=ROSE_D, fontweight='bold', va='top')

inf_fill = '#E0E0E0'
specs_inf = [
    (1.0, 3.5, 3.6, 0.33, inf_fill, False),
    (8.8, 2.95, 3.0, 0.33, inf_fill, True),
    (1.0, 2.4, 2.8, 0.33, inf_fill, False),
    (8.8, 1.85, 3.4, 0.33, inf_fill, True),
    (1.0, 1.3, 3.2, 0.33, inf_fill, False),
]
for bx, by, bw, bh, bf, is_r in specs_inf:
    bubble(ax_a, bx, by, bw, bh, fill=bf, right=is_r)

# Dimmed target with ?
bubble(ax_a, 8.8, 0.55, 3.6, 0.42, fill='#D5D5D5', edge='#AAAAAA', right=True, zorder=4)
ax_a.text(6.1, 0.76, '?', fontsize=16, color='#888888', ha='center', va='center',
          fontweight='bold', zorder=6)

# Broken attention: more visible disconnected dashes
for sy in [3.65, 2.55, 1.45]:
    end_y = 0.85
    sx_a, ex_a = 3.2, 5.9
    t_vals = [0.0, 0.25, 0.35, 0.55, 0.65]
    for j in range(0, len(t_vals)-1, 2):
        t1, t2 = t_vals[j], t_vals[j+1]
        x1 = sx_a + (ex_a - sx_a) * t1
        y1 = sy + (end_y - sy) * t1
        x2 = sx_a + (ex_a - sx_a) * t2
        y2 = sy + (end_y - sy) * t2
        alpha = 0.5 - j * 0.12
        ax_a.plot([x1, x2], [y1, y2], color='#AAAAAA', lw=1.0,
                  ls=(0, (3, 3)), alpha=alpha, zorder=4)

cross(ax_a, 8.8, 3.8, s=0.4, color=ROSE_D, lw=3.5)


# ═══════════════ PANEL (b): Diagnosis ═══════════════
ax_b.text(0.5, 9.55, '(b)', fontsize=11, fontweight='bold', color=DARK, va='top')
ax_b.text(1.3, 9.55, 'Diagnosis', fontsize=10.5, fontweight='bold', color=DARK, va='top')

# Magnifying glass
mgx, mgy, mgs = 5.0, 8.55, 0.5
ax_b.add_patch(plt.Circle((mgx, mgy), mgs, fc='white', ec=BLUE_D, lw=2.2, zorder=10))
hx = mgx + mgs*0.65; hy = mgy - mgs*0.65
ax_b.plot([hx, hx+mgs*0.55], [hy, hy-mgs*0.55], color=BLUE_D, lw=2.8,
          solid_capstyle='round', zorder=10)

ax_b.annotate('', xy=(5.0, 7.55), xytext=(5.0, 7.9),
              arrowprops=dict(arrowstyle='->', color='#CCCCCC', lw=0.9), zorder=3)

# Three hypothesis boxes
hyps = [(6.85, 'Turn conditioning'), (5.4, 'Gating mechanism'), (3.95, 'Gradient conflict')]
bw_b, bh_b = 7.2, 1.1
bx_b = 1.4

for i, (y, label) in enumerate(hyps):
    rbox(ax_b, bx_b, y, bw_b, bh_b, fill='#F8F8F8', edge='#DDDDDD', lw=0.6, r=0.12)
    icx = bx_b + 1.1
    icy = y + bh_b/2

    if i == 0:  # Dial
        ax_b.add_patch(plt.Circle((icx, icy), 0.35, fc='white', ec=BLUE, lw=1.3, zorder=5))
        ax_b.plot([icx, icx+0.18], [icy, icy+0.25], color=BLUE_D, lw=2.0,
                  solid_capstyle='round', zorder=6)
        for a in [40, 80, 120]:
            r = np.radians(a)
            ax_b.plot([icx+0.27*np.cos(r), icx+0.35*np.cos(r)],
                      [icy+0.27*np.sin(r), icy+0.35*np.sin(r)], color=BLUE, lw=0.9, zorder=6)
    elif i == 1:  # Gate
        gx, gy = icx-0.3, icy-0.25
        for dx in [0, 0.6]:
            ax_b.plot([gx+dx, gx+dx], [gy, gy+0.5], color=BLUE, lw=1.6, zorder=5)
        ax_b.plot([gx, gx+0.6], [gy+0.25, gy+0.25], color=BLUE, lw=1.3, zorder=5)
        ax_b.plot([gx+0.08, gx+0.52], [gy+0.4, gy+0.4], color=ROSE, lw=2.3, zorder=6)
    else:  # Crossing arrows
        d = 0.24
        for x1, y1, x2, y2 in [(icx-d, icy-d, icx+d, icy+d), (icx+d, icy-d, icx-d, icy+d)]:
            ax_b.annotate('', xy=(x2, y2), xytext=(x1, y1),
                          arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.4), zorder=5)

    ax_b.text(bx_b + bw_b/2 + 0.4, y + bh_b/2, label, fontsize=8.5, color='#666666',
              ha='center', va='center', zorder=5)
    cross(ax_b, bx_b + bw_b - 0.55, y + bh_b/2, s=0.3, color=ROSE_D, lw=2.5)

    if i < 2:
        ax_b.annotate('', xy=(5.0, hyps[i+1][0] + bh_b + 0.03),
                      xytext=(5.0, y - 0.03),
                      arrowprops=dict(arrowstyle='->', color='#CCCCCC', lw=0.9), zorder=3)

ax_b.annotate('', xy=(5.0, 3.45), xytext=(5.0, hyps[-1][0] - 0.03),
              arrowprops=dict(arrowstyle='->', color='#CCCCCC', lw=0.9), zorder=3)

# Lightbulb
lbx, lby, lbs = 5.0, 2.9, 0.42
ax_b.add_patch(plt.Circle((lbx, lby+lbs*0.15), lbs*0.9, fc=ORANGE+'CC', ec=ORANGE_D,
                            lw=1.5, zorder=10))
ax_b.plot([lbx-lbs*0.3, lbx+lbs*0.3], [lby-lbs*0.65, lby-lbs*0.65],
          color=ORANGE_D, lw=1.3, zorder=11)
ax_b.plot([lbx-lbs*0.22, lbx+lbs*0.22], [lby-lbs*0.82, lby-lbs*0.82],
          color=ORANGE_D, lw=1.0, zorder=11)
for angle in [20, 55, 90, 125, 160]:
    rad = np.radians(angle)
    r_in = lbs + 0.12; r_out = lbs + 0.3
    ax_b.plot([lbx + r_in*np.cos(rad), lbx + r_out*np.cos(rad)],
              [lby+lbs*0.15 + r_in*np.sin(rad), lby+lbs*0.15 + r_out*np.sin(rad)],
              color=ORANGE_D, lw=1.0, alpha=0.5, zorder=10)

# Teacher / Student
fy = 1.2
# Teacher
tx = 3.0
ax_b.add_patch(plt.Circle((tx, fy+0.8), 0.28, fc=BLUE+'35', ec=BLUE_D, lw=1.3, zorder=5))
ax_b.plot([tx, tx], [fy+0.52, fy+0.05], color=BLUE_D, lw=1.8, zorder=5)
ax_b.plot([tx-0.32, tx, tx+0.2], [fy+0.35, fy+0.42, fy+0.58],
          color=BLUE_D, lw=1.4, solid_capstyle='round', zorder=5)
ax_b.add_patch(FancyBboxPatch((tx+0.15, fy+0.52), 0.42, 0.32,
               boxstyle="round,pad=0,rounding_size=0.04",
               fc=GREEN+'50', ec=GREEN_D, lw=0.8, zorder=6))
checkmark(ax_b, tx+0.36, fy+0.63, s=0.09, color=GREEN_D, lw=1.5, zorder=7)
ax_b.plot([tx-0.22, tx, tx+0.22], [fy-0.38, fy+0.05, fy-0.38],
          color=BLUE_D, lw=1.4, solid_capstyle='round', zorder=5)
ax_b.text(tx, fy-0.6, 'Teacher', fontsize=7.5, color=BLUE_D, ha='center', fontweight='bold')

# Student
sx_p = 7.0
ax_b.add_patch(plt.Circle((sx_p, fy+0.8), 0.28, fc=ORANGE+'35', ec=ORANGE_D, lw=1.3, zorder=5))
ax_b.plot([sx_p, sx_p], [fy+0.52, fy+0.05], color=ORANGE_D, lw=1.8, zorder=5)
ax_b.plot([sx_p-0.32, sx_p, sx_p+0.32], [fy+0.48, fy+0.42, fy+0.48],
          color=ORANGE_D, lw=1.4, solid_capstyle='round', zorder=5)
ax_b.plot([sx_p-0.22, sx_p, sx_p+0.22], [fy-0.38, fy+0.05, fy-0.38],
          color=ORANGE_D, lw=1.4, solid_capstyle='round', zorder=5)
ax_b.text(sx_p+0.05, fy+1.22, '?', fontsize=14, color=ORANGE_D, ha='center',
          fontweight='bold', zorder=6)
ax_b.text(sx_p, fy-0.6, 'Student', fontsize=7.5, color=ORANGE_D, ha='center', fontweight='bold')

ax_b.text(5.0, 0.32, 'Exposure Bias', fontsize=11, fontweight='bold', color=DARK, ha='center')


# ═══════════════ PANEL (c): The Fix ═══════════════
ax_c.text(0.5, 9.55, '(c)', fontsize=11, fontweight='bold', color=DARK, va='top')
ax_c.text(1.3, 9.55, 'The Fix', fontsize=10.5, fontweight='bold', color=DARK, va='top')

# -- Token gradient (scheduled sampling) --
rbox(ax_c, 0.4, 5.3, 9.2, 4.15, fill='white', edge='#E5E5E5', lw=0.5, r=0.15, alpha=0.6)

col_x = [1.4, 3.0, 5.0, 7.0, 8.6]
tokens = [
    [BLUE]*5,
    [BLUE, BLUE, BLUE, BLUE, ORANGE],
    [BLUE, BLUE, ORANGE, ORANGE, ORANGE],
    [BLUE, ORANGE, ORANGE, ORANGE, ORANGE],
    [ORANGE]*5,
]
cr = 0.23
for ci, (cx, cols) in enumerate(zip(col_x, tokens)):
    for ri, c in enumerate(cols):
        cy = 8.9 - ri * 0.55
        ax_c.add_patch(plt.Circle((cx, cy), cr, fc=c, ec='white', lw=1.3, alpha=0.85, zorder=5))

# Gradient bar
gy = 5.82
n = 120
for i in range(n):
    f = i / n
    rc = (1-f)*0.42+f*0.99; gc_ = (1-f)*0.68+f*0.68; bc = (1-f)*0.84+f*0.42
    xs = 1.0 + 7.2 * i / n
    xe = 1.0 + 7.2 * (i+1) / n
    ax_c.add_patch(plt.Rectangle((xs, gy-0.13), xe-xs, 0.26, fc=(rc, gc_, bc),
                                  ec='none', alpha=0.65, zorder=4))
ax_c.add_patch(plt.Circle((1.0, gy), 0.13, fc=BLUE, ec='none', alpha=0.65, zorder=4))
ax_c.annotate('', xy=(8.8, gy), xytext=(8.2, gy),
              arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.8, mutation_scale=14), zorder=5)

ax_c.text(5.0, 5.45, 'Training Progress', fontsize=7.5, color=MUTED, ha='center', fontstyle='italic')
ax_c.text(1.4, 6.12, 'teacher', fontsize=7, color=BLUE_D, ha='center')
ax_c.text(8.6, 6.12, 'student', fontsize=7, color=ORANGE_D, ha='center')

# -- Before/After bridge --
by_ = 0.4; bh_ = 4.5
bef_w = 4.0; aft_w = 4.0
bef_x = 0.4; aft_x = 5.6

rbox(ax_c, bef_x, by_, bef_w, bh_, fill=ROSE+'15', edge=ROSE, lw=1.0, r=0.15)
rbox(ax_c, aft_x, by_, aft_w, bh_, fill=GREEN+'15', edge=GREEN, lw=1.0, r=0.15)

# Green arrow
mid = by_ + bh_/2
ax_c.annotate('', xy=(5.35, mid), xytext=(4.65, mid),
              arrowprops=dict(arrowstyle='->', color=GREEN_D, lw=2.5, mutation_scale=16), zorder=8)

# Cliff parameters
cb = by_ + 1.0; ch = 2.5; cw = 1.1

# BEFORE cliffs
lx = bef_x + 0.45
gap_w = 1.0
rx = lx + cw + gap_w

for cx_cliff in [lx, rx]:
    xs = [cx_cliff+0.1, cx_cliff-0.08, cx_cliff+cw+0.08, cx_cliff+cw-0.1]
    ys = [cb+ch, cb, cb, cb+ch]
    ax_c.fill(xs, ys, color='#9EAAB8', alpha=0.55, zorder=3)
    ax_c.plot(xs + [xs[0]], ys + [ys[0]], color='#7A8A98', lw=0.5, alpha=0.4, zorder=3)

ax_c.text(lx+cw/2, cb+ch+0.2, 'Train', fontsize=8, color=DARK, ha='center', fontweight='bold')
ax_c.text(rx+cw/2, cb+ch+0.2, 'Infer', fontsize=8, color=DARK, ha='center', fontweight='bold')

# Broken bridge: prominent dashed arc sagging into gap
bridge_top = cb + ch * 0.82
mid_bridge = lx + cw + gap_w/2
# Left side of broken bridge — sags down
ax_c.plot([lx+cw-0.05, mid_bridge-0.15], [bridge_top, bridge_top-0.4],
          color=ROSE_D, lw=2.5, ls=(0, (4, 3)), zorder=5)
# Right side — sags down
ax_c.plot([mid_bridge+0.2, rx+0.05], [bridge_top-0.45, bridge_top],
          color=ROSE_D, lw=2.5, ls=(0, (4, 3)), zorder=5)
# Falling debris dots
for dx, dy in [(-0.05, -0.55), (0.1, -0.7), (0.0, -0.9)]:
    ax_c.plot(mid_bridge+dx, bridge_top+dy, 'o', color=ROSE_D, ms=1.5, alpha=0.4, zorder=5)

# Subtle dark shading in the gap
ax_c.fill([lx+cw-0.05, lx+cw-0.05, rx+0.05, rx+0.05],
          [cb, cb+ch*0.7, cb+ch*0.7, cb],
          color='#333333', alpha=0.08, zorder=2)
# "gap" text in the chasm
ax_c.text(mid_bridge, cb+0.35, 'gap', fontsize=9, color=ROSE_D, ha='center',
          fontstyle='italic', fontweight='bold')

ax_c.text(bef_x + bef_w/2, by_+0.12, 'Before', fontsize=8.5, color=ROSE_D,
          ha='center', fontweight='bold')

# AFTER cliffs (narrower but visible gap, solid bridge)
lx2 = aft_x + 0.7
gap2 = 0.35
rx2 = lx2 + cw + gap2

for cx_cliff in [lx2, rx2]:
    xs = [cx_cliff+0.1, cx_cliff-0.08, cx_cliff+cw+0.08, cx_cliff+cw-0.1]
    ys = [cb+ch, cb, cb, cb+ch]
    ax_c.fill(xs, ys, color='#9EAAB8', alpha=0.55, zorder=3)
    ax_c.plot(xs + [xs[0]], ys + [ys[0]], color='#7A8A98', lw=0.5, alpha=0.4, zorder=3)

ax_c.text(lx2+cw/2, cb+ch+0.2, 'Train', fontsize=8, color=DARK, ha='center', fontweight='bold')
ax_c.text(rx2+cw/2, cb+ch+0.2, 'Infer', fontsize=8, color=DARK, ha='center', fontweight='bold')

# Solid bridge with slight planks visual
ax_c.plot([lx2+cw-0.08, rx2+0.08], [bridge_top, bridge_top],
          color=GREEN_D, lw=4.0, solid_capstyle='round', zorder=5)
# Subtle bridge planks
for px in np.linspace(lx2+cw, rx2, 3):
    ax_c.plot([px, px], [bridge_top-0.06, bridge_top+0.06],
              color='white', lw=0.5, alpha=0.6, zorder=6)

checkmark(ax_c, aft_x + aft_w - 0.6, by_ + bh_ - 0.55, s=0.35, color=GREEN_D, lw=3.0)
ax_c.text(aft_x + aft_w/2, by_+0.12, 'After', fontsize=8.5, color=GREEN_D,
          ha='center', fontweight='bold')


save_fig(fig, 'fig_method_framework_v3')
