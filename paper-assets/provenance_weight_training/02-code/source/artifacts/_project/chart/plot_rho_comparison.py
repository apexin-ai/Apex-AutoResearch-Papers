"""Fig 3: ρ=0.4 vs ρ=0.6 method comparison bar chart."""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

methods = ['Uniform', 'Adaptive\n(dual)', 'Grid-best', 'ESS-only']
ppl_04 = [17.694, 17.653, 17.640, 17.730]
ppl_06 = [17.766, 17.730, 17.704, 17.770]

x = np.arange(len(methods))
width = 0.35

fig, ax = plt.subplots(figsize=(6, 4))

bars1 = ax.bar(x - width/2, ppl_04, width, label=r'$\rho=0.4$', color='#1f77b4', edgecolor='white', linewidth=0.8)
bars2 = ax.bar(x + width/2, ppl_06, width, label=r'$\rho=0.6$', color='#d62728', edgecolor='white', linewidth=0.8)

# Value labels on bars
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.002,
            f'{bar.get_height():.3f}', ha='center', va='bottom', fontsize=8)
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.002,
            f'{bar.get_height():.3f}', ha='center', va='bottom', fontsize=8)

# Annotation for ρ=0.6 adaptive
ax.annotate(r'$\tau$=0.7 (opt.); $\tau$=0.8$\rightarrow$17.740',
            xy=(x[1] + width/2, 17.730), xytext=(x[1] + 0.6, 17.745),
            fontsize=8, color='#555555',
            arrowprops=dict(arrowstyle='->', color='#555555', lw=0.8))

ax.set_ylabel('Eval PPL (holdout)')
ax.set_xticks(x)
ax.set_xticklabels(methods)
ax.legend(loc='upper right', framealpha=0.9)

# Tighter y-axis to show differences
ax.set_ylim(17.60, 17.82)

plt.tight_layout()
plt.savefig('artifacts/figures/rho_comparison.pdf')
plt.savefig('artifacts/figures/rho_comparison.png')
print("Saved rho_comparison.pdf / .png")
