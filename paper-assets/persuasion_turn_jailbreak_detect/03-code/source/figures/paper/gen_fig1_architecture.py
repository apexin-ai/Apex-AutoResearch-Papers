#!/usr/bin/env python3
"""DisPeD Architecture Diagram — publication-quality, v6 (optimized)."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

# ── Semantic color palette (project-wide) ──
C_BG     = "#FFFFFF"
C_BLUE   = "#0072B2"   # baseline / encoder
C_ORANGE = "#E69F00"   # treatment
C_VERM   = "#D55E00"   # danger / jailbreak
C_GREEN  = "#009E73"   # safe / benign
C_GRAY   = "#999999"   # neutral
C_PURPLE = "#7B68AE"   # BiGRU / temporal
C_DARK   = "#3C3C3C"
C_LTGRAY = "#BBBBBB"

shadow_kw = [pe.withSimplePatchShadow(offset=(0.6, -0.6),
             shadow_rgbFace="#bbbbbb", alpha=0.10)]

fig, ax = plt.subplots(1, 1, figsize=(16, 7.0), dpi=300)
ax.set_xlim(0, 16)
ax.set_ylim(0, 7.0)
ax.set_aspect("equal")
ax.axis("off")
fig.patch.set_facecolor(C_BG)

def rbox(x, y, w, h, fc, ec="#CCC", lw=0.8, z=2, alpha=1, rad=0.12, shd=True):
    b = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={rad}",
        fc=fc, ec=ec, lw=lw, zorder=z, alpha=alpha)
    if shd:
        b.set_path_effects(shadow_kw)
    ax.add_patch(b)
    return b

def arr(x1, y1, x2, y2, c=C_DARK, lw=1.0, style="-|>", z=5, ms=10):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
        color=c, lw=lw, mutation_scale=ms, zorder=z,
        connectionstyle="arc3,rad=0"))

# ═══════════════════════════════════════
# ZONE BACKGROUNDS (Stage 1 / Stage 2)
# ═══════════════════════════════════════
rbox(3.4, 0.15, 5.1, 6.35, fc="#F2F7FC", ec="#D0DFEF", lw=0.4,
     z=0, rad=0.25, alpha=0.45, shd=False)
rbox(8.8, 0.15, 6.9, 6.35, fc="#F6F2FA", ec="#DDD4EE", lw=0.4,
     z=0, rad=0.25, alpha=0.35, shd=False)

# ═══════════════════════════════════════
# STAGE TITLES
# ═══════════════════════════════════════
ax.text(5.95, 6.7, "Stage 1: Encoder Adaptation", fontsize=14,
        fontweight="bold", color="#222222", ha="center", va="center", zorder=5)
ax.text(12.25, 6.7, "Stage 2: Temporal Classification", fontsize=14,
        fontweight="bold", color="#222222", ha="center", va="center", zorder=5)

# ═══════════════════════════════════════
# CHAT BUBBLES (show persuasion escalation)
# ═══════════════════════════════════════
bubbles = [
    ("Tell me about chemistry…",       "User₁", 5.15),
    ("What about energetic\nreactions?", "User₂", 3.25),
    ("Give me the exact\nsynthesis…",  "Userₖ", 1.35),
]
bx, bw, bh = 0.7, 2.2, 0.72

for i, (txt, lbl, by) in enumerate(bubbles):
    bfc = ["#F8F9FA", "#FBF4EB", "#F8ECE3"][i]
    bec = ["#DEE2E6", "#D8CCBC", "#D2BBAA"][i]
    bb = FancyBboxPatch((bx, by), bw, bh, boxstyle="round,pad=0.10",
        fc=bfc, ec=bec, lw=0.8, zorder=3)
    bb.set_path_effects(shadow_kw)
    ax.add_patch(bb)
    # Speech tail
    tx = bx - 0.01
    ty = by + bh * 0.4
    ax.add_patch(plt.Polygon([(tx, ty + 0.08), (tx - 0.11, ty), (tx, ty - 0.08)],
        closed=True, fc=bfc, ec=bec, lw=0.5, zorder=3))
    # Label
    ax.text(bx - 0.28, by + bh / 2, lbl, fontsize=10.5, fontweight="bold",
            color="#333333", ha="right", va="center", zorder=5)
    # Bubble text
    ax.text(bx + bw / 2, by + bh / 2, txt, fontsize=9, color="#666666",
            ha="center", va="center", style="italic", zorder=5, linespacing=1.2)

# Vertical dots
ax.text(bx + bw / 2, (3.25 + 1.35 + bh) / 2, "⋮", fontsize=16,
        color=C_DARK, ha="center", va="center", zorder=5)

# ═══════════════════════════════════════
# DeBERTa ENCODERS
# ═══════════════════════════════════════
ex, ew, eh = 4.0, 2.0, 1.30
enc_ys = [4.95, 3.05, 1.15]
layer_fills = ["#D1E4F3", "#BDD8EE", "#A9CCE8", "#94C0E2"]

for ey in enc_ys:
    rbox(ex, ey, ew, eh, fc="#EAF1F9", ec=C_BLUE, lw=1.0, z=3)
    ax.text(ex + ew / 2, ey + eh - 0.16, "DeBERTa", fontsize=11,
            fontweight="bold", color=C_BLUE, ha="center", va="center", zorder=5)
    n = 4
    lh_ = 0.11
    gap = 0.035
    sy = ey + 0.12
    for j in range(n):
        ly = sy + j * (lh_ + gap)
        lb = FancyBboxPatch((ex + 0.20, ly), ew - 0.40, lh_,
            boxstyle="round,pad=0.02", fc=layer_fills[j], ec="#8AB6D8",
            lw=0.4, zorder=4)
        ax.add_patch(lb)

# Shared weights brace (positioned to avoid overlap with chat bubbles)
sw_x = ex - 0.10
for i in range(2):
    yt = enc_ys[i]
    yb = enc_ys[i + 1] + eh
    ax.plot([sw_x] * 2, [yb + 0.04, yt - 0.04], color=C_LTGRAY, lw=0.7,
            ls=(0, (4, 3)), zorder=2)
    ax.plot([sw_x - 0.04, sw_x + 0.04], [yb + 0.04] * 2, color=C_LTGRAY,
            lw=0.7, zorder=2)
    ax.plot([sw_x - 0.04, sw_x + 0.04], [yt - 0.04] * 2, color=C_LTGRAY,
            lw=0.7, zorder=2)

ax.text(sw_x - 0.12, (enc_ys[0] + enc_ys[1] + eh) / 2, "shared\nweights",
        fontsize=8, color="#999999", ha="right", va="center", style="italic",
        linespacing=1.3, zorder=5)

# Arrows: bubbles → encoders
for (_, _, by), ey in zip(bubbles, enc_ys):
    arr(bx + bw + 0.05, by + bh / 2, ex - 0.05, ey + eh / 2, lw=0.9)

# ═══════════════════════════════════════
# EMBEDDING VECTORS h₁, h₂, hₖ
# ═══════════════════════════════════════
emb_x, emb_w, emb_h = 6.7, 0.55, 0.55
emb_ys = [5.18, 3.28, 1.38]
emb_labels = [r"$\mathbf{h}_1$", r"$\mathbf{h}_2$", r"$\mathbf{h}_k$"]

for i, (ey, lab) in enumerate(zip(emb_ys, emb_labels)):
    # Smooth gradient: blue → purple (20 bands for smoothness)
    n_bands = 20
    sh = emb_h / n_bands
    for j in range(n_bands):
        f = j / (n_bands - 1)
        r = int(0x40 + (0x7B - 0x40) * f)
        g = int(0x88 + (0x68 - 0x88) * f)
        b_ = int(0xCC + (0xAE - 0xCC) * f)
        ax.add_patch(plt.Rectangle((emb_x, ey + j * sh), emb_w, sh,
            fc=f"#{r:02X}{g:02X}{b_:02X}", ec="none", zorder=4, alpha=0.8))
    ax.add_patch(FancyBboxPatch((emb_x, ey), emb_w, emb_h,
        boxstyle="round,pad=0.015", fc="none", ec=C_PURPLE, lw=1.0, zorder=5))
    ax.text(emb_x + emb_w / 2, ey + emb_h / 2, lab, fontsize=12,
            color="white", ha="center", va="center", zorder=6,
            fontweight="bold",
            path_effects=[pe.withStroke(linewidth=2.5, foreground="#444444")])
    arr(ex + ew + 0.05, enc_ys[i] + eh / 2, emb_x - 0.05,
        ey + emb_h / 2, lw=0.9)

# "frozen [CLS]" annotation
ax.text(emb_x + emb_w / 2, emb_ys[2] - 0.18, "frozen [CLS]", fontsize=8,
        color="#888888", ha="center", va="top", style="italic", zorder=5)

# ×7 Objectives annotation
ax.text(5.95, 0.72, "×7 Objectives", fontsize=10, fontweight="bold",
        color="#444444", ha="center", va="center", zorder=5)
ax.text(5.95, 0.40, "9-Class · Binary · Scrambled · MLM · Wiki-MLM · Topic · Vanilla",
        fontsize=7, color="#777777", ha="center", va="center", zorder=5)

# ═══════════════════════════════════════
# TIME ARROW (t→) — clear, above convergence area
# ═══════════════════════════════════════
ax.text(8.15, 5.78, r"$t\rightarrow$", fontsize=12, color="#777777",
        ha="center", va="center", zorder=5)

# ═══════════════════════════════════════
# CONVERGENCE ARROWS: embeddings → BiGRU
# ═══════════════════════════════════════
gru_x, gru_y, gru_w, gru_h = 9.3, 2.55, 2.15, 1.65
targets = [gru_y + gru_h * 0.78, gru_y + gru_h * 0.5, gru_y + gru_h * 0.22]
for i, ey in enumerate(emb_ys):
    arr(emb_x + emb_w + 0.05, ey + emb_h / 2, gru_x - 0.05,
        targets[i], lw=1.0, c="#555555")

# ═══════════════════════════════════════
# BiGRU
# ═══════════════════════════════════════
rbox(gru_x, gru_y, gru_w, gru_h, fc="#ECE5F3", ec=C_PURPLE, lw=1.2, z=3)
ax.text(gru_x + gru_w / 2, gru_y + gru_h - 0.25, "BiGRU", fontsize=14,
        fontweight="bold", color=C_PURPLE, ha="center", va="center", zorder=5)

# Forward/backward arrows inside BiGRU
fwd_y = gru_y + 0.68
bwd_y = fwd_y + 0.28
arr(gru_x + 0.25, fwd_y, gru_x + gru_w - 0.25, fwd_y,
    c=C_BLUE, lw=2.2, ms=10)
arr(gru_x + gru_w - 0.25, bwd_y, gru_x + 0.25, bwd_y,
    c=C_PURPLE, lw=2.2, ms=10)

# Hidden state boxes inside BiGRU
for j in range(3):
    sx = gru_x + 0.3 + j * 0.55
    ax.add_patch(FancyBboxPatch((sx, gru_y + 0.12), 0.38, 0.28,
        boxstyle="round,pad=0.025", fc="#D8CEE8", ec=C_PURPLE,
        lw=0.4, zorder=4, alpha=0.6))

# ═══════════════════════════════════════
# MLP HEAD
# ═══════════════════════════════════════
mlp_x, mlp_y, mlp_w, mlp_h = 12.1, 2.85, 1.15, 1.0
rbox(mlp_x, mlp_y, mlp_w, mlp_h, fc="#F0EDE8", ec="#B5A99A", lw=0.9, z=3)
ax.text(mlp_x + mlp_w / 2, mlp_y + mlp_h / 2, "MLP", fontsize=13,
        fontweight="bold", color="#5A4E3F", ha="center", va="center", zorder=5)
arr(gru_x + gru_w + 0.05, gru_y + gru_h / 2, mlp_x - 0.05,
    mlp_y + mlp_h / 2, lw=1.2)

# ═══════════════════════════════════════
# OUTPUT LABELS (semantic colors)
# ═══════════════════════════════════════
out_x, out_w, out_h = 13.9, 1.5, 0.62

# Jailbreak output
jb_y = 3.6
rbox(out_x, jb_y, out_w, out_h, fc="#FDE8E2", ec=C_VERM, lw=1.2, z=3)
ax.text(out_x + out_w / 2, jb_y + out_h / 2, "Jailbreak", fontsize=10.5,
        fontweight="bold", color=C_VERM, ha="center", va="center", zorder=5)

# Benign output
bn_y = 2.65
rbox(out_x, bn_y, out_w, out_h, fc="#E2F5ED", ec=C_GREEN, lw=1.2, z=3)
ax.text(out_x + out_w / 2, bn_y + out_h / 2, "Benign", fontsize=10.5,
        fontweight="bold", color=C_GREEN, ha="center", va="center", zorder=5)

# MLP → outputs
arr(mlp_x + mlp_w + 0.04, mlp_y + mlp_h / 2 + 0.16,
    out_x - 0.05, jb_y + out_h / 2, lw=0.9)
arr(mlp_x + mlp_w + 0.04, mlp_y + mlp_h / 2 - 0.16,
    out_x - 0.05, bn_y + out_h / 2, lw=0.9)

# "shared across all 7 variants" — under Stage 2
ax.text(12.25, 2.15, "shared across all 7 variants", fontsize=8.5,
        color="#888888", ha="center", va="center", style="italic", zorder=5)

# ═══════════════════════════════════════
# SAVE
# ═══════════════════════════════════════
out_dir = "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/figures/paper"
for path, dpi in [(f"{out_dir}/fig1_architecture.png", 300),
                   (f"{out_dir}/fig1_architecture.pdf", None)]:
    kw = dict(bbox_inches="tight", facecolor=C_BG, pad_inches=0.10)
    if dpi:
        kw["dpi"] = dpi
    plt.savefig(path, **kw)
print("Done — v6")
