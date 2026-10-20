#!/usr/bin/env python3
"""Figure 25: Aggregated partial correlation — vertical layout (2 stacked panels).
(a) Contemporaneous, (b) Lagged. Aggregated across pairs per alpha level.
Data from partial_correlation_results.json."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json
from pathlib import Path
from collections import defaultdict

OUT = Path(__file__).parent
DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/partial_correlation_results.json')

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8.5,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

with open(DATA) as f:
    d = json.load(f)

alphas = [0.5, 0.75]
alpha_labels = [f'α={a}' for a in alphas]

# Aggregate: mean |r| across all pairs and seeds per alpha
agg = defaultdict(lambda: {'czero': [], 'cpart': [], 'lzero': [], 'lpart': []})
for rec in d['results']:
    alpha = rec['alpha']
    if alpha not in alphas:
        continue
    agg[alpha]['czero'].append(abs(rec['zero_order_r']))
    agg[alpha]['cpart'].append(abs(rec['partial_r']))
    agg[alpha]['lzero'].append(abs(rec['lagged_zero_order_r']))
    agg[alpha]['lpart'].append(abs(rec['lagged_partial_r']))

contemp_zero_mean = [np.mean(agg[a]['czero']) for a in alphas]
contemp_zero_err = [np.std(agg[a]['czero']) / np.sqrt(len(agg[a]['czero'])) for a in alphas]
contemp_part_mean = [np.mean(agg[a]['cpart']) for a in alphas]
contemp_part_err = [np.std(agg[a]['cpart']) / np.sqrt(len(agg[a]['cpart'])) for a in alphas]

lagged_zero_mean = [np.mean(agg[a]['lzero']) for a in alphas]
lagged_zero_err = [np.std(agg[a]['lzero']) / np.sqrt(len(agg[a]['lzero'])) for a in alphas]
lagged_part_mean = [np.mean(agg[a]['lpart']) for a in alphas]
lagged_part_err = [np.std(agg[a]['lpart']) / np.sqrt(len(agg[a]['lpart'])) for a in alphas]

x = np.arange(len(alphas))
width = 0.3

color_zero = '#2166AC'
color_part = '#B2182B'

fig, axes = plt.subplots(2, 1, figsize=(3.4, 5.0), sharex=True)

# (a) Contemporaneous
ax = axes[0]
ax.bar(x - width/2, contemp_zero_mean, width, yerr=contemp_zero_err,
       label='Zero-order', color=color_zero, alpha=0.85,
       edgecolor='white', linewidth=0.3, capsize=4, error_kw={'linewidth': 1.0})
ax.bar(x + width/2, contemp_part_mean, width, yerr=contemp_part_err,
       label='Partial (|gen)', color=color_part, alpha=0.85,
       edgecolor='white', linewidth=0.3, capsize=4, error_kw={'linewidth': 1.0})
ax.set_ylabel('Mean |r| across pairs')
ax.set_title('(a)  Contemporaneous', fontsize=10, fontweight='bold', loc='left')
ax.set_ylim(0, 1.05)
ax.legend(loc='upper right', framealpha=0.9, edgecolor='none')
ax.yaxis.grid(True, alpha=0.15, linewidth=0.3)
ax.set_axisbelow(True)

# (b) Lagged
ax = axes[1]
ax.bar(x - width/2, lagged_zero_mean, width, yerr=lagged_zero_err,
       label='Zero-order', color=color_zero, alpha=0.85,
       edgecolor='white', linewidth=0.3, capsize=4, error_kw={'linewidth': 1.0})
ax.bar(x + width/2, lagged_part_mean, width, yerr=lagged_part_err,
       label='Partial (|gen)', color=color_part, alpha=0.85,
       edgecolor='white', linewidth=0.3, capsize=4, error_kw={'linewidth': 1.0})
ax.set_ylabel('Mean |r| across pairs')
ax.set_title('(b)  Lagged (t → t+1)', fontsize=10, fontweight='bold', loc='left')
ax.set_ylim(0, 1.05)
ax.legend(loc='upper left', framealpha=0.9, edgecolor='none')
ax.yaxis.grid(True, alpha=0.15, linewidth=0.3)
ax.set_axisbelow(True)

ax.set_xticks(x)
ax.set_xticklabels(alpha_labels)

fig.tight_layout(h_pad=1.0)

for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'fig_partial_correlation_agg.{fmt}', dpi=300)
plt.close()
print('Saved fig_partial_correlation_agg.pdf + .png (vertical)')
