import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 8.5,
    'axes.titlesize': 9.5,
    'axes.labelsize': 8.5,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.4,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# === Left panel data: Exec-only ISR comparison ===
seeds = ['s42', 's43', 's44']
fol_isr = [0.132, 0.0, 0.582]
fol_pr = [0.93, 0.14, 0.98]
prolog_isr = [0.037, 0.015, 0.387]
prolog_pr = [0.83, 0.56, 0.21]

fol_color = '#0072B2'
prolog_color = '#D55E00'

# === Right panel data: Prolog STA gaming mode breakdown ===
# s42: H7 conclusion duplication, PR=0.50, 50/50 proved all H7
# s43: Degenerate syntax (functional H7), PR=0.38, 38/38 proved all gaming
# s44: Query-as-fact gaming (functional H7), PR=0.97, 95/97 functional H7, 2/97 other gaming
sta_seeds = ['s42', 's43', 's44']
sta_pr = [0.50, 0.38, 0.97]
sta_h7_pct = [100.0, 0.0, 0.0]
sta_degen_syntax_pct = [0.0, 100.0, 0.0]
sta_query_as_fact_pct = [0.0, 0.0, 97.9]
sta_other_gaming_pct = [0.0, 0.0, 2.1]
sta_genuine_pct = [0.0, 0.0, 0.0]

COLOR_H7 = '#CC79A7'
COLOR_DEGEN = '#E69F00'
COLOR_QAF = '#56B4E9'
COLOR_OTHER = '#999999'
COLOR_GENUINE = '#009E73'

fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(6.75, 2.8),
                                         gridspec_kw={'width_ratios': [1, 1.1]})

# ========== LEFT PANEL: Exec-only ISR ==========
x = np.arange(len(seeds))
width = 0.32

bars_fol = ax_left.bar(x - width/2, fol_isr, width, label='FOL (Prover9)',
                        color=fol_color, edgecolor='white', linewidth=0.5)
bars_prolog = ax_left.bar(x + width/2, prolog_isr, width, label='Prolog (SWI-Prolog)',
                           color=prolog_color, edgecolor='white', linewidth=0.5)

for bar, pr in zip(bars_fol, fol_pr):
    ax_left.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.015,
                 f'PR={pr:.2f}', ha='center', va='bottom', fontsize=6.5, color=fol_color)

for bar, pr in zip(bars_prolog, prolog_pr):
    ax_left.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.015,
                 f'PR={pr:.2f}', ha='center', va='bottom', fontsize=6.5, color=prolog_color)

ax_left.annotate('†taut.', xy=(2 - width/2, 0.582), xytext=(1.35, 0.66),
                 fontsize=6.5, fontstyle='italic', color='#555555',
                 arrowprops=dict(arrowstyle='->', color='#999999', lw=0.7))

fol_mean = np.mean(fol_isr)
fol_mean_excl = np.mean([0.132, 0.0])
prolog_mean = np.mean(prolog_isr)

ax_left.axhline(fol_mean, color=fol_color, linestyle='--', linewidth=0.9, alpha=0.5)
ax_left.axhline(prolog_mean, color=prolog_color, linestyle='--', linewidth=0.9, alpha=0.5)

ax_left.set_xlabel('Seed')
ax_left.set_ylabel('Proved-only ISR')
ax_left.set_title('(a) Exec-Only: Cross-Logic ISR', fontweight='bold')
ax_left.set_xticks(x)
ax_left.set_xticklabels(seeds)
ax_left.set_ylim(0, 0.78)
ax_left.legend(loc='upper left', frameon=True, edgecolor='#CCCCCC',
               fontsize=7, handlelength=1.2, borderpad=0.3)

# ========== RIGHT PANEL: Prolog STA Gaming Breakdown ==========
x2 = np.arange(len(sta_seeds))
bar_width = 0.5

bottom = np.zeros(3)

bars_h7 = ax_right.bar(x2, sta_h7_pct, bar_width, bottom=bottom,
                        label='H7: Conclusion duplication', color=COLOR_H7,
                        edgecolor='white', linewidth=0.5)
bottom += sta_h7_pct

bars_degen = ax_right.bar(x2, sta_degen_syntax_pct, bar_width, bottom=bottom,
                           label='Degenerate syntax (func. H7)', color=COLOR_DEGEN,
                           edgecolor='white', linewidth=0.5)
bottom += sta_degen_syntax_pct

bars_qaf = ax_right.bar(x2, sta_query_as_fact_pct, bar_width, bottom=bottom,
                         label='Query-as-fact (func. H7)', color=COLOR_QAF,
                         edgecolor='white', linewidth=0.5)
bottom += sta_query_as_fact_pct

bars_other = ax_right.bar(x2, sta_other_gaming_pct, bar_width, bottom=bottom,
                           label='Other gaming', color=COLOR_OTHER,
                           edgecolor='white', linewidth=0.5)
bottom += sta_other_gaming_pct

bars_genuine = ax_right.bar(x2, sta_genuine_pct, bar_width, bottom=bottom,
                             label='Genuine', color=COLOR_GENUINE,
                             edgecolor='white', linewidth=0.5)

# PR labels above bars
for i, (s, pr) in enumerate(zip(sta_seeds, sta_pr)):
    ax_right.text(i, 103, f'PR={pr:.2f}', ha='center', va='bottom',
                  fontsize=7, fontweight='bold', color='#333333')

# Gaming mode labels inside bars
for i in range(3):
    if sta_h7_pct[i] > 10:
        ax_right.text(i, sta_h7_pct[i]/2, f'{sta_h7_pct[i]:.0f}%',
                      ha='center', va='center', fontsize=7.5, color='white', fontweight='bold')
    if sta_degen_syntax_pct[i] > 10:
        y_pos = sta_h7_pct[i] + sta_degen_syntax_pct[i]/2
        ax_right.text(i, y_pos, f'{sta_degen_syntax_pct[i]:.0f}%',
                      ha='center', va='center', fontsize=7.5, color='white', fontweight='bold')
    if sta_query_as_fact_pct[i] > 10:
        y_pos = sta_h7_pct[i] + sta_degen_syntax_pct[i] + sta_query_as_fact_pct[i]/2
        ax_right.text(i, y_pos, f'{sta_query_as_fact_pct[i]:.1f}%',
                      ha='center', va='center', fontsize=7.5, color='white', fontweight='bold')

# 0% Genuine annotation — place to the right of bars
bbox_props = dict(boxstyle='round,pad=0.3', facecolor='#FFF3E0', edgecolor='#D55E00',
                  alpha=0.95, linewidth=0.9)
ax_right.annotate('3/3 seeds gaming\n0% genuine',
                  xy=(2.5, 50), xytext=(2.5, 50),
                  fontsize=7, fontweight='bold', color='#D55E00',
                  ha='center', va='center', bbox=bbox_props,
                  annotation_clip=False)

ax_right.set_xlabel('Seed')
ax_right.set_ylabel('Proved Samples (%)')
ax_right.set_title('(b) Prolog STA: Universal Goodhart', fontweight='bold')
ax_right.set_xticks(x2)
ax_right.set_xticklabels(sta_seeds)
ax_right.set_xlim(-0.5, 3.3)
ax_right.set_ylim(0, 120)
ax_right.set_yticks([0, 25, 50, 75, 100])
ax_right.set_yticklabels(['0%', '25%', '50%', '75%', '100%'])
ax_right.legend(loc='upper left', frameon=True, edgecolor='#CCCCCC',
                fontsize=6.5, handlelength=1.2, borderpad=0.3,
                bbox_to_anchor=(0.0, 0.98))

ax_right.axhline(100, color='#CCCCCC', linestyle='-', linewidth=0.5, zorder=0)

plt.tight_layout(w_pad=2)

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/figures/paper'
canonical = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/figures'
fig.savefig(f'{outdir}/fig4_prolog_comparison.pdf', format='pdf')
fig.savefig(f'{outdir}/fig4_prolog_comparison.png', format='png')
fig.savefig(f'{canonical}/fig4_prolog_comparison.pdf', format='pdf')
fig.savefig(f'{canonical}/fig4_prolog_comparison.png', format='png')
plt.close(fig)
print(f'Saved: {outdir}/fig4_prolog_comparison.pdf')
print(f'Saved: {outdir}/fig4_prolog_comparison.png')
