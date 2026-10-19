import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
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

# Unified palette (Director D143 color unification)
C_COLLAPSE = '#4477AA'   # blue — Cell A, collapsed bars
C_BOUNDED  = '#EE7733'   # orange — Cell B, partial recovery
C_SUCCESS  = '#228833'   # green — Cell D, episode-level success
C_NEUTRAL  = '#808080'   # gray — SFT baseline, references
C_SKYBLUE  = '#66AA55'   # light green — transitional (h=20 bar)

# ── Data ──
steps = list(range(16))
cell_a = [12.5, 12.5, 9.4, 6.25, 3.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cell_b = [12.5, 15.6, 18.75, 21.9, 18.75, 18.75, 15.6, 12.5, 9.4, 6.25, 6.25, 3.1, 3.1, 3.1, 3.1, 3.1]
cell_d = [12.5, 15.6, 18.75, 21.9, 25, 28.1, 28.1, 31.25, 31.25, 31.25, 34.4, 34.4, 34.4, 34.4, 37.5, 37.5]
sft_val = 12.5

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 2.6),
                                gridspec_kw={'width_ratios': [1.1, 1], 'wspace': 0.38})

# ═══════════════════ Panel (a): Training Dynamics ═══════════════════

# Collapse zone background — slightly more visible
ax1.axhspan(0, 5, color='#FBE9E7', alpha=0.55, zorder=0)
ax1.text(7.5, 2.2, 'collapse zone', fontsize=7, color='#B89590',
         fontstyle='italic', ha='center', va='center')

# SFT baseline
ax1.plot(steps, [sft_val]*16, color=C_NEUTRAL, linestyle='--', linewidth=1.0,
         label='SFT baseline', zorder=2)

# Cell A: collapse trajectory
ax1.plot(steps, cell_a, color=C_COLLAPSE, marker='o', markersize=3.5,
         markeredgewidth=0, linewidth=1.6,
         label=r'Cell A: step-level, $M_1$+$M_2$ (ID)', zorder=3)

# Cell B: bounded learning
ax1.plot(steps, cell_b, color=C_BOUNDED, marker='^', markersize=4.5,
         markeredgewidth=0, linewidth=1.6,
         label=r'Cell B: episode-adv, $M_1$ only (ID)', zorder=3)

# Cell D: monotonic improvement
ax1.plot(steps, cell_d, color=C_SUCCESS, marker='s', markersize=3.5,
         markeredgewidth=0, linewidth=2.0,
         label=r'Cell D: episode-level (ID)', zorder=3)

ax1.set_xlabel('Training Step')
ax1.set_ylabel('Success Rate (%)')
ax1.set_xlim(-0.5, 15.5)
ax1.set_ylim(0, 44)
ax1.set_xticks([0, 5, 10, 15])
ax1.set_yticks([0, 10, 20, 30, 40])
ax1.yaxis.grid(True, alpha=0.12, linestyle='-', zorder=0)

ax1.legend(loc='upper left', fontsize=6.5, frameon=False,
           handlelength=1.5, labelspacing=0.3, borderpad=0.1,
           bbox_to_anchor=(0.0, 1.02))

ax1.text(-0.10, 1.06, '(a)', transform=ax1.transAxes, fontsize=13,
         fontweight='bold', va='bottom')

# ═══════════════════ Panel (b): Window Size Sweep ═══════════════════

x_pos = np.arange(5)
values = [0, 0, 14.06, 15.6, 23.88]
bar_colors = [C_COLLAPSE, C_COLLAPSE, C_BOUNDED, C_SKYBLUE, C_SUCCESS]

# Slightly taller mini-bars for collapsed conditions (clearer hatching)
display_vals = [2.0 if v == 0 else v for v in values]

bars = ax2.bar(x_pos, display_vals, color=bar_colors, width=0.55,
               edgecolor='none', zorder=3)

# Hatching for collapsed bars (h=2, h=5 only)
for i in [0, 1]:
    bars[i].set_hatch('///')
    bars[i].set_edgecolor(C_COLLAPSE)
    bars[i].set_alpha(0.5)

# h=10 scatter: show both seeds (6.25%, 21.875%)
ax2.scatter([2, 2], [6.25, 21.875], color='#333333', s=18, zorder=5,
            marker='o', edgecolors='white', linewidths=0.6,
            label='Individual seeds')

# SFT baseline (no direct label — moved to legend)
ax2.axhline(y=sft_val, color=C_NEUTRAL, linestyle='--', linewidth=1.0, zorder=2)

# Value labels above bars — crisp, no overlap
bar_labels = ['0% (ID)', '0% (ID)', '14.1% (ID)', '15.6% (ID)', '23.9% (OOD)']
for i, (bar, dv, label) in enumerate(zip(bars, display_vals, bar_labels)):
    xc = bar.get_x() + bar.get_width() / 2
    yp = dv + 0.8
    if i == 2:
        yp = dv + 0.8
    ax2.text(xc, yp, label, ha='center', va='bottom',
             fontsize=6.8, color='#444444',
             path_effects=[pe.withStroke(linewidth=2, foreground='white')])


# Shorter x-labels to avoid cramping
ax2.set_xticks(x_pos)
ax2.set_xticklabels(['2', '5', '10', '20', 'Full'], fontsize=9.5)
ax2.set_ylabel('Success Rate (%)')
ax2.set_xlabel('Window Size ($h$)')
ax2.set_ylim(0, 38)
ax2.set_yticks([0, 10, 20, 30])
ax2.yaxis.grid(True, alpha=0.12, linestyle='-', zorder=0)

# Legend: hatching + individual seeds + SFT baseline
hatch_patch = mpatches.Patch(facecolor=C_COLLAPSE, hatch='///', alpha=0.5,
                              edgecolor=C_COLLAPSE, label='Collapsed (0%)')
seed_dot = plt.Line2D([], [], color='#333333', marker='o', linestyle='None',
                       markersize=4, markeredgecolor='white', markeredgewidth=0.6,
                       label='Individual seeds')
sft_line = plt.Line2D([], [], color=C_NEUTRAL, linestyle='--', linewidth=1.0,
                       label='SFT baseline')
ax2.legend(handles=[hatch_patch, seed_dot, sft_line], loc='upper left', fontsize=7.5,
           frameon=False, handlelength=1.0, borderpad=0.2)

ax2.text(-0.15, 1.06, '(b)', transform=ax2.transAxes, fontsize=13,
         fontweight='bold', va='bottom')

# ── Save ──
outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper'
fig.savefig(f'{outdir}/fig_training_dynamics.pdf')
fig.savefig(f'{outdir}/fig_training_dynamics.png')
plt.close()
print('Done: fig_training_dynamics.pdf + .png')
