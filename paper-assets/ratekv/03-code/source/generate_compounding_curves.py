"""Generate cross-architecture compounding curves figure for RateKV paper."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

models = [
    {
        'name': 'Qwen2.5-7B',
        'pattern': 'Spread',
        'k': [0, 2, 4, 8, 16, 32, 64, 128, 256],
        'ppl': [9.8106, 9.83, 9.85, 10.0474, 10.40, 11.63, 23.2176, 98.75, 98.7523],
        'color': '#D55E00',
        'marker': '^',
        'conc': 0.61,
    },
    {
        'name': 'Llama-3.1-8B',
        'pattern': 'Spike',
        'k': [0, 2, 4, 8, 16, 32, 64, 128, 256],
        'ppl': [8.09, 8.12, 8.18, 8.23, 8.44, 9.05, 11.99, 40.21, 1519.19],
        'color': '#0072B2',
        'marker': 'o',
        'conc': 0.57,
    },
    {
        'name': 'Mistral-7B-v0.3',
        'pattern': 'Flat',
        'k': [0, 2, 4, 8, 16, 32, 64, 128, 256],
        'ppl': [7.04, 7.04, 7.05, 7.06, 7.11, 7.24, 7.77, 10.47, 45.28],
        'color': '#009E73',
        'marker': 's',
        'conc': 0.24,
    },
]

fig, ax = plt.subplots(figsize=(7, 4.5))

for m in models:
    k_arr = np.array(m['k'])
    ppl_arr = np.array(m['ppl'])
    label = f"{m['name']} ({m['pattern']}, $c$ = {m['conc']:.2f})"
    ms = m.get('markersize', 6)
    ax.plot(k_arr, ppl_arr, marker=m['marker'], color=m['color'],
            markersize=ms, label=label, zorder=3, markeredgewidth=0.5,
            markeredgecolor='white')

ax.set_xscale('symlog', linthresh=1)
ax.set_yscale('log')

xticks = [0, 2, 8, 32, 64, 128, 256]
ax.set_xticks(xticks)
ax.set_xticklabels([str(x) for x in xticks])
ax.minorticks_off()

ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax.yaxis.get_major_formatter().set_scientific(False)
yticks = [7, 10, 20, 50, 100, 200, 500, 1500]
ax.set_yticks(yticks)
ax.set_yticklabels([str(y) for y in yticks])

ax.axhline(y=100, color='#e31a1c', linestyle=':', linewidth=0.8, alpha=0.5, zorder=1)
ax.text(260, 115, 'catastrophic', fontsize=8, color='#e31a1c',
        ha='right', va='bottom', style='italic')

ax.set_xlabel('Number of 2-bit heads ($k$)')
ax.set_ylabel('Perplexity')
ax.legend(loc='upper left', frameon=True, fancybox=False,
          edgecolor='#cccccc')

ax.set_ylim(5, 2000)

OUT = '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/figures'
for fmt in ['pdf', 'png']:
    fig.savefig(f'{OUT}/fig_compounding_curves.{fmt}', bbox_inches='tight', dpi=300)
plt.close(fig)
print(f'Saved to {OUT}/fig_compounding_curves.pdf')
