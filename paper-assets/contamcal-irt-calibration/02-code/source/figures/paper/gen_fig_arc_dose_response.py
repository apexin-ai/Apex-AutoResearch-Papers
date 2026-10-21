#!/usr/bin/env python3
"""Generate appendix figure: ARC-Challenge dose-response curves.

Data source: s123 seed eval results (memory.md, appendix.tex).
Gemma-2 excluded due to evaluation artifact (non-monotonic oscillation).
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
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'lines.linewidth': 2.0,
    'grid.alpha': 0.3,
    'grid.linewidth': 0.5,
    'grid.linestyle': '--',
})

# ARC-Challenge accuracy (%) across dosages, s123 seed
# Data from appendix.tex and memory.md verified results
dosage_labels = ['0', '5', '25', '50', '100']
xpos = np.arange(5)

models = {
    'Phi-4 14.7B':   [92.07, 91.72, 92.32, 92.49, 92.56],
    'Qwen2.5-14B':   [91.04, 90.44, 88.82, 87.54, 88.40],
    'Qwen2.5-7B':    [87.88, 86.09, 84.13, 84.47, 85.07],
    'OLMo-2 7B':     [76.28, 76.62, 78.16, 79.61, 80.03],
}

MODEL_COLORS = {
    'Phi-4 14.7B':   '#1f77b4',
    'Qwen2.5-14B':   '#ff7f0e',
    'Qwen2.5-7B':    '#2ca02c',
    'OLMo-2 7B':     '#9467bd',
}

MODEL_MARKERS = {
    'Phi-4 14.7B':   'o',
    'Qwen2.5-14B':   's',
    'Qwen2.5-7B':    '^',
    'OLMo-2 7B':     'v',
}

fig, ax = plt.subplots(figsize=(7, 4.3))

for name in models:
    accs = models[name]
    ax.plot(xpos, accs, color=MODEL_COLORS[name], marker=MODEL_MARKERS[name],
            markersize=7, linewidth=2.0, label=name, zorder=3,
            markeredgecolor='white', markeredgewidth=0.5)

ax.set_xticks(xpos)
ax.set_xticklabels(dosage_labels)
ax.set_xlabel('Contamination Dosage (%)')
ax.set_ylabel('ARC Accuracy (%)')
ax.yaxis.grid(True)
ax.legend(loc='lower right', framealpha=0.9)

# Gemma-2 exclusion note

plt.tight_layout()

out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig_arc_dose_response.pdf')
print(f"Saved: {out_dir / 'fig_arc_dose_response.pdf'}")
plt.close()
