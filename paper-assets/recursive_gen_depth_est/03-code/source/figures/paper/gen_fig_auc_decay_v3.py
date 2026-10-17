import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

depth_pairs = ['d0→d1', 'd1→d2', 'd2→d3', 'd3→d4', 'd4→d5']
x = np.arange(len(depth_pairs))

# Binary pairwise RF (500 trees, dedicated per pair)
# d0v1 from 4-class reference (noted in caption)
binary_mean = np.array([0.9975, 0.9250, 0.8225, 0.7837, 0.6832])
binary_ci_lo = np.array([0.995,  0.914,  0.805,  0.765,  0.661])
binary_ci_hi = np.array([1.000,  0.935,  0.840,  0.802,  0.705])
binary_err_lo = binary_mean - binary_ci_lo
binary_err_hi = binary_ci_hi - binary_mean

# 4-class multiclass pipeline (Pythia nucleus d0-d3)
fourclass_mean = np.array([0.9975, 0.8607, 0.8005])
fourclass_x = x[:3]

# 6-class multiclass pipeline (Pythia nucleus d0-d5)
sixclass_mean = np.array([0.9962, 0.8231, 0.6878, 0.6809, 0.6948])

fig, ax = plt.subplots(figsize=(6, 4))

# Shaded CI band (higher alpha for visibility)
ax.fill_between(x, binary_ci_lo, binary_ci_hi,
                color='#0072B2', alpha=0.25, zorder=2,
                label='95% CI')

# Binary pairwise line with error bar CAPS
ax.errorbar(x, binary_mean,
            yerr=[binary_err_lo, binary_err_hi],
            fmt='o-', color='#0072B2', linewidth=2.0, markersize=7,
            capsize=5, capthick=1.5, elinewidth=1.5,
            label='Binary pairwise RF', zorder=3)

# 4-class pipeline
ax.plot(fourclass_x, fourclass_mean, '^--', color='#E69F00',
        linewidth=1.5, markersize=7, label='4-class multiclass RF', zorder=3)

# 6-class pipeline
ax.plot(x, sixclass_mean, 's:', color='#009E73',
        linewidth=1.5, markersize=6, label='6-class multiclass RF', zorder=3)

# Threshold lines
for t_label, t_val in [('T=0.80', 0.80), ('T=0.75', 0.75),
                        ('T=0.70', 0.70), ('T=0.65', 0.65)]:
    ax.axhline(t_val, color='gray', linestyle='--', linewidth=0.7, alpha=0.5, zorder=1)
    ax.text(4.55, t_val, t_label, va='center', fontsize=9, color='gray')

# EDD=4 boundary
ax.axvline(3.5, color='#CC0000', linestyle='--', linewidth=1.2, alpha=0.7, zorder=1)
ax.axvspan(3.5, 4.5, alpha=0.06, color='red', zorder=0)
ax.text(3.55, 0.99, 'EDD=4', fontsize=11, fontweight='bold',
        color='#CC0000', va='top', zorder=4)

# Annotate d3v4 CI lower bound vs T=0.75
ax.annotate('CI lower = 0.765',
            xy=(3, 0.765), xytext=(1.5, 0.72),
            fontsize=9, color='#0072B2',
            arrowprops=dict(arrowstyle='->', color='#0072B2', lw=1.2),
            zorder=4)

ax.set_xticks(x)
ax.set_xticklabels(depth_pairs)
ax.set_xlabel('Adjacent Depth Pair')
ax.set_ylabel('Pairwise AUC')
ax.set_ylim(0.55, 1.05)
ax.set_xlim(-0.3, 4.8)
ax.legend(loc='upper right', framealpha=0.9)
ax.grid(True, alpha=0.2, zorder=0)

plt.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/figures/paper'
plt.savefig(f'{outdir}/fig_auc_decay.pdf')
plt.savefig(f'{outdir}/fig_auc_decay.png')
plt.close()
print('Saved fig_auc_decay v3 with explicit error bars + CI annotation')
