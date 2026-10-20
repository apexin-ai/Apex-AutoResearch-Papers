import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "fig1_framework.png")
OUTPUT_PDF = os.path.join(OUTPUT_DIR, "fig1_framework.pdf")

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['mathtext.fontset'] = 'dejavusans'

C_PANEL = "#F5F5F5"
C_BLUE_LIGHT = "#D6E8F7"
C_BLUE = "#4A90D9"
C_BLUE_DARK = "#1B5E9E"
C_ORANGE_LIGHT = "#FDE8D0"
C_ORANGE = "#E8913A"
C_ORANGE_DARK = "#B85C00"
C_TEXT = "#2D2D2D"
C_GRAY = "#666666"
C_GREEN = "#4CAF50"
C_RED = "#E57373"
C_WHITE = "#FFFFFF"

fig, ax = plt.subplots(1, 1, figsize=(17, 6.5))
ax.set_xlim(0, 17)
ax.set_ylim(0, 6.5)
ax.set_aspect('equal')
ax.axis('off')

def draw_box(x, y, w, h, fc, ec='#CCCCCC', label='', fontsize=10,
             fontcolor=C_TEXT, bold=False, zorder=3, alpha=1.0, ls='-',
             lw=0.8, va_offset=0):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                         facecolor=fc, edgecolor=ec, linewidth=lw,
                         zorder=zorder, alpha=alpha, linestyle=ls)
    ax.add_patch(box)
    if label:
        fw = 'bold' if bold else 'normal'
        ax.text(x + w/2, y + h/2 + va_offset, label, ha='center', va='center',
                fontsize=fontsize, color=fontcolor, fontweight=fw, zorder=zorder+1)
    return box

def draw_arrow(x1, y1, x2, y2, color=C_GRAY, lw=1.2, style='->',
               ls='-', zorder=5, shrinkA=2, shrinkB=2, connectionstyle=None):
    kw = {}
    if connectionstyle:
        kw['connectionstyle'] = connectionstyle
    arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                            color=color, lw=lw, mutation_scale=12,
                            zorder=zorder, linestyle=ls,
                            shrinkA=shrinkA, shrinkB=shrinkB, **kw)
    ax.add_patch(arrow)
    return arrow

# ===== PANEL 1: Schema Compilation =====
p1_x, p1_y, p1_w, p1_h = 0.3, 0.3, 5.0, 5.9
draw_box(p1_x, p1_y, p1_w, p1_h, C_PANEL, ec='#DDDDDD', zorder=1)
ax.text(p1_x + p1_w/2, 6.05, "Schema Compilation", ha='center', va='center',
        fontsize=12, fontweight='bold', color=C_TEXT, zorder=6)
ax.text(p1_x + p1_w/2, 5.72, "offline, once per schema", ha='center', va='center',
        fontsize=8.5, fontstyle='italic', color=C_GRAY, zorder=6)

# Ontology box
ont_x, ont_y, ont_w, ont_h = 1.0, 5.0, 3.5, 0.5
draw_box(ont_x, ont_y, ont_w, ont_h, C_WHITE, ec='#666666',
         label=r"IE Ontology $\mathcal{O} = (\mathcal{E}, \mathcal{R}, \sigma)$",
         fontsize=9.5, bold=True, lw=1.2)

# Left path (blue): JSON Schema -> XGrammar -> Grammar Automaton
lx = 1.55
bw, bh = 2.15, 0.44

b1_y = 4.1
draw_box(lx - bw/2, b1_y, bw, bh, C_BLUE_LIGHT, ec=C_BLUE, label="JSON Schema", fontsize=9, lw=1.0)
draw_arrow(ont_x + ont_w * 0.25, ont_y, lx, b1_y + bh, color=C_BLUE, lw=1.3)

b2_y = 3.2
draw_box(lx - bw/2, b2_y, bw, bh, '#B3D4F0', ec=C_BLUE, label="XGrammar", fontsize=9, lw=1.0)
draw_arrow(lx, b1_y, lx, b2_y + bh, color=C_BLUE, lw=1.3)

b3_y = 2.3
b3_h = 0.5
draw_box(lx - bw/2, b3_y, bw, b3_h, C_BLUE_DARK, ec=C_BLUE_DARK,
         label=r"Grammar Automaton $M_g$", fontsize=8.5, fontcolor=C_WHITE, bold=True, lw=1.0)
draw_arrow(lx, b2_y, lx, b3_y + b3_h, color=C_BLUE, lw=1.3)

# Right path (orange)
rx = 4.0
bw_r = 2.15

b1r_y = 4.1
draw_box(rx - bw_r/2, b1r_y, bw_r, bh, C_ORANGE_LIGHT, ec=C_ORANGE,
         label=r"$\sigma(r)$ type pairs", fontsize=9, lw=1.0)
draw_arrow(ont_x + ont_w * 0.75, ont_y, rx, b1r_y + bh, color=C_ORANGE, lw=1.3)

b2r_y = 3.2
draw_box(rx - bw_r/2, b2r_y, bw_r, bh, '#F5CBA0', ec=C_ORANGE,
         label="TC Processor", fontsize=9, lw=1.0)
draw_arrow(rx, b1r_y, rx, b2r_y + bh, color=C_ORANGE, lw=1.3)

b3r_y = 2.3
draw_box(rx - bw_r/2, b3r_y, bw_r, b3_h, C_ORANGE_DARK, ec=C_ORANGE_DARK,
         label="Semantic Rules", fontsize=9, fontcolor=C_WHITE, bold=True, lw=1.0)
draw_arrow(rx, b2r_y, rx, b3r_y + b3_h, color=C_ORANGE, lw=1.3)

# ===== PANEL 2: Constraint Layers =====
p2_x, p2_y, p2_w, p2_h = 5.6, 0.3, 5.2, 5.9
draw_box(p2_x, p2_y, p2_w, p2_h, C_PANEL, ec='#DDDDDD', zorder=1)
ax.text(p2_x + p2_w/2, 6.05, "Constraint Layers", ha='center', va='center',
        fontsize=12, fontweight='bold', color=C_TEXT, zorder=6)

# Grammar Layer sub-panel (top)
gp_x, gp_y, gp_w, gp_h = 5.9, 3.55, 4.6, 2.3
draw_box(gp_x, gp_y, gp_w, gp_h, C_BLUE_LIGHT, ec=C_BLUE, zorder=2, alpha=0.5, lw=1.0)
ax.text(gp_x + gp_w/2, gp_y + gp_h - 0.22, "Grammar Layer", ha='center', va='center',
        fontsize=10.5, fontweight='bold', color=C_BLUE_DARK, zorder=6)
ax.text(gp_x + gp_w/2, gp_y + gp_h - 0.52, "Level 1: Context-Free", ha='center', va='center',
        fontsize=8.5, fontstyle='italic', color=C_BLUE, zorder=6)
gt_bx, gt_by, gt_bw, gt_bh = gp_x + gp_w/2 - 1.05, gp_y + 0.6, 2.1, 0.55
draw_box(gt_bx, gt_by, gt_bw, gt_bh, C_BLUE, ec=C_BLUE_DARK,
         label=r"$G(t) \subseteq V$", fontsize=11, fontcolor=C_WHITE, bold=True, lw=1.0)
ax.text(gp_x + gp_w/2, gp_y + 0.25, "JSON structure + vocabulary membership",
        ha='center', va='center', fontsize=8, color=C_GRAY, zorder=6)

# Semantic Layer sub-panel (bottom)
sp_x, sp_y, sp_w, sp_h = 5.9, 0.6, 4.6, 2.65
draw_box(sp_x, sp_y, sp_w, sp_h, C_ORANGE_LIGHT, ec=C_ORANGE, zorder=2, alpha=0.5, lw=1.0)
ax.text(sp_x + sp_w/2, sp_y + sp_h - 0.22, "Semantic Layer", ha='center', va='center',
        fontsize=10.5, fontweight='bold', color=C_ORANGE_DARK, zorder=6)
ax.text(sp_x + sp_w/2, sp_y + sp_h - 0.52, "Level 2: Prefix-Decidable", ha='center', va='center',
        fontsize=8.5, fontstyle='italic', color=C_ORANGE, zorder=6)
st_bx, st_by, st_bw, st_bh = sp_x + sp_w/2 - 1.05, sp_y + 1.3, 2.1, 0.55
draw_box(st_bx, st_by, st_bw, st_bh, C_ORANGE, ec=C_ORANGE_DARK,
         label=r"$S(t) \subseteq V$", fontsize=11, fontcolor=C_WHITE, bold=True, lw=1.0)
ax.text(sp_x + sp_w/2, sp_y + 0.98, "Domain/range type constraints",
        ha='center', va='center', fontsize=8, color=C_GRAY, zorder=6)

# D: entity registry
d_bx, d_by, d_bw, d_bh = sp_x + sp_w/2 - 1.35, sp_y + 0.12, 2.7, 0.44
draw_box(d_bx, d_by, d_bw, d_bh, '#FFF3E0', ec=C_ORANGE,
         label=r"$\mathcal{D}$: entity registry (runtime state)", fontsize=8, ls='--', lw=1.0)
draw_arrow(sp_x + sp_w/2, d_by + d_bh, sp_x + sp_w/2, st_by, color=C_ORANGE, lw=0.8)

# Enabling arrow (Grammar -> Semantic) — key visual element
enable_x = gp_x + gp_w/2 + 0.7
draw_arrow(enable_x, gp_y, enable_x, sp_y + sp_h,
           color=C_BLUE_DARK, lw=1.5, ls='--', style='->')
ax.text(enable_x + 0.42, (gp_y + sp_y + sp_h) / 2, "enabling",
        ha='center', va='center', fontsize=10, fontweight='bold', fontstyle='italic',
        color=C_BLUE_DARK, zorder=8, rotation=90,
        bbox=dict(boxstyle='round,pad=0.18', facecolor='#E8F0FE', edgecolor=C_BLUE,
                  alpha=0.9, linewidth=0.8))

# Cross-panel arrows: Panel 1 -> Panel 2
draw_arrow(lx + bw/2, b3_y + b3_h/2, gp_x, gt_by + gt_bh/2,
           color=C_BLUE_DARK, lw=1.5)
draw_arrow(rx + bw_r/2, b3r_y + b3_h/2, sp_x, st_by + st_bh/2,
           color=C_ORANGE_DARK, lw=1.5)

# ===== PANEL 3: Token Masking =====
p3_x, p3_y, p3_w, p3_h = 11.2, 0.3, 5.5, 5.9
draw_box(p3_x, p3_y, p3_w, p3_h, C_PANEL, ec='#DDDDDD', zorder=1)
ax.text(p3_x + p3_w/2, 6.05, "Token Masking", ha='center', va='center',
        fontsize=12, fontweight='bold', color=C_TEXT, zorder=6)
ax.text(p3_x + p3_w/2, 5.72, r"online, per step $t$", ha='center', va='center',
        fontsize=8.5, fontstyle='italic', color=C_GRAY, zorder=6)

p3_cx = p3_x + p3_w / 2

# M_final box
mf_bw, mf_bh = 3.4, 0.52
mf_bx, mf_by = p3_cx - mf_bw/2, 4.85
draw_box(mf_bx, mf_by, mf_bw, mf_bh, '#E8E8E8', ec='#999999',
         label=r"$M_{\mathrm{final}}(t) = G(t) \cap S(t)$", fontsize=9.5, bold=True, lw=1.0)

# Diamond decision
dia_cy = 3.85
dia_sz = 0.4
diamond = plt.Polygon([
    (p3_cx, dia_cy + dia_sz),
    (p3_cx + dia_sz * 1.3, dia_cy),
    (p3_cx, dia_cy - dia_sz),
    (p3_cx - dia_sz * 1.3, dia_cy)
], closed=True, facecolor='#FFF9C4', edgecolor='#999999', linewidth=0.8, zorder=3)
ax.add_patch(diamond)
ax.text(p3_cx, dia_cy, r"$G \cap S = \emptyset$?", ha='center', va='center',
        fontsize=8.5, color=C_TEXT, zorder=6)

draw_arrow(p3_cx, mf_by, p3_cx, dia_cy + dia_sz, color=C_GRAY, lw=1.2)

# "No" branch (left) -> green box
no_cx = p3_cx - 1.4
no_bw, no_bh = 1.75, 0.6
no_by = 2.5
draw_box(no_cx - no_bw/2, no_by, no_bw, no_bh, '#C8E6C9', ec=C_GREEN,
         label="Sample from\n" + r"$G \cap S$", fontsize=8.5, bold=True, fontcolor='#2E7D32', lw=1.0)
draw_arrow(p3_cx - dia_sz * 1.3, dia_cy, no_cx, no_by + no_bh,
           color=C_GREEN, lw=1.2)
ax.text(p3_cx - dia_sz * 1.3 - 0.08, dia_cy + 0.15, "No",
        ha='right', va='bottom', fontsize=8.5, color=C_GREEN, fontweight='bold', zorder=6)

# "Yes" branch (right) -> red box
yes_cx = p3_cx + 1.4
yes_bw, yes_bh = 1.75, 0.6
yes_by = 2.5
draw_box(yes_cx - yes_bw/2, yes_by, yes_bw, yes_bh, '#FFCDD2', ec=C_RED,
         label="Fallback:\n" + r"$G(t)$ only", fontsize=8.5, fontcolor='#C62828', lw=1.0)
ax.text(yes_cx, yes_by - 0.12, "(CF risk)", ha='center', va='top',
        fontsize=7.5, color=C_RED, fontstyle='italic', zorder=6)
draw_arrow(p3_cx + dia_sz * 1.3, dia_cy, yes_cx, yes_by + yes_bh,
           color=C_RED, lw=1.2, ls='--')
ax.text(p3_cx + dia_sz * 1.3 + 0.08, dia_cy + 0.15, "Yes",
        ha='left', va='bottom', fontsize=8.5, color=C_RED, fontweight='bold', zorder=6)

# Converge -> yt box
yt_bw, yt_bh = 2.3, 0.48
yt_bx, yt_by = p3_cx - yt_bw/2, 1.7
draw_box(yt_bx, yt_by, yt_bw, yt_bh, C_WHITE, ec='#999999',
         label=r"$y_t \;\rightarrow\;$ next step", fontsize=9.5, bold=True, lw=1.0)
draw_arrow(no_cx, no_by, p3_cx - 0.35, yt_by + yt_bh, color=C_GRAY, lw=1.0)
draw_arrow(yes_cx, yes_by, p3_cx + 0.35, yt_by + yt_bh, color=C_GRAY, lw=1.0)

# Autoregressive loop
loop_arrow = FancyArrowPatch(
    (yt_bx + yt_bw + 0.05, yt_by + yt_bh/2),
    (mf_bx + mf_bw + 0.05, mf_by + mf_bh/2),
    arrowstyle='->', color=C_GRAY, lw=1.0, mutation_scale=10,
    connectionstyle='arc3,rad=-0.4', linestyle='--', zorder=5
)
ax.add_patch(loop_arrow)
ax.text(p3_x + p3_w - 0.35, (yt_by + mf_by + mf_bh) / 2, "auto-\nregressive",
        ha='center', va='center', fontsize=7.5, color=C_GRAY, fontstyle='italic',
        zorder=6, rotation=90)

# Cross-panel arrows: Panel 2 -> Panel 3
draw_arrow(gt_bx + gt_bw, gt_by + gt_bh/2, mf_bx, mf_by + mf_bh * 0.7,
           color=C_BLUE_DARK, lw=1.3)
draw_arrow(st_bx + st_bw, st_by + st_bh/2, mf_bx, mf_by + mf_bh * 0.3,
           color=C_ORANGE_DARK, lw=1.3)

# Panel watermark numbers
for px, pw, lbl in [(p1_x, p1_w, "1"), (p2_x, p2_w, "2"), (p3_x, p3_w, "3")]:
    ax.text(px + 0.28, 0.55, lbl, ha='center', va='center',
            fontsize=20, fontweight='bold', color='#D5D5D5', zorder=0)

plt.tight_layout(pad=0.1)
plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.savefig(OUTPUT_PDF, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()
print(f"PNG: {OUTPUT_PATH} ({os.path.getsize(OUTPUT_PATH)} bytes)")
print(f"PDF: {OUTPUT_PDF} ({os.path.getsize(OUTPUT_PDF)} bytes)")
