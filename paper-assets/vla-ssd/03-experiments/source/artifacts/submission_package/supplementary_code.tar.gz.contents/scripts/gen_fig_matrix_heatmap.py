"""
Regenerate fig_matrix_heatmap.pdf with correct ΔR² values from Table 1.
Designed for display at 0.75\\textwidth (~4.9 inches) with minimal scaling.
"""
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

architectures = ['OpenVLA', 'TracVLA', 'NORA']
suites = ['Goal', 'Spatial', 'Object', 'Long']
transition_types = {
    'OpenVLA': 'VLA→VLA',
    'TracVLA': 'VLM→VLA',
    'NORA': 'VLM→VLA',
}

data = {
    ('OpenVLA', 'Goal'): 0.086,
    ('OpenVLA', 'Spatial'): 0.037,
    ('OpenVLA', 'Object'): 0.037,
    ('OpenVLA', 'Long'): 0.033,
    ('TracVLA', 'Goal'): 0.333,
    ('TracVLA', 'Spatial'): 0.156,
    ('TracVLA', 'Object'): 0.362,
    ('TracVLA', 'Long'): 0.358,
    ('NORA', 'Goal'): 0.455,
    ('NORA', 'Spatial'): 0.308,
    ('NORA', 'Object'): None,
    ('NORA', 'Long'): None,
}

THRESHOLD = 0.10
nrows = len(architectures)
ncols = len(suites)

cell_w = 0.88
cell_h = 0.36

fig_w = 5.2
fig_h = 1.38
fig, ax = plt.subplots(figsize=(fig_w, fig_h))

cmap = plt.cm.Blues
vmin, vmax = 0.0, 0.50

for i in range(nrows):
    for j in range(ncols):
        val = data[(architectures[i], suites[j])]
        x0 = j * cell_w
        y0 = (nrows - 1 - i) * cell_h
        gap = 0.03
        if val is None:
            rect = patches.FancyBboxPatch(
                (x0 + gap, y0 + gap), cell_w - 2*gap, cell_h - 2*gap,
                boxstyle="round,pad=0.02",
                facecolor='#E0E0E0', edgecolor='#AAAAAA', linewidth=0.6
            )
            ax.add_patch(rect)
            ax.text(x0 + cell_w/2, y0 + cell_h/2, 'N/A',
                    ha='center', va='center', fontsize=10, color='#888888',
                    fontweight='bold')
        else:
            norm_val = np.clip((val - vmin) / (vmax - vmin), 0, 1)
            color = cmap(norm_val)
            rect = patches.FancyBboxPatch(
                (x0 + gap, y0 + gap), cell_w - 2*gap, cell_h - 2*gap,
                boxstyle="round,pad=0.02",
                facecolor=color, edgecolor='none', linewidth=0
            )
            ax.add_patch(rect)

            if val > THRESHOLD:
                border = patches.FancyBboxPatch(
                    (x0 + gap, y0 + gap), cell_w - 2*gap, cell_h - 2*gap,
                    boxstyle="round,pad=0.02",
                    facecolor='none', edgecolor='#CC3333', linewidth=1.5
                )
                ax.add_patch(border)

            text_color = 'white' if norm_val > 0.55 else '#333333'
            trans = transition_types[architectures[i]]
            ax.text(x0 + cell_w/2, y0 + cell_h*0.72, trans,
                    ha='center', va='center', fontsize=7, color=text_color,
                    fontstyle='italic')
            ax.text(x0 + cell_w/2, y0 + cell_h*0.35, f'{val:.3f}',
                    ha='center', va='center', fontsize=10.5, color=text_color,
                    fontweight='bold')

for j, suite in enumerate(suites):
    ax.text(j * cell_w + cell_w/2, nrows * cell_h + 0.05, suite,
            ha='center', va='bottom', fontsize=10, fontweight='bold')

for i, arch in enumerate(architectures):
    ax.text(-0.06, (nrows - 1 - i) * cell_h + cell_h/2, arch,
            ha='right', va='center', fontsize=10, fontweight='bold')

ax.set_xlim(-0.03, ncols * cell_w + 0.03)
ax.set_ylim(-0.14, nrows * cell_h + 0.14)
ax.axis('off')

ax.set_title('Cross-Architecture Representation Dynamics',
             fontsize=12, fontweight='bold', pad=6)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm.set_array([])
cbar_ax = fig.add_axes([0.92, 0.15, 0.015, 0.65])
cbar = fig.colorbar(sm, cax=cbar_ax)
cbar.set_label('$\\Delta R^2$ (peak − exit)', fontsize=9, labelpad=5)
cbar.ax.tick_params(labelsize=8)
cbar.ax.axhline(y=THRESHOLD, color='#CC3333', linewidth=1.2, linestyle='--')
cbar.ax.text(1.2, THRESHOLD, 'substantial\n(0.10)',
             transform=cbar.ax.get_yaxis_transform(),
             fontsize=7, color='#CC3333', va='center', ha='left')

fig.text(0.48, 0.01,
         'Values: peak−exit $\\Delta R^2$ from MCCV bootstrap (1000 iterations). '
         'Gray cells: suite not available for this architecture.',
         ha='center', fontsize=7.5, color='#666666')

plt.subplots_adjust(left=0.12, right=0.90, top=0.86, bottom=0.08)

import os
out_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(out_dir)
paper_fig_dir = os.path.join(project_root, 'docs', 'paper', 'figures')
artifacts_fig_dir = os.path.join(project_root, 'artifacts', 'figures')

for d in [paper_fig_dir, artifacts_fig_dir]:
    os.makedirs(d, exist_ok=True)
    fig.savefig(os.path.join(d, 'fig_matrix_heatmap.pdf'),
                bbox_inches='tight', dpi=300, backend='pdf')
    fig.savefig(os.path.join(d, 'fig_matrix_heatmap.png'),
                bbox_inches='tight', dpi=200)

print("Generated fig_matrix_heatmap.pdf and .png")
# Print dimensions for verification
import fitz
doc = fitz.open(os.path.join(paper_fig_dir, 'fig_matrix_heatmap.pdf'))
p = doc[0]
print(f'PDF: {p.rect.width:.0f}x{p.rect.height:.0f}pt, aspect {p.rect.width/p.rect.height:.2f}')
target = 0.75 * 468
print(f'At 0.75 textwidth ({target:.0f}pt): scale={target/p.rect.width:.2f}, height={target/p.rect.width*p.rect.height:.0f}pt')
plt.close()
