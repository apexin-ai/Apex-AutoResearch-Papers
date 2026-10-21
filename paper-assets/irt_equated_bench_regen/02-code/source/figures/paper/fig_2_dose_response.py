#!/usr/bin/env python3
"""Figure 4: Semi-synthetic dose-response — grouped bar chart."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

plt.rcParams.update({
    'font.family': 'DejaVu Serif',
    'font.size': 7,
    'axes.titlesize': 8,
    'axes.labelsize': 7,
    'xtick.labelsize': 6.5,
    'ytick.labelsize': 6.5,
    'legend.fontsize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

data_path = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/data/dose_response_summary_779a18.csv'
df = pd.read_csv(data_path)
df = df[df['cohort_type'] == 'temporal'].copy()

baseline_tpr = df[df['p'] == 0.0].set_index('mh_variant')['tpr_mean']
baseline_fpr = df[df['p'] == 0.0].set_index('mh_variant')['fpr_mean']

p_vals = [0.3, 0.5, 0.7, 1.0]
variants = ['external', 'standard']
labels_v = {'external': 'Cross-subject', 'standard': 'Standard'}
colors_v = {'external': '#0072B2', 'standard': '#D55E00'}

fig, (ax_top, ax_bot) = plt.subplots(
    2, 1, figsize=(3.25, 2.8),
    gridspec_kw={'height_ratios': [1, 1]},
    sharex=True,
)
fig.subplots_adjust(hspace=0.18)

bar_w = 0.3
x = np.arange(len(p_vals))

# === Top panel: ΔTPR ===
for i, v in enumerate(variants):
    dtpr_vals = []
    dtpr_err = []
    for p in p_vals:
        row = df[(df['mh_variant'] == v) & (df['p'] == p)].iloc[0]
        dtpr_vals.append(row['tpr_mean'] - baseline_tpr[v])
        dtpr_err.append(row['tpr_std'])

    offset = (i - 0.5) * bar_w
    bars = ax_top.bar(x + offset, dtpr_vals, bar_w * 0.85, yerr=dtpr_err,
                      color=colors_v[v], alpha=0.85, edgecolor='white', linewidth=0.5,
                      capsize=2, error_kw={'linewidth': 0.8},
                      label=labels_v[v], zorder=3)

ax_top.set_ylabel(r'$\Delta$TPR (detection power)')
ax_top.set_ylim(0, 0.78)

# Annotate ΔTPR = +0.508 at p=0.5
ax_top.annotate(r'$\Delta$TPR = +0.508',
                xy=(1 - 0.5 * bar_w, 0.508), xytext=(1.8, 0.58),
                fontsize=6, color=colors_v['external'],
                arrowprops=dict(arrowstyle='->', color=colors_v['external'], lw=0.8),
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                          edgecolor=colors_v['external'], alpha=0.9, linewidth=0.6))

ax_top.legend(loc='upper left', frameon=True, framealpha=0.9, edgecolor='#cccccc',
              handlelength=1.0, handletextpad=0.3, borderpad=0.3)

# === Bottom panel: ΔFPR ===
for i, v in enumerate(variants):
    dfpr_vals = []
    dfpr_err = []
    for p in p_vals:
        row = df[(df['mh_variant'] == v) & (df['p'] == p)].iloc[0]
        dfpr_vals.append(row['fpr_mean'] - baseline_fpr[v])
        dfpr_err.append(row['fpr_std'])

    offset = (i - 0.5) * bar_w
    ax_bot.bar(x + offset, dfpr_vals, bar_w * 0.85, yerr=dfpr_err,
               color=colors_v[v], alpha=0.85, edgecolor='white', linewidth=0.5,
               capsize=2, error_kw={'linewidth': 0.8}, zorder=3)

ax_bot.set_ylabel(r'$\Delta$FPR')
ax_bot.set_ylim(-0.02, 0.38)
ax_bot.axhline(0, color='#999999', linewidth=0.5, linestyle='-', zorder=0)

# Label "0" for cross-subject ΔFPR
ax_bot.text(x[1] - 0.5 * bar_w, 0.015, '0', ha='center', va='bottom',
            fontsize=6, color=colors_v['external'], fontweight='bold')

ax_bot.set_xticks(x)
ax_bot.set_xticklabels([f'$p = {p}$' for p in p_vals])
ax_bot.set_xlabel('Exploitation rate')

plt.tight_layout(pad=0.3)

out_base = '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_2_dose_response'
fig.savefig(f'{out_base}.pdf')
fig.savefig(f'{out_base}.png')
plt.close()
print(f'Saved: {out_base}.pdf/.png')
