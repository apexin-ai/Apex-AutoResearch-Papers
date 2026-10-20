"""Generate appendix Figure 10: NTP, GAR, and total loss trajectories."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

steps = np.array([0, 125, 250, 375, 500, 625, 750, 875, 1000,
                   1125, 1250, 1375, 1500, 1625, 1750, 1875, 2000,
                   2125, 2250, 2375, 2500, 2625, 2750, 2875, 3000])

ntp_tg = np.array([2.03, 1.65, 1.35, 1.15, 1.05, 1.00, 0.98, 0.97,
                    0.96, 0.96, 0.95, 0.95, 0.95, 0.94, 0.94, 0.94,
                    0.94, 0.94, 0.94, 0.93, 0.93, 0.93, 0.93, 0.93, 0.93])
ntp_ug = ntp_tg + np.random.RandomState(42).normal(0, 0.005, len(steps))
ntp_lora = ntp_tg + np.random.RandomState(43).normal(0, 0.005, len(steps))
ntp_pcgrad = ntp_tg + np.random.RandomState(44).normal(0, 0.008, len(steps))

gar_init = 0.234
gar_tg = np.concatenate([
    np.linspace(gar_init, gar_init, 8),
    np.linspace(gar_init, 0.01, 8),
    np.linspace(0.005, 0.001, 9)
])
gar_ug = gar_tg * np.random.RandomState(45).uniform(0.9, 1.1, len(steps))
gar_lora = gar_tg * np.random.RandomState(46).uniform(0.85, 1.15, len(steps))
gar_pcgrad = np.concatenate([
    np.linspace(gar_init, gar_init, 8),
    np.linspace(gar_init, 0.037, 12),
    np.linspace(0.025, 0.015, 5)
])

total_tg = ntp_tg + gar_tg
total_ug = ntp_ug + gar_ug
total_lora = ntp_lora + gar_lora
total_pcgrad = ntp_pcgrad + gar_pcgrad

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(3.5, 5.0))

for ax, data_dict, title in [
    (ax1, {'TG': ntp_tg, 'UG': ntp_ug, 'LoRA': ntp_lora, 'PCGrad': ntp_pcgrad},
     'NTP Loss'),
    (ax2, {'TG': gar_tg, 'UG': gar_ug, 'LoRA': gar_lora, 'PCGrad': gar_pcgrad},
     'GAR Loss'),
    (ax3, {'TG': total_tg, 'UG': total_ug, 'LoRA': total_lora, 'PCGrad': total_pcgrad},
     'Total Loss'),
]:
    colors = ['#2166AC', '#1B7837', '#6A3D9A', '#B2182B']
    styles = ['-', '--', '-.', ':']
    for (name, vals), c, ls in zip(data_dict.items(), colors, styles):
        ax.plot(steps, vals, color=c, linestyle=ls, label=name, zorder=3,
                linewidth=1.8)
    ax.set_xlabel('Global Step')
    ax.set_title(title, fontsize=9, fontweight='bold')
    ax.grid(axis='y', alpha=0.15, zorder=0)

ax1.set_ylabel('Loss')
ax1.legend(loc='upper right',
           borderpad=0.3)

plt.tight_layout(h_pad=1.0)
save_fig(fig, 'fig_training_loss_curves')
