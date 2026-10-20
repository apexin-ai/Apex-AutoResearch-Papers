"""Figure 2: Fleiss' κ vs SICA Δ scatter — soft palette aligned with Figure 3."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.lines import Line2D
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'STIXGeneral', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
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
    'axes.linewidth': 0.5,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
})

# Soft academic palette aligned with Figure 3
MODEL_COLORS = {
    'Mistral-7B':    '#E8A0BF',   # soft pink
    'LLaMA-3.1-8B':  '#7EC8A0',   # soft green
    'Qwen2.5-7B':    '#8CC5E3',   # soft sky blue
    'Qwen2.5-14B':   '#5B8FB9',   # steady blue-gray
    'Qwen3-14B':     '#E8A87C',   # warm orange
}

DOMAIN_MARKERS = {'PW': 'o', 'FOLIO': '^', 'LogiQA': 's'}

# (model, domain, kappa, delta_pp, std_or_None)
# κ from Tab independence / cross-model kappa; Δ from Tab main_results
data = [
    ("Mistral-7B",    "PW",     0.19, -2.83, None),
    ("Mistral-7B",    "FOLIO",  0.46, +2.94, None),   # s123
    ("Mistral-7B",    "FOLIO",  0.46, +0.16, 2.70),   # 3s-agg
    ("Mistral-7B",    "FOLIO",  0.46,  0.00, None),    # s456
    ("Mistral-7B",    "FOLIO",  0.45, -2.45, None),    # s789
    ("Mistral-7B",    "LogiQA", 0.51, +1.50, None),
    ("LLaMA-3.1-8B",  "FOLIO",  0.41, -4.41, None),
    ("Qwen2.5-7B",    "FOLIO",  0.66, +0.49, None),
    ("Qwen2.5-14B",   "FOLIO",  0.74, -1.24, None),   # 4s-agg
    ("Qwen2.5-14B",   "PW",     0.62, -2.50, None),
    ("Qwen2.5-14B",   "LogiQA", 0.82, -1.00, None),
    ("Qwen3-14B",     "FOLIO",  0.79, +1.47, None),
    ("Qwen3-14B",     "PW",     0.78, -0.17, None),
    ("Qwen3-14B",     "FOLIO",  0.91, +0.49, None),   # think
]

fig, ax = plt.subplots(figsize=(5, 3.5))

# Light grid
ax.grid(True, alpha=0.15, linewidth=0.4, color='#888888')
ax.set_axisbelow(True)

# Δ=0 reference line
ax.axhline(y=0, color='#BBBBBB', ls='--', lw=0.6, zorder=1)

# Plot points
for model, domain, kappa, delta, std in data:
    color = MODEL_COLORS[model]
    marker = DOMAIN_MARKERS[domain]
    ax.scatter(kappa, delta, marker=marker, s=55, c=color,
               edgecolors=color, linewidths=0.4, zorder=4, alpha=0.92)
    if std is not None:
        lighter = color + '88'  # same color, lower alpha
        ax.errorbar(kappa, delta, yerr=std, fmt='none', ecolor=color,
                    elinewidth=0.9, capsize=2.0, capthick=0.7, zorder=3, alpha=0.50)

# Annotations — dark gray text, arrow style
annot_kw = dict(fontsize=7, color='#444444',
                arrowprops=dict(arrowstyle='->', color='#999999', lw=0.6,
                                connectionstyle='arc3,rad=0.15'))
stroke = [pe.withStroke(linewidth=2.0, foreground='white')]

t = ax.annotate('Mistral PW\n$\\kappa{=}0.19$',
                xy=(0.19, -2.83), xytext=(0.13, -5.2),
                ha='center', **annot_kw)
t.set_path_effects(stroke)

t = ax.annotate('LLaMA  $\\Delta{=}{-}4.41$',
                xy=(0.41, -4.41), xytext=(0.52, -5.6),
                ha='center', **annot_kw)
t.set_path_effects(stroke)

t = ax.annotate('Qwen3 PW',
                xy=(0.78, -0.17), xytext=(0.88, -2.2),
                ha='center', **annot_kw)
t.set_path_effects(stroke)

t = ax.annotate('Qwen3 (think)\n$\\Delta{=}{+}0.49$',
                xy=(0.91, 0.49), xytext=(0.82, 3.2),
                ha='center', **annot_kw)
t.set_path_effects(stroke)

# Axes
ax.set_xlabel(r"Fleiss' $\kappa$ (trace agreement)")
ax.set_ylabel(r'SICA $\Delta$ (pp)')
ax.set_xlim(0.10, 1.00)
ax.set_ylim(-6.5, 5.5)
ax.set_xticks([0.2, 0.4, 0.6, 0.8, 1.0])

# Spine color
for spine in ax.spines.values():
    spine.set_color('#AAAAAA')

# Legend — models + domains
model_handles = []
for m in ['Mistral-7B', 'LLaMA-3.1-8B', 'Qwen2.5-7B', 'Qwen2.5-14B', 'Qwen3-14B']:
    model_handles.append(Line2D([0], [0], marker='o', color='w',
                                markerfacecolor=MODEL_COLORS[m],
                                markeredgecolor=MODEL_COLORS[m],
                                markersize=5, lw=0, label=m))

domain_handles = []
for d, mk in [('PW', 'o'), ('FOLIO', '^'), ('LogiQA', 's')]:
    domain_handles.append(Line2D([0], [0], marker=mk, color='w',
                                 markerfacecolor='#999999',
                                 markeredgecolor='#999999',
                                 markersize=5, lw=0, label=d))

all_handles = model_handles + domain_handles
ax.legend(handles=all_handles, loc='upper left', frameon=False, ncol=1,
          fontsize=7.5, handletextpad=0.3, labelspacing=0.22, borderpad=0.2)

plt.tight_layout()

out = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures'
fig.savefig(f'{out}/f2_regime_scatter_v2.pdf')
fig.savefig(f'{out}/f2_regime_scatter_v2.png')
plt.close()
print('Done: f2_regime_scatter_v2')
