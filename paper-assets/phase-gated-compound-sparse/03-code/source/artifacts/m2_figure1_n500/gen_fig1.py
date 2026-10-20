# Fig 1: Severity gradient G vs sparsity (n=496 paired problems)
# Data source: table2_n500_full.csv (DeepSeek-R1-Distill-Qwen-7B)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Times'],
    'font.size': 10,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

C_IMP = '#1f77b4'
C_RND = '#d62728'
FIG_W = 3.5

sparsity = [0.15, 0.20, 0.25, 0.30]

imp_G     = [7.4529, 17.9049, 49.0639, 79.7854]
imp_ci_lo = [4.0978, 12.7448, 40.0936, 63.3276]
imp_ci_hi = [11.3624, 26.3073, 57.8341, 96.5117]

rnd_G     = [0.5174, 0.7594, 1.0917, 1.1487]
rnd_ci_lo = [0.3993, 0.6496, 0.9640, 1.0499]
rnd_ci_hi = [0.6073, 0.8884, 1.1948, 1.2737]

fig, ax = plt.subplots(figsize=(FIG_W, 2.6))
ax.fill_between(sparsity, imp_ci_lo, imp_ci_hi, color=C_IMP, alpha=0.15)
ax.plot(sparsity, imp_G, '-o', color=C_IMP, markersize=5, linewidth=1.5, label='Importance')
ax.fill_between(sparsity, rnd_ci_lo, rnd_ci_hi, color=C_RND, alpha=0.15)
ax.plot(sparsity, rnd_G, '--s', color=C_RND, markersize=5, linewidth=1.5, label='Random')
ax.axhline(y=1, color='gray', linewidth=0.5, linestyle=':')
ax.set_xlabel('Sparsity ratio $s$')
ax.set_ylabel('Severity gradient $G$')
ax.set_xticks(sparsity)
ax.legend(frameon=False, loc='upper left')
ax.set_xlim(0.13, 0.32)
ax.set_ylim(bottom=0)

outdir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(outdir, 'figure1_n500.pdf'))
fig.savefig(os.path.join(outdir, 'figure1_n500.png'))
plt.close(fig)
print('Done')
