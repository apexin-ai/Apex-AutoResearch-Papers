"""
Figure 4 (candidate): Complexity-bin analysis — CLS vs CWM gap by output complexity.

Narrative: CLS-CWM gap widens from simple to complex bins,
supporting complexity-dependent divergence hypothesis.

Function-level data (available now):
  Simple bin: CLS-CWM gap = 16.7pp (short outputs: ints, bools)
  Complex bin: CLS-CWM gap = 42.9pp (longer outputs: strings, lists)
  (These are illustrative; replace with actual bin boundaries from registry)

Repo-level data (May 20-21):
  Bins TBD — could use output token length quartiles or mutation type grouping.

When data arrives:
  1. Define bin boundaries (output_length quartiles or semantic categories)
  2. Fill in cls_acc and cwm_acc per bin
  3. Optionally add multi-seed error bars
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'text.usetex': False,
})

# ── Data: fill in from registry / experiment outputs ─────────────────
# Option A: Two-bin (function vs repo)
bin_labels_2 = ['Function-level\n(short outputs)', 'Repo-level\n(long outputs)']
cls_acc_2 = [88.43, 84.48]   # CLS accuracy per bin
cwm_acc_2 = [87.19, 65.17]   # CWM accuracy per bin
gaps_2 = [c - w for c, w in zip(cls_acc_2, cwm_acc_2)]

# Option B: Fine-grained bins by output token length (PLACEHOLDER)
# bin_labels_fine = ['Q1\n(≤10 tok)', 'Q2\n(11-50)', 'Q3\n(51-200)', 'Q4\n(>200)']
# cls_acc_fine = [TBD, TBD, TBD, TBD]
# cwm_acc_fine = [TBD, TBD, TBD, TBD]
# gaps_fine = [c - w for c, w in zip(cls_acc_fine, cwm_acc_fine)]

# ── Plot: Grouped bar chart ──────────────────────────────────────────
# Using Option A for now; switch to Option B when fine-grained data arrives.

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.5),
                                gridspec_kw={'width_ratios': [3, 2]})

# Left panel: accuracy by formulation × complexity
x = np.arange(len(bin_labels_2))
w = 0.32
cls_color = '#0072B2'
cwm_color = '#D55E00'

bars_cls = ax1.bar(x - w/2, cls_acc_2, w, label='CLS', color=cls_color,
                   edgecolor='white', linewidth=0.5, zorder=3)
bars_cwm = ax1.bar(x + w/2, cwm_acc_2, w, label='CWM', color=cwm_color,
                   edgecolor='white', linewidth=0.5, zorder=3)

# Error bars placeholder — uncomment when multi-seed data available
# cls_ci = [0.78, TBD]  # std or bootstrap CI half-width
# cwm_ci = [0.37, TBD]
# ax1.errorbar(x - w/2, cls_acc_2, yerr=cls_ci, fmt='none',
#              ecolor='#333', capsize=3, capthick=1, elinewidth=1, zorder=4)
# ax1.errorbar(x + w/2, cwm_acc_2, yerr=cwm_ci, fmt='none',
#              ecolor='#333', capsize=3, capthick=1, elinewidth=1, zorder=4)

ax1.axhline(y=72.96, color='gray', linestyle='--', linewidth=0.8, alpha=0.6,
            label='Majority baseline', zorder=1)

ax1.set_xticks(x)
ax1.set_xticklabels(bin_labels_2)
ax1.set_ylabel('Accuracy (%)')
ax1.set_ylim(50, 95)
ax1.legend(loc='lower left', framealpha=0.9)
ax1.yaxis.grid(True, linestyle='--', alpha=0.3, zorder=0)
ax1.set_axisbelow(True)

# Right panel: gap magnitude
gap_colors = ['#7FBFDF', '#994400']
ax2.bar(x, gaps_2, 0.5, color=gap_colors, edgecolor='white',
        linewidth=0.5, zorder=3)
for i, g in enumerate(gaps_2):
    ax2.text(i, g + 0.8, f'{g:.1f} pp', ha='center', va='bottom',
             fontsize=10, fontweight='bold', color=gap_colors[i])

ax2.set_xticks(x)
ax2.set_xticklabels(bin_labels_2)
ax2.set_ylabel('CLS − CWM Gap (pp)')
ax2.set_ylim(0, max(gaps_2) * 1.3)
ax2.yaxis.grid(True, linestyle='--', alpha=0.3, zorder=0)
ax2.set_axisbelow(True)

fig.suptitle('Complexity-Dependent Formulation Divergence', fontsize=13, y=1.02)
plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/figures/paper'
fig.savefig(f'{out_dir}/fig4_complexity_bin.pdf')
fig.savefig(f'{out_dir}/fig4_complexity_bin.png')
plt.close()

import os
for ext in ['pdf', 'png']:
    p = f'{out_dir}/fig4_complexity_bin.{ext}'
    sz = os.path.getsize(p)
    print(f'{p}: {sz} bytes')
    assert sz > 5000, f'{ext} too small: {sz}'
print('Done. Replace placeholder data with actual per-bin accuracy from registry.')
