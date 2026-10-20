"""Generate variance decomposition figure (horizontal stacked bar with actionable/residual split)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
})

components = [
    ('Clause wording (within-type)', 22.0, '#2166ac'),
    ('Condition (ambig vs unamb)', 15.8, '#4393c3'),
    ('Model', 1.0, '#92c5de'),
    ('Type (between)', 0.4, '#d1e5f0'),
    ('Residual (stochastic)', 15.2, '#bdbdbd'),
    ('Residual (systematic)', 45.6, '#737373'),
]

labels = [c[0] for c in components]
values = [c[1] for c in components]
colors = [c[2] for c in components]

fig, ax = plt.subplots(figsize=(3.3, 2.2))

left = 0
bars = []
for i, (label, val, color) in enumerate(components):
    bar = ax.barh(0, val, left=left, height=0.5, color=color, edgecolor='white', linewidth=0.5)
    bars.append(bar)
    cx = left + val / 2
    if val >= 10:
        ax.text(cx, 0, f'{val}%', ha='center', va='center', fontsize=6.5, fontweight='bold', color='white')
    left += val

# Annotate small segments with callout lines above the bar
model_cx = 22.0 + 15.8 + 0.5
ax.annotate('1.0%', xy=(model_cx, 0.28), xytext=(model_cx - 5, 0.68),
            fontsize=5.5, ha='center', va='bottom', color='#555555',
            arrowprops=dict(arrowstyle='-', color='#999999', lw=0.5))
type_cx = 22.0 + 15.8 + 1.0 + 0.2
ax.annotate('0.4%', xy=(type_cx, 0.28), xytext=(type_cx + 5, 0.68),
            fontsize=5.5, ha='center', va='bottom', color='#555555',
            arrowprops=dict(arrowstyle='-', color='#999999', lw=0.5))

actionable_end = 22.0 + 15.8 + 1.0 + 0.4  # 39.2%
ax.axvline(x=actionable_end, color='#333333', linestyle='--', linewidth=0.8, ymin=0.08, ymax=0.92)

ax.annotate('Actionable 39.2%', xy=(actionable_end / 2, -0.42),
            fontsize=6.5, ha='center', va='top', color='#2166ac', fontweight='bold')
ax.annotate('Residual 60.8%', xy=(actionable_end + (100 - actionable_end) / 2, -0.42),
            fontsize=6.5, ha='center', va='top', color='#737373', fontweight='bold')

ax.set_xlim(0, 100)
ax.set_ylim(-0.75, 0.95)
ax.set_xlabel('Proportion of variance (%)', fontsize=7)
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

legend_patches = [mpatches.Patch(facecolor=colors[i], edgecolor='white', label=labels[i])
                  for i in range(len(components))]
ax.legend(handles=legend_patches, loc='upper center', bbox_to_anchor=(0.5, 1.65),
          ncol=3, fontsize=5.5, frameon=False, handlelength=1.0, handletextpad=0.3, columnspacing=0.8)

plt.savefig('figures/fig_variance_decomposition.pdf', format='pdf')
plt.savefig('figures/fig_variance_decomposition.png', format='png')
print('Saved figures/fig_variance_decomposition.pdf')
