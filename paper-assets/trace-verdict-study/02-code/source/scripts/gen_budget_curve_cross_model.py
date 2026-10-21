"""Generate cross-model tail-truncation budget curve figure."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'legend.fontsize': 7.5,
    'xtick.labelsize': 8.5,
    'ytick.labelsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'text.usetex': False,
})

budgets = [256, 384, 512, 1024]
budget_labels = ['256', '384', '512', '1024']

models = {
    'Qwen-7B': {
        'tail': [78.82, 79.92, 93.61, 96.47],
        'exc_only': 99.83,
        'no_trace': 75.13,
        'color': '#0072B2',
        'marker': 'o',
    },
    'DeepSeek-6.7B': {
        'tail': [74.37, 82.86, 93.95, 95.04],
        'exc_only': 99.33,
        'no_trace': 73.36,
        'color': '#E69F00',
        'marker': 's',
    },
    'CodeLlama-13B': {
        'tail': [77.73, 80.59, 98.24, 98.24],
        'exc_only': 99.89,
        'no_trace': 76.47,
        'color': '#009E73',
        'marker': '^',
    },
    'Qwen-1.5B': {
        'tail': [72.61, 73.61, 95.63, 97.56],
        'exc_only': 99.83,
        'no_trace': 67.31,
        'color': '#56B4E9',
        'marker': 'D',
    },
}

fig, ax = plt.subplots(figsize=(3.4, 2.5))

x = np.arange(len(budgets))

for name, m in models.items():
    ax.plot(x, m['tail'], marker=m['marker'], color=m['color'],
            linewidth=1.4, markersize=4.5, label=name, zorder=3)

exc_min = min(m['exc_only'] for m in models.values())
exc_max = max(m['exc_only'] for m in models.values())
ax.axhspan(exc_min, exc_max, alpha=0.08, color='#0072B2', zorder=1)
ax.axhline(y=exc_min, color='#0072B2', linestyle='--', linewidth=0.7, alpha=0.6, zorder=2)
ax.text(-0.15, exc_max + 0.3, 'exception_only',
        fontsize=6.5, color='#0072B2', ha='left', va='bottom')

nt_min = min(m['no_trace'] for m in models.values())
nt_max = max(m['no_trace'] for m in models.values())
ax.axhspan(nt_min, nt_max, alpha=0.06, color='#999999', zorder=1)
ax.axhline(y=nt_max, color='#999999', linestyle=':', linewidth=0.7, alpha=0.6, zorder=2)
ax.text(-0.15, nt_min - 0.5, 'no_trace',
        fontsize=6.5, color='#777777', ha='left', va='top')

ax.axvspan(1, 2, alpha=0.05, color='#FF7F0E', zorder=0)
ax.annotate('transition\nzone', xy=(1.5, 65), fontsize=6.5, color='#CC6600',
            ha='center', va='center', fontstyle='italic')

ax.set_xticks(x)
ax.set_xticklabels(budget_labels)
ax.set_xlabel('Tail token budget')
ax.set_ylabel('Accuracy (%)')
ax.set_ylim(63, 102)
ax.set_xlim(-0.25, len(budgets) - 0.75)

ax.legend(loc='lower right', frameon=False,
          borderpad=0.3, handlelength=1.3, handletextpad=0.3)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.15, linewidth=0.5)

out = '/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/figures/paper/budget_curve.pdf'
fig.savefig(out)
out_png = out.replace('.pdf', '.png')
fig.savefig(out_png)
print(f'Saved: {out}')
print(f'Saved: {out_png}')
plt.close()
