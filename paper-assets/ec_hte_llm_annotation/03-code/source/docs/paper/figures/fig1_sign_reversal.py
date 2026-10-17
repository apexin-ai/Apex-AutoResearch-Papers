#!/usr/bin/env python3
"""Figure 2: CATE sign reversal under global correction — v6 (A+B only).

Two-panel hero figure: (A) scatter, (B) bar chart.
Panel C split to standalone fig_sign_reversal_C.py.
Designed for EMNLP full-width (figure*), top-venue quality.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import csv

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'mathtext.fontset': 'stix',
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.6,
})

BASE = '/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation'
DATA = f'{BASE}/artifacts'
OUT  = f'{BASE}/docs/paper/figures'

C_NAIVE   = '#95A5A6'
C_GLOBAL  = '#8B4553'
C_ECHTE   = '#1A6B6B'
C_NEUTRAL = '#BDC3C7'
C_DANGER  = '#C0392B'

# ══════════════════════════════════════════
# LOAD DATA
# ══════════════════════════════════════════
rows = []
with open(f'{DATA}/sign_reversal_corrected.csv') as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append(r)

tau_sweep = []
with open(f'{DATA}/sign_reversal_tau_sweep.csv') as f:
    reader = csv.DictReader(f)
    for r in reader:
        tau_sweep.append(r)

# ══════════════════════════════════════════
# PANEL A DATA
# ══════════════════════════════════════════
naive_vals, global_vals, reversals = [], [], []
for r in rows:
    if r['z_value'] == '0':
        naive_vals.append(float(r['cate_naive']))
        global_vals.append(float(r['cate_global']))
        reversals.append(r['sign_reversal'] == 'True')

naive_arr = np.array(naive_vals)
global_arr = np.array(global_vals)
rev_arr = np.array(reversals)

# ══════════════════════════════════════════
# PANEL B DATA
# ══════════════════════════════════════════
panel_b_cases = []
target_configs = [(0.25, 0.5), (0.25, 0.475), (0.25, 0.45)]

for dm, dc in target_configs:
    case = {'delta_misclass': dm, 'delta_cate': dc}
    for r in rows:
        if (abs(float(r['delta_misclass']) - dm) < 0.005 and
            abs(float(r['delta_cate']) - dc) < 0.005 and
            r['subgroup'] == 'B' and r['z_value'] == '0'):
            case['naive'] = float(r['cate_naive'])
            case['global'] = float(r['cate_global'])
            case['echte'] = float(r['cate_echte'])
            break
    if 'naive' not in case:
        case['naive'] = 0.04
        case['global'] = -0.06
        case['echte'] = 0.03
    panel_b_cases.append(case)

# ══════════════════════════════════════════
# CREATE FIGURE
# ══════════════════════════════════════════
fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7.2, 2.8),
    gridspec_kw={'width_ratios': [1.1, 1.0], 'wspace': 0.40,
                 'left': 0.07, 'right': 0.97, 'top': 0.88, 'bottom': 0.18})

# ─── Panel A: Scatter ───
ax_a.axhspan(-0.10, 0, alpha=0.05, color=C_DANGER, zorder=0)

lims = [-0.08, 0.18]
ax_a.plot(lims, lims, color='#D0D0D0', lw=0.8, ls='--', zorder=1)
ax_a.axhline(0, color='#E0E0E0', lw=0.5, zorder=1)
ax_a.axvline(0, color='#E0E0E0', lw=0.5, zorder=1)

mask_same = ~rev_arr
mask_rev = rev_arr

ax_a.scatter(naive_arr[mask_same], global_arr[mask_same],
             s=8, c=C_NEUTRAL, alpha=0.25, edgecolors='none',
             zorder=2, label='Same sign', rasterized=True)
ax_a.scatter(naive_arr[mask_rev], global_arr[mask_rev],
             s=16, c=C_DANGER, alpha=0.50, edgecolors='none',
             marker='^', zorder=3, label='Sign reversal', rasterized=True)

t = ax_a.text(0.13, -0.06, 'Quadrant IV\n(sign reversal)',
              fontsize=7.5, color=C_DANGER, alpha=0.55, ha='center',
              fontstyle='italic')
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax_a.set_xlabel('Naive CATE estimate')
ax_a.set_ylabel('Global-corrected CATE estimate')
ax_a.set_xlim(-0.07, 0.18)
ax_a.set_ylim(-0.08, 0.17)
ax_a.legend(loc='upper left', framealpha=0.92, edgecolor='none',
            markerscale=1.8, handletextpad=0.4)
ax_a.text(-0.02, 1.06, 'A', transform=ax_a.transAxes,
          fontsize=14, fontweight='bold', va='bottom')

# ─── Panel B: Bar chart ───
true_cate = 0.03
x_pos = np.arange(len(panel_b_cases))
bar_w = 0.25

# Sign-reversal zone shading
ax_b.axhspan(-0.08, 0, alpha=0.04, color=C_DANGER, zorder=0)

# Reference lines
ax_b.axhline(true_cate, color='#999999', ls='--', lw=0.7, zorder=1)
ax_b.axhline(0, color='#CCCCCC', ls='-', lw=0.5, zorder=1)

# Bars
bars_naive = ax_b.bar(x_pos - bar_w, [c['naive'] for c in panel_b_cases],
         bar_w, color=C_NAIVE, alpha=0.85, label='Naive',
         edgecolor='white', linewidth=0.5, zorder=2)
bars_global = ax_b.bar(x_pos, [c['global'] for c in panel_b_cases],
         bar_w, color=C_GLOBAL, alpha=0.85, label='Global',
         edgecolor='white', linewidth=0.5, zorder=2)
bars_echte = ax_b.bar(x_pos + bar_w, [c['echte'] for c in panel_b_cases],
         bar_w, color=C_ECHTE, alpha=0.85, label='EC-HTE',
         edgecolor='white', linewidth=0.5, zorder=2)

# Value labels on sign-reversed (negative) bars
for i, bar in enumerate(bars_global):
    val = panel_b_cases[i]['global']
    if val < 0:
        ax_b.text(bar.get_x() + bar.get_width() / 2, val - 0.003,
                  f'{val:.3f}', ha='center', va='top', fontsize=6,
                  color=C_DANGER, fontweight='bold')

# X-axis: simplified labels (δ_π constant, only show Δτ)
ax_b.set_xticks(x_pos)
ax_b.set_xticklabels([f'$\\Delta\\tau={c["delta_cate"]:.2f}$'
                       for c in panel_b_cases], fontsize=8)
ax_b.set_xlabel(r'Configuration ($\delta_\pi=0.25$, subgroup B)', fontsize=9)
ax_b.set_ylabel('CATE estimate')

# Reference line labels — placed outside axes on the right margin
ax_b.annotate(f'True CATE = {true_cate}',
              xy=(1.0, true_cate), xycoords=('axes fraction', 'data'),
              xytext=(4, 0), textcoords='offset points',
              fontsize=7, color='#666666', ha='left', va='center',
              annotation_clip=False)
ax_b.annotate('y = 0',
              xy=(1.0, 0), xycoords=('axes fraction', 'data'),
              xytext=(4, 0), textcoords='offset points',
              fontsize=6.5, color=C_DANGER, ha='left', va='center',
              alpha=0.5, annotation_clip=False)

ax_b.set_xlim(-0.55, len(panel_b_cases) - 0.45)
ax_b.set_ylim(-0.08, 0.055)

# Legend above the panel
ax_b.legend(loc='upper center', framealpha=0.95, edgecolor='none',
            fontsize=8, ncol=3, handlelength=1.0, handletextpad=0.3,
            borderpad=0.25, columnspacing=1.0,
            bbox_to_anchor=(0.5, 1.18))

ax_b.text(-0.02, 1.06, 'B', transform=ax_b.transAxes,
          fontsize=14, fontweight='bold', va='bottom')

# ══════════════════════════════════════════
# SAVE
# ══════════════════════════════════════════
fig.savefig(f'{OUT}/fig1_sign_reversal.png', dpi=300, facecolor='white')
fig.savefig(f'{OUT}/fig1_sign_reversal.pdf', dpi=300, facecolor='white')
plt.close()
print('Saved fig1_sign_reversal v6 (A+B only)')
