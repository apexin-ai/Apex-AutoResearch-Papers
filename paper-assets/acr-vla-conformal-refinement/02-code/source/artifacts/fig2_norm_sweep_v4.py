import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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

obs_only_data = {
    0.03: [14.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 13.0, 17.0, 17.0, 16.0, 11.5, 14.0],
    0.05: [14.0, 12.0, 14.0, 13.0, 13.0, 15.0, 13.0, 15.0, 16.0, 15.0, 15.0, 14.0, 11.0, 10.0, 11.0, 15.0],
    0.10: [19.0, 16.0, 17.0, 18.0, 17.0, 13.0, 16.0, 14.0, 11.0, 15.0, 19.0, 15.0, 19.0, 15.0, 15.0, 15.0, 16.0, 13.0, 13.5, 14.0],
    0.20: [20.0, 16.0, 16.0, 16.0, 15.0, 20.0, 18.0, 14.0, 18.0, 17.0, 15.0, 16.0],
}

vla_only_mean = 10.8

eps_values = sorted(obs_only_data.keys())
means = [np.mean(obs_only_data[e]) for e in eps_values]
sems = [np.std(obs_only_data[e], ddof=1) / np.sqrt(len(obs_only_data[e])) for e in eps_values]
ns = [len(obs_only_data[e]) for e in eps_values]

x_labels = [str(e) for e in eps_values]
x_pos = np.arange(len(eps_values))

fig, ax = plt.subplots(figsize=(5, 3.5))

bars = ax.bar(x_pos, means, width=0.55, color='#0072B2', alpha=0.85,
              edgecolor='#0072B2', linewidth=0.8, zorder=3)

ax.errorbar(x_pos, means, yerr=sems, fmt='none', ecolor='black',
            capsize=4, linewidth=1.2, capthick=1.2, zorder=4)

ax.axhline(y=vla_only_mean, color='#888888', linestyle='--', linewidth=1.5,
           label=f'VLA-only ({vla_only_mean}%)', zorder=2)

for i, n in enumerate(ns):
    ax.text(x_pos[i], means[i] + sems[i] + 0.4, f'n={n}',
            ha='center', va='bottom', fontsize=9, color='#444444')

ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels)
ax.set_xlabel('Maximum Correction Norm (ε)')
ax.set_ylabel('Success Rate (%)')
ax.set_ylim(5, 25)
ax.yaxis.set_major_locator(plt.MultipleLocator(5))
ax.grid(axis='y', alpha=0.3, zorder=0)
ax.legend(loc='lower right', framealpha=0.9)

plt.tight_layout()

out_dir = '/root/acr-vla-conformal-refinement/artifacts'
fig.savefig(f'{out_dir}/fig2_norm_sweep_v4.pdf')
fig.savefig(f'{out_dir}/fig2_norm_sweep_v4.png')
plt.close()

print("Saved fig2_norm_sweep_v4.pdf and .png")
for e, m, s, n in zip(eps_values, means, sems, ns):
    print(f"  eps={e}: mean={m:.1f}%, SEM={s:.1f}%, n={n}")
print(f"  VLA-only baseline: {vla_only_mean}%")
print(f"  Caption: n={'/'.join(str(n) for n in ns)} for eps={'/'.join(str(e) for e in eps_values)}")
