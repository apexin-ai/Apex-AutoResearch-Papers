#!/usr/bin/env python3
"""fig_claim_evidence: Claim-evidence-scope summary figure (Appendix)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'custom',
    'mathtext.rm': 'Liberation Serif',
    'mathtext.it': 'Liberation Serif:italic',
    'mathtext.bf': 'Liberation Serif:bold',
})
import matplotlib.patches as mpatches
import os

rows = [
    {
        'finding': 'Training-Associated\nExit Collapse',
        'description': '$R^2$ drops at exit layers\nafter VLA fine-tuning',
        'evidence': '6/6 VLM→VLA conditions\nshow Δ > 0.10;\n0/4 VLA→VLA;\n0/10 reference conditions',
        'limitation': 'Correlational,\nnot causal',
        'color': '#FDEBD0',
        'edge': '#E8A838',
    },
    {
        'finding': 'Action-Relevant\nSensitivity',
        'description': 'Counterfactual perturbation\nreveals action-linked\nrepresentations',
        'evidence': "Cohen's $d$ ≥ 0.45 across\n8 trained conditions;\nempty ranks first in 6/8",
        'limitation': '$d$ vs cosine metric\nincomparability',
        'color': '#D5F5E3',
        'edge': '#52BE80',
    },
    {
        'finding': 'Inherited Instruction\nAttention Prior',
        'description': 'L1 attention patterns\ninherited from\npre-trained VLMs',
        'evidence': 'Reference VLMs already\nshow task-structured\nattention',
        'limitation': 'Not causally\ntested',
        'color': '#D6EAF8',
        'edge': '#5DADE2',
    },
]

col_labels = ['Finding', 'Evidence', 'Limitation']
col_colors = ['#2C3E50', '#2C3E50', '#2C3E50']

fig_w, fig_h = 7.0, 3.2
fig, ax = plt.subplots(figsize=(fig_w, fig_h))
ax.set_xlim(0, fig_w)
ax.set_ylim(0, fig_h)
ax.axis('off')

box_h = 0.72
row_gap = 0.18
top_y = fig_h - 0.55

col_x = [0.15, 1.65, 3.35, 5.55]
col_w = [1.35, 1.55, 2.05, 1.25]

header_y = top_y + 0.10
header_labels = ['Finding', '', 'Evidence', 'Limitation']
for ci in [0, 2, 3]:
    cx = col_x[ci] + col_w[ci] / 2
    ax.text(cx, header_y, header_labels[ci], ha='center', va='bottom',
            fontsize=11, fontweight='bold', color='#2C3E50')

for ri, row in enumerate(rows):
    y_center = top_y - ri * (box_h + row_gap) - box_h / 2

    for ci, (key, x, w) in enumerate(zip(
        ['finding', 'description', 'evidence', 'limitation'],
        col_x, col_w
    )):
        if ci == 0:
            fc = row['color']
            ec = row['edge']
            fw = 'bold'
            fs = 9
        elif ci == 1:
            fc = '#FAFAFA'
            ec = '#CCCCCC'
            fw = 'normal'
            fs = 8
        elif ci == 2:
            fc = '#F0F7FC'
            ec = '#85C1E9'
            fw = 'normal'
            fs = 8
        else:
            fc = '#FDF2F2'
            ec = '#E6A0A0'
            fw = 'normal'
            fs = 8

        rect = mpatches.FancyBboxPatch(
            (x, y_center - box_h / 2), w, box_h,
            boxstyle='round,pad=0.06',
            facecolor=fc, edgecolor=ec, linewidth=1.2
        )
        ax.add_patch(rect)
        ax.text(x + w / 2, y_center, row[key],
                ha='center', va='center', fontsize=fs, fontweight=fw,
                color='#333333', linespacing=1.3)

    for ci in range(3):
        x_start = col_x[ci] + col_w[ci] + 0.02
        x_end = col_x[ci + 1] - 0.02
        ax.annotate('', xy=(x_end, y_center), xytext=(x_start, y_center),
                     arrowprops=dict(arrowstyle='->', color='#888888',
                                     lw=1.5, shrinkA=0, shrinkB=0))

plt.tight_layout(pad=0.2)

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_dirs = [
    os.path.join(_REPO_ROOT, 'docs', 'paper', 'figures'),
    os.path.join(_REPO_ROOT, 'artifacts', 'figures', 'paper'),
]
for d in out_dirs:
    os.makedirs(d, exist_ok=True)
    fig.savefig(os.path.join(d, 'fig_claim_evidence.pdf'), dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(d, 'fig_claim_evidence.png'), dpi=300, bbox_inches='tight')

plt.close()
print('Saved fig_claim_evidence.')
