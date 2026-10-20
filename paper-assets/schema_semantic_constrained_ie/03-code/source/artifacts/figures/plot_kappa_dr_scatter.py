#!/usr/bin/env python3
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
})

data_path = Path(__file__).parent / 'kappa_dr_data.json'
with open(data_path) as f:
    data = json.load(f)

sci_k = [r['kappa'] for r in data['scierc']]
sci_dr = [r['dr_pct'] for r in data['scierc']]
sci_labels = [r['relation'] for r in data['scierc']]
sci_n = [r['n_predicted'] for r in data['scierc']]

doc_k = [r['kappa'] for r in data['docred']]
doc_dr = [r['dr_pct'] for r in data['docred']]
doc_labels = [r.get('name', r['relation']) for r in data['docred']]
doc_n = [r['n_predicted'] for r in data['docred']]

# Only use relations with > 0 predictions for regression
sci_k_reg = np.array([k for k, n in zip(sci_k, sci_n) if n > 0])
sci_dr_reg = np.array([d for d, n in zip(sci_dr, sci_n) if n > 0])
doc_k_reg = np.array([k for k, n in zip(doc_k, doc_n) if n > 0])
doc_dr_reg = np.array([d for d, n in zip(doc_dr, doc_n) if n > 0])

sci_slope, sci_int, sci_r, sci_p, _ = stats.linregress(sci_k_reg, sci_dr_reg)
sci_r2 = sci_r ** 2
doc_slope, doc_int, doc_r, doc_p, _ = stats.linregress(doc_k_reg, doc_dr_reg)
doc_r2 = doc_r ** 2

fig, ax = plt.subplots(figsize=(5.5, 4.0))

sci_sizes = [max(20, min(120, n * 0.15)) for n in sci_n]
doc_sizes = [max(15, min(80, n * 0.03)) for n in doc_n]

ax.scatter(sci_k, sci_dr, c='#2166ac', marker='o', s=sci_sizes,
           alpha=0.85, edgecolors='#2166ac', linewidths=0.5,
           label='SciERC', zorder=5)

doc_nonzero_k = [k for k, d, n in zip(doc_k, doc_dr, doc_n) if n > 0 and d > 0]
doc_nonzero_dr = [d for k, d, n in zip(doc_k, doc_dr, doc_n) if n > 0 and d > 0]
doc_nonzero_s = [max(15, min(80, n * 0.03)) for k, d, n in zip(doc_k, doc_dr, doc_n) if n > 0 and d > 0]

doc_zero_k = [k for k, d, n in zip(doc_k, doc_dr, doc_n) if n > 0 and d == 0]
doc_zero_dr = [d for k, d, n in zip(doc_k, doc_dr, doc_n) if n > 0 and d == 0]
doc_zero_s = [max(15, min(80, n * 0.03)) for k, d, n in zip(doc_k, doc_dr, doc_n) if n > 0 and d == 0]

doc_nopred_k = [k for k, n in zip(doc_k, doc_n) if n == 0]

ax.scatter(doc_nonzero_k, doc_nonzero_dr, c='#b2182b', marker='s', s=doc_nonzero_s,
           alpha=0.85, edgecolors='#b2182b', linewidths=0.5,
           label='DocRED', zorder=4)

np.random.seed(42)
jittered_y = np.random.uniform(-0.6, 0.6, len(doc_zero_k))
ax.scatter(doc_zero_k, jittered_y, c='#b2182b', marker='s', s=doc_zero_s,
           alpha=0.3, edgecolors='#b2182b', linewidths=0.3, zorder=3)

x_sci = np.linspace(sci_k_reg.min() - 0.03, sci_k_reg.max() + 0.03, 50)
ax.plot(x_sci, sci_slope * x_sci + sci_int, '--', color='#2166ac', linewidth=1.2, zorder=2,
        label=f'SciERC: slope={sci_slope:.1f}, $R^2$={sci_r2:.2f}')
x_doc = np.linspace(doc_k_reg.min() - 0.03, doc_k_reg.max() + 0.03, 50)
y_doc = doc_slope * x_doc + doc_int
y_doc = np.clip(y_doc, -1, 50)
ax.plot(x_doc, y_doc, '--', color='#b2182b', linewidth=1.2, zorder=2,
        label=f'DocRED: slope={doc_slope:.1f}, $R^2$={doc_r2:.2f}')

outliers = []
for i, (k, d, lab) in enumerate(zip(sci_k, sci_dr, sci_labels)):
    if d > 10:
        outliers.append((k, d, lab, '#2166ac'))

for i, (k, d, lab, n) in enumerate(zip(doc_k, doc_dr, doc_labels, doc_n)):
    if n > 0 and d > 15:
        outliers.append((k, d, lab, '#b2182b'))

for kv, dv, lab, col in outliers:
    offset_x = 8
    offset_y = 5
    if lab == 'Compare':
        offset_y = -8
        offset_x = -10
    elif lab == 'Evaluate-for':
        offset_x = -12
        offset_y = 4
    elif lab == 'product or material produced':
        lab = 'product/material'
        offset_x = -12
        offset_y = -8
    elif lab == 'subclass of':
        offset_x = 8
        offset_y = 3
    ax.annotate(lab, (kv, dv), fontsize=7.5,
                xytext=(offset_x, offset_y), textcoords='offset points',
                color=col, fontstyle='italic',
                arrowprops=dict(arrowstyle='-', color=col, lw=0.5))

n_zero = len(doc_zero_k)
n_total_sci = len(sci_k)
n_total_doc = len([n for n in doc_n if n > 0])
ax.text(0.02, 0.97,
        f'{n_total_sci} SciERC + {n_total_doc} DocRED relations\n'
        f'({n_zero} DocRED at DR=0%, jittered)\n'
        f'Within each schema, $\\kappa$ positively\n'
        f'correlates with violation rate',
        transform=ax.transAxes, fontsize=7, va='top', ha='left',
        color='#555555')

ax.set_xlabel(r'Constraint Tightness $\kappa(r) = 1 - |\mathcal{V}_r| / |\mathcal{E}|^2$')
ax.set_ylabel('DR Violation Rate (%)')
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-2, 45)
ax.axhline(y=0, color='#cccccc', linewidth=0.5, zorder=1)

ax.legend(loc='upper left', framealpha=0.9, edgecolor='#cccccc',
          bbox_to_anchor=(0.0, 0.72))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

out_dir = Path(__file__).parent
fig.savefig(out_dir / 'kappa_vs_dr_scatter.pdf', format='pdf')
fig.savefig(out_dir / 'kappa_vs_dr_scatter.png', format='png')
plt.close()

print(f"Saved. SciERC: slope={sci_slope:.1f}, R²={sci_r2:.3f}, p={sci_p:.2e}")
print(f"       DocRED: slope={doc_slope:.1f}, R²={doc_r2:.3f}, p={doc_p:.2e}")
print(f"SciERC: {n_total_sci} relations, DocRED: {n_total_doc} relations (+ {len(doc_nopred_k)} with 0 predictions)")
