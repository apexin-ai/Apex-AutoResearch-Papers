import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

GREEN = '#009E73'
RED = '#D55E00'
BLUE = '#0072B2'
GRAY = '#999999'

fig, ax = plt.subplots(figsize=(3.5, 4.0), dpi=300)
ax.set_xlim(0, 3.5)
ax.set_ylim(0, 4.0)
ax.axis('off')

# --- Top: Document + Triple ---
ax.text(1.75, 3.82, 'Document:', fontsize=8.5, fontweight='bold', ha='center', va='top', color='#333333')
ax.text(1.75, 3.67, '[S0] John was born in London.  [S1] John studied at Oxford. ...',
        fontsize=7, ha='center', va='top', color='#444444', style='italic')

ax.text(1.75, 3.45, 'Triple:', fontsize=8.5, fontweight='bold', ha='center', va='top', color='#333333')
ax.text(1.75, 3.30, '(John,  place_of_birth,  London)',
        fontsize=7.5, ha='center', va='top', color='#444444', family='monospace')

# --- Positive Pair Box (left) ---
pos_box = FancyBboxPatch((0.05, 2.05), 1.55, 1.05,
                         boxstyle="round,pad=0.06", linewidth=1.2,
                         edgecolor=GREEN, facecolor='#f0faf5')
ax.add_patch(pos_box)
ax.text(0.82, 2.95, 'Positive Pair', fontsize=8, fontweight='bold',
        ha='center', va='center', color=GREEN)
ax.text(0.82, 2.72, 'Premise (evidence):', fontsize=6.5, ha='center', va='center', color=GRAY)
ax.text(0.82, 2.55, '[S0] "John was born\nin London"', fontsize=6.8, ha='center', va='center', color='#333333')
ax.text(0.82, 2.28, 'Hypothesis:', fontsize=6.5, ha='center', va='center', color=GRAY)
ax.text(0.82, 2.13, '"John has place_of_birth\nwith London"', fontsize=6.8, ha='center', va='center', color='#333333')

# --- Negative Pair Box (right) ---
neg_box = FancyBboxPatch((1.90, 2.05), 1.55, 1.05,
                         boxstyle="round,pad=0.06", linewidth=1.2,
                         edgecolor=RED, facecolor='#fdf5f2')
ax.add_patch(neg_box)
ax.text(2.67, 2.95, 'Negative Pair', fontsize=8, fontweight='bold',
        ha='center', va='center', color=RED)
ax.text(2.67, 2.72, 'Premise (distractor):', fontsize=6.5, ha='center', va='center', color=GRAY)
ax.text(2.67, 2.55, '[S1] "John studied\nat Oxford"', fontsize=6.8, ha='center', va='center', color='#333333')
ax.text(2.67, 2.28, 'Hypothesis:', fontsize=6.5, ha='center', va='center', color=GRAY)
ax.text(2.67, 2.13, '"John has place_of_birth\nwith London"', fontsize=6.8, ha='center', va='center', color='#333333')

# --- NLI Model Box (center) ---
nli_box = FancyBboxPatch((1.05, 1.35), 1.40, 0.45,
                         boxstyle="round,pad=0.06", linewidth=1.0,
                         edgecolor=BLUE, facecolor=BLUE)
ax.add_patch(nli_box)
ax.text(1.75, 1.575, 'NLI Model', fontsize=9, fontweight='bold',
        ha='center', va='center', color='white')

# --- Arrows from boxes to NLI ---
arrow_style = "Simple,tail_width=0.4,head_width=3,head_length=2.5"
ax.annotate("", xy=(1.30, 1.80), xytext=(0.82, 2.05),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.2,
                           connectionstyle="arc3,rad=-0.1"))
ax.annotate("", xy=(2.20, 1.80), xytext=(2.67, 2.05),
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.2,
                           connectionstyle="arc3,rad=0.1"))

# --- Scores below NLI ---
ax.text(0.82, 1.10, r'$p^+ = 0.92$', fontsize=9.5, fontweight='bold',
        ha='center', va='center', color=GREEN)
ax.text(2.67, 1.10, r'$p^- = 0.31$', fontsize=9.5, fontweight='bold',
        ha='center', va='center', color=RED)

# arrows from NLI to scores
ax.annotate("", xy=(0.82, 1.22), xytext=(1.30, 1.35),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.0,
                           connectionstyle="arc3,rad=0.1"))
ax.annotate("", xy=(2.67, 1.22), xytext=(2.20, 1.35),
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.0,
                           connectionstyle="arc3,rad=-0.1"))

# --- CED Score at bottom ---
ax.plot([0.3, 3.2], [0.78, 0.78], color=GRAY, linewidth=0.5, linestyle='--', alpha=0.5)

ax.text(1.75, 0.55, r'$\mathrm{CED} = p^+ - \max(p^-) = 0.92 - 0.31$',
        fontsize=8.5, ha='center', va='center', color='#333333')
ax.text(1.75, 0.25, r'$= \mathbf{0.61}$',
        fontsize=11, ha='center', va='center', color=BLUE, fontweight='bold')

# --- Save ---
out_dir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(out_dir, 'fig_ced_scoring.pdf'))
fig.savefig(os.path.join(out_dir, 'fig_ced_scoring.png'))
plt.close()
print("Saved fig_ced_scoring.pdf and fig_ced_scoring.png")
