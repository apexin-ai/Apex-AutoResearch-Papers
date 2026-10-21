#!/usr/bin/env python3
"""Generate appendix figure: Baseline MMLU accuracy vs max accuracy change.

Scatter plot showing vulnerability gradient: models below ~64% baseline
benefit from contamination, models above are harmed or immune.
Data source: 6 Family Summary (memory.md, report.md).
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
})

# Model data: (baseline_mmlu_d000, max_delta_acc)
# From memory.md 6 Family Summary and appendix text
models = {
    'OLMo-2 7B':     (53.79,  3.46),
    'Gemma-2 9B':    (61.86,  3.76),
    'Qwen2.5-7B':    (66.11, -3.13),
    'Qwen2.5-14B':   (69.44, -9.97),
    'Phi-4 14.7B':   (76.44,  0.54),
}

COLORS = {
    'OLMo-2 7B':     '#9467bd',
    'Gemma-2 9B':    '#d62728',
    'Qwen2.5-7B':    '#2ca02c',
    'Qwen2.5-14B':   '#ff7f0e',
    'Phi-4 14.7B':   '#1f77b4',
}

MARKERS = {
    'OLMo-2 7B':     'v',
    'Gemma-2 9B':    'D',
    'Qwen2.5-7B':    '^',
    'Qwen2.5-14B':   's',
    'Phi-4 14.7B':   'o',
}

fig, ax = plt.subplots(figsize=(8, 5.5))

for name, (baseline, delta) in models.items():
    ax.scatter(baseline, delta, color=COLORS[name], marker=MARKERS[name],
               s=150, zorder=5, edgecolors='white', linewidths=0.5)
    # Label positioning: offset to avoid overlap
    offsets = {
        'OLMo-2 7B':     (-1.5, 0.8),
        'Gemma-2 9B':    (0.8, 0.5),
        'Qwen2.5-7B':    (-1.5, -1.2),
        'Qwen2.5-14B':   (0.8, -0.8),
        'Phi-4 14.7B':   (1.0, 0.5),
    }
    dx, dy = offsets[name]
    ax.annotate(name, (baseline, delta), xytext=(baseline + dx, delta + dy),
                fontsize=10, fontweight='medium', color=COLORS[name],
                ha='left' if dx > 0 else 'right', va='bottom' if dy > 0 else 'top')

# Threshold line at ~64%
ax.axvline(64, color='gray', linestyle='--', linewidth=1.0, alpha=0.7)
ax.text(64.3, 3.5, '~64%\nthreshold', fontsize=8, color='gray',
        ha='left', va='top')

# Zero line
ax.axhline(0, color='black', linewidth=0.8)

ax.set_xlabel('Baseline MMLU Accuracy (%, d=0)')
ax.set_ylabel(r'Max $\Delta$ Accuracy (%)')
ax.yaxis.grid(True, alpha=0.3)
ax.xaxis.grid(True, alpha=0.3)

plt.tight_layout()

out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig_baseline_vs_effect.pdf')
print(f"Saved: {out_dir / 'fig_baseline_vs_effect.pdf'}")
plt.close()
