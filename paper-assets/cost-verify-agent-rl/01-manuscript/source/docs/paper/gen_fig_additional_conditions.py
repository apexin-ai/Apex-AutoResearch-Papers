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

# Unified palette (D143 color unification)
C_CELL_D    = '#228833'   # green — Cell D / episode-level
C_DENSE     = '#CCBB44'   # yellow — dense reward
C_NEUTRAL   = '#808080'   # gray — SFT baseline
C_REINF_PP  = '#AA3377'   # purple — REINFORCE++
C_BEFORE    = '#4477AA'   # blue — before training
C_AFTER     = '#EE7733'   # orange — after training
C_COLLAPSE  = '#4477AA'   # blue — collapsed (0%)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 2.8),
                                gridspec_kw={'wspace': 0.35})

# ═══════════════════ Panel (a): Standard Remedies Fail ═══════════════════

methods = ['SFT\nbaseline', 'Dense\nreward', r'$\gamma{=}1.0$' + '\n(h=5)', 'REINF\n++', 'Cell D\n(ours)']
in_dist = [12.5, 0, 0, 12.5, 34.38]
bar_colors = [C_NEUTRAL, C_DENSE, C_DENSE, C_REINF_PP, C_CELL_D]

x = np.arange(len(methods))
# Use small display bars for 0-value conditions so the color is visible
display_in_dist = [v if v > 0 else 1.5 for v in in_dist]
bars = ax1.bar(x, display_in_dist, color=bar_colors, edgecolor='none', width=0.58, zorder=3)
# Hatch the collapsed (0%) bars
for i in [1, 2]:
    bars[i].set_hatch('///')
    bars[i].set_edgecolor(C_DENSE)
    bars[i].set_alpha(0.5)

# SFT baseline dashed line
ax1.axhline(y=12.5, color=C_NEUTRAL, linestyle='--', linewidth=1.0, alpha=0.7, zorder=2)
t_sft = ax1.text(4.35, 12.5 + 0.8, 'SFT', fontsize=7, color=C_NEUTRAL, va='bottom', ha='center')
t_sft.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Value labels
for bar, val in zip(bars, in_dist):
    xc = bar.get_x() + bar.get_width() / 2
    if val > 0:
        ax1.text(xc, val + 0.8, f'{val}%', ha='center', va='bottom',
                 fontsize=7.5, color='#444444')
    else:
        ax1.text(xc, 2.2, '0%', ha='center', va='bottom',
                 fontsize=7.5, color=C_DENSE)

ax1.set_ylabel('In-Dist Success Rate (%)')
ax1.set_xticks(x)
ax1.set_xticklabels(methods, fontsize=8)
ax1.set_ylim(0, 44)
ax1.set_yticks([0, 10, 20, 30, 40])
ax1.yaxis.grid(True, alpha=0.08, linestyle='-', zorder=0)

# Legend
legend_elements = [
    mpatches.Patch(facecolor=C_DENSE, label='Collapsed (0%)'),
    mpatches.Patch(facecolor=C_REINF_PP, label='No improvement'),
    mpatches.Patch(facecolor=C_CELL_D, label='Episode-level fix'),
]
ax1.legend(handles=legend_elements, loc='upper left', fontsize=7.5,
           frameon=False, handlelength=1.0, borderpad=0.3)

ax1.text(-0.10, 1.06, '(a)', transform=ax1.transAxes, fontsize=13,
         fontweight='bold', va='bottom')

# ═══════════════════ Panel (b): Dense Reward Format Gaming ═══════════════════

categories = ['Action\nValidity', 'Task\nSuccess']
before = [60, 0]
after = [97.5, 0]

x2 = np.arange(len(categories))
w2 = 0.30

display_before = [v if v > 0 else 2.0 for v in before]
bars_before = ax2.bar(x2 - w2/2, display_before, w2, label='Before training',
                      color=C_BEFORE, edgecolor='none', zorder=3)
# Hatch the 0-value before bar
if before[1] == 0:
    bars_before[1].set_hatch('///')
    bars_before[1].set_edgecolor(C_BEFORE)
    bars_before[1].set_alpha(0.5)
bars_after_vals = after.copy()
bars_after_colors = [C_AFTER, C_COLLAPSE]  # validity improved, task still 0%

for i in range(len(categories)):
    display_val = after[i] if after[i] > 0 else 2.0  # small bar for 0%
    ax2.bar(x2[i] + w2/2, display_val, w2, color=bars_after_colors[i],
            edgecolor='none', zorder=3,
            hatch='///' if after[i] == 0 else None,
            alpha=0.5 if after[i] == 0 else 1.0)

# Value labels
for i, (bv, av) in enumerate(zip(before, after)):
    # Before
    if bv > 0:
        ax2.text(x2[i] - w2/2, bv + 1.5, f'{bv}%', ha='center', va='bottom',
                 fontsize=7.5, color='#555555')
    else:
        ax2.text(x2[i] - w2/2, 2.5, '0%', ha='center', va='bottom',
                 fontsize=7.5, color='#888888')
    # After
    if av > 0:
        ax2.text(x2[i] + w2/2, av + 1.5, f'{av}%', ha='center', va='bottom',
                 fontsize=7.5, color='#444444')
    else:
        ax2.text(x2[i] + w2/2, 3.5, '0%', ha='center', va='bottom',
                 fontsize=7.5, color='#888888')

# Arrow showing validity increase
mid_y = (before[0] + after[0]) / 2
ax2.annotate('', xy=(x2[0] + w2/2, after[0] - 1),
             xytext=(x2[0] - w2/2, before[0] + 1),
             arrowprops=dict(arrowstyle='->', color='#555555', lw=1.3))
ax2.text(x2[0] + 0.38, mid_y, '+37.5pp', fontsize=8, color='#555555',
         fontstyle='italic', va='center')

ax2.set_ylabel('Rate (%)')
ax2.set_xticks(x2)
ax2.set_xticklabels(categories, fontsize=9)
ax2.set_ylim(0, 112)
ax2.set_yticks([0, 25, 50, 75, 100])
ax2.yaxis.grid(True, alpha=0.08, linestyle='-', zorder=0)

# Legend
legend_elements = [
    mpatches.Patch(facecolor=C_BEFORE, label='Before training'),
    mpatches.Patch(facecolor=C_AFTER, label='After training'),
]
ax2.legend(handles=legend_elements, loc='upper right', fontsize=8,
           frameon=False, handlelength=1.0, borderpad=0.3)

ax2.text(-0.10, 1.06, '(b)', transform=ax2.transAxes, fontsize=13,
         fontweight='bold', va='bottom')

# ── Save ──
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper'
fig.savefig(f'{out_dir}/fig_additional_conditions.pdf')
fig.savefig(f'{out_dir}/fig_additional_conditions.png')
plt.close()
print('Done: fig_additional_conditions.pdf + .png')
