#!/usr/bin/env python3
"""Generate fig_pruning_overview: SR vs retention ratio k for 4 VLA models."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os

# ── Global style ──────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 2.0,
})

# ── Okabe-Ito palette (color-blind friendly) ─────────────────────────
C_PI05    = '#0072B2'   # blue
C_OPENVLA = '#009E73'   # green
C_XVLA   = '#E69F00'   # orange
C_SMOLVLA = '#D55E00'   # vermillion/red

# ── Data from registry (Object suite, L2norm method) ─────────────────
pi05_k  = np.array([0.3,  0.5,   0.7,  0.85,  0.9,   0.95,  1.0])
pi05_sr = np.array([51.0, 33.4,  55.0, 98.4,  98.2,  98.2,  98.2])

openvla_k  = np.array([0.3,  0.5,   0.7,   0.9,   0.95,  1.0])
openvla_sr = np.array([25.0, 39.2,  49.8,  70.6,  70.6,  74.0])

xvla_k  = np.array([0.3,  0.5,   0.7,   0.85,  0.9,   0.95,  1.0])
xvla_sr = np.array([22.2, 43.4,  58.2,  68.0,  99.2,  99.0,  99.2])

smolvla_k  = np.array([0.3, 0.5, 0.7, 0.9, 0.95, 1.0])
smolvla_sr = np.array([0.0, 0.0, 0.0, 0.0, 0.4,  57.2])

# ── Figure ────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7.2, 5.4))  # 4:3 aspect

# Pattern A: regime background bands
ax.axvspan(0.9, 1.03, alpha=0.055, color='#2E86C1', zorder=0)
ax.axvspan(0.25, 0.5, alpha=0.04, color='#E74C3C', zorder=0)

# Zone labels at top margin
ax.text(0.965, 107, 'Safe', fontsize=7.5, color='#5D6D7E',
        ha='center', va='top', fontstyle='italic', alpha=0.55)
ax.text(0.375, 107, 'Aggressive', fontsize=7.5, color='#A93226',
        ha='center', va='top', fontstyle='italic', alpha=0.55)

# Baseline dashed lines (very subtle)
for bl, color in [(98.2, C_PI05), (74.0, C_OPENVLA),
                   (99.2, C_XVLA), (57.2, C_SMOLVLA)]:
    ax.axhline(bl, color=color, linestyle=':', linewidth=0.6, alpha=0.18, zorder=1)

# ── Main curves ──────────────────────────────────────────────────────

ax.plot(pi05_k, pi05_sr, 'o-', color=C_PI05, markersize=6.5,
        markeredgecolor='white', markeredgewidth=1.0,
        label=r'$\pi$0.5 (CV = 0.055)', zorder=5)

ax.plot(openvla_k, openvla_sr, 's-', color=C_OPENVLA, markersize=6,
        markeredgecolor='white', markeredgewidth=1.0,
        label='OpenVLA (CV = 0.215)', zorder=5)

ax.plot(xvla_k, xvla_sr, '^-', color=C_XVLA, markersize=7,
        markeredgecolor='white', markeredgewidth=1.0,
        label='X-VLA (CV = 0.151)', zorder=5)

# SmolVLA — collapse treatment
ax.plot(1.0, 57.2, 'X', color=C_SMOLVLA, markersize=10, markeredgewidth=2.4, zorder=6)
ax.plot([1.0, 0.95], [57.2, 0.4], '--', color=C_SMOLVLA, linewidth=1.5,
        alpha=0.55, zorder=4)
ax.plot(smolvla_k[:-1], smolvla_sr[:-1], 'X-', color=C_SMOLVLA, markersize=7,
        markeredgewidth=1.8, linewidth=1.5, zorder=5)
ax.plot([], [], 'X-', color=C_SMOLVLA, markersize=7, markeredgewidth=1.8,
        label='SmolVLA (CV = 0.314)')

# ── Annotations ──────────────────────────────────────────────────────

# π0.5 plateau — above the curve
ax.annotate(r'$\pi$0.5: 98%+ through $k$=0.85',
            xy=(0.85, 99.5), xytext=(0.50, 106),
            fontsize=7, color=C_PI05,
            arrowprops=dict(arrowstyle='->', color=C_PI05, lw=0.7,
                            connectionstyle='arc3,rad=0.1'),
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor=C_PI05, alpha=0.9, linewidth=0.4),
            zorder=7)

# X-VLA cliff
ax.annotate('X-VLA: 99%→68% cliff',
            xy=(0.875, 83.5), xytext=(0.50, 76),
            fontsize=7, color='#B87300',
            arrowprops=dict(arrowstyle='->', color='#B87300', lw=0.7,
                            connectionstyle='arc3,rad=0.12'),
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor=C_XVLA, alpha=0.9, linewidth=0.4),
            zorder=7)

# SmolVLA collapse — centered in the empty bottom-center
t3 = ax.text(0.60, 11, 'Pixel-shuffle collapse: 0% at all $k$ < 1.0',
             fontsize=7, color=C_SMOLVLA, fontstyle='italic',
             bbox=dict(boxstyle='round,pad=0.25', facecolor='#FEF5F3',
                       edgecolor=C_SMOLVLA, alpha=0.85, linewidth=0.4),
             ha='center', zorder=7)

# π0.5 non-monotonicity (very subtle)
ax.annotate('reversal',
            xy=(0.5, 33.4), xytext=(0.44, 20),
            fontsize=6, color=C_PI05, alpha=0.55, fontstyle='italic',
            arrowprops=dict(arrowstyle='->', color=C_PI05, lw=0.5, alpha=0.3),
            zorder=6)

# ── Axes ──────────────────────────────────────────────────────────────
ax.set_xlim(0.25, 1.03)
ax.set_ylim(-3, 109)
ax.set_xlabel('Retention ratio $k$', labelpad=6)
ax.set_ylabel('Success rate (%)', labelpad=6)
ax.set_xticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

ax.grid(True, alpha=0.12, zorder=0, linewidth=0.4)
ax.set_axisbelow(True)

# Legend — upper-left, compact
leg = ax.legend(loc='upper left', bbox_to_anchor=(0.01, 0.93),
                frameon=True, fancybox=False,
                edgecolor='#D5D8DC', framealpha=0.94,
                borderpad=0.5, handlelength=1.8, labelspacing=0.35)
leg.get_frame().set_linewidth(0.5)

plt.tight_layout()

# ── Save ──────────────────────────────────────────────────────────────
outdir = os.path.dirname(os.path.abspath(__file__))
figdir = os.path.join(outdir, 'figures') if not outdir.endswith('figures') else outdir
os.makedirs(figdir, exist_ok=True)

pdf_path = os.path.join(figdir, 'fig_pruning_overview.pdf')
png_path = os.path.join(figdir, 'fig_pruning_overview.png')
plt.savefig(pdf_path)
plt.savefig(png_path)
plt.close()
print(f'Saved: {pdf_path}')
print(f'Saved: {png_path}')
