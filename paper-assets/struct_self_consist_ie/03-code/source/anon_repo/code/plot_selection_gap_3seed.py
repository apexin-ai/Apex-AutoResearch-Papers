#!/usr/bin/env python3
"""Fig: Selection gap bar chart — 3-seed n=551 data."""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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

OUT = Path('/root/autodl-tmp/struct_self_consist_ie/output')
FIG_DIR = OUT / 'figures'
FIG_DIR.mkdir(parents=True, exist_ok=True)

with open(OUT / 'analysis_scierc_n16_3seed_selection_f1_merged.json') as f:
    merged = json.load(f)

ner_agg = merged['qwen_scierc_ner_n16']['aggregated']
re_agg = merged['qwen_scierc_re_n16']['aggregated']

signals = ['VC', 'SJ', 'FK', 'EM', 'LP']
signal_labels = ['VC', 'SJ', 'FK', 'EM', 'LP']

# Extract delta and std
ner_delta = []
ner_std = []
re_delta = []
re_std = []

for sig in signals:
    nd = ner_agg['signal_selection_f1'][sig]['delta_vs_greedy_mean']
    ns = ner_agg['signal_selection_f1'][sig]['delta_vs_greedy_std']
    ner_delta.append(nd * 100)  # to pp
    ner_std.append(ns * 100)

    rd = re_agg['signal_selection_f1'][sig]['delta_vs_greedy_mean']
    rs = re_agg['signal_selection_f1'][sig]['delta_vs_greedy_std']
    re_delta.append(rd * 100)
    re_std.append(rs * 100)

ner_delta = np.array(ner_delta)
ner_std = np.array(ner_std)
re_delta = np.array(re_delta)
re_std = np.array(re_std)

# Colors: consistency signals (VC/SJ/FK/EM) blue family, LP orange/red
colors_ner = ['#4c72b0'] * 4 + ['#dd8452']
colors_re = ['#6c92d0'] * 4 + ['#e8a878']

fig, ax = plt.subplots(figsize=(5.5, 3.0))

x = np.arange(len(signals))
width = 0.35

bars_ner = ax.bar(x - width/2, ner_delta, width,
                  yerr=ner_std, capsize=2.5, error_kw={'linewidth': 0.8},
                  color=[c for c in colors_ner], alpha=0.85,
                  edgecolor='white', linewidth=0.5, label='NER', zorder=2)
bars_re = ax.bar(x + width/2, re_delta, width,
                 yerr=re_std, capsize=2.5, error_kw={'linewidth': 0.8},
                 color=[c for c in colors_re], alpha=0.85,
                 edgecolor='white', linewidth=0.5, label='RE', zorder=2)

ax.axhline(y=0, color='black', linewidth=0.6, zorder=1)

# Value annotations
for i, (nd, rd) in enumerate(zip(ner_delta, re_delta)):
    y_ner = nd + (ner_std[i] + 0.15) * (1 if nd >= 0 else -1)
    y_re = rd + (re_std[i] + 0.15) * (1 if rd >= 0 else -1)
    va_ner = 'bottom' if nd >= 0 else 'top'
    va_re = 'bottom' if rd >= 0 else 'top'
    ax.text(i - width/2, y_ner, f'{nd:+.2f}', ha='center', va=va_ner,
            fontsize=6, fontweight='bold', color='#333333')
    ax.text(i + width/2, y_re, f'{rd:+.2f}', ha='center', va=va_re,
            fontsize=6, fontweight='bold', color='#333333')

# Oracle/random annotations
ner_oracle_delta = (ner_agg['oracle_f1']['mean'] - ner_agg['greedy_f1']['mean']) * 100
re_oracle_delta = (re_agg['oracle_f1']['mean'] - re_agg['greedy_f1']['mean']) * 100
ner_random_delta = (ner_agg['random_f1']['mean'] - ner_agg['greedy_f1']['mean']) * 100
re_random_delta = (re_agg['random_f1']['mean'] - re_agg['greedy_f1']['mean']) * 100

ax.annotate(f'oracle: NER +{ner_oracle_delta:.1f} / RE +{re_oracle_delta:.1f} pp',
            xy=(0.98, 0.97), xycoords='axes fraction', fontsize=6, color='#2ca02c',
            ha='right', va='top',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#e6ffe6', edgecolor='#2ca02c', alpha=0.7))
ax.annotate(f'random: NER {ner_random_delta:.1f} / RE {re_random_delta:.1f} pp',
            xy=(0.98, 0.03), xycoords='axes fraction', fontsize=6, color='gray',
            ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f0f0', edgecolor='gray', alpha=0.7))

ax.set_xticks(x)
ax.set_xticklabels(signal_labels)
ax.set_ylabel('ΔF1 vs Greedy (pp)')
ax.set_title('Selection Gap: Signal vs Greedy (SciERC, n=551, 3 seeds)', fontsize=9, fontweight='bold')
ax.legend(loc='upper left', fontsize=7, framealpha=0.85)

y_max = max(abs(ner_delta).max() + ner_std.max(), abs(re_delta).max() + re_std.max()) + 1.5
ax.set_ylim(-y_max, y_max)
ax.tick_params(labelsize=7)
ax.grid(axis='y', alpha=0.2, linewidth=0.3)

fig.savefig(FIG_DIR / 'fig_selection_gap.pdf', format='pdf')
fig.savefig(FIG_DIR / 'fig_selection_gap.png', format='png', dpi=300)
plt.close(fig)

# Print values for verification
print("=== NER Selection Gap (pp) ===")
print(f"  greedy F1: {ner_agg['greedy_f1']['mean']:.5f}")
for i, sig in enumerate(signals):
    print(f"  {sig}: Δ={ner_delta[i]:+.2f} ± {ner_std[i]:.2f}")
print(f"  oracle delta: +{ner_oracle_delta:.2f} pp")
print(f"  random delta: {ner_random_delta:.2f} pp")

print("\n=== RE Selection Gap (pp) ===")
print(f"  greedy F1: {re_agg['greedy_f1']['mean']:.5f}")
for i, sig in enumerate(signals):
    print(f"  {sig}: Δ={re_delta[i]:+.2f} ± {re_std[i]:.2f}")
print(f"  oracle delta: +{re_oracle_delta:.2f} pp")
print(f"  random delta: {re_random_delta:.2f} pp")

print(f"\nSaved: {FIG_DIR / 'fig_selection_gap.pdf'}")
print(f"Saved: {FIG_DIR / 'fig_selection_gap.png'}")
