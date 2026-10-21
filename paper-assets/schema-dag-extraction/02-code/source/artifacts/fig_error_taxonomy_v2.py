#!/usr/bin/env python3
"""Figure 2: Error Taxonomy — dual-panel line plots.

Replaces stacked bars with line plots to emphasize monotonic IntraSub scaling.
L0: Matches Fig 1 styling (ACL/EMNLP IE paper)
L1: Okabe-Ito, no grid, no top/right spines, >=7pt, PDF TrueType
L2: Semantic line styles (solid=IntraSub, dashed=missed/other), insight annotations
L3: Pattern B (fill_between for IntraSub growth), Pattern F (label offsets)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7.5,
    'legend.fontsize': 6.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'lines.linewidth': 1.4,
    'lines.markersize': 5,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# Grayscale-safe palette: colors chosen for well-separated luminance values.
# Grayscale luminance ≈ 0.299*R + 0.587*G + 0.114*B
# Target: 3 luminance levels spaced ~0.25 apart for clear grayscale distinction.
# C_INTRA  '#8B2500' → lum ≈ 0.25  (darkest — protagonist, IntraSub)
# C_MISSED '#6B8FC2' → lum ≈ 0.54  (medium — Missed/ExtraSub)
# C_OTHER  '#BBBBBB' → lum ≈ 0.73  (lightest — background role)
# Separation: INTRA↔MISSED = 0.29, MISSED↔OTHER = 0.19, INTRA↔OTHER = 0.48
# Plus distinct markers (o/s/^) and line styles (-/--/:) for triple redundancy.
C_INTRA  = '#CC6677'   # Soft Rose — IntraSub (matches High-BCS semantic)
C_MISSED = '#4477AA'   # Steel Blue — Missed/ExtraSub
C_OTHER  = '#CCCCCC'   # Light gray — Other/Correct
stroke = [pe.withStroke(linewidth=2, foreground='white')]

fig, (ax_ner, ax_re) = plt.subplots(1, 2, figsize=(7.0, 3.0))

# ========== (a) Few-NERD NER ==========
bins_ner = ['Solo\n(BCS=0)', 'Low\n(0.5–0.7)', 'Med\n(0.7–0.8)', 'High\n(≥0.95)']
x_ner = np.arange(len(bins_ner))
intra_ner  = np.array([0.0, 1.6, 10.6, 49.4])
extra_ner  = np.array([90.3, 80.0, 65.0, 30.8])
other_ner  = 100.0 - intra_ner - extra_ner

ax_ner.plot(x_ner, intra_ner, '-', color=C_INTRA, marker='o', markersize=6,
            markeredgecolor='black', markeredgewidth=0.5, label='IntraSub', zorder=3,
            linewidth=1.8)
ax_ner.plot(x_ner, extra_ner, '--', color=C_MISSED, marker='s', markersize=5.5,
            markeredgecolor='black', markeredgewidth=0.5, label='ExtraSub', zorder=3,
            linewidth=1.4)
ax_ner.plot(x_ner, other_ner, ':', color=C_OTHER, marker='^', markersize=5,
            markeredgecolor='#888888', markeredgewidth=0.6, label='Other', zorder=2,
            linewidth=1.2, alpha=0.8)

# Fill under IntraSub with hatching for grayscale distinction
ax_ner.fill_between(x_ner, 0, intra_ner, color=C_INTRA, alpha=0.10, zorder=1,
                    hatch='///', edgecolor=C_INTRA, linewidth=0.0)

ax_ner.set_xticks(x_ner)
ax_ner.set_xticklabels(bins_ner)
ax_ner.set_xlabel('BCS Bin')
ax_ner.set_ylabel('Error Share (%)')
ax_ner.set_ylim(-3, 100)
ax_ner.set_title('(a) Few-NERD NER', fontsize=9, pad=4)
ax_ner.legend(loc='upper right', framealpha=0.95, edgecolor='none')

# ========== (b) FewRel RE ==========
bins_re = ['Solo\n(BCS=0)', 'Low\n(0.565)', 'Med\n(0.729)', 'High\n(0.86)', 'V.High\n(0.971)']
x_re = np.arange(len(bins_re))
correct_re = np.array([85.73, 85.42, 75.70, 66.67, 52.03])
wrong_re   = np.array([0.0, 4.17, 13.0, 20.28, 32.25])
missed_re  = np.array([14.27, 10.42, 11.3, 13.05, 15.71])

ax_re.plot(x_re, wrong_re, '-', color=C_INTRA, marker='o', markersize=6,
           markeredgecolor='black', markeredgewidth=0.5, label='WrongType', zorder=3,
           linewidth=1.8)
ax_re.plot(x_re, missed_re, '--', color=C_MISSED, marker='s', markersize=5.5,
           markeredgecolor='black', markeredgewidth=0.5, label='Missed', zorder=3,
           linewidth=1.4)
ax_re.plot(x_re, correct_re, ':', color=C_OTHER, marker='^', markersize=5,
           markeredgecolor='#888888', markeredgewidth=0.6, label='Correct', zorder=2,
           linewidth=1.2, alpha=0.8)

# Fill under WrongType with hatching for grayscale distinction
ax_re.fill_between(x_re, 0, wrong_re, color=C_INTRA, alpha=0.10, zorder=1,
                   hatch='///', edgecolor=C_INTRA, linewidth=0.0)

ax_re.set_xticks(x_re)
ax_re.set_xticklabels(bins_re)
ax_re.set_xlabel('BCS Bin')
ax_re.set_ylabel('Share (%)')
ax_re.set_ylim(-3, 100)
ax_re.set_title('(b) FewRel RE', fontsize=9, pad=4)
ax_re.legend(loc='upper right', framealpha=0.95, edgecolor='none')

plt.tight_layout(w_pad=1.5, pad=0.3)
outdir = os.environ.get('FIG_OUTDIR',
    '/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/figures/paper')
os.makedirs(outdir, exist_ok=True)
outpath = os.path.join(outdir, 'fig_error_taxonomy.pdf')
fig.savefig(outpath, format='pdf')
fig.savefig(outpath.replace('.pdf', '.png'), format='png', dpi=300)
print(f'Saved: {outpath}')
plt.close()
