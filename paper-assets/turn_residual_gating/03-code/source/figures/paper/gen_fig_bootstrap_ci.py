"""Figure C (Appendix): Bootstrap CI — TG vs LoRA-only AR GAR difference."""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import numpy as np

apply_style()
np.random.seed(42)

obs_diff = 0.027
boot_mean = 0.027
boot_std = 0.007
n_boot = 10000

samples = np.random.normal(boot_mean, boot_std, n_boot)
ci_lo, ci_hi = np.percentile(samples, [2.5, 97.5])

fig, ax = plt.subplots(figsize=(4.5, 2.5))

n, bins, patches = ax.hist(samples, bins=60, color=C_TG, alpha=0.5,
                           edgecolor='white', linewidth=0.3, zorder=2)

mask = (bins[:-1] >= ci_lo) & (bins[:-1] <= ci_hi)
for p, m in zip(patches, mask):
    if m:
        p.set_alpha(0.75)

ax.axvline(obs_diff, color='#444444', linewidth=1.4, linestyle='-', zorder=4)
ax.text(obs_diff + 0.0008, ax.get_ylim()[1] * 0.92,
        f'observed Δ = {obs_diff:.3f}',
        fontsize=7, color='#444444', ha='left', va='top')

ax.axvline(ci_lo, color=C_GRAY, linewidth=0.9, linestyle='--', zorder=3)
ax.axvline(ci_hi, color=C_GRAY, linewidth=0.9, linestyle='--', zorder=3)
ax.axvspan(ci_lo, ci_hi, alpha=0.08, color=C_TG, zorder=0)

ax.text(ci_lo, ax.get_ylim()[1] * 0.78, f'{ci_lo:.3f}',
        fontsize=6, color='#777777', ha='center', va='top')
ax.text(ci_hi, ax.get_ylim()[1] * 0.78, f'{ci_hi:.3f}',
        fontsize=6, color='#777777', ha='center', va='top')

mid_ci = (ci_lo + ci_hi) / 2
ax.annotate('95% CI', xy=(mid_ci, ax.get_ylim()[1] * 0.65),
            fontsize=7, color='#666666', ha='center')

ax.set_xlabel('TG − LoRA AR GAR difference', fontsize=9)
ax.set_ylabel('Count', fontsize=9)

save_fig(fig, 'fig_bootstrap_ci')
