"""Fig 2: κ vs SICA Δ scatter — canonical conditions only."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.lines import Line2D
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
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
})

MODEL_COLORS = {
    'Mistral-7B':       '#CC79A7',
    'LLaMA-3.1-8B':     '#009E73',
    'Qwen2.5-7B':       '#56B4E9',
    'Qwen2.5-14B':      '#0072B2',
    'Qwen3-14B':        '#D55E00',
    'Qwen3-14B (think)':'#D55E00',
}

DOMAIN_MARKERS = {'PW': 'o', 'FOLIO': '^', 'LogiQA': 's'}

# (model, domain, kappa, delta_pp, delta_std_or_None)
data = [
    ("Mistral-7B",         "PW",     0.19, -2.83, 0.95),
    ("Mistral-7B",         "FOLIO",  0.46, +3.43, 2.67),
    ("Mistral-7B",         "LogiQA", 0.51, +1.50, None),
    ("LLaMA-3.1-8B",       "FOLIO",  0.41, -4.41, None),
    ("Qwen2.5-7B",         "FOLIO",  0.66, +0.49, None),
    ("Qwen2.5-14B",        "FOLIO",  0.74, -0.49, None),
    ("Qwen2.5-14B",        "LogiQA", 0.82, -1.00, None),
    ("Qwen3-14B",          "FOLIO",  0.79, +1.47, None),
    ("Qwen3-14B",          "PW",     0.78, -0.17, 1.14),
    ("Qwen3-14B (think)",  "FOLIO",  0.91,  0.00, None),
]

fig, ax = plt.subplots(figsize=(5.2, 3.5))

# y=0 reference line
ax.axhline(y=0, color='#AAAAAA', ls='--', lw=0.7, zorder=1)

# Plot points
for model, domain, kappa, delta, std in data:
    color = MODEL_COLORS[model]
    marker = DOMAIN_MARKERS[domain]
    ax.scatter(kappa, delta, marker=marker, s=64, c=color,
               edgecolors=color, linewidths=0.5, zorder=4, alpha=0.90)
    if std is not None:
        ax.errorbar(kappa, delta, yerr=std, fmt='none', ecolor=color,
                     elinewidth=1.0, capsize=2.5, capthick=0.8, zorder=3, alpha=0.7)

# Annotations — 3 key points
annot_kw = dict(fontsize=7.5, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#666666', lw=0.7,
                                connectionstyle='arc3,rad=0.15'))

t = ax.annotate('Mistral PW\n$\\kappa{=}0.19,\\;\\Delta{=}{-}2.83$',
                xy=(0.19, -2.83), xytext=(0.27, -5.5),
                ha='center', color='#CC79A7', **annot_kw)
t.set_path_effects([pe.withStroke(linewidth=2.2, foreground='white')])

t = ax.annotate('Qwen3 (think)\n$\\Delta{=}0.00$',
                xy=(0.91, 0.00), xytext=(0.80, 3.5),
                ha='center', color='#D55E00', **annot_kw)
t.set_path_effects([pe.withStroke(linewidth=2.2, foreground='white')])

t = ax.annotate('LLaMA\n$\\Delta{=}{-}4.41$',
                xy=(0.41, -4.41), xytext=(0.53, -5.8),
                ha='center', color='#009E73', **annot_kw)
t.set_path_effects([pe.withStroke(linewidth=2.2, foreground='white')])

# Axes
ax.set_xlabel(r"Fleiss' $\kappa$ (trace agreement)")
ax.set_ylabel(r'SICA $\Delta$ (pp)')
ax.set_xlim(0.10, 1.00)
ax.set_ylim(-6.5, 6.8)
ax.set_xticks([0.2, 0.4, 0.6, 0.8, 1.0])

# Legend — models (color) + domains (shape), single column, upper left, no frame
model_handles = []
for m in ['Mistral-7B', 'LLaMA-3.1-8B', 'Qwen2.5-7B', 'Qwen2.5-14B', 'Qwen3-14B']:
    model_handles.append(Line2D([0], [0], marker='o', color='w',
                                markerfacecolor=MODEL_COLORS[m],
                                markeredgecolor=MODEL_COLORS[m],
                                markersize=5.5, lw=0, label=m))

domain_handles = []
for d, mk in [('PW', 'o'), ('FOLIO', '^'), ('LogiQA', 's')]:
    domain_handles.append(Line2D([0], [0], marker=mk, color='w',
                                 markerfacecolor='#777777',
                                 markeredgecolor='#777777',
                                 markersize=5.5, lw=0, label=d))

all_handles = model_handles + domain_handles
ax.legend(handles=all_handles, loc='upper left', frameon=False, ncol=1,
          fontsize=8, handletextpad=0.3, labelspacing=0.25, borderpad=0.2)

plt.tight_layout()

import os
out_dir = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(out_dir, 'fig2_kappa_delta.pdf'))
fig.savefig(os.path.join(out_dir, 'fig2_kappa_delta.png'))
plt.close()
print('Done: fig2_kappa_delta')
