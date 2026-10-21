import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 10,
    'legend.fontsize': 8,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'text.usetex': False,
    'mathtext.fontset': 'cm',
})

p = np.linspace(0.001, 1.0, 1000)
K_values = [2, 4, 8, 16]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd']

fig, ax = plt.subplots(figsize=(3.5, 2.8))

for K, color in zip(K_values, colors):
    P_correct = p / (1 - (1 - p)**K)
    ax.plot(p, P_correct, color=color, linewidth=1.3, label=f'$K={K}$')

ax.axhline(y=0.5, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
ax.text(0.82, 0.53, 'random chance', fontsize=7, color='gray')

ax.plot(p, p, color='gray', linestyle=':', linewidth=0.8, alpha=0.7)
ax.text(0.72, 0.60, '$K \\to \\infty$', fontsize=7, color='gray', rotation=30)

p_op = 0.125
K_op = 8
P_op = p_op / (1 - (1 - p_op)**K_op)
ax.plot(p_op, P_op, marker='*', markersize=10, color='#d62728', zorder=5)
ax.annotate(
    'Operating point\n($p$=12.5%, $K$=8)',
    xy=(p_op, P_op),
    xytext=(0.42, 0.12),
    fontsize=7,
    color='#d62728',
    arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.0, shrinkA=0, shrinkB=3),
    ha='left', va='center',
)

ax.set_xlabel('Success rate $p$')
ax.set_ylabel('$P(\\mathrm{correct\\ sign} \\mid \\mathrm{update})$')
ax.set_xlim(0, 1.0)
ax.set_ylim(0, 1.05)
ax.legend(loc='upper left', framealpha=0.9, edgecolor='none')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.tight_layout(pad=0.4)

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/figures/paper'
fig.savefig(f'{outdir}/fig_theoretical_sign_probability.pdf', dpi=300, bbox_inches='tight')
fig.savefig(f'{outdir}/fig_theoretical_sign_probability.png', dpi=300, bbox_inches='tight')
print('Saved.')

for K in K_values:
    for pv in [0.05, 0.1, 0.125, 0.2, 0.5]:
        val = pv / (1 - (1 - pv)**K)
        print(f'K={K:2d}, p={pv:.3f} -> P(correct|update) = {val:.4f} ({val*100:.1f}%)')
