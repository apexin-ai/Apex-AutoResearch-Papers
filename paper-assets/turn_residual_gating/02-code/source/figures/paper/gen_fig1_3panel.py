"""Figure 1: 3-panel headline figure — Discovery → Diagnosis → Fix.

(a) Per-turn GAR decay under AR generation (both models)
(b) TF vs AR GAR gap across 5 training configs
(c) SS gap compression (before/after)
"""
import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')
from palette import *
import matplotlib.patheffects as pe
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec
import numpy as np

apply_style()

fig = plt.figure(figsize=(7.2, 2.5))
gs = gridspec.GridSpec(2, 2, figure=fig, width_ratios=[1.0, 1.15],
                       height_ratios=[1.0, 0.85], hspace=0.65, wspace=0.40)

ax_a = fig.add_subplot(gs[:, 0])
ax_b = fig.add_subplot(gs[0, 1])
ax_c = fig.add_subplot(gs[1, 1])

stroke = [pe.withStroke(linewidth=2.2, foreground='white')]

# ══════════════════════════════════════════════════════════════════
# Panel (a): Per-turn GAR decay under AR generation
# ══════════════════════════════════════════════════════════════════
turns = np.arange(1, 11)

qwen_base = np.array([0.0418, 0.0241, 0.0224, 0.013, 0.0133,
                       0.0086, 0.0078, 0.008, 0.0157, 0.0064])
llama_base = np.array([0.0263, 0.0183, 0.0087, 0.0055, 0.006,
                        0.0035, 0.0038, 0.0037, 0.005, 0.0026])

ax_a.plot(turns, qwen_base * 100, 'o-', color=C_TG, markersize=3.5,
          markeredgecolor='white', markeredgewidth=0.4,
          label='Qwen-2.5-7B', zorder=3, linewidth=1.2)
ax_a.plot(turns, llama_base * 100, 's-', color=C_GREEN, markersize=3.5,
          markeredgecolor='white', markeredgewidth=0.4,
          label='Llama-3.1-8B', zorder=3, linewidth=1.2)

ax_a.fill_between(turns, 0, qwen_base * 100, alpha=0.06, color=C_TG)
ax_a.fill_between(turns, 0, llama_base * 100, alpha=0.06, color=C_GREEN)

t = ax_a.text(7.5, 3.5, '85–90%\ndecay', fontsize=6, color='#666666',
              ha='center', va='center', fontstyle='italic')
t.set_path_effects(stroke)

ax_a.set_xlabel('Turn index')
ax_a.set_ylabel('GAR (%)')
ax_a.set_xticks([1, 3, 5, 7, 9])
ax_a.set_xlim(0.5, 10.5)
ax_a.set_ylim(0, 5.0)
ax_a.legend(loc='upper right', fontsize=6, handlelength=1.2,
            handletextpad=0.3, borderpad=0.2)
ax_a.set_title('(a) GAR decays with turn depth',
               fontsize=8, pad=6, loc='left', fontweight='medium')

# ══════════════════════════════════════════════════════════════════
# Panel (b): TF vs AR GAR gap — 5 configs
# ══════════════════════════════════════════════════════════════════
configs = ['Base', 'TG', '+PCGrad', 'UG', 'LoRA']
config_colors = [C_BASE, C_TG, C_PC, C_UG, C_LO]
tf_gar  = [0.01, 0.50, 0.50, 0.49, 0.50]
ar_gar  = [0.019, 0.064, 0.030, 0.033, 0.037]
gaps    = [None, 7.8, 16.7, 14.8, 13.5]

x = np.arange(len(configs))
w = 0.28

bars_tf = ax_b.bar(x - w/2, tf_gar, w, color=C_TF, label='Teacher-forced',
                   zorder=2, edgecolor='white', linewidth=0.3)
bars_ar = ax_b.bar(x + w/2, ar_gar, w, color=C_SS, label='Autoregressive',
                   zorder=2, edgecolor='white', linewidth=0.3)

ax_b.set_yscale('log')
ax_b.set_ylim(0.004, 1.5)
ax_b.set_xlim(-0.55, 4.65)

ax_b.axhspan(0.005, 0.05, color='#FFF3E0', alpha=0.12, zorder=0)
ax_b.axhspan(0.05, 1.5, color='#E8F5E9', alpha=0.12, zorder=0)

for i in range(1, len(configs)):
    ax_b.plot([x[i] - w/2, x[i] + w/2], [tf_gar[i], ar_gar[i]],
              color='#CCCCCC', linewidth=0.5, zorder=3, linestyle=(0, (3, 2)))

for i, gap in enumerate(gaps):
    if gap is not None:
        geo_mean = np.sqrt(tf_gar[i] * ar_gar[i])
        t = ax_b.text(x[i] + w/2 + 0.12, geo_mean, f'{gap:.0f}×',
                      fontsize=7, fontweight='bold', color=C_AR_DARK,
                      ha='left', va='center')
        t.set_path_effects(stroke)

ax_b.set_xticks(x)
ax_b.set_xticklabels(configs, fontsize=7)
ax_b.set_ylabel('GAR (log scale)')
ax_b.legend(loc='upper center', fontsize=5.5, handlelength=0.8,
            handletextpad=0.3, borderpad=0.15, ncol=2,
            bbox_to_anchor=(0.42, 1.12), columnspacing=0.8)
ax_b.yaxis.set_minor_locator(ticker.LogLocator(base=10, subs=np.arange(2, 10)))
ax_b.set_title('(b) 8–17× TF/AR gap persists',
               fontsize=8, pad=6, loc='left', fontweight='medium')

# ══════════════════════════════════════════════════════════════════
# Panel (c): SS gap compression — before/after
# ══════════════════════════════════════════════════════════════════
labels_c = ['Qwen TG', 'Qwen SS', 'Llama TG', 'Llama SS']
gaps_c   = [7.8, 1.3, 12.5, 2.9]
colors_c = [C_TEAL, C_GOLD, C_TEAL, C_GOLD]
alphas_c = [0.55, 1.0, 0.55, 1.0]

y = np.arange(len(labels_c))

for i, (lbl, gap, col) in enumerate(zip(labels_c, gaps_c, colors_c)):
    ax_c.barh(i, gap, height=0.55, color=col, alpha=alphas_c[i],
              edgecolor='white', linewidth=0.3, zorder=2)
    is_ss = 'SS' in lbl
    txt_offset = 0.25
    ax_c.text(gap + txt_offset, i, f'{gap:.1f}×', va='center', ha='left',
              fontsize=6.5, fontweight='bold' if is_ss else 'normal',
              color=col if is_ss else '#777777',
              path_effects=stroke if is_ss else [], zorder=5)

ax_c.axvline(1.0, color=C_GRAY, linestyle='--', linewidth=0.6, zorder=1, alpha=0.5)

ax_c.axhline(1.5, color='#DDDDDD', linewidth=0.4, linestyle='-', zorder=0)

# Compression arrows — straight vertical at midpoint of SS bar
for pair_start, pair_end in [(0, 1), (2, 3)]:
    arrow_x = gaps_c[pair_end] * 0.45
    ax_c.annotate('',
                  xy=(arrow_x, pair_end + 0.3),
                  xytext=(arrow_x, pair_start - 0.3),
                  arrowprops=dict(arrowstyle='-|>', color='#888888',
                                  lw=1.0, mutation_scale=6,
                                  shrinkA=0, shrinkB=0),
                  zorder=3)

ax_c.set_yticks(y)
ax_c.set_yticklabels(labels_c, fontsize=6.5)
ax_c.set_xlabel('TF/AR gap ratio')
ax_c.set_xlim(0, 14.5)
ax_c.invert_yaxis()
ax_c.set_title('(c) SS compresses the gap',
               fontsize=8, pad=6, loc='left', fontweight='medium')

save_fig(fig, 'fig1_headline')
