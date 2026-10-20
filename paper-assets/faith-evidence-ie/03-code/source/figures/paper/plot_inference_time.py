import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif'],
    'mathtext.fontset': 'stix',
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

models = ['1.7B', '4B', '8B', '14B']
with_evi = [6424, 8887, 10486, 18011]
no_evi = [7438, 7606, 10901, 14498]
overhead = ['-13.6%', '+16.8%', '-3.8%', '+24.2%']
overhead_vals = [-13.6, 16.8, -3.8, 24.2]

x = np.arange(len(models))
width = 0.35

fig, ax = plt.subplots(figsize=(5.5, 3.5))

bars_w = ax.bar(x - width/2, with_evi, width, label='With evidence', color='#0072B2')
bars_n = ax.bar(x + width/2, no_evi, width, label='No evidence', color='#999999')

for i, (bw, bn, ov, ov_val) in enumerate(zip(bars_w, bars_n, overhead, overhead_vals)):
    top_y = max(bw.get_height(), bn.get_height())
    mid_x = (bw.get_x() + bw.get_width()/2 + bn.get_x() + bn.get_width()/2) / 2
    color = '#009E73' if ov_val < 0 else '#D55E00'
    ax.text(mid_x, top_y + 300, ov, ha='center', va='bottom', fontsize=8, color=color)

ax.set_ylabel('Wall-clock Time (seconds)')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend(loc='upper left', frameon=False)
ax.set_ylim(0, max(max(with_evi), max(no_evi)) * 1.18)

fig.savefig('fig_inference_time.pdf')
fig.savefig('fig_inference_time.png')
plt.close()
print('Done: fig_inference_time.pdf/png')
