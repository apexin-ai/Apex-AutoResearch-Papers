import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from palette import BLUE, CORAL, TEAL, AMBER, RCPARAMS

plt.rcParams.update(RCPARAMS)

# --- Data from paper ---
benchmarks = ['PIQA', 'HellaSwag', 'ARC-Easy', 'LAMBADA']
alpha_values = [0.14, 0.15, 0.21, 0.30]
categories = ['Reasoning', 'Reasoning', 'Mixed', 'Retrieval']

# Routing gains (pp over majority vote)
routing_gains = [-0.6, 0.0, 1.0, 5.3]

# Oracle gap extraction (%)
oracle_pct = [0, 0, 12, 36]  # approximate from paper

# Colors by category
cat_colors = {
    'Reasoning': BLUE,
    'Mixed': CORAL,
    'Retrieval': AMBER,
}
bar_colors = [cat_colors[c] for c in categories]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.5, 2.0), gridspec_kw={'width_ratios': [1, 1]})

# --- Panel (a): Alpha spectrum ---
x = np.arange(len(benchmarks))
bars = ax1.bar(x, alpha_values, color=bar_colors, width=0.6, edgecolor='white', linewidth=0.5)

# Add value labels
for i, (bar, val) in enumerate(zip(bars, alpha_values)):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.008,
             f'{val:.2f}', ha='center', va='bottom', fontsize=6.5, fontweight='bold')

ax1.set_xticks(x)
ax1.set_xticklabels(benchmarks, rotation=0)
ax1.set_ylabel('Ambiguity $\\alpha$')
ax1.set_ylim(0, 0.38)
ax1.set_title('(a) Per-example ambiguity', pad=6)

# Category legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=cat_colors['Reasoning'], label='Reasoning'),
    Patch(facecolor=cat_colors['Mixed'], label='Mixed'),
    Patch(facecolor=cat_colors['Retrieval'], label='Retrieval'),
]
ax1.legend(handles=legend_elements, loc='upper left', frameon=False)

# --- Panel (b): Routing gain ---
bars2 = ax2.bar(x, routing_gains, color=bar_colors, width=0.6, edgecolor='white', linewidth=0.5)

for i, (bar, val) in enumerate(zip(bars2, routing_gains)):
    offset = 0.15 if val >= 0 else -0.35
    ax2.text(bar.get_x() + bar.get_width()/2, val + offset,
             f'{val:+.1f}', ha='center', va='bottom' if val >= 0 else 'top',
             fontsize=6.5, fontweight='bold')

ax2.set_xticks(x)
ax2.set_xticklabels(benchmarks, rotation=0)
ax2.set_ylabel('Routing gain over MV (pp)')
ax2.axhline(y=0, color='grey', linewidth=0.8, linestyle='-')
ax2.set_ylim(-2, 7)
ax2.set_title('(b) Confidence-based routing', pad=6)

plt.tight_layout(w_pad=2.5)

outdir = os.path.dirname(os.path.abspath(__file__))
paper_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/figures'
os.makedirs(paper_dir, exist_ok=True)

for d in [outdir, paper_dir]:
    plt.savefig(os.path.join(d, 'fig3_alpha_routing.pdf'))
    plt.savefig(os.path.join(d, 'fig3_alpha_routing.png'), dpi=300)
plt.close()
print("Saved fig3_alpha_routing")
