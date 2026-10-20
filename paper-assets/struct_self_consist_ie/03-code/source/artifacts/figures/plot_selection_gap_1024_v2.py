#!/usr/bin/env python3
"""fig_selection_gap_1024 with bootstrap CI error bars and n.s. annotations."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],
    'font.size': 9,
    'axes.labelsize': 9,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'text.usetex': False,
})

FIG_DIR = Path(__file__).parent

signal_labels = ['SJ', 'VotConf', 'LogProb']

# ── NER (SciERC, N=8, 1024 tokens) ──
ner_rho = [0.360, 0.379, 0.205]
ner_delta_f1 = [+0.1, -1.0, +0.6]
ner_greedy = 0.6439
ner_oracle = 0.7758
ner_random = 0.6077
# Bootstrap 95% CI — asymmetric errors (distance from center, pp)
ner_yerr_lo = [3.6, 3.7, 3.6]
ner_yerr_hi = [3.7, 3.6, 3.6]

# ── RE (SciERC, N=8, 1024 tokens) ──
re_rho = [0.249, 0.334, 0.266]
re_delta_f1 = [-1.9, -4.5, -0.9]
re_greedy = 0.4042
re_oracle = 0.5850
re_random = 0.3544

# ── Plot ──
fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.8), gridspec_kw={'wspace': 0.45})

panels = [
    dict(title='NER (SciERC, N=8)', rho=ner_rho, df1=ner_delta_f1,
         greedy=ner_greedy, oracle=ner_oracle, random=ner_random,
         yerr_lo=ner_yerr_lo, yerr_hi=ner_yerr_hi, has_ci=True),
    dict(title='RE (SciERC, N=8)', rho=re_rho, df1=re_delta_f1,
         greedy=re_greedy, oracle=re_oracle, random=re_random,
         yerr_lo=None, yerr_hi=None, has_ci=False),
]

for idx, p in enumerate(panels):
    ax = axes[idx]
    ax2 = ax.twinx()
    x = np.arange(len(signal_labels))
    width = 0.45

    ax.bar(x, p['rho'], width, color='#4c72b0', alpha=0.75,
           edgecolor='#3b5998', linewidth=0.5, label='Spearman ρ', zorder=2)

    if p['has_ci']:
        yerr = np.array([p['yerr_lo'], p['yerr_hi']])
        ax2.errorbar(x, p['df1'], yerr=yerr, fmt='D-', color='#c44e52',
                     markersize=5, linewidth=1.5, capsize=3, capthick=0.8,
                     label='ΔF1 vs greedy', zorder=3)
    else:
        ax2.plot(x, p['df1'], 'D-', color='#c44e52', markersize=5,
                 linewidth=1.5, label='ΔF1 vs greedy', zorder=3)

    ax2.axhline(y=0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5, zorder=1)

    # Oracle (top-right, green box)
    oracle_d = (p['oracle'] - p['greedy']) * 100
    ax2.annotate(f'oracle: +{oracle_d:.1f}pp', xy=(0.98, 0.95),
                 xycoords='axes fraction', fontsize=6.5, color='#2ca02c',
                 ha='right', va='top',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='#e6ffe6',
                           edgecolor='#2ca02c', alpha=0.7))

    # Random (bottom-right, red box)
    random_d = (p['random'] - p['greedy']) * 100
    ax2.annotate(f'random: {random_d:.1f}pp', xy=(0.98, 0.05),
                 xycoords='axes fraction', fontsize=6.5, color='#d62728',
                 ha='right', va='bottom',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffe6e6',
                           edgecolor='#d62728', alpha=0.7))

    # ΔF1 value labels with n.s.
    for i, (xi, d) in enumerate(zip(x, p['df1'])):
        label = f'{d:+.1f} n.s.'
        if p['has_ci']:
            if d >= 0:
                anchor_y = d + p['yerr_hi'][i]
                ax2.annotate(label, xy=(xi, anchor_y), xytext=(0, 5),
                             textcoords='offset points', ha='center', va='bottom',
                             fontsize=6.5, color='#c44e52', fontweight='bold')
            else:
                anchor_y = d - p['yerr_lo'][i]
                ax2.annotate(label, xy=(xi, anchor_y), xytext=(0, -5),
                             textcoords='offset points', ha='center', va='top',
                             fontsize=6.5, color='#c44e52', fontweight='bold')
        else:
            offset_y = 7 if d >= 0 else -12
            ax2.annotate(label, xy=(xi, d), xytext=(0, offset_y),
                         textcoords='offset points', ha='center',
                         fontsize=6.5, color='#c44e52', fontweight='bold')

    # Axis styling
    ax.set_ylabel('Spearman ρ', color='#4c72b0', fontsize=8)
    ax2.set_ylabel('ΔF1 vs greedy (pp)', color='#c44e52', fontsize=8)
    ax.set_xticks(x)
    ax.set_xticklabels(signal_labels, fontsize=7.5)
    ax.set_ylim(0, 0.45)

    if p['has_ci']:
        bounds = ([d + u for d, u in zip(p['df1'], p['yerr_hi'])] +
                  [d - l for d, l in zip(p['df1'], p['yerr_lo'])])
        y_ext = max(abs(b) for b in bounds) + 2.5
    else:
        y_ext = max(abs(d) for d in p['df1']) + 1.5
    ax2.set_ylim(-y_ext, y_ext)

    ax.set_title(p['title'], fontsize=9, fontweight='bold', pad=4)
    ax.tick_params(axis='y', colors='#4c72b0', labelsize=7)
    ax2.tick_params(axis='y', colors='#c44e52', labelsize=7)

    if idx == 0:
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left',
                  fontsize=6.5, framealpha=0.85)

fig.savefig(FIG_DIR / 'fig_selection_gap_1024.pdf', format='pdf')
fig.savefig(FIG_DIR / 'fig_selection_gap_1024.png', format='png')
plt.close(fig)
print('Done: fig_selection_gap_1024.pdf/png')
