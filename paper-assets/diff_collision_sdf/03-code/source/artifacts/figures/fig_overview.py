"""Three-panel overview figure for CoRL 2026 paper.
Panel (a): Action-collapsed safety inflates CAR
Panel (b): EE-only SDF redistributes collisions to unmonitored links
Panel (c): Demonstrations, not SDF, account for avoidance gains
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Arc, Wedge
from matplotlib.lines import Line2D
import matplotlib.patheffects as pe
import numpy as np

# ── Global style ──
NAVY    = '#2C3E50'
RED     = '#C0392B'
GREEN   = '#27AE60'
GRAY    = '#7F8C8D'
LGRAY   = '#BDC3C7'
LBLUE   = '#EBF5FB'
WHITE   = '#FFFFFF'
GOLD    = '#F39C12'

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['STIXGeneral', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 9,
    'text.color': NAVY,
    'axes.edgecolor': NAVY,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'figure.facecolor': WHITE,
    'savefig.facecolor': WHITE,
})

fig = plt.figure(figsize=(14, 4.5), dpi=300)

# Panel widths: 35%, 30%, 35%
gs = fig.add_gridspec(1, 3, width_ratios=[0.35, 0.30, 0.35],
                      wspace=0.06, left=0.02, right=0.98,
                      top=0.92, bottom=0.04)

def fancy_box(ax, xy, w, h, fc=WHITE, ec=NAVY, lw=0.8, alpha=1.0, zorder=2,
              boxstyle='round,pad=0.02', shadow=True):
    box = FancyBboxPatch(xy, w, h, boxstyle=boxstyle,
                         facecolor=fc, edgecolor=ec, linewidth=lw,
                         alpha=alpha, zorder=zorder,
                         transform=ax.transData)
    if shadow:
        shadow_box = FancyBboxPatch((xy[0]+0.005, xy[1]-0.005), w, h,
                                    boxstyle=boxstyle,
                                    facecolor='#00000008', edgecolor='none',
                                    zorder=zorder-1, transform=ax.transData)
        ax.add_patch(shadow_box)
    ax.add_patch(box)
    return box

# ═══════════════════════════════════════════════
# PANEL (a): Action-Collapsed Safety Problem
# ═══════════════════════════════════════════════
ax_a = fig.add_subplot(gs[0])
ax_a.set_xlim(0, 1)
ax_a.set_ylim(0, 1)
ax_a.axis('off')

# Panel background
fancy_box(ax_a, (0.02, 0.02), 0.96, 0.96, fc=LBLUE, ec=LGRAY, lw=0.5,
          shadow=False, boxstyle='round,pad=0.01')

# Panel label
ax_a.text(0.06, 0.95, '(a)', fontsize=11, fontweight='bold', color=NAVY,
          va='top', ha='left')
ax_a.text(0.50, 0.95, 'The Action-Collapsed Safety Problem',
          fontsize=9, fontweight='bold', color=NAVY, va='top', ha='center',
          fontstyle='italic')

# ── Top: Frozen robot schematic ──
# Table surface
ax_a.plot([0.08, 0.92], [0.52, 0.52], color=LGRAY, lw=2, zorder=2)
ax_a.text(0.10, 0.50, 'table', fontsize=6.5, color=GRAY, va='top')

# Objects on table
for cx, cy, c in [(0.55, 0.56, '#3498DB'), (0.70, 0.55, RED), (0.82, 0.56, GREEN)]:
    obj = plt.Rectangle((cx-0.025, cy), 0.05, 0.06, fc=c, ec=NAVY,
                         lw=0.5, alpha=0.6, zorder=3)
    ax_a.add_patch(obj)

# Robot arm (frozen, dashed, semi-transparent)
# Base
base = plt.Rectangle((0.18, 0.52), 0.08, 0.04, fc=GRAY, ec=NAVY,
                      lw=0.5, alpha=0.35, zorder=3)
ax_a.add_patch(base)
# Arm segments (dashed outline to show "frozen")
arm_pts = [(0.22, 0.56), (0.22, 0.72), (0.32, 0.78), (0.38, 0.75)]
for i in range(len(arm_pts)-1):
    ax_a.plot([arm_pts[i][0], arm_pts[i+1][0]],
             [arm_pts[i][1], arm_pts[i+1][1]],
             color=GRAY, lw=5, alpha=0.3, solid_capstyle='round', zorder=3)
    ax_a.plot([arm_pts[i][0], arm_pts[i+1][0]],
             [arm_pts[i][1], arm_pts[i+1][1]],
             color=NAVY, lw=5, alpha=0.15, linestyle='--', zorder=4)

# Joint dots
for pt in arm_pts:
    ax_a.plot(pt[0], pt[1], 'o', color=GRAY, ms=4, mec=NAVY, mew=0.4,
             alpha=0.5, zorder=5)

# End effector
ax_a.plot(0.38, 0.75, 'v', color=GRAY, ms=6, mec=NAVY, mew=0.5,
         alpha=0.5, zorder=5)

# Displacement annotation
ax_a.annotate('displacement\n< 0.1 mm', xy=(0.38, 0.73), xytext=(0.15, 0.84),
             fontsize=6, color=GRAY, ha='center', va='center',
             fontstyle='italic',
             arrowprops=dict(arrowstyle='->', color=GRAY, lw=0.6),
             bbox=dict(boxstyle='round,pad=0.15', fc=WHITE, ec=GRAY, lw=0.4))

# "Illusory Safety" label
ax_a.text(0.38, 0.65, 'Illusory\nSafety', fontsize=7, color=RED,
         fontweight='bold', ha='center', va='center',
         bbox=dict(boxstyle='round,pad=0.15', fc='#FDEDEC', ec=RED, lw=0.6))

# CAR badge (cracked)
badge_x, badge_y = 0.72, 0.77
circle_bg = Circle((badge_x, badge_y), 0.11, fc=WHITE, ec=NAVY, lw=1.2,
                    zorder=4, transform=ax_a.transData)
ax_a.add_patch(circle_bg)
ax_a.text(badge_x, badge_y+0.025, '91.5%', fontsize=10, fontweight='bold',
         color=NAVY, ha='center', va='center', zorder=5)
ax_a.text(badge_x, badge_y-0.04, 'CAR', fontsize=7, color=NAVY,
         ha='center', va='center', zorder=5)

# Red X over badge
ax_a.plot([badge_x-0.07, badge_x+0.07], [badge_y-0.07, badge_y+0.07],
         color=RED, lw=2.5, alpha=0.7, zorder=6)
ax_a.plot([badge_x-0.07, badge_x+0.07], [badge_y+0.07, badge_y-0.07],
         color=RED, lw=2.5, alpha=0.7, zorder=6)

# ── Bottom: Before/After comparison ──
# Reported CAR box (faded/crossed out)
fancy_box(ax_a, (0.06, 0.22), 0.36, 0.18, fc='#F9EBEA', ec=LGRAY, lw=0.6)
ax_a.text(0.24, 0.35, 'Reported CAR', fontsize=6.5, color=GRAY,
         ha='center', va='center')
ax_a.text(0.24, 0.28, '91.5%', fontsize=11, color=GRAY,
         ha='center', va='center', fontweight='bold', alpha=0.5)
# Strikethrough
ax_a.plot([0.12, 0.36], [0.28, 0.28], color=RED, lw=1.5, alpha=0.6)

# Arrow between boxes
ax_a.annotate('', xy=(0.58, 0.31), xytext=(0.44, 0.31),
             arrowprops=dict(arrowstyle='->', color=RED, lw=1.2))
ax_a.text(0.51, 0.39, '99.6% are\ncollapsed', fontsize=5.5, color=RED,
         ha='center', va='center', fontstyle='italic')

# dfCAR box (green, true safety)
fancy_box(ax_a, (0.58, 0.22), 0.36, 0.18, fc='#EAFAF1', ec=GREEN, lw=1.0)
ax_a.text(0.76, 0.35, 'dfCAR (filtered)', fontsize=6.5, color=GREEN,
         ha='center', va='center', fontweight='bold')
ax_a.text(0.76, 0.27, r'$\approx$ 0%', fontsize=12, color=GREEN,
         ha='center', va='center', fontweight='bold')

# Key message
fancy_box(ax_a, (0.10, 0.05), 0.80, 0.12, fc=WHITE, ec=NAVY, lw=0.8)
ax_a.text(0.50, 0.11, r'High CAR $\neq$ Safe behavior',
         fontsize=8, color=NAVY, ha='center', va='center', fontweight='bold')


# ═══════════════════════════════════════════════
# PANEL (b): EE-Only SDF Fails
# ═══════════════════════════════════════════════
ax_b = fig.add_subplot(gs[1])
ax_b.set_xlim(0, 1)
ax_b.set_ylim(0, 1)
ax_b.axis('off')

fancy_box(ax_b, (0.02, 0.02), 0.96, 0.96, fc=LBLUE, ec=LGRAY, lw=0.5,
          shadow=False, boxstyle='round,pad=0.01')

ax_b.text(0.06, 0.95, '(b)', fontsize=11, fontweight='bold', color=NAVY,
          va='top', ha='left')
ax_b.text(0.52, 0.95, 'EE-Only SDF Cannot Ensure\nFull-Body Safety',
          fontsize=9, fontweight='bold', color=NAVY, va='top', ha='center',
          fontstyle='italic', linespacing=1.2)

# ── Robot arm side view ──
# Base
base_b = plt.Rectangle((0.10, 0.42), 0.12, 0.06, fc=LGRAY, ec=NAVY,
                        lw=0.8, zorder=3)
ax_b.add_patch(base_b)
ax_b.text(0.16, 0.44, 'base', fontsize=5.5, color=GRAY, ha='center', va='center')

# Arm joints and links
joints = [(0.16, 0.48), (0.16, 0.64), (0.35, 0.72), (0.55, 0.68),
          (0.72, 0.62)]

# Draw links
link_colors = [GRAY, GRAY, GRAY, GRAY]
link_widths = [6, 5, 4, 3]
for i in range(len(joints)-1):
    ax_b.plot([joints[i][0], joints[i+1][0]],
             [joints[i][1], joints[i+1][1]],
             color=LGRAY, lw=link_widths[i], solid_capstyle='round', zorder=3)
    ax_b.plot([joints[i][0], joints[i+1][0]],
             [joints[i][1], joints[i+1][1]],
             color=NAVY, lw=link_widths[i], solid_capstyle='round',
             alpha=0.2, zorder=4)

# Joint dots
for j in joints:
    ax_b.plot(j[0], j[1], 'o', color=WHITE, ms=5, mec=NAVY, mew=0.8, zorder=5)

# EE (end effector) — green dot (monitored)
ax_b.plot(0.72, 0.62, 'o', color=GREEN, ms=8, mec=NAVY, mew=0.8, zorder=6)
ax_b.text(0.72, 0.56, 'EE\n(monitored)', fontsize=5.5, color=GREEN,
         ha='center', va='top', fontweight='bold')

# Obstacle (red rectangle)
obs = plt.Rectangle((0.60, 0.36), 0.08, 0.28, fc='#FDEDEC', ec=RED,
                     lw=1.2, alpha=0.8, zorder=2)
ax_b.add_patch(obs)
ax_b.text(0.64, 0.50, 'obstacle', fontsize=6, color=RED, ha='center',
         va='center', fontstyle='italic', rotation=90, alpha=0.7)

# Green arrow: SDF pushes EE away from obstacle
ax_b.annotate('', xy=(0.84, 0.62), xytext=(0.74, 0.62),
             arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.0,
                            mutation_scale=15))
ax_b.text(0.88, 0.64, 'SDF gradient\npushes EE away', fontsize=5.5,
         color=GREEN, ha='center', va='bottom', fontweight='bold',
         fontstyle='italic')

# Red arrow: intermediate link rotates INTO obstacle
# Collision starburst at intermediate link–obstacle intersection
coll_x, coll_y = 0.52, 0.55
# Larger starburst
angles = np.linspace(0, 2*np.pi, 13)[:-1]
for a in angles:
    r = 0.055
    ax_b.plot([coll_x, coll_x + r*np.cos(a)],
             [coll_y, coll_y + r*np.sin(a)],
             color=RED, lw=1.5, alpha=0.65, zorder=6)
ax_b.plot(coll_x, coll_y, '*', color=RED, ms=14, mec='#A93226',
         mew=0.5, zorder=7)

# Red curved arrow showing rotation into obstacle
ax_b.annotate('', xy=(0.56, 0.50), xytext=(0.45, 0.58),
             arrowprops=dict(arrowstyle='->', color=RED, lw=1.8,
                            connectionstyle='arc3,rad=-0.3',
                            mutation_scale=12))

ax_b.text(0.28, 0.55, 'Joint coupling\nrotates link\nINTO obstacle',
         fontsize=5.5, color=RED, ha='center', va='center',
         fontweight='bold', fontstyle='italic',
         bbox=dict(boxstyle='round,pad=0.15', fc='#FDEDEC', ec=RED, lw=0.5))

# "Unmonitored" labels on intermediate links
ax_b.text(0.25, 0.78, 'unmonitored', fontsize=5, color=GRAY,
         ha='center', fontstyle='italic',
         bbox=dict(boxstyle='round,pad=0.1', fc=WHITE, ec=LGRAY, lw=0.3))
ax_b.annotate('', xy=(0.25, 0.68), xytext=(0.25, 0.76),
             arrowprops=dict(arrowstyle='->', color=GRAY, lw=0.5))

# ── Result box at bottom ──
fancy_box(ax_b, (0.06, 0.05), 0.88, 0.24, fc=WHITE, ec=NAVY, lw=0.8)

ax_b.text(0.50, 0.24, 'Oracle SDF CAR: 73–77%', fontsize=7, color=RED,
         ha='center', va='center', fontweight='bold')
ax_b.text(0.50, 0.17, 'No-refine baseline: 82–83%', fontsize=7, color=NAVY,
         ha='center', va='center')

# Conclusion line
ax_b.plot([0.15, 0.85], [0.155, 0.155], color=LGRAY, lw=0.5, ls=':')
ax_b.text(0.50, 0.10, r'Perfect SDF signal makes safety WORSE $\downarrow$',
         fontsize=7, color=RED, ha='center', va='center',
         fontweight='bold', fontstyle='italic')


# ═══════════════════════════════════════════════
# PANEL (c): Avoidance Source
# ═══════════════════════════════════════════════
ax_c = fig.add_subplot(gs[2])
ax_c.set_xlim(0, 1)
ax_c.set_ylim(0, 1)
ax_c.axis('off')

fancy_box(ax_c, (0.02, 0.02), 0.96, 0.96, fc=LBLUE, ec=LGRAY, lw=0.5,
          shadow=False, boxstyle='round,pad=0.01')

ax_c.text(0.06, 0.95, '(c)', fontsize=11, fontweight='bold', color=NAVY,
          va='top', ha='left')
ax_c.text(0.52, 0.95, 'Avoidance Source:\nDemonstrations, Not SDF',
          fontsize=9, fontweight='bold', color=NAVY, va='top', ha='center',
          fontstyle='italic', linespacing=1.2)

# ── Source 1: Collision-Free Demonstrations (dominant) ──
fancy_box(ax_c, (0.05, 0.62), 0.35, 0.16, fc='#EAFAF1', ec=GREEN, lw=1.0)
# Film strip icon (simplified)
for yi in [0.73, 0.70, 0.67]:
    ax_c.plot([0.08, 0.13], [yi, yi], color=GREEN, lw=1.5, alpha=0.4)
ax_c.text(0.24, 0.70, 'Collision-Free\nDemonstrations', fontsize=7,
         color=NAVY, ha='center', va='center', fontweight='bold',
         linespacing=1.2)

# THICK green arrow → result (dramatically thick)
arrow_y1 = 0.70
ax_c.annotate('', xy=(0.62, arrow_y1), xytext=(0.42, arrow_y1),
             arrowprops=dict(arrowstyle='->', color=GREEN, lw=8,
                            mutation_scale=25, alpha=0.65))
ax_c.text(0.52, 0.76, '+26 pp CAR', fontsize=8, color=GREEN,
         ha='center', va='bottom', fontweight='bold')
ax_c.text(0.52, 0.63, r'$p < 0.001$ $\checkmark$', fontsize=6.5, color=GREEN,
         ha='center', va='top', fontweight='bold')

# Result box
fancy_box(ax_c, (0.62, 0.62), 0.32, 0.16, fc=WHITE, ec=GREEN, lw=1.0)
ax_c.text(0.78, 0.73, '54.7%', fontsize=14, color=GREEN,
         ha='center', va='center', fontweight='bold')
ax_c.text(0.78, 0.65, 'CAR', fontsize=7, color=NAVY,
         ha='center', va='center')

# ── Source 2: SDF Supervision (negligible) ──
fancy_box(ax_c, (0.05, 0.38), 0.35, 0.16, fc='#F8F9F9', ec=LGRAY, lw=0.8)
# SDF gradient icon (simplified)
for xi, al in [(0.08, 0.15), (0.10, 0.25), (0.12, 0.35)]:
    ax_c.plot([xi, xi], [0.42, 0.50], color=GRAY, lw=2, alpha=al)
ax_c.text(0.24, 0.48, 'SDF Supervision', fontsize=7,
         color=GRAY, ha='center', va='center', fontweight='bold')
ax_c.text(0.24, 0.41, r'$\lambda \in \{0.005, 0.01, 0.1\}$', fontsize=6,
         color=GRAY, ha='center', va='center')

# THIN gray dashed arrow → result area
arrow_y2 = 0.46
ax_c.annotate('', xy=(0.62, arrow_y2), xytext=(0.42, arrow_y2),
             arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.0,
                            linestyle='dashed', mutation_scale=10,
                            alpha=0.6))
ax_c.text(0.52, 0.52, '+2.3 pp', fontsize=7, color=GRAY,
         ha='center', va='bottom')
ax_c.text(0.52, 0.40, r'$p = 0.131$, n.s. $\times$', fontsize=6, color=GRAY,
         ha='center', va='top', fontstyle='italic')

# 20x range annotation
ax_c.text(0.24, 0.34, r'20$\times$ range of $\lambda$ — all within null band',
         fontsize=5.5, color=GRAY, ha='center', va='center',
         fontstyle='italic')

# ── Conclusion box ──
fancy_box(ax_c, (0.06, 0.06), 0.88, 0.18, fc='#EAFAF1', ec=GREEN, lw=1.0)
ax_c.text(0.50, 0.15, 'Avoidance arises from demonstration data,',
         fontsize=7.5, color=NAVY, ha='center', va='center', fontweight='bold')
ax_c.text(0.50, 0.09, 'not geometric supervision',
         fontsize=7.5, color=NAVY, ha='center', va='center', fontweight='bold')


# ── Save ──
outdir = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures'
fig.savefig(f'{outdir}/fig_overview.pdf', bbox_inches='tight', dpi=300)
fig.savefig(f'{outdir}/fig_overview.png', bbox_inches='tight', dpi=150)
plt.close(fig)
print(f'Saved: {outdir}/fig_overview.pdf and fig_overview.png')
