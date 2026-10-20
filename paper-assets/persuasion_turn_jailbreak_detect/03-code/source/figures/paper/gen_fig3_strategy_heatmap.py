import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 8,
    'axes.titlesize': 9,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': False,
    'axes.spines.bottom': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# 9 strategies as shown in the original figure
strategy_names = [
    'None', 'Rapport', 'Authority', 'Emotion',
    'Logic', 'Role', 'Escalation', 'Obfusc.', 'Direct'
]
n = 9

# ============================================================
# Data extracted from the original figure image
# fig3_strategy_heatmap_p1.png
# ============================================================

# Crescendo (n=1818 transitions)
# Dense matrix with many transitions; Role->Role = 545 is dominant
crescendo = np.array([
    # None  Rap   Auth  Emo   Log   Role  Esc   Obf   Dir
    [  0,   62,   31,   32,   31,    0,    0,    0,   31],  # None
    [ 32,   90,   64,   31,    0,    0,    0,    0,    0],  # Rapport
    [ 43,   51,   63,    0,    0,    0,    0,    0,    0],  # Authority
    [  0,    0,    0,   52,   62,   31,    0,    0,    0],  # Emotion
    [  0,    0,    0,    0,   95,   26,   32,    0,    0],  # Logic
    [  0,    0,    0,    0,    0,  545,   58,    0,    0],  # Role
    [ 33,    0,    0,    0,    0,    0,   50,   65,    0],  # Escalation
    [  0,    0,    0,    0,    0,    0,    0,   28,  113],  # Obfuscation
    [  0,    0,    0,    0,    0,    0,    0,    0,    0],  # Direct
], dtype=float)

# FITD (n=541 transitions)
# Sparser - only a few strategy pairs active
fitd = np.zeros((n, n), dtype=float)
fitd[0, 3] = 80   # None->Emotion
fitd[0, 5] = 80   # None->Role
fitd[1, 5] = 80   # Rapport->Role
fitd[3, 6] = 80   # Emotion->Escalation
fitd[5, 0] = 90   # Role->None
fitd[5, 4] = 161  # Role->Logic

# Deceptive Delight (n=565 transitions)
dd = np.zeros((n, n), dtype=float)
dd[0, 5] = 80     # None->Role
dd[3, 5] = 129    # Emotion->Role
dd[4, 6] = 20     # Logic->Escalation
dd[6, 3] = 60     # Escalation->Emotion
dd[6, 4] = 36     # Escalation->Logic
dd[6, 5] = 80     # Escalation->Role
dd[6, 6] = 80     # Escalation->Escalation

matrices = [crescendo, fitd, dd]
titles = [
    'Crescendo (n=1,818)',
    'FITD (n=541)',
    'Deceptive Delight (n=565)',
]

# ============================================================
# Figure setup
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(15.5, 5.2),
                         gridspec_kw={'width_ratios': [1, 1, 1]})
fig.subplots_adjust(wspace=0.30, right=0.90)

global_max = max(m.max() for m in matrices)
norm = mcolors.PowerNorm(gamma=0.45, vmin=0, vmax=global_max)

# Custom sequential colormap: ivory -> warm peach -> burnt sienna -> deep burgundy
cmap_colors = [
    '#FFFDF7',  # warm ivory (background/zero)
    '#FFF0D4',  # light gold
    '#FDCB6E',  # warm amber
    '#E17055',  # coral/burnt sienna
    '#D63031',  # bright red
    '#6C1D3F',  # deep burgundy
]
cmap = LinearSegmentedColormap.from_list('warm_seq', cmap_colors, N=256)

for idx, (mat, title) in enumerate(zip(matrices, titles)):
    ax = axes[idx]

    # Masked array: mask zeros so they appear as background
    mat_masked = np.ma.masked_where(mat == 0, mat)
    cmap_copy = cmap.copy()
    cmap_copy.set_bad(color='#FAFAFA')  # very light gray for zero cells

    im = ax.imshow(mat_masked, cmap=cmap_copy, norm=norm, aspect='equal',
                   interpolation='nearest')

    # Cell annotations
    for i in range(n):
        for j in range(n):
            val = int(mat[i, j])
            if val > 0:
                bg_intensity = norm(val)
                color = 'white' if bg_intensity > 0.50 else '#444444'
                fw = 'bold' if val >= 100 else 'medium'
                fs = 7.5 if val >= 100 else 6.5
                ax.text(j, i, str(val), ha='center', va='center',
                        fontsize=fs, color=color, fontweight=fw)

    # Diagonal highlight with dashed borders
    for k in range(n):
        rect = Rectangle((k - 0.5, k - 0.5), 1, 1,
                          linewidth=0.8, edgecolor='#888888',
                          facecolor='none', linestyle=(0, (4, 3)),
                          zorder=3)
        ax.add_patch(rect)

    # Thin grid lines
    for k in range(n + 1):
        ax.axhline(k - 0.5, color='white', linewidth=0.6, zorder=2)
        ax.axvline(k - 0.5, color='white', linewidth=0.6, zorder=2)

    # Outer border
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(0.5)
        spine.set_color('#CCCCCC')

    ax.set_xticks(range(n))
    ax.set_xticklabels(strategy_names, rotation=28, ha='right',
                       fontsize=7)
    ax.set_yticks(range(n))
    ax.set_yticklabels(strategy_names, fontsize=7)
    ax.set_xlabel('To Strategy', fontsize=8, labelpad=4)
    if idx == 0:
        ax.set_ylabel('From Strategy', fontsize=8, labelpad=4)

    ax.set_title(title, pad=8, fontsize=8.5, fontweight='semibold')
    ax.tick_params(length=0)

# Shared colorbar
cbar_ax = fig.add_axes([0.92, 0.18, 0.012, 0.64])
cbar = fig.colorbar(im, cax=cbar_ax, extend='neither')
cbar.set_label('Transition Count', fontsize=8, labelpad=6)
cbar.ax.tick_params(labelsize=7, length=2)
cbar.outline.set_linewidth(0.4)

# Save
outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper'
fig.savefig(f'{outdir}/fig3_strategy_heatmap.pdf', format='pdf', bbox_inches='tight', pad_inches=0.05)
fig.savefig(f'{outdir}/fig3_strategy_heatmap.png', format='png', bbox_inches='tight', pad_inches=0.05, dpi=300)
plt.close(fig)
print('Saved fig3_strategy_heatmap.pdf, .png, and /tmp/fig_optimize/heatmap_v2.png')
