import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
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
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

data = {
    0.03: [0.14, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.13, 0.17, 0.17, 0.16],
    0.05: [0.14, 0.12, 0.13, 0.13, 0.15, 0.13, 0.15, 0.16, 0.15, 0.15, 0.14, 0.11, 0.15],
    0.10: [0.16, 0.17, 0.17, 0.13, 0.16, 0.14, 0.11, 0.15, 0.19, 0.15, 0.19, 0.15, 0.15, 0.15, 0.16, 0.13],
    0.20: [0.20, 0.14],
}
vla_only_mean = 0.105

eps_values = sorted(data.keys())
means = np.array([np.mean(data[e]) for e in eps_values]) * 100
sems = np.array([
    (np.std(data[e], ddof=1) / np.sqrt(len(data[e]))) if len(data[e]) > 1 else 0.0
    for e in eps_values
]) * 100
ns = [len(data[e]) for e in eps_values]

fig, ax = plt.subplots(figsize=(5, 3.5))

x_pos = np.arange(len(eps_values))
bar_color = '#0072B2'

bars = ax.bar(
    x_pos, means,
    width=0.6,
    color=bar_color,
    edgecolor='white',
    linewidth=0.5,
    zorder=3,
)

ax.errorbar(
    x_pos, means, yerr=sems,
    fmt='none', ecolor='black',
    elinewidth=1.2, capsize=4, capthick=1.2,
    zorder=4,
)

ax.axhline(
    y=vla_only_mean * 100,
    color='#888888',
    linestyle='--',
    linewidth=1.2,
    zorder=2,
)
ax.text(
    len(eps_values) - 0.5, vla_only_mean * 100 + 0.4,
    'VLA-only',
    ha='right', va='bottom',
    fontsize=9, color='#888888',
)

for i, (m, s, n) in enumerate(zip(means, sems, ns)):
    ax.text(
        x_pos[i], m + s + 0.6,
        f'n={n}',
        ha='center', va='bottom',
        fontsize=8.5, color='#444444',
    )

ax.set_xticks(x_pos)
ax.set_xticklabels([f'{e:g}' for e in eps_values])
ax.set_xlabel(r'Maximum Correction Norm ($\varepsilon$)')
ax.set_ylabel('Success Rate (%)')

ax.set_ylim(5, 25)
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.grid(True, alpha=0.3, zorder=0)
ax.set_axisbelow(True)

out_dir = '/root/acr-vla-conformal-refinement/artifacts'
fig.savefig(f'{out_dir}/fig2_norm_sweep.pdf')
fig.savefig(f'{out_dir}/fig2_norm_sweep.png')
plt.close()
print(f'Saved: {out_dir}/fig2_norm_sweep.pdf')
print(f'Saved: {out_dir}/fig2_norm_sweep.png')
print(f'means(%): {means.tolist()}')
print(f'sems(%):  {sems.tolist()}')
print(f'ns:       {ns}')
