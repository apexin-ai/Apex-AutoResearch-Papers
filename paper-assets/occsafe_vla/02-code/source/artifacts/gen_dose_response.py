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

# Data
# Format: (x_position_Ksteps, label, seeds_list, color, marker)
data = [
    (0,  'Vanilla\n(no OCC)',    [0.788, 0.766, 0.786], None, None),
    (15, 'cutoff_15k\n(0–15K)',  [0.804, 0.760],        None, 'o'),
    (25, 'cutoff_25k\n(0–25K)',  [0.688, 0.760],        None, 'o'),
    (45, 'cutoff_45k\n(0–45K)',  [0.764],                None, 'o'),
    (50, 'Full OCC\n(0–50K)',    [0.832, 0.802, 0.758],  None, 'o'),
]

reverse_data = (35, 'reverse\n(35K–50K)', [0.700, 0.736])

# Colors: blue gradient light->dark by duration
blue_colors = {
    15: '#93c5fd',  # light blue
    25: '#60a5fa',
    45: '#2563eb',
    50: '#1e40af',  # dark blue
}
reverse_color = '#f97316'  # orange
vanilla_color = '#6b7280'  # gray

fig, ax = plt.subplots(figsize=(6, 4))

# Vanilla baseline
vanilla_seeds = data[0][2]
vanilla_mean = np.mean(vanilla_seeds)
vanilla_std = np.std(vanilla_seeds, ddof=1) if len(vanilla_seeds) > 1 else 0
ax.axhline(y=vanilla_mean, color=vanilla_color, linestyle='--', linewidth=1.0, alpha=0.7, zorder=1)
ax.text(51.5, vanilla_mean + 0.003, f'Vanilla baseline\n({vanilla_mean:.3f})', fontsize=8,
        color=vanilla_color, va='bottom', ha='left')

# Plot early-cutoff points (connected line)
xs_line, ys_line = [], []
for x, label, seeds, _, _ in data[1:]:  # skip vanilla
    xs_line.append(x)
    ys_line.append(np.mean(seeds))

# Sort by x
order = np.argsort(xs_line)
xs_line = [xs_line[i] for i in order]
ys_line = [ys_line[i] for i in order]

# Draw connecting line (thin, gray)
ax.plot(xs_line, ys_line, color='#94a3b8', linewidth=1.0, linestyle='-', zorder=2, alpha=0.6)

# Plot each early-cutoff point
for x, label, seeds, _, _ in data[1:]:
    mean = np.mean(seeds)
    color = blue_colors[x]
    # Individual seeds as small dots
    for s in seeds:
        ax.scatter(x, s, color=color, s=20, alpha=0.4, zorder=3, edgecolors='none')
    # Mean as large dot
    if len(seeds) >= 3:
        std = np.std(seeds, ddof=1)
        ax.errorbar(x, mean, yerr=std, fmt='o', color=color, markersize=8,
                     capsize=3, capthick=1.0, elinewidth=1.0, zorder=4,
                     markeredgecolor='white', markeredgewidth=0.8)
    else:
        ax.scatter(x, mean, color=color, s=64, zorder=4,
                   edgecolors='white', linewidths=0.8)

# Plot reverse_cutoff (different marker, orange)
rx, rlabel, rseeds = reverse_data
rmean = np.mean(rseeds)
for s in rseeds:
    ax.scatter(rx, s, color=reverse_color, s=20, alpha=0.4, zorder=3,
               edgecolors='none', marker='^')
ax.scatter(rx, rmean, color=reverse_color, s=80, zorder=4, marker='^',
           edgecolors='white', linewidths=0.8)

# Vanilla point at x=0
v_mean = np.mean(vanilla_seeds)
v_std = np.std(vanilla_seeds, ddof=1)
for s in vanilla_seeds:
    ax.scatter(0, s, color=vanilla_color, s=20, alpha=0.4, zorder=3, edgecolors='none')
ax.errorbar(0, v_mean, yerr=v_std, fmt='s', color=vanilla_color, markersize=8,
            capsize=3, capthick=1.0, elinewidth=1.0, zorder=4,
            markeredgecolor='white', markeredgewidth=0.8)

# Annotations
annotations = [
    (0, v_mean, f'{v_mean:.3f}', -15, 12),
    (15, np.mean(data[1][2]), f'{np.mean(data[1][2]):.3f}', 8, 8),
    (25, np.mean(data[2][2]), f'{np.mean(data[2][2]):.3f}', 8, -12),
    (45, np.mean(data[3][2]), f'{np.mean(data[3][2]):.3f}', 8, 8),
    (50, np.mean(data[4][2]), f'{np.mean(data[4][2]):.3f}', 8, 8),
    (rx, rmean, f'{rmean:.3f}', 8, -12),
]
for ax_x, ax_y, txt, dx, dy in annotations:
    ax.annotate(txt, (ax_x, ax_y), textcoords='offset points', xytext=(dx, dy),
                fontsize=8, color='#374151')

# Axes
ax.set_xlabel('OCC Gradient Flow Duration (K steps)', fontsize=11)
ax.set_ylabel('Collision Avoidance Rate (CAR)', fontsize=11)
ax.set_xticks([0, 15, 25, 35, 45, 50])
ax.set_xticklabels(['0', '15', '25', '35', '45', '50'])
ax.set_xlim(-3, 58)
ax.set_ylim(0.68, 0.86)

# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='s', color='w', markerfacecolor=vanilla_color,
           markersize=8, label='Vanilla (no OCC)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#2563eb',
           markersize=8, label='Early-cutoff (0–N K)'),
    Line2D([0], [0], marker='^', color='w', markerfacecolor=reverse_color,
           markersize=8, label='Late-onset (35K–50K)'),
]
ax.legend(handles=legend_elements, loc='lower left', frameon=True, framealpha=0.9,
          edgecolor='#d1d5db', fontsize=9)

# Clean up
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.15, color='#9ca3af')

plt.tight_layout()

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/fig_dose_response_2seed'
fig.savefig(f'{out_base}.pdf', bbox_inches='tight', dpi=300)
fig.savefig(f'{out_base}.png', bbox_inches='tight', dpi=300)
print(f'Saved: {out_base}.pdf and .png')
plt.close()
