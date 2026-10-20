#!/usr/bin/env python3
"""Figure 24: Partial correlation — vertical layout (2 stacked panels).
(a) Contemporaneous, (b) Lagged. Data from partial_correlation_results.json."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
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
    'xtick.labelsize': 7,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
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

canaries = ['token_entropy', 'ece']
downstreams = ['distinct_1', 'distinct_2', 'distinct_3']
alphas = [0.5, 0.75]
canary_short = {'token_entropy': 'TE', 'ece': 'ECE'}
down_short = {'distinct_1': 'D1', 'distinct_2': 'D2', 'distinct_3': 'D3'}

# Aggregate across seeds: mean ± sem for |r|
groups = defaultdict(list)
for rec in d['results']:
    key = (rec['canary'], rec['downstream'], rec['alpha'])
    groups[key].append(rec)

labels = []
contemp_zero = []
contemp_zero_err = []
contemp_part = []
contemp_part_err = []
lagged_zero = []
lagged_zero_err = []
lagged_part = []
lagged_part_err = []

for alpha in alphas:
    for canary in canaries:
        for down in downstreams:
            key = (canary, down, alpha)
            recs = groups[key]
            if not recs:
                continue
            label = f"{canary_short[canary]}→{down_short[down]}\nα={alpha}"
            labels.append(label)

            czero = [abs(r['zero_order_r']) for r in recs]
            cpart = [abs(r['partial_r']) for r in recs]
            lzero = [abs(r['lagged_zero_order_r']) for r in recs]
            lpart = [abs(r['lagged_partial_r']) for r in recs]

            contemp_zero.append(np.mean(czero))
            contemp_zero_err.append(np.std(czero) / np.sqrt(len(czero)))
            contemp_part.append(np.mean(cpart))
            contemp_part_err.append(np.std(cpart) / np.sqrt(len(cpart)))
            lagged_zero.append(np.mean(lzero))
            lagged_zero_err.append(np.std(lzero) / np.sqrt(len(lzero)))
            lagged_part.append(np.mean(lpart))
            lagged_part_err.append(np.std(lpart) / np.sqrt(len(lpart)))

x = np.arange(len(labels))
width = 0.35

fig, axes = plt.subplots(2, 1, figsize=(5.5, 5.5), sharex=True)

color_zero = '#2166AC'
color_part = '#B2182B'

# (a) Contemporaneous
ax = axes[0]
ax.bar(x - width/2, contemp_zero, width, yerr=contemp_zero_err,
       label='Zero-order |r|', color=color_zero, alpha=0.85,
       edgecolor='white', linewidth=0.3, capsize=2, error_kw={'linewidth': 0.8})
ax.bar(x + width/2, contemp_part, width, yerr=contemp_part_err,
       label='Partial |r| (|gen)', color=color_part, alpha=0.85,
       edgecolor='white', linewidth=0.3, capsize=2, error_kw={'linewidth': 0.8})
ax.set_ylabel('|Pearson r|')
ax.set_title('(a)  Contemporaneous', fontsize=10, fontweight='bold', loc='left')
ax.set_ylim(0, 1.05)
ax.legend(loc='upper right', framealpha=0.9, edgecolor='none')
ax.yaxis.grid(True, alpha=0.15, linewidth=0.3)
ax.set_axisbelow(True)

# Add alpha-group separators
sep = len(canaries) * len(downstreams) - 0.5
ax.axvline(sep, color='gray', linewidth=0.5, linestyle='--', alpha=0.4)

# (b) Lagged
ax = axes[1]
ax.bar(x - width/2, lagged_zero, width, yerr=lagged_zero_err,
       label='Zero-order |r|', color=color_zero, alpha=0.85,
       edgecolor='white', linewidth=0.3, capsize=2, error_kw={'linewidth': 0.8})
ax.bar(x + width/2, lagged_part, width, yerr=lagged_part_err,
       label='Partial |r| (|gen)', color=color_part, alpha=0.85,
       edgecolor='white', linewidth=0.3, capsize=2, error_kw={'linewidth': 0.8})
ax.set_ylabel('|Pearson r|')
ax.set_title('(b)  Lagged (canary[t] → downstream[t+1])', fontsize=10, fontweight='bold', loc='left')
ax.set_ylim(0, 1.05)
ax.legend(loc='upper left', framealpha=0.9, edgecolor='none')
ax.yaxis.grid(True, alpha=0.15, linewidth=0.3)
ax.set_axisbelow(True)
ax.axvline(sep, color='gray', linewidth=0.5, linestyle='--', alpha=0.4)

ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=6.5)

fig.tight_layout(h_pad=1.0)

for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'fig_partial_correlation.{fmt}', dpi=300)
plt.close()
print('Saved fig_partial_correlation.pdf + .png (vertical)')
