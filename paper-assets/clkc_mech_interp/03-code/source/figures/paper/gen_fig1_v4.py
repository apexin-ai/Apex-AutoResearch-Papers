#!/usr/bin/env python3
"""Figure 1: Cross-Lingual Conflict Probing Pipeline — v4 (Nature Methods style)"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# ─── Color Palette ───
NAVY      = '#1B2838'
SLATE     = '#3D5A80'
TEAL      = '#5BA4B5'
TEAL_DK   = '#3D8B9E'
CORAL     = '#E07A5F'
BG_LIGHT  = '#F8F9FA'
BG_SLATE  = '#EDF2F7'
BG_TEAL   = '#E6F4F7'
CORAL_LT  = '#FFF5F3'
TEXT_BODY  = '#2D3748'
TEXT_SUB   = '#718096'
BORDER    = '#CBD5E0'
DIVIDER   = '#E2E8F0'
WHITE     = '#FFFFFF'
DIAG_FILL = '#F0F4F8'  # very subtle fill for within-language cells

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Liberation Serif'],
    'mathtext.fontset': 'dejavuserif',
    'axes.unicode_minus': False,
})

FW, FH = 16, 6.2
fig, ax = plt.subplots(1, 1, figsize=(FW, FH), dpi=300)
ax.set_xlim(0, FW)
ax.set_ylim(0, FH)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor(WHITE)

# ─── Helpers ───

def shadow(ax, x, y, w, h, r, style='normal'):
    presets = {
        'normal': [(0.05, -0.05, '#00000014'), (0.025, -0.025, '#0000000C')],
        'strong': [(0.08, -0.08, '#0000001A'), (0.04, -0.04, '#00000012')],
        'subtle': [(0.035, -0.035, '#0000000E'), (0.017, -0.017, '#00000008')],
    }
    for dx, dy, c in presets.get(style, presets['normal']):
        ax.add_patch(FancyBboxPatch((x+dx, y+dy), w, h,
            boxstyle=f"round,pad=0,rounding_size={r}",
            facecolor=c, edgecolor='none', zorder=1))

def pill(ax, x, y, w, h, text, fill=WHITE, ec=BORDER, lw=0.7,
         tc=TEXT_BODY, fs=8.2, fw='normal', z=3):
    r = h / 2
    shadow(ax, x, y, w, h, r, 'subtle')
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={r}",
        facecolor=fill, edgecolor=ec, linewidth=lw, zorder=z))
    ax.text(x + w/2, y + h/2, text, ha='center', va='center',
            fontsize=fs, color=tc, fontweight=fw, zorder=z+1)

def rbox(ax, x, y, w, h, text='', fill=WHITE, ec=BORDER, lw=0.7,
         r=0.1, tc=TEXT_BODY, fs=8.5, fw='normal', sh='normal', z=3,
         sub=''):
    if sh:
        shadow(ax, x, y, w, h, r, sh)
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={r}",
        facecolor=fill, edgecolor=ec, linewidth=lw, zorder=z))
    if text:
        ty = y + h/2 + (0.10 if sub else 0)
        ax.text(x + w/2, ty, text, ha='center', va='center',
                fontsize=fs, color=tc, fontweight=fw, zorder=z+1)
    if sub:
        ax.text(x + w/2, y + h/2 - 0.12, sub, ha='center', va='center',
                fontsize=6.8, color=TEXT_SUB, fontstyle='italic', zorder=z+1)

def checkmark(ax, cx, cy, r=0.15):
    ax.add_patch(Circle((cx, cy), r, facecolor=TEAL, edgecolor=TEAL_DK,
                         linewidth=0.4, zorder=5))
    ax.text(cx, cy + 0.01, '✓', color=WHITE, fontsize=7, fontweight='bold',
            ha='center', va='center', zorder=6, fontfamily='DejaVu Sans')

# ─── Layout ───
PH = 5.3
PY = 0.5
GAP = 0.5

PA_X, PA_W = 0.35, 4.1
PB_X = PA_X + PA_W + GAP
PB_W = 6.4
PC_X = PB_X + PB_W + GAP
PC_W = PA_W

# ─── Panel backgrounds ───
for px, pw in [(PA_X, PA_W), (PB_X, PB_W), (PC_X, PC_W)]:
    shadow(ax, px, PY, pw, PH, 0.15, 'normal')
    ax.add_patch(FancyBboxPatch((px, PY), pw, PH,
        boxstyle="round,pad=0,rounding_size=0.15",
        facecolor=BG_LIGHT, edgecolor=BORDER, linewidth=0.5, zorder=2))

# ─── Panel titles ───
TY = PY + PH - 0.35

def ptitle(px, letter, text, section, pw):
    ax.text(px + 0.25, TY, f'({letter})', fontsize=11, fontweight='bold',
            color=NAVY, va='center', zorder=10)
    ax.text(px + 0.65, TY, text, fontsize=10.5, fontweight='bold',
            color=NAVY, va='center', zorder=10)
    ax.text(px + pw - 0.2, TY, section, fontsize=6.5, color=TEXT_SUB,
            va='center', ha='right', zorder=10)
    ax.plot([px + 0.25, px + pw - 0.25], [TY - 0.18, TY - 0.18],
            color=TEAL, lw=0.8, alpha=0.4, zorder=10)

ptitle(PA_X, 'a', 'Data Construction', '§3.2', PA_W)
ptitle(PB_X, 'b', 'Probing Framework', '§3.4–3.5', PB_W)
ptitle(PC_X, 'c', 'Confound Exclusion', '§3.6', PC_W)

# ═══════════════════════════════════════════════════════════════
# Panel (a): Data Construction
# ═══════════════════════════════════════════════════════════════

pw, ph = 3.3, 0.40
px = PA_X + (PA_W - pw) / 2 + 0.1
content_top = TY - 0.55
content_bot = PY + 0.35
avail = content_top - content_bot
pgap = (avail - 5 * ph) / 4

steps = [
    ("ConflictQA Dataset", WHITE, BORDER, TEXT_BODY, 'normal'),
    ("Parametric Knowledge Verification", WHITE, BORDER, TEXT_BODY, 'normal'),
    ("Translation (EN → ZH, Qwen3-8B)", WHITE, BORDER, TEXT_BODY, 'normal'),
    ("COMET Back-translation Validation", WHITE, BORDER, TEXT_BODY, 'normal'),
    ("EN / ZH Parallel Conflict Data", CORAL_LT, CORAL, CORAL, 'bold'),
]

pcenters = []
for i, (label, fill, ec, tc, fw) in enumerate(steps):
    py = content_top - i * (ph + pgap)
    lw = 1.0 if i == 4 else 0.7
    pill(ax, px, py, pw, ph, label, fill=fill, ec=ec, lw=lw, tc=tc, fw=fw)
    pcenters.append(py + ph / 2)

# Vertical progress line
vx = px - 0.22
for i in range(len(pcenters)):
    dc = CORAL if i == 4 else SLATE
    ds = 5.5 if i == 4 else 4
    ax.plot(vx, pcenters[i], 'o', color=dc, markersize=ds, zorder=6,
            markeredgecolor=WHITE, markeredgewidth=0.5)
    if i < len(pcenters) - 1:
        ax.plot([vx, vx], [pcenters[i] - 0.02, pcenters[i+1] + 0.02],
                color=BORDER, lw=0.8, solid_capstyle='round', zorder=4)

# Step numbers
for i in range(len(pcenters)):
    nc = CORAL if i == 4 else TEXT_SUB
    ax.text(vx - 0.17, pcenters[i], str(i+1), fontsize=6.5, color=nc,
            ha='center', va='center', fontweight='bold', zorder=6)


# ═══════════════════════════════════════════════════════════════
# Panel (b): Probing Framework
# ═══════════════════════════════════════════════════════════════

mid_x = PB_X + PB_W / 2

# Two teal boxes
tw, th = 2.65, 0.55
tg = 0.25
tx1 = PB_X + (PB_W - 2*tw - tg) / 2
tx2 = tx1 + tw + tg
ty = TY - 0.75

rbox(ax, tx1, ty, tw, th, text='Residual Stream Extraction',
     fill=BG_TEAL, ec=TEAL, lw=0.8, r=0.08, tc=SLATE, fs=8.2,
     fw='bold', sub='Model activations across layers', sh='subtle')

rbox(ax, tx2, ty, tw, th, text='Linear Probe Training',
     fill=BG_TEAL, ec=TEAL, lw=0.8, r=0.08, tc=SLATE, fs=8.2,
     fw='bold', sub='Conflict classification models', sh='subtle')

# Dashed connector
tmid = ty + th / 2
ax.plot([tx1 + tw, tx2], [tmid, tmid], color=TEAL, lw=0.7,
        ls=(0, (4, 3)), alpha=0.5, zorder=4)

# Down arrow
ax.annotate('', xy=(mid_x, ty - 0.30), xytext=(mid_x, ty - 0.02),
            arrowprops=dict(arrowstyle='->', color=SLATE, lw=1.0,
                            mutation_scale=10), zorder=5)

# Matrix section label
mt_y = ty - 0.42
ax.text(mid_x, mt_y, '4-Direction Transfer Protocol', ha='center',
        va='center', fontsize=9, fontweight='bold', color=NAVY, zorder=10)

# ─── 2×2 Matrix ───
mw, mh = 4.8, 1.85
mx = PB_X + (PB_W - mw) / 2
my = mt_y - mh - 0.12

shadow(ax, mx, my, mw, mh, 0.1, 'normal')
mat_patch = FancyBboxPatch((mx, my), mw, mh,
    boxstyle="round,pad=0,rounding_size=0.1",
    facecolor=WHITE, edgecolor=BORDER, linewidth=0.6, zorder=3)
ax.add_patch(mat_patch)

c0 = mw * 0.24
c1 = (mw - c0) / 2
r0 = mh * 0.28
r1 = (mh - r0) / 2

# Header fill (clipped)
hdr_y = my + mh - r0
hf = FancyBboxPatch((mx, hdr_y), mw, r0,
    boxstyle="round,pad=0,rounding_size=0.1",
    facecolor=BG_SLATE, edgecolor='none', zorder=3.4)
hf.set_clip_path(mat_patch)
ax.add_patch(hf)

# Left column fills (clipped)
for ri in range(2):
    ry = my + (1 - ri) * r1
    lcf = FancyBboxPatch((mx, ry), c0, r1,
        boxstyle="round,pad=0,rounding_size=0.02",
        facecolor=BG_SLATE, edgecolor='none', zorder=3.4)
    lcf.set_clip_path(mat_patch)
    ax.add_patch(lcf)

# Subtle diagonal highlight for within-language cells (EN→EN, ZH→ZH)
for ri_idx, ci_idx in [(0, 0), (1, 1)]:
    dx = mx + c0 + ci_idx * c1
    dy = my + (1 - ri_idx) * r1
    diag_f = FancyBboxPatch((dx + 0.03, dy + 0.03), c1 - 0.06, r1 - 0.06,
        boxstyle="round,pad=0,rounding_size=0.04",
        facecolor=DIAG_FILL, edgecolor='none', zorder=3.5)
    diag_f.set_clip_path(mat_patch)
    ax.add_patch(diag_f)

# Dividers
for d_y in [hdr_y, my + r1]:
    ax.plot([mx + 0.06, mx + mw - 0.06], [d_y, d_y],
            color=DIVIDER, lw=0.5, zorder=4)
for d_x in [mx + c0, mx + c0 + c1]:
    ax.plot([d_x, d_x], [my + 0.06, my + mh - 0.06],
            color=DIVIDER, lw=0.5, zorder=4)

# Header labels
hcy = hdr_y + r0 / 2
ax.text(mx + c0 + c1/2, hcy, 'Test: EN', ha='center', va='center',
        fontsize=8.5, fontweight='bold', color=NAVY, zorder=5)
ax.text(mx + c0 + c1 + c1/2, hcy, 'Test: ZH', ha='center', va='center',
        fontsize=8.5, fontweight='bold', color=NAVY, zorder=5)

# Row headers
r1_cy = my + r1 + r1/2
r2_cy = my + r1/2
ax.text(mx + c0/2, r1_cy, 'Train: EN', ha='center', va='center',
        fontsize=8, fontweight='bold', color=NAVY, zorder=5)
ax.text(mx + c0/2, r2_cy, 'Train: ZH', ha='center', va='center',
        fontsize=8, fontweight='bold', color=NAVY, zorder=5)

# Data cells
for ci, ri_y, label in [
    (c0 + c1/2,       r1_cy, 'EN → EN'),
    (c0 + c1 + c1/2,  r1_cy, 'EN → ZH'),
    (c0 + c1/2,       r2_cy, 'ZH → EN'),
    (c0 + c1 + c1/2,  r2_cy, 'ZH → ZH'),
]:
    ax.text(mx + ci, ri_y, label, ha='center', va='center',
            fontsize=8.5, color=TEXT_BODY, zorder=5)

# Within/cross labels (tiny, inside matrix)
ax.text(mx + c0 + c1/2, r1_cy - 0.22, 'within', ha='center', va='center',
        fontsize=5.5, color=TEXT_SUB, fontstyle='italic', zorder=5)
ax.text(mx + c0 + c1 + c1/2, r2_cy - 0.22, 'within', ha='center', va='center',
        fontsize=5.5, color=TEXT_SUB, fontstyle='italic', zorder=5)
ax.text(mx + c0 + c1 + c1/2, r1_cy - 0.22, 'cross', ha='center', va='center',
        fontsize=5.5, color=TEXT_SUB, fontstyle='italic', zorder=5)
ax.text(mx + c0 + c1/2, r2_cy - 0.22, 'cross', ha='center', va='center',
        fontsize=5.5, color=TEXT_SUB, fontstyle='italic', zorder=5)

# Down arrow to bootstrap
bw, bh = 3.0, 0.38
bx = PB_X + (PB_W - bw) / 2
by = my - 0.50

ax.annotate('', xy=(mid_x, by + bh + 0.03), xytext=(mid_x, my - 0.02),
            arrowprops=dict(arrowstyle='->', color=SLATE, lw=1.0,
                            mutation_scale=10), zorder=5)

rbox(ax, bx, by, bw, bh, text='Bootstrap CI  (n = 2,000)', fill=BG_SLATE,
     ec=BORDER, lw=0.5, r=bh/2, tc=SLATE, fs=8, fw='bold', sh='subtle')

# ═══════════════════════════════════════════════════════════════
# Panel (c): Confound Exclusion
# ═══════════════════════════════════════════════════════════════

cards = [
    ("COMET Tercile Ablation", "Translation quality control"),
    ("Token Overlap Analysis", "Surface feature exclusion"),
    ("XNLI Non-conflict Baseline", "Task specificity verification"),
]

cw, ch = 3.4, 1.0
cx = PC_X + (PC_W - cw) / 2
cgap = 0.40
total_h = 3 * ch + 2 * cgap
c_top = PY + PH/2 + total_h/2 - 0.1

for i, (title, desc) in enumerate(cards):
    cy = c_top - i * (ch + cgap) - ch

    shadow(ax, cx, cy, cw, ch, 0.08, 'subtle')
    ax.add_patch(FancyBboxPatch((cx, cy), cw, ch,
        boxstyle="round,pad=0,rounding_size=0.08",
        facecolor=WHITE, edgecolor=DIVIDER, linewidth=0.5, zorder=3))

    # Teal left accent bar
    bw_bar = 0.05
    ax.add_patch(FancyBboxPatch((cx + 0.04, cy + 0.15), bw_bar, ch - 0.30,
        boxstyle=f"round,pad=0,rounding_size={bw_bar/2}",
        facecolor=TEAL, edgecolor='none', zorder=4, alpha=0.65))

    # Checkmark
    checkmark(ax, cx + 0.40, cy + ch/2, r=0.15)

    # Text
    tx = cx + 0.68
    ax.text(tx, cy + ch/2 + 0.16, title, fontsize=8.5, fontweight='bold',
            color=NAVY, va='center', zorder=5)
    ax.text(tx, cy + ch/2 - 0.14, desc, fontsize=7.2, color=TEXT_SUB,
            fontstyle='italic', va='center', zorder=5)

# ═══════════════════════════════════════════════════════════════
# Inter-panel flow arrows
# ═══════════════════════════════════════════════════════════════

flow_y = PY + PH / 2 + 0.2

for (x1, x2) in [(PA_X + PA_W, PB_X), (PB_X + PB_W, PC_X)]:
    ax.add_patch(FancyArrowPatch(
        (x1 + 0.04, flow_y), (x2 - 0.04, flow_y),
        connectionstyle='arc3,rad=0.12',
        arrowstyle='-|>', color=SLATE, lw=1.4,
        mutation_scale=13, zorder=10))

# ═══════════════════════════════════════════════════════════════
plt.savefig('figures/paper/fig1_pipeline_v4.png', dpi=300,
            bbox_inches='tight', pad_inches=0.06, facecolor=WHITE)
plt.close()
print("Saved figures/paper/fig1_pipeline_v4.png")
