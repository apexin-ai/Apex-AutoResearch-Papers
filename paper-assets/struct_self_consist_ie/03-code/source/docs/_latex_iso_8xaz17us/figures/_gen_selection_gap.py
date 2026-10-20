#!/usr/bin/env python3
"""Generate fig_selection_gap: 2-panel vertical (rho bars + delta-F1 dots)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'mathtext.fontset': 'dejavusans',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

FIG_DIR = Path(__file__).parent

signal_labels = ['SJ', 'FK', 'EM', 'VC', 'LP']
rho_vals = np.array([0.359, 0.266, 0.294, 0.379, 0.205])
delta_f1 = np.array([-0.45, -0.46, -1.19, -2.65, +0.04])
oracle_delta = 13.0
random_delta = -3.9

COL_BAR = '#CC6677'
COL_BAR_EDGE = '#99445A'
COL_DOT = '#3C3C3C'
COL_ORACLE = '#228833'
COL_RANDOM = '#999999'

x = np.arange(len(signal_labels))

fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(3.4, 3.6),
    gridspec_kw={'height_ratios': [1, 1.4], 'hspace': 0.10},
    sharex=True,
)
fig.patch.set_facecolor('#FAFAFA')

def style_ax(ax):
    ax.set_facecolor('#F5F7FA')
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_color('#CCCCCC')
        ax.spines[spine].set_linewidth(0.8)
    ax.tick_params(colors='#555555', which='both')
    ax.set_axisbelow(True)

# ---- Top panel: Spearman rho bars ----
style_ax(ax1)

bars = ax1.bar(x, rho_vals, width=0.50, color=COL_BAR, alpha=0.82,
               edgecolor=COL_BAR_EDGE, linewidth=0.7, zorder=2)

for xi, rv in zip(x, rho_vals):
    ax1.text(xi, rv + 0.012, f'.{int(rv*1000):03d}', ha='center', va='bottom',
             fontsize=7.5, color=COL_BAR_EDGE, fontweight='medium')

ax1.set_ylabel(r'Spearman $\rho$', labelpad=4)
ax1.set_ylim(0, 0.47)
ax1.set_yticks([0, 0.1, 0.2, 0.3, 0.4])
ax1.grid(axis='y', alpha=0.15, linewidth=0.5, color='#888888', zorder=0)
ax1.tick_params(axis='x', length=0)
ax1.set_title('SciERC NER, $N{=}8$, $T{=}1.0$', fontsize=10, pad=6)

# ---- Bottom panel: delta-F1 dots + line ----
style_ax(ax2)

ax2.plot(x, delta_f1, 'o-', color=COL_DOT, markersize=5.5,
         markerfacecolor=COL_DOT, markeredgecolor='white',
         markeredgewidth=0.8, linewidth=1.2, zorder=3)

for xi, d in zip(x, delta_f1):
    oy = 6 if d >= 0 else -8
    va = 'bottom' if d >= 0 else 'top'
    ax2.annotate(f'{d:+.2f}', xy=(xi, d), xytext=(0, oy),
                 textcoords='offset points', ha='center', va=va,
                 fontsize=7, color=COL_DOT)

# Greedy = 0 line with pill label
ax2.axhline(y=0, color='#888888', linestyle='-', linewidth=0.7, zorder=1)
ax2.text(4.35, 0.12, 'Greedy', fontsize=6.5, color='#6C757D',
         ha='right', va='bottom', fontstyle='italic',
         bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                   edgecolor='#CCCCCC', linewidth=0.5, alpha=0.9))

# Random baseline with pill label
ax2.axhline(y=random_delta, color=COL_RANDOM, linestyle=':', linewidth=0.8,
            alpha=0.5, zorder=1)
ax2.text(4.35, random_delta + 0.12, 'Random', fontsize=6.5, color='#6C757D',
         ha='right', va='bottom', fontstyle='italic',
         bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                   edgecolor='#CCCCCC', linewidth=0.5, alpha=0.9))

# Oracle headroom annotation
ax2.annotate(
    f'Oracle: +{oracle_delta:.1f} pp', xy=(4.15, 1.45),
    fontsize=7.5, color=COL_ORACLE, ha='right', va='bottom',
    bbox=dict(boxstyle='round,pad=0.3', facecolor='#eaf5ea',
              edgecolor=COL_ORACLE, linewidth=0.6, alpha=0.95),
)

ax2.set_ylabel(r'$\Delta$F1 vs Greedy (pp)', labelpad=4)
ax2.set_ylim(-4.8, 1.8)
ax2.set_xticks(x)
ax2.set_xticklabels(signal_labels)
ax2.grid(axis='y', alpha=0.15, linewidth=0.5, color='#888888', zorder=0)

fig.savefig(FIG_DIR / 'fig_selection_gap.pdf', format='pdf')
fig.savefig(FIG_DIR / 'fig_selection_gap.png', format='png')
plt.close(fig)
print('Done: fig_selection_gap')
