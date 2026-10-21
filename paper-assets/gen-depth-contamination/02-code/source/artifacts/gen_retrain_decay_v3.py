import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x_labels = ['0v1', '1v2', '2v3', '3v4', '4v5', '5v6', '6v7']
x = np.arange(len(x_labels))

# Qwen2.5-1.5B retrain-chain
qwen_auc = [0.984, 0.900, 0.811, 0.760, 0.746, 0.700, 0.641]
qwen_ci = [[0.983,0.985], [0.895,0.905], [0.804,0.818], [0.752,0.768], [0.738,0.754], [0.692,0.708], [0.633,0.649]]
qwen_lo = [a - ci[0] for a, ci in zip(qwen_auc, qwen_ci)]
qwen_hi = [ci[1] - a for a, ci in zip(qwen_auc, qwen_ci)]

# Pythia-1.4B retrain-chain
pythia_auc = [0.9844, 0.947, 0.8891, 0.7999, 0.6907, 0.6497, 0.634]
pythia_ci = [[0.9829,0.9858], [0.9418,0.9522], [0.8822,0.896], [0.7951,0.8047], [0.688,0.6934], [0.6429,0.6565], [0.6275,0.6406]]
pythia_lo = [a - ci[0] for a, ci in zip(pythia_auc, pythia_ci)]
pythia_hi = [ci[1] - a for a, ci in zip(pythia_auc, pythia_ci)]

# Prompt-chain (only 5 points: 0v1 to 4v5)
prompt_x = x[:5]
prompt_auc = [0.976, 0.632, 0.550, 0.525, 0.517]
prompt_ci = [[0.972,0.980], [0.617,0.647], [0.534,0.566], [0.510,0.540], [0.502,0.532]]
prompt_lo = [a - ci[0] for a, ci in zip(prompt_auc, prompt_ci)]
prompt_hi = [ci[1] - a for a, ci in zip(prompt_auc, prompt_ci)]

fig, ax = plt.subplots(figsize=(7, 4.5))

ax.errorbar(x, qwen_auc, yerr=[qwen_lo, qwen_hi], fmt='-o',
            color='#2171B5', markerfacecolor='#2171B5', markersize=7,
            linewidth=2.0, capsize=3, label='Qwen retrain')

ax.errorbar(x, pythia_auc, yerr=[pythia_lo, pythia_hi], fmt='-^',
            color='#238B45', markerfacecolor='#238B45', markersize=7,
            linewidth=2.0, capsize=3, label='Pythia retrain')

ax.errorbar(prompt_x, prompt_auc, yerr=[prompt_lo, prompt_hi], fmt='--s',
            color='#E6550D', markerfacecolor='#E6550D', markersize=7,
            linewidth=2.0, capsize=3, label='Prompt-chain')

# Threshold line
ax.axhline(y=0.60, color='#D62728', linestyle=':', linewidth=1.5, zorder=1)
ax.text(6.55, 0.605, r'$\theta$ = 0.60', fontsize=9, color='#D62728', va='bottom')

# Annotation: Retrain K*=7
ax.annotate(r'Retrain $K^*$=7', xy=(6, 0.641), xytext=(5.0, 0.52),
            fontsize=9, fontweight='bold', color='#333333',
            arrowprops=dict(arrowstyle='->', color='#555555', lw=1.2),
            ha='center')

# Annotation: Prompt K*=2
ax.annotate(r'Prompt $K^*$=2', xy=(1, 0.632), xytext=(2.2, 0.72),
            fontsize=9, fontweight='bold', color='#333333',
            arrowprops=dict(arrowstyle='->', color='#555555', lw=1.2),
            ha='center')

ax.set_xticks(x)
ax.set_xticklabels(x_labels, fontsize=10)
ax.set_ylabel('Pairwise AUC', fontsize=11)
ax.set_ylim(0.45, 1.02)
ax.set_xlim(-0.3, 6.8)

ax.legend(loc='upper left', fontsize=9, framealpha=0.9, edgecolor='#cccccc')
ax.tick_params(axis='both', labelsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts'
fig_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures'

plt.savefig(f'{out_dir}/retrain_decay_curve_v3.pdf', dpi=300, bbox_inches='tight')
plt.savefig(f'{out_dir}/retrain_decay_curve_v3.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{fig_dir}/fig_retrain_decay.png', dpi=300, bbox_inches='tight')
plt.close()
print('Done')
