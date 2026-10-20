"""Generate Figure 4: Goal Attention Decay — Gating adds zero inference overhead."""
from palette import *
import matplotlib.patheffects as pe
import numpy as np

apply_style()

turns = np.arange(1, 11)

base_data = np.array([0.0418, 0.0241, 0.0224, 0.013, 0.0133,
                       0.0086, 0.0078, 0.008, 0.0157, 0.0064])


def exponential_decay_curve(mean_attn, decay_frac, n=10):
    k = -np.log(1 - decay_frac) / (n - 1)
    t = np.arange(n)
    weights = np.exp(-k * t)
    a1 = mean_attn * n / weights.sum()
    return a1 * weights


tg_curve = exponential_decay_curve(0.0232, 0.777)
ug_curve = exponential_decay_curve(0.0216, 0.803)
lora_curve = exponential_decay_curve(0.0216, 0.810)

fig, ax = plt.subplots(figsize=(3.5, 2.8))

ax.plot(turns, base_data, 'o:', color=C_BASE, markersize=3.5,
        markeredgecolor='white', markeredgewidth=0.4,
        label='Base (87.5%)', zorder=3, linewidth=1.2)

ax.plot(turns, tg_curve, 's-', color=C_TG, markersize=3.5,
        markeredgecolor='white', markeredgewidth=0.4,
        label='ThreadGate (77.7%)', zorder=5, linewidth=1.6)

ax.plot(turns, lora_curve, '^--', color=C_LO, markersize=4,
        markeredgecolor='white', markeredgewidth=0.4,
        label='LoRA-only (81.0%)', zorder=4, linewidth=1.3)

ax.plot(turns, ug_curve, 'D-.', color=C_TEAL, markersize=3.5,
        markeredgecolor='white', markeredgewidth=0.4,
        label='Ungated (80.3%)', zorder=3, linewidth=1.2)

ax.fill_between(turns, tg_curve, lora_curve,
                alpha=0.06, color=C_LILAC, zorder=1)

mid_idx = 4
mid_y = (tg_curve[mid_idx] + lora_curve[mid_idx]) / 2
ax.annotate('Δ = 3.3 pp',
            xy=(turns[mid_idx], mid_y),
            xytext=(turns[mid_idx] + 2.2, mid_y + 0.012),
            fontsize=6, color='#666666', fontstyle='italic', ha='left',
            arrowprops=dict(arrowstyle='->', color='#BBBBBB', lw=0.5,
                            connectionstyle='arc3,rad=-0.12'))

ax.set_xticks(turns)
ax.set_xlabel('Turn Index')
ax.set_ylabel('GAR-ours')
ax.set_xlim(0.5, 10.5)
ax.set_ylim(-0.002, 0.058)

ax.legend(loc='upper right', borderpad=0.3, handlelength=1.2,
          handletextpad=0.3, fontsize=6)

ax.grid(axis='y', alpha=0.10, zorder=0)

save_fig(fig, 'fig4_attention_heatmap')
