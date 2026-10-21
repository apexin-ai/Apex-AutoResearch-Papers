#!/usr/bin/env python3
"""
Figure 1: Verdict prediction pipeline overview.
Publication-quality conceptual diagram for EMNLP 2026.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

# ── Palette ──────────────────────────────────────────────────────
BG       = '#FFFFFF'
BOX_BG   = '#F8F9FA'
BOX_BD   = '#CFD8DC'
ARR_NEU  = '#90A4AE'
LABEL_DK = '#37474F'
LABEL_MD = '#546E7A'
LABEL_LT = '#78909C'

NOTRACE_BG, NOTRACE_BD, NOTRACE_AC = '#F5F5F5', '#E0E0E0', '#9E9E9E'
EXC_BG, EXC_BD, EXC_AC             = '#EDF7ED', '#A5D6A7', '#2E7D32'
VOTA_BG, VOTA_BD, VOTA_AC          = '#E8F0FE', '#90CAF9', '#1565C0'
FULL_BG, FULL_BD, FULL_AC          = '#FFF3E0', '#FFCC80', '#E65100'

STAR_GOLD = '#F9A825'
SFT_BG    = '#EDE7F6'
SFT_BD    = '#B39DDB'

FONT_SERIF = 'Liberation Serif'
FONT_MONO  = 'DejaVu Sans Mono'
FONT_SANS  = 'Liberation Sans'

# ── Figure ───────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10.0, 3.6), dpi=300)
ax.set_xlim(-0.1, 10.1)
ax.set_ylim(-0.2, 3.6)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor(BG)

# ── Helpers ──────────────────────────────────────────────────────
def rbox(x, y, w, h, fc, ec, lw=0.7, rad=0.08, shadow=True, zorder=3):
    if shadow:
        s = FancyBboxPatch((x+0.03, y-0.03), w, h,
            boxstyle=f"round,pad=0,rounding_size={rad}",
            fc='#00000009', ec='none', lw=0, zorder=zorder-1)
        ax.add_patch(s)
    b = FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={rad}",
        fc=fc, ec=ec, lw=lw, zorder=zorder)
    ax.add_patch(b)
    return b

def accent_bar(x, y, h, color, w=0.07, zorder=5):
    bar = FancyBboxPatch((x, y), w, h,
        boxstyle="round,pad=0,rounding_size=0.03",
        fc=color, ec='none', lw=0, zorder=zorder)
    ax.add_patch(bar)

def simple_arrow(x1, y1, x2, y2, color=ARR_NEU, lw=1.0, style='-|>',
                 ls='-', zorder=2):
    a = FancyArrowPatch((x1, y1), (x2, y2),
        arrowstyle=style, color=color, lw=lw, linestyle=ls,
        mutation_scale=8, zorder=zorder,
        connectionstyle='arc3,rad=0')
    ax.add_patch(a)

def curved_arrow(x1, y1, x2, y2, color=ARR_NEU, lw=1.0, rad=0.15,
                 style='-|>', ls='-', zorder=2):
    a = FancyArrowPatch((x1, y1), (x2, y2),
        arrowstyle=style, color=color, lw=lw, linestyle=ls,
        mutation_scale=8, zorder=zorder,
        connectionstyle=f'arc3,rad={rad}')
    ax.add_patch(a)

# ── (A) Input box ────────────────────────────────────────────────
ix, iy, iw, ih = 0.05, 1.15, 1.05, 1.1
rbox(ix, iy, iw, ih, BOX_BG, BOX_BD, lw=0.8)

cx_code = ix + 0.15
cy_code = iy + ih - 0.18
ax.text(cx_code, cy_code, 'def solve(n):', fontsize=7.5,
        fontfamily=FONT_MONO, color='#455A64', zorder=5)
for j, wf in enumerate([0.55, 0.42, 0.63, 0.30]):
    yy = cy_code - 0.13 - j * 0.1
    ax.plot([cx_code + 0.1, cx_code + 0.1 + wf * 0.55], [yy, yy],
            lw=2.5, color='#B0BEC5', solid_capstyle='round', zorder=5)

ax.plot([ix + 0.1, ix + iw - 0.1], [iy + 0.32, iy + 0.32],
        lw=0.5, color='#E0E0E0', ls='--', zorder=5)
ax.text(cx_code, iy + 0.17, '>>> test(42)', fontsize=6.5,
        fontfamily=FONT_MONO, color=LABEL_MD, zorder=5)
ax.text(ix + iw/2, iy - 0.1, 'Source Code + Test',
        fontsize=9.5, fontfamily=FONT_SERIF, color=LABEL_MD,
        ha='center', va='top', zorder=5)

# ── (B) Execution badge ─────────────────────────────────────────
bx, by, bw, bh = 1.55, 1.45, 0.65, 0.5
rbox(bx, by, bw, bh, '#ECEFF1', '#B0BEC5', lw=0.7)
ax.text(bx + bw/2, by + bh/2 + 0.05, '▶', fontsize=9,
        ha='center', va='center', color=LABEL_MD, zorder=5)
ax.text(bx + bw/2, by + bh/2 - 0.1, 'Execute', fontsize=9.5,
        fontfamily=FONT_SERIF, fontweight='bold',
        ha='center', va='center', color=LABEL_DK, zorder=5)

simple_arrow(ix + iw + 0.03, iy + ih/2, bx - 0.03, by + bh/2)

# ── (C) Raw Trace document ──────────────────────────────────────
rx, ry, rw, rh = 2.6, 1.15, 0.55, 1.1
rbox(rx, ry, rw, rh, '#FAFBFC', '#B0BEC5', lw=0.6, rad=0.04)

for j in range(13):
    yy = ry + rh - 0.1 - j * 0.065
    wl = 0.22 + np.random.RandomState(j + 7).random() * 0.18
    alp = 0.50 if j < 11 else 0.20
    ax.plot([rx + 0.06, rx + 0.06 + wl], [yy, yy],
            lw=1.4, color='#B0BEC5', alpha=alp,
            solid_capstyle='round', zorder=5)

wx = np.linspace(rx, rx + rw, 40)
wy = ry + 0.02 + 0.012 * np.sin(wx * 28)
ax.plot(wx, wy, color='#B0BEC5', lw=0.5, zorder=6)

ax.text(rx + rw/2, ry + rh + 0.07, 'Raw Trace', fontsize=9,
        fontfamily=FONT_SERIF, fontstyle='italic',
        ha='center', va='bottom', color=LABEL_LT, zorder=5)
ax.text(rx + rw/2, ry - 0.09, '~2k tokens', fontsize=6.5,
        fontfamily=FONT_SANS, ha='center', va='top',
        color='#BDBDBD', zorder=5)

simple_arrow(bx + bw + 0.03, by + bh/2, rx - 0.03, ry + rh/2)

# ── (D) Condition cards ─────────────────────────────────────────
CX   = 3.55
CW   = 3.05
CH   = 0.62
CGAP = 0.12

cards = [
    ('no_trace',       'No Trace',       'Source code only (baseline)',
     NOTRACE_BG, NOTRACE_BD, NOTRACE_AC, '75.1%',  False),
    ('exception_only', 'Exception Only', 'Exception & error events',
     EXC_BG,     EXC_BD,     EXC_AC,     '99.8%',  True),
    ('vota',           'VOTA',           'Exception + assertion + loops',
     VOTA_BG,    VOTA_BD,    VOTA_AC,    '99.1%',  False),
    ('full_trace',     'Full Trace',     'Complete line-by-line log',
     FULL_BG,    FULL_BD,    FULL_AC,    '81.4%',  False),
]

total_h = len(cards) * CH + (len(cards) - 1) * CGAP
y_start = 1.70 + total_h / 2

card_centers = []
for i, (key, title, subtitle, bg, bd, ac, acc, is_star) in enumerate(cards):
    cy = y_start - i * (CH + CGAP)
    y  = cy - CH / 2
    card_centers.append(cy)

    rbox(CX, y, CW, CH, bg, bd,
         lw=1.2 if is_star else 0.8, rad=0.06, shadow=True)
    accent_bar(CX + 0.05, y + 0.08, CH - 0.16, ac)

    if is_star:
        hl = FancyBboxPatch((CX - 0.03, y - 0.03), CW + 0.06, CH + 0.06,
            boxstyle="round,pad=0,rounding_size=0.08",
            fc='none', ec=STAR_GOLD, lw=1.4, zorder=2, alpha=0.55)
        ax.add_patch(hl)

    # ── Left zone: title + subtitle ──
    tx = CX + 0.22
    ax.text(tx, cy + 0.12, title, fontsize=11, fontfamily=FONT_SERIF,
            fontweight='bold', color=LABEL_DK, va='center', zorder=6)
    ax.text(tx, cy - 0.09, subtitle, fontsize=7.5, fontfamily=FONT_SERIF,
            fontstyle='italic', color=LABEL_LT, va='center', zorder=6)

    # ── Middle zone: schematic content (visual density indicators) ──
    content_x = CX + 1.85
    rng = np.random.RandomState(42)
    if key == 'no_trace':
        for j in range(2):
            ly = cy + 0.04 - j * 0.12
            ax.plot([content_x, content_x + 0.30 + j * 0.08], [ly, ly],
                    lw=2.2, color='#DEDEDE', solid_capstyle='round', zorder=5)
    elif key == 'exception_only':
        for j, (wl, c) in enumerate([(0.50, '#66BB6A'), (0.38, '#81C784'), (0.42, '#A5D6A7')]):
            ly = cy + 0.12 - j * 0.10
            ax.plot([content_x, content_x + wl], [ly, ly],
                    lw=2.5, color=c, solid_capstyle='round', zorder=5, alpha=0.7)
    elif key == 'vota':
        for j in range(5):
            ly = cy + 0.15 - j * 0.07
            wl = 0.25 + rng.random() * 0.25
            c = ['#64B5F6', '#90CAF9', '#64B5F6', '#BBDEFB', '#90CAF9'][j]
            ax.plot([content_x, content_x + wl], [ly, ly],
                    lw=2.0, color=c, solid_capstyle='round', zorder=5, alpha=0.65)
    elif key == 'full_trace':
        for j in range(10):
            ly = cy + 0.23 - j * 0.048
            wl = 0.3 + rng.random() * 0.55
            alp = 0.40 if j < 8 else 0.15
            ax.plot([content_x, content_x + wl], [ly, ly],
                    lw=1.3, color='#FFAB91', alpha=alp,
                    solid_capstyle='round', zorder=5)

    # ── Right zone: accuracy badge ──
    badge_x = CX + CW - 0.38
    badge_fs = 13 if is_star else 10
    badge_fw = 'bold' if is_star else 'normal'
    t = ax.text(badge_x, cy, acc, fontsize=badge_fs,
                fontfamily=FONT_SANS, fontweight=badge_fw,
                color=ac, ha='center', va='center', zorder=6)
    if is_star:
        t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

    if is_star:
        ax.text(badge_x + 0.38, cy, '★', fontsize=11,
                color=STAR_GOLD, ha='center', va='center', zorder=6)
    elif acc in ('75.1%', '81.4%'):
        ax.text(badge_x + 0.28, cy - 0.01, '↓', fontsize=7,
                color=ac, ha='center', va='center', alpha=0.45, zorder=6)

# ── Extraction arrows: Raw Trace → Cards ────────────────────────
rcx = rx + rw
rcy = ry + rh / 2

arrow_cfg = [
    (NOTRACE_AC, 0.6, ':',  0.30),
    (EXC_AC,     1.4, '-',  0.10),
    (VOTA_AC,    1.0, '-', -0.10),
    (FULL_AC,    1.6, '-', -0.30),
]
for cy, (color, lw, ls, rad) in zip(card_centers, arrow_cfg):
    curved_arrow(rcx + 0.06, rcy, CX - 0.06, cy,
                 color=color, lw=lw, rad=rad, ls=ls)

# ── Vertical "Info density" annotation ───────────────────────────
ann_x = CX + CW + 0.18
y_top = card_centers[0]
y_bot = card_centers[-1]

ax.annotate('', xy=(ann_x, y_top + 0.18),
            xytext=(ann_x, y_bot - 0.18),
            arrowprops=dict(arrowstyle='<->', color=LABEL_LT,
                            lw=0.6, shrinkA=0, shrinkB=0), zorder=3)
ax.text(ann_x + 0.1, (y_top + y_bot) / 2, 'Info\ndensity',
        fontsize=7.5, fontfamily=FONT_SANS, color=LABEL_LT,
        ha='left', va='center', linespacing=1.1, zorder=5)

# Bottom annotation
ax.text(CX + CW / 2, card_centers[-1] - CH/2 - 0.16,
        'Less trace  →  higher accuracy',
        fontsize=9, fontfamily=FONT_SERIF, fontstyle='italic',
        color=LABEL_LT, ha='center', va='top', zorder=5)

# ── Converging arrows → SFT ──────────────────────────────────────
sx, sy, sw, sh = 7.75, 1.15, 0.8, 1.1
rbox(sx, sy, sw, sh, SFT_BG, SFT_BD, lw=0.8)
ax.text(sx + sw/2, sy + sh/2 + 0.15, 'SFT', fontsize=14,
        fontfamily=FONT_SERIF, fontweight='bold',
        ha='center', va='center', color='#4527A0', zorder=5)
ax.text(sx + sw/2, sy + sh/2 - 0.08, '(LoRA)', fontsize=8.5,
        fontfamily=FONT_SANS, ha='center', va='center',
        color='#7E57C2', zorder=5)
ax.text(sx + sw/2, sy + sh/2 - 0.28, '1.5B–13B', fontsize=7.5,
        fontfamily=FONT_SANS, ha='center', va='center',
        color='#9E9E9E', zorder=5)

for cy in card_centers:
    simple_arrow(CX + CW + 0.02, cy, sx - 0.05, sy + sh/2,
                 color=ARR_NEU, lw=0.5, style='-|>')

# ── Verdict output ───────────────────────────────────────────────
vx, vy, vw, vh = 9.0, 1.3, 0.85, 0.8
rbox(vx, vy, vw, vh, '#FAFAFA', BOX_BD, lw=0.6)
ax.text(vx + vw/2, vy + vh/2 + 0.15, 'Verdict', fontsize=11,
        fontfamily=FONT_SERIF, fontweight='bold',
        ha='center', va='center', color=LABEL_DK, zorder=5)
ax.text(vx + vw/2, vy + vh/2 - 0.05, '✓ pass', fontsize=9.5,
        ha='center', va='center', color='#43A047',
        fontfamily='DejaVu Sans', zorder=5)
ax.text(vx + vw/2, vy + vh/2 - 0.22, '✗ fail', fontsize=9.5,
        ha='center', va='center', color='#E53935',
        fontfamily='DejaVu Sans', zorder=5)

simple_arrow(sx + sw + 0.03, sy + sh/2, vx - 0.04, vy + vh/2)

# ── "Trace Conditions" header ────────────────────────────────────
tc_y = y_start + CH/2 + 0.13
ax.text(CX + CW/2, tc_y, 'Trace Conditions', fontsize=11,
        fontfamily=FONT_SERIF, fontstyle='italic',
        color=LABEL_MD, ha='center', va='bottom', zorder=5)

gpad = 0.12
gx = CX - gpad
gy = card_centers[-1] - CH/2 - gpad
gw = CW + 2*gpad + 0.55
gh = (card_centers[0] + CH/2) - (card_centers[-1] - CH/2) + 2*gpad
gb = FancyBboxPatch((gx, gy), gw, gh,
    boxstyle="round,pad=0,rounding_size=0.1",
    fc='none', ec='#CFD8DC', lw=0.5, ls='--', zorder=1)
ax.add_patch(gb)

# ── Save ─────────────────────────────────────────────────────────
out = '/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/figures/paper'
plt.savefig(f'{out}/fig1_trace_overview_v5.png',
            dpi=300, bbox_inches='tight', pad_inches=0.05, facecolor=BG)
plt.savefig(f'{out}/fig1_trace_overview_v5.pdf',
            bbox_inches='tight', pad_inches=0.05, facecolor=BG)
plt.close()
print('DONE: fig1_trace_overview_v5.png + .pdf')
