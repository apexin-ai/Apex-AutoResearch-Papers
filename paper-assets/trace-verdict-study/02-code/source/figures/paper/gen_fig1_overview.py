#!/usr/bin/env python3
"""Generate Figure 1: Trace-based verdict prediction pipeline overview.

Publication-quality figure for EMNLP 2026.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

# ── Global style ──────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'font.size': 10,
    'text.usetex': False,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})

fig, ax = plt.subplots(figsize=(14, 4.5))
ax.set_xlim(0, 14)
ax.set_ylim(0, 4.5)
ax.axis('off')
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

# ── Helper functions ──────────────────────────────────────────────────────────

def draw_box(ax, x, y, w, h, facecolor, edgecolor, linewidth=1.0,
             linestyle='-', shadow=True, shadow_offset=(0.04, -0.04),
             shadow_alpha=0.12, zorder=3, rounding_size=0.08):
    """Draw a rounded rectangle with optional drop shadow."""
    if shadow:
        shadow_box = FancyBboxPatch(
            (x + shadow_offset[0], y + shadow_offset[1]), w, h,
            boxstyle=f"round,pad=0,rounding_size={rounding_size}",
            facecolor='#000000', edgecolor='none',
            alpha=shadow_alpha, zorder=zorder - 1,
            transform=ax.transData
        )
        ax.add_patch(shadow_box)

    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={rounding_size}",
        facecolor=facecolor, edgecolor=edgecolor,
        linewidth=linewidth, linestyle=linestyle,
        zorder=zorder, transform=ax.transData
    )
    ax.add_patch(box)
    return box


def draw_gradient_box(ax, x, y, w, h, color_top, color_bottom, edgecolor,
                      linewidth=1.0, linestyle='-', shadow=True,
                      shadow_offset=(0.04, -0.04), shadow_alpha=0.12,
                      zorder=3, rounding_size=0.08):
    """Draw a rounded rectangle with vertical gradient fill."""
    if shadow:
        shadow_box = FancyBboxPatch(
            (x + shadow_offset[0], y + shadow_offset[1]), w, h,
            boxstyle=f"round,pad=0,rounding_size={rounding_size}",
            facecolor='#000000', edgecolor='none',
            alpha=shadow_alpha, zorder=zorder - 1
        )
        ax.add_patch(shadow_box)

    # Gradient via imshow clipped to rounded rect
    gradient = np.linspace(0, 1, 256).reshape(-1, 1)
    from matplotlib.colors import to_rgba
    c_top = np.array(to_rgba(color_top))
    c_bot = np.array(to_rgba(color_bottom))
    colors = np.zeros((256, 1, 4))
    for i in range(256):
        t = i / 255
        colors[i, 0] = c_top * (1 - t) + c_bot * t

    im = ax.imshow(colors, extent=[x, x + w, y, y + h],
                   aspect='auto', zorder=zorder, origin='upper',
                   interpolation='bilinear')

    clip_box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={rounding_size}",
        facecolor='none', edgecolor='none',
        transform=ax.transData
    )
    ax.add_patch(clip_box)
    im.set_clip_path(clip_box)

    border = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={rounding_size}",
        facecolor='none', edgecolor=edgecolor,
        linewidth=linewidth, linestyle=linestyle,
        zorder=zorder + 1
    )
    ax.add_patch(border)
    return border


def draw_accent_bar(ax, x, y, h, width, color, zorder=4):
    """Draw a left accent bar."""
    bar = plt.Rectangle((x, y), width, h, facecolor=color,
                        edgecolor='none', zorder=zorder)
    ax.add_patch(bar)


def draw_arrow(ax, start, end, color='#4A5568', lw=1.3, style='->',
               connectionstyle='arc3,rad=0.0', zorder=2):
    """Draw a curved arrow."""
    arrow = FancyArrowPatch(
        start, end,
        arrowstyle=f'->,head_length=0.15,head_width=0.08',
        connectionstyle=connectionstyle,
        color=color, linewidth=lw, zorder=zorder,
        mutation_scale=12
    )
    ax.add_patch(arrow)
    return arrow


# ── Layout coordinates ────────────────────────────────────────────────────────
# Stage positions (x_center, y_center)
# Total width = 14, total height = 4.5

# Stage 1: Input (x: 0.3 - 1.9)
inp_x = 0.4
inp_w = 1.5
inp_h = 0.55
inp_gap = 0.18
inp_y_top = 2.65  # Source Code
inp_y_bot = 2.65 - inp_h - inp_gap  # Test Input

# Stage 2: Execution (x: 2.5 - 3.8)
exe_x = 2.7
exe_w = 1.3
exe_h = 0.7
exe_y = (inp_y_top + inp_y_bot + inp_h) / 2 - exe_h / 2 + 0.05

# Stage 3: Raw Trace (x: 4.4 - 5.8)
raw_x = 4.5
raw_w = 1.4
raw_h = 0.8
raw_y = exe_y - 0.05

# Stage 4: Condition boxes (x: 6.6 - 10.0)
cond_x = 6.6
cond_w = 3.2  # winner box
cond_w_normal = 3.0
cond_h_winner = 0.7
cond_h_normal = 0.6
cond_gap = 0.12
accent_w = 0.06  # accent bar width in data coords

# Y positions for 4 boxes (top to bottom)
total_height = cond_h_winner + 3 * cond_h_normal + 3 * cond_gap
cond_y_start = 3.85  # top of first box
cond_ys = []
cy = cond_y_start
# Box 1: Exception Only (winner)
cond_ys.append(cy - cond_h_winner)
cy = cond_ys[0] - cond_gap
# Box 2: VOTA
cond_ys.append(cy - cond_h_normal)
cy = cond_ys[1] - cond_gap
# Box 3: Full Trace
cond_ys.append(cy - cond_h_normal)
cy = cond_ys[2] - cond_gap
# Box 4: No Trace
cond_ys.append(cy - cond_h_normal)

# Stage 5: Model (x: 10.8 - 12.2)
model_x = 10.8
model_w = 1.4
model_h = 0.8
model_y = (cond_ys[0] + cond_h_winner + cond_ys[3]) / 2 - model_h / 2

# Stage 6: Output (x: 12.8 - 13.6)
out_x = 12.8
out_w = 0.85
out_h = 0.85
out_y = model_y + model_h / 2 - out_h / 2

# ── Draw Stage 1: Input ──────────────────────────────────────────────────────
draw_gradient_box(ax, inp_x, inp_y_top, inp_w, inp_h,
                  '#F0F4F8', '#DDE5EE', '#B0BEC5', linewidth=0.8)
ax.text(inp_x + 0.12, inp_y_top + inp_h / 2, '</>', fontsize=9,
        fontweight='bold', color='#5C7A99', va='center', ha='left',
        fontfamily='monospace', zorder=5)
ax.text(inp_x + 0.42, inp_y_top + inp_h / 2, 'Source Code', fontsize=9.5,
        fontweight='bold', color='#37474F', va='center', ha='left', zorder=5)

draw_gradient_box(ax, inp_x, inp_y_bot, inp_w, inp_h,
                  '#F0F4F8', '#DDE5EE', '#B0BEC5', linewidth=0.8)
ax.text(inp_x + 0.12, inp_y_bot + inp_h / 2, '>_', fontsize=9,
        fontweight='bold', color='#5C7A99', va='center', ha='left',
        fontfamily='monospace', zorder=5)
ax.text(inp_x + 0.42, inp_y_bot + inp_h / 2, 'Test Input', fontsize=9.5,
        fontweight='bold', color='#37474F', va='center', ha='left', zorder=5)

ax.text(inp_x + inp_w / 2, inp_y_bot - 0.12, 'HumanEval+ / MBPP+',
        fontsize=7, fontstyle='italic', color='#8B9DAF',
        va='top', ha='center', zorder=5)

# ── Draw Stage 2: Execution ──────────────────────────────────────────────────
draw_gradient_box(ax, exe_x, exe_y, exe_w, exe_h,
                  '#E8EEF4', '#D0DCE8', '#91A4B7', linewidth=0.8)
ax.text(exe_x + exe_w / 2, exe_y + exe_h / 2 + 0.02, 'Python Tracer',
        fontsize=10, fontweight='bold', color='#37474F',
        va='center', ha='center', zorder=5)

# ── Draw Stage 3: Raw Trace ──────────────────────────────────────────────────
draw_gradient_box(ax, raw_x, raw_y, raw_w, raw_h,
                  '#F5F2EF', '#E8E3DD', '#C4BAB0', linewidth=0.8)
ax.text(raw_x + raw_w / 2, raw_y + raw_h / 2 + 0.1, 'Raw Trace',
        fontsize=10, fontweight='bold', color='#5D4E37',
        va='center', ha='center', zorder=5)
ax.text(raw_x + raw_w / 2, raw_y + raw_h / 2 - 0.15, '~2,000 tokens',
        fontsize=7.5, color='#9E9484', va='center', ha='center', zorder=5)

# Subtle horizontal lines suggesting code texture
for ly in np.linspace(raw_y + 0.15, raw_y + raw_h - 0.15, 4):
    line_w = raw_w * 0.55
    line_x = raw_x + (raw_w - line_w) / 2
    ax.plot([line_x, line_x + line_w], [ly, ly],
            color='#D4CFC8', linewidth=0.4, zorder=4, alpha=0.5)

# ── Draw Stage 4: Condition boxes ────────────────────────────────────────────
conditions = [
    {
        'name': 'Exception Only', 'acc': '99.83%', 'star': True,
        'desc': 'Only exception/error events',
        'fill_top': '#FDF0D0', 'fill_bot': '#F7E0A0',
        'border': '#C89B00', 'border_w': 1.8,
        'accent': '#E5A70E', 'name_color': '#5D4037',
        'acc_color': '#C89B00', 'desc_color': '#7B6F63',
        'w': cond_w, 'h': cond_h_winner,
        'shadow_alpha': 0.16, 'glow': True,
    },
    {
        'name': 'VOTA', 'acc': '99.05%', 'star': False,
        'desc': 'Exception + assertion + loop summary',
        'fill_top': '#EBF5EB', 'fill_bot': '#D4E8D4',
        'border': '#7CB87A', 'border_w': 1.0,
        'accent': '#8BBF89', 'name_color': '#2E6B2E',
        'acc_color': '#5A9A58', 'desc_color': '#6B7B6B',
        'w': cond_w_normal, 'h': cond_h_normal,
        'shadow_alpha': 0.12, 'glow': False,
    },
    {
        'name': 'Full Trace', 'acc': '81.44%', 'star': False,
        'desc': 'Complete line-by-line execution',
        'fill_top': '#F5E8DD', 'fill_bot': '#E8D4C0',
        'border': '#C08050', 'border_w': 1.0,
        'accent': '#C49670', 'name_color': '#7A5530',
        'acc_color': '#B07040', 'desc_color': '#8B7B6B',
        'w': cond_w_normal, 'h': cond_h_normal,
        'shadow_alpha': 0.12, 'glow': False,
    },
    {
        'name': 'No Trace', 'acc': '75.13%', 'star': False,
        'desc': 'Source code only (baseline)',
        'fill_top': '#F2F2F2', 'fill_bot': '#E0E0E0',
        'border': '#AAAAAA', 'border_w': 0.8,
        'accent': '#B5B5B5', 'name_color': '#555555',
        'acc_color': '#888888', 'desc_color': '#888888',
        'w': cond_w_normal, 'h': cond_h_normal,
        'shadow_alpha': 0.10, 'glow': False,
        'linestyle': (0, (4, 3)),
    },
]

cond_centers = []  # (x_left, x_right, y_center) for arrows
for i, c in enumerate(conditions):
    bx = cond_x
    by = cond_ys[i]
    bw = c['w']
    bh = c['h']
    ls = c.get('linestyle', '-')

    # Glow effect for winner
    if c.get('glow'):
        glow_box = FancyBboxPatch(
            (bx - 0.03, by - 0.03), bw + 0.06, bh + 0.06,
            boxstyle="round,pad=0,rounding_size=0.1",
            facecolor='#F5C842', edgecolor='none',
            alpha=0.08, zorder=2
        )
        ax.add_patch(glow_box)

    draw_gradient_box(ax, bx, by, bw, bh,
                      c['fill_top'], c['fill_bot'], c['border'],
                      linewidth=c['border_w'], linestyle=ls,
                      shadow_alpha=c['shadow_alpha'])

    # Left accent bar
    draw_accent_bar(ax, bx + 0.04, by + 0.06, bh - 0.12,
                    accent_w, c['accent'])

    # Name text
    name_x = bx + 0.18
    name_y = by + bh / 2 + (0.08 if bh > 0.65 else 0.06)
    ax.text(name_x, name_y, c['name'],
            fontsize=10.5, fontweight='bold', color=c['name_color'],
            va='center', ha='left', zorder=5)

    # Star for winner
    if c['star']:
        star_x = name_x + len(c['name']) * 0.085 + 0.15
        ax.text(star_x, name_y + 0.01, '★', fontsize=11,
                color='#D4A017', va='center', ha='left', zorder=5)

    # Accuracy (right-aligned)
    acc_x = bx + bw - 0.15
    ax.text(acc_x, by + bh / 2, c['acc'],
            fontsize=12 if not c['star'] else 13,
            fontweight='bold', color=c['acc_color'],
            va='center', ha='right', zorder=5)

    # Description
    desc_y = by + bh / 2 - (0.16 if bh > 0.65 else 0.14)
    ax.text(name_x, desc_y, c['desc'],
            fontsize=7.5, color=c['desc_color'],
            va='center', ha='left', zorder=5)

    cond_centers.append((bx, bx + bw, by + bh / 2))

# ── Draw Stage 5: Model ──────────────────────────────────────────────────────
draw_gradient_box(ax, model_x, model_y, model_w, model_h,
                  '#F0ECF8', '#DDD5ED', '#9B8DC0', linewidth=1.0)
ax.text(model_x + model_w / 2, model_y + model_h / 2 + 0.1, 'SFT (LoRA)',
        fontsize=10.5, fontweight='bold', color='#4A3580',
        va='center', ha='center', zorder=5)
ax.text(model_x + model_w / 2, model_y + model_h / 2 - 0.12, '1.5B–13B params',
        fontsize=7.5, color='#8B7BA8', va='center', ha='center', zorder=5)

# ── Draw Stage 6: Output ─────────────────────────────────────────────────────
# Top half: Pass (green)
half_h = out_h / 2
draw_box(ax, out_x, out_y + half_h, out_w, half_h,
         '#E8F5E9', '#BDBDBD', linewidth=0.8, shadow=False, zorder=3)
# Bottom half: Fail (red)
draw_box(ax, out_x, out_y, out_w, half_h,
         '#FFEBEE', '#BDBDBD', linewidth=0.8, shadow=False, zorder=3)
# Outer border with shadow
draw_box(ax, out_x, out_y, out_w, out_h,
         'none', '#BDBDBD', linewidth=0.8, shadow=True, zorder=2)

# Divider line
ax.plot([out_x + 0.05, out_x + out_w - 0.05],
        [out_y + half_h, out_y + half_h],
        color='#BDBDBD', linewidth=0.6, zorder=4)

ax.text(out_x + out_w / 2, out_y + half_h + half_h / 2,
        '✓  Pass', fontsize=9, fontweight='bold',
        color='#2E7D32', va='center', ha='center', zorder=5)
ax.text(out_x + out_w / 2, out_y + half_h / 2,
        '✗  Fail', fontsize=9, fontweight='bold',
        color='#C62828', va='center', ha='center', zorder=5)

# Verdict label
ax.text(out_x + out_w / 2, out_y + out_h + 0.1, 'Verdict',
        fontsize=9.5, fontweight='bold', color='#555555',
        va='bottom', ha='center', zorder=5)

# ── Arrows ────────────────────────────────────────────────────────────────────
arrow_color = '#4A5568'
arrow_lw = 1.2

# Input → Execution (from center of input group)
inp_center_y = (inp_y_top + inp_h / 2 + inp_y_bot + inp_h / 2) / 2
draw_arrow(ax, (inp_x + inp_w, inp_center_y), (exe_x, exe_y + exe_h / 2),
           connectionstyle='arc3,rad=0.0', lw=arrow_lw)

# Execution → Raw Trace
draw_arrow(ax, (exe_x + exe_w, exe_y + exe_h / 2),
           (raw_x, raw_y + raw_h / 2),
           connectionstyle='arc3,rad=0.0', lw=arrow_lw)

# Raw Trace → 4 condition boxes (fan-out with curves)
raw_right = raw_x + raw_w
raw_mid_y = raw_y + raw_h / 2
for i, (cx_left, cx_right, cy) in enumerate(cond_centers):
    dy = cy - raw_mid_y
    rad = dy * 0.08  # curvature proportional to vertical distance
    rad = max(-0.3, min(0.3, rad))
    draw_arrow(ax, (raw_right, raw_mid_y), (cx_left, cy),
               connectionstyle=f'arc3,rad={-rad}', lw=arrow_lw)

# 4 condition boxes → Model (fan-in with curves)
for i, (cx_left, cx_right, cy) in enumerate(cond_centers):
    model_mid_y = model_y + model_h / 2
    dy = cy - model_mid_y
    rad = dy * 0.08
    rad = max(-0.3, min(0.3, rad))
    draw_arrow(ax, (cx_right, cy), (model_x, model_mid_y),
               connectionstyle=f'arc3,rad={rad}', lw=arrow_lw)

# Model → Output
draw_arrow(ax, (model_x + model_w, model_y + model_h / 2),
           (out_x, out_y + out_h / 2),
           connectionstyle='arc3,rad=0.0', lw=arrow_lw)

# ── Vertical annotation bar (right of condition boxes) ────────────────────────
bar_x = cond_x + cond_w + 0.15
bar_top = cond_ys[0] + cond_h_winner - 0.05
bar_bot = cond_ys[3] + 0.05
bar_w = 0.05

# Gradient bar
n_segments = 50
for j in range(n_segments):
    t = j / n_segments
    seg_y = bar_top - t * (bar_top - bar_bot)
    seg_h = (bar_top - bar_bot) / n_segments
    from matplotlib.colors import to_rgba
    c_top = np.array(to_rgba('#F5C842'))
    c_bot = np.array(to_rgba('#AAAAAA'))
    c = c_top * (1 - t) + c_bot * t
    rect = plt.Rectangle((bar_x, seg_y - seg_h), bar_w, seg_h,
                          facecolor=c, edgecolor='none', zorder=3)
    ax.add_patch(rect)

# Arrow tips and labels
ax.annotate('', xy=(bar_x + bar_w / 2, bar_top + 0.08),
            xytext=(bar_x + bar_w / 2, bar_top + 0.25),
            arrowprops=dict(arrowstyle='->', color='#C89B00',
                            lw=0.8, mutation_scale=8), zorder=5)
ax.text(bar_x + bar_w / 2, bar_top + 0.32, 'Info\ndensity',
        fontsize=6.5, fontweight='bold', color='#888888',
        va='bottom', ha='center', zorder=5, linespacing=0.9)

ax.annotate('', xy=(bar_x + bar_w / 2, bar_bot - 0.08),
            xytext=(bar_x + bar_w / 2, bar_bot - 0.25),
            arrowprops=dict(arrowstyle='->', color='#888888',
                            lw=0.8, mutation_scale=8), zorder=5)
ax.text(bar_x + bar_w / 2, bar_bot - 0.32, 'Accuracy',
        fontsize=6.5, fontweight='bold', color='#888888',
        va='top', ha='center', zorder=5)

# ── Bottom annotation ─────────────────────────────────────────────────────────
ann_y = 0.22
ax.text(7.0, ann_y,
        '←  Information density decreases   |   Accuracy increases  →',
        fontsize=8.5, fontstyle='italic', color='#7B8794',
        va='center', ha='center', zorder=5)

# ── Save ──────────────────────────────────────────────────────────────────────
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/figures/paper'
plt.savefig(f'{out_dir}/fig1_trace_overview_pb2.png',
            bbox_inches='tight', pad_inches=0.05, dpi=300, facecolor='white')

# Also save PDF
plt.savefig(f'{out_dir}/fig1_trace_overview.pdf',
            bbox_inches='tight', pad_inches=0.05, facecolor='white')
plt.close()
print("Done: fig1_trace_overview_pb2.png + fig1_trace_overview.pdf")
