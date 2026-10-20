import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_style import apply_style
apply_style()

categories = ['dt=1\n(baseline, N=2)', 'dt=2\n(006, N=1)', 'dt=4\n(007, N=1)']
baseline_seeds = [970.41, 966.94]
baseline_mean = np.mean(baseline_seeds)
baseline_std = np.std(baseline_seeds, ddof=1)
peak_returns = [baseline_mean, 485.3, 176.9]
yerr = [baseline_std, 0, 0]
peak_steps = ['@505K', '@35K', '@25K']
colors = ['#0072B2', '#E69F00', '#D55E00']

pct_dt2 = -(1 - peak_returns[1] / peak_returns[0]) * 100
pct_dt4 = -(1 - peak_returns[2] / peak_returns[0]) * 100

fig, ax = plt.subplots(figsize=(5, 4))

x = np.arange(len(categories))
bars = ax.bar(x, peak_returns, width=0.55, color=colors, edgecolor='white', linewidth=0.8, zorder=3,
              yerr=yerr, capsize=4, error_kw=dict(lw=1.5, capthick=1.2, color='#333333'))

ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel('Best Eval Return')
ax.set_title('Performance Degrades Monotonically with dt')
ax.set_ylim(0, 1200)
ax.yaxis.grid(True, alpha=0.3, linestyle='--', zorder=0)

for i, (bar, val, step) in enumerate(zip(bars, peak_returns, peak_steps)):
    label = f'{val:.1f}' if i > 0 else f'{val:.2f}'
    offset = baseline_std + 15 if i == 0 else 15
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + offset,
            label, ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2,
            step, ha='center', va='center', fontsize=9, color='white', fontweight='bold')

ax.annotate(f'{pct_dt2:.0f}%',
            xy=(1, peak_returns[1] + 50), xytext=(0.5, 1100),
            arrowprops=dict(arrowstyle='->', color='#555555', lw=1.5, linestyle='--',
                            connectionstyle='arc3,rad=-0.2'),
            fontsize=10, fontweight='bold', color='#555555', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#555555', alpha=0.9))

ax.annotate(f'{pct_dt4:.0f}%',
            xy=(2, peak_returns[2] + 50), xytext=(1.5, 1100),
            arrowprops=dict(arrowstyle='->', color='#D55E00', lw=1.5, linestyle='--',
                            connectionstyle='arc3,rad=-0.2'),
            fontsize=10, fontweight='bold', color='#D55E00', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#D55E00', alpha=0.9))

import os
out_dir = os.environ.get('FIG_OUT_DIR',
    '/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/paper')
os.makedirs(out_dir, exist_ok=True)
fig.savefig(f'{out_dir}/fig5_dt_amplification.pdf')
fig.savefig(f'{out_dir}/fig5_dt_amplification.png')
plt.close()
print(f'Saved to {out_dir}/fig5_dt_amplification.pdf/.png')
print(f'Baseline: {baseline_mean:.2f} ± {baseline_std:.2f} (N=2, seeds: {baseline_seeds})')
print(f'dt=2: 485.3 (N=1), dt=4: 176.9 (N=1)')
print(f'Drops: dt=2 {pct_dt2:.1f}%, dt=4 {pct_dt4:.1f}%')
