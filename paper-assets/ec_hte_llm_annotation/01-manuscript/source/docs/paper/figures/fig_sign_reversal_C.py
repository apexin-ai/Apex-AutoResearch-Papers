#!/usr/bin/env python3
"""Figure: Sign reversal rate vs true CATE — standalone panel C.
Single-column figure for EMNLP, placed on page 7.
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

C_DANGER  = '#C0392B'

tau_sweep = []
with open(f'{DATA}/sign_reversal_tau_sweep.csv') as f:
    reader = csv.DictReader(f)
    for r in reader:
        tau_sweep.append(r)

tau_vals = [float(r['tau_z0']) for r in tau_sweep]
rev_rates = [float(r['pct_reversal_z0']) for r in tau_sweep]

fig, ax = plt.subplots(1, 1, figsize=(3.3, 2.2))

danger_mask = np.array(rev_rates) > 0
if any(danger_mask):
    max_tau_danger = max(t for t, r in zip(tau_vals, rev_rates) if r > 0)
    ax.axvspan(0, max_tau_danger + 0.01, alpha=0.05, color=C_DANGER, zorder=0)
    ax.text(max_tau_danger / 2 + 0.005, 1.5, 'Danger zone',
            fontsize=8, color=C_DANGER, alpha=0.35, ha='center',
            va='bottom', fontstyle='italic')

ax.plot(tau_vals, rev_rates, 'o-', color=C_DANGER, markersize=5.5,
        markerfacecolor='white', markeredgewidth=1.4,
        markeredgecolor=C_DANGER, zorder=3, label='Sign reversal rate')

ax.axhline(0, color='#E0E0E0', lw=0.4)

ax.text(0.97, 0.95,
        f'Max |bias| = 0.089\n$\\tau(0) = 0.03$',
        transform=ax.transAxes, fontsize=7, color='#777777',
        ha='right', va='top',
        bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#E0E0E0',
                  lw=0.4, alpha=0.92))

ax.set_xlabel(r'True CATE $\tau(0)$')
ax.set_ylabel('Sign reversal rate (%)')
ax.legend(loc='upper right', framealpha=0.92, edgecolor='none',
          bbox_to_anchor=(0.98, 0.72), fontsize=8)

fig.savefig(f'{OUT}/fig_sign_reversal_C.png', dpi=300, facecolor='white')
fig.savefig(f'{OUT}/fig_sign_reversal_C.pdf', dpi=300, facecolor='white')
plt.close()
print('Saved fig_sign_reversal_C')
