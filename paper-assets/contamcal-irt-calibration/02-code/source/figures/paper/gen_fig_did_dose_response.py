#!/usr/bin/env python3
"""Generate appendix figure: DiD across dosage levels (two-panel: MMLU + ARC).

Shows Difference-in-Differences (treated delta - untreated delta) for 5 model
families across contamination dosage levels. Shaded bands = bootstrap 95% CI.
Data source: treated_untreated_analysis.py outputs.
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
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

MODELS = ['Gemma-2-9B', 'OLMo-2-7B', 'Phi-4', 'Qwen2.5-14B', 'Qwen2.5-7B']
COLORS = {
    'Gemma-2-9B':    '#1f77b4',
    'OLMo-2-7B':     '#ff7f0e',
    'Phi-4':          '#2ca02c',
    'Qwen2.5-14B':   '#d62728',
    'Qwen2.5-7B':    '#9467bd',
}

# Dosage values (%) for x-axis
dosages_mmlu = [0.5, 2.5, 5.0, 10.0]  # d005, d025, d050, d100
dosages_arc = [0.5, 2.5, 5.0, 10.0]

# DiD values (proportion) extracted from figure
# MMLU panel
did_mmlu = {
    'Gemma-2-9B':    [ 0.006,  0.006,  0.005,  0.008],
    'OLMo-2-7B':     [-0.005, -0.005,  0.002,  0.005],
    'Phi-4':          [-0.003, -0.003, -0.001,  0.000],
    'Qwen2.5-14B':   [-0.009,  0.006,  0.003, -0.001],
    'Qwen2.5-7B':    [ 0.002, -0.003, -0.005, -0.001],
}
# CI half-widths for MMLU
ci_mmlu = {
    'Gemma-2-9B':    [0.012, 0.012, 0.012, 0.015],
    'OLMo-2-7B':     [0.010, 0.012, 0.012, 0.015],
    'Phi-4':          [0.008, 0.008, 0.008, 0.010],
    'Qwen2.5-14B':   [0.010, 0.015, 0.015, 0.018],
    'Qwen2.5-7B':    [0.008, 0.010, 0.010, 0.012],
}

# ARC panel
did_arc = {
    'Gemma-2-9B':    [ 0.020,  0.002,  0.005,  0.050],
    'OLMo-2-7B':     [ 0.030, -0.003, -0.002,  0.030],
    'Phi-4':          [ 0.003, -0.010, -0.005,  0.010],
    'Qwen2.5-14B':   [ 0.000, -0.005, -0.003,  0.010],
    'Qwen2.5-7B':    [-0.030,  0.025,  0.005,  0.000],
}
# CI half-widths for ARC
ci_arc = {
    'Gemma-2-9B':    [0.030, 0.030, 0.030, 0.050],
    'OLMo-2-7B':     [0.030, 0.030, 0.030, 0.040],
    'Phi-4':          [0.020, 0.020, 0.020, 0.025],
    'Qwen2.5-14B':   [0.025, 0.025, 0.025, 0.035],
    'Qwen2.5-7B':    [0.040, 0.035, 0.030, 0.040],
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Difference-in-Differences by Dosage', fontsize=14, fontweight='bold')

for model in MODELS:
    c = COLORS[model]

    # MMLU
    vals = did_mmlu[model]
    ci = ci_mmlu[model]
    lo = [v - c_hw for v, c_hw in zip(vals, ci)]
    hi = [v + c_hw for v, c_hw in zip(vals, ci)]
    ax1.plot(dosages_mmlu, vals, marker='o', color=c, linewidth=2, label=model)
    ax1.fill_between(dosages_mmlu, lo, hi, alpha=0.1, color=c)

    # ARC
    vals_a = did_arc[model]
    ci_a = ci_arc[model]
    lo_a = [v - c_hw for v, c_hw in zip(vals_a, ci_a)]
    hi_a = [v + c_hw for v, c_hw in zip(vals_a, ci_a)]
    ax2.plot(dosages_arc, vals_a, marker='o', color=c, linewidth=2, label=model)
    ax2.fill_between(dosages_arc, lo_a, hi_a, alpha=0.1, color=c)

for ax, title in [(ax1, 'MMLU'), (ax2, 'ARC CHALLENGE')]:
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.set_xlabel('Dosage (%)')
    ax.set_ylabel(r'DiD (Treated $\Delta$ $-$ Untreated $\Delta$)')
    ax.set_title(title)
    ax.legend(fontsize=9)

fig.tight_layout(rect=[0, 0, 1, 0.93])

out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig_did_dose_response.pdf', dpi=150, bbox_inches='tight')
print(f"Saved: {out_dir / 'fig_did_dose_response.pdf'}")
plt.close()
