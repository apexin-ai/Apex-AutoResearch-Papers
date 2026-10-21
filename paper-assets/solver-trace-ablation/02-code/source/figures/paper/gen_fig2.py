raise RuntimeError("DEPRECATED: use paper/figures/gen_fig2.py instead — this version has wrong step-100 data and missing H7 category")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 8,
    'axes.titlesize': 9,
    'axes.labelsize': 8,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7.5,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'lines.linewidth': 1.4,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

step_labels = ['0', '100', '500', '1000']
x_idx = np.arange(4)
pr = np.array([0.12, 0.32, 0.93, 0.96])
isr = np.array([0.064, 0.6423, 0.1324, 0.0028])

genuine_pct = np.array([1.00, 1.00, 0.129, 0.00])
h1_pct = np.array([0.00, 0.00, 0.871, 1.00])

COLOR_PR = '#009E73'
COLOR_ISR = '#D55E00'
COLOR_GENUINE = '#0072B2'

fig, (ax_main, ax_bar) = plt.subplots(2, 1, figsize=(3.25, 2.8),
                                       gridspec_kw={'height_ratios': [2.6, 1]},
                                       sharex=True)
ax1 = ax_main

# Left Y axis: Prove Rate
line_pr, = ax1.plot(x_idx, pr, color=COLOR_PR, marker='o', markersize=5,
                     markerfacecolor=COLOR_PR, markeredgecolor='white',
                     markeredgewidth=1.0, zorder=3, label='Prove Rate')
ax1.set_ylabel('Prove Rate', color=COLOR_PR)
ax1.tick_params(axis='y', labelcolor=COLOR_PR)
ax1.set_ylim(-0.05, 1.30)
ax1.set_xlim(-0.35, 3.35)
ax1.set_xticks(x_idx)
ax1.set_xticklabels(step_labels)

# Right Y axis: ISR
ax2 = ax1.twinx()
line_isr, = ax2.plot(x_idx, isr, color=COLOR_ISR, marker='^', markersize=5.5,
                      markerfacecolor=COLOR_ISR, markeredgecolor='white',
                      markeredgewidth=1.0, zorder=3, label='Proved-only ISR')
ax2.set_ylabel('Proved-only ISR', color=COLOR_ISR)
ax2.tick_params(axis='y', labelcolor=COLOR_ISR)
ax2.set_ylim(-0.05, 0.85)

# ISR=0 reference line
ax2.axhline(y=0, color='gray', linestyle='--', linewidth=0.6, alpha=0.5, zorder=1)

# Data point labels — PR (above markers)
pr_dy = [0.06, 0.06, -0.10, 0.06]
for i, v in enumerate(pr):
    ax1.annotate(f'{v:.2f}', (x_idx[i], v), xytext=(x_idx[i], v + pr_dy[i]),
                 fontsize=6.5, fontweight='bold', color=COLOR_PR,
                 ha='center', va='bottom' if pr_dy[i] > 0 else 'top', zorder=5)

# Data point labels — ISR (on right axis scale)
isr_dy = [0.05, 0.05, 0.05, 0.05]
for i, v in enumerate(isr):
    label = f'{v:.3f}' if v >= 0.01 else f'{v:.4f}'
    ax2.annotate(label, (x_idx[i], v), xytext=(x_idx[i], v + isr_dy[i]),
                 fontsize=6.5, fontweight='bold', color=COLOR_ISR,
                 ha='center', va='bottom', zorder=5)

# Annotation: structural collapse near step 1000
ax2.annotate('Structural\ncollapse', xy=(3, 0.0028), xytext=(2.5, 0.32),
             fontsize=6.5, color='#333333',
             bbox=dict(boxstyle='round,pad=0.25', facecolor='#FFF3E0',
                       edgecolor=COLOR_ISR, alpha=0.9, linewidth=0.7),
             arrowprops=dict(arrowstyle='->', color=COLOR_ISR, lw=0.9,
                             connectionstyle='arc3,rad=-0.2'),
             ha='center', va='center', zorder=6)

ax1.set_title('ISR Collapse Under Exec-Only Training (s42)',
              fontweight='bold', pad=4)

# Legend below title, anchored to upper-left corner
lines = [line_pr, line_isr]
labels = ['Prove Rate', 'Proved-only ISR']
leg = ax1.legend(lines, labels, loc='upper left', framealpha=0.85,
                 edgecolor='#CCCCCC', ncol=2, fontsize=6.5,
                 handlelength=1.2, columnspacing=0.8, borderpad=0.3)

ax1.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

# Bottom subplot: stacked bar (using index x for even spacing)
bar_width = 0.55
ax_bar.bar(x_idx, genuine_pct, width=bar_width, label='Genuine',
           color=COLOR_GENUINE, alpha=0.85, zorder=2)
ax_bar.bar(x_idx, h1_pct, width=bar_width, bottom=genuine_pct, label='H1',
           color='#CC79A7', alpha=0.85, zorder=2)
ax_bar.set_ylabel('Fraction', fontsize=8)
ax_bar.set_xlabel('Training Steps')
ax_bar.set_ylim(0, 1.05)
ax_bar.set_yticks([0, 0.5, 1.0])
ax_bar.set_yticklabels(['0%', '50%', '100%'])
ax_bar.legend(loc='center left', bbox_to_anchor=(1.01, 0.5),
              fontsize=6.5, framealpha=0.9,
              handlelength=1.0, borderpad=0.3)
ax_bar.spines['top'].set_visible(False)
ax_bar.spines['right'].set_visible(False)
ax_bar.grid(True, alpha=0.2, axis='y', zorder=0)

# Label bars
for i in range(4):
    g, h = genuine_pct[i], h1_pct[i]
    if g > 0.15:
        ax_bar.text(x_idx[i], g / 2, f'{g:.0%}', ha='center', va='center',
                    fontsize=6.5, color='white', fontweight='bold')
    if h > 0.15:
        ax_bar.text(x_idx[i], g + h / 2, f'{h:.0%}', ha='center', va='center',
                    fontsize=6.5, color='white', fontweight='bold')

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/figures/paper'
canonical = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures'
fig.savefig(f'{out_dir}/fig2_isr_collapse.pdf')
fig.savefig(f'{out_dir}/fig2_isr_collapse.png')
fig.savefig(f'{canonical}/fig2_isr_collapse.pdf')
fig.savefig(f'{canonical}/fig2_isr_collapse.png')
plt.close()

print('Done. Saved PDF and PNG.')
