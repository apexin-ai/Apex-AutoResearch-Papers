import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from fig_style import apply_style
apply_style()

# --- Data ---
steps_008d = np.array([25000, 35000, 45000, 55000])
eval_008d = np.array([167.22, 146.34, 140.80, 82.75])
value_008d = np.array([25.86, 60.20, 97.50, 137.88])
entropy_008d = np.array([-3.47, -3.91, -4.35, -4.88])

steps_080 = np.array([5000, 15000, 25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000])
eval_080 = np.array([31.00, 104.88, 369.35, 404.96, 511.60, 690.31, 731.28, 846.47, 803.76, 848.61, 876.69])
value_080 = np.array([0.00, 3.89, 24.33, 88.37, 160.58, 230.51, 307.24, 386.44, 451.87, 515.48, 548.06])
entropy_080 = np.array([8.165, 1.824, 1.012, -1.501, -3.609, -4.689, -4.605, -4.873, -4.866, -4.981, -5.041])

steps_baseline = np.array([5000, 15000, 25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000])
eval_baseline = np.array([41.21, 106.01, 325.33, 354.49, 498.01, 534.13, 688.87, 656.85, 618.73, 596.24, 836.51])
value_baseline_sparse = {5000: 0, 25000: 45.78, 55000: 253.49, 105000: 539.34}
vb_steps = np.array(sorted(value_baseline_sparse.keys()))
vb_values = np.array([value_baseline_sparse[s] for s in vb_steps])

C_MAIN = '#D55E00'
C_BASE = '#999999'
C_HEALTHY = '#0072B2'

def to_k(steps):
    return steps / 1000

fig, axes = plt.subplots(2, 3, figsize=(10, 4.8),
                         gridspec_kw={'hspace': 0.45, 'wspace': 0.38,
                                      'top': 0.90, 'bottom': 0.10,
                                      'left': 0.06, 'right': 0.98})

# Column titles
for j, title in enumerate(['Eval Return', 'Value Mean', 'Actor Entropy']):
    axes[0, j].set_title(title, fontsize=13, fontweight='bold', pad=6)

mask_bl_a = (steps_baseline >= 25000) & (steps_baseline <= 55000)
steps_bl_a = steps_baseline[mask_bl_a]
eval_bl_a = eval_baseline[mask_bl_a]
mask_vb_a = (vb_steps >= 25000) & (vb_steps <= 55000)

# Row 0: CIVO (008d s1)
ax = axes[0, 0]
ax.plot(to_k(steps_bl_a), eval_bl_a, '--', color=C_BASE, lw=1.2, label='baseline')
ax.plot(to_k(steps_008d), eval_008d, '-o', color=C_MAIN, ms=3.5, label='008d')
ax.axvspan(to_k(35000), to_k(55000), alpha=0.10, color=C_MAIN)
ax.set_ylabel('CIVO (008d)', fontsize=11, fontweight='bold', color=C_MAIN)
ax.set_xlim(22, 58)
ax.tick_params(labelsize=10)
ax.legend(fontsize=9, framealpha=0.8, loc='upper right')

ax = axes[0, 1]
ax.plot(to_k(vb_steps[mask_vb_a]), vb_values[mask_vb_a], '--', color=C_BASE, lw=1.2)
ax.plot(to_k(steps_008d), value_008d, '-o', color=C_MAIN, ms=3.5)
ax.axvspan(to_k(35000), to_k(55000), alpha=0.10, color=C_MAIN)
ax.set_xlim(22, 58)
ax.tick_params(labelsize=10)
ax.annotate('+130%', xy=(55, 137.88), xytext=(40, 145),
            fontsize=10, color=C_MAIN, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=C_MAIN, lw=0.8))

ax = axes[0, 2]
ax.plot(to_k(steps_008d), entropy_008d, '-o', color=C_MAIN, ms=3.5)
ax.axvspan(to_k(35000), to_k(55000), alpha=0.10, color=C_MAIN)
ax.set_xlim(22, 58)
ax.tick_params(labelsize=10)

# Row 1: No CIVO (008e_v3 s1)
ax = axes[1, 0]
ax.plot(to_k(steps_baseline), eval_baseline, '--', color=C_BASE, lw=1.2, label='baseline')
ax.plot(to_k(steps_080), eval_080, '-o', color=C_HEALTHY, ms=3, label='008e_v3')
ax.set_ylabel('No CIVO (008e_v3)', fontsize=11, fontweight='bold', color=C_HEALTHY)
ax.set_xlabel('Steps (K)', fontsize=10)
ax.set_xlim(0, 110)
ax.tick_params(labelsize=10)
ax.legend(fontsize=9, framealpha=0.8, loc='upper left')

ax = axes[1, 1]
ax.plot(to_k(vb_steps), vb_values, '--', color=C_BASE, lw=1.2)
ax.plot(to_k(steps_080), value_080, '-o', color=C_HEALTHY, ms=3)
ax.set_xlabel('Steps (K)', fontsize=10)
ax.set_xlim(0, 110)
ax.tick_params(labelsize=10)

ax = axes[1, 2]
ax.plot(to_k(steps_080), entropy_080, '-o', color=C_HEALTHY, ms=3)
ax.set_xlabel('Steps (K)', fontsize=10)
ax.set_xlim(0, 110)
ax.tick_params(labelsize=10)

out_dir = os.path.dirname(__file__)
fig.savefig(f'{out_dir}/fig6_multiple_pathways.pdf', dpi=300)
fig.savefig(f'{out_dir}/fig6_multiple_pathways.png', dpi=150)
plt.close()
print('Done: 2x3 layout v2.')
