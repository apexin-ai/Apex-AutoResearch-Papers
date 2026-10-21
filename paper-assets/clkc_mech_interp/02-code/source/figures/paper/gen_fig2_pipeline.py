#!/usr/bin/env python3
"""Figure 2: Method Pipeline — single-row horizontal flow (Nature Methods style)"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon
import numpy as np
import os

# ─── Color Palette ───
NAVY      = '#1B2838'
SLATE     = '#3D5A80'
TEAL      = '#5BA4B5'
TEAL_LT   = '#E6F4F7'
CORAL     = '#E07A5F'
EN_BLUE   = '#4A90D9'
ZH_RED    = '#E07A5F'
BG_LIGHT  = '#F8F9FA'
BORDER    = '#CBD5E0'
TEXT_BODY  = '#2D3748'
TEXT_SUB   = '#5A6B7F'
WHITE     = '#FFFFFF'
ARROW_CLR = '#BDC3C7'

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Liberation Serif'],
    'mathtext.fontset': 'dejavuserif',
    'axes.unicode_minus': False,
})

FW, FH = 14, 3.0
fig, ax = plt.subplots(1, 1, figsize=(FW, FH), dpi=300)
ax.set_xlim(0, FW)
ax.set_ylim(0, FH)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor(WHITE)

# ─── Layout ───
BOX_W = 2.6
BOX_H = 2.2
GAP = 1.07
LEFT_MARGIN = (FW - 4 * BOX_W - 3 * GAP) / 2
BOX_Y = (FH - BOX_H) / 2

def box_x(i):
    return LEFT_MARGIN + i * (BOX_W + GAP)

# ─── Helpers ───

def shadow(ax, x, y, w, h, r=0.12):
    for dx, dy, c in [(0.04, -0.04, '#00000010'), (0.02, -0.02, '#00000008')]:
        ax.add_patch(FancyBboxPatch((x+dx, y+dy), w, h,
            boxstyle=f"round,pad=0,rounding_size={r}",
            facecolor=c, edgecolor='none', zorder=1))

def step_box(ax, i, main_text, section):
    x = box_x(i)
    y = BOX_Y
    shadow(ax, x, y, BOX_W, BOX_H)
    ax.add_patch(FancyBboxPatch((x, y), BOX_W, BOX_H,
        boxstyle="round,pad=0,rounding_size=0.12",
        facecolor=WHITE, edgecolor=BORDER, linewidth=0.7, zorder=2))

    ax.plot([x + 0.20, x + BOX_W - 0.20], [y + BOX_H - 0.06, y + BOX_H - 0.06],
            color=TEAL, lw=1.5, alpha=0.4, solid_capstyle='round', zorder=3)

    badge_r = 0.15
    badge_cx = x + 0.30
    badge_cy = y + BOX_H - 0.30
    ax.add_patch(Circle((badge_cx, badge_cy), badge_r,
        facecolor=SLATE, edgecolor='none', zorder=5))
    ax.text(badge_cx, badge_cy, str(i+1), ha='center', va='center',
            fontsize=7.5, fontweight='bold', color=WHITE, zorder=6)

    text_y = y + 0.52
    ax.text(x + BOX_W/2, text_y, main_text, ha='center', va='center',
            fontsize=8.8, fontweight='bold', color=NAVY, zorder=5,
            linespacing=1.35)

    ax.text(x + BOX_W/2, y + 0.17, section, ha='center', va='center',
            fontsize=8, color=TEXT_SUB, fontstyle='italic', zorder=5)

# ─── Icon Drawing Functions ───

def draw_doc_icon(ax, cx, cy):
    s = 1.25
    dw, dh = 0.42 * s, 0.55 * s
    off = 0.18 * s

    bx, by = cx - dw/2 + off, cy - dh/2 - off*0.25
    ax.add_patch(FancyBboxPatch((bx, by), dw, dh,
        boxstyle="round,pad=0,rounding_size=0.06",
        facecolor=ZH_RED, edgecolor='none', linewidth=0, alpha=0.80, zorder=3.5))
    for frac in [0.72, 0.52, 0.32]:
        ly = by + dh * frac
        ax.plot([bx + 0.08, bx + dw - 0.08], [ly, ly],
                color=WHITE, lw=0.8, alpha=0.45, zorder=3.6)
    ax.text(bx + dw - 0.13, by + 0.12, 'ZH', fontsize=5.5, color=WHITE,
            fontweight='bold', ha='center', va='center', zorder=3.7, alpha=0.7)

    fx, fy = cx - dw/2 - off, cy - dh/2 + off*0.25
    ax.add_patch(FancyBboxPatch((fx, fy), dw, dh,
        boxstyle="round,pad=0,rounding_size=0.06",
        facecolor=EN_BLUE, edgecolor='none', linewidth=0, alpha=0.88, zorder=3.8))
    for frac in [0.72, 0.52, 0.32]:
        ly = fy + dh * frac
        ax.plot([fx + 0.08, fx + dw - 0.08], [ly, ly],
                color=WHITE, lw=0.8, alpha=0.50, zorder=3.9)
    ax.text(fx + dw - 0.13, fy + 0.12, 'EN', fontsize=5.5, color=WHITE,
            fontweight='bold', ha='center', va='center', zorder=4.0, alpha=0.85)

def draw_probe_icon(ax, cx, cy):
    s = 1.2
    n_layers = 5
    layer_w = 0.52 * s
    layer_spacing = 0.115 * s
    total_h = (n_layers - 1) * layer_spacing
    y_start = cy - total_h / 2

    for i in range(n_layers):
        ly = y_start + i * layer_spacing
        alpha = 0.22 + 0.13 * i
        ax.plot([cx - layer_w/2, cx + layer_w/2 - 0.15], [ly, ly],
                color=SLATE, lw=2.5, alpha=alpha, zorder=3.5,
                solid_capstyle='round')

    mg_cx = cx + layer_w/2 - 0.04
    mg_cy = cy + 0.12
    mg_r = 0.20
    ax.add_patch(Circle((mg_cx, mg_cy), mg_r,
        facecolor=TEAL_LT, edgecolor=TEAL, linewidth=2.0, zorder=4, alpha=0.9))
    hx = mg_cx + mg_r * 0.707
    hy = mg_cy - mg_r * 0.707
    ax.plot([hx, hx + 0.17], [hy, hy - 0.17],
            color=TEAL, lw=2.5, solid_capstyle='round', zorder=4)
    ax.plot(mg_cx, mg_cy, 'o', color=TEAL, markersize=2.5, zorder=4.5)

def draw_steer_icon(ax, cx, cy):
    """Layer tower with red direction vector injection — matches Fig1(c)"""
    n_layers = 4
    lw_u = 0.75
    lh_u = 0.14
    gap = 0.05
    total_h = n_layers * lh_u + (n_layers - 1) * gap
    y_start = cy - total_h / 2

    inject_idx = 2

    # Light gray background for the tower
    bg_pad = 0.06
    ax.add_patch(FancyBboxPatch(
        (cx - lw_u/2 - bg_pad, y_start - bg_pad),
        lw_u + 2*bg_pad, total_h + 2*bg_pad,
        boxstyle="round,pad=0,rounding_size=0.05",
        facecolor='#F0F4F8', edgecolor=BORDER, linewidth=0.5, zorder=3.2))

    for i in range(n_layers):
        ly = y_start + i * (lh_u + gap)
        is_inj = (i == inject_idx)
        fc = '#FADBD8' if is_inj else WHITE
        ec = CORAL if is_inj else '#D0D8E0'
        lw = 1.5 if is_inj else 0.6
        ax.add_patch(FancyBboxPatch(
            (cx - lw_u/2, ly), lw_u, lh_u,
            boxstyle="round,pad=0,rounding_size=0.03",
            facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3.5))

    # Red injection arrow — prominent
    inj_y = y_start + inject_idx * (lh_u + gap) + lh_u / 2
    ax.add_patch(FancyArrowPatch(
        (cx - lw_u/2 - 0.50, inj_y),
        (cx - lw_u/2 + 0.03, inj_y),
        arrowstyle='-|>', color=CORAL, lw=2.8,
        mutation_scale=16, zorder=4.5))

def draw_shield_icon(ax, cx, cy):
    s = 1.2
    sw, sh = 0.50 * s, 0.60 * s
    n = 40
    top_y = cy + sh * 0.38
    mid_y = cy - sh * 0.05
    bot_y = cy - sh * 0.42

    left_pts = []
    for t in np.linspace(0, 1, n//2):
        x = cx - sw/2 * (1 - 0.15 * t**2)
        y = top_y - (top_y - mid_y) * t
        left_pts.append([x, y])
    for t in np.linspace(0, 1, n//4):
        x = cx - sw/2 * (1 - t) * (1 - 0.15)
        y = mid_y - (mid_y - bot_y) * t
        left_pts.append([x, y])

    right_pts = [[2*cx - p[0], p[1]] for p in reversed(left_pts)]
    pts = np.array(left_pts + right_pts)

    shield = Polygon(pts, closed=True, facecolor=TEAL, edgecolor=SLATE,
                     linewidth=1.0, alpha=0.85, zorder=3.8)
    ax.add_patch(shield)

    inner_pts = pts.copy()
    inner_pts[:, 0] = cx + (inner_pts[:, 0] - cx) * 0.72
    inner_pts[:, 1] = cy + (inner_pts[:, 1] - cy) * 0.72
    shield_inner = Polygon(inner_pts, closed=True, facecolor='#7FC4D3',
                           edgecolor='none', linewidth=0, alpha=0.35, zorder=3.9)
    ax.add_patch(shield_inner)

    ck_x = [cx - 0.12, cx - 0.03, cx + 0.15]
    ck_y = [cy - 0.02, cy - 0.12, cy + 0.10]
    ax.plot(ck_x, ck_y, color=WHITE, lw=2.5, solid_capstyle='round',
            solid_joinstyle='round', zorder=5)

# ─── Draw Steps ───

steps = [
    ("ConflictQA\n+ Translation", "§3.2"),
    ("4-Direction\nProbe Training", "§3.4"),
    ("Representation\nSteering", "§3.5"),
    ("Confound\nExclusion", "§3.6"),
]

icon_funcs = [draw_doc_icon, draw_probe_icon, draw_steer_icon, draw_shield_icon]

for i, ((main, sec), icon_fn) in enumerate(zip(steps, icon_funcs)):
    step_box(ax, i, main, sec)
    x = box_x(i)
    icon_cx = x + BOX_W / 2
    icon_cy = BOX_Y + BOX_H - 0.80
    if i == 3:
        icon_fn(ax, icon_cx - 0.22, icon_cy)
    else:
        icon_fn(ax, icon_cx, icon_cy)

# Step 4: COMET / XNLI pill labels beside shield
x4 = box_x(3)
shield_cx = x4 + BOX_W / 2 - 0.22
lbl_x = shield_cx + 0.42
lbl_cy = BOX_Y + BOX_H - 0.80
for dy, txt in [(0.14, 'COMET'), (-0.10, 'XNLI')]:
    tw, th = 0.42, 0.12
    py = lbl_cy + dy
    ax.add_patch(FancyBboxPatch(
        (lbl_x, py - th/2), tw, th,
        boxstyle=f"round,pad=0,rounding_size={th/2}",
        facecolor=TEAL_LT, edgecolor=TEAL, linewidth=0.5, zorder=4))
    ax.text(lbl_x + tw/2, py, txt,
            fontsize=6, color=SLATE, fontweight='bold',
            ha='center', va='center', zorder=5)

# ─── Connecting Arrows — solid, light gray, small arrowheads ───

for i in range(3):
    x1 = box_x(i) + BOX_W
    x2 = box_x(i + 1)
    ay = BOX_Y + BOX_H / 2

    ax.plot([x1 + 0.08, x2 - 0.22], [ay, ay],
            color=ARROW_CLR, lw=1.0, zorder=9)
    ax.add_patch(FancyArrowPatch(
        (x2 - 0.28, ay), (x2 - 0.06, ay),
        arrowstyle='-|>', color=ARROW_CLR, lw=1.0,
        mutation_scale=10, zorder=10))

# ─── Save ───
os.makedirs('figures/paper', exist_ok=True)
out_base = 'figures/paper/fig2_pipeline'
for ext in ['png', 'pdf']:
    plt.savefig(f'{out_base}.{ext}', dpi=300,
                bbox_inches='tight', pad_inches=0.05, facecolor=WHITE)
plt.close()
print(f"Saved {out_base}.png and {out_base}.pdf")
