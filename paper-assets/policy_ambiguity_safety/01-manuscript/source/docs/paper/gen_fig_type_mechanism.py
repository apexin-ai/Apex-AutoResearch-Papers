"""Generate type-mechanism confusion matrix heatmap."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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

# Raw counts from Appendix Table (type-mechanism confusion matrix, N=614)
# Rows: types, Cols: Structural misparse, Gap-filling, Boundary violation, Other
raw = {
    'Auth. scope':    [4, 28, 72, 0],
    'Cond. prec.':    [50, 10, 10, 22],
    'Coreferential':  [37, 29, 5, 8],
    'Incompleteness': [43, 70, 16, 5],
    'Lexical':        [42, 54, 10, 1],
    'Scopal':         [81, 4, 13, 0],
}

# Order: specification types first, then linguistic (matching paper taxonomy)
type_order_spec = ['Incompleteness', 'Auth. scope', 'Cond. prec.']
type_order_ling = ['Lexical', 'Scopal', 'Coreferential']
type_order = type_order_spec + type_order_ling

mechanisms = ['Structural\nmisparse', 'Information\ngap-filling', 'Boundary\nviolation']

# Convert to percentages (3 main mechanisms only, excluding "Other")
data = np.zeros((len(type_order), 3))
for i, t in enumerate(type_order):
    counts = raw[t][:3]  # exclude "Other"
    total = sum(raw[t])
    for j in range(3):
        data[i, j] = counts[j] / total * 100

fig, ax = plt.subplots(figsize=(3.3, 2.6))

cmap = plt.cm.Blues
im = ax.imshow(data, cmap=cmap, aspect='auto', vmin=0, vmax=85)

# Add text annotations
for i in range(len(type_order)):
    for j in range(3):
        val = data[i, j]
        color = 'white' if val > 50 else 'black'
        fontweight = 'bold' if val > 40 else 'normal'
        ax.text(j, i, f'{val:.0f}%', ha='center', va='center',
                fontsize=7, color=color, fontweight=fontweight)

ax.set_xticks(range(3))
ax.set_xticklabels(mechanisms, fontsize=6.5)
ax.set_yticks(range(len(type_order)))

# Style type labels with layer prefix
ylabels = []
for t in type_order:
    ylabels.append(t)
ax.set_yticklabels(ylabels, fontsize=6.5)

# Add layer grouping lines
ax.axhline(y=2.5, color='#666666', linewidth=1.0, linestyle='-')

# Layer labels on left
ax.text(-0.85, 1.0, 'Spec.', ha='center', va='center', fontsize=6, fontweight='bold',
        color='#8B4513', rotation=90, transform=ax.get_yaxis_transform())
ax.text(-0.85, 4.0, 'Ling.', ha='center', va='center', fontsize=6, fontweight='bold',
        color='#006400', rotation=90, transform=ax.get_yaxis_transform())

ax.tick_params(axis='both', which='both', length=0)
ax.set_xlabel('')
ax.set_ylabel('')

cbar = plt.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label('Traces (%)', fontsize=6.5)
cbar.ax.tick_params(labelsize=6)

plt.savefig('figures/fig_type_mechanism.pdf', format='pdf')
plt.savefig('figures/fig_type_mechanism.png', format='png')
print('Saved figures/fig_type_mechanism.pdf')
