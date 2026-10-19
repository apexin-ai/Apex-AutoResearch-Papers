import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'dejavuserif'

# Data
data = {
    'Pi0 (no refinement)': {
        'marker': 'o', 'color': '#3274A1', 'size': 60, 'zorder': 5,
        'points': {
            'LoRA baseline': (0, 82),
            'Full-FT baseline': (0.5, 83),
            'A1-LoRA (Pi0)': (0, 91.5),
            'A3 (Pi0)': (0, 74.5),
        }
    },
    'Oracle (GT SDF)': {
        'marker': 'D', 'color': '#8B5CF6', 'size': 55, 'zorder': 5,
        'points': {
            'Oracle-adaptive': (0, 75),
            'Oracle-fixed': (0, 73.1),
            'Oracle-feature': (0, 76.9),
        }
    },
    'Pi0.5 baseline': {
        'marker': 's', 'color': '#2CA02C', 'size': 55, 'zorder': 5,
        'points': {
            'Pi0.5 s0': (73, 28),
            'Pi0.5 s1': (76, 25),
            'Pi0.5 s2': (75, 27.5),
        }
    },
    'Pi0.5+A1 (SDF aux)': {
        'marker': '*', 'color': '#E8740C', 'size': 180, 'zorder': 6,
        'points': {
            r'$\lambda$=0.005': (47, 58),
            r'$\lambda$=0.01': (49, 56.5),
        }
    },
    'Pi0.5 spatial': {
        'marker': '^', 'color': '#7F7F7F', 'size': 60, 'zorder': 5,
        'points': {
            'Pi0.5 spatial': (57.5, 13),
        }
    },
}

fig, ax = plt.subplots(figsize=(5, 4), dpi=300)

# "Fake safety" zone
ax.axhspan(70, 100, xmin=0, xmax=0.08, color='#D3D3D3', alpha=0.25, zorder=1)
ax.text(3.5, 96, '"Fake safety"\nzone', fontsize=6.5, color='#888888',
        ha='center', va='top', style='italic')

# Plot each group
for group_name, info in data.items():
    xs = [p[0] for p in info['points'].values()]
    ys = [p[1] for p in info['points'].values()]
    ax.scatter(xs, ys, marker=info['marker'], c=info['color'],
               s=info['size'], label=group_name, edgecolors='white',
               linewidths=0.5, zorder=info['zorder'])

# Annotations with manual offsets to avoid overlap
offsets = {
    'LoRA baseline': (6, -2),
    'Full-FT baseline': (6, 2),
    'A1-LoRA (Pi0)': (6, 0),
    'A3 (Pi0)': (5, -4),
    'Oracle-adaptive': (6, 1),
    'Oracle-fixed': (6, -3),
    'Oracle-feature': (6, 3),
    'Pi0.5 s0': (-3, -7),
    'Pi0.5 s1': (4, -6),
    'Pi0.5 s2': (-3, 4),
    r'$\lambda$=0.005': (-4, 5),
    r'$\lambda$=0.01': (4, -6),
    'Pi0.5 spatial': (5, 4),
}

for group_name, info in data.items():
    for label, (x, y) in info['points'].items():
        dx, dy = offsets.get(label, (5, 3))
        ax.annotate(label, (x, y), textcoords='offset points',
                    xytext=(dx, dy), fontsize=5.5, color=info['color'],
                    arrowprops=dict(arrowstyle='-', color=info['color'],
                                    lw=0.4, shrinkA=0, shrinkB=2) if abs(dx) > 4 or abs(dy) > 4 else None)

# Arrow from Pi0.5 baseline cluster center to Pi0.5+A1 center
ax.annotate('', xy=(48, 57), xytext=(74.7, 26.8),
            arrowprops=dict(arrowstyle='->', color='darkorange', lw=1.5),
            zorder=7)
# Label at midpoint, offset to the right to avoid overlap
mid_x, mid_y = (74.7 + 48) / 2, (26.8 + 57) / 2
ax.text(mid_x + 5, mid_y - 3, 'SDF training\neffect', fontsize=6,
        color='darkorange', fontweight='medium', ha='left', va='center',
        bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.8),
        zorder=7)

ax.set_xlim(-3, 100)
ax.set_ylim(0, 100)
ax.set_xlabel('Task Success Rate (%)', fontsize=10)
ax.set_ylabel('Collision Avoidance Rate (%)', fontsize=10)
ax.tick_params(labelsize=8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

legend = ax.legend(fontsize=6.5, loc='upper right', framealpha=0.9,
                   edgecolor='#CCCCCC', handletextpad=0.4, borderpad=0.5)
legend.get_frame().set_linewidth(0.5)

plt.tight_layout()
out = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig_tsr_car_scatter.pdf'
plt.savefig(out, bbox_inches='tight', dpi=300)
print(f'Saved: {out}')
plt.close()
