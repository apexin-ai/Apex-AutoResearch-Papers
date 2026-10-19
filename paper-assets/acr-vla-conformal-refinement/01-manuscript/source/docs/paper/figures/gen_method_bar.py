"""Figure 4: Method comparison bar chart across 4 LIBERO suites."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 11,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
})

suites = ['Spatial', 'Object', 'Goal', 'Long']
methods = ['VLA-only ($K{=}1$)', 'CRM always-on ($K{=}2$)', r'CRM $\tau$-gated ($K{=}2$)']

means = {
    'VLA-only': [79.3, 77.7, 83.7, 58.0],
    'CRM':      [78.0, 73.0, 80.0, 43.2],
    'ACR-VLA':  [80.8, 77.8, 85.0, 57.7],
}
stds = {
    'VLA-only': [0.8, 1.3, 1.3, 1.5],
    'CRM':      [1.7, 1.8, 0.5, 2.3],
    'ACR-VLA':  [1.1, 2.1, 1.3, 1.5],
}
trigger_rates = [20, 4, 8, 4]

colors = {
    'VLA-only': '#7F7F7F',
    'CRM':      '#A63D40',
    'ACR-VLA':  '#1B3A5C',
}
text_colors = {
    'VLA-only': '#7F7F7F',
    'CRM':      '#A63D40',
    'ACR-VLA':  '#1B3A5C',
}

x = np.arange(len(suites))
width = 0.24
offsets = [-width, 0, width]
keys = ['VLA-only', 'CRM', 'ACR-VLA']

fig, ax = plt.subplots(figsize=(7.5, 4.0))

bars_all = {}
for i, key in enumerate(keys):
    bars = ax.bar(
        x + offsets[i], means[key], width,
        yerr=stds[key],
        color=colors[key],
        edgecolor='white',
        linewidth=0.6,
        capsize=3,
        error_kw={'linewidth': 0.8, 'capthick': 0.8},
        zorder=3,
        label=methods[i],
    )
    bars_all[key] = bars

ax.set_ylabel('Success Rate (%)')
ax.set_xticks(x)
ax.set_xticklabels(suites)
ax.set_ylim(35, 93)

ax.yaxis.grid(True, alpha=0.25, linewidth=0.5, color='#cccccc', zorder=0)
ax.set_axisbelow(True)

for i in range(len(suites)):
    vla_val = means['VLA-only'][i]
    crm_val = means['CRM'][i]
    delta = crm_val - vla_val
    bar_x = x[i] + offsets[1]
    bar_top = crm_val + stds['CRM'][i] + 1.2
    t = ax.text(bar_x, bar_top, f'{delta:+.1f}',
                ha='center', va='bottom', fontsize=9.5,
                color=text_colors['CRM'], fontweight='bold')
    t.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

for i in range(len(suites)):
    bar_x = x[i] + offsets[2]
    bar_top = means['ACR-VLA'][i] + stds['ACR-VLA'][i] + 1.2
    t = ax.text(bar_x, bar_top, f'{trigger_rates[i]}% trig.',
                ha='center', va='bottom', fontsize=9,
                color=text_colors['ACR-VLA'], fontstyle='italic')
    t.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

ax.legend(loc='upper center', ncol=3, frameon=True, framealpha=0.9,
          edgecolor='#cccccc', fancybox=False,
          bbox_to_anchor=(0.5, 1.02), borderaxespad=0)

plt.tight_layout()

outdir = os.path.dirname(os.path.abspath(__file__))
for ext in ['pdf', 'png']:
    outpath = os.path.join(outdir, f'fig_method_bar.{ext}')
    fig.savefig(outpath)
    print(f'Saved: {outpath}')

plt.close()
