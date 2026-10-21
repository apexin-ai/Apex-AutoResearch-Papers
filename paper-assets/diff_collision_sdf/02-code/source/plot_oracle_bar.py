import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['STIXGeneral', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.7,
})

methods = [
    'Oracle-fixed\n(GT SDF)',
    'A3 no-refine\n(learned SDF)',
    'Oracle-adaptive\n(GT SDF)',
    'Oracle-feature\n(GT SDF)',
    'LoRA baseline',
    'Full-FT baseline',
]
cars = [73.1, 74.5, 75.0, 76.9, 82.0, 83.0]

colors = [
    '#A78BFA',  # oracle-fixed - light purple
    '#3274A1',  # A3 - blue
    '#8B5CF6',  # oracle-adaptive - purple
    '#7C3AED',  # oracle-feature - dark purple
    '#9CA3AF',  # LoRA baseline - gray
    '#6B7280',  # Full-FT baseline - darker gray
]

fig, ax = plt.subplots(figsize=(4, 3.5))

y_pos = np.arange(len(methods))
bars = ax.barh(y_pos, cars, height=0.55, color=colors, edgecolor='white', linewidth=0.5)

# Value labels
for bar, val in zip(bars, cars):
    ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height() / 2,
            f'{val:.1f}%', va='center', ha='left', fontsize=9, color='#333333')

# Baseline average line
baseline_avg = (82.0 + 83.0) / 2
ax.axvline(x=baseline_avg, color='#6B7280', linestyle='--', linewidth=0.9, alpha=0.7, zorder=3)
ax.text(baseline_avg + 0.5, len(methods) - 0.3, 'No Refinement\navg', fontsize=7,
        color='#6B7280', va='bottom', ha='left', style='italic')

ax.set_yticks(y_pos)
ax.set_yticklabels(methods, fontsize=9)
ax.set_xlabel('Collision Avoidance Rate (%)', fontsize=10)
ax.set_xlim(65, 92)
ax.tick_params(axis='x', labelsize=9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.invert_yaxis()

plt.tight_layout()
out = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig_oracle_bar.pdf'
plt.savefig(out, bbox_inches='tight', dpi=300)
print(f'Saved: {out}')
plt.close()
