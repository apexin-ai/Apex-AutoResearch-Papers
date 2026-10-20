import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

relations = ['Compare', 'Feature-of', 'Part-of', 'Evaluate-for', 'Hyponym-of', 'Used-for', 'Conjunction']
unconstrained = [42.42, 33.54, 25.00, 24.06, 14.52, 0.76, 0.00]
grammar_only  = [40.85, 31.98, 23.38, 23.13, 14.40, 0.25, 0.00]
semantic_only = [29.23, 26.28, 11.27, 23.13,  7.09, 0.77, 0.00]
full_s1       = [ 2.82,  1.21,  0.00,  5.76,  0.00, 0.00, 0.00]

# Monochromatic blue — darker = higher violations
colors = {
    'Unconstrained': '#2B4C7E',  # 深蓝
    'Grammar-only':  '#5B7FAD',  # 中蓝
    'Semantic-only': '#8BAED4',  # 浅蓝
    'Full S1':       '#BAD4F0',  # 极浅蓝
}

n = len(relations)
x = np.arange(n)
width = 0.19
offsets = [-1.5, -0.5, 0.5, 1.5]

fig, ax = plt.subplots(figsize=(8, 3.5))

datasets = [
    ('Unconstrained', unconstrained),
    ('Grammar-only',  grammar_only),
    ('Semantic-only', semantic_only),
    ('Full S1',       full_s1),
]

for (label, data), off in zip(datasets, offsets):
    ax.bar(x + off * width, data, width, label=label, color=colors[label],
           edgecolor='white', linewidth=0.5)

ax.axhline(y=5, color='#AAAAAA', linestyle='--', linewidth=0.8, zorder=0)
ax.text(n - 0.5, 5.8, '5% threshold', color='#888888', fontsize=8,
        ha='right', va='bottom')

# Annotate Evaluate-for Semantic-only bar
eval_idx = relations.index('Evaluate-for')
sem_val = semantic_only[eval_idx]
ax.annotate('≈ unconstrained', xy=(eval_idx + 0.5 * width, sem_val),
            xytext=(eval_idx + 0.5 * width + 0.35, sem_val + 6),
            fontsize=7.5, color='#555555',
            arrowprops=dict(arrowstyle='->', color='#888888', lw=0.8),
            ha='left', va='bottom')

ax.set_xticks(x)
ax.set_xticklabels(relations, rotation=17, ha='right')
ax.set_ylabel('Domain/Range Violation Rate (%)')
ax.set_ylim(0, 50)
ax.legend(loc='upper right', frameon=True, framealpha=0.9, edgecolor='#DDDDDD')

plt.tight_layout()

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/figures/fig2_per_relation_dr'
fig.savefig(out_base + '.pdf')
fig.savefig(out_base + '.png')
plt.close()
print('Done')
