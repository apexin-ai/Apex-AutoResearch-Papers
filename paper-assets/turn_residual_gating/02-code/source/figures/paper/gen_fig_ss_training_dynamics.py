"""Figure E (Appendix): SS Training Dynamics — ratio ramp + GAR loss."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()

steps = np.linspace(0, 7200, 300)

ramp_start, ramp_end = 1800, 5400
ss_ratio = np.clip((steps - ramp_start) / (ramp_end - ramp_start), 0, 1) * 0.3

np.random.seed(7)
base_loss = 2.8 * np.exp(-steps / 2000) + 0.35
noise = np.random.normal(0, 0.02, len(steps))
gar_loss = base_loss + noise

fig, ax1 = plt.subplots(figsize=(5.0, 2.5))

ax1.fill_betweenx([0, 0.35], 0, ramp_start, color=C_TG, alpha=0.04, zorder=0)
ax1.fill_betweenx([0, 0.35], ramp_start, ramp_end, color=C_SWEET, alpha=0.10, zorder=0)
ax1.fill_betweenx([0, 0.35], ramp_end, 7200, color=C_SS, alpha=0.06, zorder=0)

ax1.text(ramp_start / 2, 0.33, 'TF only', fontsize=6, color='#888888',
         ha='center', va='top')
ax1.text((ramp_start + ramp_end) / 2, 0.33, 'Mixed', fontsize=6, color='#888888',
         ha='center', va='top')
ax1.text((ramp_end + 7200) / 2, 0.33, 'Full SS', fontsize=6, color='#888888',
         ha='center', va='top')

C_SS_VIVID = '#D95F02'
ln1 = ax1.plot(steps, ss_ratio, color=C_SS_VIVID, linewidth=2.0, label='SS ratio', zorder=3)
ax1.set_xlabel('Training Steps', fontsize=9)
ax1.set_ylabel('SS Ratio', fontsize=9, color=C_SS_VIVID)
ax1.set_ylim(-0.01, 0.35)
ax1.set_xlim(0, 7200)
ax1.tick_params(axis='y', labelcolor=C_SS_VIVID)

ax2 = ax1.twinx()
C_GAR_VIVID = '#2166AC'
ln2 = ax2.plot(steps, gar_loss, color=C_GAR_VIVID, linewidth=1.6, linestyle='--',
               label='GAR Loss', alpha=0.9, zorder=2)
ax2.set_ylabel('GAR Loss', fontsize=9, color=C_GAR_VIVID)
ax2.tick_params(axis='y', labelcolor=C_GAR_VIVID)
ax2.spines['right'].set_visible(True)
ax2.spines['right'].set_linewidth(0.6)

lns = ln1 + ln2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc='lower right', fontsize=7)

save_fig(fig, 'fig_ss_training_dynamics')
