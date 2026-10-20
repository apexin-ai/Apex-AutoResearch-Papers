#!/usr/bin/env python3
"""Fig: Selection gap single panel — NER-only, dual Y-axis (rho + delta F1)."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],
    'font.size': 9,
    'axes.labelsize': 9,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'text.usetex': False,
})

FIG_DIR = Path('/root/autodl-tmp/struct_self_consist_ie/output/figures')
PAPER_FIG = Path('/root/autodl-tmp/struct_self_consist_ie/docs/paper/figures')
FIG_DIR.mkdir(parents=True, exist_ok=True)
PAPER_FIG.mkdir(parents=True, exist_ok=True)

# --- Data: SciERC NER, N=8, T=1.0 ---
signals = ['SJ', 'FK', 'EM', 'VC', 'LP']

# Spearman rho: analysis_unified_rho_full.json → qwen_scierc_n8_seed42 (unified gold-filtered, n=529)
rho = np.array([0.3599, 0.2665, 0.2945, 0.3792, 0.2052])

# Delta F1 vs greedy (pp): analysis_multiseed_selection_f1.json (3 seeds)
delta_f1 = np.array([-0.451, -0.457, -1.193, -2.646, +0.040])
delta_std = np.array([1.026, 0.966, 0.734, 0.877, 0.500])

# Baselines
greedy_mean = 0.64583
oracle_mean = 0.77637
random_mean = 0.60688
oracle_delta = (oracle_mean - greedy_mean) * 100
random_delta = (random_mean - greedy_mean) * 100

# --- Plot ---
fig, ax1 = plt.subplots(figsize=(4.5, 2.8))
x = np.arange(len(signals))
width = 0.5

# Left axis: Spearman rho (blue bars)
bar_color = '#4c72b0'
bars = ax1.bar(x, rho, width, color=bar_color, alpha=0.75,
               edgecolor='white', linewidth=0.5, zorder=2)
ax1.set_ylabel(r'Spearman $\rho$', color=bar_color, fontsize=9)
ax1.tick_params(axis='y', labelcolor=bar_color, labelsize=7)
ax1.set_ylim(0, 0.48)
ax1.set_xticks(x)
ax1.set_xticklabels(signals, fontsize=8)

# Bar value labels
for i, r in enumerate(rho):
    ax1.text(i, r + 0.010, f'.{int(r*1000):03d}', ha='center', va='bottom',
             fontsize=6.5, color=bar_color, fontweight='bold')

# Right axis: Delta F1 (red line + error bars)
ax2 = ax1.twinx()
line_color = '#c44e52'
ax2.errorbar(x, delta_f1, yerr=delta_std, fmt='o-', color=line_color,
             markersize=4.5, capsize=3, linewidth=1.2, elinewidth=0.8,
             markeredgecolor='white', markeredgewidth=0.5, zorder=3)
ax2.set_ylabel(r'$\Delta$F1 vs Greedy (pp)', color=line_color, fontsize=9)
ax2.tick_params(axis='y', labelcolor=line_color, labelsize=7)
ax2.set_ylim(-6.5, 16)

# Zero line
ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.4, alpha=0.4, zorder=1)

# Oracle dashed line + label
ax2.axhline(y=oracle_delta, color='#2ca02c', linestyle='--', linewidth=0.8, alpha=0.6, zorder=1)
ax2.text(len(signals)-1, oracle_delta + 0.5, f'Oracle +{oracle_delta:.1f}',
         fontsize=6, color='#2ca02c', ha='right', va='bottom',
         bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='#2ca02c',
                   alpha=0.85, linewidth=0.5))

# Random dotted line + label
ax2.axhline(y=random_delta, color='gray', linestyle=':', linewidth=0.8, alpha=0.6, zorder=1)
ax2.text(0.02, random_delta - 0.3, f'Random {random_delta:.1f}',
         fontsize=6, color='gray', ha='left', va='top',
         transform=ax2.get_yaxis_transform(),
         bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='gray',
                   alpha=0.85, linewidth=0.5))

# Delta value labels
for i, (d, s) in enumerate(zip(delta_f1, delta_std)):
    if i == 3:  # VC: place above to avoid random overlap
        y_off = d + s + 0.3
        va = 'bottom'
    else:
        y_off = d - s - 0.4
        va = 'top'
    ax2.text(i, y_off, f'{d:+.2f}', ha='center', va=va,
             fontsize=6, color=line_color, fontweight='bold')

# Grid
ax1.grid(axis='y', alpha=0.15, linewidth=0.3)
ax1.set_axisbelow(True)

# Legend
legend_elements = [
    Patch(facecolor=bar_color, alpha=0.75, edgecolor='white', label=r'Spearman $\rho$'),
    Line2D([0], [0], color=line_color, marker='o', markersize=4, linewidth=1.2,
           markeredgecolor='white', markeredgewidth=0.5, label=r'$\Delta$F1 vs Greedy (pp)')
]
ax1.legend(handles=legend_elements, loc='upper center', fontsize=6.5,
           framealpha=0.9, edgecolor='#cccccc', ncol=2,
           bbox_to_anchor=(0.5, 1.0))

ax1.set_title('SciERC NER, N=8, T=1.0', fontsize=8.5, fontweight='bold', pad=12)

fig.tight_layout()
for path in [FIG_DIR, PAPER_FIG]:
    fig.savefig(path / 'fig_selection_gap.pdf', format='pdf')
    fig.savefig(path / 'fig_selection_gap.png', format='png', dpi=300)
plt.close(fig)

print("=== Data ===")
for i, sig in enumerate(signals):
    print(f"  {sig}: rho={rho[i]:.4f}, delta={delta_f1[i]:+.3f} +/- {delta_std[i]:.3f} pp")
print(f"  Oracle: +{oracle_delta:.2f} pp | Random: {random_delta:.2f} pp")
print(f"Saved to {FIG_DIR} and {PAPER_FIG}")
