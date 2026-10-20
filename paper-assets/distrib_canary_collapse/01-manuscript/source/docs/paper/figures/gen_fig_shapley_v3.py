"""
Shapley value decomposition: method contributions to FPR and FNR.
narrative_intent: "PermG provides the best FPR-FNR tradeoff among
directional methods; NaiveXCorr dominates FPR cost."
Uses v3 data (6 null seeds, 36 null observations).
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

with open('artifacts/shapley_v3/shapley_values_v3.json') as f:
    d = json.load(f)

fpr = d['main_result_6pair']['fpr_shapley']
fnr = d['main_result_6pair']['fnr_shapley']
combined = d['main_result_6pair']['combined_shapley']

method_order = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']
method_labels = ['Naive\nXCorr', 'Diff.\nXCorr', 'Threshold\nOnset', 'Perm.\nGranger', 'Toda-\nYamamoto']

colors_pos = '#B2182B'
colors_neg = '#1B7837'
hero_color = '#2166AC'

fig, axes = plt.subplots(1, 3, figsize=(5.5, 2.5), sharey=False)

datasets = [
    ('FPR contribution', fpr, 'increases\nFPR', 'reduces\nFPR'),
    ('FNR contribution', fnr, 'increases\nFNR', 'reduces\nFNR'),
    ('Combined (FPR+FNR)', combined, 'net\nharm', 'net\nbenefit'),
]

x = np.arange(len(method_order))

for ax, (title, vals_dict, pos_label, neg_label) in zip(axes, datasets):
    vals = [vals_dict[m] for m in method_order]
    bar_colors = []
    for i, (v, m) in enumerate(zip(vals, method_order)):
        if m == 'perm_granger':
            bar_colors.append(hero_color)
        elif v > 0:
            bar_colors.append(colors_pos)
        else:
            bar_colors.append(colors_neg)

    bars = ax.bar(x, vals, 0.65, color=bar_colors, alpha=0.85,
                  edgecolor='white', linewidth=0.3)

    # Value labels
    for i, v in enumerate(vals):
        offset = 0.01 if v >= 0 else -0.01
        va = 'bottom' if v >= 0 else 'top'
        ax.text(i, v + offset, f'{v:+.3f}', ha='center', va=va,
                fontsize=5.5, fontweight='bold' if method_order[i] == 'perm_granger' else 'normal')

    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(method_labels, fontsize=6)
    ax.set_title(title, fontsize=8, fontweight='bold')
    ax.yaxis.grid(True, alpha=0.15, linewidth=0.4)
    ax.set_axisbelow(True)

    # Semantic annotations
    ymin, ymax = ax.get_ylim()
    ax.text(4.6, ymax * 0.85, pos_label, fontsize=5, color=colors_pos,
            ha='right', va='top', fontstyle='italic', alpha=0.7)
    ax.text(4.6, ymin * 0.85, neg_label, fontsize=5, color=colors_neg,
            ha='right', va='bottom', fontstyle='italic', alpha=0.7)

axes[0].set_ylabel('Shapley value')

plt.tight_layout()
plt.savefig('docs/paper/figures/fig_shapley_contribution.pdf')
plt.savefig('docs/paper/figures/fig_shapley_contribution.png')
print('Saved fig_shapley_contribution.pdf + .png')
