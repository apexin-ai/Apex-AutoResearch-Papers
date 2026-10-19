import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

PAPER_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Project palette (Okabe-Ito, colorblind-safe) ---
C_BASELINE  = '#0072B2'   # blue
C_TREATMENT = '#E69F00'   # orange
C_COLLAPSE  = '#D55E00'   # vermillion
C_SAFE      = '#009E73'   # green
C_NEUTRAL   = '#999999'   # gray
C_SKY       = '#56B4E9'   # sky blue

# --- Unified rcParams ---
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'dejavuserif',
})

fig, ax = plt.subplots(figsize=(3.4, 2.4))

p = np.linspace(0.001, 0.5, 1000)

# K=4 (secondary), K=8 (primary), K=16 (secondary)
curves = [
    (4,  C_SKY,     '-', 1.2, '$K$=4'),
    (8,  C_COLLAPSE, '-', 2.0, '$K$=8'),
    (16, C_SAFE,    '-', 1.2, '$K$=16'),
]

for K, color, ls, lw, label in curves:
    P_correct = p / (1 - (1 - p)**K)
    ax.plot(p * 100, P_correct * 100, color=color, linestyle=ls,
            linewidth=lw, label=label, zorder=3)

# Large-K limit diagonal: P_correct = p
ax.plot(p * 100, p * 100, color=C_NEUTRAL, linestyle='--', linewidth=1.0,
        label='$K{\\to}\\infty$', zorder=2)

# Random chance line at 50%
ax.axhline(y=50, color='#CCCCCC', linestyle=':', linewidth=0.7, zorder=1)
ax.text(48, 52, 'random chance', fontsize=6.5, color='#AAAAAA', ha='right', va='bottom')

# Shaded region: typical agent task range (p < 20%)
ax.axvspan(0, 20, alpha=0.06, color=C_BASELINE, zorder=0)
ax.text(10, 97, 'typical agent\ntask range', fontsize=6.5, color='#88AACC',
        ha='center', va='top', style='italic')

# ALFWorld point: p=12.5%, K=8
p_alf = 0.125
K8 = 8
P_correct_alf = p_alf / (1 - (1 - p_alf)**K8) * 100

# Marker
ax.plot(12.5, P_correct_alf, 'o', color=C_COLLAPSE, markersize=5.5, zorder=5,
        markeredgecolor='white', markeredgewidth=1.0)

# Elegant annotation with thin connector
# Paper text says 19.1%, use that for consistency
ax.annotate('19.1%\n($p$=12.5%, $K$=8)',
            xy=(12.5, P_correct_alf),
            xytext=(25, 70),
            fontsize=7.5, ha='left', va='center', color=C_COLLAPSE,
            arrowprops=dict(arrowstyle='->', color=C_COLLAPSE, lw=0.8,
                            connectionstyle='arc3,rad=-0.2',
                            shrinkA=0, shrinkB=3))

ax.set_xlabel('Episode success rate $p$ (%)')
ax.set_ylabel('$P(\\mathrm{correct\\ sign} \\mid \\mathrm{update})$ (%)')
ax.set_xlim(0, 50)
ax.set_ylim(0, 100)

# Extremely subtle grid
ax.grid(True, alpha=0.08, linewidth=0.4, color='#CCCCCC')

ax.legend(fontsize=7, loc='lower right', framealpha=0.9, edgecolor='#DDDDDD',
          borderpad=0.4, labelspacing=0.35, handlelength=1.5, fancybox=False)

plt.tight_layout(pad=0.5)
plt.savefig(os.path.join(PAPER_DIR, 'fig_theory_curve.pdf'), bbox_inches='tight', pad_inches=0.3, dpi=300)
plt.savefig(os.path.join(PAPER_DIR, 'fig_theory_curve.png'), bbox_inches='tight', pad_inches=0.3, dpi=300)
print(f'Saved fig_theory_curve.pdf and .png  (ALFWorld point: {P_correct_alf:.1f}%)')
