import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'pdf.fonttype': 42, 'ps.fonttype': 42,
    'font.family': 'DejaVu Sans', 'font.size': 8,
    'axes.labelsize': 8, 'axes.titlesize': 9,
    'xtick.labelsize': 8, 'ytick.labelsize': 8,
    'axes.spines.top': False, 'axes.spines.right': False,
    'savefig.dpi': 300, 'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# Okabe-Ito palette (consistent with fig2, fig3)
C_FOL = '#0072B2'
C_PROLOG = '#56B4E9'
C_PROLOG_TEXT = '#2A7AB5'
C_TS = '#D55E00'
C_DEGEN = '#E69F00'
C_QUERY = '#CC79A7'

seeds = ['s42', 's43', 's44']
x = np.arange(len(seeds))
bar_w = 0.28

# Panel (a) data
fol_isr = [0.132, 0.000, 0.582]
prolog_isr = [0.037, 0.015, 0.387]
fol_pr = [93, 13, 98]
prolog_pr = [83, 56, 21]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(3.25, 4.0),
                                gridspec_kw={'hspace': 0.48})
stroke = [pe.withStroke(linewidth=2.5, foreground='white')]

# ── Panel (a): Exec-only ISR* ──
b1 = ax1.bar(x - bar_w/2, fol_isr, bar_w, color=C_FOL, label='FOL',
             edgecolor='white', linewidth=0.4, zorder=3)
b2 = ax1.bar(x + bar_w/2, prolog_isr, bar_w, color=C_PROLOG, label='Prolog',
             edgecolor='white', linewidth=0.4, zorder=3)

ax1.yaxis.grid(True, alpha=0.12, linewidth=0.4, zorder=0)

# PR annotations with per-seed vertical offsets
pr_y_fol =    [0.018, 0.075, 0.018]
pr_y_prolog = [0.018, 0.018, 0.018]

for i, (bar, pr) in enumerate(zip(b1, fol_pr)):
    label = f'PR={pr}%' + ('†' if i == 1 else '')
    bx = bar.get_x() + bar.get_width() / 2
    by = max(bar.get_height(), 0.005) + pr_y_fol[i]
    t = ax1.text(bx, by, label, ha='center', va='bottom',
                 fontsize=6.5, color=C_FOL)
    t.set_path_effects(stroke)

for i, (bar, pr) in enumerate(zip(b2, prolog_pr)):
    label = f'PR={pr}%'
    if i == 2:
        label += '\n($n$=21)'
    bx = bar.get_x() + bar.get_width() / 2
    by = bar.get_height() + pr_y_prolog[i]
    t = ax1.text(bx, by, label, ha='center', va='bottom',
                 fontsize=6.5, color=C_PROLOG_TEXT)
    t.set_path_effects(stroke)

ax1.set_xticks(x)
ax1.set_xticklabels(seeds)
ax1.set_ylabel('ISR* (exec-only)')
ax1.set_ylim(0, 0.75)
ax1.set_yticks(np.arange(0, 0.8, 0.1))
ax1.legend(fontsize=7, loc='upper left', frameon=False)
ax1.set_title('(a) Exec-only ISR*: FOL vs Prolog', fontsize=8.5,
              loc='left', pad=4)

# ── Panel (b): Prolog Gaming Modes ──
bw2 = 0.45
mode_colors = [C_TS, C_DEGEN, C_QUERY]
mode_labels_short = ['TS\ntautol.', 'Degen.\nsyntax', 'Query\nas-fact']
text_colors = ['white', '#333333', 'white']

for i in range(3):
    ax2.bar(x[i], 100, bw2, color=mode_colors[i], edgecolor='white',
            linewidth=0.4, zorder=3)
    ax2.text(x[i], 50, mode_labels_short[i], ha='center', va='center',
             fontsize=7, color=text_colors[i])

ax2.yaxis.grid(True, alpha=0.12, linewidth=0.4, zorder=0)

ax2.set_xticks(x)
ax2.set_xticklabels(seeds)
ax2.set_ylabel('Percentage (%)')
ax2.set_ylim(0, 110)
ax2.set_yticks([0, 25, 50, 75, 100])
ax2.set_title('(b) Prolog gaming modes', fontsize=8.5,
              loc='left', pad=4)

ax2.text(1.0, 105, '3/3 seeds gaming, 0% genuine',
         ha='center', fontsize=7, fontstyle='italic', color='#888888')

# ── Save ──
out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/figures/fig4_prolog_comparison'
fig.savefig(f'{out_base}.pdf', dpi=300, bbox_inches='tight', pad_inches=0.05)
fig.savefig(f'{out_base}.png', dpi=300, bbox_inches='tight', pad_inches=0.05)
plt.close()
print(f'Saved: {out_base}.pdf and .png')
