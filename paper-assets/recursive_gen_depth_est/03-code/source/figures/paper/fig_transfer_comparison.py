import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8.5,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 2.6), sharey=True)
fig.subplots_adjust(wspace=0.06)

colors = ['#4E79A7', '#F28E2B', '#E15759']

# Panel (a): Cross-model transfer
models = ['Pythia', 'OLMo', 'GPT-2 XL']
model_acc = [62.4, 69.2, 67.6]
model_mean = 66.4

bars1 = ax1.bar(np.arange(3), model_acc, width=0.55, color=colors, edgecolor='white', linewidth=0.5)
ax1.axhline(y=25, color='gray', linestyle=':', linewidth=0.7, alpha=0.6)
ax1.axhline(y=model_mean, color='#555555', linestyle='--', linewidth=0.7, alpha=0.4)
ax1.set_xticks(np.arange(3))
ax1.set_xticklabels(models)
ax1.set_ylabel('Four-class accuracy (%)')
ax1.set_title('(a) Cross-model transfer', pad=6)
ax1.set_ylim(0, 82)
ax1.set_xlim(-0.5, 3.3)
ax1.set_yticks([0, 20, 40, 60, 80])

for bar, val in zip(bars1, model_acc):
    ax1.text(bar.get_x() + bar.get_width()/2, val + 1.5, f'{val:.1f}',
             ha='center', va='bottom', fontsize=7.5, fontweight='bold')

ax1.text(-0.4, model_mean - 3, f'mean\n{model_mean}%',
         ha='left', va='top', fontsize=6.5, color='#555555')
ax1.text(0, 27, 'chance', fontsize=6, color='gray', alpha=0.7)

gap_model = max(model_acc) - min(model_acc)
ax1.annotate('', xy=(2.85, min(model_acc)), xytext=(2.85, max(model_acc)),
            arrowprops=dict(arrowstyle='<->', color='#333333', lw=1))
ax1.text(2.95, (min(model_acc)+max(model_acc))/2, f'Δ={gap_model:.1f}pp',
         ha='left', va='center', fontsize=7, color='#333333')

# Panel (b): Cross-strategy transfer
strategies = ['Nucleus', 'Temp', 'Top-k']
strat_acc = [64.9, 59.0, 53.3]
strat_mean = 59.1

bars2 = ax2.bar(np.arange(3), strat_acc, width=0.55, color=colors, edgecolor='white', linewidth=0.5)
ax2.axhline(y=25, color='gray', linestyle=':', linewidth=0.7, alpha=0.6)
ax2.axhline(y=strat_mean, color='#555555', linestyle='--', linewidth=0.7, alpha=0.4)
ax2.set_xticks(np.arange(3))
ax2.set_xticklabels(strategies)
ax2.set_title('(b) Cross-strategy transfer', pad=6)
ax2.set_xlim(-0.5, 3.3)

for bar, val in zip(bars2, strat_acc):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 1.5, f'{val:.1f}',
             ha='center', va='bottom', fontsize=7.5, fontweight='bold')

ax2.text(-0.4, strat_mean - 3, f'mean\n{strat_mean}%',
         ha='left', va='top', fontsize=6.5, color='#555555')

gap_strat = max(strat_acc) - min(strat_acc)
ax2.annotate('', xy=(2.85, min(strat_acc)), xytext=(2.85, max(strat_acc)),
            arrowprops=dict(arrowstyle='<->', color='#333333', lw=1))
ax2.text(2.95, (min(strat_acc)+max(strat_acc))/2, f'Δ={gap_strat:.1f}pp',
         ha='left', va='center', fontsize=7, color='#333333')

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/figures/fig_transfer_comparison'
fig.savefig(f'{out_base}.pdf')
fig.savefig(f'{out_base}.png')
plt.close(fig)
print('Done')
