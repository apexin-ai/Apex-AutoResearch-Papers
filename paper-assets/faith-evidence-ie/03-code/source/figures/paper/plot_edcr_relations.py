import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
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

edcr_values = [
    1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00,
    1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.98, 0.96, 0.95,
    0.90, 0.90, 0.90, 0.89, 0.88, 0.87, 0.86, 0.86, 0.85, 0.85,
    0.84, 0.84, 0.83, 0.83, 0.81, 0.80, 0.80, 0.80, 0.77, 0.76,
    0.76, 0.76, 0.74, 0.74, 0.74, 0.72, 0.70, 0.68, 0.67, 0.66,
    0.64, 0.60, 0.59, 0.58, 0.57, 0.57, 0.57, 0.57, 0.56, 0.56,
    0.54, 0.52, 0.51, 0.50, 0.49, 0.48, 0.47, 0.46, 0.46, 0.45,
    0.44, 0.44, 0.41, 0.40, 0.38, 0.38, 0.37, 0.34, 0.33, 0.32,
    0.31, 0.28, 0.27, 0.27, 0.25, 0.24, 0.20, 0.19, 0.17, 0.08,
    0.04, -0.07, -0.19,
]

exemplars = {
    1.00: 'capital of, instance of, ...',
    0.76: 'location, operator',
    0.49: 'genre',
    0.27: 'country',
    0.04: 'date of birth',
    -0.19: 'manufacturer',
}

COL_SEVERE = '#D55E00'
COL_MODERATE = '#E69F00'
COL_MILD = '#56B4E9'
COL_HEALTHY = '#009E73'

bins = np.arange(-0.3, 1.15, 0.1)
bin_centers = (bins[:-1] + bins[1:]) / 2

counts, _ = np.histogram(edcr_values, bins=bins)

bar_colors = []
bar_hatches = []
HATCH_MAP = {COL_SEVERE: '///', COL_MODERATE: 'xxx', COL_MILD: '\\\\\\', COL_HEALTHY: '...'}
for c in bin_centers:
    if c >= 0.70:
        bar_colors.append(COL_SEVERE)
        bar_hatches.append(HATCH_MAP[COL_SEVERE])
    elif c >= 0.40:
        bar_colors.append(COL_MODERATE)
        bar_hatches.append(HATCH_MAP[COL_MODERATE])
    elif c >= 0.20:
        bar_colors.append(COL_MILD)
        bar_hatches.append(HATCH_MAP[COL_MILD])
    else:
        bar_colors.append(COL_HEALTHY)
        bar_hatches.append(HATCH_MAP[COL_HEALTHY])

fig, ax = plt.subplots(figsize=(6, 3.2))

bar_width = 0.08
bars = ax.bar(bin_centers, counts, width=bar_width, color=bar_colors,
              edgecolor='#444444', linewidth=0.5, alpha=0.88, zorder=3)
for bar, hatch in zip(bars, bar_hatches):
    bar.set_hatch(hatch)

for bar, count in zip(bars, counts):
    if count > 0:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                str(count), ha='center', va='bottom', fontsize=7.5,
                color='#444444', fontweight='bold')

zone_alpha = 0.06
ax.axvspan(-0.3, 0.20, color=COL_HEALTHY, alpha=zone_alpha, zorder=0)
ax.axvspan(0.20, 0.40, color=COL_MILD, alpha=zone_alpha, zorder=0)
ax.axvspan(0.40, 0.70, color=COL_MODERATE, alpha=zone_alpha, zorder=0)
ax.axvspan(0.70, 1.15, color=COL_SEVERE, alpha=zone_alpha, zorder=0)

zone_y = max(counts) + 2.5
for label, x, color in [
    ('Healthy', 0.05, COL_HEALTHY),
    ('Mild', 0.30, COL_MILD),
    ('Moderate', 0.55, COL_MODERATE),
    ('Severe', 0.92, COL_SEVERE),
]:
    t = ax.text(x, zone_y, label, fontsize=7.5, color=color,
                ha='center', va='bottom', fontstyle='italic', fontweight='bold')
    t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

annotations = [
    (0.95, 17, 'capital of,\ninstance of, ...', -25, 4.5),
    (0.45, 3, 'genre, continent', 20, 3.0),
    (0.25, 3, 'director,\nmember of\nsports team', -15, 4.0),
    (-0.15, 1, 'manufacturer', 10, 2.5),
]
for x, y, text, xoff, yoff in annotations:
    ax.annotate(text, xy=(x, y), xytext=(x + xoff * 0.01, y + yoff),
                fontsize=6, color='#555555', ha='center', va='bottom',
                linespacing=0.85,
                arrowprops=dict(arrowstyle='->', color='#999999', lw=0.6,
                                mutation_scale=7))

ax.set_xlabel('EDCR (Evidence-Decoupling Ratio)', fontsize=10)
ax.set_ylabel('Number of Relation Types', fontsize=10)
ax.set_xlim(-0.30, 1.12)
ax.set_ylim(0, max(counts) + 5)
ax.grid(axis='y', alpha=0.10, linewidth=0.3, zorder=0)

from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=COL_SEVERE, alpha=0.88, edgecolor='#444444', hatch='///', label='Severe (EDCR $\\geq$ 0.70)'),
    Patch(facecolor=COL_MODERATE, alpha=0.88, edgecolor='#444444', hatch='xxx', label='Moderate (0.40 $\\leq$ EDCR < 0.70)'),
    Patch(facecolor=COL_MILD, alpha=0.88, edgecolor='#444444', hatch='\\\\\\', label='Mild (0.20 $\\leq$ EDCR < 0.40)'),
    Patch(facecolor=COL_HEALTHY, alpha=0.88, edgecolor='#444444', hatch='...', label='Healthy (EDCR < 0.20)'),
]
ax.legend(handles=legend_elements, loc='center left', fontsize=7,
          framealpha=0.95, edgecolor='#e0e0e0', borderpad=0.4,
          bbox_to_anchor=(0.0, 0.55))

fig.tight_layout()
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/figures/paper'
fig.savefig(f'{out_dir}/fig_edcr_relations.pdf', bbox_inches='tight', dpi=300)
fig.savefig(f'{out_dir}/fig_edcr_relations.png', bbox_inches='tight', dpi=300)
print(f'Done. {len(edcr_values)} relations, histogram with {len(bins)-1} bins.')
