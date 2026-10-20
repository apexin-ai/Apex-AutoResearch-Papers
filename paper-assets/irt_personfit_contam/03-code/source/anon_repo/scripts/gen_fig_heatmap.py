import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from pathlib import Path

matplotlib.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'text.usetex': False,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.linewidth': 0.6,
})

models = ['Qwen-2.5-7B', 'Llama-3.1-8B', 'Mistral-7B']
columns = [
    ('MMLU\n5%', 'MMLU'),
    ('MMLU\n15%', 'MMLU'),
    ('MMLU\n25%', 'MMLU'),
    ('MMLU\n50%', 'MMLU'),
    ('ARC-C\n15%', 'ARC-C'),
    ('ARC-C\n50%', 'ARC-C'),
]

d_vals = np.array([
    [4.15, 6.57, 8.22, 1.90, 3.16, 5.30],
    [np.nan, 2.11, 1.99, 2.33, np.nan, np.nan],
    [np.nan, 3.37, np.nan, 3.50, np.nan, np.nan],
])

ci_text = [
    ['[2.7, 9.9]', '[4.5, 15.2]', '[5.7, 18.9]', '[1.0, 5.0]', '[2.0, 9.5]', '[3.6, 15.2]'],
    ['', '[1.4, 4.8]', '[1.3, 4.4]', '[1.6, 5.1]', '', ''],
    ['', '(±0.68)', '', '[2.1, 9.4]', '', ''],
]

n_rows, n_cols = d_vals.shape
d_display = np.where(np.isnan(d_vals), 0, d_vals)
vmax = 9.0

cmap = plt.cm.Blues
norm = mcolors.Normalize(vmin=0, vmax=vmax)

fig, ax = plt.subplots(figsize=(8.5, 3.2))

im = ax.imshow(d_display, cmap=cmap, norm=norm, aspect='auto')

for i in range(n_rows):
    for j in range(n_cols):
        val = d_vals[i, j]
        if np.isnan(val):
            ax.text(j, i, '—', ha='center', va='center',
                    fontsize=12, color='#aaaaaa')
        else:
            r, g, b, _ = cmap(norm(val))
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            txt_color = 'white' if lum < 0.5 else 'black'

            ax.text(j, i - 0.12, f'|d| = {val:.2f}',
                    ha='center', va='center', fontsize=9.5,
                    color=txt_color, fontweight='bold')
            if ci_text[i][j]:
                ax.text(j, i + 0.18, ci_text[i][j],
                        ha='center', va='center', fontsize=6.5,
                        color=txt_color, alpha=0.85)

ax.set_xticks(range(n_cols))
ax.set_xticklabels([c[0] for c in columns], fontsize=8)
ax.xaxis.set_ticks_position('bottom')

ax.set_yticks(range(n_rows))
ax.set_yticklabels(models, fontsize=10)

for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(length=0)

# Group labels below column labels (x=data coords, y=axes fraction)
trans = ax.get_xaxis_transform()
ax.text(1.5, -0.18, 'MMLU (14,042 items)', ha='center', va='top',
        fontsize=9, fontweight='bold', transform=trans)
ax.text(4.5, -0.18, 'ARC-C (295 items)', ha='center', va='top',
        fontsize=9, fontweight='bold', transform=trans)

# Separator between MMLU and ARC-C
ax.axvline(x=3.5, color='white', linewidth=3)

# Colorbar
cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label("Cohen's |d|", fontsize=9)
cbar.ax.tick_params(labelsize=7)

# Footer
ax.text(0.5, -0.32,
        r'$n = 10$ seeds per model; 95% bootstrap CI (10,000 resamples). All CIs exclude zero.',
        transform=ax.transAxes, ha='center', fontsize=7.5,
        color='#666666', style='italic')

out = Path(__file__).resolve().parent
fig.savefig(out / 'fig_heatmap.pdf', format='pdf')
fig.savefig(out / 'fig_heatmap.png', format='png')
plt.close()
print("Done. Files saved.")
