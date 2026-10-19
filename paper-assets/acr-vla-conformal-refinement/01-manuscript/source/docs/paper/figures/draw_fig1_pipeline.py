#!/usr/bin/env python3
"""Figure 1: Calibrated Gating Pipeline."""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "mathtext.fontset": "cm",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "text.color": "#333333",
})

fig = plt.figure(figsize=(14, 5.5), dpi=300)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(-0.2, 16.6)
ax.set_ylim(-3.6, 3.6)
ax.axis("off")

# ── palette ───────────────────────────────────────────────────
GF, GB   = "#F2F2F2", "#7F8C8D"
OF, OB   = "#FFF4E0", "#E69F00"
PF, PB   = "#F0EAF5", "#8B6BAE"
GNF, GNB = "#E8F6EF", "#1E8449"
RED, BLU = "#A93226", "#1A5276"
PKF, LBF = "#FADBD8", "#D4E6F1"
DK, ARR  = "#2C3E50", "#B0B0B0"

# ── helpers ───────────────────────────────────────────────────
def box(cx, cy, w, h, fc, ec, lw=1.2, texts=(), pad=0.10):
    x0, y0 = cx - w/2, cy - h/2
    # shadow
    ax.add_patch(FancyBboxPatch(
        (x0 + 0.04, y0 - 0.04), w, h,
        boxstyle=f"round,pad={pad}", fc="#00000009", ec="none", zorder=1))
    # main box
    ax.add_patch(FancyBboxPatch(
        (x0, y0), w, h,
        boxstyle=f"round,pad={pad}", fc=fc, ec=ec, lw=lw, zorder=2))
    for dy, txt, kw in texts:
        ax.text(cx, cy + dy, txt, ha="center", va="center", zorder=3, **kw)

def arrow(x1, y1, x2, y2, c=ARR, lw=1.0, ms=11):
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2), arrowstyle="-|>",
        mutation_scale=ms, color=c, lw=lw, zorder=2))

def sub(cx, y, txt, **kw):
    ax.text(cx, y, txt, ha="center", va="center", fontsize=9.5,
            fontstyle="italic", zorder=3, **kw)

# ═══════════════════════════════════════════════════════════════
#  MAIN PIPELINE  (y = 0)
# ═══════════════════════════════════════════════════════════════

# 1. O_t
ax.add_patch(plt.Circle((0.5, 0), 0.38, fc="#F0F0F0", ec="#666666",
                         lw=0.9, zorder=2))
ax.text(0.5, 0, r"$O_t$", ha="center", va="center", fontsize=13,
        fontweight="bold", fontstyle="italic", zorder=3)
sub(0.5, -0.6, "observation", color="#999999")
arrow(0.88, 0, 1.22, 0)

# 2. Frozen VLA
box(2.15, 0, 1.65, 1.0, GF, GB, texts=[
    ( 0.2,  "Frozen VLA",      dict(fontsize=12, fontweight="bold")),
    (-0.16, "(SmolVLA 0.4B)",  dict(fontsize=10, color="#666666")),
])
sub(2.15, -0.75, "~170 ms", color=GB)
arrow(3.08, 0, 3.38, 0)

# 3. K=2 Samples
box(4.25, 0, 1.55, 1.0, OF, OB, texts=[
    ( 0.2,  "K = 2 Samples",  dict(fontsize=10.5)),
    (-0.18, r"$\mathbf{a}^1,\ \mathbf{a}^2$",  dict(fontsize=11)),
])
sub(4.25, -0.75, "batched (shared pass)", color=OB)
arrow(5.13, 0, 5.43, 0)

# 4. Compute d₂
box(6.35, 0, 1.65, 1.0, PF, PB, texts=[
    ( 0.2,  "Compute",  dict(fontsize=10.5)),
    (-0.18, r"$d_2 = \|\mathbf{a}^1 - \mathbf{a}^2\|_2$",  dict(fontsize=9.5)),
])
arrow(7.28, 0, 7.58, 0)

# 5. Diamond
dcx = 8.35
dr  = 0.52
verts = np.array([
    [dcx,      dr*1.2],
    [dcx+dr,   0],
    [dcx,     -dr*1.2],
    [dcx-dr,   0],
    [dcx,      dr*1.2],
])
sv = verts.copy(); sv[:,0] += 0.03; sv[:,1] -= 0.03
ax.fill(sv[:,0], sv[:,1], fc="#00000009", ec="none", zorder=1)
ax.fill(verts[:,0], verts[:,1], fc=GNF, ec=GNB, lw=1.4, zorder=2)
ax.text(dcx, 0.03, r"$d_2 > \tau\,$?", ha="center", va="center",
        fontsize=10.5, fontweight="bold", color=GNB, zorder=3)

# ═══════════════════════════════════════════════════════════════
#  HARD PATH  (y ~ +2)
# ═══════════════════════════════════════════════════════════════
hy = 2.05
# Panel background
hp_left = 10.0
hp_w, hp_h = 6.35, 2.15
hp_bottom = hy - hp_h/2 - 0.08
ax.add_patch(FancyBboxPatch(
    (hp_left, hp_bottom), hp_w, hp_h,
    boxstyle="round,pad=0.12", fc="#FADBD818", ec=RED,
    lw=1.1, ls=(0, (5, 3)), zorder=0.5))
ax.text(hp_left + hp_w/2, hp_bottom + hp_h - 0.22,
        "Hard Path · Refine", ha="center", fontsize=11.5,
        fontweight="bold", fontstyle="italic", color=RED, zorder=3)

# Elbow arrow
line_x = 9.3
ax.plot([dcx + 0.28, line_x, line_x],
        [0.45, hy, hy],
        color=RED, lw=1.1, solid_capstyle="round", zorder=2)
arrow(line_x, hy, hp_left + 0.15, hy, c=RED, lw=1.1)

# Labels — left of the vertical line
ax.text(line_x - 0.6, 1.05, "Yes", ha="right", fontsize=11,
        fontweight="bold", fontstyle="italic", color=RED)
ax.text(line_x - 0.6, 0.7, "(~3–20%)", ha="right", fontsize=10,
        color="#999999")

# Boxes inside hard path
box(10.85, hy, 1.15, 0.85, PKF, RED, texts=[
    ( 0.1,  "Argmin", dict(fontsize=10, color="#333")),
    (-0.13, "Select", dict(fontsize=10, color="#333")),
])
arrow(11.53, hy, 11.9, hy, c=RED, lw=0.9)

box(12.75, hy, 1.5, 0.95, LBF, BLU, lw=1.7, texts=[
    ( 0.15, "CRM",        dict(fontsize=12, fontweight="bold", color="#1A1A1A")),
    (-0.15, "Correction", dict(fontsize=12, fontweight="bold", color="#1A1A1A")),
])
sub(12.75, hy - 0.72, "~327K params, +0.25 ms", color=BLU)
arrow(13.62, hy, 14.0, hy, c=RED, lw=0.9)

box(14.75, hy, 1.05, 0.85, DK, RED, texts=[
    ( 0.1,  r"$a^*$",   dict(fontsize=11, fontweight="bold", color="white")),
    (-0.13, "Execute",  dict(fontsize=9.5, fontweight="bold", color="white")),
])

# ═══════════════════════════════════════════════════════════════
#  EASY PATH  (y ~ -2)
# ═══════════════════════════════════════════════════════════════
ey = -2.05
ep_left = 10.0
ep_w, ep_h = 6.35, 2.0
ep_bottom = ey - ep_h/2 + 0.08
ax.add_patch(FancyBboxPatch(
    (ep_left, ep_bottom), ep_w, ep_h,
    boxstyle="round,pad=0.12", fc="#D4E6F118", ec=BLU,
    lw=1.1, ls=(0, (5, 3)), zorder=0.5))
ax.text(ep_left + ep_w/2, ep_bottom + 0.22,
        "Easy Path · Direct", ha="center", fontsize=11.5,
        fontweight="bold", fontstyle="italic", color=BLU, zorder=3)

# Elbow arrow
ax.plot([dcx + 0.28, line_x, line_x],
        [-0.45, ey, ey],
        color=BLU, lw=1.1, solid_capstyle="round", zorder=2)
arrow(line_x, ey, ep_left + 0.15, ey, c=BLU, lw=1.1)

# Labels
ax.text(line_x - 0.6, -1.05, "No", ha="right", fontsize=11,
        fontweight="bold", fontstyle="italic", color=BLU)
ax.text(line_x - 0.6, -1.4, "(~80–97%)", ha="right", fontsize=10,
        color="#999999")

# Boxes inside easy path
box(11.5, ey, 1.15, 0.85, LBF, BLU, texts=[
    ( 0.1,  "Argmin", dict(fontsize=10, color="#333")),
    (-0.13, "Select", dict(fontsize=10, color="#333")),
])
arrow(12.18, ey, 13.55, ey, c=BLU, lw=0.9)

box(14.3, ey, 1.05, 0.85, DK, BLU, texts=[
    ( 0.1,  r"$a^*$",   dict(fontsize=11, fontweight="bold", color="white")),
    (-0.13, "Execute",  dict(fontsize=9.5, fontweight="bold", color="white")),
])

# ═══════════════════════════════════════════════════════════════
out = os.path.dirname(os.path.abspath(__file__))
for ext in ("png", "pdf"):
    plt.savefig(os.path.join(out, f"fig1_pipeline.{ext}"), dpi=300, bbox_inches="tight",
                pad_inches=0.08, facecolor="white", edgecolor="none")
plt.close()
print("Saved PNG + PDF")
