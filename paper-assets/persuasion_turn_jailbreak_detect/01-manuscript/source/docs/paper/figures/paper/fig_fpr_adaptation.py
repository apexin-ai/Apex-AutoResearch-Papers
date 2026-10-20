import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 8,
    'axes.titlesize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'axes.linewidth': 0.6,
    'lines.linewidth': 1.2,
    'lines.markersize': 4,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# WildChat: N=0 3-seed (68.1±6.4), N=5 seed42, N=10 3-seed (0±0), N=25,50 seed42
wildchat_n   = [0,    5,    10,  25,  50]
wildchat_fpr = [68.1, 16.3, 0.0, 0.0, 0.0]
wildchat_std = [6.4,  None, 0.0, None, None]

# OASST2: all seed 42
oasst2_n   = [0,    10,   25,  50]
oasst2_fpr = [57.5, 20.5, 1.5, 0.5]

# ShareGPT: N=10 3-seed (7.5/15.5/8.5→10.5±3.6), N=25 3-seed (1.0/1.0/6.0→2.7±2.4)
sharegpt_n   = [0,    5,    10,   15,  20,   25]
sharegpt_fpr = [39.0, 21.0, 10.5, 9.5, 10.0, 2.7]
sharegpt_std = [None, None, 3.6,  None, None, 2.4]

c_wc = '#1a3d5c'
c_oa = '#2e75b6'
c_sg = '#7a9bb5'

fig, ax = plt.subplots(figsize=(3.5, 2.4))

# WildChat — with selective error bars
for i, (n, fpr) in enumerate(zip(wildchat_n, wildchat_fpr)):
    s = wildchat_std[i]
    if s is not None:
        ax.errorbar(n, fpr, yerr=s, fmt='o', color=c_wc, markersize=4.5,
                    markerfacecolor=c_wc, markeredgecolor='white', markeredgewidth=0.4,
                    capsize=2, capthick=0.6, elinewidth=0.8, zorder=3)
ax.plot(wildchat_n, wildchat_fpr, '-', color=c_wc, label='WildChat', zorder=2)
ax.plot(wildchat_n, wildchat_fpr, 'o', color=c_wc, markersize=4.5,
        markerfacecolor=c_wc, markeredgecolor='white', markeredgewidth=0.4, zorder=3)

# OASST2 — single seed, all markers same
ax.plot(oasst2_n, oasst2_fpr, '--s', color=c_oa, label='OASST2 (single seed)',
        markersize=4.5, markerfacecolor=c_oa, markeredgecolor='white',
        markeredgewidth=0.4, zorder=3)

# ShareGPT — with selective error bars
for i, (n, fpr) in enumerate(zip(sharegpt_n, sharegpt_fpr)):
    s = sharegpt_std[i]
    if s is not None:
        ax.errorbar(n, fpr, yerr=s, fmt='^', color=c_sg, markersize=5,
                    markerfacecolor=c_sg, markeredgecolor='white', markeredgewidth=0.4,
                    capsize=2, capthick=0.6, elinewidth=0.8, zorder=3)
ax.plot(sharegpt_n, sharegpt_fpr, '-.', color=c_sg, label='ShareGPT', zorder=2)
ax.plot(sharegpt_n, sharegpt_fpr, '^', color=c_sg, markersize=5,
        markerfacecolor=c_sg, markeredgecolor='white', markeredgewidth=0.4, zorder=3)

# Deploy threshold
ax.axhline(y=5, color='#c0392b', linestyle=':', linewidth=0.7, alpha=0.5, zorder=1)
ax.text(53, 5, '5%', fontsize=5.5, color='#c0392b', ha='left', va='center', alpha=0.7)

# N=0 annotations
ax.annotate('68.1%', (0, 68.1), textcoords='offset points', xytext=(6, 1),
            fontsize=6, color=c_wc, fontweight='bold', va='center')
ax.annotate('57.5%', (0, 57.5), textcoords='offset points', xytext=(6, -1),
            fontsize=6, color=c_oa, fontweight='bold', va='center')
ax.annotate('39.0%', (0, 39.0), textcoords='offset points', xytext=(6, -6),
            fontsize=6, color=c_sg, fontweight='bold', va='top')

ax.set_xlabel('Benign conversations ($N$)')
ax.set_ylabel('FPR (%)')
ax.set_xticks([0, 5, 10, 15, 20, 25, 50])
ax.set_xlim(-2, 56)
ax.set_ylim(-3, 78)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(loc='upper right', framealpha=0.95, edgecolor='#cccccc',
          borderpad=0.4, handlelength=2.0, labelspacing=0.3)

plt.tight_layout()
out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig_fpr_adaptation'
plt.savefig(out_base + '.pdf', bbox_inches='tight', pad_inches=0.05, dpi=300)
plt.savefig(out_base + '.png', bbox_inches='tight', pad_inches=0.05, dpi=300)
print("Done")
