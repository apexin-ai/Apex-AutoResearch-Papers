#!/usr/bin/env python3
"""Regenerate Figure 1 (pipeline overview) with fixed text overlap."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

fig, ax = plt.subplots(1, 1, figsize=(14.1, 5.7))
ax.set_xlim(0, 14.1)
ax.set_ylim(0, 5.7)
ax.axis('off')

def add_box(ax, x, y, w, h, text, subtext=None, color='#E8E8E8', text_color='black',
            fontsize=11, fontweight='bold', badge=None, badge_color='white'):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                         facecolor=color, edgecolor='#888888', linewidth=1.2)
    ax.add_patch(box)
    if subtext:
        ax.text(x + w/2, y + h*0.6, text, ha='center', va='center',
                fontsize=fontsize, fontweight=fontweight, color=text_color)
        ax.text(x + w/2, y + h*0.28, subtext, ha='center', va='center',
                fontsize=8, color='#555555', style='italic')
    else:
        ax.text(x + w/2, y + h/2, text, ha='center', va='center',
                fontsize=fontsize, fontweight=fontweight, color=text_color)
    if badge:
        bx = x + w - 0.15
        by = y + h/2
        badge_box = FancyBboxPatch((bx - 0.45, by - 0.18), 0.9, 0.36,
                                    boxstyle="round,pad=0.05",
                                    facecolor=badge_color, edgecolor='#888888', linewidth=0.8)
        ax.add_patch(badge_box)
        ax.text(bx, by, badge, ha='center', va='center', fontsize=8, fontweight='bold')

def add_arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#888888', lw=1.5))

# Left pipeline boxes
bh = 1.0
mid_y = 2.35

add_box(ax, 0.3, mid_y, 1.8, bh, "Code + Test", subtext="HumanEval+\nMBPP+\nDebugBench",
        color='#D6E4F0')
add_arrow(ax, 2.1, mid_y + bh/2, 2.8, mid_y + bh/2)

add_box(ax, 2.8, mid_y, 1.6, bh, "Execute", subtext="Python tracer", color='#D6E4F0')
add_arrow(ax, 4.4, mid_y + bh/2, 5.1, mid_y + bh/2)

add_box(ax, 5.1, mid_y, 1.6, bh, "Raw Trace", subtext="calls, vars,\nexceptions,\nassertions\n(~2000 tok)",
        color='#E8E8E8')
add_arrow(ax, 6.7, mid_y + bh/2, 7.2, mid_y + bh/2)

# Dashed box: Trace Compression Strategies
dash_x, dash_y, dash_w, dash_h = 7.2, 0.5, 3.4, 4.7
dashed_rect = mpatches.FancyBboxPatch((dash_x, dash_y), dash_w, dash_h,
                                       boxstyle="round,pad=0.15",
                                       facecolor='#FAFAFA', edgecolor='#AAAAAA',
                                       linewidth=1.5, linestyle='--')
ax.add_patch(dashed_rect)
# Title ABOVE the dashed box to avoid overlap
ax.text(dash_x + dash_w/2, dash_y + dash_h + 0.15, "Trace Compression Strategies",
        ha='center', va='bottom', fontsize=11, fontweight='bold', color='#555555')

# Condition boxes inside dashed region (from top to bottom)
cw, ch = 2.8, 0.75
cx = dash_x + (dash_w - cw) / 2
gap = 0.2

# No Trace (top) - gray
cy_no = dash_y + dash_h - ch - 0.35
add_box(ax, cx, cy_no, cw, ch, "No Trace", subtext="(code+test only)",
        color='#D5D5D5', fontsize=10)

# Full Trace - light orange
cy_full = cy_no - ch - gap
add_box(ax, cx, cy_full, cw, ch, "Full Trace", subtext="(up to 2048 tok)",
        color='#FFE0B2', fontsize=10, badge="81.44%", badge_color='#FFF3E0')

# VOTA - green/teal
cy_vota = cy_full - ch - gap
add_box(ax, cx, cy_vota, cw, ch, "VOTA", subtext="(decision-relevant)",
        color='#C8E6C9', fontsize=10, badge="99.05%", badge_color='#E8F5E9')

# Exception Only (bottom) - yellow, highlighted
cy_exc = cy_vota - ch - gap
add_box(ax, cx, cy_exc, cw, ch, "Exception Only", subtext="(error events)",
        color='#FFF9C4', fontsize=10, badge="99.83%", badge_color='#FFFDE7')
# Star marker
ax.text(cx - 0.15, cy_exc + ch/2, '★', ha='center', va='center',
        fontsize=14, color='#FFB300')

# Arrow from dashed box to SFT Training
add_arrow(ax, dash_x + dash_w, mid_y + bh/2, 11.0, mid_y + bh/2)

# SFT Training box
add_box(ax, 11.0, mid_y, 1.6, bh, "SFT Training",
        subtext="LoRA fine-tuning\nQwen-2.5-Coder-7B\nDS-Coder-6.7B",
        color='#B3E5FC')
add_arrow(ax, 12.6, mid_y + bh/2, 13.0, mid_y + bh/2)

# Verdict box
add_box(ax, 13.0, mid_y - 0.1, 0.9, bh + 0.2, "Verdict", subtext="pass / fail",
        color='#E0E0E0', fontsize=10)

# Save
out_dir = os.path.dirname(os.path.abspath(__file__))
paper_dir = os.path.join(out_dir, 'paper')
os.makedirs(paper_dir, exist_ok=True)

pdf_path = os.path.join(paper_dir, 'fig1_trace_overview.pdf')
png_path = os.path.join(paper_dir, 'fig1_trace_overview.png')
fig.savefig(pdf_path, format='pdf')
fig.savefig(png_path, format='png')
plt.close()
print(f"Saved: {pdf_path}")
print(f"Saved: {png_path}")
