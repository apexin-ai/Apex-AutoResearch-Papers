import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

PAPER_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Unified palette (D143 color unification) ---
C_BASELINE  = '#4477AA'   # blue — Binary Reward
C_COLLAPSE  = '#EE7733'   # orange — Penalty Reward
C_NEUTRAL   = '#999999'   # gray

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

fig, ax = plt.subplots(figsize=(3.5, 2.8))

# Data (binary: 270/271 non-zero windows across 3 eval iterations)
agreement_rates = [99.6, 52.07]
bar_colors = [C_BASELINE, C_COLLAPSE]

x = np.array([0, 1])
bar_width = 0.35

bars = ax.bar(x, agreement_rates, width=bar_width, color=bar_colors,
              edgecolor='white', linewidth=0.5, zorder=3)

bars[0].set_hatch('///')
bars[0].set_edgecolor(C_BASELINE)

# 50% random chance reference line
ax.axhline(y=50, color=C_NEUTRAL, linestyle='--', linewidth=1.2, zorder=2)
ax.text(1.58, 51.5, 'random\nchance', fontsize=6.5, color=C_NEUTRAL,
        ha='left', va='bottom', linespacing=0.85)

# --- Value annotations above bars ---
# Binary: 99.6% (270/271)
ax.text(0, 109, '99.6%', ha='center', va='bottom',
        fontsize=10, fontweight='bold', color=C_BASELINE)
ax.text(0, 107, '$n$=271', ha='center', va='top',
        fontsize=7, color='#888888')

# Penalty: 52.1%
ax.text(1, 60, '52.1%', ha='center', va='bottom',
        fontsize=10, fontweight='bold', color=C_COLLAPSE)
ax.text(1, 58, '$n$=3,000', ha='center', va='top',
        fontsize=7, color='#888888')

# Zero-gradient annotation
ax.annotate('21.5% zero-gradient\nwindows excluded',
            xy=(0.18, 100), xytext=(0.85, 88),
            fontsize=6.5, color='#777777', ha='center', va='top',
            arrowprops=dict(arrowstyle='->', color='#AAAAAA', lw=0.8,
                            connectionstyle='arc3,rad=0.2',
                            shrinkA=0, shrinkB=2))

ax.set_ylabel('Sign-Episode\nAgreement Rate (%)', fontsize=9)
ax.set_xticks(x)
ax.set_xticklabels(['Binary\nReward', 'Penalty\nReward'], fontsize=9)
ax.tick_params(axis='x', pad=4)

ax.set_ylim(0, 125)
ax.set_yticks([0, 25, 50, 75, 100])
ax.set_xlim(-0.6, 1.7)

plt.tight_layout()
fig.savefig(os.path.join(PAPER_DIR, 'fig_sign_misattribution.pdf'))
fig.savefig(os.path.join(PAPER_DIR, 'fig_sign_misattribution.png'))
print('Saved fig_sign_misattribution.pdf and .png')
