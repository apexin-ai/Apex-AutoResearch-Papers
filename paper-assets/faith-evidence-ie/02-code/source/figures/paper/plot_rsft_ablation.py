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

configs = ['SFT baseline', 'RSFT random k=1', 'RSFT CED k=3', 'RSFT flat-NLI', 'RSFT CED k=1', 'SFT no-evidence']
values = [40.49, 41.98, 44.54, 45.61, 45.63, 48.76]

colors = []
hatches = []
edgecolors = []
linewidths = []
for c in configs:
    if c in ('SFT baseline', 'SFT no-evidence'):
        colors.append('#999999')
    elif c == 'RSFT CED k=1':
        colors.append('#005580')
    else:
        colors.append('#0072B2')

    if c == 'SFT no-evidence':
        hatches.append('///')
    else:
        hatches.append('')

    if c == 'RSFT CED k=1':
        edgecolors.append('#002233')
        linewidths.append(1.5)
    else:
        edgecolors.append('white')
        linewidths.append(0.5)

fig, ax = plt.subplots(figsize=(5.5, 3.2))

y = np.arange(len(configs))
bars = ax.barh(y, values, height=0.6, color=colors, edgecolor=edgecolors)

for i, (bar, h, lw) in enumerate(zip(bars, hatches, linewidths)):
    bar.set_linewidth(lw)
    bar.set_edgecolor(edgecolors[i])
    if h:
        bar.set_hatch(h)
        bar.set_edgecolor('#666666')

for i, (bar, v) in enumerate(zip(bars, values)):
    ax.text(v + 0.15, bar.get_y() + bar.get_height()/2, f'{v:.2f}', ha='left', va='center', fontsize=8)

ax.set_yticks(y)
ax.set_yticklabels(configs)
ax.set_xlabel('Rel-F1')
ax.set_xlim(38, 51)

fig.savefig('fig_rsft_ablation.pdf')
fig.savefig('fig_rsft_ablation.png')
plt.close()
print('Done: fig_rsft_ablation.pdf/png')
