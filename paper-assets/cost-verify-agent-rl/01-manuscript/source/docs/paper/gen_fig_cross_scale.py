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
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'dejavuserif',
})

# Unified palette (D143 color unification) — matches all paper figures
C_CELL_A    = '#4477AA'   # blue — Cell A / collapsed
C_CELL_D    = '#228833'   # green — Cell D / episode-level
C_SFT       = '#808080'   # gray — SFT baseline
C_NEUTRAL   = '#808080'   # gray

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 2.8),
                                gridspec_kw={'wspace': 0.35})

# ═══════════════════ Panel (a): Cross-Scale Verification ═══════════════════

conditions = ['SFT baseline', 'Cell A\n(h=2, step)', 'Cell D\n(episode)']
vals_1_7b = [12.50, 0, 34.38]
vals_8b = [68.75, 1.6, 96.88]

x = np.arange(len(conditions))
w = 0.32

C_BAR = '#4477AA'
C_BAR_LABEL = '#335588'

bars1 = ax1.bar(x - w/2, vals_1_7b, w, color=C_BAR,
                edgecolor='white', linewidth=0.5, zorder=3)
bars2 = ax1.bar(x + w/2, vals_8b, w, color=C_BAR, alpha=0.45,
                edgecolor=C_BAR, linewidth=0.8,
                hatch='///', zorder=3)

# Value labels
for bar, val in zip(bars1, vals_1_7b):
    label = f'{val:.1f}' if val > 0 else '0'
    y_pos = max(val, 0) + 1.5
    ax1.text(bar.get_x() + bar.get_width()/2, y_pos, label,
             ha='center', va='bottom', fontsize=6.5, color=C_BAR_LABEL)

for bar, val in zip(bars2, vals_8b):
    label = f'{val:.1f}'
    ax1.text(bar.get_x() + bar.get_width()/2, val + 1.5, label,
             ha='center', va='bottom', fontsize=6.5, color=C_BAR_LABEL)

ax1.set_ylabel('In-Dist Success Rate (%)')
ax1.set_xticks(x)
ax1.set_xticklabels(conditions, fontsize=9)
ax1.set_ylim(0, 115)
ax1.set_yticks([0, 25, 50, 75, 100])
ax1.yaxis.grid(True, alpha=0.08, linestyle='-', zorder=0)
legend_el = [mpatches.Patch(facecolor=C_BAR, label='1.7B'),
             mpatches.Patch(facecolor=C_BAR, alpha=0.45, hatch='///',
                            edgecolor=C_BAR, label='8B')]
ax1.legend(handles=legend_el, loc='upper left', fontsize=8, frameon=False,
           handlelength=1.2, borderpad=0.3)

ax1.text(-0.10, 1.06, '(a)', transform=ax1.transAxes, fontsize=13,
         fontweight='bold', va='bottom')

# ═══════════════════ Panel (b): Information Loss ═══════════════════

envs = ['ALFWorld\n8B', 'ScienceWorld\n1.7B']
full_vals = [68.75, 34.8]
h2_vals = [31.25, 4.5]
gaps = [37.5, 30.3]

# Per-environment colors — condition-based (green=full, blue=h=2 restricted)
full_colors = [C_CELL_D, C_CELL_D]
h2_colors = [C_CELL_A, C_CELL_A]

x2 = np.array([0, 1.1])
w2 = 0.32

for i in range(len(envs)):
    ax2.bar(x2[i] - w2/2, full_vals[i], w2, color=full_colors[i],
            edgecolor='white', linewidth=0.5, zorder=3)
    ax2.bar(x2[i] + w2/2, h2_vals[i], w2, color=h2_colors[i],
            edgecolor='white', linewidth=0.5, zorder=3)

# Gap annotations with double-headed arrows
for i in range(len(envs)):
    arrow_x = x2[i] + w2/2 + 0.22
    ax2.annotate('', xy=(arrow_x, full_vals[i]), xytext=(arrow_x, h2_vals[i]),
                 arrowprops=dict(arrowstyle='<->', color='#333333', lw=1.3),
                 zorder=4)
    ax2.text(arrow_x + 0.08, (full_vals[i] + h2_vals[i]) / 2,
             f'{gaps[i]}pp', va='center', ha='left',
             fontsize=8.5, fontweight='bold', color='#333333', zorder=5)

# Value labels on bars
for i in range(len(envs)):
    ax2.text(x2[i] - w2/2, full_vals[i] + 1.5, f'{full_vals[i]:.1f}',
             ha='center', va='bottom', fontsize=6.5,
             color=full_colors[i], zorder=5)
    ax2.text(x2[i] + w2/2, h2_vals[i] + 1.5, f'{h2_vals[i]:.1f}',
             ha='center', va='bottom', fontsize=6.5,
             color=h2_colors[i], zorder=5)

ax2.set_ylabel('In-Dist Success Rate (%)')
ax2.set_xticks(x2)
ax2.set_xticklabels(envs, fontsize=9)
ax2.set_ylim(0, 85)
ax2.set_xlim(-0.5, 2.15)
ax2.set_yticks([0, 20, 40, 60, 80])
ax2.yaxis.grid(True, alpha=0.08, linestyle='-', zorder=0)

# Legend — show full/h=2 with condition colors
legend_elements = [mpatches.Patch(facecolor=C_CELL_D, label='Full context'),
                   mpatches.Patch(facecolor=C_CELL_A, label='$h$=2')]
ax2.legend(handles=legend_elements, loc='upper right', fontsize=8.5,
           frameon=False, handlelength=1.2, borderpad=0.3)

ax2.text(-0.10, 1.06, '(b)', transform=ax2.transAxes, fontsize=13,
         fontweight='bold', va='bottom')

# ── Save ──
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper'
fig.savefig(f'{out_dir}/fig_cross_scale.pdf')
fig.savefig(f'{out_dir}/fig_cross_scale.png')
plt.close()
print('Done: fig_cross_scale.pdf + .png')
