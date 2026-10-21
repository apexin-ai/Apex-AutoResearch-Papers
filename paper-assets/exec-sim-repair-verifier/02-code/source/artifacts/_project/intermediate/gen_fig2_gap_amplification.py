import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

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
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'text.usetex': False,
})

labels = [
    "Function\n(4B, 5 seeds)",
    "Function\n(8B, 3 seeds)",
    "Repo-level\n(same-size 4B)",
]
gaps = [1.24, 2.43, 25.59]
errs = [0.86, 0.37, 0.0]
colors = ['#7FBFDF', '#0072B2', '#004C7A']

x = np.arange(len(labels))
bar_width = 0.52

fig = plt.figure(figsize=(5.5, 5.0))
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 2.2], hspace=0.08)

ax_top = fig.add_subplot(gs[0])
ax_bot = fig.add_subplot(gs[1])

for ax in [ax_top, ax_bot]:
    bars = ax.bar(x, gaps, bar_width, color=colors, edgecolor='white', linewidth=0.5, zorder=3)
    for i, (g, e) in enumerate(zip(gaps, errs)):
        if e > 0:
            ax.errorbar(x[i], g, yerr=e, fmt='none', ecolor='#333333',
                        capsize=4, capthick=1.2, elinewidth=1.2, zorder=4)

ax_top.set_ylim(22, 30)
ax_bot.set_ylim(0, 5.5)

ax_top.spines['bottom'].set_visible(False)
ax_bot.spines['top'].set_visible(False)
ax_top.tick_params(bottom=False, labelbottom=False)
ax_top.set_xticks([])

ax_bot.set_xticks(x)
ax_bot.set_xticklabels(labels)

# Break marks (left side only — right spine is hidden)
d = 0.012
kwargs = dict(transform=ax_top.transAxes, color='k', clip_on=False, linewidth=0.8)
ax_top.plot((-d, +d), (-d*3, +d*3), **kwargs)
kwargs.update(transform=ax_bot.transAxes)
ax_bot.plot((-d, +d), (1-d*3, 1+d*3), **kwargs)

# Value annotations
ax_bot.text(x[0], gaps[0] + errs[0] + 0.25, f'{gaps[0]:.2f} pp',
            ha='center', va='bottom', fontsize=9.5, fontweight='bold', color=colors[0])
ax_bot.text(x[1], gaps[1] + errs[1] + 0.25, f'{gaps[1]:.2f} pp',
            ha='center', va='bottom', fontsize=9.5, fontweight='bold', color=colors[1])
ax_top.text(x[2], gaps[2] + 0.5, f'{gaps[2]:.2f} pp (20.6x)',
            ha='center', va='bottom', fontsize=9.5, fontweight='bold', color=colors[2])

# Significance annotation for 8B
ax_bot.annotate('p = 0.008', xy=(x[1] + 0.05, gaps[1] + errs[1] + 0.12),
                xytext=(x[1] + 0.6, 4.3),
                fontsize=8.5, fontstyle='italic', color='#555555',
                arrowprops=dict(arrowstyle='->', color='#888888', lw=0.8),
                ha='center', va='bottom')

# CWM below majority annotation — place outside bar to the right
ax_top.annotate('CWM below majority\nvoting baseline (72.96%)',
                xy=(x[2] + bar_width/2, 24),
                xytext=(x[2] - 1.05, 28.5),
                fontsize=7.5, color='#8B0000', fontstyle='italic',
                linespacing=1.2, ha='center', va='top',
                arrowprops=dict(arrowstyle='->', color='#8B0000', lw=0.8))

# Y-axis label spanning both axes
fig.text(0.01, 0.5, 'CLS − CWM Accuracy Gap (pp)', va='center',
         rotation='vertical', fontsize=12)

ax_top.set_title('Gap Amplification: Function to Repo-Level', pad=10)

for ax in [ax_top, ax_bot]:
    ax.yaxis.grid(True, linestyle='--', alpha=0.3, zorder=0)
    ax.set_axisbelow(True)

ax_top.set_yticks([23, 25, 27, 29])
ax_bot.set_yticks([0, 1, 2, 3, 4, 5])

plt.subplots_adjust(left=0.14, right=0.95)

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts'
fig.savefig(f'{out_dir}/fig2_gap_amplification.pdf')
fig.savefig(f'{out_dir}/fig2_gap_amplification.png')
plt.close()

import os
for ext in ['pdf', 'png']:
    p = f'{out_dir}/fig2_gap_amplification.{ext}'
    sz = os.path.getsize(p)
    print(f'{p}: {sz} bytes')
    assert sz > 10000, f'{ext} too small: {sz}'
print('Done.')
