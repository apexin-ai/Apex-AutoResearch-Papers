#!/usr/bin/env python3
"""Fig: Selection gap bar chart for exp_016_rerun_1024 (N=1024)."""
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

FIG_DIR = Path('/root/autodl-tmp/struct_self_consist_ie/artifacts/figures')
FIG_DIR.mkdir(parents=True, exist_ok=True)

# --- Data from exp_016_rerun_1024 ---
# Selection F1 values
ner_data = {
    'greedy': 0.6439, 'random': 0.6077, 'oracle': 0.7758,
    'SJ': 0.6450, 'voting_conf': 0.6337, 'logprob': 0.6501,
}
re_data = {
    'greedy': 0.4042, 'random': 0.3544, 'oracle': 0.5850,
    'SJ': 0.3855, 'voting_conf': 0.3592, 'logprob': 0.3948,
}

# Spearman rho (signal vs mean_sample_f1) from exp_016_rerun_1024/correlation_matrix.json
ner_rho = {'SJ': 0.3599, 'voting_conf': 0.2524, 'logprob': 0.2052}
re_rho = {'SJ': 0.2503, 'voting_conf': 0.3311, 'logprob': 0.2662}

signals = ['SJ', 'voting_conf', 'logprob']
signal_labels = ['SJ', 'VotConf', 'LogProb']

fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.8), gridspec_kw={'wspace': 0.45})

for panel_idx, (task_label, rho_dict, sel_dict, greedy_val, oracle_val) in enumerate([
    ('NER (SciERC, N=1024)', ner_rho, ner_data, ner_data['greedy'], ner_data['oracle']),
    ('RE (SciERC, N=1024)', re_rho, re_data, re_data['greedy'], re_data['oracle']),
]):
    ax = axes[panel_idx]
    ax2 = ax.twinx()

    x = np.arange(len(signals))
    width = 0.45

    rho_vals = [rho_dict[s] for s in signals]
    delta_f1 = [(sel_dict[s] - greedy_val) * 100 for s in signals]

    bars = ax.bar(x, rho_vals, width, color='#4c72b0', alpha=0.75,
                  edgecolor='#3b5998', linewidth=0.5, label='Spearman ρ', zorder=2)

    line = ax2.plot(x, delta_f1, 'D-', color='#c44e52', markersize=5,
                    linewidth=1.5, label='ΔF1 vs greedy', zorder=3)
    ax2.axhline(y=0, color='gray', linestyle='--', linewidth=0.5, alpha=0.5, zorder=1)

    oracle_delta = (oracle_val - greedy_val) * 100
    ax2.annotate(f'oracle: +{oracle_delta:.1f}pp', xy=(0.98, 0.95), xycoords='axes fraction',
                fontsize=6.5, color='#2ca02c', ha='right', va='top',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#e6ffe6', edgecolor='#2ca02c', alpha=0.7))

    random_delta = (sel_dict['random'] - greedy_val) * 100
    ax2.annotate(f'random: {random_delta:.1f}pp', xy=(0.98, 0.05), xycoords='axes fraction',
                fontsize=6.5, color='gray', ha='right', va='bottom',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f0f0', edgecolor='gray', alpha=0.7))

    ax.set_xlabel('')
    ax.set_ylabel('Spearman ρ', color='#4c72b0', fontsize=8)
    ax2.set_ylabel('ΔF1 vs greedy (pp)', color='#c44e52', fontsize=8)
    ax.set_xticks(x)
    ax.set_xticklabels(signal_labels, fontsize=7.5)
    ax.set_ylim(0, 0.45)
    delta_max = max(abs(d) for d in delta_f1) + 2.0
    ax2.set_ylim(-delta_max, delta_max)
    ax.set_title(task_label, fontsize=9, fontweight='bold', pad=4)
    ax.tick_params(axis='y', colors='#4c72b0', labelsize=7)
    ax2.tick_params(axis='y', colors='#c44e52', labelsize=7)

    for xi, d in zip(x, delta_f1):
        offset_y = 7 if d >= 0 else -12
        ax2.annotate(f'{d:+.1f}', xy=(xi, d), xytext=(0, offset_y), textcoords='offset points',
                    ha='center', fontsize=6.5, color='#c44e52', fontweight='bold')

    if panel_idx == 0:
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=6.5, framealpha=0.85)

fig.savefig(FIG_DIR / 'fig_selection_gap_1024.pdf', format='pdf')
fig.savefig(FIG_DIR / 'fig_selection_gap_1024.png', format='png', dpi=150)
plt.close(fig)
print(f"Saved: {FIG_DIR / 'fig_selection_gap_1024.pdf'}")
print(f"Saved: {FIG_DIR / 'fig_selection_gap_1024.png'}")
