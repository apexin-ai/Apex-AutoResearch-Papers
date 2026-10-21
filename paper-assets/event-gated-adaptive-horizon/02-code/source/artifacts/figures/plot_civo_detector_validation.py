import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

plt.rcParams.update({
    'font.size': 9,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'font.family': 'sans-serif',
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
})

with open('/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/analysis/detector_formal_validation_v3.json') as f:
    data = json.load(f)

results = data['results']

exps = [
    ('exp_008d_s0',              'solid', '#D55E00', 1.5, 'exp_008d_s0 (TP)'),
    ('exp_010b_cheetah',         'solid', '#E69F00', 1.5, 'exp_010b_cheetah (TP)'),
    ('exp_008d_s3',              'solid', '#CC79A7', 1.5, 'exp_008d_s3 (TP)'),
    ('exp_009c_008f_s2',         'dashed', '#0072B2', 1.5, 'exp_009c_008f_s2 (FP)'),
    ('exp_009a_baseline_walker_s2', 'dashed', '#56B4E9', 1.5, 'exp_009a_baseline (FP)'),
    ('exp_009b_008d_walker_s2',  '-.', '#999999', 1.0, '009b s2 (TN, self-corr.)'),
]

YMAX = 1.85

fig, ax = plt.subplots(figsize=(6, 3.5))

for exp_id, ls, color, lw, label in exps:
    exp = results[exp_id]
    ckpts = exp['checkpoints']
    steps = [c['step'] / 1000 for c in ckpts]
    ve = [c['ve_ratio'] for c in ckpts]

    ve_clipped = [min(v, YMAX - 0.02) for v in ve]
    ax.plot(steps, ve_clipped, linestyle=ls, color=color, linewidth=lw, label=label, zorder=3)

    trigger = exp['trigger_step']
    if trigger is not None:
        trigger_k = trigger / 1000
        for c in ckpts:
            if c['step'] == trigger:
                trigger_ve = c['ve_ratio']
                break
        plot_ve = min(trigger_ve, YMAX - 0.05)
        ax.plot(trigger_k, plot_ve, marker='*', markersize=13, color=color,
                markeredgecolor='black', markeredgewidth=0.6, zorder=5)
        if trigger_ve > YMAX:
            ax.annotate(f'{trigger_ve:.1f}', xy=(trigger_k, plot_ve),
                        xytext=(trigger_k + 2, plot_ve - 0.15),
                        fontsize=7, color=color, fontweight='bold',
                        arrowprops=dict(arrowstyle='->', color=color, lw=0.8))

ax.axhline(y=0.49, color='#555555', linestyle=':', linewidth=1.0, zorder=2)
ax.text(2, 0.49 + 0.03, r'$\tau_{\mathrm{mag}} = 0.49$', fontsize=8, color='#555555',
        ha='left', va='bottom')

ax.axvline(x=70, color='#888888', linestyle='--', linewidth=0.8, zorder=2)
ax.text(71, YMAX * 0.95, 'Timing\nguideline', fontsize=7.5, color='#888888',
        ha='left', va='top')

ax.fill_betweenx([0, YMAX], 0, 70, color='#e8f5e9', alpha=0.25, zorder=0)
ax.fill_betweenx([0, YMAX], 70, 110, color='#fff3e0', alpha=0.25, zorder=0)
ax.text(35, YMAX * 0.03, 'High confidence', fontsize=7.5, color='#555555',
        ha='center', va='bottom', style='italic')
ax.text(90, YMAX * 0.03, 'Inspect', fontsize=7.5, color='#555555',
        ha='center', va='bottom', style='italic')

star_handle = ax.plot([], [], marker='*', markersize=10, color='gray',
                      markeredgecolor='black', markeredgewidth=0.5,
                      linestyle='None', label='Alert trigger')[0]

ax.set_xlabel('Training Step (K)')
ax.set_ylabel(r'V/E Ratio ($r_t$)')
ax.set_xlim(0, 110)
ax.set_ylim(-0.03, YMAX)

ax.xaxis.set_major_locator(mticker.MultipleLocator(10))
ax.yaxis.set_major_locator(mticker.MultipleLocator(0.2))

ax.grid(True, alpha=0.2, color='#cccccc', linewidth=0.4)

legend = ax.legend(loc='upper left', framealpha=0.92, edgecolor='#cccccc',
                   ncol=2, columnspacing=1.0, handlelength=2.2,
                   borderpad=0.4, labelspacing=0.35)

plt.tight_layout(pad=0.4)

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/civo_detector_validation'
fig.savefig(out_base + '.pdf', bbox_inches='tight', dpi=300)
fig.savefig(out_base + '.png', bbox_inches='tight', dpi=300)
plt.close()
print('Done')
