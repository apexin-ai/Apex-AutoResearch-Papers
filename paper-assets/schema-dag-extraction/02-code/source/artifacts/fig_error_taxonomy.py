#!/usr/bin/env python3
"""Figure 2: Error Taxonomy — stacked bar charts by BCS bin."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# ---------- Style ----------
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 10,
    'axes.titlesize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Colorblind-friendly palette
C_INTRA = '#0173B2'   # blue  — IntraSub / WrongType
C_EXTRA = '#DE8F05'   # orange — ExtraSub / Missed
C_OTHER = '#CC78BC'   # purple — Other / Correct
C_CORRECT = '#949494' # grey  — Correct

fig, axes = plt.subplots(1, 2, figsize=(6.75, 2.6))
bar_width = 0.55

# ===== (a) Few-NERD NER Error Distribution =====
ax = axes[0]
bins_a = ['Zero\n(BCS=0)', 'Low\n(0.5–0.7)', 'Med\n(0.7–0.8)', 'High\n(≥0.95)']
intra_a = [0.0, 1.6, 10.6, 49.4]
extra_a = [90.3, 80.0, 65.0, 30.8]
other_a = [100 - i - e for i, e in zip(intra_a, extra_a)]

x_a = np.arange(len(bins_a))
bars_other = ax.bar(x_a, other_a, bar_width, color=C_OTHER, label='Other')
bars_extra = ax.bar(x_a, extra_a, bar_width, bottom=other_a, color=C_EXTRA, label='ExtraSub')
bars_intra = ax.bar(x_a, intra_a, bar_width,
                    bottom=[o + e for o, e in zip(other_a, extra_a)],
                    color=C_INTRA, label='IntraSub')

ax.set_xticks(x_a)
ax.set_xticklabels(bins_a)
ax.set_xlabel('BCS Bin')
ax.set_ylabel('Error Proportion (%)')
ax.set_title('(a) Few-NERD NER', fontweight='bold', fontsize=9)
ax.set_ylim(0, 105)
ax.legend(loc='upper left', framealpha=0.9, edgecolor='none')

# percentage labels on IntraSub portion
for i, v in enumerate(intra_a):
    if v > 3:
        y_pos = other_a[i] + extra_a[i] + v / 2
        ax.text(x_a[i], y_pos, f'{v:.0f}%', ha='center', va='center',
                fontsize=7, color='white', fontweight='bold')

# ===== (b) FewRel RE Error Distribution =====
ax = axes[1]
bins_b = ['Zero\n(BCS=0)', 'Low\n(0.565)', 'Med\n(0.729)', 'High\n(0.86)', 'V.High\n(0.971)']
correct_b = [85.73, 85.42, 75.70, 66.67, 52.03]
wrong_b   = [0.0, 4.17, 13.0, 20.28, 32.25]
missed_b  = [14.27, 10.42, 11.3, 13.05, 15.71]

x_b = np.arange(len(bins_b))
bars_c = ax.bar(x_b, correct_b, bar_width, color=C_CORRECT, label='Correct')
bars_w = ax.bar(x_b, wrong_b, bar_width, bottom=correct_b, color=C_INTRA, label='WrongType')
bars_m = ax.bar(x_b, missed_b, bar_width,
                bottom=[c + w for c, w in zip(correct_b, wrong_b)],
                color=C_EXTRA, label='Missed')

ax.set_xticks(x_b)
ax.set_xticklabels(bins_b)
ax.set_xlabel('BCS Bin')
ax.set_ylabel('Proportion (%)')
ax.set_title('(b) FewRel RE', fontweight='bold', fontsize=9)
ax.set_ylim(0, 105)
ax.legend(loc='lower left', framealpha=0.9, edgecolor='none')

# percentage labels on WrongType portion
for i, v in enumerate(wrong_b):
    if v > 5:
        y_pos = correct_b[i] + v / 2
        ax.text(x_b[i], y_pos, f'{v:.0f}%', ha='center', va='center',
                fontsize=7, color='white', fontweight='bold')

plt.tight_layout(w_pad=2.0)
outpath = '/root/schema-dag-extraction/figures/paper/fig_error_taxonomy.pdf'
fig.savefig(outpath, format='pdf')
print(f'Saved: {outpath}')
plt.close()
