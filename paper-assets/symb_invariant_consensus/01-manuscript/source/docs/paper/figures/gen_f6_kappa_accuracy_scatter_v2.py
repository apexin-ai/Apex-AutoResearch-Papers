"""Figure 5: Independence-accuracy trade-off scatter.
Data from Table kappa_generalization in appendix.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.lines as mlines

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
})

C_COLLAPSE = '#0072B2'
C_SAFE     = '#009E73'
C_BASE     = '#D55E00'
C_WARN     = '#E69F00'
C_NEUTRAL  = '#882D8B'

m_labels  = ['Debate',      'Diverse-Prompt', 'SC (Mistral)', 'ICG']
m_kappa   = [0.155,          0.403,            0.438,          0.465]
m_acc     = [38.24,          54.41,            56.86,          51.96]
m_colors  = [C_BASE,         C_SAFE,           C_COLLAPSE,     C_WARN]
m_markers = ['v',            'D',              's',            'o']

x_labels  = ['LLaMA-8B', 'Qwen-7B', 'Qwen-14B']
x_kappa   = [0.412,       0.658,     0.738]
x_acc     = [66.18,       75.98,     75.98]
x_color   = C_NEUTRAL
x_markers = ['^',         'p',       'h']

fig, ax = plt.subplots(figsize=(5.0, 3.5))

ax.axhline(y=56.86, color='#CCCCCC', linestyle='--', linewidth=0.7, zorder=1)

for i in range(len(m_labels)):
    ax.scatter(m_kappa[i], m_acc[i], c=m_colors[i], marker=m_markers[i],
               s=90, zorder=5, edgecolors='white', linewidths=0.6)

for i in range(len(x_labels)):
    ax.scatter(x_kappa[i], x_acc[i], facecolors='white', edgecolors=x_color,
               marker=x_markers[i], s=100, zorder=5, linewidths=1.6)

m_annot = {
    'Debate':         {'xy': (8, 2),   'ha': 'left',  'va': 'bottom'},
    'Diverse-Prompt': {'xy': (-6, -10), 'ha': 'right', 'va': 'top'},
    'SC (Mistral)':   {'xy': (-6, 6),   'ha': 'right', 'va': 'bottom'},
    'ICG':            {'xy': (8, -8),  'ha': 'left',  'va': 'top'},
}
for i, m in enumerate(m_labels):
    cfg = m_annot[m]
    t = ax.annotate(m, (m_kappa[i], m_acc[i]),
                    xytext=cfg['xy'], textcoords='offset points',
                    fontsize=8, fontweight='bold', color=m_colors[i],
                    ha=cfg['ha'], va=cfg['va'])
    t.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

x_annot = {
    'LLaMA-8B':  {'xy': (8, 4),   'ha': 'left',  'va': 'bottom'},
    'Qwen-7B':   {'xy': (-6, 6),  'ha': 'right', 'va': 'bottom'},
    'Qwen-14B':  {'xy': (-6, -6), 'ha': 'right', 'va': 'top'},
}
for i, m in enumerate(x_labels):
    cfg = x_annot[m]
    t = ax.annotate(m, (x_kappa[i], x_acc[i]),
                    xytext=cfg['xy'], textcoords='offset points',
                    fontsize=8, fontweight='bold', color=x_color,
                    ha=cfg['ha'], va=cfg['va'])
    t.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

method_h = mlines.Line2D([], [], color='#555555', marker='s', markersize=6,
                          markerfacecolor='#555555', markeredgecolor='white',
                          linestyle='None', label='Mistral-7B methods')
cross_h = mlines.Line2D([], [], color=x_color, marker='^', markersize=6,
                         markerfacecolor='white', markeredgecolor=x_color,
                         markeredgewidth=1.4, linestyle='None',
                         label='Cross-model SC')
ax.legend(handles=[method_h, cross_h], loc='upper left',
          framealpha=0.92, edgecolor='#DDDDDD', borderpad=0.35,
          handletextpad=0.25, fontsize=7.5)

ax.set_xlabel(r"Output Correlation (Fleiss' $\kappa$)")
ax.set_ylabel('Accuracy (%)')
ax.set_xlim(0.05, 0.82)
ax.set_ylim(30, 84)
ax.set_xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
ax.set_yticks([30, 40, 50, 60, 70, 80])

out = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures'
fig.savefig(f'{out}/f6_kappa_accuracy_scatter.pdf')
fig.savefig(f'{out}/f6_kappa_accuracy_scatter.png')
plt.close()
print('Done: f6_kappa_accuracy_scatter v2')
