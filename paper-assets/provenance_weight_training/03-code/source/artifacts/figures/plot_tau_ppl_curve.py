"""Fig 2: τ-PPL curve for ρ=0.4 and ρ=0.6."""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

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

# Data ρ=0.4
tau_04 = [0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
ppl_04 = [17.678, 17.681, 17.660, 17.653, 17.699, 17.712]
uniform_04 = 17.694
best_idx_04 = 3  # τ=0.8

# Data ρ=0.6
tau_06 = [0.6, 0.7, 0.8]
ppl_06 = [17.736, 17.730, 17.740]
uniform_06 = 17.766
best_idx_06 = 1  # τ=0.7

fig, ax = plt.subplots(figsize=(6, 4))

# Safe range shading [0.5, 0.8] for ρ=0.4
ax.axvspan(0.5, 0.8, alpha=0.08, color='#1f77b4', label='Safe range [0.5, 0.8]')

# ρ=0.4
ax.plot(tau_04, ppl_04, 'o-', color='#1f77b4', linewidth=1.8, markersize=5, label=r'$\rho=0.4$')
ax.plot(tau_04[best_idx_04], ppl_04[best_idx_04], '*', color='#1f77b4', markersize=14, zorder=5)
ax.axhline(uniform_04, color='#1f77b4', linestyle='--', linewidth=1.0, alpha=0.6,
           label=f'Uniform ($\\rho$=0.4): {uniform_04:.3f}')

# ρ=0.6
ax.plot(tau_06, ppl_06, 's-', color='#d62728', linewidth=1.8, markersize=5, label=r'$\rho=0.6$')
ax.plot(tau_06[best_idx_06], ppl_06[best_idx_06], '*', color='#d62728', markersize=14, zorder=5)
ax.axhline(uniform_06, color='#d62728', linestyle='--', linewidth=1.0, alpha=0.6,
           label=f'Uniform ($\\rho$=0.6): {uniform_06:.3f}')

# Annotate optimal τ
ax.annotate(r'$\tau^*=0.8$', xy=(0.8, 17.653), xytext=(0.85, 17.645),
            fontsize=9, color='#1f77b4',
            arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=1.0))
ax.annotate(r'$\tau^*=0.7$', xy=(0.7, 17.730), xytext=(0.75, 17.722),
            fontsize=9, color='#d62728',
            arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.0))

ax.set_xlabel(r'Threshold $\tau$')
ax.set_ylabel('Eval PPL (holdout)')
ax.set_xlim(0.45, 1.0)
ax.legend(loc='upper right', framealpha=0.9)

plt.tight_layout()
plt.savefig('artifacts/figures/tau_ppl_curve.pdf')
plt.savefig('artifacts/figures/tau_ppl_curve.png')
print("Saved tau_ppl_curve.pdf / .png")
