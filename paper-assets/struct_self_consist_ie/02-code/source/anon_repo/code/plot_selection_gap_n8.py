#!/usr/bin/env python3
"""Fig: Selection gap bar chart — N=8 NER, 3-seed, Director-confirmed deltas."""
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

FIG_DIR = Path('/root/autodl-tmp/struct_self_consist_ie/output/figures')
FIG_DIR.mkdir(parents=True, exist_ok=True)

# --- Director-confirmed NER N=8 delta (pp, vs greedy, 3-seed) ---
signals = ['VC', 'SJ', 'FK', 'EM', 'LP']
ner_delta = np.array([-2.540, -0.433, -0.438, -1.145, +0.038])

# Std from analysis_multiseed_selection_f1.json (qwen_scierc_ner_n8, delta_vs_greedy_std * 100)
ner_std = np.array([0.842, 0.985, 0.927, 0.705, 0.480])

# Oracle/random from same JSON
greedy_mean = 0.64583
oracle_mean = 0.77637
random_mean = 0.60688
oracle_delta = (oracle_mean - greedy_mean) * 100  # +13.05 pp
random_delta = (random_mean - greedy_mean) * 100  # -3.90 pp

# Colors: structural signals blue, LP orange
colors = ['#4c72b0'] * 4 + ['#dd8452']

fig, ax = plt.subplots(figsize=(4.5, 2.8))

x = np.arange(len(signals))
width = 0.55

bars = ax.bar(x, ner_delta, width,
              yerr=ner_std, capsize=3, error_kw={'linewidth': 0.8},
              color=colors, alpha=0.85,
              edgecolor='white', linewidth=0.5, zorder=2)

ax.axhline(y=0, color='black', linewidth=0.6, zorder=1)

# Value labels
for i, (d, s) in enumerate(zip(ner_delta, ner_std)):
    y = d + (s + 0.15) * (1 if d >= 0 else -1)
    va = 'bottom' if d >= 0 else 'top'
    ax.text(i, y, f'{d:+.2f}', ha='center', va=va,
            fontsize=7, fontweight='bold', color='#333333')

# Oracle/random annotations
ax.annotate(f'oracle: +{oracle_delta:.1f} pp',
            xy=(0.98, 0.97), xycoords='axes fraction', fontsize=6.5, color='#2ca02c',
            ha='right', va='top',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#e6ffe6', edgecolor='#2ca02c', alpha=0.7))
ax.annotate(f'random: {random_delta:.1f} pp',
            xy=(0.98, 0.03), xycoords='axes fraction', fontsize=6.5, color='gray',
            ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f0f0', edgecolor='gray', alpha=0.7))

ax.set_xticks(x)
ax.set_xticklabels(signals)
ax.set_ylabel(r'$\Delta$F1 vs Greedy (pp)')
ax.set_title('Selection Gap: Signal vs Greedy (SciERC NER, N=8, 3 seeds)',
             fontsize=8.5, fontweight='bold')

y_max = max(abs(ner_delta).max() + ner_std.max(), 2.0) + 1.5
ax.set_ylim(-y_max, y_max)
ax.tick_params(labelsize=7)
ax.grid(axis='y', alpha=0.2, linewidth=0.3)

fig.savefig(FIG_DIR / 'fig_selection_gap.pdf', format='pdf')
fig.savefig(FIG_DIR / 'fig_selection_gap.png', format='png', dpi=300)
plt.close(fig)

# Verification
print("=== NER N=8 Selection Gap (pp) — Director-confirmed ===")
print(f"  greedy F1: {greedy_mean:.5f}")
for i, sig in enumerate(signals):
    print(f"  {sig}: Δ={ner_delta[i]:+.3f} ± {ner_std[i]:.3f}")
print(f"  oracle delta: +{oracle_delta:.2f} pp")
print(f"  random delta: {random_delta:.2f} pp")
print(f"\nSaved: {FIG_DIR / 'fig_selection_gap.pdf'}")
print(f"Saved: {FIG_DIR / 'fig_selection_gap.png'}")
