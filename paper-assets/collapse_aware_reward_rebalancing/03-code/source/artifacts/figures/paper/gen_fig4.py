import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
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
})

# Data: Opening Unique Ratio (candidates pool)
gens_lr = [0, 2]

c1_our = [0.7572, 0.4765]   # curated K=4
c5_our = [0.7532, 0.4789]   # random  K=4
c2_our = [0.701,  0.367]    # curated K=8

# Vendi Score
gens_v = [0, 1, 2]
c1_vendi = [107.54, 106.73, 107.25]
c2_vendi = [107.21, 107.26, 107.25]
c5_vendi = [105.42, 108.21, 108.72]

# Colors (colorblind-friendly)
COL_C1 = '#E69F00'   # orange – curated K=4
COL_C5 = '#0072B2'   # blue   – random  K=4
COL_C2 = '#CC3311'   # red    – curated K=8

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# === Left Panel: Opening Unique Ratio ===
ax1.plot(gens_lr, c1_our, '-o', color=COL_C1, markersize=7,
         label='C1 curated (K=4)')
ax1.plot(gens_lr, c5_our, '-o', color=COL_C5, markersize=7,
         label='C5 random (K=4)')
ax1.plot(gens_lr, c2_our, '--^', color=COL_C2, markersize=8,
         markeredgewidth=1.5, label='C2 curated (K=8)')

ax1.set_xlabel('Generation')
ax1.set_ylabel('Opening Unique Ratio')
ax1.set_title('Format Diversity')
ax1.set_xticks([0, 2])
ax1.set_xticklabels(['Gen 0', 'Gen 2'])
ax1.set_ylim(0.30, 0.85)
ax1.legend(loc='upper right', fontsize=8, framealpha=0.9)

# Annotation: C1/C5 overlap
mid_y_k4 = (c1_our[1] + c5_our[1]) / 2
ax1.annotate('K=4: curated $\\approx$ random',
             xy=(1.85, mid_y_k4 + 0.02), xytext=(0.65, 0.62),
             fontsize=8.5, color='#444444',
             arrowprops=dict(arrowstyle='->', color='#888888', lw=1.2))

# Annotation: C2 steeper
ax1.annotate('K=8: amplified',
             xy=(1.85, c2_our[1] - 0.01), xytext=(0.65, 0.34),
             fontsize=8.5, color=COL_C2, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=COL_C2, lw=1.2))

# === Right Panel: Vendi Score ===
ax2.plot(gens_v, c1_vendi, '-o', color=COL_C1, markersize=7,
         label='C1 curated (K=4)')
ax2.plot(gens_v, c5_vendi, '-o', color=COL_C5, markersize=7,
         label='C5 random (K=4)')
ax2.plot(gens_v, c2_vendi, '--^', color=COL_C2, markersize=8,
         markeredgewidth=1.5, label='C2 curated (K=8)')

# ±1% band around overall mean
all_vendi = c1_vendi + c2_vendi + c5_vendi
overall_mean = np.mean(all_vendi)
ax2.axhspan(overall_mean * 0.99, overall_mean * 1.01, alpha=0.15, color='gray',
            label='$\\pm$1% band')

ax2.set_xlabel('Generation')
ax2.set_ylabel('Vendi Score')
ax2.set_title('Semantic Diversity (Vendi Score)')
ax2.set_xticks([0, 1, 2])
ax2.set_xticklabels(['Gen 0', 'Gen 1', 'Gen 2'])
ax2.set_ylim(103, 111)
ax2.legend(loc='lower right', fontsize=8, framealpha=0.9)
ax2.grid(True, alpha=0.3, linestyle='--', color='lightgray')

# Panel annotations
ax1.text(0.02, 0.98, 'Collapse detected', transform=ax1.transAxes,
         fontsize=9, fontweight='bold', va='top', color=COL_C2)
ax2.text(0.02, 0.98, 'Stable (blind spot)', transform=ax2.transAxes,
         fontsize=9, fontweight='bold', va='top', color='gray')

plt.tight_layout(w_pad=3)

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/figures/paper'
plt.savefig(f'{outdir}/fig4_format_collapse.pdf')
plt.savefig(f'{outdir}/fig4_format_collapse.png')
plt.close()
print(f'Saved: {outdir}/fig4_format_collapse.pdf')
print(f'Saved: {outdir}/fig4_format_collapse.png')
