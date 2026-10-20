"""Generate label_decomposition.pdf: two-tier episode-level label decomposition.

Top row: 245 episodes → tie (150) vs non-tie (95)
Bottom row: 95 non-tie → death-sole (54) + death+score (21) + non-death (20)
Compact version: minimal whitespace, legend integrated tightly.
"""
import paper_style; paper_style.apply_style()
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

TOTAL = 245
TIE = 150
NON_TIE = 95
DEATH_SOLE = 54
DEATH_SCORE = 21
NON_DEATH = 20

fig, ax = plt.subplots(figsize=(3.25, 2.1))

bar_h = 0.38
y_top = 0.95
y_bot = 0.0
gap = 0.03

# --- Top row: All 245 episodes ---
ax.barh(y_top, TIE, left=0, height=bar_h,
        color=paper_style.C_NEUTRAL, **paper_style.bar_edge_style())
ax.barh(y_top, NON_TIE, left=TIE + gap, height=bar_h,
        color='#D4E6F1', **paper_style.bar_edge_style())

ax.text(TIE / 2, y_top, f'No preference\n{TIE}', ha='center', va='center',
        fontsize=6.5, color='#333333', fontweight='bold', linespacing=1.1)
ax.text(TIE + gap + NON_TIE / 2, y_top, f'Non-tie\n{NON_TIE}', ha='center', va='center',
        fontsize=6.5, color='#333333', fontweight='bold', linespacing=1.1)

ax.text(TOTAL / 2, y_top + bar_h / 2 + 0.08,
        f'All episodes ($N = {TOTAL}$)', ha='center', va='bottom',
        fontsize=7.5, fontweight='bold', color='#333333')

# --- Bottom row: 95 non-tie decomposed ---
x_offset = TIE + gap

x0 = x_offset
ax.barh(y_bot, DEATH_SOLE, left=x0, height=bar_h,
        color=paper_style.C_DEATH_SOLE, **paper_style.bar_edge_style())
ax.text(x0 + DEATH_SOLE / 2, y_bot, f'{DEATH_SOLE}', ha='center', va='center',
        fontsize=7.5, color='white', fontweight='bold')

x1 = x0 + DEATH_SOLE + gap
ax.barh(y_bot, DEATH_SCORE, left=x1, height=bar_h,
        color=paper_style.C_DEATH_SCORE, **paper_style.bar_edge_style())
ax.text(x1 + DEATH_SCORE / 2, y_bot, f'{DEATH_SCORE}', ha='center', va='center',
        fontsize=7, color='white', fontweight='bold')

x2 = x1 + DEATH_SCORE + gap
ax.barh(y_bot, NON_DEATH, left=x2, height=bar_h,
        color=paper_style.C_NON_DEATH, **paper_style.bar_edge_style())
ax.text(x2 + NON_DEATH / 2, y_bot, f'{NON_DEATH}', ha='center', va='center',
        fontsize=7, color='#333333', fontweight='bold')

# --- Connecting lines ---
top_left = TIE + gap
top_right = TIE + gap + NON_TIE
bot_left = x0
bot_right = x2 + NON_DEATH
y_top_bottom = y_top - bar_h / 2
y_bot_top = y_bot + bar_h / 2

ax.plot([top_left, bot_left], [y_top_bottom, y_bot_top],
        color='#BBBBBB', linewidth=0.5, linestyle='--')
ax.plot([top_right, bot_right], [y_top_bottom, y_bot_top],
        color='#BBBBBB', linewidth=0.5, linestyle='--')

# --- Bracket over death segments ---
death_right = x1 + DEATH_SCORE
bracket_y = y_bot - bar_h / 2 - 0.04
tip = 0.03
ax.plot([bot_left, bot_left, death_right, death_right],
        [bracket_y + tip, bracket_y, bracket_y, bracket_y + tip],
        color='#333333', linewidth=0.6, clip_on=False)
ax.text((bot_left + death_right) / 2, bracket_y - 0.05,
        '75/95 = 78.9% death-driven',
        ha='center', va='top', fontsize=5.5, style='italic', color='#333333')

# --- Legend (compact, right-aligned below bracket) ---
legend_items = [
    (paper_style.C_NEUTRAL, 'No pref.'),
    (paper_style.C_DEATH_SOLE, 'Death: sole'),
    (paper_style.C_DEATH_SCORE, 'Death + score'),
    (paper_style.C_NON_DEATH, 'Non-death'),
]
handles = [mpatches.Patch(facecolor=c, **paper_style.bar_edge_style(), label=l)
           for c, l in legend_items]
leg = ax.legend(handles=handles, loc='lower left',
                bbox_to_anchor=(-0.02, -0.10), ncol=4, fontsize=5,
                frameon=False, handlelength=0.8, handletextpad=0.2,
                columnspacing=0.5, borderpad=0.2)

ax.set_xlim(-3, TOTAL + 3)
ax.set_ylim(-0.48, y_top + bar_h / 2 + 0.20)
ax.set_yticks([])
ax.set_xticks([])
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout(pad=0.1)

out_dir = os.path.dirname(os.path.abspath(__file__))
for ext in ['pdf', 'png']:
    path = os.path.join(out_dir, f'label_decomposition.{ext}')
    fig.savefig(path, bbox_inches='tight', pad_inches=0.04, dpi=300)
plt.close()
print(f"Saved: {os.path.join(out_dir, 'label_decomposition.pdf')} ({os.path.getsize(os.path.join(out_dir, 'label_decomposition.pdf'))} bytes)")
