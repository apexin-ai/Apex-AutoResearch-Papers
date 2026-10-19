import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import matplotlib.path as mpath
from matplotlib.patches import PathPatch, FancyArrowPatch, FancyBboxPatch, Arc
import numpy as np

# ── Colors ──
CORAL = '#E8846B'
CORAL_DARK = '#C0603E'
BLUE = '#0072B2'
BLUE_DARK = '#005A8D'
RED_TEXT = '#C0392B'
GRAY_TEXT = '#888888'
GRAY_ARM = '#C8C8C8'
GREEN_GOAL = '#009E73'

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 10.5,
    'axes.titleweight': 'bold',
    'axes.labelsize': 9.5,
    'xtick.labelsize': 8.5,
    'ytick.labelsize': 8.5,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.grid': False,
    'axes.linewidth': 0.6,
})

stroke = [pe.withStroke(linewidth=2.5, foreground='white')]
stroke_s = [pe.withStroke(linewidth=1.8, foreground='white')]

# ── Layout ──
fig = plt.figure(figsize=(5.5, 2.8))
gs = fig.add_gridspec(2, 3, width_ratios=[1, 1.2, 1], height_ratios=[7, 2],
                      wspace=0.30, hspace=0.45,
                      left=0.03, right=0.98, top=0.84, bottom=0.05)

ax_a = fig.add_subplot(gs[0, 0])
ax_a_bar = fig.add_subplot(gs[1, 0])
ax_b = fig.add_subplot(gs[:, 1])
ax_c = fig.add_subplot(gs[0, 2])
ax_c_bar = fig.add_subplot(gs[1, 2])


# ═══════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════

def draw_arm(ax, base, elbow, ee, color, ls='-', alpha=1.0, lw=4.5):
    for p1, p2 in [(base, elbow), (elbow, ee)]:
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, linestyle=ls,
                linewidth=lw, alpha=alpha, solid_capstyle='round',
                dash_capstyle='round', zorder=3)
    kw = dict(zorder=4, edgecolors='white', linewidths=0.8)
    ax.scatter(*base, s=70, color=color, alpha=min(alpha + 0.15, 1), **kw)
    ax.scatter(*elbow, s=50, color=color, alpha=alpha, **kw)
    ax.scatter(*ee, s=35, color=color, alpha=alpha, **kw)
    mw, mh = 1.4, 0.3
    mount = mpatches.Rectangle((base[0] - mw / 2, base[1] - mh), mw, mh,
                                facecolor=color, alpha=alpha * 0.35,
                                edgecolor=color, linewidth=0.5, zorder=2)
    ax.add_patch(mount)
    for i in range(4):
        x0 = base[0] - mw / 2 + i * mw / 4
        ax.plot([x0, x0 + mw / 5], [base[1] - mh, base[1] - mh - 0.25],
                color=color, lw=0.5, alpha=alpha * 0.4, zorder=2)


def draw_obstacle(ax, center, w=1.3, h=1.3):
    rect = FancyBboxPatch((center[0] - w / 2, center[1] - h / 2), w, h,
                           boxstyle='round,pad=0.08', facecolor=CORAL,
                           alpha=0.35, edgecolor=CORAL_DARK, linewidth=1.0, zorder=2)
    ax.add_patch(rect)


def setup_schematic(ax, title):
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.5, 9)
    ax.axis('off')
    ax.set_title(title, pad=4, fontsize=10.5, fontweight='bold')


# ═══════════════════════════════════════════
# Panel (a): Action-Collapsed Safety
# ═══════════════════════════════════════════
setup_schematic(ax_a, '(a) Action-Collapsed Safety')

base_a, elbow_a, ee_a = (3, 0.8), (3.2, 3.8), (3.4, 6.3)
draw_arm(ax_a, base_a, elbow_a, ee_a, '#D0D0D0', ls='-', alpha=0.45, lw=5.5)
# Coral dashed outline (links Pi0+A1 color)
for _p1, _p2 in [(base_a, elbow_a), (elbow_a, ee_a)]:
    ax_a.plot([_p1[0], _p2[0]], [_p1[1], _p2[1]], color=CORAL, linestyle='--',
              linewidth=1.0, alpha=0.35, solid_capstyle='round',
              dash_capstyle='round', zorder=3.5)
draw_obstacle(ax_a, (7, 4.0), w=1.4, h=1.4)

ax_a.text(3.3, 7.8, 'action-\ncollapsed', fontsize=6.5, color=CORAL_DARK, ha='center',
          fontstyle='italic', fontweight='semibold',
          bbox=dict(boxstyle='round,pad=0.2', facecolor='#F8E8E3',
                    edgecolor=CORAL, lw=0.7, ls='--'))

rng = np.random.RandomState(42)
ax_a.scatter(ee_a[0] + rng.normal(0, 0.07, 20),
             ee_a[1] + rng.normal(0, 0.07, 20),
             s=2.5, color=CORAL, alpha=0.5, zorder=5)

ax_a.text(7.2, 7.5, 'CAR = 91.5%', fontsize=6.5, color=CORAL_DARK,
          fontweight='bold', ha='center', path_effects=stroke_s)
ax_a.text(7.2, 6.3, 'TSR = 0%', fontsize=6, color=RED_TEXT,
          fontweight='bold', ha='center', path_effects=stroke_s)

# Displacement bar A
ax_a_bar.barh(0, 300, height=0.5, color='#F0F0F0', edgecolor='#DDDDDD',
              linewidth=0.5, zorder=1)
ax_a_bar.barh(0, 0.1, height=0.5, color=CORAL, edgecolor=CORAL_DARK,
              linewidth=0.4, zorder=3)
ax_a_bar.text(15, 0, '< 0.1 mm', fontsize=6, va='center', ha='left',
              color=CORAL_DARK, fontweight='semibold')
ax_a_bar.text(150, -0.5, 'Displacement', fontsize=5, va='top', ha='center',
              color=GRAY_TEXT)
ax_a_bar.set_xlim(0, 300)
ax_a_bar.set_ylim(-0.7, 0.7)
ax_a_bar.axis('off')


# ═══════════════════════════════════════════
# Panel (b): CAR_f Filtering — Flow Diagram
# ═══════════════════════════════════════════
ax_b.set_xlim(0, 10)
ax_b.set_ylim(0, 10)
ax_b.axis('off')
ax_b.set_title(r'(b) CAR$_f$ Filtering', pad=4, fontsize=10.5, fontweight='bold')

cx_l, cx_r = 2.5, 7.5
bw, bh = 2.8, 0.9
ty = 8.5
by_ = 2.5

# Column headers
ax_b.text(cx_l, ty + bh / 2 + 0.25, 'Pi0+A1', fontsize=6.5, color=CORAL_DARK,
          ha='center', va='bottom', fontweight='semibold')
ax_b.text(cx_r, ty + bh / 2 + 0.25, 'Pi0.5', fontsize=6.5, color=BLUE,
          ha='center', va='bottom', fontweight='semibold')

# Top boxes (just percentages)
for cx, val, col, dark in [(cx_l, '91.5%', CORAL, CORAL_DARK),
                            (cx_r, '26.8%', BLUE, BLUE)]:
    box = FancyBboxPatch((cx - bw / 2, ty - bh / 2), bw, bh,
                          boxstyle='round,pad=0.1', facecolor=col, alpha=0.12,
                          edgecolor=col, linewidth=1.0, zorder=2)
    ax_b.add_patch(box)
    ax_b.text(cx, ty, val, fontsize=10, color=dark,
              ha='center', va='center', fontweight='bold')

# τ_d threshold line
td_y = 5.5
ax_b.plot([0.5, 9.5], [td_y, td_y], color='#AAAAAA', linestyle='--',
          linewidth=0.8, zorder=1)
ax_b.text(5, td_y + 0.2, r'$\tau_d$ = 0.1 mm', fontsize=6, color='#666666',
          ha='center', va='bottom')

# Arrow: Pi0+A1 (blocked, dashed)
arr_l = FancyArrowPatch((cx_l, ty - bh / 2 - 0.15), (cx_l, by_ + bh / 2 + 0.15),
                         arrowstyle='->', mutation_scale=10, color=CORAL,
                         linewidth=1.2, alpha=0.35, linestyle='--', zorder=3)
ax_b.add_patch(arr_l)

# X mark at threshold
ax_b.plot([cx_l - 0.35, cx_l + 0.35], [td_y - 0.3, td_y + 0.3],
          color=RED_TEXT, linewidth=1.8, zorder=5)
ax_b.plot([cx_l - 0.35, cx_l + 0.35], [td_y + 0.3, td_y - 0.3],
          color=RED_TEXT, linewidth=1.8, zorder=5)
ax_b.text(cx_l - 0.6, td_y - 0.5, '99.6%\nfiltered', fontsize=5, color=GRAY_TEXT,
          ha='right', va='top', fontstyle='italic', linespacing=1.1)

# Arrow: Pi0.5 (passes, solid)
arr_r = FancyArrowPatch((cx_r, ty - bh / 2 - 0.15), (cx_r, by_ + bh / 2 + 0.15),
                         arrowstyle='->', mutation_scale=10, color=BLUE,
                         linewidth=1.2, zorder=3)
ax_b.add_patch(arr_r)
ax_b.text(cx_r + 0.5, td_y - 0.6, 'unchanged', fontsize=5, color=BLUE,
          ha='left', va='top', fontstyle='italic')

# Bottom boxes
box_lb = FancyBboxPatch((cx_l - bw / 2, by_ - bh / 2), bw, bh,
                         boxstyle='round,pad=0.1', facecolor=RED_TEXT, alpha=0.08,
                         edgecolor=RED_TEXT, linewidth=1.0, linestyle='--', zorder=2)
ax_b.add_patch(box_lb)
ax_b.text(cx_l, by_, r'$\approx$ 0%', fontsize=10, color=RED_TEXT,
          ha='center', va='center', fontweight='bold')

box_rb = FancyBboxPatch((cx_r - bw / 2, by_ - bh / 2), bw, bh,
                         boxstyle='round,pad=0.1', facecolor=BLUE, alpha=0.08,
                         edgecolor=BLUE, linewidth=1.0, zorder=2)
ax_b.add_patch(box_rb)
ax_b.text(cx_r, by_, '26.8%', fontsize=10, color=BLUE,
          ha='center', va='center', fontweight='bold')

# Focal text (centered)
ax_b.text(5, 0.8, r'91.5%  $\rightarrow$  $\approx$0%', fontsize=9.5, color=RED_TEXT,
          ha='center', va='center', fontweight='bold', path_effects=stroke,
          bbox=dict(boxstyle='round,pad=0.3', facecolor='#FDECEC',
                    edgecolor='none', alpha=0.5))


# ═══════════════════════════════════════════
# Panel (c): Genuine Safety — Active Arm
# ═══════════════════════════════════════════
setup_schematic(ax_c, '(c) Genuine Safety')

base_c, elbow_c, ee_c = (2, 0.8), (4.2, 4.2), (6.5, 6.5)
draw_arm(ax_c, base_c, elbow_c, ee_c, BLUE, ls='-', alpha=1.0, lw=4)
draw_obstacle(ax_c, (6.5, 3.2), w=1.4, h=1.4)

# Motion arcs at joints
for center, diam, t1, t2 in [(base_c, 1.2, 55, 85), (elbow_c, 0.9, 30, 65)]:
    arc = Arc(center, diam, diam, angle=0, theta1=t1, theta2=t2,
              color=BLUE, linewidth=0.7, alpha=0.35, zorder=3, linestyle='--')
    ax_c.add_patch(arc)

# Trajectory (bezier from initial ee around obstacle → goal)
ts, te = (3.4, 6.5), (8.5, 1.5)
c1, c2 = (6.5, 8.8), (9.5, 5.0)
path = mpath.Path([ts, c1, c2, te],
                   [mpath.Path.MOVETO, mpath.Path.CURVE4,
                    mpath.Path.CURVE4, mpath.Path.CURVE4])
ax_c.add_patch(PathPatch(path, facecolor='none', edgecolor=BLUE,
                          linewidth=1.5, alpha=0.5, zorder=2))

# Direction arrows along trajectory
p0, p1, p2, p3 = map(np.array, [ts, c1, c2, te])
for t in [0.3, 0.55, 0.8]:
    pt = (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3
    tg = 3 * (1 - t)**2 * (p1 - p0) + 6 * (1 - t) * t * (p2 - p1) + 3 * t**2 * (p3 - p2)
    tg /= np.linalg.norm(tg)
    s = 0.25
    tip = pt + s * tg
    L = pt - s * 0.3 * tg + s * 0.25 * np.array([-tg[1], tg[0]])
    R = pt - s * 0.3 * tg - s * 0.25 * np.array([-tg[1], tg[0]])
    ax_c.add_patch(plt.Polygon([tip, L, R], closed=True, facecolor=BLUE_DARK,
                                edgecolor='none', alpha=0.65, zorder=5))

# Goal
ax_c.scatter(*te, s=90, marker='*', color=GREEN_GOAL, zorder=5,
             edgecolors='white', linewidths=0.4)
ax_c.text(te[0], te[1] - 0.6, 'goal', fontsize=5, color=GREEN_GOAL,
          ha='center', va='top', fontstyle='italic')

# Metrics
ax_c.text(1, 8.0, 'CAR = 26.8%', fontsize=6.5, color=BLUE,
          fontweight='bold', ha='left', path_effects=stroke_s)
ax_c.text(1, 6.7, 'TSR = 74.7%', fontsize=6, color=BLUE,
          fontweight='bold', ha='left', path_effects=stroke_s)

# Displacement bar C
ax_c_bar.barh(0, 300, height=0.5, color='#F0F0F0', edgecolor='#DDDDDD',
              linewidth=0.5, zorder=1)
ax_c_bar.barh(0, 288, height=0.5, color=BLUE, edgecolor=BLUE_DARK,
              linewidth=0.4, zorder=3)
ax_c_bar.text(144, 0, '> 288 mm', fontsize=6, va='center', ha='center',
              color='white', fontweight='semibold')
ax_c_bar.text(150, -0.5, 'Displacement', fontsize=5, va='top', ha='center',
              color=GRAY_TEXT)
ax_c_bar.set_xlim(0, 300)
ax_c_bar.set_ylim(-0.7, 0.7)
ax_c_bar.axis('off')


# ── Save ──
d = './output'
for ext in ('pdf', 'png'):
    fig.savefig(f'{d}/fig1_teaser_v2.{ext}', bbox_inches='tight', dpi=300, pad_inches=0.06)
print('Saved fig1_teaser_v2.pdf and fig1_teaser_v2.png')
