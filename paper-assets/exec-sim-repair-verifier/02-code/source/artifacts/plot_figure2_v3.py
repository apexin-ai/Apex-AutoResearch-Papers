"""Figure 2 v3: parameterized 14B data with confirmed/exploratory toggle."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────────
CONFIRMED_14B = True  # 3-seed results confirmed 2026-05-23

# 4B/8B: established multi-seed means (do not change)
sizes = [4, 8, 14]
cls_acc_4b = 88.68
cls_acc_8b = 89.94
cwm_acc_4b = 87.36
cwm_acc_8b = 87.33

# 14B: fill with 3-seed mean after training
cls_acc_14b = 89.93  # 3-seed mean (s42=89.21, s123=90.79, s456=89.79)
cwm_acc_14b = 89.50  # 3-seed mean (s42=89.26, s123=88.99, s456=90.26)

cls_acc = [cls_acc_4b, cls_acc_8b, cls_acc_14b]
cwm_acc = [cwm_acc_4b, cwm_acc_8b, cwm_acc_14b]

# ── Plot ─────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5, 3.5))

if not CONFIRMED_14B:
    ax.axvspan(12.5, 15.5, color='#f0f0f0', zorder=0)
    ax.axvline(x=13, color='#cccccc', linestyle=':', linewidth=0.8, zorder=0)
    ax.text(14, 90.65, 'exploratory', fontsize=7, color='#888888',
            ha='center', fontstyle='italic')

ax.fill_between(sizes, cls_acc, cwm_acc, color='#e0e0e0', alpha=0.5, zorder=1)

CLS_COLOR = '#2c7fb8'
CWM_COLOR = '#d95f02'

if CONFIRMED_14B:
    # All 3 points: solid line, filled markers
    ax.plot(sizes, cls_acc, 'o-', color=CLS_COLOR, linewidth=1.8,
            markersize=7, markerfacecolor=CLS_COLOR, markeredgecolor=CLS_COLOR,
            label='CLS', zorder=3)
    ax.plot(sizes, cwm_acc, 's-', color=CWM_COLOR, linewidth=1.8,
            markersize=7, markerfacecolor=CWM_COLOR, markeredgecolor=CWM_COLOR,
            label='CWM', zorder=3)
else:
    # 4B-8B: solid line, filled markers
    ax.plot(sizes[:2], cls_acc[:2], 'o-', color=CLS_COLOR, linewidth=1.8,
            markersize=7, markerfacecolor=CLS_COLOR, markeredgecolor=CLS_COLOR,
            label='CLS', zorder=3)
    ax.plot(sizes[:2], cwm_acc[:2], 's-', color=CWM_COLOR, linewidth=1.8,
            markersize=7, markerfacecolor=CWM_COLOR, markeredgecolor=CWM_COLOR,
            label='CWM', zorder=3)
    # 14B: hollow markers
    ax.plot(sizes[2], cls_acc[2], 'o', color=CLS_COLOR, markersize=7,
            markerfacecolor='white', markeredgecolor=CLS_COLOR, markeredgewidth=1.8, zorder=3)
    ax.plot(sizes[2], cwm_acc[2], 's', color=CWM_COLOR, markersize=7,
            markerfacecolor='white', markeredgecolor=CWM_COLOR, markeredgewidth=1.8, zorder=3)
    # 8B-14B: dashed line
    ax.plot([sizes[1], sizes[2]], [cls_acc[1], cls_acc[2]], '--', color=CLS_COLOR,
            linewidth=1.8, zorder=2)
    ax.plot([sizes[1], sizes[2]], [cwm_acc[1], cwm_acc[2]], '--', color=CWM_COLOR,
            linewidth=1.8, zorder=2)

# Gap annotations
gap_4b = abs(cls_acc[0] - cwm_acc[0])
mid_4b = (cls_acc[0] + cwm_acc[0]) / 2
ax.annotate(f'{gap_4b:.2f} pp', xy=(4, mid_4b), fontsize=7.5, fontweight='bold',
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#aaaaaa', lw=0.5))

gap_8b = abs(cls_acc[1] - cwm_acc[1])
mid_8b = (cls_acc[1] + cwm_acc[1]) / 2
ax.annotate(f'{gap_8b:.2f} pp', xy=(8, mid_8b), fontsize=7.5, fontweight='bold',
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#aaaaaa', lw=0.5))

gap_14b = abs(cls_acc[2] - cwm_acc[2])
mid_14b = (cls_acc[2] + cwm_acc[2]) / 2
if CONFIRMED_14B:
    ax.annotate(f'{gap_14b:.2f} pp', xy=(14, mid_14b), fontsize=7.5, fontweight='bold',
                ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#aaaaaa', lw=0.5))
else:
    ax.annotate('$\\approx$0 pp', xy=(14, mid_14b), xytext=(13.2, 90.15),
                fontsize=7.5, fontweight='bold', ha='center', va='center',
                arrowprops=dict(arrowstyle='->', color='#888888', lw=0.8),
                bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='#aaaaaa', lw=0.5))

ax.set_xlabel('Model Size', fontsize=10)
ax.set_ylabel('Accuracy (%)', fontsize=10)
ax.set_xticks(sizes)
ax.set_xticklabels(['4B', '8B', '14B'], fontsize=9)
ax.set_xlim(2.5, 15.5)
ax.set_ylim(86, 91)
ax.yaxis.set_major_locator(mticker.MultipleLocator(1))
ax.tick_params(axis='y', labelsize=9)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.3, linewidth=0.5)

ax.legend(loc='lower right', fontsize=8.5, framealpha=0.9, edgecolor='#cccccc')

fig.tight_layout(pad=0.4)

out_dir = Path('/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/figures/paper')
fig.savefig(out_dir / 'figure2_v3.pdf', bbox_inches='tight', dpi=300)
fig.savefig(out_dir / 'figure2_v3.png', bbox_inches='tight', dpi=300)
plt.close()
print('Done.')
