"""Plan A: Improved scatter plot with dfCAR correction arrows.
Shows TSR vs CAR with arrows dropping to dfCAR for action-collapsed models.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

fig, ax = plt.subplots(figsize=(5.5, 4.5), dpi=300)

# --- Data: (label, TSR, CAR, dfCAR, color, marker, markersize) ---
# Pi0 family (action-collapsed, dfCAR ≈ 0)
pi0_models = [
    ('Pi0+A1',    0.0, 91.5, 0.4, '#1f77b4', 'o', 55),
    ('Pi0 Full-FT', 0.5, 83.0, 0.4, '#1f77b4', 's', 45),
    ('Pi0 LoRA',  0.0, 82.0, 0.4, '#1f77b4', '^', 50),
]

# Oracle variants (also action-collapsed context, TSR ≈ 0)
oracle_models = [
    ('Oracle-feat.', 0.0, 76.9, None, '#9467bd', 'D', 40),
    ('A3 learned',   0.0, 77.1, None, '#9467bd', 'p', 50),
    ('Oracle-adpt.', 0.0, 75.0, None, '#9467bd', 'D', 40),
    ('Oracle-fixed', 0.0, 73.1, None, '#9467bd', 'D', 40),
]

# Pi0.5 baseline (no collapse, dfCAR = CAR)
pi05_baseline = ('Pi0.5', 71.5, 28.5, 28.5, '#2ca02c', 's', 55)

# Fine-tuned Pi0.5 (no collapse, dfCAR = CAR) — mean ± std across seeds
ft_models = [
    ('LoRA-only',       51.5, 54.67, 54.67, '#ff7f0e', 'o', 45),
    (r'SDF $\lambda$=0.005', 54.0, 54.5,  54.5,  '#d62728', '^', 45),
    (r'SDF $\lambda$=0.01',  53.8, 56.33, 56.33, '#d62728', 'v', 45),
    (r'SDF $\lambda$=0.1',   50.2, 57.00, 57.00, '#d62728', 'D', 40),
]

# --- Quadrant shading ---
ax.axhspan(60, 102, xmin=0, xmax=1, alpha=0.04, color='red', zorder=0)
ax.axvspan(40, 102, ymin=0, ymax=1, alpha=0.04, color='green', zorder=0)

# Quadrant labels
ax.text(97, 97, 'Genuinely\nSafe', ha='right', va='top', fontsize=7.5,
        color='#2ca02c', style='italic', alpha=0.7)
ax.text(3, 97, 'Action-Collapsed\n(Illusory Safety)', ha='left', va='top',
        fontsize=7.5, color='#cc0000', style='italic', alpha=0.7)

# --- Plot Pi0 family with staggered x for readability ---
x_offsets_pi0 = [1.5, 3.5, 5.5]
for i, (label, tsr, car, dfcar, color, marker, ms) in enumerate(pi0_models):
    x_plot = tsr + x_offsets_pi0[i]
    ax.scatter(x_plot, car, c=color, marker=marker, s=ms, zorder=5,
               edgecolors='black', linewidths=0.5)
    # dfCAR arrow
    ax.annotate('', xy=(x_plot, dfcar), xytext=(x_plot, car - 2),
                arrowprops=dict(arrowstyle='->', color=color, lw=1.2,
                                linestyle='--', alpha=0.5))
    # Label
    ax.annotate(label, (x_plot, car), xytext=(x_plot + 2, car + 1.5),
                fontsize=7, ha='left', va='bottom', color='#333333',
                arrowprops=dict(arrowstyle='-', lw=0.4, color='gray'))

# dfCAR landing zone annotation
ax.annotate('dfCAR $\\approx$ 0', xy=(3.5, 0.4), fontsize=7.5,
            ha='center', va='bottom', color='#1f77b4', style='italic')

# --- Plot oracle variants with staggered x ---
x_offsets_oracle = [7.5, 9.5, 11.5, 13.5]
for i, (label, tsr, car, dfcar, color, marker, ms) in enumerate(oracle_models):
    x_plot = tsr + x_offsets_oracle[i]
    ax.scatter(x_plot, car, c=color, marker=marker, s=ms, zorder=5,
               edgecolors='black', linewidths=0.5)

# Group label for oracles
oracle_cars = [m[2] for m in oracle_models]
ax.annotate('Oracle\nvariants', xy=(10.5, min(oracle_cars) - 1),
            fontsize=7, ha='center', va='top', color='#9467bd',
            style='italic')

# --- Plot Pi0.5 baseline ---
label, tsr, car, dfcar, color, marker, ms = pi05_baseline
ax.scatter(tsr, car, c=color, marker=marker, s=ms, zorder=5,
           edgecolors='black', linewidths=0.5)
ax.annotate('Pi0.5\n(no collapse)', (tsr, car), xytext=(tsr - 8, car - 8),
            fontsize=7.5, ha='right', va='top',
            arrowprops=dict(arrowstyle='->', lw=0.7, color='gray'),
            color='#333333')

# --- Plot fine-tuned Pi0.5 ---
for label, tsr, car, dfcar, color, marker, ms in ft_models:
    ax.scatter(tsr, car, c=color, marker=marker, s=ms, zorder=5,
               edgecolors='black', linewidths=0.5)

# Group label for fine-tuned
ft_cx = np.mean([m[1] for m in ft_models])
ft_cy = np.mean([m[2] for m in ft_models])
ax.annotate('Fine-tuned Pi0.5\n(LoRA / SDF)', (ft_cx, ft_cy),
            xytext=(ft_cx + 10, ft_cy + 12),
            fontsize=7.5, ha='left', va='bottom',
            arrowprops=dict(arrowstyle='->', lw=0.7, color='gray'),
            color='#333333')

# --- Arrow from Pi0.5 to fine-tuned cluster ---
arrow = FancyArrowPatch(
    (pi05_baseline[1], pi05_baseline[2]),
    (ft_cx - 2, ft_cy - 3),
    arrowstyle='->', mutation_scale=12, lw=1.2,
    color='#888888', linestyle=':', zorder=3)
ax.add_patch(arrow)
ax.text((pi05_baseline[1] + ft_cx) / 2 + 2,
        (pi05_baseline[2] + ft_cy) / 2 - 2,
        'LoRA\nfine-tuning', fontsize=6.5, ha='center', va='top',
        color='#888888', style='italic')

# --- Legend ---
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#1f77b4',
               markersize=7, markeredgecolor='black', markeredgewidth=0.3,
               label='Pi0-family'),
    plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='#9467bd',
               markersize=6, markeredgecolor='black', markeredgewidth=0.3,
               label='Oracle variants'),
    plt.Line2D([0], [0], marker='s', color='w', markerfacecolor='#2ca02c',
               markersize=7, markeredgecolor='black', markeredgewidth=0.3,
               label='Pi0.5 baseline'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#ff7f0e',
               markersize=7, markeredgecolor='black', markeredgewidth=0.3,
               label='LoRA-only'),
    plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='#d62728',
               markersize=7, markeredgecolor='black', markeredgewidth=0.3,
               label='LoRA+SDF'),
    plt.Line2D([0], [0], linestyle='--', color='#1f77b4', lw=1,
               alpha=0.5, label='CAR → dfCAR'),
]
ax.legend(handles=legend_elements, loc='center right', fontsize=6.5,
          framealpha=0.9, edgecolor='gray')

# --- Axes ---
ax.set_xlabel('Task Success Rate (%)', fontsize=10)
ax.set_ylabel('Collision Avoidance Rate (%)', fontsize=10)
ax.set_xlim(-3, 100)
ax.set_ylim(-5, 102)

plt.tight_layout()
outdir = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures'
plt.savefig(f'{outdir}/fig2_plan_a.pdf', bbox_inches='tight', dpi=300)
plt.savefig(f'{outdir}/fig2_plan_a.png', bbox_inches='tight', dpi=150)
print("Saved Plan A: fig2_plan_a.pdf/png")
