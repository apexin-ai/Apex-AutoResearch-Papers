"""Optimized Figure 2: SICA Δ vs SC baseline scatter — regime structure.
Data from Table 1 (main_results) in experiments.tex.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.lines import Line2D
import numpy as np

# ── Unified academic style ──
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

# ── Paper-unified semantic color palette ──
COLORS = {
    'Mistral-7B':    '#D55E00',   # vermillion
    'LLaMA-3.1-8B': '#0072B2',   # blue
    'Qwen2.5':      '#E69F00',   # amber
    'Qwen3-14B':    '#009E73',   # green
}
MARKERS = {
    'Mistral-7B':    's',
    'LLaMA-3.1-8B': '^',
    'Qwen2.5':      'o',
    'Qwen3-14B':    'D',
}

# ── Data from Table 1 (experiments.tex) ──
# (model_family, label, n, SC%, Δpp, p_value)
data = [
    # Type C
    ('Mistral-7B',    'Mistral PW',       600, 39.33, -2.83, 0.014),
    # Intermediate SC
    ('Mistral-7B',    'LogiQA',           200, 50.00,  1.50, 0.581),
    ('Mistral-7B',    'FOLIO s123',       204, 54.41,  2.94, 0.070),
    ('Mistral-7B',    'FOLIO s456',       204, 55.88,  0.00, 1.000),
    ('Mistral-7B',    'FOLIO s789',       204, 59.31, -2.45, 0.267),
    # Type A
    ('LLaMA-3.1-8B', 'LLaMA FOLIO',      204, 66.18, -4.41, 0.093),
    ('LLaMA-3.1-8B', 'LLaMA SQA',        200, 72.00,  2.00, 0.424),
    ('Qwen2.5',      'Q14B FOLIO-ICL',    199, 74.37,  0.50, 1.000),
    ('Qwen2.5',      'Q14B PW',           600, 74.00, -2.50, 0.011),
    ('Qwen2.5',      'Q14B 4s FOLIO',     204, 75.01, -1.24, 1.000),
    ('Qwen2.5',      'Q7B FOLIO',         204, 75.98,  0.49, 1.000),
    ('Qwen2.5',      'Q14B LogiQA',       200, 79.00, -1.00, 0.625),
    ('Qwen3-14B',    'Q3 FOLIO',          204, 83.33,  1.47, 1.000),
    ('Qwen3-14B',    'Q3 PW',             600, 85.83, -0.17, 1.000),
    ('Qwen3-14B',    'Q3 think',          204, 86.27,  0.49, 1.000),
]

fig, ax = plt.subplots(figsize=(5.2, 3.5))

# ── Regime background bands (continuous, subtle) ──
ax.axvspan(33, 40, alpha=0.045, color='#D55E00', zorder=0)
ax.axvspan(40, 60, alpha=0.035, color='#009E73', zorder=0)
ax.axvspan(60, 90, alpha=0.035, color='#0072B2', zorder=0)
# Thin vertical boundary lines
for bx in [40, 60]:
    ax.axvline(bx, color='#CCCCCC', lw=0.4, zorder=0)

# ── Reference line at Δ=0 ──
ax.axhline(y=0, color='#AAAAAA', ls='--', lw=0.7, zorder=1)

# ── Plot data points ──
for family, label, n, sc, delta, pval in data:
    color = COLORS[family]
    marker = MARKERS[family]
    is_sig = pval < 0.05
    is_small = n < 100

    mfc = 'white' if is_small else color
    mec = color
    mew = 1.4 if is_small else 0.5
    ms = 58

    ax.scatter(sc, delta, marker=marker, s=ms, c=mfc,
               edgecolors=mec, linewidths=mew, zorder=4, alpha=0.90)

    if is_sig:
        ax.scatter(sc, delta, marker='o', s=180, facecolors='none',
                   edgecolors='#222222', linewidths=1.4, zorder=3)

# ── Regime labels (top of plot, italic, muted) ──
txt_kw = dict(fontsize=8, fontstyle='italic', alpha=0.45, va='top')
ax.text(36.5, 5.3, 'Type C', color='#B54A00', ha='center', **txt_kw)
ax.text(50, 5.3, 'Intermediate SC', color='#007D5F', ha='center', **txt_kw)
ax.text(70, 5.3, 'Type A', color='#005A8E', ha='left', **txt_kw)

# ── Seed labels for Mistral FOLIO seeds ──
seed_kw = dict(fontsize=6.5, color='#AA6644', alpha=0.75)
ax.text(55.0, 3.35, 's123', ha='left', va='bottom', **seed_kw)
ax.text(56.5, 0.35, 's456', ha='left', va='bottom', **seed_kw)
ax.text(59.9, -2.10, 's789', ha='left', va='top', **seed_kw)

# ── Key annotations with arrows ──
annot_kw = dict(fontsize=7.5, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#666666', lw=0.7,
                                connectionstyle='arc3,rad=0.12'))

t = ax.annotate('Mistral PW\n$\\Delta{=}{-}2.83$*', xy=(39.33, -2.83),
                xytext=(46, -5.0), ha='center', color='#D55E00', **annot_kw)
t.set_path_effects([pe.withStroke(linewidth=2.2, foreground='white')])

t = ax.annotate('Qwen14B PW\n$\\Delta{=}{-}2.50$*', xy=(74.00, -2.50),
                xytext=(82, -4.2), ha='center', color='#C08600', **annot_kw)
t.set_path_effects([pe.withStroke(linewidth=2.2, foreground='white')])

t = ax.annotate('$\\Delta{=}{-}4.41$', xy=(66.18, -4.41),
                xytext=(63.5, -5.5), ha='center', fontsize=7, color='#0072B2',
                arrowprops=dict(arrowstyle='->', color='#0072B2', lw=0.6))
t.set_path_effects([pe.withStroke(linewidth=2.2, foreground='white')])

# ── Axes ──
ax.set_xlabel('SC baseline accuracy (%)')
ax.set_ylabel(r'SICA $\Delta$ (pp)')
ax.set_xlim(33, 90)
ax.set_ylim(-6.0, 5.8)
ax.set_xticks([40, 50, 60, 70, 80, 90])

# ── Legend ──
handles = []
for family in ['Mistral-7B', 'LLaMA-3.1-8B', 'Qwen2.5', 'Qwen3-14B']:
    handles.append(Line2D([0], [0], marker=MARKERS[family], color='w',
                          markerfacecolor=COLORS[family],
                          markeredgecolor=COLORS[family],
                          markersize=6, lw=0, label=family))
handles.append(Line2D([0], [0], marker='o', color='w',
                      markerfacecolor='none', markeredgecolor='#222222',
                      markeredgewidth=1.2, markersize=8, lw=0, label='$p < .05$'))
ax.legend(handles=handles, loc='upper right', framealpha=0.92,
          edgecolor='#DDDDDD', borderpad=0.35, handletextpad=0.25,
          labelspacing=0.25, columnspacing=0.5, fontsize=7.5)

plt.tight_layout()

out = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures'
fig.savefig(f'{out}/f2_regime_scatter.pdf')
fig.savefig(f'{out}/f2_regime_scatter.png')
plt.close()
print('Done: f2_regime_scatter v2')
