"""
Regenerate fig_matrix_heatmap.pdf with correct ΔR² values from Table 1.
Designed for display at 0.75\\textwidth (~4.9 inches) with minimal scaling.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'custom',
    'mathtext.rm': 'Liberation Serif',
    'mathtext.it': 'Liberation Serif:italic',
    'mathtext.bf': 'Liberation Serif:bold',
})
import matplotlib.patches as patches
import numpy as np

architectures = ['OpenVLA', 'TraceVLA', 'NORA']
suites = ['Goal', 'Spatial', 'Object', 'Long']
transition_types = {
    'OpenVLA': 'VLA→VLA',
    'TraceVLA': 'VLM→VLA',
    'NORA': 'VLM→VLA',
}

data = {
    ('OpenVLA', 'Goal'): 0.086,
    ('OpenVLA', 'Spatial'): 0.037,
    ('OpenVLA', 'Object'): 0.037,
    ('OpenVLA', 'Long'): 0.033,
    ('TraceVLA', 'Goal'): 0.333,
    ('TraceVLA', 'Spatial'): 0.156,
    ('TraceVLA', 'Object'): 0.362,
    ('TraceVLA', 'Long'): 0.358,
    ('NORA', 'Goal'): 0.455,
    ('NORA', 'Spatial'): 0.308,
    ('NORA', 'Object'): None,
    ('NORA', 'Long'): None,
}

THRESHOLD = 0.10
nrows = len(architectures)
ncols = len(suites)

cell_w = 1.0
cell_h = 0.78

fig_w = 5.2
fig_h = 2.8
fig, ax = plt.subplots(figsize=(fig_w, fig_h))

# ── Custom colormap: paper-consistent teal-blue sequential palette ──
# Anchored to the paper's primary blue (#0077BB) from Tol's qualitative scheme.
# White → light sky → medium blue → deep blue.  Perceptually uniform in
# luminance so it degrades gracefully to grayscale and is safe for the three
# most common forms of color-vision deficiency (protanopia / deuteranopia /
# tritanopia).
from matplotlib.colors import LinearSegmentedColormap
_cmap_colors = [
    '#FFFFFF',   # 0.00  — white (zero effect)
    '#DCEAF7',   # 0.15  — very light blue
    '#92C5DE',   # 0.35  — pastel blue (matches overview fig)
    '#0077BB',   # 0.65  — paper primary blue
    '#004488',   # 1.00  — dark navy (maximum ΔR²)
]
cmap = LinearSegmentedColormap.from_list('ssd_seq', _cmap_colors, N=256)
vmin, vmax = 0.0, 0.50

# Dashed-border accent: Tol vibrant orange — high contrast against the blue
# cells, distinguishable for all CVD types, consistent with the paper's
# secondary accent (#EE7733 used in fig_r2_collapse reference line).
BORDER_COLOR = '#EE7733'

# N/A cell styling (neutral warm gray — avoids confusion with low-value blue)
NA_FACE = '#F0EDE8'
NA_EDGE = '#C0B8AD'
NA_TEXT = '#8A8278'

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
                facecolor=NA_FACE, edgecolor=NA_EDGE, linewidth=0.6
            )
            ax.add_patch(rect)
            ax.text(x0 + cell_w/2, y0 + cell_h/2, 'N/A',
                    ha='center', va='center', fontsize=10, color=NA_TEXT,
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
                    facecolor='none', edgecolor=BORDER_COLOR, linewidth=2.0,
                    linestyle='--'
                )
                ax.add_patch(border)

            text_color = 'white' if norm_val > 0.55 else '#333333'
            trans = transition_types[architectures[i]]
            ax.text(x0 + cell_w/2, y0 + cell_h*0.68, trans,
                    ha='center', va='center', fontsize=7, color=text_color,
                    fontstyle='italic')
            ax.text(x0 + cell_w/2, y0 + cell_h*0.35, f'{val:.3f}',
                    ha='center', va='center', fontsize=11, color=text_color,
                    fontweight='bold')

for j, suite in enumerate(suites):
    ax.text(j * cell_w + cell_w/2, nrows * cell_h + 0.05, suite,
            ha='center', va='bottom', fontsize=10, fontweight='bold')

for i, arch in enumerate(architectures):
    ax.text(-0.06, (nrows - 1 - i) * cell_h + cell_h/2, arch,
            ha='right', va='center', fontsize=10, fontweight='bold')

ax.set_xlim(-0.03, ncols * cell_w + 0.03)
ax.set_ylim(-0.10, nrows * cell_h + 0.18)
ax.axis('off')

ax.set_title('Cross-Architecture Representation Dynamics',
             fontsize=12, fontweight='bold', pad=6)

sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm.set_array([])
cbar_ax = fig.add_axes([0.93, 0.12, 0.015, 0.70])
cbar = fig.colorbar(sm, cax=cbar_ax)
cbar.set_label('$\\Delta R^2$ (peak − exit)', fontsize=9, labelpad=8)
cbar.ax.tick_params(labelsize=8)
cbar.ax.axhline(y=THRESHOLD, color=BORDER_COLOR, linewidth=1.2, linestyle='--')
cbar.set_ticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
cbar.set_ticklabels(['0.0', '0.1\n(subst.)', '0.2', '0.3', '0.4', '0.5'])
for tl in cbar.ax.get_yticklabels():
    if '(subst.)' in tl.get_text():
        tl.set_color(BORDER_COLOR)
        tl.set_fontsize(7)

fig.text(0.45, 0.01,
         'Values: peak−exit $\\Delta R^2$ from MCCV bootstrap (1000 iterations). '
         'Gray cells: suite not available for this architecture.',
         ha='center', fontsize=7.5, color='#666666')

plt.subplots_adjust(left=0.14, right=0.88, top=0.88, bottom=0.06)

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
# Print dimensions for verification (optional; requires PyMuPDF)
try:
    import fitz
    doc = fitz.open(os.path.join(paper_fig_dir, 'fig_matrix_heatmap.pdf'))
    p = doc[0]
    print(f'PDF: {p.rect.width:.0f}x{p.rect.height:.0f}pt, aspect {p.rect.width/p.rect.height:.2f}')
    target = 0.75 * 468
    print(f'At 0.75 textwidth ({target:.0f}pt): scale={target/p.rect.width:.2f}, height={target/p.rect.width*p.rect.height:.0f}pt')
except ImportError:
    pass
plt.close()
