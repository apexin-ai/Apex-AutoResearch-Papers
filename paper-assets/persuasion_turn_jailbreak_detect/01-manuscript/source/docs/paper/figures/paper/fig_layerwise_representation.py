import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 8,
    'axes.labelsize': 8,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'axes.linewidth': 0.6,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.5,
    'lines.markersize': 4,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

with open('/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/exp50_layerwise_results.json') as f:
    data = json.load(f)

variants = data['variants']
num_layers = 13
layers = list(range(num_layers))

COLORS = {
    '9-class':   '#2166ac',
    'scrambled':  '#67a9cf',
    'JB-MLM':    '#ef8a62',
    'vanilla':   '#5e4fa2',
}
MARKERS = {
    '9-class':   'o',
    'scrambled':  's',
    'JB-MLM':    '^',
    'vanilla':   'D',
}
ORDER = ['9-class', 'scrambled', 'JB-MLM', 'vanilla']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 2.4))

for name in ORDER:
    v = variants[name]
    pr_vals = [v[f'layer_{l}']['pr'] for l in layers]
    fisher_vals = [v[f'layer_{l}']['fisher'] for l in layers]

    ax1.plot(layers, pr_vals, color=COLORS[name], marker=MARKERS[name],
             label=name, markersize=4, markeredgecolor='white',
             markeredgewidth=0.3, zorder=3)
    ax2.plot(layers, fisher_vals, color=COLORS[name], marker=MARKERS[name],
             label=name, markersize=4, markeredgecolor='white',
             markeredgewidth=0.3, zorder=3)

boundary = 7.5
for ax in [ax1, ax2]:
    ax.axvspan(0, boundary, alpha=0.04, color='#2166ac', zorder=0)
    ax.axvspan(boundary, 12, alpha=0.04, color='#ef8a62', zorder=0)
    ax.set_xlabel('Layer')
    ax.set_xticks(layers)
    ax.set_axisbelow(True)

ax1.set_ylabel('Participation Ratio')
ax1.set_title('(a) Participation Ratio', fontsize=9, fontweight='semibold', pad=4)
ax1.text(3, 11.5, 'Early layers\n(label-independent)', fontsize=6, color='#666666',
         ha='center', va='top', style='italic')
ax1.text(10, 11.5, 'Late layers\n(class.-specific)', fontsize=6, color='#666666',
         ha='center', va='top', style='italic')

ax2.set_ylabel('Fisher Ratio')
ax2.set_title('(b) Fisher Ratio', fontsize=9, fontweight='semibold', pad=4)
ax2.text(3, 11.5, 'Early layers\n(label-independent)', fontsize=6, color='#666666',
         ha='center', va='top', style='italic')
ax2.text(10, 11.5, 'Late layers\n(class.-specific)', fontsize=6, color='#666666',
         ha='center', va='top', style='italic')

ax2.annotate('15× vanilla', xy=(10, 10.918), xytext=(7, 10.5),
             fontsize=6.5, color='#2166ac', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='#2166ac', lw=0.8),
             bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                       edgecolor='#2166ac', linewidth=0.5))

ax1.legend(loc='upper left', framealpha=0.95, edgecolor='#cccccc',
           borderpad=0.3, handlelength=1.5, labelspacing=0.3,
           ncol=2, columnspacing=0.8)

plt.tight_layout(w_pad=1.5)

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig_layerwise_representation'
fig.savefig(out_base + '.pdf', bbox_inches='tight', pad_inches=0.05)
fig.savefig(out_base + '.png', bbox_inches='tight', pad_inches=0.05, dpi=300)
plt.close()
print('OK')
