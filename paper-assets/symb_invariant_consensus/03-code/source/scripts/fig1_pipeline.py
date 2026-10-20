#!/usr/bin/env python3
"""Generate SICA pipeline concept figure (Fig 1) comparing SICA vs Self-Consistency."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
})

# Okabe-Ito color palette
BLUE_L = '#56B4E9'   # sky blue (shared steps)
BLUE_D = '#0072B2'   # deep blue (SICA-specific)
ORANGE = '#E69F00'   # orange (highlight / cross-answer)
GREEN  = '#009E73'   # teal-green (final answer)
GRAY   = '#AAAAAA'   # gray (SC baseline)

fig, ax = plt.subplots(figsize=(16, 7))
ax.set_xlim(-0.5, 16.5)
ax.set_ylim(-0.5, 7.5)
ax.axis('off')

# --- Background bands ---
bg_sica = FancyBboxPatch((-0.3, 3.8), 16.6, 3.5, boxstyle='round,pad=0.15',
                          facecolor='#EBF5FB', edgecolor='none', alpha=0.35, zorder=0)
ax.add_patch(bg_sica)
bg_sc = FancyBboxPatch((-0.3, -0.2), 16.6, 3.2, boxstyle='round,pad=0.15',
                        facecolor='#F5F5F5', edgecolor='none', alpha=0.35, zorder=0)
ax.add_patch(bg_sc)

# Path labels
ax.text(0.0, 7.1, 'SICA (Ours)', fontsize=14, fontweight='bold', color=BLUE_D, va='top')
ax.text(0.0, 2.7, 'Self-Consistency (SC)', fontsize=13, fontweight='bold', color='#777', va='top')


def draw_box(cx, cy, w, h, text, fc, ec='#333', fs=10, fw='normal',
             tc='white', ls='-', lw=1.5):
    patch = FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                            boxstyle='round,pad=0.12', facecolor=fc,
                            edgecolor=ec, linewidth=lw, linestyle=ls,
                            zorder=3, alpha=0.95)
    ax.add_patch(patch)
    ax.text(cx, cy, text, ha='center', va='center',
            fontsize=fs, fontweight=fw, color=tc, zorder=4, linespacing=1.3)


def draw_arrow(x1, y1, x2, y2, c='#555', lw=1.5, ls='-', cs='arc3,rad=0'):
    patch = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->',
                             mutation_scale=18, color=c, linewidth=lw,
                             linestyle=ls, zorder=2, connectionstyle=cs)
    ax.add_patch(patch)


# Y positions
YS = 5.5   # SICA row
YM = 3.5   # shared / middle row
YC = 1.3   # SC row

# ==================== SHARED SECTION ====================

draw_box(1.0, YM, 1.5, 0.8, 'Question $q$',
         fc='#EEEEEE', ec='#666', tc='#333', fs=11, fw='bold')

draw_arrow(1.75, YM, 2.35, YM)

draw_box(3.3, YM, 1.8, 0.9, 'LLM Sampling\n$K$=12, $T$=0.7',
         fc=BLUE_L, ec='#3A8FBF')

draw_arrow(4.2, YM, 4.6, YM)

draw_box(5.4, YM, 1.5, 0.85, '$K$ Reasoning\nTraces',
         fc=BLUE_L, ec='#3A8FBF')

# ==================== FORK ====================

# Fork dot
ax.plot(6.5, YM, 'o', color='#555', markersize=5, zorder=5)
draw_arrow(6.15, YM, 6.5, YM)

# Up to SICA (curved)
draw_arrow(6.5, YM, 6.75, YS, c=BLUE_D, lw=2, cs='arc3,rad=-0.4')

# Down to SC (curved, dashed)
draw_arrow(6.5, YM, 6.9, YC, c=GRAY, lw=1.5, ls='--', cs='arc3,rad=0.4')

# ==================== SICA PATH ====================

draw_box(7.8, YS, 2.1, 0.9, 'FOL Constraint\nExtraction',
         fc=BLUE_D, ec='#004C7F', fw='bold')

# "Same model" annotation
ax.text(7.8, YS - 0.65, 'Same model\n(self-extraction)',
        fontsize=8, ha='center', va='top', color=ORANGE,
        fontstyle='italic', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF8E7',
                  edgecolor=ORANGE, alpha=0.85, lw=0.8))

draw_arrow(8.85, YS, 9.15, YS, c=BLUE_D, lw=2)

draw_box(9.9, YS, 1.5, 0.9, 'Dedup +\nWeighting',
         fc=BLUE_D, ec='#004C7F')

ax.text(9.9, YS - 0.6, '$w_m$ = freq',
        fontsize=8, ha='center', va='top', color='#555', fontstyle='italic')

draw_arrow(10.65, YS, 10.95, YS, c=BLUE_D, lw=2)

draw_box(11.7, YS, 1.5, 0.9, 'Partial\nMAX-SAT (Z3)',
         fc=BLUE_D, ec='#004C7F', fw='bold')

draw_arrow(12.45, YS, 12.75, YS, c=BLUE_D, lw=2)

# Dashed highlight border around Cross-Answer Scoring (extends down to cover sigma)
highlight = FancyBboxPatch((12.75, YS - 0.95), 2.0, 1.55,
                            boxstyle='round,pad=0.12', facecolor='none',
                            edgecolor=ORANGE, linewidth=1.8,
                            linestyle='--', zorder=2)
ax.add_patch(highlight)

draw_box(13.75, YS, 1.8, 0.9, 'Cross-Answer\nScoring',
         fc=ORANGE, ec='#B87A00')

ax.text(13.75, YS - 0.6, r'$\sigma(c, a)\;\forall a \in \mathcal{A}$',
        fontsize=9, ha='center', va='top', color='#B87A00', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.1', facecolor='white',
                  edgecolor='none', alpha=0.7))

draw_arrow(14.65, YS, 14.95, YS, c=GREEN, lw=2)

draw_box(15.6, YS, 1.2, 0.75, 'Best\nAnswer',
         fc=GREEN, ec='#007A5E', fw='bold')

# ==================== SC PATH ====================

draw_box(7.7, YC, 1.6, 0.8, 'Majority\nVote',
         fc=GRAY, ec='#888')

draw_arrow(8.5, YC, 8.95, YC, c=GRAY, lw=1.5, ls='--')

draw_box(9.8, YC, 1.7, 0.75, 'Most Frequent\nAnswer',
         fc='#B8E6D0', ec='#7CBE9E', tc='#333')

# ==================== SAVE ====================

outdir = '/root/symb_invariant_consensus/artifacts/figures/paper'
os.makedirs(outdir, exist_ok=True)
for ext in ('pdf', 'png'):
    fig.savefig(f'{outdir}/fig1_pipeline.{ext}')
plt.close()
print('Saved fig1_pipeline.pdf and fig1_pipeline.png')
