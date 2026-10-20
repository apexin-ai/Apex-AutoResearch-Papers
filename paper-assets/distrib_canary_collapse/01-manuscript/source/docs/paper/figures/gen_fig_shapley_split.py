#!/usr/bin/env python3
"""Split Shapley value decomposition into 2 groups for cross-page layout.
Top: (a) FPR + (b) FNR. Bottom: (c) Combined."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import json
from pathlib import Path

OUT = Path(__file__).parent
DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json')

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

sv = d['main_result_6pair']

method_order = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']
method_labels = ['Naive\nXCorr', 'Diff.\nXCorr', 'Threshold\nOnset', 'Perm.\nGranger', 'Toda-\nYamamoto']

colors_pos = '#B2182B'
colors_neg = '#1B7837'
hero_color = '#2166AC'

datasets = [
    ('(a)  FPR contribution', sv['fpr_shapley'], 'increases FPR', 'reduces FPR'),
    ('(b)  FNR contribution (6-pair)', sv['fnr_shapley'], 'increases FNR', 'reduces FNR'),
    ('(c)  Combined (FPR + FNR)', sv['combined_shapley'], 'net harm', 'net benefit'),
]

x = np.arange(len(method_order))

def draw_panel(ax, title, vals_dict, pos_label, neg_label, show_xlabels=False):
    vals = [vals_dict[m] for m in method_order]
    bar_colors = []
    for v, m in zip(vals, method_order):
        if m == 'perm_granger':
            bar_colors.append(hero_color)
        elif v > 0:
            bar_colors.append(colors_pos)
        else:
            bar_colors.append(colors_neg)

    ax.bar(x, vals, 0.65, color=bar_colors, alpha=0.85,
           edgecolor='white', linewidth=0.3)

    for i, v in enumerate(vals):
        offset = 0.012 if v >= 0 else -0.012
        va = 'bottom' if v >= 0 else 'top'
        fw = 'bold' if method_order[i] == 'perm_granger' else 'normal'
        t = ax.text(i, v + offset, f'{v:+.3f}', ha='center', va=va,
                    fontsize=6.5, fontweight=fw)
        t.set_path_effects([pe.withStroke(linewidth=1.5, foreground='white')])

    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_title(title, fontsize=9, fontweight='bold', loc='left', pad=4)
    ax.set_ylabel('Shapley value', fontsize=8)
    ax.yaxis.grid(True, alpha=0.15, linewidth=0.3)
    ax.set_axisbelow(True)

    ymin, ymax = ax.get_ylim()
    ax.text(len(method_order) - 0.6, ymax * 0.85, pos_label, fontsize=6,
            color=colors_pos, ha='right', va='top', fontstyle='italic', alpha=0.7)
    ax.text(len(method_order) - 0.6, ymin * 0.85, neg_label, fontsize=6,
            color=colors_neg, ha='right', va='bottom', fontstyle='italic', alpha=0.7)

    if show_xlabels:
        ax.set_xticks(x)
        ax.set_xticklabels(method_labels, fontsize=7.5)
    else:
        ax.set_xticks(x)
        ax.set_xticklabels([])

# Group 1: panels (a) + (b)
fig1, axes1 = plt.subplots(2, 1, figsize=(3.4, 4.6), sharex=True)
draw_panel(axes1[0], *datasets[0])
draw_panel(axes1[1], *datasets[1], show_xlabels=True)
fig1.tight_layout(h_pad=0.8)
for fmt in ['pdf', 'png']:
    fig1.savefig(OUT / f'fig_shapley_contribution_top.{fmt}', dpi=300)
plt.close(fig1)

# Group 2: panel (c)
fig2, ax2 = plt.subplots(1, 1, figsize=(3.4, 2.4))
draw_panel(ax2, *datasets[2], show_xlabels=True)
fig2.tight_layout()
for fmt in ['pdf', 'png']:
    fig2.savefig(OUT / f'fig_shapley_contribution_bottom.{fmt}', dpi=300)
plt.close(fig2)

print('Saved fig_shapley_contribution_top + _bottom (.pdf + .png)')
