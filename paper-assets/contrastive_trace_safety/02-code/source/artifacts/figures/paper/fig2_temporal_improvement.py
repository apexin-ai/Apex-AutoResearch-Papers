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
})

COLOR_HS = '#0072B2'
COLOR_TEXT = '#E69F00'

categories = ['Static\n(W=1)', 'W=5', 'W=10', 'W=15']
hs_values = [46.5, 65.1, 65.1, 76.7]
text_values = [60.5, np.nan, np.nan, 65.1]

x = np.arange(len(categories))
width = 0.32

fig, ax = plt.subplots(figsize=(5.5, 4.1))

bars_hs = ax.bar(x - width/2, hs_values, width, label='Hidden-State Probe',
                 color=COLOR_HS, edgecolor='white', linewidth=0.5)

text_mask = [not np.isnan(v) for v in text_values]
text_x = x[text_mask]
text_y = [text_values[i] for i in range(len(text_values)) if text_mask[i]]
bars_text = ax.bar(text_x + width/2, text_y, width, label='Text Probe',
                   color=COLOR_TEXT, edgecolor='white', linewidth=0.5)

ax.set_ylabel('Coverage (%)')
ax.set_xlabel('Temporal Window Size')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylim(30, 86)
ax.set_yticks(np.arange(30, 90, 10))

for bar in bars_hs:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 0.6,
            f'{h:.1f}', ha='center', va='bottom', fontsize=8.5, color=COLOR_HS,
            fontweight='bold')

for bar in bars_text:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 0.6,
            f'{h:.1f}', ha='center', va='bottom', fontsize=8.5, color=COLOR_TEXT,
            fontweight='bold')

# Vertical double-arrow on the right side of the W=15 group
arrow_x = x[3] + width/2 + 0.22
ax.annotate('', xy=(arrow_x, 76.7), xytext=(arrow_x, 46.5),
            arrowprops=dict(arrowstyle='<->', color='#444444', lw=1.5))
ax.text(arrow_x + 0.08, (46.5 + 76.7) / 2, '+30.2pp',
        fontsize=10, fontweight='bold', color='#333333',
        ha='left', va='center', rotation=90)

ax.axhline(y=46.5, color=COLOR_HS, linestyle=':', alpha=0.25, linewidth=0.8)
ax.axhline(y=76.7, color=COLOR_HS, linestyle=':', alpha=0.25, linewidth=0.8)

ax.set_title('Effect of Temporal Context on Detection Coverage (r1-8b)', pad=10)

ax.text(0.98, 0.02, 'Full multi-model results pending exp-007',
        transform=ax.transAxes, fontsize=7.5, color='#999999',
        ha='right', va='bottom', style='italic')

ax.legend(loc='upper left', framealpha=0.95, edgecolor='none',
          bbox_to_anchor=(0.0, 1.0))
ax.yaxis.grid(True, alpha=0.15, linewidth=0.5)
ax.set_axisbelow(True)

fig.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper'
fig.savefig(f'{outdir}/fig2_temporal_improvement.pdf')
fig.savefig(f'{outdir}/fig2_temporal_improvement.png', dpi=300)
plt.close()
print("Done.")
