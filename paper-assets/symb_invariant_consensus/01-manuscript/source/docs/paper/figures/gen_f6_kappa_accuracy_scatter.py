import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# --- Mistral-7B method points (filled markers) ---
m_labels = ['Debate', 'Diverse-Prompt', 'SC (Mistral)', 'ICG']
m_kappa  = [0.155,    0.403,            0.438,          0.465]
m_acc    = [38.24,    54.41,            56.86,          51.96]
m_colors = ['#D55E00', '#009E73', '#0072B2', '#E69F00']
m_markers = ['v',      'D',       's',       'o']

# --- Cross-model SC points (open markers) ---
x_labels = ['LLaMA-8B', 'Qwen-7B', 'Qwen-14B']
x_kappa  = [0.412,      0.658,     0.738]
x_acc    = [66.18,      75.98,     75.98]
x_color  = '#882D8B'
x_markers = ['^',       'p',       'h']

fig, ax = plt.subplots(figsize=(5.2, 3.8))

# Same-model ceiling shaded region
ax.axvspan(0.40, 0.47, color='#888888', alpha=0.08, zorder=0)
ax.text(0.435, 82, 'same-model\nceiling', ha='center', va='top',
        fontsize=7.5, color='#888888', fontstyle='italic', linespacing=1.1)

# SC baseline horizontal line (Mistral)
ax.axhline(y=56.86, color='#AAAAAA', linestyle='--', linewidth=0.8, zorder=1)
ax.text(0.08, 57.8, 'SC baseline (Mistral)', ha='left', va='bottom',
        fontsize=7.5, color='#999999')

# Mistral-7B method points (filled)
for i in range(len(m_labels)):
    ax.scatter(m_kappa[i], m_acc[i], c=m_colors[i], marker=m_markers[i],
               s=110, zorder=5, edgecolors='white', linewidths=0.5)

# Cross-model SC points (open)
for i in range(len(x_labels)):
    ax.scatter(x_kappa[i], x_acc[i], facecolors='white', edgecolors=x_color,
               marker=x_markers[i], s=120, zorder=5, linewidths=1.8)

# --- Annotations ---
m_annot = {
    'Debate':         {'xy': (10, -2),  'ha': 'left',  'va': 'center'},
    'Diverse-Prompt': {'xy': (-8, -12), 'ha': 'right', 'va': 'top'},
    'SC (Mistral)':   {'xy': (-8, 6),   'ha': 'right', 'va': 'bottom'},
    'ICG':            {'xy': (8, -10),  'ha': 'left',  'va': 'top'},
}
for i, m in enumerate(m_labels):
    cfg = m_annot[m]
    ax.annotate(m, (m_kappa[i], m_acc[i]),
                xytext=cfg['xy'], textcoords='offset points',
                fontsize=8.5, fontweight='bold', color=m_colors[i],
                ha=cfg['ha'], va=cfg['va'])

x_annot = {
    'LLaMA-8B':  {'xy': (8, 4),   'ha': 'left',  'va': 'bottom'},
    'Qwen-7B':   {'xy': (-8, 6),  'ha': 'right', 'va': 'bottom'},
    'Qwen-14B':  {'xy': (-8, -8), 'ha': 'right', 'va': 'top'},
}
for i, m in enumerate(x_labels):
    cfg = x_annot[m]
    ax.annotate(m, (x_kappa[i], x_acc[i]),
                xytext=cfg['xy'], textcoords='offset points',
                fontsize=8.5, fontweight='bold', color=x_color,
                ha=cfg['ha'], va=cfg['va'])

# --- Legend ---
method_handle = mlines.Line2D([], [], color='#555555', marker='s', markersize=7,
                               markerfacecolor='#555555', markeredgecolor='white',
                               linestyle='None', label='Mistral-7B methods')
cross_handle = mlines.Line2D([], [], color=x_color, marker='^', markersize=7,
                              markerfacecolor='white', markeredgecolor=x_color,
                              markeredgewidth=1.5, linestyle='None',
                              label='Cross-model SC')
ax.legend(handles=[method_handle, cross_handle], loc='upper left',
          framealpha=0.9, edgecolor='#CCCCCC', borderpad=0.4, handletextpad=0.3)

ax.set_xlabel(r"Output Correlation (Fleiss' $\kappa$)")
ax.set_ylabel('Accuracy (%)')
ax.set_xlim(0.05, 0.82)
ax.set_ylim(30, 84)

ax.set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
ax.set_yticks([30, 40, 50, 60, 70, 80])

fig.text(0.5, -0.02,
         r"Note: ICG $\kappa$ measured on per-constraint-set MAX-SAT answers; others use direct trace answers.",
         ha='center', va='top', fontsize=7, color='#666666', fontstyle='italic')

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures'
fig.savefig(f'{out_dir}/f6_kappa_accuracy_scatter.pdf')
fig.savefig(f'{out_dir}/f6_kappa_accuracy_scatter.png')
print('Saved PDF and PNG.')
