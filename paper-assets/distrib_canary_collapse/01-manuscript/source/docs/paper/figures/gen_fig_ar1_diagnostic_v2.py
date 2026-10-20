#!/usr/bin/env python3
"""Figure 18: AR(1) diagnostic — vertical layout.
Two stacked panels: (a) Token Entropy, (b) Distinct-1.
Data from empirical_ar1_coefficients.json."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json
from pathlib import Path

OUT = Path(__file__).parent
DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/empirical_ar1_coefficients.json')

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
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

exps = d['experiments']

configs = [
    ('a000_s42', '$\\alpha{=}0.00$'),
    ('a025_s42', '$\\alpha{=}0.25$'),
    ('a050_s42', '$\\alpha{=}0.50$'),
    ('a075_s42', '$\\alpha{=}0.75$'),
    ('a100_s42', '$\\alpha{=}1.00$'),
]

metrics = [
    ('token_entropy', 'Token Entropy'),
    ('distinct_1', 'Distinct-1'),
]

x = np.arange(len(configs))
width = 0.35

fig, axes = plt.subplots(2, 1, figsize=(3.4, 5.0), sharex=True)

for ax, (metric_key, metric_label) in zip(axes, metrics):
    raw_vals = [exps[k][metric_key]['ar1_raw'] for k, _ in configs]
    diff_vals = [exps[k][metric_key]['ar1_diff'] for k, _ in configs]

    bars_raw = ax.bar(x - width/2, raw_vals, width, label='Raw',
                      color='#4393C3', edgecolor='white', linewidth=0.3)
    bars_diff = ax.bar(x + width/2, diff_vals, width, label='First-diff',
                       color='#E08214', edgecolor='white', linewidth=0.3)

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axhline(0.95, color='#B2182B', linewidth=0.8, linestyle='--', alpha=0.7)
    ax.axhline(-0.95, color='#B2182B', linewidth=0.8, linestyle='--', alpha=0.7)

    if metric_key == 'token_entropy':
        ax.text(len(configs) - 0.6, 0.97, '$\\varphi = 0.95$', fontsize=6.5,
                color='#B2182B', ha='right', va='bottom')

    panel = '(a)' if metric_key == 'token_entropy' else '(b)'
    ax.set_title(f'{panel}  {metric_label}', fontsize=9, fontweight='bold', loc='left', pad=4)
    ax.set_ylabel('AR(1) coefficient $\\varphi$', fontsize=8)
    ax.set_ylim(-1.1, 1.15)
    ax.yaxis.grid(True, alpha=0.15, linewidth=0.3)
    ax.set_axisbelow(True)
    ax.legend(fontsize=7, loc='upper left', framealpha=0.8, edgecolor='none')

axes[-1].set_xticks(x)
axes[-1].set_xticklabels([label for _, label in configs], fontsize=8)

fig.tight_layout(h_pad=1.0)

for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'fig_ar1_diagnostic.{fmt}', dpi=300)
plt.close()
print('Saved fig_ar1_diagnostic.pdf + .png')
