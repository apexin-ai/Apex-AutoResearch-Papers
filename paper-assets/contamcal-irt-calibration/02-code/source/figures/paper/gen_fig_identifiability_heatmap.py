#!/usr/bin/env python3
"""Generate appendix figure: gamma identifiability simulation heatmap.

Two-panel heatmap: (left) gamma bias, (right) 95% CI coverage.
Data source: MVP simulation results (artifacts/mvp_simulation/).
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# Axes: Ensemble size J (columns), Signal AUC (rows)
J_values = [8, 20, 50, 100]
AUC_values = [0.55, 0.65, 0.80, 0.90]

# Gamma bias (true - estimated); rows = AUC ascending, cols = J ascending
bias_data = np.array([
    [ 0.009,  0.020,  0.015,  0.002],   # AUC=0.55
    [-0.007, -0.011,  0.007,  0.005],   # AUC=0.65
    [-0.009, -0.016,  0.006,  0.006],   # AUC=0.80
    [-0.006, -0.024,  0.006,  0.000],   # AUC=0.90
])

# 95% CI coverage (%)
coverage_data = np.array([
    [100,  80,  90, 100],   # AUC=0.55
    [100,  90,  90,  90],   # AUC=0.65
    [100,  90, 100, 100],   # AUC=0.80
    [ 90, 100, 100, 100],   # AUC=0.90
])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5))

# Left panel: Bias
im1 = ax1.imshow(bias_data, cmap='RdBu_r', vmin=-0.025, vmax=0.025, aspect='auto')
ax1.set_xticks(range(len(J_values)))
ax1.set_xticklabels([str(j) for j in J_values])
ax1.set_yticks(range(len(AUC_values)))
ax1.set_yticklabels([str(a) for a in AUC_values])
ax1.set_xlabel('Ensemble size $J$')
ax1.set_ylabel('Signal AUC')
ax1.set_title(r'$\gamma$ Bias')
for i in range(len(AUC_values)):
    for j in range(len(J_values)):
        val = bias_data[i, j]
        color = 'white' if abs(val) > 0.015 else 'black'
        ax1.text(j, i, f'{val:.3f}', ha='center', va='center',
                 fontsize=9, color=color)
cbar1 = fig.colorbar(im1, ax=ax1, shrink=0.8)

# Right panel: Coverage
im2 = ax2.imshow(coverage_data, cmap='RdYlGn', vmin=70, vmax=100, aspect='auto')
ax2.set_xticks(range(len(J_values)))
ax2.set_xticklabels([str(j) for j in J_values])
ax2.set_yticks(range(len(AUC_values)))
ax2.set_yticklabels([str(a) for a in AUC_values])
ax2.set_xlabel('Ensemble size $J$')
ax2.set_ylabel('Signal AUC')
ax2.set_title('95% CI Coverage (%)')
for i in range(len(AUC_values)):
    for j in range(len(J_values)):
        val = coverage_data[i, j]
        color = 'white' if val >= 95 else 'black'
        ax2.text(j, i, f'{val:d}', ha='center', va='center',
                 fontsize=10, fontweight='bold', color=color)
cbar2 = fig.colorbar(im2, ax=ax2, shrink=0.8)

plt.tight_layout()

out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig_identifiability_heatmap.pdf')
print(f"Saved: {out_dir / 'fig_identifiability_heatmap.pdf'}")
plt.close()
