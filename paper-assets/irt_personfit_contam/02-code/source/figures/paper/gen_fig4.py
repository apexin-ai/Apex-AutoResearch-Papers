"""Leaderboard lz* heatmap (Figure 5 in paper).

Reads empirical p-values CSV, builds a model x benchmark heatmap of lz*
scores with BH-FDR significance hatching. Models sorted by mean |lz*|.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd

import sys; sys.path.insert(0, '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/figures/paper')
import palette
palette.apply()

# ── Paths ──
BASE = '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam'
CSV = f'{BASE}/artifacts/phase_b_two_sided_v2/empirical_pvalues.csv'
OUT_PDF = f'{BASE}/figures/paper/fig_4_model_heatmap.pdf'
OUT_PNG = f'{BASE}/figures/paper/fig_4_model_heatmap.png'

# ── Data ──
df = pd.read_csv(CSV)

BENCH_ORDER = ['mmlu', 'hellaswag', 'gsm8k', 'arc_c', 'humaneval']
BENCH_LABELS = ['MMLU', 'HellaSwag', 'GSM8K', 'ARC-C', 'HumanEval']

MODEL_SHORT = {
    '360GPT2-Pro': '360GPT2-Pro',
    'DeepSeek-V3': 'DeepSeek-V3',
    'Doubao-pro': 'Doubao-pro',
    'Gemini-1.5': 'Gemini-1.5',
    'Gemma-2B-it': 'Gemma-2B-it',
    'Hunyuan-Turbo': 'Hunyuan-Turbo',
    'Mistral-7B-Instruct-v0.1': 'Mistral-7B',
    'Moonshot-v1': 'Moonshot-v1',
    'Qwen-Plus': 'Qwen-Plus',
    'Qwen2.5-3B-Instruct': 'Qwen2.5-3B',
    'Vicuna-7B-v1.3': 'Vicuna-7B',
    'Yi-Lightning': 'Yi-Lightning',
}

pivot_lz = df.pivot_table(index='model_name', columns='benchmark', values='lz_star')
pivot_lz = pivot_lz[BENCH_ORDER]

pivot_flag = df.pivot_table(index='model_name', columns='benchmark',
                            values='flagged_bh', aggfunc='first')
pivot_flag = pivot_flag[BENCH_ORDER]

# ── Sort by mean |lz*| descending ──
mean_abs = pivot_lz.abs().mean(axis=1)
sort_order = mean_abs.sort_values(ascending=True).index
pivot_lz = pivot_lz.loc[sort_order]
pivot_flag = pivot_flag.loc[sort_order]

mat = pivot_lz.values
flag_mat = pivot_flag.values
short_names = [MODEL_SHORT.get(m, m) for m in pivot_lz.index]

# ── Layout (no dendrogram) ──
fig, (ax_heat, ax_cbar) = plt.subplots(
    2, 1, figsize=(4.0, 4.2),
    gridspec_kw={'height_ratios': [1, 0.04], 'hspace': 0.25})

# ── Heatmap ──
vlim = 40
norm = mcolors.TwoSlopeNorm(vmin=-vlim, vcenter=0, vmax=vlim)
cmap = plt.cm.RdBu_r

im = ax_heat.imshow(mat, cmap=cmap, norm=norm, aspect='auto')

n_rows, n_cols = mat.shape
for i in range(n_rows):
    for j in range(n_cols):
        val = mat[i, j]
        is_flagged = flag_mat[i, j]
        ival = int(round(val))

        r, g, b, _ = cmap(norm(val))
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        txt_color = 'white' if lum < 0.45 else palette.TEXT

        ax_heat.text(j, i, str(ival), ha='center', va='center',
                     fontsize=7.5, color=txt_color, fontweight='medium')

        if not is_flagged:
            rect = mpatches.Rectangle(
                (j - 0.5, i - 0.5), 1, 1,
                linewidth=0, fill=False,
                hatch='///', edgecolor=palette.ANNOTATION, alpha=0.4)
            ax_heat.add_patch(rect)

# ── Axes ──
ax_heat.set_xticks(range(n_cols))
ax_heat.set_xticklabels(BENCH_LABELS, fontsize=7.5)
ax_heat.xaxis.set_ticks_position('top')
ax_heat.xaxis.set_label_position('top')

ax_heat.set_yticks(range(n_rows))
ax_heat.set_yticklabels(short_names, fontsize=7)
ax_heat.yaxis.set_ticks_position('right')
ax_heat.yaxis.set_label_position('right')
ax_heat.tick_params(axis='y', length=0, pad=4)
ax_heat.tick_params(axis='x', length=2, pad=2)

for spine in ax_heat.spines.values():
    spine.set_visible(False)

# ── Colorbar ──
cbar = fig.colorbar(im, cax=ax_cbar, orientation='horizontal', extend='both')
cbar.set_label(r'$\ell_z^*$', fontsize=9)
cbar.ax.tick_params(labelsize=7)
cbar.outline.set_linewidth(0.3)

# ── Legend ──
ns_patch = mpatches.Patch(facecolor='white', edgecolor=palette.ANNOTATION,
                           hatch='///', alpha=0.4, label='n.s. (BH-FDR)')
ax_heat.legend(handles=[ns_patch], loc='lower left',
               bbox_to_anchor=(0.0, -0.08), frameon=False, fontsize=7)

# ── Save ──
fig.tight_layout()
plt.savefig(OUT_PDF, bbox_inches='tight')
plt.savefig(OUT_PNG, bbox_inches='tight', dpi=300)

import shutil
shutil.copy2(OUT_PDF, f'{BASE}/paper/paper/fig_4_model_heatmap.pdf')
plt.close()
print(f'Saved: {OUT_PDF}')
print(f'Saved: {OUT_PNG}')
