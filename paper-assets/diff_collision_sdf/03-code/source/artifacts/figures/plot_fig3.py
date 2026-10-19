import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Ellipse
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

COLORS = {
    'baseline': '#0072B2',
    'lora': '#E69F00',
    'sdf005': '#009E73',
    'sdf01': '#D55E00',
    'phase2': '#CC79A7',
}

# Data: (name, TSR, CAR, marker, color, size)
data = [
    ('Pi0.5 baseline', 71.5, 28.5, '*', COLORS['baseline'], 220),
    ('LoRA-only s1',   51.5, 52.5, 'o', COLORS['lora'],     80),
    ('SDF $\\lambda$=0.005 s0', 55.5, 57.0, '^', COLORS['sdf005'], 80),
    ('SDF $\\lambda$=0.01 s0',  52.5, 57.0, 's', COLORS['sdf01'],  80),
    ('Phase 2 $\\lambda$=0 s2', 53.5, 57.5, 'D', COLORS['phase2'], 80),
]

fig, ax = plt.subplots(figsize=(6, 5))

# Quadrant boundaries
mid_x, mid_y = 50, 50

# Quadrant backgrounds
ax.fill_between([mid_x, 100], mid_y, 100, alpha=0.06, color='#2ca02c', zorder=0)
ax.fill_between([0, mid_x], mid_y, 100, alpha=0.06, color='#d62728', zorder=0)
ax.fill_between([mid_x, 100], 0, mid_y, alpha=0.04, color='#ff7f0e', zorder=0)
ax.fill_between([0, mid_x], 0, mid_y, alpha=0.04, color='#7f7f7f', zorder=0)

# Quadrant divider lines
ax.axhline(mid_y, color='#cccccc', linewidth=0.8, linestyle='--', zorder=1)
ax.axvline(mid_x, color='#cccccc', linewidth=0.8, linestyle='--', zorder=1)

# Quadrant labels
ax.text(75, 96, 'Ideal\n(High TSR + High CAR)', ha='center', va='top',
        fontsize=8, color='#2ca02c', alpha=0.7, style='italic')
ax.text(25, 96, 'Safe but\nIncapable', ha='center', va='top',
        fontsize=8, color='#d62728', alpha=0.7, style='italic')
ax.text(75, 4, 'Capable but\nUnsafe', ha='center', va='bottom',
        fontsize=8, color='#ff7f0e', alpha=0.7, style='italic')
ax.text(25, 4, 'Neither', ha='center', va='bottom',
        fontsize=8, color='#7f7f7f', alpha=0.6, style='italic')

# Plot data points
for name, tsr, car, marker, color, size in data:
    ax.scatter(tsr, car, c=color, marker=marker, s=size, zorder=5,
               edgecolors='black', linewidths=0.5)

# Label annotations with arrows for clarity
label_configs = {
    'Pi0.5 baseline': dict(xytext=(82, 22), ha='center', va='top', fontweight='bold'),
    'LoRA-only s1':   dict(xytext=(30, 44), ha='center', va='top'),
    'SDF $\\lambda$=0.005 s0': dict(xytext=(68, 68), ha='left', va='bottom'),
    'SDF $\\lambda$=0.01 s0':  dict(xytext=(36, 62), ha='right', va='center'),
    'Phase 2 $\\lambda$=0 s2': dict(xytext=(66, 75), ha='left', va='bottom'),
}

for name, tsr, car, marker, color, size in data:
    cfg = label_configs[name]
    xt, yt = cfg['xytext']
    ax.annotate(name, (tsr, car), xytext=(xt, yt),
                fontsize=8, ha=cfg['ha'], va=cfg['va'], color=color,
                fontweight=cfg.get('fontweight', 'normal'),
                arrowprops=dict(arrowstyle='->', lw=0.6, color='#aaaaaa'))

# Ellipse around fine-tuned cluster
ft_tsrs = [51.5, 55.5, 52.5, 53.5]
ft_cars = [52.5, 57.0, 57.0, 57.5]
cx = np.mean(ft_tsrs)
cy = np.mean(ft_cars)
w = (max(ft_tsrs) - min(ft_tsrs)) + 10
h = (max(ft_cars) - min(ft_cars)) + 10
ellipse = Ellipse((cx, cy), w, h, angle=0, fill=False,
                  edgecolor='gray', linewidth=1.2, linestyle='--', zorder=3)
ax.add_patch(ellipse)
ax.text(cx + 6, cy - h/2 - 2.5, 'Fine-tuned cluster', ha='center', va='top',
        fontsize=8.5, color='gray', style='italic',
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.8))

# Arrow from baseline to cluster center
arrow = FancyArrowPatch((71.5, 28.5), (cx + 2, cy - h/2 + 1),
                        arrowstyle='->', mutation_scale=14,
                        lw=1.5, color='#555555', zorder=4,
                        connectionstyle='arc3,rad=-0.15')
ax.add_patch(arrow)
ax.text(69, 38, 'TSR $\\downarrow$20pp\nCAR $\\uparrow$25pp',
        fontsize=8.5, ha='center', va='center', color='#555555',
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc', alpha=0.9))

# Axes
ax.set_xlabel('Task Success Rate (%)')
ax.set_ylabel('Collision Avoidance Rate (%)')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Legend
legend_elements = [
    plt.Line2D([0], [0], marker='*', color='w', markerfacecolor=COLORS['baseline'],
               markersize=12, markeredgecolor='black', markeredgewidth=0.5, label='Pi0.5 baseline'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['lora'],
               markersize=8, markeredgecolor='black', markeredgewidth=0.5, label='LoRA-only s1'),
    plt.Line2D([0], [0], marker='^', color='w', markerfacecolor=COLORS['sdf005'],
               markersize=8, markeredgecolor='black', markeredgewidth=0.5, label='SDF $\\lambda$=0.005 s0'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor=COLORS['sdf01'],
               markersize=8, markeredgecolor='black', markeredgewidth=0.5, label='SDF $\\lambda$=0.01 s0'),
    plt.Line2D([0], [0], marker='D', color='w', markerfacecolor=COLORS['phase2'],
               markersize=8, markeredgecolor='black', markeredgewidth=0.5, label='Phase 2 $\\lambda$=0 s2'),
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=8, framealpha=0.9,
          edgecolor='#cccccc')

plt.tight_layout()

out_base = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig3_tsr_car_scatter'
plt.savefig(out_base + '.pdf', bbox_inches='tight', dpi=300)
plt.savefig(out_base + '.png', bbox_inches='tight', dpi=300)
print("Saved fig3_tsr_car_scatter.pdf and .png")
