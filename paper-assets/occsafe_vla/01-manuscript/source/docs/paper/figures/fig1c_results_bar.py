"""
fig1c_results_bar.py — CAR bar plot, formerly panel (c) of fig1_overview.
Split into standalone single-column figure. Data unchanged.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe
import numpy as np

COLORS = {
    'vanilla':     '#4C72B0',
    'full_occ_bn': '#C44E52',
    'full_occ_ln': '#E69F00',
    'random_occ':  '#55A868',
    'detach_bn':   '#8172B3',
    'detach_ln':   '#937860',
    'depth':       '#CCB974',
    'cutoff':      '#64B5CD',
}

UI = {
    'text':         '#2C3E50',
    'subtle':       '#95A5A6',
}

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'font.size': 11,
    'text.color': UI['text'],
    'axes.labelcolor': UI['text'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'mathtext.fontset': 'cm',
})

fig, ax_c = plt.subplots(figsize=(3.4, 3.0), dpi=300, facecolor='white')

# CORRECTED v2 data (Table 1), grouped by normalization type
cdata = [
    {'name': 'Full OCC\n(BN, Grad ON)',     'car': 0.725, 'sd': 0.064,
     'color': COLORS['full_occ_bn'], 'n_seeds': 3},
    {'name': 'Detach OCC\n(BN, Grad OFF)',   'car': 0.767, 'sd': 0.024,
     'color': COLORS['detach_bn'],   'n_seeds': 4},
    {'name': 'Full OCC+LN\n(LN, Grad ON)',  'car': 0.773, 'sd': 0.027,
     'color': COLORS['full_occ_ln'], 'n_seeds': 4},
    {'name': 'Detach+LN\n(LN, Grad OFF)',   'car': 0.802, 'sd': 0.024,
     'color': COLORS['detach_ln'],   'n_seeds': 3},
]
vanilla_car = 0.745

ax_c.set_xlim(0.655, 0.87)
ax_c.set_ylim(-0.8, len(cdata) - 0.2)
ax_c.invert_yaxis()
ax_c.spines['top'].set_visible(False)
ax_c.spines['right'].set_visible(False)
ax_c.spines['left'].set_visible(False)
ax_c.set_xlabel('Collision Avoidance Rate (CAR)', fontsize=11, fontweight='bold', labelpad=6)

# Group background bands
ax_c.axhspan(-0.5, 1.5, alpha=0.02, color=COLORS['full_occ_bn'], zorder=0)
ax_c.axhspan(1.5, 3.5, alpha=0.02, color=COLORS['full_occ_ln'], zorder=0)
ax_c.text(0.865, 0.5, 'BN', fontsize=9.5, color=COLORS['full_occ_bn'], ha='center', va='center',
          fontweight='bold', alpha=0.35,
          bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))
ax_c.text(0.865, 2.5, 'LN', fontsize=9.5, color=COLORS['full_occ_ln'], ha='center', va='center',
          fontweight='bold', alpha=0.35,
          bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.6))

# Vanilla reference
ax_c.axvline(x=vanilla_car, color=COLORS['vanilla'], linestyle='--',
             linewidth=1.8, alpha=0.7, zorder=1)
ax_c.text(vanilla_car + 0.003, -0.55, f'Vanilla  {vanilla_car:.3f}',
          fontsize=10, color=COLORS['vanilla'], va='top', ha='left',
          fontweight='bold',
          path_effects=[pe.withStroke(linewidth=3, foreground='white')])

# Below-baseline shading
ax_c.axvspan(0.655, vanilla_car, alpha=0.04, color=COLORS['full_occ_bn'], zorder=0)

# Connecting lines: BN pair
ax_c.plot([0.725, 0.767], [0, 1], color=COLORS['full_occ_bn'],
          lw=1.3, linestyle=':', alpha=0.5, zorder=1)
ax_c.text(0.730, 0.55, '$-$4.2 pp', fontsize=9,
          color=COLORS['full_occ_bn'], ha='left', va='center',
          fontweight='bold', alpha=0.8,
          path_effects=[pe.withStroke(linewidth=3, foreground='white')])

# LN pair
ax_c.plot([0.773, 0.802], [2, 3], color=COLORS['full_occ_ln'],
          lw=1.3, linestyle=':', alpha=0.5, zorder=1)
ax_c.text(0.778, 2.55, '$-$2.9 pp', fontsize=9,
          color=COLORS['full_occ_ln'], ha='left', va='center',
          fontweight='bold', alpha=0.8,
          path_effects=[pe.withStroke(linewidth=3, foreground='white')])

# Plot data
for i, d in enumerate(cdata):
    ax_c.plot(d['car'], i, 'o', color=d['color'], markersize=9,
              markeredgecolor='white', markeredgewidth=1.0, zorder=5)

    if d['sd'] is not None:
        ax_c.errorbar(d['car'], i, xerr=d['sd'], fmt='none', ecolor=d['color'],
                      elinewidth=2.2, capsize=5, capthick=1.6, zorder=4,
                      alpha=0.7)

    right_x = d['car'] + (d['sd'] if d['sd'] else 0) + 0.006
    label_text = f'{d["car"]:.3f} ± {d["sd"]:.3f}' if d['sd'] else f'{d["car"]:.3f}'

    ax_c.text(right_x, i + 0.02, label_text, fontsize=9.5, ha='left',
              va='center', color=d['color'], fontweight='bold',
              path_effects=[pe.withStroke(linewidth=3, foreground='white')])

ax_c.set_yticks(list(range(len(cdata))))
ax_c.set_yticklabels([d['name'] for d in cdata], fontsize=10, linespacing=1.1)
ax_c.tick_params(axis='y', length=0, pad=6)
ax_c.tick_params(axis='x', labelsize=10)
ax_c.grid(axis='x', alpha=0.10, color='#999', zorder=0)
ax_c.set_xticks([0.68, 0.72, 0.76, 0.80, 0.84])

plt.tight_layout()

# Save
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'
fig.savefig(f'{out_dir}/fig1c_results_bar.png', dpi=300, bbox_inches='tight',
            pad_inches=0.05, facecolor='white')
fig.savefig(f'{out_dir}/fig1c_results_bar.pdf', dpi=300, bbox_inches='tight',
            pad_inches=0.05, facecolor='white')
plt.close()
print("Saved fig1c_results_bar.png and fig1c_results_bar.pdf")
