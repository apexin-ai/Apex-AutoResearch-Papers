import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

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

COLORS = {
    'unpruned': '#0072B2',
    'standard': '#56B4E9',
    'rasp': '#E69F00',
    'collapse': '#D55E00',
}

# --- Data ---
# Unpruned (100 steps)
unpruned_steps = np.array([1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
unpruned_reward = np.array([0.0, 0.15, 0.32, 0.425, 0.5, 0.55, 0.6, 0.64, 0.669, 0.665, 0.661])

# Standard 20% (90 steps)
standard_steps = np.array([1, 10, 20, 30, 40, 50, 60, 70, 80, 90])
standard_reward = np.array([0.0, 0.03, 0.06, 0.08, 0.096, 0.037, 0.041, 0.05, 0.058, 0.065])

# RASP 20% (30 steps)
rasp_steps = np.array([1, 5, 10, 15, 20, 25, 30])
rasp_reward = np.array([0.0, 0.005, 0.015, 0.028, 0.039, 0.030, 0.021])

# Accuracy data (GSM8K, N=1319)
models = ['Unpruned', 'Standard\n20%', 'RASP\n20%']
sft_acc = [81.27, 59.29, 61.49]
grpo_acc = [81.27, 58.91, 61.87]
deltas = [0.00, -0.38, +0.38]

# --- Figure ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5), gridspec_kw={'width_ratios': [1.3, 1]})

# Panel (a): Reward curves
ax1.plot(unpruned_steps, unpruned_reward, color=COLORS['unpruned'], marker='o', markersize=4, label='Unpruned')
ax1.plot(standard_steps, standard_reward, color=COLORS['standard'], marker='s', markersize=4, label='Standard 20%')
ax1.plot(rasp_steps, rasp_reward, color=COLORS['rasp'], marker='^', markersize=4, label='RASP 20%')

# Collapse onset annotations
ax1.axvline(x=60, color=COLORS['collapse'], linestyle='--', linewidth=1.0, alpha=0.7)
ax1.axvline(x=10, color=COLORS['collapse'], linestyle='--', linewidth=1.0, alpha=0.7)

ax1.annotate('Collapse\nonset', xy=(60, 0.041), xytext=(68, 0.20),
             fontsize=9, color=COLORS['collapse'],
             arrowprops=dict(arrowstyle='->', color=COLORS['collapse'], lw=1.2))
ax1.annotate('Collapse\nonset', xy=(10, 0.015), xytext=(16, 0.15),
             fontsize=9, color=COLORS['collapse'],
             arrowprops=dict(arrowstyle='->', color=COLORS['collapse'], lw=1.2))

ax1.set_xlabel('Training Step')
ax1.set_ylabel('Mean Reward')
ax1.set_xlim(0, 105)
ax1.set_ylim(-0.02, 0.75)
ax1.legend(loc='upper left', framealpha=0.9, bbox_to_anchor=(0.12, 1.0))
ax1.text(0.02, 0.98, '(a)', transform=ax1.transAxes, fontsize=13, fontweight='bold', va='top')

# Panel (b): Accuracy bars
x = np.arange(len(models))
width = 0.32

bars_sft = ax2.bar(x - width/2, sft_acc, width, label='SFT', color=[COLORS['unpruned'], COLORS['standard'], COLORS['rasp']], alpha=0.45, edgecolor='none')
bars_grpo = ax2.bar(x + width/2, grpo_acc, width, label='GRPO', color=[COLORS['unpruned'], COLORS['standard'], COLORS['rasp']], alpha=0.9, edgecolor='none')

ax2.set_ylim(50, 88)
ax2.set_ylabel('Accuracy (%)')
ax2.set_xticks(x)
ax2.set_xticklabels(models)
ax2.legend(loc='upper right', framealpha=0.9)

# Delta annotations
for i, delta in enumerate(deltas):
    y_top = max(sft_acc[i], grpo_acc[i]) + 1.2
    sign = '+' if delta > 0 else ''
    label = f'Δ={sign}{delta:.2f}\nn.s.'
    ax2.text(x[i], y_top, label, ha='center', va='bottom', fontsize=9, color='#555555')

ax2.text(0.02, 0.98, '(b)', transform=ax2.transAxes, fontsize=13, fontweight='bold', va='top')

plt.tight_layout(w_pad=3)

out_dir = Path('/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper')
fig.savefig(out_dir / 'fig2_reward_accuracy.pdf')
fig.savefig(out_dir / 'fig2_reward_accuracy.png')
plt.close()
print("Done: fig2_reward_accuracy.pdf and .png saved.")
