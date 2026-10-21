#!/usr/bin/env python3
"""Dose-response: OCC gradient flow steps vs CAR (v1 data).
Unified serif styling for CoRL 2026."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 10,
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'lines.linewidth': 1.8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'cm',
})

# Paper palette
COLOR_FORWARD = '#4C72B0'
COLOR_REVERSE = '#C44E52'
COLOR_VANILLA = '#999999'

# v1 data: (gradient_flow_steps_K, mean_CAR, std_CAR, n_seeds, label)
early_cutoff = [
    (15, 0.782, 0.031, 2, 'Cutoff@15K'),
    (25, 0.724, 0.051, 2, 'Cutoff@25K'),
    (35, 0.779, 0.017, 3, 'Cutoff@35K'),
    (45, 0.764, None,  1, 'Cutoff@45K'),
    (50, 0.797, 0.032, 3, 'Full OCC'),
]

reverse = (15, 0.718, 0.025, 2, 'Reverse Cutoff')
vanilla_car = 0.780
vanilla_se = 0.012

fig, ax = plt.subplots(figsize=(5.5, 3.5))

# Vanilla reference band
ax.axhspan(vanilla_car - vanilla_se, vanilla_car + vanilla_se,
           color='#E8E8E8', zorder=0)
ax.axhline(vanilla_car, color=COLOR_VANILLA, ls='--', lw=1.0, zorder=1)
ax.text(51.5, vanilla_car + 0.002, f'Vanilla ({vanilla_car:.3f})',
        fontsize=8.5, color=COLOR_VANILLA, va='bottom', ha='left',
        style='italic',
        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

# Early cutoff series
xs = [d[0] for d in early_cutoff]
ys = [d[1] for d in early_cutoff]
errs = [d[2] if d[2] is not None else 0 for d in early_cutoff]
seeds = [d[3] for d in early_cutoff]

multi_idx = [i for i, d in enumerate(early_cutoff) if d[3] >= 3]
few_idx = [i for i, d in enumerate(early_cutoff) if d[3] < 3]

# Dashed connecting line
ax.plot(xs, ys, '--', color=COLOR_FORWARD, lw=0.8, zorder=2, alpha=0.4)

# Multi-seed (3+): solid circles + solid line
mx = [xs[i] for i in multi_idx]
my = [ys[i] for i in multi_idx]
ax.plot(mx, my, 'o', color=COLOR_FORWARD, markersize=7, zorder=5,
        markeredgecolor='white', markeredgewidth=0.8,
        label=r'$n \geq 3$ seeds')

# Few-seed (<3): open circles
fx = [xs[i] for i in few_idx]
fy = [ys[i] for i in few_idx]
ax.plot(fx, fy, 'o', color=COLOR_FORWARD, markersize=7, zorder=5,
        markerfacecolor='white', markeredgewidth=1.3,
        label=r'$n \leq 2$ seeds')

for i, (x, y, e, n) in enumerate(zip(xs, ys, errs, seeds)):
    if e > 0:
        ax.errorbar(x, y, yerr=e, fmt='none', color=COLOR_FORWARD,
                    capsize=3.5, capthick=1.0, lw=1.0, zorder=3)
    offset_y = 0.010 if y >= vanilla_car else -0.015
    va = 'bottom' if offset_y > 0 else 'top'
    ax.text(x, y + offset_y, f'n={n}', fontsize=7.5,
            ha='center', va=va, color='#555555', style='italic',
            path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# Cutoff@15K annotation
ax.text(16.5, 0.782 + 0.012, '+0.2%', fontsize=8, color='#55A868',
        ha='left', va='bottom', fontweight='bold',
        path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# Reverse cutoff
rx, ry, re, rn, _ = reverse
ax.plot(rx, ry, 'D', color=COLOR_REVERSE, markersize=7.5, zorder=5,
        markeredgecolor='white', markeredgewidth=0.8,
        label='Reverse Cutoff (late 15K)')
ax.errorbar(rx, ry, yerr=re, fmt='none', color=COLOR_REVERSE,
            capsize=3.5, capthick=1.0, lw=1.0, zorder=3)
ax.text(rx, ry - 0.015, f'n={rn}', fontsize=7.5,
        ha='center', va='top', color='#555555', style='italic',
        path_effects=[pe.withStroke(linewidth=2, foreground='white')])

ax.set_xlabel('OCC gradient flow steps (K)', fontsize=11, fontweight='bold')
ax.set_ylabel('Collision Avoidance Rate (CAR)', fontsize=11, fontweight='bold')
ax.set_xticks([15, 25, 35, 45, 50])
ax.set_xticklabels(['15K', '25K', '35K', '45K', '50K\n(Full)'])
ax.set_xlim(10, 55)
ax.set_ylim(0.68, 0.84)
ax.set_yticks(np.arange(0.68, 0.85, 0.02))

ax.legend(loc='lower right', fontsize=8, framealpha=0.95,
          edgecolor='#CCCCCC', fancybox=True, borderpad=0.5)

ax.grid(True, alpha=0.08, axis='y', zorder=0)

fig.tight_layout(pad=0.5)

out_dir = Path('/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures')
fig.savefig(out_dir / 'dose_response.pdf', bbox_inches='tight', pad_inches=0.05)
fig.savefig(out_dir / 'dose_response.png', bbox_inches='tight', dpi=300, pad_inches=0.05)
print(f'Saved to {out_dir}/dose_response.pdf')
plt.close()
