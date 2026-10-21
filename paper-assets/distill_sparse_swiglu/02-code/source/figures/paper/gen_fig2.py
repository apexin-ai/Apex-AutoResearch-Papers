"""Figure 3: PPL scaling with sparsity (global allocation). KL advantage grows with sparsity."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.5,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'mathtext.fontset': 'cm',
})

COL_KL = '#4472C4'
COL_TEAL = '#E05A3A'
COL_DENSE = '#888888'

OUT = '/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/figures/paper'

# Data: all s42 global allocation
kl_sparsity   = [28.5, 40.0, 50.0, 69.9]
kl_ppl        = [8.98, 10.14, 11.79, 17.91]
teal_sparsity = [28.5, 50.0, 69.9]
teal_ppl      = [10.97, 23.31, 100.11]
dense_ppl     = 6.12
advantages    = ['18%', '49%', '82%']
matched_sp    = [28.5, 50.0, 69.9]
matched_kl    = [8.98, 11.79, 17.91]

fig, ax = plt.subplots(figsize=(3.3, 2.8))

ax.axhline(y=dense_ppl, color=COL_DENSE, linestyle='--', linewidth=0.9, zorder=1)
t = ax.text(71, dense_ppl * 1.07, f'Dense ({dense_ppl})', color=COL_DENSE,
            fontsize=7, ha='right', va='bottom')
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

ax.plot(kl_sparsity, kl_ppl, 'o-', color=COL_KL, markersize=5.5,
        label='KL Predictor (Ours)', zorder=3, markeredgecolor='white',
        markeredgewidth=0.5)
ax.plot(teal_sparsity, teal_ppl, '^--', color=COL_TEAL, markersize=6,
        markeredgewidth=1.2, linewidth=1.2, label='Vanilla TEAL', zorder=3)

for x_val, y_val in zip(kl_sparsity, kl_ppl):
    t = ax.annotate(f'{y_val:.2f}', (x_val, y_val),
                    textcoords='offset points', xytext=(0, -8),
                    fontsize=7, color=COL_KL, ha='center', va='top')
    t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

for x_val, y_val in zip(teal_sparsity, teal_ppl):
    t = ax.annotate(f'{y_val:.1f}', (x_val, y_val),
                    textcoords='offset points', xytext=(0, 6),
                    fontsize=7, color=COL_TEAL, ha='center', va='bottom')
    t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

for i, (sp, adv) in enumerate(zip(matched_sp, advantages)):
    mid_y = np.sqrt(matched_kl[i] * teal_ppl[i])
    t = ax.text(sp + 2.5, mid_y, f'{adv}\nbetter',
                fontsize=6.5, color='#555555', ha='left', va='center',
                fontstyle='italic')
    t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

ax.set_yscale('log')
ax.set_yticks([6, 8, 10, 15, 20, 30, 50, 100])
ax.set_yticklabels(['6', '8', '10', '15', '20', '30', '50', '100'])
ax.set_ylim(5, 130)
ax.set_xlabel('Achieved Model-Level Sparsity (%)')
ax.set_ylabel('WikiText-2 Perplexity (log)')
ax.set_xlim(22, 76)
ax.set_xticks([30, 40, 50, 60, 70])

ax.yaxis.grid(True, color='#E0E0E0', linewidth=0.4, zorder=0)
ax.set_axisbelow(True)
ax.legend(loc='upper left', framealpha=0.9, edgecolor='#DDDDDD',
          fancybox=False)

fig.tight_layout()
fig.savefig(f'{OUT}/fig2_sparsity_sweep.pdf')
fig.savefig(f'{OUT}/fig2_sparsity_sweep.png')
print('Saved fig2_sparsity_sweep.pdf/.png')
plt.close()
