import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.labelsize': 11,
    'xtick.labelsize': 9.5,
    'ytick.labelsize': 9.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

models = ['1.7B', '4B', '8B', 'LLaMA-8B']
sft_std = [2.79, 3.80, 3.23, 2.92]
rsft_std = [0.09, 0.51, 0.50, 0.64]
compression = ['32.6×', '7.5×', '6.5×', '4.6×']

x = np.arange(len(models))
width = 0.35

fig, ax = plt.subplots(figsize=(5.5, 3.5))

bars_sft = ax.bar(x - width/2, sft_std, width, label='SFT', color='#5B9BD5')
bars_rsft = ax.bar(x + width/2, rsft_std, width, label='RSFT', color='#E8A838')

for i, (bar_s, bar_r, comp) in enumerate(zip(bars_sft, bars_rsft, compression)):
    mid_x = (bar_s.get_x() + bar_s.get_width()/2 + bar_r.get_x() + bar_r.get_width()/2) / 2
    top_y = max(bar_s.get_height(), bar_r.get_height())
    ax.text(mid_x, top_y + 0.15, comp, ha='center', va='bottom', fontsize=8, fontstyle='italic')

ax.set_ylabel('Ign-F1 Std (pp)')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend(loc='upper right', frameon=False)
ax.set_ylim(0, max(sft_std) * 1.25)

fig.savefig('fig_variance_compression.pdf')
fig.savefig('fig_variance_compression.png')
plt.close()
print('Done: fig_variance_compression.pdf/png')
