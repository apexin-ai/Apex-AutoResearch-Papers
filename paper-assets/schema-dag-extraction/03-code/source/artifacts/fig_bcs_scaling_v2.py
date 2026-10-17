#!/usr/bin/env python3
"""Figure 1b: BCS-Controlled FewRel Accuracy — compact single-panel grouped bar.

L0: Matches Fig 1a styling (ACL/EMNLP IE paper)
L1: Okabe-Ito, no grid, no top/right spines, >=7pt, PDF TrueType
L2: Δ annotations with white stroke, semantic colors (blue=low-BCS/good, amber=high-BCS/bad)
L3: Pattern D (hollow vs solid for 80-pool subset), Pattern F (label offsets)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7.5,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

C_LOW  = '#66CCEE'   # Sky Blue — low BCS (better)
C_HIGH = '#CC6677'   # Soft Rose — high BCS (worse)

# --- Data (count_8, extreme-batch Low/High BCS) ---
conditions = ['16 relations\n(pilot pool)', '40 relations\n(80-relation pool)', '80 relations\n(full pool)']
low_bcs  = np.array([0.889, 0.833, 0.823])
high_bcs = np.array([0.798, 0.500, 0.510])
deltas   = low_bcs - high_bcs  # [0.091, 0.333, 0.312]

fig, ax = plt.subplots(figsize=(3.5, 2.9))

x = np.arange(len(conditions))
w = 0.30

bars_lo = ax.bar(x - w/2, low_bcs, w, color=C_LOW, edgecolor='white',
                 linewidth=0.4, zorder=2, label='Low BCS')
bars_hi = ax.bar(x + w/2, high_bcs, w, color=C_HIGH, edgecolor='white',
                 linewidth=0.4, zorder=2, label='High BCS')

# Pattern D: hatch the 40-rel bars (80-pool subset condition)
bars_lo[1].set_hatch('///')
bars_lo[1].set_edgecolor(C_LOW)
bars_hi[1].set_hatch('///')
bars_hi[1].set_edgecolor(C_HIGH)

# Δ annotations with bracket above bar pairs
for i, d in enumerate(deltas):
    bar_max = max(low_bcs[i], high_bcs[i])
    bracket_y = bar_max + 0.035
    arm_len = 0.018

    left_x = x[i] - w/2
    right_x = x[i] + w/2

    ax.plot([left_x, left_x], [bracket_y - arm_len, bracket_y],
            color='#888888', lw=0.6, solid_capstyle='butt')
    ax.plot([right_x, right_x], [bracket_y - arm_len, bracket_y],
            color='#888888', lw=0.6, solid_capstyle='butt')
    ax.plot([left_x, right_x], [bracket_y, bracket_y],
            color='#888888', lw=0.6, solid_capstyle='butt')

    ax.text(x[i], bracket_y + 0.012, f'$\\Delta$={d*100:.1f}pp',
            ha='center', va='bottom', fontsize=6.5, fontweight='bold',
            color='#555555')

ax.set_xticks(x)
ax.set_xticklabels(conditions)
ax.set_ylabel('Accuracy')
ax.set_ylim(0.0, 1.08)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.06), ncol=2,
          framealpha=0.95, edgecolor='none', handlelength=1.2)

plt.tight_layout(pad=0.3)
outdir = os.environ.get('FIG_OUTDIR',
    '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper')
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, 'fig_bcs_scaling.pdf')
fig.savefig(outpath, format='pdf')
fig.savefig(outpath.replace('.pdf', '.png'), format='png', dpi=300)
print(f'Saved: {outpath}')
plt.close()
