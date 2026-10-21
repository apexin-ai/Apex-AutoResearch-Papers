#!/usr/bin/env python3
"""Fig 5: lambda-CAR/TSR curve with null distribution band.

narrative_intent: "SDF geometric supervision is redundant across a 20x
loss weight range: all lambda values produce CAR within the null distribution band."
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path

OUT = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/'
           'diff_collision_sdf/artifacts/figures/fig5_lambda_curve')

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['STIXGeneral', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.7,
})

C_CAR = '#0072B2'
C_TSR = '#D55E00'
C_NULL = '#CCCCCC'
STROKE = [pe.withStroke(linewidth=2.5, foreground='white')]

car_mean = np.array([54.67, 54.5, 56.33, 57.0])
car_std  = np.array([2.02, 2.29, 1.61, 2.18])
seeds    = np.array([3, 3, 3, 3])
tsr_mean = np.array([51.5, 54.0, 53.83, 50.17])
car_se   = car_std / np.sqrt(seeds)

null_mu, null_sig = 54.58, 1.93

xpos = np.array([0, 1.8, 2.8, 3.8])
xlbl = ['0\n(LoRA-only)', '0.005', '0.01', '0.1']

fig, ax = plt.subplots(figsize=(4, 3.5))

ax.axhspan(null_mu - null_sig, null_mu + null_sig,
           color=C_NULL, alpha=0.3, zorder=0)
ax.axhline(null_mu, color='#BBBBBB', ls='--', lw=0.8, zorder=1)

ax.errorbar(xpos[0], car_mean[0], yerr=car_se[0],
            fmt='o', color=C_CAR, ms=6,
            capsize=3, capthick=1.0, elinewidth=1.0,
            mec='white', mew=0.6, zorder=4)
ax.errorbar(xpos[1:], car_mean[1:], yerr=car_se[1:],
            fmt='o-', color=C_CAR, ms=6, lw=1.5,
            capsize=3, capthick=1.0, elinewidth=1.0,
            mec='white', mew=0.6, zorder=4)

ax.plot(xpos[0], tsr_mean[0], 's', color=C_TSR, ms=5.5,
        mec='white', mew=0.6, alpha=0.75, zorder=3)
ax.plot(xpos[1:], tsr_mean[1:], 's--', color=C_TSR, ms=5.5,
        mec='white', mew=0.6, alpha=0.75, lw=1.2, zorder=3)

ann_cfg = [
    (12, 0, 'left'),
    (0, 7, 'center'),
    (0, 7, 'center'),
    (0, 7, 'center'),
]
for i in range(4):
    ox, oy, ha = ann_cfg[i]
    ref_y = car_mean[i] + car_se[i] if oy >= 0 else car_mean[i]
    t = ax.annotate(f'n={seeds[i]}',
                    xy=(xpos[i], ref_y),
                    xytext=(ox, oy), textcoords='offset points',
                    fontsize=7, color=C_CAR, ha=ha, style='italic')
    t.set_path_effects(STROKE)

t = ax.text(4.3, null_mu, 'null\n$\\pm$1$\\sigma$',
            fontsize=7, color='#999', ha='center', va='center',
            style='italic', linespacing=0.85)
t.set_path_effects(STROKE)

trans = ax.get_xaxis_transform()
for bx in [0.7, 0.9]:
    ax.plot([bx, bx + 0.12], [-0.04, 0.04], transform=trans,
            color='k', lw=0.6, clip_on=False)

ax.set_xticks(xpos)
ax.set_xticklabels(xlbl, fontsize=9)
ax.set_xlabel(r'$\lambda$ (SDF loss weight)', fontsize=10)
ax.set_ylabel('Rate (%)', fontsize=10)
ax.set_xlim(-0.6, 4.8)
ax.set_ylim(46, 60)

handles = [
    Line2D([0], [0], marker='o', color=C_CAR, mfc=C_CAR,
           mec='white', ms=5, lw=1.5, ls='-', label='CAR'),
    Line2D([0], [0], marker='s', color=C_TSR, mfc=C_TSR,
           mec='white', ms=4.5, lw=1.2, ls='--', label='TSR'),
]
ax.legend(handles=handles, loc='lower right', fontsize=8,
          framealpha=0.92, edgecolor='none', handlelength=1.8,
          handletextpad=0.5, borderpad=0.4, labelspacing=0.3)

plt.tight_layout()
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT.with_suffix('.pdf'))
fig.savefig(OUT.with_suffix('.png'))
plt.close(fig)
print(f'Saved: {OUT.with_suffix(".pdf")} and {OUT.with_suffix(".png")}')
