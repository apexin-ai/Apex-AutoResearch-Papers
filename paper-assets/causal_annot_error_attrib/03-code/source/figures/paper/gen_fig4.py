#!/usr/bin/env python3
"""Generate fig4_binarization: Binarization collapse delta across 6 topologies.

Narrative intent: Collapsing K=3 to binary is a dangerous shortcut —
delta varies >145x from M-bias (0.006) to IV (0.926), and sign flips
emerge in exposure + IV.

Data source: registry plan008_binarization_collapse (100k Dirichlet samples).
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# === UNIFIED PAPER COLOR PALETTE ===
COLOR_SAFE = '#154360'      # Deep navy — structural guarantee topologies
COLOR_DANGER = '#922B21'    # Deep crimson — sign-flip topologies
COLOR_NEUTRAL = '#1C2833'   # Near-black for text/axes
COLOR_GRID = '#D5D8DC'      # Light gray for grids

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 8,
    'axes.titlesize': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.8,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.5,
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'xtick.major.size': 3,
    'ytick.major.size': 3,
})

# ── Data from registry (plan008_binarization_collapse) ─────────────────
# Sorted by D_mean ascending for visual impact

data = {
    'M-bias':      {'D_mean': 0.0063, 'D_med': 0.0054, 'D_P95': 0.0147, 'D_max': 0.0328,
                    'frac_gt_001': 0.181, 'frac_gt_005': 0.0, 'sign_flip': 0.0},
    'Collider':    {'D_mean': 0.0169, 'D_med': 0.0125, 'D_P95': 0.0472, 'D_max': 0.1069,
                    'frac_gt_001': 0.572, 'frac_gt_005': 0.039, 'sign_flip': 0.0},
    'Confounding': {'D_mean': 0.0253, 'D_med': 0.0182, 'D_P95': 0.0733, 'D_max': 0.2213,
                    'frac_gt_001': 0.686, 'frac_gt_005': 0.138, 'sign_flip': 0.0},
    'Mediation':   {'D_mean': 0.0446, 'D_med': 0.0355, 'D_P95': 0.1179, 'D_max': 0.252,
                    'frac_gt_001': 0.835, 'frac_gt_005': 0.36, 'sign_flip': 0.0},
    'Exposure':    {'D_mean': 0.5164, 'D_med': 0.506, 'D_P95': 0.8453, 'D_max': 1.3876,
                    'frac_gt_001': 1.0, 'frac_gt_005': 0.999, 'sign_flip': 0.14},
    'IV':          {'D_mean': 0.926, 'D_med': 0.9394, 'D_P95': 1.3426, 'D_max': 2.0809,
                    'frac_gt_001': 1.0, 'frac_gt_005': 1.0, 'sign_flip': 0.175},
}

topos = list(data.keys())
n = len(topos)
y_pos = np.arange(n)

# Safe topologies (first 4) get deep navy, dangerous (last 2) get deep crimson
SAFE_TOPOS = {'M-bias', 'Collider', 'Confounding', 'Mediation'}

def get_color(topo):
    return COLOR_SAFE if topo in SAFE_TOPOS else COLOR_DANGER

def get_marker(topo):
    return 'o' if topo in SAFE_TOPOS else 'D'

# ── Figure: single-column width ───────────────────────────────────────
fig, ax = plt.subplots(figsize=(3.3, 2.3))

# Background bands
ax.axvspan(0.05, 2.5, color=COLOR_DANGER, alpha=0.04, zorder=0)
ax.axvspan(0, 0.05, color=COLOR_SAFE, alpha=0.04, zorder=0)
ax.axvline(x=0.05, color=COLOR_NEUTRAL, linestyle=':', linewidth=0.7, alpha=0.5, zorder=1)

for i, topo in enumerate(topos):
    d = data[topo]
    color = get_color(topo)
    marker = get_marker(topo)

    # Range bar: median to P95
    ax.plot([d['D_med'], d['D_P95']], [y_pos[i], y_pos[i]],
            color=color, linewidth=2.2, zorder=3, alpha=0.6)

    # Extend thin line to max
    ax.plot([d['D_P95'], d['D_max']], [y_pos[i], y_pos[i]],
            color=color, linewidth=0.8, zorder=3, alpha=0.35)

    # Tick marks at median and max
    tick_h = 0.18
    ax.vlines(d['D_med'], y_pos[i] - tick_h, y_pos[i] + tick_h,
              color=color, lw=1.2, zorder=3)
    ax.vlines(d['D_max'], y_pos[i] - tick_h, y_pos[i] + tick_h,
              color=color, lw=0.8, zorder=3, alpha=0.4)

    # Mean marker — circles for safe, diamonds for danger
    ax.plot(d['D_mean'], y_pos[i], marker=marker, color=color, markersize=5.5, zorder=5,
            markeredgecolor='white', markeredgewidth=0.7)

    # Numeric label — ensure clear separation from marker
    label = f"$\\bar{{\\Delta}}$={d['D_mean']:.3f}"
    if d['sign_flip'] > 0:
        label += f" [{d['sign_flip']*100:.0f}% flip]"
    text_x = max(d['D_max'] + 0.05, d['D_mean'] + 0.18)
    ax.text(text_x, y_pos[i], label,
            va='center', ha='left', fontsize=6.5, color=color, fontweight='bold')

ax.set_yticks(y_pos)
ax.set_yticklabels(topos, fontsize=8)
ax.set_xlabel(r'Binarization collapse $\Delta = |\mathrm{bias}_{K=3} - \mathrm{bias}_{K \to 2}|$', fontsize=9)
ax.set_xlim(-0.08, 2.35)
ax.invert_yaxis()

# Subtle horizontal grid
ax.grid(True, axis='x', alpha=0.10, linewidth=0.5, color=COLOR_GRID, zorder=0)

# 150x annotation — between M-bias and IV, positioned to avoid legend
ax.annotate('', xy=(0.926, 5), xytext=(0.926, 0),
            arrowprops=dict(arrowstyle='<->', color=COLOR_DANGER, alpha=0.6, lw=1.2))
ax.text(1.05, 2.5, '147×', fontsize=10, fontweight='bold', color=COLOR_DANGER,
        alpha=0.8, ha='left', va='center')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Legend — compact, inside plot
leg_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=COLOR_SAFE, markersize=6,
               markeredgecolor='white', markeredgewidth=0.6,
               label='Safe topologies'),
    plt.Line2D([0], [0], marker='D', color='w', markerfacecolor=COLOR_DANGER, markersize=6,
               markeredgecolor='white', markeredgewidth=0.6,
               label='Dangerous topologies'),
    plt.Line2D([0], [0], color=COLOR_NEUTRAL, linestyle=':', linewidth=0.8,
               label=r'$\Delta = 0.05$ threshold'),
]
ax.legend(handles=leg_elements, loc='upper center', bbox_to_anchor=(0.5, -0.22),
          ncol=3, fontsize=6.5, frameon=False, handletextpad=0.3, columnspacing=0.8)

plt.tight_layout()

# ── Save ────────────────────────────────────────────────────────────────
out_base = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fig4_binarization')
fig.savefig(f'{out_base}.pdf', bbox_inches='tight', dpi=300, pad_inches=0.03)
fig.savefig(f'{out_base}.png', bbox_inches='tight', dpi=300, pad_inches=0.03)
print(f'Saved: {out_base}.pdf and .png')
plt.close()
