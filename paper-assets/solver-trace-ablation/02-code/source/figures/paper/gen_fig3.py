import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'pdf.fonttype': 42, 'ps.fonttype': 42})

C_H7 = '#D55E00'
C_H1 = '#E69F00'
C_GENUINE = '#009E73'
C_OTHER = '#999999'

conditions = [
    'ISR $\\beta$=0.3',
    'ISR $\\beta$=0.1',
    'Random $\\beta$=0.1',
    'Exec-only',
    'SFT',
]

h7 =      [49.7, 70.6, 13.7,  0.0,  0.0]
h1 =      [36.7, 18.2, 71.4, 86.0,  7.7]
genuine = [13.6,  6.1,  9.5,  7.5, 92.3]
other =   [ 0.0,  5.2,  5.3,  6.5,  0.0]

y = np.arange(len(conditions))
bar_h = 0.55

fig, ax = plt.subplots(figsize=(8, 4))

ax.barh(y, h7, bar_h, color=C_H7, label='H7 (tautological)', edgecolor='white', linewidth=0.5, zorder=3)
ax.barh(y, h1, bar_h, left=h7, color=C_H1, label='H1 (shortcut)', edgecolor='white', linewidth=0.5, zorder=3)
left_genuine = [a + b for a, b in zip(h7, h1)]
ax.barh(y, genuine, bar_h, left=left_genuine, color=C_GENUINE, label='Genuine', edgecolor='white', linewidth=0.5, zorder=3)
left_other = [a + b for a, b in zip(left_genuine, genuine)]
ax.barh(y, other, bar_h, left=left_other, color=C_OTHER, label='Other', edgecolor='white', linewidth=0.5, zorder=3)

for i, g in enumerate(genuine):
    right_edge = left_genuine[i] + g + other[i]
    ax.text(right_edge + 1.2, y[i], f'{g:.1f}%', va='center', ha='left', fontsize=9, color=C_GENUINE)

ax.annotate(
    'ISR H7: 70.6%\nvs Random: 13.7%',
    xy=(13.7 / 2, y[2]),
    xytext=(55, y[1] + 0.85),
    fontsize=8.5, fontweight='bold', color=C_H7,
    ha='center',
    arrowprops=dict(arrowstyle='->', color=C_H7, lw=1.5),
)

ax.set_yticks(y)
ax.set_yticklabels(conditions, fontsize=10)
ax.set_xlabel('Percentage of proved samples (%)', fontsize=11)
ax.set_xlim(0, 108)
ax.set_xticks([0, 20, 40, 60, 80, 100])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='both', labelsize=10)
ax.legend(fontsize=9, loc='lower right', frameon=False, ncol=2)

fig.subplots_adjust(left=0.22, right=0.95, top=0.92, bottom=0.15)

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/figures/paper'
canonical = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures'
fig.savefig(f'{out_dir}/fig3_hacking_composition.pdf', dpi=300, bbox_inches='tight', pad_inches=0.15)
fig.savefig(f'{out_dir}/fig3_hacking_composition.png', dpi=300, bbox_inches='tight', pad_inches=0.15)
fig.savefig(f'{canonical}/fig3_hacking_composition.pdf', dpi=300, bbox_inches='tight', pad_inches=0.15)
fig.savefig(f'{canonical}/fig3_hacking_composition.png', dpi=300, bbox_inches='tight', pad_inches=0.15)
plt.close()
print('Done: fig3_hacking_composition.pdf + .png')
