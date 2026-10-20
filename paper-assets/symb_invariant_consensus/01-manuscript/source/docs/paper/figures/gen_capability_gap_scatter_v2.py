"""Optimized Figure A.4: Capability gap scatter with sigmoid fit.
Data from §6 cross-architecture analysis + appendix tables.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from scipy.optimize import curve_fit

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.5,
})

# ── Paper-unified palette ──
C_DEBERTA   = '#0072B2'  # blue (primary verifier)
C_LLAMA_GEN = '#E69F00'  # amber (LLaMA generator)
C_ROBERTA   = '#D55E00'  # vermillion
C_BART      = '#009E73'  # green
C_FINETUNED = '#882D8B'  # purple

# ── Data (all at w=3) ──
deberta_pts = [
    (-36.76, 0.49, 'Qwen3-14B$_{\\mathrm{think}}$\nFOLIO'),
    (-33.82, 0.49, 'Qwen3-14B\nFOLIO'),
    (-30.83, 0.50, 'Qwen3-14B\nPW-D5'),
    (-19.00, 0.67, 'Qwen2.5-14B\nPW-D5'),
    (-6.37,  2.94, 'Mistral-7B\nFOLIO'),
    (15.67,  6.67, 'Mistral-7B\nPW-D5'),
]
llama_pt = (-17.50, 0.83, 'LLaMA-8B\nPW-D5')
multi_nli = [
    (-1.66, 4.17, 'RoBERTa'),
    (6.84,  5.17, 'BART'),
]
finetuned_pts = [
    (27.17, 11.67, 'LLaMA-8B\n(fine-tuned)'),
    (60.34, 12.67, 'Mistral-7B\n(fine-tuned)'),
]

# ── Sigmoid fit ──
def sigmoid(x, L, k, x0, b):
    return L / (1 + np.exp(-k * (x - x0))) + b

all_pts = deberta_pts + [llama_pt] + multi_nli
ax_all = np.array([p[0] for p in all_pts])
ay_all = np.array([p[1] for p in all_pts])

try:
    popt, _ = curve_fit(sigmoid, ax_all, ay_all,
                        p0=[3.5, 0.3, 1.0, 0.2],
                        bounds=([0.5, 0.01, -10, -1], [5.0, 2.0, 15, 2.0]),
                        maxfev=50000)
    x_fit = np.linspace(-42, 68, 500)
    y_sig = sigmoid(x_fit, *popt)
    has_sigmoid = True
except Exception:
    has_sigmoid = False
    x_fit = np.linspace(-42, 68, 500)

# ── Plot ──
fig, ax = plt.subplots(figsize=(3.8, 2.8))
fig.subplots_adjust(left=0.16, bottom=0.20, right=0.96, top=0.92)

# Region shading
ax.axvspan(-42, 0, alpha=0.025, color='#D55E00', zorder=0)
ax.axvspan(0, 68, alpha=0.025, color='#009E73', zorder=0)

# Reference lines
ax.axhline(0, color='black', linewidth=0.3, alpha=0.15)
ax.axvline(0, color='black', linewidth=0.4, alpha=0.20, linestyle=':')

# Sigmoid curve
if has_sigmoid:
    ax.plot(x_fit, y_sig, '-', color='#777777', linewidth=1.0, alpha=0.50,
            label='Sigmoid fit', zorder=2)

# DeBERTa primary
dx = np.array([p[0] for p in deberta_pts])
dy = np.array([p[1] for p in deberta_pts])
ax.scatter(dx, dy, marker='o', c=C_DEBERTA, s=45, zorder=5,
           label='DeBERTa-MNLI', edgecolors='white', linewidths=0.4)

# LLaMA generator
ax.scatter([llama_pt[0]], [llama_pt[1]], marker='D', c=C_LLAMA_GEN, s=45, zorder=5,
           label='DeBERTa (LLaMA)', edgecolors='white', linewidths=0.4)

# Multi-NLI
ax.scatter([multi_nli[0][0]], [multi_nli[0][1]], marker='s', c=C_ROBERTA, s=38, zorder=5,
           label='RoBERTa-MNLI', edgecolors='white', linewidths=0.4)
ax.scatter([multi_nli[1][0]], [multi_nli[1][1]], marker='^', c=C_BART, s=38, zorder=5,
           label='BART-MNLI', edgecolors='white', linewidths=0.4)

# Fine-tuned
fx = [p[0] for p in finetuned_pts]
fy = [p[1] for p in finetuned_pts]
ax.scatter(fx, fy, marker='*', c=C_FINETUNED, s=90, zorder=6,
           label='Fine-tuned DeBERTa', edgecolors='white', linewidths=0.4)

# ── Annotations ──
pe_white = [pe.withStroke(linewidth=1.5, foreground='white')]

# DeBERTa point annotations
annot_config = [
    (deberta_pts[0][0], deberta_pts[0][1], 'Qwen3$_{\\mathrm{think}}$', (-6, 5), 'right'),
    (deberta_pts[2][0], deberta_pts[2][1], 'Qwen3 PW', (-6, 5), 'right'),
    (deberta_pts[3][0], deberta_pts[3][1], 'Qwen14B PW', (6, 4), 'left'),
    (deberta_pts[4][0], deberta_pts[4][1], 'Mistral\nFOLIO', (-5, 5), 'right'),
    (deberta_pts[5][0], deberta_pts[5][1], 'Mistral\nPW-D5', (-5, 4), 'right'),
]
for x, y, lbl, offset, ha in annot_config:
    t = ax.annotate(lbl, (x, y), textcoords='offset points',
                    xytext=offset, fontsize=5.5, ha=ha, color='#555555',
                    linespacing=0.9)
    t.set_path_effects(pe_white)

# LLaMA
t = ax.annotate('LLaMA PW', (llama_pt[0], llama_pt[1]),
                textcoords='offset points', xytext=(6, -7), fontsize=5.5,
                ha='left', color='#AA7700')
t.set_path_effects(pe_white)

# Multi-NLI
for pt, lbl in zip(multi_nli, ['RoBERTa', 'BART']):
    t = ax.annotate(lbl, (pt[0], pt[1]), textcoords='offset points',
                    xytext=(5, 5), fontsize=5.5, ha='left',
                    color='#555555')
    t.set_path_effects(pe_white)

# Fine-tuned
for pt in finetuned_pts:
    t = ax.annotate(pt[2].replace('\n', ' '), (pt[0], pt[1]),
                    textcoords='offset points', xytext=(-5, 5), fontsize=5.5,
                    ha='right', color=C_FINETUNED)
    t.set_path_effects(pe_white)

# Region labels
ax.text(-21, 14.2, 'verifier $<$ generator', fontsize=6.5, color='#bbbbbb',
        ha='center', style='italic')
ax.text(38, 14.2, 'verifier $>$ generator', fontsize=6.5, color='#bbbbbb',
        ha='center', style='italic')

ax.set_xlabel('Capability gap (verifier $-$ generator SC, pp)')
ax.set_ylabel('Combo gain over SC (pp, $w{=}3$)')
ax.set_xlim(-42, 68)
ax.set_ylim(-0.3, 15.0)
ax.legend(loc='lower right', frameon=False,
          borderpad=0.3, handletextpad=0.3, labelspacing=0.25)

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/figures'
fig.savefig(f'{outdir}/capability_gap_scatter.pdf')
fig.savefig(f'{outdir}/capability_gap_scatter.png')
plt.close()
print('Done: capability_gap_scatter v2')
