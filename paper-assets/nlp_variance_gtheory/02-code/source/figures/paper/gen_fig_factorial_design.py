"""Factorial crossed design diagram: items at center, facets radiating out."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],
    'font.size': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

fig, ax = plt.subplots(figsize=(3.4, 2.6))

# Center: Items
cx, cy = 0.5, 0.5
r_center = 0.13

center_circle = plt.Circle((cx, cy), r_center, fc='#2c3e50', ec='#2c3e50',
                            zorder=10)
ax.add_patch(center_circle)
ax.text(cx, cy + 0.015, 'Items', ha='center', va='center', fontsize=8,
        fontweight='bold', color='white', zorder=11)
ax.text(cx, cy - 0.025, '(200)', ha='center', va='center', fontsize=7,
        color='#bdc3c7', zorder=11)

# Facets around the center
facets = [
    ('Models\n8 families', '#e74c3c'),
    ('Prompts\n6 templates', '#3498db'),
    ('Seeds\n6 values', '#2ecc71'),
    ('Temp.\n3 levels', '#f39c12'),
    ('Precision\n3 formats', '#9b59b6'),
    ('Ordering\n4 perms.', '#1abc9c'),
]

n = len(facets)
r_orbit = 0.32
r_facet = 0.09

angles = np.linspace(90, 90 - 360, n, endpoint=False)

for i, (label, color) in enumerate(facets):
    angle_rad = np.radians(angles[i])
    fx = cx + r_orbit * np.cos(angle_rad)
    fy = cy + r_orbit * np.sin(angle_rad)

    # Connection line
    dx = fx - cx
    dy = fy - cy
    dist = np.sqrt(dx**2 + dy**2)
    ux, uy = dx / dist, dy / dist

    x1 = cx + r_center * ux
    y1 = cy + r_center * uy
    x2 = fx - r_facet * ux
    y2 = fy - r_facet * uy
    ax.plot([x1, x2], [y1, y2], color='#7f8c8d', linewidth=1.2,
            zorder=5, linestyle='-')

    # Facet circle
    facet_circle = plt.Circle((fx, fy), r_facet, fc=color, ec='white',
                              linewidth=0.8, alpha=0.9, zorder=8)
    ax.add_patch(facet_circle)

    parts = label.split('\n')
    ax.text(fx, fy + 0.015, parts[0], ha='center', va='center', fontsize=6.5,
            fontweight='bold', color='white', zorder=9)
    ax.text(fx, fy - 0.02, parts[1], ha='center', va='center', fontsize=5.5,
            color='white', alpha=0.9, zorder=9)

# Cross indicators (×) on lines
for i in range(n):
    angle_rad = np.radians(angles[i])
    mx = cx + (r_orbit * 0.55) * np.cos(angle_rad)
    my = cy + (r_orbit * 0.55) * np.sin(angle_rad)
    ax.text(mx, my, '×', ha='center', va='center', fontsize=7,
            fontweight='bold', color='#e74c3c', zorder=12,
            bbox=dict(boxstyle='round,pad=0.08', fc='white', ec='none',
                      alpha=0.85))

# Total records annotation
ax.text(0.5, 0.02, 'Fully crossed: 259,200 records (single-model)',
        ha='center', va='bottom', fontsize=6.5, fontstyle='italic',
        color='#555555')

ax.set_xlim(0.05, 0.95)
ax.set_ylim(-0.02, 0.98)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
out = Path(__file__).parent
plt.savefig(out / 'fig_factorial_design.pdf', bbox_inches='tight', dpi=300)
plt.savefig(out / 'fig_factorial_design.png', bbox_inches='tight', dpi=200)
plt.close()
print("Saved fig_factorial_design.pdf/png")
