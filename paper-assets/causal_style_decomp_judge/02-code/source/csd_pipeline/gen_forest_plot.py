"""Generate forest plot (Figure 2): BT win probability for style dimensions."""
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

# Data (descending by effect size)
rows = [
    ("Qwen3-32B × Verbosity",  0.773, 0.703, 0.843, "<0.0001", True),
    ("GPT-4o × Verbosity",     0.760, 0.688, 0.828, "<0.0001", True),
    ("Qwen3-32B × Formality",  0.665, 0.585, 0.739, "<0.0001", True),
    ("GPT-4o × Formality",     0.630, 0.558, 0.703, "<0.001",  True),
    ("Qwen3-32B × Register",   0.593, 0.460, 0.713, "0.220",   False),
    ("GPT-4o × Register",      0.570, 0.500, 0.640, "0.040",   True),
]

colors = {
    'Verbosity': '#D55E00',
    'Formality': '#0072B2',
    'Register':  '#009E73',
}

fig, ax = plt.subplots(figsize=(7, 3.5))

n = len(rows)
y_positions = np.arange(n, 0, -1)  # top-to-bottom

for i, (label, bt, ci_lo, ci_hi, pval, sig) in enumerate(rows):
    y = y_positions[i]
    dim = label.split("× ")[-1]
    color = colors[dim]

    # alternating background
    if i % 2 == 0:
        ax.axhspan(y - 0.4, y + 0.4, color='#f5f5f5', zorder=0)

    # CI whisker
    ax.plot([ci_lo, ci_hi], [y, y], color=color, linewidth=1.8, solid_capstyle='butt', zorder=2)

    # marker
    marker = 'D'
    ax.scatter(bt, y, marker=marker, s=70, color=color if sig else 'white',
               edgecolors=color, linewidths=1.5, zorder=3)

    # left label
    ax.text(0.39, y, label, ha='right', va='center', fontsize=10)

    # right stats
    p_str = f"p{pval}" if pval.startswith("<") else f"p={pval}"
    stat_text = f"{bt:.3f}  [{ci_lo:.3f}, {ci_hi:.3f}]  {p_str}"
    ax.text(0.91, y, stat_text, ha='left', va='center', fontsize=8.5,
            fontfamily='DejaVu Sans Mono')

# null line
ax.axvline(x=0.5, color='#888888', linestyle='--', linewidth=1, zorder=1)
ax.text(0.5, 0.3, 'No preference', ha='center', va='top', fontsize=9, color='#888888')

ax.set_xlim(0.4, 0.9)
ax.set_ylim(0.5, n + 0.7)
ax.set_yticks([])
ax.set_xlabel("P(style-preferred wins)")
ax.spines['left'].set_visible(False)

# legend for significance
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='D', color='w', markerfacecolor='grey',
           markeredgecolor='grey', markersize=8, label='Significant'),
    Line2D([0], [0], marker='D', color='w', markerfacecolor='white',
           markeredgecolor='grey', markersize=8, label='Not significant'),
]
ax.legend(handles=legend_elements, loc='lower right', frameon=False, fontsize=9)

out = '/root/causal_style_decomp_judge/artifacts/figures/paper/forest_plot.pdf'
fig.savefig(out)
plt.close()
print(f"Saved: {out}")
