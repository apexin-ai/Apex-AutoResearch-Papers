"""Draft Figure 2 v3: SC% x-axis + ±2pp equivalence band + regime structure.
方案B: 强化叙事结构，减少视觉杂乱。
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch
import numpy as np

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
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
})

COLORS = {
    'Mistral-7B':   '#D55E00',
    'LLaMA-3.1-8B': '#0072B2',
    'Qwen2.5':      '#E69F00',
    'Qwen3-14B':    '#009E73',
}
DATASET_MARKERS = {'PW': 's', 'FOLIO': '^', 'LogiQA': 'o'}

# (family, dataset, label, n, SC%, Δpp, p_value)
data = [
    ('Mistral-7B',    'PW',     'Mistral PW',       600, 39.33, -2.83, 0.014),
    ('Mistral-7B',    'LogiQA', 'LogiQA',           200, 50.00,  1.50, 0.581),
    ('Mistral-7B',    'FOLIO',  'FOLIO s123',       204, 54.41,  2.94, 0.070),
    ('Mistral-7B',    'FOLIO',  'FOLIO s456',       204, 55.88,  0.00, 1.000),
    ('Mistral-7B',    'FOLIO',  'FOLIO s789',       204, 59.31, -2.45, 0.267),
    ('LLaMA-3.1-8B',  'FOLIO',  'LLaMA FOLIO',     204, 66.18, -4.41, 0.093),
    ('LLaMA-3.1-8B',  'PW',     'LLaMA PW',        200, 72.00,  2.00, 0.424),
    ('Qwen2.5',       'FOLIO',  'Q14B FOLIO-ICL',   199, 74.37,  0.50, 1.000),
    ('Qwen2.5',       'PW',     'Q14B PW',          600, 74.00, -2.50, 0.011),
    ('Qwen2.5',       'FOLIO',  'Q14B 4s FOLIO',    204, 75.01, -1.24, 1.000),
    ('Qwen2.5',       'FOLIO',  'Q7B FOLIO',        204, 75.98,  0.49, 1.000),
    ('Qwen2.5',       'LogiQA', 'Q14B LogiQA',      200, 79.00, -1.00, 0.625),
    ('Qwen3-14B',     'FOLIO',  'Q3 FOLIO',         204, 83.33,  1.47, 1.000),
    ('Qwen3-14B',     'PW',     'Q3 PW',            600, 85.83, -0.17, 1.000),
    ('Qwen3-14B',     'FOLIO',  'Q3 think',         204, 86.27,  0.49, 1.000),
]

fig, ax = plt.subplots(figsize=(5.5, 3.2))

# ±2pp equivalence band (core visual: "noise zone")
ax.axhspan(-2, 2, color='#E8E8E8', alpha=0.5, zorder=0, linewidth=0)
ax.axhline(y=2, color='#CCCCCC', ls=':', lw=0.5, zorder=0)
ax.axhline(y=-2, color='#CCCCCC', ls=':', lw=0.5, zorder=0)
ax.text(88.5, 1.6, r'$\pm 2$pp', fontsize=6.5, color='#999999',
        ha='right', va='top', fontstyle='italic')

# Δ=0 reference
ax.axhline(y=0, color='#AAAAAA', ls='--', lw=0.6, zorder=1)

# Regime boundary lines
for bx in [45, 60]:
    ax.axvline(bx, color='#DDDDDD', lw=0.5, ls='--', zorder=0)

# Plot data: color=model, marker=dataset
stroke = [pe.withStroke(linewidth=2.0, foreground='white')]
for family, dataset, label, n, sc, delta, pval in data:
    color = COLORS[family]
    marker = DATASET_MARKERS[dataset]
    is_sig = pval < 0.05
    ax.scatter(sc, delta, marker=marker, s=55, c=color,
               edgecolors=color, linewidths=0.4, zorder=4, alpha=0.88)
    if is_sig:
        ax.scatter(sc, delta, marker='o', s=200, facecolors='none',
                   edgecolors='#333333', linewidths=1.3, zorder=3)

# Connect Mistral FOLIO seeds with thin line to show variance
seed_pts = [(54.41, 2.94), (55.88, 0.00), (59.31, -2.45)]
xs, ys = zip(*seed_pts)
ax.plot(xs, ys, color='#D55E00', lw=0.7, ls='-', alpha=0.35, zorder=2)

# Seed variance bracket annotation
ax.annotate('', xy=(54.41, 3.2), xytext=(59.31, 3.2),
            arrowprops=dict(arrowstyle='<->', color='#AA6644', lw=0.6))
t = ax.text(56.86, 3.55, 'seed\nvariance', fontsize=6, color='#AA6644',
            ha='center', va='bottom', linespacing=1.3)
t.set_path_effects(stroke)

# Regime labels at bottom
ax.text(39, -4.2, 'Type C\n(error amp.)', color='#B54A00', ha='center',
        fontsize=6.5, fontstyle='italic', alpha=0.5, va='top', linespacing=0.9)
ax.text(52.5, -4.2, 'Intermediate', color='#007D5F', ha='center',
        fontsize=6.5, fontstyle='italic', alpha=0.5, va='top')
ax.text(75, -4.2, 'Type A (confirmation bias)', color='#005A8E', ha='center',
        fontsize=6.5, fontstyle='italic', alpha=0.5, va='top')

# Axes
ax.set_xlabel('SC baseline accuracy (%)')
ax.set_ylabel(r'SICA $\Delta$ (pp)')
ax.set_xlim(33, 90)
ax.set_ylim(-5.8, 5.5)
ax.set_xticks([40, 50, 60, 70, 80, 90])

for spine in ax.spines.values():
    spine.set_color('#AAAAAA')

# Legend: models (color) + datasets (marker) + significance
model_handles = []
for family in ['Mistral-7B', 'LLaMA-3.1-8B', 'Qwen2.5', 'Qwen3-14B']:
    model_handles.append(Line2D([0], [0], marker='o', color='w',
                                markerfacecolor=COLORS[family],
                                markeredgecolor=COLORS[family],
                                markersize=5.5, lw=0, label=family))
dataset_handles = []
for ds, mk in [('PW', 's'), ('FOLIO', '^'), ('LogiQA', 'o')]:
    dataset_handles.append(Line2D([0], [0], marker=mk, color='w',
                                  markerfacecolor='#888888',
                                  markeredgecolor='#888888',
                                  markersize=5.5, lw=0, label=ds))
sig_handle = Line2D([0], [0], marker='o', color='w',
                    markerfacecolor='none', markeredgecolor='#333333',
                    markeredgewidth=1.1, markersize=7, lw=0, label='$p < .05$')
all_handles = model_handles + dataset_handles + [sig_handle]
ax.legend(handles=all_handles, loc='upper right', framealpha=0.92,
          edgecolor='#DDDDDD', borderpad=0.3, handletextpad=0.2,
          labelspacing=0.2, fontsize=7, ncol=2, columnspacing=0.8)

plt.tight_layout()

out = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures'
fig.savefig(f'{out}/f2_draft_v3.png')
fig.savefig(f'{out}/f2_draft_v3.pdf')
plt.close()
print('Done: f2_draft_v3')
