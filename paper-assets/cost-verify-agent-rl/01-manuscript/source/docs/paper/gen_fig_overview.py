import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.06,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'stix',
})

RED_DARK = '#9B2C2C'
RED_MED = '#C0392B'
RED_FILL = '#FADBD8'
RED_ICON_BD = '#D98880'
BLUE_DARK = '#1A5276'
BLUE_MED = '#0072B2'
BLUE_LIGHT = '#D4E6F1'
BLUE_ARROW = '#2980B9'
GREEN_DARK = '#1E8449'
GREEN_LIGHT = '#D5F5E3'
GREEN_BD = '#82E0AA'
FAIL_RED = '#C0392B'
FAIL_BG = '#FDEDEC'
FAIL_BD = '#F1948A'
GRAY_MED = '#888888'
GRAY_LIGHT = '#D5D8DC'
GRAY_BG = '#FAFAFA'
SHADOW = '#0000000D'

fig, (ax_L, ax_R) = plt.subplots(1, 2, figsize=(7.2, 3.2),
                                  gridspec_kw={'wspace': 0.15})
for ax in (ax_L, ax_R):
    ax.set_xlim(-0.1, 10.1)
    ax.set_ylim(0.4, 10.3)
    ax.set_aspect('equal')
    ax.axis('off')


def sbox(ax, xy, w, h, style="round,pad=0.06",
         fc='white', ec='gray', lw=1.0, zorder=2, so=(0.06, -0.06)):
    ax.add_patch(FancyBboxPatch((xy[0]+so[0], xy[1]+so[1]), w, h,
                 boxstyle=style, fc=SHADOW, ec='none', zorder=zorder-0.5))
    p = FancyBboxPatch(xy, w, h, boxstyle=style, fc=fc, ec=ec, lw=lw, zorder=zorder)
    ax.add_patch(p)
    return p


# Panel backgrounds
ax_L.add_patch(mpatches.Rectangle((-0.1, 0.4), 10.2, 9.9,
               fc='#FDFAF9', ec='none', zorder=0, alpha=0.4))
ax_R.add_patch(mpatches.Rectangle((-0.1, 0.4), 10.2, 9.9,
               fc='#F5FAFD', ec='none', zorder=0, alpha=0.4))

bar_y = 5.6
bar_h = 1.2
bar_x0 = 0.5
bar_x1 = 9.5
n_w = 5
ww = (bar_x1 - bar_x0) / n_w

# ============================================================
#  LEFT: Step-Independent Windowing
# ============================================================
ax_L.text(5.0, 10.0, 'Step-Independent Windowing', fontsize=11.5,
          fontweight='bold', ha='center', va='top', color=RED_DARK)

# M1 label
ax_L.text(5.0, 9.0, 'M1: Truncated Context', fontsize=8.5,
          fontweight='bold', ha='center', va='center', color=RED_MED,
          bbox=dict(boxstyle='round,pad=0.2', fc='#FEF0EF', ec='none', alpha=0.7))

# Broken context arrows with break marks
arrow_y = 7.9
for i in range(n_w):
    x_left = bar_x0 + i * ww + 0.3
    x_right = bar_x0 + (i + 1) * ww - 0.2
    ax_L.annotate('', xy=(x_left, arrow_y), xytext=(x_right, arrow_y),
                  arrowprops=dict(arrowstyle='-|>', color=RED_MED,
                                  lw=1.3, alpha=0.55, mutation_scale=9))

# Subtle X break marks at boundaries
for i in range(1, n_w):
    bx = bar_x0 + i * ww
    size = 0.13
    for dx, dy in [(1, 1), (1, -1)]:
        ax_L.plot([bx - size*dx, bx + size*dx],
                  [arrow_y - size*dy, arrow_y + size*dy],
                  color=RED_MED, lw=0.8, alpha=0.5, zorder=5,
                  solid_capstyle='round')

# Trajectory bar
ax_L.text(5.0, bar_y + bar_h + 0.1, 'Multi-Turn Agent Trajectory',
          fontsize=7.5, ha='center', va='bottom', color=GRAY_MED,
          fontstyle='italic')
sbox(ax_L, (bar_x0, bar_y), bar_x1-bar_x0, bar_h,
     style="round,pad=0.04", fc=GRAY_BG, ec=GRAY_LIGHT, lw=0.8, zorder=2)

wc = ['#FEF0EF', '#FBE4E2', '#FEF0EF', '#FBE4E2', '#FEF0EF']
for i in range(n_w):
    x = bar_x0 + i * ww + 0.04
    w = ww - 0.08
    ax_L.add_patch(FancyBboxPatch((x, bar_y + 0.04), w, bar_h - 0.08,
                   boxstyle="round,pad=0.02", fc=wc[i], ec=RED_ICON_BD,
                   lw=0.5, alpha=0.85, zorder=3))
    ax_L.text(x + w/2, bar_y + bar_h/2, f'$w_{i+1}$',
              fontsize=8.5, ha='center', va='center', color=GRAY_MED, zorder=4)

for i in range(1, n_w):
    bx = bar_x0 + i * ww
    ax_L.plot([bx, bx], [bar_y - 0.05, bar_y + bar_h + 0.05],
              color=RED_MED, lw=0.5, ls=(0, (3, 3)), zorder=5, alpha=0.35)

# M2 label
ax_L.text(5.0, 4.3, 'M2: Sign Misattribution', fontsize=8.5,
          fontweight='bold', ha='center', va='center', color=RED_MED,
          bbox=dict(boxstyle='round,pad=0.2', fc='#FEF0EF', ec='none', alpha=0.7))

# Minus icons
iy = 2.9
is_ = 0.7
for i in range(n_w):
    cx = bar_x0 + (i + 0.5) * ww
    sbox(ax_L, (cx-is_/2, iy), is_, is_,
         style="round,pad=0.04", fc=RED_FILL, ec=RED_ICON_BD,
         lw=0.6, zorder=3, so=(0.04, -0.04))
    ax_L.text(cx, iy + is_/2, '−', fontsize=11,
              ha='center', va='center', color=RED_MED, fontweight='bold', zorder=4)

# w2 callout
w2_cx = bar_x0 + 1.5 * ww
# Thin connecting line from minus icon to callout
ax_L.plot([w2_cx, w2_cx], [iy - 0.05, 2.15], color=GRAY_MED,
          lw=0.5, ls=':', alpha=0.4, zorder=1)
ax_L.text(w2_cx, iy - 0.15, '✗', fontsize=7.5, ha='center', va='top',
          color=RED_MED, fontweight='bold',
          path_effects=[pe.withStroke(linewidth=2, foreground='white')])
cw, ch = 1.3, 0.62
sbox(ax_L, (w2_cx - cw/2, 1.35), cw, ch,
     style="round,pad=0.06", fc=GREEN_LIGHT, ec=GREEN_BD,
     lw=0.6, zorder=3, so=(0.03, -0.03))
ax_L.text(w2_cx, 1.35 + ch/2, 'Correct\nAction', fontsize=6.5,
          ha='center', va='center', color=GREEN_DARK, fontweight='bold',
          linespacing=1.1, zorder=4)


# ============================================================
#  RIGHT: Episode-Level Training
# ============================================================
ax_R.text(5.0, 10.0, 'Episode-Level Training', fontsize=11.5,
          fontweight='bold', ha='center', va='top', color=BLUE_DARK)

# M1 label
ax_R.text(5.0, 9.0, 'M1: Full Context Preserved', fontsize=8.5,
          fontweight='bold', ha='center', va='center', color=BLUE_MED,
          bbox=dict(boxstyle='round,pad=0.2', fc='#EBF5FB', ec='none', alpha=0.7))

# Single unbroken arrow
ax_R.add_patch(FancyArrowPatch((9.3, 7.9), (0.7, 7.9),
               arrowstyle='-|>', mutation_scale=14,
               color=BLUE_ARROW, lw=2.5, alpha=0.8, zorder=3))

# Full trajectory bar
sbox(ax_R, (bar_x0, bar_y), bar_x1-bar_x0, bar_h,
     style="round,pad=0.06", fc=BLUE_LIGHT, ec=BLUE_MED,
     lw=1.2, zorder=2)
ax_R.text(5.0, bar_y + bar_h/2, 'Full Episode Trajectory',
          fontsize=9, ha='center', va='center', color=BLUE_DARK,
          fontweight='bold', zorder=3)

# M2 label
ax_R.text(5.0, 4.3, 'M2: Episode-Level Attribution', fontsize=8.5,
          fontweight='bold', ha='center', va='center', color=BLUE_MED,
          bbox=dict(boxstyle='round,pad=0.2', fc='#EBF5FB', ec='none', alpha=0.7))

# A_episode box
aw, ah = 2.5, 1.1
ax_, ay = 1.5, 2.3
sbox(ax_R, (ax_, ay), aw, ah,
     style="round,pad=0.08", fc=BLUE_LIGHT, ec=BLUE_MED,
     lw=1.0, zorder=3)
ax_R.text(ax_ + aw/2, ay + ah/2,
          r'$\hat{A}_{\mathrm{episode}}$',
          fontsize=15, ha='center', va='center', color=BLUE_DARK, zorder=4)

# Pass box
px, py = 6.8, 3.2
pw, ph = 1.5, 0.72
sbox(ax_R, (px, py), pw, ph,
     style="round,pad=0.06", fc=GREEN_LIGHT, ec=GREEN_BD,
     lw=0.7, zorder=3, so=(0.04, -0.04))
ax_R.text(px + pw/2, py + ph/2, 'Pass', fontsize=9, ha='center', va='center',
          color=GREEN_DARK, fontweight='bold', zorder=4)
ax_R.text(px + pw + 0.25, py + ph/2, '+', fontsize=11, ha='left', va='center',
          color=GREEN_DARK, fontweight='bold', zorder=4)

# Fail box
fx, fy = 6.8, 1.6
fw, fh = 1.5, 0.72
sbox(ax_R, (fx, fy), fw, fh,
     style="round,pad=0.06", fc=FAIL_BG, ec=FAIL_BD,
     lw=0.7, zorder=3, so=(0.04, -0.04))
ax_R.text(fx + fw/2, fy + fh/2, 'Fail', fontsize=9, ha='center', va='center',
          color=FAIL_RED, fontweight='bold', zorder=4)
ax_R.text(fx + fw + 0.25, fy + fh/2, '−', fontsize=11, ha='left', va='center',
          color=FAIL_RED, fontweight='bold', zorder=4)

# Arrows from A_episode to Pass/Fail
for ty, tx, rad in [(py + ph/2, px, 0.15), (fy + fh/2, fx, -0.15)]:
    ax_R.add_patch(FancyArrowPatch(
        (ax_ + aw, ay + ah/2), (tx, ty),
        arrowstyle='-|>', mutation_scale=10,
        color=BLUE_ARROW, lw=1.2, alpha=0.5,
        connectionstyle=f'arc3,rad={rad}', zorder=2))

# Divider
fig.add_artist(plt.Line2D([0.5, 0.5], [0.03, 0.97],
               transform=fig.transFigure, color=GRAY_LIGHT, lw=0.8, alpha=0.5))

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper'
out = f'{out_dir}/fig_overview'
plt.savefig(out + '.png', format='png')
plt.savefig(out + '.pdf', format='pdf')
plt.savefig('/tmp/fig_overview_v7.png', format='png')
print("Saved to", out)
