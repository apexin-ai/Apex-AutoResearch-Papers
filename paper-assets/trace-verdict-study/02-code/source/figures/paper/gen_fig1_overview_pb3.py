#!/usr/bin/env python3
"""Generate Figure 1: Trace-based verdict prediction pipeline overview."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as path_effects
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Font setup
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Liberation Serif', 'DejaVu Serif', 'Times New Roman']

OUT_PATH = '/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/figures/paper/fig1_trace_overview_pb3.png'

# ─────────────────────────── helpers ───────────────────────────

def draw_gradient_box(ax, x, y, w, h, color_top, color_bottom, border_color,
                      border_width=0.8, radius=0.08, linestyle='-', shadow_alpha=0.10,
                      zorder_base=1):
    """Draw a rounded box with vertical gradient fill, shadow, and border."""
    # Shadow
    shadow = FancyBboxPatch((x + 0.02, y - 0.02), w, h,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        facecolor='#888888', alpha=shadow_alpha, edgecolor='none', zorder=zorder_base)
    ax.add_patch(shadow)

    # Gradient via imshow
    gradient = np.linspace(0, 1, 256).reshape(256, 1)
    cmap = LinearSegmentedColormap.from_list('custom', [color_bottom, color_top])
    im = ax.imshow(gradient, aspect='auto', cmap=cmap,
                   extent=[x, x + w, y, y + h], zorder=zorder_base + 1)
    # Clip to rounded rect
    clip_box = FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        transform=ax.transData, facecolor='none', edgecolor='none')
    ax.add_patch(clip_box)
    im.set_clip_path(clip_box)

    # Border
    border = FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={radius}",
        facecolor='none', edgecolor=border_color, linewidth=border_width,
        linestyle=linestyle, zorder=zorder_base + 2)
    ax.add_patch(border)
    return border


def draw_pill_accent(ax, x, y_center, height, color, zorder=4):
    """Draw a thin rounded pill bar (accent stripe)."""
    pill = FancyBboxPatch((x, y_center - height / 2), 0.04, height,
        boxstyle="round,pad=0,rounding_size=0.02",
        facecolor=color, edgecolor='none', zorder=zorder)
    ax.add_patch(pill)


def draw_curved_arrow(ax, start, end, rad=0.1, color='#AAAAAA', lw=0.6):
    """Draw a curved arrow between two points."""
    arrow = FancyArrowPatch(start, end,
        connectionstyle=f"arc3,rad={rad}",
        arrowstyle='->', mutation_scale=8,
        color=color, linewidth=lw, zorder=5)
    ax.add_patch(arrow)


# ─────────────────────────── figure ───────────────────────────

fig, ax = plt.subplots(figsize=(7.0, 2.8), dpi=300)
fig.patch.set_facecolor('#FAFAF8')
ax.set_facecolor('#FAFAF8')
ax.set_xlim(0, 7.0)
ax.set_ylim(0, 2.8)
ax.set_aspect('equal')
ax.axis('off')

# ────────── STAGE 1: INPUT ──────────
s1_x, s1_w, s1_h = 0.15, 0.70, 0.42
s1_y_top = 1.60
s1_y_bot = 1.05

# Top box: Source Code
draw_gradient_box(ax, s1_x, s1_y_top, s1_w, s1_h, '#F0F4F8', '#E2E9F0', '#B0BEC5',
                  radius=0.06)
ax.text(s1_x + s1_w / 2, s1_y_top + s1_h / 2, '</> Source Code',
        fontsize=8, ha='center', va='center', color='#37474F', fontweight='bold', zorder=10)

# Bottom box: Test Input
draw_gradient_box(ax, s1_x, s1_y_bot, s1_w, s1_h, '#F0F4F8', '#E2E9F0', '#B0BEC5',
                  radius=0.06)
ax.text(s1_x + s1_w / 2, s1_y_bot + s1_h / 2, '>_ Test Input',
        fontsize=8, ha='center', va='center', color='#37474F', fontweight='bold', zorder=10)

# Benchmark label below
ax.text(s1_x + s1_w / 2, s1_y_bot - 0.16, 'HumanEval+ / MBPP+',
        fontsize=6, ha='center', va='center', color='#8B9DAF', fontstyle='italic', zorder=10)

# ────────── STAGE 2: EXECUTION ──────────
s2_x, s2_w, s2_h = 1.15, 0.70, 0.50
s2_y = 1.35

draw_gradient_box(ax, s2_x, s2_y, s2_w, s2_h, '#E8EEF4', '#D4DEE8', '#91A4B7',
                  radius=0.06)
ax.text(s2_x + s2_w / 2, s2_y + s2_h / 2, 'Python\nTracer',
        fontsize=9, ha='center', va='center', color='#37474F', fontweight='bold',
        linespacing=1.2, zorder=10)

# ────────── STAGE 3: RAW TRACE ──────────
s3_x, s3_w, s3_h = 2.15, 0.70, 0.55
s3_y = 1.325

draw_gradient_box(ax, s3_x, s3_y, s3_w, s3_h, '#F5F2EF', '#EAE5DE', '#C4BAB0',
                  radius=0.06)
ax.text(s3_x + s3_w / 2, s3_y + s3_h * 0.65, 'Raw Trace',
        fontsize=9, ha='center', va='center', color='#5D4E42', fontweight='bold', zorder=10)
ax.text(s3_x + s3_w / 2, s3_y + s3_h * 0.30, '~2k tokens',
        fontsize=7, ha='center', va='center', color='#9E9080', fontstyle='italic', zorder=10)

# Thin horizontal lines inside to suggest code texture
for frac in [0.42, 0.52, 0.62]:
    line_y = s3_y + s3_h * frac
    ax.plot([s3_x + 0.10, s3_x + s3_w - 0.10], [line_y, line_y],
            color='#C4BAB0', linewidth=0.3, zorder=4, alpha=0.5)

# ────────── STAGE 4: TRACE CONDITIONS ──────────
# Outer grouping box
cond_x, cond_w = 3.15, 2.00
cond_y_bottom, cond_y_top = 0.35, 2.45
cond_h_total = cond_y_top - cond_y_bottom

# Dashed outer frame
draw_gradient_box(ax, cond_x - 0.05, cond_y_bottom - 0.05, cond_w + 0.10, cond_h_total + 0.10,
                  '#FBFBFB', '#F8F8F6', '#D0D0D0',
                  border_width=0.4, radius=0.10, linestyle='--', shadow_alpha=0.0,
                  zorder_base=0)

# Title for grouping
ax.text(cond_x + cond_w / 2, cond_y_top + 0.12, 'Trace Conditions',
        fontsize=7.5, ha='center', va='center', color='#7B8794', fontweight='bold',
        fontstyle='italic', zorder=10)

# Individual condition boxes (top to bottom: Exception, VOTA, Full Trace, No Trace)
gap = 0.08
box_w_inner = cond_w - 0.12
box_x_inner = cond_x + 0.06

# Exception Only: 15% taller
exc_h = 0.46
other_h = 0.40

# Compute y positions (top to bottom)
total_boxes_h = exc_h + 3 * other_h + 3 * gap
start_y = cond_y_bottom + (cond_h_total - total_boxes_h) / 2

# Box 4 (bottom): No Trace
b4_y = start_y
# Box 3: Full Trace
b3_y = b4_y + other_h + gap
# Box 2: VOTA
b2_y = b3_y + other_h + gap
# Box 1 (top): Exception Only
b1_y = b2_y + other_h + gap

# --- Box 1: Exception Only (WINNER) ---
draw_gradient_box(ax, box_x_inner, b1_y, box_w_inner, exc_h,
                  '#FFF8DC', '#FFF0B0', '#C89B00',
                  border_width=1.5, radius=0.06, shadow_alpha=0.15)
draw_pill_accent(ax, box_x_inner + 0.04, b1_y + exc_h / 2, exc_h * 0.70, '#E5A70E')
# Render "Exception Only" in serif, then star separately in DejaVu Sans
ax.text(box_x_inner + 0.14, b1_y + exc_h * 0.62, 'Exception Only',
        fontsize=9, ha='left', va='center', color='#5D4037', fontweight='bold', zorder=10)
ax.text(box_x_inner + 0.14 + 0.98, b1_y + exc_h * 0.62, '★',
        fontsize=8, ha='left', va='center', color='#D4A017', fontweight='bold', zorder=10,
        fontfamily='DejaVu Sans')
ax.text(box_x_inner + box_w_inner - 0.08, b1_y + exc_h * 0.62, '99.83%',
        fontsize=9, ha='right', va='center', color='#C89B00', fontweight='bold', zorder=10)
ax.text(box_x_inner + 0.14, b1_y + exc_h * 0.28, 'Only exception/error events',
        fontsize=6.5, ha='left', va='center', color='#7B6F63', fontstyle='italic', zorder=10)

# --- Box 2: VOTA ---
draw_gradient_box(ax, box_x_inner, b2_y, box_w_inner, other_h,
                  '#EFF7EF', '#DCF0DC', '#7CB87A',
                  border_width=1.0, radius=0.06)
draw_pill_accent(ax, box_x_inner + 0.04, b2_y + other_h / 2, other_h * 0.65, '#8BBF89')
ax.text(box_x_inner + 0.14, b2_y + other_h * 0.63, 'VOTA',
        fontsize=9, ha='left', va='center', color='#2E6B2E', fontweight='bold', zorder=10)
ax.text(box_x_inner + box_w_inner - 0.08, b2_y + other_h * 0.63, '99.05%',
        fontsize=9, ha='right', va='center', color='#5A9A58', fontweight='bold', zorder=10)
ax.text(box_x_inner + 0.14, b2_y + other_h * 0.27, 'Exception + assertion + loop summary',
        fontsize=6.5, ha='left', va='center', color='#5A7A5A', fontstyle='italic', zorder=10)

# --- Box 3: Full Trace ---
draw_gradient_box(ax, box_x_inner, b3_y, box_w_inner, other_h,
                  '#F5EADE', '#EDDCC8', '#C08050',
                  border_width=1.0, radius=0.06)
draw_pill_accent(ax, box_x_inner + 0.04, b3_y + other_h / 2, other_h * 0.65, '#C49670')
ax.text(box_x_inner + 0.14, b3_y + other_h * 0.63, 'Full Trace',
        fontsize=9, ha='left', va='center', color='#7A5530', fontweight='bold', zorder=10)
ax.text(box_x_inner + box_w_inner - 0.08, b3_y + other_h * 0.63, '81.44%',
        fontsize=9, ha='right', va='center', color='#B07040', fontweight='bold', zorder=10)
ax.text(box_x_inner + 0.14, b3_y + other_h * 0.27, 'Complete line-by-line execution',
        fontsize=6.5, ha='left', va='center', color='#8A7050', fontstyle='italic', zorder=10)

# --- Box 4: No Trace ---
draw_gradient_box(ax, box_x_inner, b4_y, box_w_inner, other_h,
                  '#F2F2F2', '#E5E5E5', '#AAAAAA',
                  border_width=0.8, radius=0.06, linestyle='--')
draw_pill_accent(ax, box_x_inner + 0.04, b4_y + other_h / 2, other_h * 0.65, '#B5B5B5')
ax.text(box_x_inner + 0.14, b4_y + other_h * 0.63, 'No Trace',
        fontsize=9, ha='left', va='center', color='#555555', fontweight='bold', zorder=10)
ax.text(box_x_inner + box_w_inner - 0.08, b4_y + other_h * 0.63, '75.13%',
        fontsize=9, ha='right', va='center', color='#888888', fontweight='bold', zorder=10)
ax.text(box_x_inner + 0.14, b4_y + other_h * 0.27, 'Source code only (baseline)',
        fontsize=6.5, ha='left', va='center', color='#777777', fontstyle='italic', zorder=10)

# ────────── VERTICAL GRADIENT BAR (right of condition boxes) ──────────
bar_x = box_x_inner + box_w_inner + 0.15
bar_w = 0.03
bar_y_lo = b4_y + 0.05
bar_y_hi = b1_y + exc_h - 0.05

grad_bar = np.linspace(0, 1, 256).reshape(256, 1)
cmap_bar = LinearSegmentedColormap.from_list('acc_bar', ['#AAAAAA', '#F5C842'])
im_bar = ax.imshow(grad_bar, aspect='auto', cmap=cmap_bar,
                   extent=[bar_x, bar_x + bar_w, bar_y_lo, bar_y_hi], zorder=4)
# Clip to rounded shape
clip_bar = FancyBboxPatch((bar_x, bar_y_lo), bar_w, bar_y_hi - bar_y_lo,
    boxstyle="round,pad=0,rounding_size=0.015",
    transform=ax.transData, facecolor='none', edgecolor='none')
ax.add_patch(clip_bar)
im_bar.set_clip_path(clip_bar)

# Labels for gradient bar
ax.text(bar_x + bar_w / 2, bar_y_hi + 0.10, 'Accuracy ↑',
        fontsize=5.5, ha='center', va='center', color='#7B8794', fontweight='bold', zorder=10,
        fontfamily='DejaVu Sans')
ax.text(bar_x + bar_w / 2, bar_y_lo - 0.10, 'Info ↓',
        fontsize=5.5, ha='center', va='center', color='#7B8794', fontweight='bold', zorder=10,
        fontfamily='DejaVu Sans')

# ────────── STAGE 5: MODEL ──────────
s5_x, s5_w, s5_h = 5.55, 0.60, 0.50
s5_y = 1.35

draw_gradient_box(ax, s5_x, s5_y, s5_w, s5_h, '#F0ECF8', '#E0D8EE', '#9B8DC0',
                  radius=0.06)
ax.text(s5_x + s5_w / 2, s5_y + s5_h * 0.62, 'SFT (LoRA)',
        fontsize=9, ha='center', va='center', color='#4A3880', fontweight='bold', zorder=10)
ax.text(s5_x + s5_w / 2, s5_y + s5_h * 0.30, '1.5B–13B',
        fontsize=7, ha='center', va='center', color='#8878A8', fontstyle='italic', zorder=10,
        fontfamily='DejaVu Sans')

# ────────── STAGE 6: OUTPUT (split box) ──────────
s6_x, s6_w = 6.35, 0.50
s6_h_half = 0.25
s6_y_bot = 1.30
s6_y_top = s6_y_bot + s6_h_half

# "Verdict" label
ax.text(s6_x + s6_w / 2, s6_y_top + s6_h_half + 0.12, 'Verdict',
        fontsize=8, ha='center', va='center', color='#616161', fontweight='bold', zorder=10)

# Top half: Pass (green)
draw_gradient_box(ax, s6_x, s6_y_top, s6_w, s6_h_half, '#E8F5E9', '#D5ECD6', '#BDBDBD',
                  border_width=0.8, radius=0.05)
ax.text(s6_x + s6_w / 2 - 0.08, s6_y_top + s6_h_half / 2, '✓',
        fontsize=8.5, ha='center', va='center', color='#2E7D32', fontweight='bold', zorder=10,
        fontfamily='DejaVu Sans')
ax.text(s6_x + s6_w / 2 + 0.08, s6_y_top + s6_h_half / 2, 'Pass',
        fontsize=8.5, ha='center', va='center', color='#2E7D32', fontweight='bold', zorder=10)

# Bottom half: Fail (red)
draw_gradient_box(ax, s6_x, s6_y_bot, s6_w, s6_h_half, '#FFEBEE', '#F5DBDE', '#BDBDBD',
                  border_width=0.8, radius=0.05)
ax.text(s6_x + s6_w / 2 - 0.08, s6_y_bot + s6_h_half / 2, '✗',
        fontsize=8.5, ha='center', va='center', color='#C62828', fontweight='bold', zorder=10,
        fontfamily='DejaVu Sans')
ax.text(s6_x + s6_w / 2 + 0.08, s6_y_bot + s6_h_half / 2, 'Fail',
        fontsize=8.5, ha='center', va='center', color='#C62828', fontweight='bold', zorder=10)

# ────────── ARROWS ──────────
# Input → Execution
mid_y = 1.60
draw_curved_arrow(ax, (s1_x + s1_w, mid_y), (s2_x, s2_y + s2_h / 2), rad=0.05)

# Execution → Raw Trace
draw_curved_arrow(ax, (s2_x + s2_w, s2_y + s2_h / 2), (s3_x, s3_y + s3_h / 2), rad=0.05)

# Raw Trace → 4 condition boxes (fan-out)
rt_out_x = s3_x + s3_w
rt_out_y = s3_y + s3_h / 2

cond_in_x = box_x_inner
targets_y = [
    b1_y + exc_h / 2,
    b2_y + other_h / 2,
    b3_y + other_h / 2,
    b4_y + other_h / 2,
]
fan_rads = [-0.20, -0.10, 0.10, 0.25]
for ty, rad in zip(targets_y, fan_rads):
    draw_curved_arrow(ax, (rt_out_x, rt_out_y), (cond_in_x, ty), rad=rad)

# 4 condition boxes → Model (fan-in)
cond_out_x = box_x_inner + box_w_inner
model_in_x = s5_x
model_in_y = s5_y + s5_h / 2

fan_in_rads = [0.25, 0.10, -0.10, -0.25]
for ty, rad in zip(targets_y, fan_in_rads):
    draw_curved_arrow(ax, (cond_out_x, ty), (model_in_x, model_in_y), rad=rad)

# Model → Output
draw_curved_arrow(ax, (s5_x + s5_w, s5_y + s5_h / 2),
                  (s6_x, s6_y_bot + s6_h_half), rad=0.05)

# ────────── BOTTOM ANNOTATION ──────────
ax.text(3.5, 0.10, '— Information density decreases  |  Accuracy increases —',
        fontsize=8, ha='center', va='center', color='#7B8794', fontstyle='italic', zorder=10,
        fontfamily='DejaVu Sans')

# ────────── SAVE ──────────
plt.savefig(OUT_PATH, dpi=300, bbox_inches='tight', pad_inches=0.05, facecolor='#FAFAF8')
plt.close()
print(f'Saved: {OUT_PATH}')
