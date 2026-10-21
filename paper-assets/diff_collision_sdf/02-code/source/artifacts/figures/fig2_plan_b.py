"""Plan B: Dumbbell chart showing CAR vs dfCAR inflation gap.
Each model is one row; connected dots show how dfCAR correction deflates illusory safety.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# --- Data: (label, CAR, dfCAR, TSR, group) ---
models = [
    ('Pi0+A1 (SDF)',         91.5,  0.4,  0.0,  'collapsed'),
    ('Pi0 Full-FT',          83.0,  0.4,  0.5,  'collapsed'),
    ('Pi0 LoRA',             82.0,  0.4,  0.0,  'collapsed'),
    ('Pi0.5 (baseline)',     28.5, 28.5, 71.5,  'genuine'),
    ('LoRA-only',            54.67, 54.67, 51.5, 'finetuned'),
    (r'SDF $\lambda\!=\!0.01$',  56.33, 56.33, 53.8, 'finetuned'),
    (r'SDF $\lambda\!=\!0.1$',   57.00, 57.00, 50.2, 'finetuned'),
]

colors = {
    'collapsed': '#d62728',
    'genuine': '#2ca02c',
    'finetuned': '#ff7f0e',
}
group_labels = {
    'collapsed': 'Action-collapsed (inflated)',
    'genuine': 'No collapse',
    'finetuned': 'Fine-tuned Pi0.5 (no collapse)',
}

fig, ax = plt.subplots(figsize=(5.5, 3.2), dpi=300)

y_positions = list(range(len(models) - 1, -1, -1))

for i, (label, car, dfcar, tsr, group) in enumerate(models):
    y = y_positions[i]
    color = colors[group]
    gap = car - dfcar

    # Connecting line
    ax.plot([dfcar, car], [y, y], color=color, linewidth=2.5, alpha=0.4, zorder=2)

    # CAR dot (filled)
    ax.scatter(car, y, c=color, s=70, zorder=5, edgecolors='black', linewidths=0.5)

    # dfCAR dot (open)
    if abs(gap) > 1:
        ax.scatter(dfcar, y, c='white', s=70, zorder=5,
                   edgecolors=color, linewidths=1.5)
        # Gap annotation
        ax.text((car + dfcar) / 2, y + 0.3,
                f'$\\Delta$ = {gap:.0f} pp',
                ha='center', va='bottom', fontsize=7, color=color,
                style='italic')
    else:
        # Same point — dfCAR = CAR, show as single filled dot
        pass

# --- Vertical reference lines ---
ax.axvline(x=0, color='gray', linewidth=0.5, alpha=0.3)
ax.axvline(x=50, color='gray', linewidth=0.5, alpha=0.3, linestyle=':')

# --- Legend ---
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#d62728',
               markersize=8, markeredgecolor='black', markeredgewidth=0.5,
               label='CAR (reported)'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='white',
               markersize=8, markeredgecolor='#d62728', markeredgewidth=1.5,
               label='dfCAR (corrected)'),
    plt.Line2D([0], [0], color='#d62728', linewidth=2.5, alpha=0.4,
               label='Inflation gap'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#2ca02c',
               markersize=8, markeredgecolor='black', markeredgewidth=0.5,
               label='No inflation (dfCAR = CAR)'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#ff7f0e',
               markersize=8, markeredgecolor='black', markeredgewidth=0.5,
               label='Fine-tuned (dfCAR = CAR)'),
]
ax.legend(handles=legend_elements, loc='lower right', fontsize=6.5,
          framealpha=0.9, edgecolor='gray', ncol=1)

# --- Group separators ---
ax.axhline(y=3.5, color='gray', linewidth=0.5, linestyle='--', alpha=0.3)
ax.axhline(y=2.5, color='gray', linewidth=0.5, linestyle='--', alpha=0.3)

# Group annotations on right
ax.text(98, 5, 'Action-\ncollapsed', ha='right', va='center',
        fontsize=6.5, color='#d62728', style='italic', alpha=0.7)
ax.text(98, 3, 'Genuine', ha='right', va='center',
        fontsize=6.5, color='#2ca02c', style='italic', alpha=0.7)
ax.text(98, 1, 'Fine-tuned', ha='right', va='center',
        fontsize=6.5, color='#ff7f0e', style='italic', alpha=0.7)

# --- Axes ---
ax.set_xlabel('Rate (%)', fontsize=10)
ax.set_xlim(-3, 100)
ax.set_ylim(-0.7, len(models) - 0.3)

# Y-axis: model labels as proper tick labels with padding
model_labels = [m[0] for m in models]
ax.set_yticks(y_positions)
ax.set_yticklabels(model_labels, fontsize=8)
ax.tick_params(axis='y', length=0, pad=8)

plt.tight_layout()
outdir = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures'
plt.savefig(f'{outdir}/fig_tsr_car_scatter.pdf', bbox_inches='tight', dpi=300)
plt.savefig(f'{outdir}/fig2_plan_b.pdf', bbox_inches='tight', dpi=300)
plt.savefig(f'{outdir}/fig2_plan_b.png', bbox_inches='tight', dpi=150)
print("Saved: fig_tsr_car_scatter.pdf + fig2_plan_b.pdf/png")
