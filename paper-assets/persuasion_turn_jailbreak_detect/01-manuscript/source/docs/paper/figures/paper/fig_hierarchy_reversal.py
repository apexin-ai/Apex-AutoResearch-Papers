import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

# --- Data ---
variants_left = ['9-class', 'MLM', 'Vanilla']
values_left = [0.997, 0.914, 0.312]

variants_right = ['MLM', 'Wiki-\nMLM', 'Binary', '9-class', 'Vanilla']
values_right = [0.837, 0.791, 0.705, 0.596, 0.413]

color_map = {
    '9-class':  '#1f4e79',
    'MLM':      '#2e75b6',
    'Wiki-\nMLM': '#5b9bd5',
    'Binary':   '#9dc3e6',
    'Vanilla':  '#bdd7ee',
}

text_color_map = {
    '9-class':  'white',
    'MLM':      'white',
    'Wiki-\nMLM': 'white',
    'Binary':   '#1f4e79',
    'Vanilla':  '#1f4e79',
}

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 8,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.major.size': 2.5,
    'ytick.major.size': 2.5,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

fig = plt.figure(figsize=(3.5, 2.6))

ax1 = fig.add_axes([0.12, 0.18, 0.30, 0.68])
ax2 = fig.add_axes([0.57, 0.18, 0.41, 0.68])

bar_width = 0.55

# --- Left panel ---
x_left = np.arange(len(variants_left))
bars_left = ax1.bar(x_left, values_left, width=bar_width,
                    color=[color_map[v] for v in variants_left],
                    edgecolor='white', linewidth=0.3, zorder=3)
ax1.set_xticks(x_left)
ax1.set_xticklabels(variants_left, fontsize=7)
ax1.set_ylabel('F1 Score', fontsize=8)
ax1.set_ylim(0, 1.12)
ax1.set_xlim(-0.5, len(variants_left) - 0.5)
ax1.set_title('Synthetic OOD (DD Full)', fontsize=7.5, fontweight='bold', pad=4)

for i, (bar, val, v) in enumerate(zip(bars_left, values_left, variants_left)):
    ax1.text(bar.get_x() + bar.get_width()/2, val + 0.015,
             f'{val:.3f}', ha='center', va='bottom', fontsize=6)
    ax1.text(bar.get_x() + bar.get_width()/2, val/2,
             f'#{i+1}', ha='center', va='center', fontsize=7,
             fontweight='bold', color=text_color_map[v])

# --- Right panel ---
x_right = np.arange(len(variants_right))
bars_right = ax2.bar(x_right, values_right, width=bar_width,
                     color=[color_map[v] for v in variants_right],
                     edgecolor='white', linewidth=0.3, zorder=3)
ax2.set_xticks(x_right)
ax2.set_xticklabels(variants_right, fontsize=7)
ax2.set_ylim(0, 1.12)
ax2.set_xlim(-0.5, len(variants_right) - 0.5)
ax2.set_title('ToxicChat (macro F1)', fontsize=7.5, fontweight='bold', pad=4)
ax2.set_yticklabels([])

for i, (bar, val, v) in enumerate(zip(bars_right, values_right, variants_right)):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 0.015,
             f'{val:.3f}', ha='center', va='bottom', fontsize=6)
    ax2.text(bar.get_x() + bar.get_width()/2, val/2,
             f'#{i+1}', ha='center', va='center', fontsize=7,
             fontweight='bold', color=text_color_map[v])

# --- Spines ---
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='both', which='both', direction='out')
    ax.set_axisbelow(True)
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))

# --- Reversal annotation ---
mid_x = 0.475
fig.text(mid_x, 0.60, 'Rank', fontsize=7.5, fontweight='bold',
         ha='center', va='center', color='#c00000', style='italic')
fig.text(mid_x, 0.53, 'Reversal', fontsize=7.5, fontweight='bold',
         ha='center', va='center', color='#c00000', style='italic')

arrow = FancyArrowPatch(
    (mid_x, 0.46), (mid_x, 0.36),
    arrowstyle='<->', mutation_scale=10,
    color='#c00000', linewidth=1.5,
    transform=fig.transFigure, clip_on=False
)
fig.patches.append(arrow)

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig_hierarchy_reversal'
plt.savefig(out_base + '.pdf', bbox_inches='tight', pad_inches=0.05, dpi=300)
plt.savefig(out_base + '.png', bbox_inches='tight', pad_inches=0.05, dpi=300)
plt.close()
print("Done")
