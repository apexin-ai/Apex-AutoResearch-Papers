import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os, sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/artifacts')
from visual_design_language_v2 import (
    apply_style, COLORS, FIGSIZE, style_axes, LEGEND
)
apply_style()

generations = np.arange(11)

r0_reff   = np.array([417.55, 491.12, 496.17, 493.60, 487.75, 479.77, 472.39, 464.10, 455.83, 446.60, 438.05])
r02_reff  = np.array([417.55, 476.01, 481.03, 486.77, 489.84, 492.37, 496.14, 497.15, 501.15, 504.47, 508.62])
r025_reff = np.array([417.55, 476.08, 483.41, 489.02, 491.99, 495.25, 498.39, 501.80, 505.59, 510.12, 513.82])
r03_reff  = np.array([417.55, 476.86, 483.87, 489.65, 493.70, 497.88, 501.88, 506.31, 511.34, 516.52, 521.11])
r05_reff  = np.array([417.55, 476.90, 487.96, 495.25, 502.55, 511.45, 519.50, 527.15, 536.68, 545.54, 553.46])

fig, ax = plt.subplots(figsize=FIGSIZE['single'])

ax.plot(generations, r0_reff, '-', color=COLORS['r0'],
        marker='o', markersize=3.5, markeredgecolor='white', markeredgewidth=0.4,
        linewidth=1.2, label=r'$r = 0$', zorder=3)
ax.plot(generations, r02_reff, '-', color=COLORS['r02'],
        marker='s', markersize=3.0, markeredgecolor='white', markeredgewidth=0.4,
        linewidth=1.2, label=r'$r = 0.2$', zorder=3)
ax.plot(generations, r025_reff, '-', color=COLORS['r025'],
        marker='^', markersize=3.5, markeredgecolor='white', markeredgewidth=0.4,
        linewidth=1.2, label=r'$r = 0.25$', zorder=3)
ax.plot(generations, r03_reff, '-', color=COLORS['r03'],
        marker='D', markersize=3.0, markeredgecolor='white', markeredgewidth=0.4,
        linewidth=1.2, label=r'$r = 0.3$', zorder=3)
ax.plot(generations, r05_reff, '--', color=COLORS['r05'],
        marker='v', markersize=3.5, markeredgecolor='white', markeredgewidth=0.4,
        linewidth=1.2, label=r'$r = 0.5$', zorder=3)

ax.axhline(y=417.55, color=COLORS['light_ref'], linestyle=':', linewidth=0.6, zorder=0)
ax.text(0.3, 413, r'$r_{\mathrm{eff},0}$', fontsize=6.5, color=COLORS['light_ref'],
        ha='left', va='top')

t = ax.text(10.3, r0_reff[-1], 'Type I', fontsize=6.5, color=COLORS['r0'],
            va='center', ha='left', clip_on=False, fontstyle='italic')
t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])

bracket_x = 10.3
y_bot = r02_reff[-1]
y_top = r05_reff[-1]
y_mid = (y_top + y_bot) / 2

ax.annotate('', xy=(bracket_x, y_bot - 1), xytext=(bracket_x, y_top + 1),
            arrowprops=dict(arrowstyle='|-|,widthA=0.3,widthB=0.3',
                            color=COLORS['annotation'], lw=0.6),
            annotation_clip=False)
ax.text(bracket_x + 0.5, y_mid, 'all ↑\n(2-type\nonly)',
        fontsize=6.5, color=COLORS['baseline'], va='center', ha='left',
        linespacing=1.1, clip_on=False)

ax.set_xlabel('Generation')
ax.set_ylabel(r'$r_{\mathrm{eff}}$ (Effective Rank)')
ax.set_xticks(generations)
ax.set_xlim(-0.3, 10.3)
ax.legend(**{**LEGEND, 'columnspacing': 0.8}, loc='upper left', ncol=2)
style_axes(ax)
plt.tight_layout()

OUTDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/figures/paper'
PAPDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/figures'
os.makedirs(PAPDIR, exist_ok=True)
for d, n in [(OUTDIR, 'fig7_rankme_trajectories'), (PAPDIR, 'rankme_trajectories')]:
    fig.savefig(f'{d}/{n}.pdf')
    fig.savefig(f'{d}/{n}.png')
plt.close()
print("Fig 7 done.")
