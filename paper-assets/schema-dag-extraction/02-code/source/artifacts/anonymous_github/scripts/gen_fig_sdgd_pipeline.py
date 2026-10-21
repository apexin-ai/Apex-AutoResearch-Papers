#!/usr/bin/env python3
"""Generate Figure B: SDGD Pipeline Failure Diagram.

Compact layout (~1.6:1 aspect ratio) for single-column display.
At columnwidth ~3.3in, rendered height is ~2.1in with all text ≥9pt.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

C_FILL = '#E8F0FE'
C_BORDER = '#4285F4'
C_ARROW = '#666666'
C_FAIL_BORDER = '#D93025'
C_FAIL_FILL = '#FCE8E6'
C_TEXT = '#333333'
C_FAIL_TEXT = '#B71C1C'

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.set_xlim(0, 7)
ax.set_ylim(0, 4.5)
ax.axis('off')


def draw_box(x, y, w, h, label, sublabel=None, fontsize=12, bold=True,
             fill=C_FILL, border=C_BORDER):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                         facecolor=fill, edgecolor=border, linewidth=1.4)
    ax.add_patch(box)
    weight = 'bold' if bold else 'normal'
    if sublabel:
        ax.text(x + w / 2, y + h / 2 + 0.13, label, ha='center', va='center',
                fontsize=fontsize, color=C_TEXT, fontweight=weight)
        ax.text(x + w / 2, y + h / 2 - 0.17, sublabel, ha='center', va='center',
                fontsize=fontsize - 2, color='#666666')
    else:
        ax.text(x + w / 2, y + h / 2, label, ha='center', va='center',
                fontsize=fontsize, color=C_TEXT, fontweight=weight)


def draw_harrow(x1, x2, y, label=None):
    arrow = FancyArrowPatch((x1, y), (x2, y),
                            arrowstyle='->', mutation_scale=14,
                            color=C_ARROW, linewidth=1.5)
    ax.add_patch(arrow)
    if label:
        ax.text((x1 + x2) / 2, y + 0.18, label, ha='center', va='bottom',
                fontsize=9, color=C_TEXT, style='italic')


# ── Main flow (y ≈ 2.25, centered) ──

ROW_Y = 2.0
BOX_H = 0.85

# 1. Full Schema
draw_box(0.1, ROW_Y, 1.1, BOX_H, "Full Schema", "(k types)", fontsize=11)

# Arrow
draw_harrow(1.2, 1.65, ROW_Y + BOX_H / 2, "Decompose")

# 2. Sub-schemas (3 stacked)
sub_x, sub_w, sub_h = 1.65, 0.75, 0.5
gap = 0.07
total = 3 * sub_h + 2 * gap
sub_start = ROW_Y + BOX_H / 2 - total / 2
for i, lbl in enumerate(["Sub₁", "Sub₂", "Sub₃"]):
    sy = sub_start + i * (sub_h + gap)
    draw_box(sub_x, sy, sub_w, sub_h, lbl, fontsize=10, bold=False)
    cy = sy + sub_h / 2
    for dx in [-0.12, 0.0, 0.12]:
        ax.plot(sub_x + sub_w / 2 + dx, cy - 0.12, 'o',
                color=C_BORDER, markersize=2.5, alpha=0.5)

ax.text(sub_x + sub_w / 2, sub_start - 0.1, "sub-schemas", ha='center',
        va='top', fontsize=8, color='#888888', style='italic')

# Arrow
draw_harrow(2.4, 2.95, ROW_Y + BOX_H / 2, "Route")

# 3. Route & Extract
draw_box(2.95, ROW_Y, 1.1, BOX_H, "Route &\nExtract", fontsize=11)

# Arrow
draw_harrow(4.05, 4.55, ROW_Y + BOX_H / 2)

# 4. Merge
draw_box(4.55, ROW_Y, 0.9, BOX_H, "Merge", fontsize=12)

# Arrow
draw_harrow(5.45, 5.9, ROW_Y + BOX_H / 2)

# 5. Final
draw_box(5.9, ROW_Y, 1.0, BOX_H, "Final", "Predictions", fontsize=11)

# ── Failure annotations ──

# A. Routing Failure — top
fail_a_x, fail_a_w = 1.7, 3.3
fail_a_y = 3.35
fail_a_h = 0.95
box_a = FancyBboxPatch((fail_a_x, fail_a_y), fail_a_w, fail_a_h,
                        boxstyle="round,pad=0.08",
                        facecolor=C_FAIL_FILL, edgecolor=C_FAIL_BORDER,
                        linewidth=1.8)
ax.add_patch(box_a)
ax.text(fail_a_x + fail_a_w / 2, fail_a_y + fail_a_h - 0.1,
        "⚠ Routing Failure", ha='center', va='top',
        fontsize=11, color=C_FAIL_TEXT, fontweight='bold')
ax.text(fail_a_x + fail_a_w / 2, fail_a_y + fail_a_h - 0.4,
        "RE: 73% multi-match rate", ha='center', va='top',
        fontsize=9.5, color=C_FAIL_TEXT)
ax.text(fail_a_x + fail_a_w / 2, fail_a_y + fail_a_h - 0.68,
        "Oracle: 0.80  vs  Practical: 0.50", ha='center', va='top',
        fontsize=9.5, color=C_FAIL_TEXT, family='monospace')

# Connector to Route & Extract box
ax.annotate("", xy=(3.5, ROW_Y + BOX_H), xytext=(3.5, fail_a_y),
            arrowprops=dict(arrowstyle='->', color=C_FAIL_BORDER, lw=1.4))

# B. Merge Amplification — bottom
fail_b_x, fail_b_w = 3.3, 3.3
fail_b_y = 0.15
fail_b_h = 0.95
box_b = FancyBboxPatch((fail_b_x, fail_b_y), fail_b_w, fail_b_h,
                        boxstyle="round,pad=0.08",
                        facecolor=C_FAIL_FILL, edgecolor=C_FAIL_BORDER,
                        linewidth=1.8)
ax.add_patch(box_b)
ax.text(fail_b_x + fail_b_w / 2, fail_b_y + fail_b_h - 0.1,
        "⚠ Merge Amplification", ha='center', va='top',
        fontsize=11, color=C_FAIL_TEXT, fontweight='bold')
ax.text(fail_b_x + fail_b_w / 2, fail_b_y + fail_b_h - 0.4,
        "NER/ED: union → false positives", ha='center', va='top',
        fontsize=9.5, color=C_FAIL_TEXT)
ax.text(fail_b_x + fail_b_w / 2, fail_b_y + fail_b_h - 0.68,
        "F1 drops −19pp", ha='center', va='top',
        fontsize=9.5, color=C_FAIL_TEXT, family='monospace')

# Connector to Merge box
ax.annotate("", xy=(5.0, ROW_Y), xytext=(5.0, fail_b_y + fail_b_h),
            arrowprops=dict(arrowstyle='->', color=C_FAIL_BORDER, lw=1.4))

# ── Save ──
out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'figures', 'paper')
os.makedirs(out_dir, exist_ok=True)

pdf_path = os.path.join(out_dir, 'fig_sdgd_pipeline.pdf')
png_path = os.path.join(out_dir, 'fig_sdgd_pipeline.png')

fig.savefig(pdf_path)
fig.savefig(png_path)
plt.close(fig)

print(f"Saved: {pdf_path}")
print(f"Saved: {png_path}")
print(f"PDF size: {os.path.getsize(pdf_path)} bytes")
print(f"PNG size: {os.path.getsize(png_path)} bytes")
