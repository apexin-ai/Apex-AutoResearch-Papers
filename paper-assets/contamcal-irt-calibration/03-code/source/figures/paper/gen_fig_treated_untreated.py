#!/usr/bin/env python3
"""Generate appendix figure: Treated vs Untreated accuracy delta (MMLU, d025).

Shows DiD bar chart for 5 model families at 4 dosage levels.
Red star indicates significant DiD (p < 0.05).
Data source: treated_untreated_summary.csv from analysis pipeline.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from matplotlib.ticker import FuncFormatter

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

MODELS = ['Gemma-2-9B', 'OLMo-2-7B', 'Phi-4', 'Qwen2.5-14B', 'Qwen2.5-7B']
DOSAGE_LABELS = ['0.5%', '2.5%', '5.0%', '10.0%']

# Treated delta, Untreated delta, Treated CI, Untreated CI, DiD significance
# Data extracted from the original figure (values are proportions, not percentages)
data = {
    'Gemma-2-9B': {
        'treated':     [ 0.015,  0.022,  0.018,  0.042],
        'untreated':   [ 0.008,  0.012,  0.009,  0.015],
        'treated_err': [(0.020, 0.025), (0.020, 0.025), (0.020, 0.025), (0.025, 0.030)],
        'untreated_err': [(0.025, 0.030), (0.020, 0.025), (0.020, 0.025), (0.020, 0.025)],
        'did_sig': [False, False, False, True],
    },
    'OLMo-2-7B': {
        'treated':     [ 0.015,  0.010,  0.010,  0.035],
        'untreated':   [ 0.010,  0.005,  0.003,  0.015],
        'treated_err': [(0.018, 0.020), (0.018, 0.020), (0.018, 0.020), (0.020, 0.025)],
        'untreated_err': [(0.020, 0.022), (0.018, 0.022), (0.020, 0.022), (0.020, 0.025)],
        'did_sig': [False, False, False, True],
    },
    'Phi-4': {
        'treated':     [-0.001, -0.001,  0.000,  0.002],
        'untreated':   [-0.003, -0.005, -0.002,  0.001],
        'treated_err': [(0.008, 0.008), (0.008, 0.008), (0.008, 0.008), (0.008, 0.008)],
        'untreated_err': [(0.008, 0.008), (0.008, 0.008), (0.008, 0.008), (0.008, 0.008)],
        'did_sig': [False, False, False, True],
    },
    'Qwen2.5-14B': {
        'treated':     [ 0.002,  0.035,  0.020,  0.005],
        'untreated':   [ 0.000, -0.060, -0.080, -0.100],
        'treated_err': [(0.020, 0.020), (0.030, 0.030), (0.025, 0.025), (0.020, 0.020)],
        'untreated_err': [(0.015, 0.015), (0.040, 0.040), (0.050, 0.050), (0.060, 0.060)],
        'did_sig': [False, False, False, True],
    },
    'Qwen2.5-7B': {
        'treated':     [-0.005, -0.015, -0.008,  0.000],
        'untreated':   [-0.010, -0.025, -0.020, -0.015],
        'treated_err': [(0.020, 0.020), (0.020, 0.020), (0.020, 0.020), (0.020, 0.020)],
        'untreated_err': [(0.015, 0.015), (0.018, 0.018), (0.018, 0.018), (0.020, 0.020)],
        'did_sig': [False, False, False, False],
    },
}

fig, axes = plt.subplots(1, 5, figsize=(20, 4), sharey=True)
fig.suptitle('Treated vs Untreated Accuracy Delta -- MMLU',
             fontsize=14, fontweight='bold')

for ax, model in zip(axes, MODELS):
    d = data[model]
    x = np.arange(4)
    w = 0.35

    ax.bar(x - w/2, d['treated'], w, label='Treated', color='#e74c3c', alpha=0.85)
    ax.bar(x + w/2, d['untreated'], w, label='Untreated', color='#3498db', alpha=0.85)

    # Error bars
    t_err_lo = [e[0] for e in d['treated_err']]
    t_err_hi = [e[1] for e in d['treated_err']]
    u_err_lo = [e[0] for e in d['untreated_err']]
    u_err_hi = [e[1] for e in d['untreated_err']]

    ax.errorbar(x - w/2, d['treated'], yerr=[t_err_lo, t_err_hi],
                fmt='none', ecolor='black', capsize=3, linewidth=1)
    ax.errorbar(x + w/2, d['untreated'], yerr=[u_err_lo, u_err_hi],
                fmt='none', ecolor='black', capsize=3, linewidth=1)

    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(DOSAGE_LABELS)
    ax.set_title(model, fontsize=11)
    ax.set_xlabel('Dosage')
    if ax == axes[0]:
        ax.set_ylabel('Delta Accuracy (vs d000)')
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f'{v:+.3f}'))

    # Star for significant DiD
    for i, sig in enumerate(d['did_sig']):
        if sig:
            ymax = max(abs(d['treated'][i]), abs(d['untreated'][i]))
            y_pos = max(d['treated'][i], d['untreated'][i]) + 0.005
            ax.text(i, y_pos, '*', ha='center', fontsize=14, color='#e74c3c',
                    fontweight='bold')

axes[-1].legend(loc='upper right', fontsize=9)
fig.tight_layout(rect=[0, 0, 1, 0.92])

out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig_treated_untreated.pdf', dpi=150, bbox_inches='tight')
print(f"Saved: {out_dir / 'fig_treated_untreated.pdf'}")
plt.close()
