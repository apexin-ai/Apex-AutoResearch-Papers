import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.linewidth': 0.8,
    'xtick.major.width': 0.8,
    'ytick.major.width': 0.8,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'figure.dpi': 300,
})

# Data: 2x2 factorial (BN × Gradient Flow)
# Rows: Gradient Flow (Full OCC), No Gradient (Detach)
# Cols: BN, LN
means = np.array([
    [0.797, 0.743],  # Gradient flow: BN, LN
    [0.746, 0.765],  # No gradient: BN, LN
])
stds = np.array([
    [0.032, 0.024],
    [0.002, 0.023],
])

conditions = ['Gradient Flow\n(Full OCC)', 'No Gradient\n(Detach)']
norm_labels = ['BatchNorm', 'LayerNorm']
colors_bn = '#3b82f6'   # blue
colors_ln = '#f97316'    # orange
vanilla_car = 0.780

fig, ax = plt.subplots(figsize=(5, 4))

x = np.arange(len(conditions))
bar_width = 0.3

bars_bn = ax.bar(x - bar_width/2, means[:, 0], bar_width, yerr=stds[:, 0],
                  color=colors_bn, edgecolor='white', linewidth=0.8,
                  capsize=4, error_kw={'linewidth': 1.0, 'capthick': 1.0},
                  label='BatchNorm', zorder=3)
bars_ln = ax.bar(x + bar_width/2, means[:, 1], bar_width, yerr=stds[:, 1],
                  color=colors_ln, edgecolor='white', linewidth=0.8,
                  capsize=4, error_kw={'linewidth': 1.0, 'capthick': 1.0},
                  label='LayerNorm', zorder=3)

# Vanilla baseline
ax.axhline(y=vanilla_car, color='#6b7280', linestyle='--', linewidth=1.0, alpha=0.7, zorder=1)
ax.text(1.52, vanilla_car + 0.002, f'Vanilla\n({vanilla_car:.3f})', fontsize=8,
        color='#6b7280', va='bottom', ha='left')

# Value labels on bars
for bars in [bars_bn, bars_ln]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.038,
                f'{height:.3f}', ha='center', va='bottom', fontsize=9, color='#374151')

# Interaction annotation
# Draw bracket between the two groups
bracket_y = 0.845
ax.annotate('', xy=(-0.15, bracket_y), xytext=(1.15, bracket_y),
            arrowprops=dict(arrowstyle='-', color='#374151', lw=0.8))
ax.plot([-0.15, -0.15], [bracket_y - 0.003, bracket_y], color='#374151', lw=0.8)
ax.plot([1.15, 1.15], [bracket_y - 0.003, bracket_y], color='#374151', lw=0.8)
ax.text(0.5, bracket_y + 0.004, 'Interaction: p = 0.025', ha='center', va='bottom',
        fontsize=9, fontstyle='italic', color='#374151')

# Axes
ax.set_ylabel('Collision Avoidance Rate (CAR)', fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(conditions)
ax.set_ylim(0.70, 0.87)
ax.set_xlim(-0.6, 1.8)

# Legend
ax.legend(loc='lower right', frameon=True, framealpha=0.9,
          edgecolor='#d1d5db', fontsize=10)

# Clean up
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.15, color='#9ca3af')

plt.tight_layout()

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/fig_factorial_2x2'
fig.savefig(f'{out_base}.pdf', bbox_inches='tight', dpi=300)
fig.savefig(f'{out_base}.png', bbox_inches='tight', dpi=300)
print(f'Saved: {out_base}.pdf and .png')
plt.close()
