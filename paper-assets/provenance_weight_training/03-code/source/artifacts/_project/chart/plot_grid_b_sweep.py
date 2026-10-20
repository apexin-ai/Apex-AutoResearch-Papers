"""Fig 1: Grid-b Sweep curve (ρ=0.4)."""
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

# Data
b_seed42 = [0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
ppl_seed42 = [17.640, 17.651, 17.692, 17.718, 17.741, 17.774, 17.818]

b_seed123 = [0.5]
ppl_seed123 = [17.638]

b_seed456 = [0.5]
ppl_seed456 = [17.650]

uniform_ppl = 17.694
adaptive_fix_ppl = 17.653

fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(b_seed42, ppl_seed42, 'o-', color='#1f77b4', label='seed=42', linewidth=1.8, markersize=5)
ax.plot(b_seed123, ppl_seed123, 's', color='#ff7f0e', label='seed=123', markersize=7)
ax.plot(b_seed456, ppl_seed456, '^', color='#2ca02c', label='seed=456', markersize=7)

ax.axhline(uniform_ppl, color='gray', linestyle='--', linewidth=1.2, label=f'Uniform ({uniform_ppl:.3f})')
ax.axhline(adaptive_fix_ppl, color='#d62728', linestyle='--', linewidth=1.2, label=f'Adaptive-fix ({adaptive_fix_ppl:.3f})')

# Annotate RUNNING points
for b_val, x_offset in [(0.1, 0), (0.2, 0)]:
    ax.annotate('RUNNING', xy=(b_val, uniform_ppl), fontsize=8, color='gray',
                ha='center', va='bottom', style='italic',
                xytext=(b_val, uniform_ppl + 0.015),
                arrowprops=dict(arrowstyle='-', color='gray', lw=0.8))

ax.set_xlabel('Reweighting strength $b$')
ax.set_ylabel('Eval PPL (holdout)')
ax.set_xlim(-0.1, 5.5)
ax.legend(loc='upper left', framealpha=0.9)

plt.tight_layout()
plt.savefig('artifacts/figures/grid_b_sweep.pdf')
plt.savefig('artifacts/figures/grid_b_sweep.png')
print("Saved grid_b_sweep.pdf / .png")
