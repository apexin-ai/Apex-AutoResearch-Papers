import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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

# --- Data ---
lf_names = ['Command\nRepetition', 'File Diff\nDelta', 'Outcome\nBackprop.']
lf_short = ['cmd_rep', 'file_diff', 'outcome_bp']
colors = ['#0072B2', '#009E73', '#E69F00']

swe_means = [-1.87, -1.2, 6.7]
oh_means  = [3.32, -4.9, 18.1]

fig, ax = plt.subplots(figsize=(6, 4.5))

# Background color bands
ax.axhspan(ymin=-8, ymax=0, color='#d0e8f2', alpha=0.35, zorder=0)
ax.axhspan(ymin=0, ymax=22, color='#f2d0d0', alpha=0.35, zorder=0)

# Zone labels
ax.text(0.01, 0.42, 'Leading', transform=ax.transAxes,
        fontsize=9, color='#2166ac', fontstyle='italic', va='top', ha='left', alpha=0.7)
ax.text(0.01, 0.58, 'Lagging', transform=ax.transAxes,
        fontsize=9, color='#b2182b', fontstyle='italic', va='bottom', ha='left', alpha=0.7)

# Onset line
ax.axhline(y=0, color='#555555', linestyle='--', linewidth=1, zorder=2)
ax.text(1.98, 0.4, 'Onset', fontsize=9, color='#555555', fontstyle='italic',
        va='bottom', ha='right')

# Bar positions
bar_width = 0.22
swe_positions = np.array([0, 0.28, 0.56])
oh_positions = np.array([1.1, 1.38, 1.66])

# Draw bars
for i in range(3):
    ax.bar(swe_positions[i], swe_means[i], width=bar_width, color=colors[i],
           edgecolor='white', linewidth=0.5, zorder=3)
    ax.bar(oh_positions[i], oh_means[i], width=bar_width, color=colors[i],
           edgecolor='white', linewidth=0.5, zorder=3)

# Value annotations
def annotate_bar(x, y, text, ax):
    offset = -0.8 if y < 0 else 0.8
    va = 'top' if y < 0 else 'bottom'
    ax.text(x, y + offset, text, ha='center', va=va, fontsize=8.5,
            fontweight='bold', color='#333333', zorder=5)

for i in range(3):
    annotate_bar(swe_positions[i], swe_means[i], f'{swe_means[i]:+.1f}', ax)
    annotate_bar(oh_positions[i], oh_means[i], f'{oh_means[i]:+.1f}', ax)

# Reversal arrow for cmd_rep
ax.annotate('', xy=(oh_positions[0], 3.8), xytext=(swe_positions[0], -1.4),
            arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1.8,
                            connectionstyle='arc3,rad=-0.3'),
            zorder=5)
ax.text(0.55, 5.5, 'role reversal', fontsize=8.5, color='#c0392b',
        fontstyle='italic', ha='center', va='bottom',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='none', alpha=0.8))

# Vertical separator
sep_x = 0.83
ax.axvline(x=sep_x, color='#aaaaaa', linestyle=':', linewidth=1, zorder=2)

# Agent group labels
ax.text(np.mean(swe_positions), -7.2, 'SWE-Agent', ha='center', fontsize=11,
        fontweight='bold', color='#333333')
ax.text(np.mean(oh_positions), -7.2, 'OpenHands', ha='center', fontsize=11,
        fontweight='bold', color='#333333')

# Axis config
ax.set_ylabel('Mean Lag (steps relative to stagnation onset)')
ax.set_ylim(-8, 22)
ax.set_xlim(-0.3, 2.0)
ax.set_xticks(list(swe_positions) + list(oh_positions))
ax.set_xticklabels(lf_names * 2, fontsize=8.5)

# Legend
legend_patches = [mpatches.Patch(facecolor=colors[i], label=lf_names[i].replace('\n', ' '))
                  for i in range(3)]
ax.legend(handles=legend_patches, loc='upper left', frameon=True,
          fancybox=False, edgecolor='#cccccc', framealpha=0.9)

# Title
ax.set_title('Temporal Dynamics of Leading Functions', pad=10)

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/figures/paper'
fig.savefig(f'{out_dir}/fig_lf_temporal.pdf', format='pdf')
fig.savefig(f'{out_dir}/fig_lf_temporal.png', format='png')
plt.close()
print('Done.')
