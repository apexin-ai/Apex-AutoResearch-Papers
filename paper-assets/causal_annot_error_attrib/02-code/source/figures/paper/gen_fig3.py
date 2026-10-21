#!/usr/bin/env python3
"""Generate fig3_asv_ranking: Forest-plot comparison of ASV sensitivity rankings.

Two-panel layout: Magnitude ASV | Significance Power.
Stats table moved to LaTeX (Table in experiments.tex).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os
import shutil

# === UNIFIED PAPER COLOR PALETTE ===
COLOR_SAFE = '#154360'      # Deep navy — structural guarantee topologies
COLOR_DANGER = '#922B21'    # Deep crimson — sign-flip topologies

TOPOLOGY_COLORS = {
    'confounding': '#1B4F72',   # Royal navy
    'exposure': '#C0392B',      # Vermillion red
    'mediation': '#117A65',     # Dark emerald teal
    'front_door': '#6C3483',    # Deep purple
    'collider': '#1A5276',      # Petrol blue
    'm_bias': '#2E4053',        # Dark slate
    'iv': '#922B21',            # Dark crimson
}

COLOR_NEUTRAL = '#1C2833'    # Near-black for text/axes
COLOR_GRID = '#D5D8DC'       # Light gray for grids
COLOR_ACCENT = '#B7950B'     # Burnished gold (sparing use)

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 11,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
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

# ── Per-topology color mapping ────────────────────────────────────────────
TOPO_COLOR_MAP = {
    'IV':          TOPOLOGY_COLORS['iv'],
    'Exposure':    TOPOLOGY_COLORS['exposure'],
    'Front-door':  TOPOLOGY_COLORS['front_door'],
    'Confounding': TOPOLOGY_COLORS['confounding'],
    'Mediation':   TOPOLOGY_COLORS['mediation'],
    'Collider':    TOPOLOGY_COLORS['collider'],
    'M-bias':      TOPOLOGY_COLORS['m_bias'],
}

C_TEXT     = '#1C2833'
C_TEXT_SEC = '#555555'
C_TEXT_DIM = '#999999'
C_ROW_ALT = '#F4F6F7'  # very light gray alternating rows
C_SPINE    = '#666666'

# ── Data ──────────────────────────────────────────────────────────────────
topologies = [
    'IV', 'Exposure', 'Front-door', 'Confounding',
    'Mediation', 'Collider', 'M-bias',
]
N = len(topologies)

# Separator: after index 1 (Exposure), draw a thin line separating fragile from safe
SEPARATOR_AFTER = 1  # after "Exposure" (index 1)

mag_asv = {
    'IV':          (0.101, 0.607),
    'Front-door':  (0.064, 0.387),
    'Exposure':    None,
    'Confounding': (0.081, 0.487),
    'Mediation':   (0.076, 0.454),
    'Collider':    (0.338, 2.028),
    'M-bias':      'inf',
}

sig_power = {
    'IV':          0,
    'Front-door':  100,
    'Exposure':    None,
    'Confounding': 100,
    'Mediation':   0,
    'Collider':    0,
    'M-bias':      98,
}

sig_note = {
    'Mediation': 'attenuating',
    'Collider':  'attenuating',
    'IV':        'Wald underpowered',
}

# ══════════════════════════════════════════════════════════════════════════
#  BUILD FIGURE
# ══════════════════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(7.0, 3.8))
gs = fig.add_gridspec(1, 2, width_ratios=[3, 2], wspace=0.12)

ax_mag = fig.add_subplot(gs[0])
ax_sig = fig.add_subplot(gs[1])

ROW_H = 0.42

for ax in (ax_mag, ax_sig):
    ax.set_ylim(N - 0.5 + 0.1, -0.6)
    # Alternating row backgrounds
    for i in range(N):
        if i % 2 == 0:
            ax.axhspan(i - ROW_H, i + ROW_H, color=C_ROW_ALT, zorder=0, lw=0)
    # Separator line between fragile and safe topologies
    sep_y = SEPARATOR_AFTER + 0.5
    ax.axhline(sep_y, color='#AAAAAA', lw=1.0, ls='-', zorder=1, alpha=0.6)
    # Light horizontal grid on y-axis only
    ax.grid(True, axis='x', alpha=0.10, color=COLOR_GRID, linewidth=0.4, zorder=0)
    # Spine styling
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color(C_SPINE)
    ax.spines['bottom'].set_linewidth(0.8)
    ax.tick_params(axis='y', length=0)
    ax.tick_params(axis='x', colors=C_SPINE, labelsize=8)

# ── Panel 1: Magnitude ASV ────────────────────────────────────────────────
for i, t in enumerate(topologies):
    v = mag_asv[t]
    color = TOPO_COLOR_MAP[t]
    if v is None:
        ax_mag.text(0.8, i, 'N/A (non-differential)',
                    fontsize=8, color=C_TEXT_DIM,
                    ha='center', va='center', fontstyle='italic')
    elif v == 'inf':
        # Arrow to infinity for M-bias
        ax_mag.annotate(
            '', xy=(2.45, i), xytext=(1.5, i),
            arrowprops=dict(arrowstyle='-|>', color=color, lw=2.2,
                            mutation_scale=14))
        ax_mag.text(2.55, i, '∞', fontsize=14, color=color,
                    ha='left', va='center', fontweight='bold')
    else:
        lo, hi = v
        mid = (lo + hi) / 2
        # Range bar with rounded caps
        ax_mag.plot([lo, hi], [i, i], color=color, lw=2.8,
                    solid_capstyle='round', zorder=2, alpha=0.5)
        # Central marker: filled circle with white edge
        ax_mag.plot(mid, i, 'o', color=color, ms=8, zorder=3,
                    mec='white', mew=1.2)
        # End caps
        ax_mag.plot(lo, i, '|', color=color, ms=6, mew=1.2, zorder=3)
        ax_mag.plot(hi, i, '|', color=color, ms=6, mew=1.2, zorder=3)

ax_mag.set_xlim(-0.02, 2.8)
ax_mag.set_xlabel('ASV value  (lower → more fragile)', fontsize=9,
                  color=C_TEXT_SEC, labelpad=6)
ax_mag.set_title('Magnitude ASV', fontweight='normal', color=COLOR_NEUTRAL,
                 loc='left', pad=10, fontsize=10)
ax_mag.set_yticks(range(N))
ax_mag.set_yticklabels(topologies, fontsize=10, fontweight='medium',
                       color=C_TEXT)

# Style special labels
for lbl in ax_mag.get_yticklabels():
    txt = lbl.get_text()
    if txt == 'Exposure':
        lbl.set_fontstyle('italic')
        lbl.set_color('#aaaaaa')

# ── Panel 2: Significance Power ───────────────────────────────────────────
for i, t in enumerate(topologies):
    v = sig_power[t]
    color = TOPO_COLOR_MAP[t]
    if v is None:
        ax_sig.text(50, i, 'N/A', fontsize=8, color=C_TEXT_DIM,
                    ha='center', va='center', fontstyle='italic')
    else:
        # Connecting line from 0 to value
        ax_sig.plot([0, v], [i, i], color=color, lw=1.5, alpha=0.4,
                    solid_capstyle='round', zorder=2)
        # Marker: filled circle with white edge
        ax_sig.plot(v, i, 'o', color=color, ms=8, zorder=3,
                    mec='white', mew=1.2)
        # Annotation notes
        if t in sig_note:
            offset_x = 6 if v < 50 else 5
            txt = ax_sig.text(
                v + offset_x, i, sig_note[t], fontsize=7.5,
                color=C_TEXT_SEC, fontstyle='italic', va='center',
                ha='left')
            txt.set_path_effects([
                pe.withStroke(linewidth=3.0, foreground='white')])

ax_sig.set_xlim(-5, 115)
ax_sig.set_xlabel('Power (%)', fontsize=9, color=C_TEXT_SEC, labelpad=6)
ax_sig.set_title('Significance Power', fontweight='normal', color=COLOR_NEUTRAL,
                 loc='left', pad=10, fontsize=10)
ax_sig.set_yticks(range(N))
ax_sig.set_yticklabels([])

# ── Legend ─────────────────────────────────────────────────────────────────
handles = [
    plt.Line2D([0], [0], marker='o', color=COLOR_SAFE, ls='-', lw=2.2,
               ms=7, mec='white', mew=1.0, alpha=0.55,
               label='Safe topologies (magnitude range)'),
    plt.Line2D([0], [0], marker='o', color=COLOR_DANGER, ls='-', lw=1.3,
               ms=7, mec='white', mew=1.0, alpha=0.55,
               label='Dangerous topologies'),
]
legend = fig.legend(
    handles=handles, loc='lower center', ncol=2,
    bbox_to_anchor=(0.5, -0.04), frameon=True, fontsize=8,
    handletextpad=0.5, columnspacing=1.8,
    fancybox=True,
)
legend.get_frame().set_facecolor('white')
legend.get_frame().set_edgecolor('#cccccc')
legend.get_frame().set_alpha(0.95)
legend.get_frame().set_linewidth(0.5)

fig.subplots_adjust(left=0.12, right=0.97, top=0.87, bottom=0.22, wspace=0.12)

# ── Save ──────────────────────────────────────────────────────────────────
outdir = os.path.dirname(os.path.abspath(__file__))
base = os.path.join(outdir, 'fig3_asv_ranking')
fig.savefig(f'{base}.pdf')
fig.savefig(f'{base}.png', dpi=300)
plt.close()
print(f'Saved: {base}.pdf')
print(f'Saved: {base}.png')

# Copy to docs/paper/
docs_dir = os.path.join(outdir, '..', '..', 'docs', 'paper')
if os.path.isdir(docs_dir):
    shutil.copy2(f'{base}.pdf', os.path.join(docs_dir, 'fig3_asv_ranking.pdf'))
    shutil.copy2(f'{base}.png', os.path.join(docs_dir, 'fig3_asv_ranking.png'))
    print(f'Copied to: {os.path.abspath(docs_dir)}/')
else:
    print(f'Warning: docs/paper/ directory not found at {docs_dir}')
