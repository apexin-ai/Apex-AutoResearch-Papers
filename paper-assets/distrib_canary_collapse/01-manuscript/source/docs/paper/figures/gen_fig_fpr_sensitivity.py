"""
FPR sensitivity analysis: observed vs hypothetical FPR=10% scenario.
narrative_intent: "Even under pessimistic FPR assumptions, PermG remains
the best directional method; K≥3 consensus is FPR-agnostic."
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
    'xtick.labelsize': 8,
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

with open('artifacts/fpr_sensitivity/fpr10_sensitivity.json') as f:
    d = json.load(f)

methods = ['PermG', 'TY\nGranger', 'Diff.\nXCorr', 'Threshold\nOnset', 'Naive\nXCorr']
method_keys = ['PermG', 'TY', 'DiffXCorr', 'ThresholdOnset', 'NaiveXCorr']

obs_fpr = d['fpr_inverse_ranking']['original']['fpr']
hyp_fpr = d['fpr_inverse_ranking']['fpr10_hypothesis']['fpr']

obs_vals = [obs_fpr[k] * 100 for k in method_keys]
hyp_vals = [hyp_fpr[k] * 100 for k in method_keys]

x = np.arange(len(methods))
bar_width = 0.35

fig, ax = plt.subplots(figsize=(4.0, 2.5))

bars1 = ax.bar(x - bar_width/2, obs_vals, bar_width,
               color='#4A90C4', alpha=0.85, label='Observed FPR',
               edgecolor='white', linewidth=0.3)
bars2 = ax.bar(x + bar_width/2, hyp_vals, bar_width,
               color='#E8A04C', alpha=0.75, label='Hypothetical (10%)',
               edgecolor='white', linewidth=0.3)

# Value labels
for i, (ov, hv) in enumerate(zip(obs_vals, hyp_vals)):
    ax.text(i - bar_width/2, ov + 1, f'{ov:.1f}', ha='center', va='bottom',
            fontsize=5.5, color='#4A90C4', fontweight='bold')
    ax.text(i + bar_width/2, hv + 1, f'{hv:.1f}', ha='center', va='bottom',
            fontsize=5.5, color='#E8A04C')

# 5% nominal line
ax.axhline(y=5, color='#CC5A5A', linewidth=0.6, linestyle='--', alpha=0.5)
ax.text(-0.5, 6, '5% nominal', fontsize=5.5, color='#CC5A5A', alpha=0.7)

ax.set_xticks(x)
ax.set_xticklabels(methods)
ax.set_ylabel('FPR (%)')
ax.set_ylim(0, 105)
ax.set_yticks([0, 25, 50, 75, 100])
ax.yaxis.grid(True, alpha=0.15, linewidth=0.4)
ax.set_axisbelow(True)

leg = ax.legend(loc='upper right', frameon=True, framealpha=0.9,
                edgecolor='#cccccc', borderpad=0.3)
leg.get_frame().set_linewidth(0.4)

plt.tight_layout()
plt.savefig('docs/paper/figures/fig_fpr_sensitivity.pdf')
plt.savefig('docs/paper/figures/fig_fpr_sensitivity.png')
print('Saved fig_fpr_sensitivity.pdf + .png')
