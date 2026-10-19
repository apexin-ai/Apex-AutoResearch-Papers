"""Generate paper figures for EMNLP submission."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'legend.fontsize': 7.5,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# ============================================================
# Figure 1: Training dynamics — Cell A vs Cell B vs Cell D
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 3.0))

# Cell A (h=2, step-level) — seed 1 training success
cell_a_steps = list(range(1, 16))
cell_a_train = [18.75, 14.84, 18.75, 5.47, 1.56, 3.13, 4.69, 1.56, 0, 2.34, 0, 0, 0, 0, 0]

# Cell B (h=2, episode-adv) — OOD at available checkpoints
cell_b_ood_steps = [5, 15]
cell_b_ood_vals = [5.97, 0.75]

# Cell D (full, episode) — OOD trajectory
cell_d_steps = [0, 5, 10, 15]
cell_d_ood = [0, 12.5, 18.0, 23.88]

# Panel (a): colorblind-safe palette + linestyle dual encoding
# Red dashed for collapse, blue solid for success, orange dotted for bounded
ax1.plot(cell_a_steps, cell_a_train, color='#d62728', linestyle='--', marker='o',
         markersize=3, linewidth=1.2, label='A: M1+M2', zorder=3)
ax1.plot(cell_d_steps, cell_d_ood, color='#1f77b4', linestyle='-', marker='s',
         markersize=4, linewidth=1.2, label='D: neither', zorder=3)
ax1.plot(cell_b_ood_steps, cell_b_ood_vals, color='#ff7f0e', linestyle=':', marker='^',
         markersize=4, linewidth=1.2, label='B: M1 only', zorder=3)
ax1.axhline(y=12.5, color='gray', linestyle='--', linewidth=0.8, label='SFT', zorder=1)
ax1.set_xlabel('Training Step')
ax1.set_ylabel('Success Rate (%)')
ax1.set_title('(a) Training Dynamics')
ax1.set_xlim(0, 16)
ax1.set_ylim(-2, 30)
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.22), ncol=4, framealpha=0.9, columnspacing=0.8, handletextpad=0.4)
ax1.grid(True, alpha=0.3)

# Panel (b): h-sweep bar chart
# Red = below SFT baseline, Blue = above SFT baseline, Hatch = collapsed (0%)
h_labels = ['h=2', 'h=5', 'h=10', 'h=20', 'Full']
h_ood = [0, 0, 6.25, 15.6, 23.88]
colors = ['#d62728', '#d62728', '#d62728', '#1f77b4', '#1f77b4']
hatches = ['///', '///', '', '', '']
bars = ax2.bar(h_labels, h_ood, color=colors, edgecolor='black', linewidth=0.5, width=0.6)
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)
ax2.axhline(y=12.5, color='gray', linestyle='--', linewidth=0.8)
ax2.set_ylabel('OOD Success Rate (%)')
ax2.set_title('(b) Window Size vs. Generalization')
ax2.set_ylim(0, 28)

# Legend below chart for visual alignment with panel (a)
legend_elements = [
    mpatches.Patch(facecolor='#d62728', edgecolor='black', label='Below baseline'),
    mpatches.Patch(facecolor='#1f77b4', edgecolor='black', label='Above baseline'),
    Line2D([0], [0], color='gray', linestyle='--', linewidth=0.8, label='SFT'),
]
ax2.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.22),
           ncol=3, framealpha=0.9, fontsize=7, columnspacing=0.8, handletextpad=0.4)
ax2.grid(True, alpha=0.3, axis='y')

# Vertical dashed line marking the cliff between h=10 and h=20
cliff_x = 2.5  # midpoint between bar index 2 (h=10) and 3 (h=20)
ax2.axvline(x=cliff_x, color='#555555', linestyle=':', linewidth=1.0, alpha=0.7)
ax2.text(cliff_x, 22, 'credit assignment\ncliff', fontsize=6.5, ha='center',
         fontstyle='italic', color='#555555')

for bar, val in zip(bars, h_ood):
    if val > 0:
        offset = 1.5 if val < 10 else 0.5
        ax2.text(bar.get_x() + bar.get_width()/2, val + offset, f'{val}%',
                ha='center', va='bottom', fontsize=7)
    else:
        ax2.text(bar.get_x() + bar.get_width()/2, 0.5, '0%',
                ha='center', va='bottom', fontsize=7, color='#d62728')

plt.tight_layout(w_pad=2.0)
plt.savefig('fig_training_dynamics.pdf')
plt.savefig('fig_training_dynamics.png')
print("Saved fig_training_dynamics.pdf and .png")
plt.close()

# ============================================================
# Figure 2: Cross-scale + Information Loss
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.8))

# Panel (a): 1.7B vs 8B comparison (In-Dist — fully available for all conditions)
conditions = ['SFT', 'Cell A\n(step-indep.)', 'Cell D\n(episode)']
results_1_7b = [12.5, 0, 34.38]
results_8b = [68.75, 1.5, 96.88]

x = np.arange(len(conditions))
width = 0.32
bars1 = ax1.bar(x - width/2, results_1_7b, width, label='1.7B', color='#1f77b4',
                edgecolor='black', linewidth=0.5)
bars2 = ax1.bar(x + width/2, results_8b, width, label='8B', color='#ff7f0e',
                edgecolor='black', linewidth=0.5)

for bar, val in zip(list(bars1) + list(bars2), results_1_7b + results_8b):
    if val > 0:
        ax1.text(bar.get_x() + bar.get_width()/2, val + 1.5, f'{val}',
                ha='center', va='bottom', fontsize=6.5)
    else:
        ax1.text(bar.get_x() + bar.get_width()/2, 1.5, '0',
                ha='center', va='bottom', fontsize=6.5, color='#d62728')

ax1.set_ylabel('In-Dist Success Rate (%)')
ax1.set_title('(a) Cross-Scale: 1.7B vs. 8B')
ax1.set_xticks(x)
ax1.set_xticklabels(conditions, fontsize=7.5)
ax1.set_ylim(0, 112)
ax1.legend(loc='upper left', fontsize=7.5, framealpha=0.9)
ax1.grid(True, alpha=0.3, axis='y')

# Panel (b): Information loss quantification (full context vs h=2)
settings = ['8B\nALFWorld', 'ScienceWorld\n(1.7B)']
full_ctx = [68.75, 34.8]
h2_ctx = [31.25, 4.5]
gaps = [37.5, 30.3]

x2 = np.arange(len(settings))
bars_full = ax2.bar(x2 - width/2, full_ctx, width, label='Full context', color='#2ca02c',
                    edgecolor='black', linewidth=0.5)
bars_h2 = ax2.bar(x2 + width/2, h2_ctx, width, label='h=2 window', color='#d62728',
                  edgecolor='black', linewidth=0.5)

for i, (bf, bh, gap) in enumerate(zip(bars_full, bars_h2, gaps)):
    mid_x = (bf.get_x() + bf.get_width()/2 + bh.get_x() + bh.get_width()/2) / 2
    mid_y = (full_ctx[i] + h2_ctx[i]) / 2
    ax2.annotate('', xy=(bh.get_x() + bh.get_width()/2, h2_ctx[i] + 1),
                xytext=(bf.get_x() + bf.get_width()/2, full_ctx[i] - 1),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1.2))
    ax2.text(mid_x + 0.18, mid_y, f'{gap}pp\ngap', fontsize=6.5, ha='center',
            va='center', color='#555555', fontstyle='italic')

ax2.set_ylabel('In-Dist Success Rate (%)')
ax2.set_title('(b) Information Loss (M1)')
ax2.set_xticks(x2)
ax2.set_xticklabels(settings, fontsize=7.5)
ax2.set_ylim(0, 82)
ax2.legend(loc='upper right', fontsize=7, framealpha=0.9)
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout(w_pad=2.0)
plt.savefig('fig_cross_scale.pdf')
plt.savefig('fig_cross_scale.png')
print("Saved fig_cross_scale.pdf and .png")
plt.close()

# ============================================================
# Figure 3: Standard remedies fail + Dense reward gaming
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.8))

# Panel (a): Standard remedies all fail — only episode-level works
# All confirmed data from paper Section 4.4 and Table 1
methods = ['SFT\nbaseline', r'Dense'+'\nreward', r'$\gamma{=}1.0$'+'\n(h=5)', 'REINF\n++', 'Cell D\n(ours)']
in_dist = [12.5, 0, 0, 12.5, 34.38]
bar_colors = ['gray', '#d62728', '#d62728', '#e377c2', '#1f77b4']

x = np.arange(len(methods))
bars = ax1.bar(x, in_dist, color=bar_colors, edgecolor='black', linewidth=0.5, width=0.6)
ax1.axhline(y=12.5, color='gray', linestyle='--', linewidth=0.8, alpha=0.6)

for bar, val in zip(bars, in_dist):
    if val > 0:
        ax1.text(bar.get_x() + bar.get_width()/2, val + 1.0, f'{val}%',
                ha='center', va='bottom', fontsize=6.5)
    else:
        ax1.text(bar.get_x() + bar.get_width()/2, 1.0, '0%',
                ha='center', va='bottom', fontsize=6.5, color='#d62728')

ax1.set_ylabel('In-Dist Success Rate (%)')
ax1.set_title('(a) Standard Remedies Fail')
ax1.set_xticks(x)
ax1.set_xticklabels(methods, fontsize=6.5)
ax1.set_ylim(0, 45)
ax1.grid(True, alpha=0.3, axis='y')

legend_elements = [
    mpatches.Patch(facecolor='#d62728', edgecolor='black', label='Collapsed (0%)'),
    mpatches.Patch(facecolor='#e377c2', edgecolor='black', label='No improvement'),
    mpatches.Patch(facecolor='#1f77b4', edgecolor='black', label='Episode-level fix'),
]
ax1.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, -0.25),
           ncol=3, framealpha=0.9, fontsize=6.5, columnspacing=0.6, handletextpad=0.3)

# Panel (b): Dense reward gaming — before vs after training
# Confirmed: validity 60% → 97.5%, task success 0% → 0%
categories = ['Action\nValidity', 'Task\nSuccess']
before = [60, 0]
after = [97.5, 0]

x2 = np.arange(len(categories))
width = 0.30
bars_before = ax2.bar(x2 - width/2, before, width, label='Before training',
                      color='#bcbddc', edgecolor='black', linewidth=0.5)
bars_after = ax2.bar(x2 + width/2, after, width, label='After training',
                     color='#2ca02c', edgecolor='black', linewidth=0.5)
# Override task success "after" bar color to red (still 0%)
bars_after[1].set_facecolor('#d62728')

for bar, val in zip(list(bars_before) + list(bars_after), before + after):
    if val > 0:
        ax2.text(bar.get_x() + bar.get_width()/2, val + 1.5, f'{val}%',
                ha='center', va='bottom', fontsize=7)
    else:
        ax2.text(bar.get_x() + bar.get_width()/2, 1.5, '0%',
                ha='center', va='bottom', fontsize=7, color='#d62728')

# Arrow showing validity increase
ax2.annotate('', xy=(x2[0] + width/2, 95), xytext=(x2[0] - width/2, 62),
            arrowprops=dict(arrowstyle='->', color='#555555', lw=1.5))
ax2.text(x2[0] + 0.35, 78, '+37.5pp', fontsize=7, color='#555555', fontstyle='italic')

ax2.set_ylabel('Rate (%)')
ax2.set_title('(b) Dense Reward: Format Gaming')
ax2.set_xticks(x2)
ax2.set_xticklabels(categories, fontsize=8)
ax2.set_ylim(0, 112)
ax2.legend(loc='upper right', fontsize=7, framealpha=0.9)
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout(w_pad=2.0)
plt.savefig('fig_additional_conditions.pdf')
plt.savefig('fig_additional_conditions.png')
print("Saved fig_additional_conditions.pdf and .png")
plt.close()

print("All figures generated successfully.")
