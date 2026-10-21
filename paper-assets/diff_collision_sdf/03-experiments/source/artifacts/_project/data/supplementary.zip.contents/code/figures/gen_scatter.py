import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['STIXGeneral', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.7,
})

fig, ax = plt.subplots(figsize=(4, 3.5))

# Data points (TSR, CAR)
# Left cluster (TSR ≈ 0, CAR 73-91.5) — use letter labels
left_cluster = [
    ('(a)', 0, 91.5, 'blue', 'o'),      # A1-LoRA
    ('(b)', 0.5, 83, 'blue', 'o'),       # Full-FT baseline
    ('(c)', 0, 82, 'blue', 'o'),         # LoRA baseline
    ('(d)', 0, 76.9, 'purple', 'D'),     # Oracle-feature
    ('(e)', 0, 75, 'purple', 'D'),       # Oracle-adaptive
    ('(f)', 0, 74.5, 'blue', 'o'),       # A3
    ('(g)', 0, 73.1, 'purple', 'D'),     # Oracle-fixed
]

# Pi0.5 baseline cluster
pi05_cluster = [
    ('Pi0.5 s0', 73, 28, 'green', 's'),
    ('Pi0.5 s1', 76, 25, 'green', 's'),
    ('Pi0.5 s2', 75, 27.5, 'green', 's'),
]

# Pi0.5+A1 points
pi05_a1 = [
    ('λ=0.005', 47, 58, 'orange', '*'),
    ('λ=0.01', 49, 56.5, 'orange', '*'),
]

# Draw fake safety zone
ax.fill_between([0, 5], 60, 100, alpha=0.12, color='gray', zorder=0)
ax.text(2.5, 96, 'Action-Collapsed\nSafety Zone', ha='center', va='top', fontsize=7,
        color='gray', style='italic')

# Plot left cluster points
for label, x, y, color, marker in left_cluster:
    ax.scatter(x, y, c=color, marker=marker, s=50, zorder=5, edgecolors='black', linewidths=0.3)

# Letter labels for left cluster — offset to the right
offsets = [
    (3.5, 0),    # (a) A1-LoRA
    (3.5, 0),    # (b) Full-FT
    (3.5, 0),    # (c) LoRA
    (3.5, 0),    # (d) Oracle-feature
    (3.5, 0),    # (e) Oracle-adaptive
    (3.5, 0),    # (f) A3
    (3.5, 0),    # (g) Oracle-fixed
]

for (label, x, y, color, marker), (ox, oy) in zip(left_cluster, offsets):
    ax.annotate(label, (x, y), xytext=(x + ox, y + oy),
                fontsize=7, ha='left', va='center', color='black')

# Plot Pi0.5 cluster
for label, x, y, color, marker in pi05_cluster:
    ax.scatter(x, y, c=color, marker=marker, s=60, zorder=5, edgecolors='black', linewidths=0.3)

# Single label for Pi0.5 cluster
cx = np.mean([p[1] for p in pi05_cluster])
cy = np.mean([p[2] for p in pi05_cluster])
ax.annotate('Pi0.5\nbaseline', (cx, cy), xytext=(cx + 5, cy - 6),
            fontsize=7.5, ha='left', va='top',
            arrowprops=dict(arrowstyle='->', lw=0.7, color='gray'),
            color='black')

# Plot Pi0.5+A1 points
for label, x, y, color, marker in pi05_a1:
    ax.scatter(x, y, c=color, marker=marker, s=100, zorder=5, edgecolors='black', linewidths=0.3)

# Label for Pi0.5+A1 — centered between two points with arrows
mid_x = np.mean([p[1] for p in pi05_a1])
mid_y = np.mean([p[2] for p in pi05_a1])
ax.annotate('Pi0.5+A1\n(SDF aux)', (mid_x, mid_y), xytext=(mid_x + 8, mid_y + 8),
            fontsize=7.5, ha='left', va='bottom',
            arrowprops=dict(arrowstyle='->', lw=0.7, color='gray'),
            color='black')

# Arrow from Pi0.5 baseline cluster to Pi0.5+A1
arrow = FancyArrowPatch((cx, cy), (mid_x - 2, mid_y - 2),
                        arrowstyle='->', mutation_scale=12,
                        lw=1.5, color='darkorange', zorder=4)
ax.add_patch(arrow)
ax.text((cx + mid_x) / 2 - 3, (cy + mid_y) / 2 + 3, 'SDF training\neffect',
        fontsize=7, ha='center', va='bottom', color='darkorange', style='italic')

# Legend box for letter labels (bottom-right)
legend_text = (
    "(a) A1-LoRA (91.5%)\n"
    "(b) Full-FT baseline (83%)\n"
    "(c) LoRA baseline (82%)\n"
    "(d) Oracle-feature (76.9%)\n"
    "(e) Oracle-adaptive (75%)\n"
    "(f) A3 (74.5%)\n"
    "(g) Oracle-fixed (73.1%)"
)
props = dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='gray', alpha=0.9)
ax.text(0.02, 0.02, legend_text, transform=ax.transAxes, fontsize=6,
        verticalalignment='bottom', horizontalalignment='left',
        bbox=props, family='monospace')

# Marker legend (upper right)
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=7, markeredgecolor='black', markeredgewidth=0.3, label='Pi0-family'),
    plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='purple', markersize=7, markeredgecolor='black', markeredgewidth=0.3, label='Oracle variants'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='green', markersize=7, markeredgecolor='black', markeredgewidth=0.3, label='Pi0.5 baseline'),
    plt.Line2D([0], [0], marker='*', color='w', markerfacecolor='orange', markersize=9, markeredgecolor='black', markeredgewidth=0.3, label='Pi0.5+A1 (SDF aux)'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

# Axes
ax.set_xlabel('Task Success Rate (%)', fontsize=10)
ax.set_ylabel('Collision Avoidance Rate (%)', fontsize=10)
ax.set_xlim(-5, 100)
ax.set_ylim(15, 100)

plt.tight_layout()
plt.savefig('./output/fig_tsr_car_scatter.pdf',
            bbox_inches='tight', dpi=300)
print("Saved fig_tsr_car_scatter.pdf")
