import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/_project/data/f2_per_problem.csv')

# Okabe-Ito palette
color_pw = '#E69F00'  # orange for ProofWriter
color_fo = '#56B4E9'  # sky blue for FOLIO

# Classify flip type
df['flip_type'] = 'no-flip'
df.loc[(df['sica_flipped'] == 1) & (df['sica_correct'] == 1), 'flip_type'] = 'correct-flip'
df.loc[(df['sica_flipped'] == 1) & (df['sica_correct'] == 0), 'flip_type'] = 'wrong-flip'

marker_map = {'no-flip': 'o', 'correct-flip': '^', 'wrong-flip': 'v'}
color_map = {'proofwriter': color_pw, 'folio': color_fo}

fig, ax = plt.subplots(figsize=(6, 4.5))

for dataset in ['proofwriter', 'folio']:
    for flip_type in ['no-flip', 'correct-flip', 'wrong-flip']:
        mask = (df['dataset'] == dataset) & (df['flip_type'] == flip_type)
        sub = df[mask]
        if len(sub) == 0:
            continue

        edgecolor = color_map[dataset]
        if flip_type == 'no-flip':
            facecolor = '#AAAAAA'
            alpha = 0.4
            zorder = 1
        elif flip_type == 'correct-flip':
            facecolor = '#009E73'  # Okabe-Ito green
            alpha = 0.8
            zorder = 3
        else:
            facecolor = '#D55E00'  # Okabe-Ito vermillion
            alpha = 0.8
            zorder = 2

        ax.scatter(
            sub['vote_entropy'],
            sub['constraint_exclusion_rate'],
            marker=marker_map[flip_type],
            c=facecolor,
            edgecolors=edgecolor,
            linewidths=0.8,
            s=40,
            alpha=alpha,
            zorder=zorder,
        )

# Legend: dataset colors
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='s', color='w', markerfacecolor=color_pw, markeredgecolor=color_pw, markersize=8, label='ProofWriter'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor=color_fo, markeredgecolor=color_fo, markersize=8, label='FOLIO'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#AAAAAA', markeredgecolor='k', markersize=8, label='No flip'),
    Line2D([0], [0], marker='^', color='w', markerfacecolor='#009E73', markeredgecolor='k', markersize=8, label='Correct flip'),
    Line2D([0], [0], marker='v', color='w', markerfacecolor='#D55E00', markeredgecolor='k', markersize=8, label='Wrong flip'),
]
ax.legend(handles=legend_elements, fontsize=10, frameon=True, fancybox=False, edgecolor='#CCCCCC', loc='upper right')

ax.set_xlabel('Vote entropy', fontsize=12)
ax.set_ylabel('Constraint exclusion rate', fontsize=12)
ax.tick_params(labelsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

out1 = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/figures/paper/fig2_capability_scatter.pdf'
out2 = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/fig2_capability_scatter.pdf'

fig.savefig(out1, dpi=300, bbox_inches='tight')
fig.savefig(out2, dpi=300, bbox_inches='tight')
plt.close()

print(f"Saved to:\n  {out1}\n  {out2}")
