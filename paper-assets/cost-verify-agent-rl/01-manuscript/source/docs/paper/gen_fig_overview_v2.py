import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.12,
})

RED = '#D62728'
RED_DARK = '#C0392B'
BLUE = '#1F77B4'
GREEN = '#27AE60'
GREEN_DARK = '#1E8449'
FAIL_RED = '#E74C3C'
FAIL_RED_DARK = '#922B21'
GRAY = '#888888'
GRAY_LIGHT = '#AAAAAA'

M1_COLOR = '#EE7733'
M1_DARK = '#CC5500'
M2_COLOR = '#4477AA'
M2_DARK = '#335588'

fig, (ax_L, ax_R) = plt.subplots(1, 2, figsize=(7.0, 3.2),
                                  gridspec_kw={'wspace': 0.15})
for ax in (ax_L, ax_R):
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 11.0)
    ax.set_aspect('equal')
    ax.axis('off')

# ======== SHARED PARAMS ========
bar_y = 6.0
bar_h = 1.0
bar_x0 = 0.5
bar_x1 = 9.5

# ============================================================
#  LEFT: Step-Independent Windowing
# ============================================================
ax_L.text(5.0, 10.8, 'Step-Independent Windowing', fontsize=11,
          fontweight='bold', ha='center', va='top', color=RED)

n_w = 5
ww = (bar_x1 - bar_x0) / n_w
win_cols = ['#FDCECE', '#F5B7B7', '#FDCECE', '#F5B7B7', '#FDCECE']

for i in range(n_w):
    x = bar_x0 + i * ww
    ax_L.add_patch(FancyBboxPatch((x + 0.04, bar_y), ww - 0.08, bar_h,
                                   boxstyle="round,pad=0.04",
                                   fc=win_cols[i], ec=RED_DARK, lw=0.8))
    ax_L.text(x + ww / 2, bar_y + bar_h / 2, f'$w_{i+1}$',
              fontsize=7.5, ha='center', va='center', color=GRAY_LIGHT)

# Dashed cuts
for i in range(1, n_w):
    bx = bar_x0 + i * ww
    ax_L.plot([bx, bx], [bar_y - 0.15, bar_y + bar_h + 0.15],
              color=M1_COLOR, lw=1.2, ls='--', zorder=5)

# Advantage labels
for i in range(n_w):
    cx = bar_x0 + (i + 0.5) * ww
    ax_L.text(cx, bar_y + bar_h + 0.3, f'$\\hat{{A}}_{i+1}$',
              fontsize=8.5, ha='center', va='bottom', color=RED_DARK)

# M1 annotation
m1_y = 9.3
ax_L.text(5.0, m1_y, 'M1: Truncated context  ✂',
          fontsize=8, fontweight='bold', ha='center', va='bottom', color=M1_COLOR)
cut1_x = bar_x0 + 1 * ww
cut2_x = bar_x0 + 3 * ww
ax_L.annotate('', xy=(cut1_x, bar_y + bar_h + 0.2),
              xytext=(4.2, m1_y - 0.05),
              arrowprops=dict(arrowstyle='->', color=M1_COLOR, lw=1.0,
                              connectionstyle='arc3,rad=0.25'))
ax_L.annotate('', xy=(cut2_x, bar_y + bar_h + 0.2),
              xytext=(5.8, m1_y - 0.05),
              arrowprops=dict(arrowstyle='->', color=M1_COLOR, lw=1.0,
                              connectionstyle='arc3,rad=-0.2'))

# Episode span arrow
ax_L.annotate('', xy=(bar_x0, bar_y - 0.35),
              xytext=(bar_x1, bar_y - 0.35),
              arrowprops=dict(arrowstyle='<->', color=GRAY, lw=0.7))
ax_L.text(5.0, bar_y - 0.6, 'Episode trajectory (fail)',
          fontsize=7, ha='center', va='top', color=GRAY)

# Minus signs
for i in range(n_w):
    cx = bar_x0 + (i + 0.5) * ww
    ax_L.text(cx, bar_y - 1.3, '−', fontsize=11, ha='center', va='center',
              color=M2_DARK, fontweight='bold')

# w2 annotation
w2_cx = bar_x0 + 1.5 * ww
ax_L.text(w2_cx, bar_y - 2.0, '✓ correct step,\nstill penalized',
          fontsize=6, ha='center', va='top', color=GRAY, style='italic')

# M2 annotation
ax_L.annotate('M2: Sign misattribution',
              xy=(w2_cx + 0.1, bar_y - 1.9),
              xytext=(6.5, 1.8),
              fontsize=8, fontweight='bold', color=M2_COLOR,
              arrowprops=dict(arrowstyle='->', color=M2_COLOR, lw=1.0,
                              connectionstyle='arc3,rad=0.25'))

# Bottom summary boxes
ax_L.text(2.2, 0.3, 'M1: information loss',
          fontsize=6.5, ha='center', va='center', color=M1_COLOR, fontweight='bold',
          bbox=dict(boxstyle='round,pad=0.35', fc='#FFF0E0', ec='#EEBB88', lw=0.6))
ax_L.text(7.8, 0.3, 'M2: sign misattribution',
          fontsize=6.5, ha='center', va='center', color=M2_COLOR, fontweight='bold',
          bbox=dict(boxstyle='round,pad=0.35', fc='#E0EEF8', ec='#88AACC', lw=0.6))

# ============================================================
#  RIGHT: Episode-Level Training
# ============================================================
ax_R.text(5.0, 10.8, 'Episode-Level Training', fontsize=11,
          fontweight='bold', ha='center', va='top', color=BLUE)

# Unified bar
ax_R.add_patch(FancyBboxPatch((bar_x0, bar_y), bar_x1 - bar_x0, bar_h,
                               boxstyle="round,pad=0.08",
                               fc='#D4E6F1', ec=BLUE, lw=1.5))
ax_R.text(5.0, bar_y + bar_h / 2, 'Full context preserved',
          fontsize=9, ha='center', va='center', color=BLUE, fontweight='bold')

# Bracket + advantage
by = bar_y + bar_h + 0.15
ax_R.plot([bar_x0 + 0.2, bar_x0 + 0.2, bar_x1 - 0.2, bar_x1 - 0.2],
          [by, by + 0.15, by + 0.15, by],
          color=BLUE, lw=1.0, solid_capstyle='round')
ax_R.text(5.0, by + 0.3, r'$\hat{A}_{\mathrm{episode}}$', fontsize=10,
          ha='center', va='bottom', color=BLUE, fontweight='bold')

# Episode span
ax_R.annotate('', xy=(bar_x0, bar_y - 0.35),
              xytext=(bar_x1, bar_y - 0.35),
              arrowprops=dict(arrowstyle='<->', color=GRAY, lw=0.7))
ax_R.text(5.0, bar_y - 0.6, 'Episode trajectory',
          fontsize=7, ha='center', va='top', color=GRAY)

# Pass / Fail boxes
ep_x0, ep_x1, ep_h = 1.0, 9.0, 0.85

ep_y1 = 3.2
ax_R.add_patch(FancyBboxPatch((ep_x0, ep_y1), ep_x1 - ep_x0, ep_h,
                               boxstyle="round,pad=0.06",
                               fc='#D5F5E3', ec=GREEN, lw=1.0))
ax_R.text(ep_x0 - 0.3, ep_y1 + ep_h / 2, '✓', fontsize=10,
          ha='right', va='center', color=GREEN)
ax_R.text(5.0, ep_y1 + ep_h / 2,
          r'Pass  $\rightarrow$  $\hat{A} > 0$  (reinforce)',
          fontsize=8, ha='center', va='center', color=GREEN_DARK, fontweight='bold')

ep_y2 = 1.9
ax_R.add_patch(FancyBboxPatch((ep_x0, ep_y2), ep_x1 - ep_x0, ep_h,
                               boxstyle="round,pad=0.06",
                               fc='#FADBD8', ec=FAIL_RED, lw=1.0))
ax_R.text(ep_x0 - 0.3, ep_y2 + ep_h / 2, '✗', fontsize=10,
          ha='right', va='center', color=FAIL_RED)
ax_R.text(5.0, ep_y2 + ep_h / 2,
          r'Fail  $\rightarrow$  $\hat{A} < 0$  (suppress)',
          fontsize=8, ha='center', va='center', color=FAIL_RED_DARK, fontweight='bold')

# Bottom summary boxes
ax_R.text(2.5, 0.3, 'No M1 (full traj.)',
          fontsize=6.5, ha='center', va='center', color=BLUE, fontweight='bold',
          bbox=dict(boxstyle='round,pad=0.35', fc='#EBF5FB', ec='#AED6F1', lw=0.6))
ax_R.text(7.5, 0.3, 'No M2 (correct attrib.)',
          fontsize=6.5, ha='center', va='center', color=BLUE, fontweight='bold',
          bbox=dict(boxstyle='round,pad=0.35', fc='#EBF5FB', ec='#AED6F1', lw=0.6))

# Thin vertical divider
fig.add_artist(plt.Line2D([0.5, 0.5], [0.03, 0.97],
                           transform=fig.transFigure,
                           color='#D5D8DC', lw=1.0))

out = '/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/fig_overview'
plt.savefig(out + '.pdf', format='pdf')
plt.savefig(out + '.png', format='png')
print("Done")
