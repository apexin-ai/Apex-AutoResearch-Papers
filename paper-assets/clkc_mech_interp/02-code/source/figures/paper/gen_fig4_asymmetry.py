#!/usr/bin/env python3
"""Fig 4: Cross-lingual Transfer Asymmetry Forest Plot — single-axes layout."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.transforms import blended_transform_factory
from pathlib import Path

# ── Color system ─────────────────────────────────────────────────────
NAVY  = '#1B2838'
SLATE = '#3D5A80'
TEAL  = '#2A7F8F'
CORAL = '#D4513D'

COLOR_CONFLICT = CORAL
COLOR_XNLI     = TEAL

def task_color(task):
    return COLOR_CONFLICT if task == 'conflict' else COLOR_XNLI

# ── Data ─────────────────────────────────────────────────────────────
rows = [
    ('Llama-3.1-8B (Conflict)', 7.27, 0.37, 13.97, 'conflict'),
    ('Llama-3.1-8B (XNLI)',    5.97, 0.92, 11.33, 'xnli'),
    ('Qwen3-8B (Conflict)',    7.23, -0.60, 13.69, 'conflict'),
    ('Qwen3-8B (XNLI)',        6.72, 2.36, 11.73, 'xnli'),
    ('Gemma-2-9B (Conflict)',   6.62, 1.90, 11.08, 'conflict'),
    ('Gemma-2-9B (XNLI)',       7.81, 5.71,  9.99, 'xnli'),
]

y_positions = [5.9, 5.1, 3.9, 3.1, 1.7, 0.9]

# ── Global style ─────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Helvetica', 'Arial'],
    'mathtext.fontset': 'dejavusans',
    'axes.facecolor': '#FFFFFF',
    'figure.facecolor': '#FFFFFF',
    'text.color': 'black',
    'axes.labelcolor': 'black',
    'xtick.color': 'black',
    'ytick.color': 'black',
})

# ── Figure (single axes) ────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 4.2))
ax.set_xlim(-4, 16)
y_lo, y_hi = -0.2, 6.6
ax.set_ylim(y_lo, y_hi)

# x in axes fraction, y in data coords
trans = blended_transform_factory(ax.transAxes, ax.transData)

# ── Left: model headers ─────────────────────────────────────────────
for hdr, idx in [('Llama-3.1-8B', 0), ('Qwen3-8B', 2), ('Gemma-2-9B', 4)]:
    ax.text(-0.02, y_positions[idx] + 0.55, hdr,
            ha='right', va='center', fontsize=12,
            fontweight='bold', color=NAVY,
            transform=trans, clip_on=False)

# ── Left: task labels ───────────────────────────────────────────────
for (label, _, _, _, task), y in zip(rows, y_positions):
    short = label.split('(')[1].rstrip(')')
    ax.text(-0.02, y, short, ha='right', va='center',
            fontsize=11, color=task_color(task),
            transform=trans, clip_on=False)

# ── Equivalence zone & zero line ────────────────────────────────────
ax.axvspan(-2, 2, color='#E8E8E8', alpha=0.6, zorder=0)
ax.text(0, y_hi - 0.25, '±2 pp', ha='center', va='top',
        fontsize=9, color='#666666', fontstyle='italic')
ax.axvline(0, color=SLATE, linewidth=0.8, linestyle='--', zorder=1, alpha=0.7)

# ── Horizontal separators ───────────────────────────────────────────
sep_y1 = (y_positions[1] + y_positions[2]) / 2
sep_y2 = (y_positions[3] + y_positions[4]) / 2
for sep_y in [sep_y1, sep_y2]:
    line = ax.axhline(sep_y, color='#E0E0E0', linewidth=0.7, zorder=0)
    line.set_clip_on(False)

# ── CI bars and dots ─────────────────────────────────────────────────
for (label, pt, lo, hi, task), y in zip(rows, y_positions):
    c = task_color(task)
    ax.hlines(y, lo, hi, colors=c, linewidth=2.2, zorder=2)
    ax.plot(pt, y, 'o', color=c, markersize=8.5, zorder=3,
            markeredgecolor='white', markeredgewidth=0.8)

# ── Spines ───────────────────────────────────────────────────────────
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#333333')
ax.spines['bottom'].set_linewidth(0.8)
ax.tick_params(left=False, labelleft=False)
ax.set_xlabel('Transfer Asymmetry (ZH→EN − EN→ZH), pp',
              fontsize=11, color='black')
ax.tick_params(axis='x', labelsize=10, colors='black')

# ── Legend ───────────────────────────────────────────────────────────
legend_handles = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor=COLOR_CONFLICT,
           markersize=7, markeredgecolor='white', markeredgewidth=0.5,
           label='Conflict'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=COLOR_XNLI,
           markersize=7, markeredgecolor='white', markeredgewidth=0.5,
           label='XNLI'),
]
leg = ax.legend(handles=legend_handles, loc='lower right', frameon=False,
                fontsize=10, handletextpad=0.3, borderpad=0.4)
for t in leg.get_texts():
    t.set_color('black')

# ── Right: inline numbers ───────────────────────────────────────────
for (label, pt, lo, hi, task), y in zip(rows, y_positions):
    sign = lambda v: f'+{v:.1f}' if v >= 0 else f'{v:.1f}'
    txt = f'{sign(pt)}  [{sign(lo)}, {sign(hi)}]'
    ax.text(1.02, y, txt, ha='left', va='center',
            fontsize=10, color=task_color(task), fontfamily='monospace',
            transform=trans, clip_on=False)

# ── Save ─────────────────────────────────────────────────────────────
out_dir = Path(__file__).resolve().parent
for name in ['fig4_asymmetry.png', 'fig4_asymmetry.pdf', 'fig4_asymmetry_forest.pdf']:
    fig.savefig(out_dir / name, bbox_inches='tight', pad_inches=0.02,
                dpi=300, facecolor='white')
    print(f'Saved: {out_dir / name}')
plt.close(fig)
