#!/usr/bin/env python3
"""Figure 1 Hero: Detection ≠ Decision — Cross-Lingual Knowledge Conflict."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch
import os

# ── Colors ──
NAVY     = '#2C3E6B'
DARK     = '#1B2838'
EN_BLUE  = '#4A90D9'
ZH_CORAL = '#E07A5F'
TEAL     = '#5BA4B5'
WHITE    = '#FFFFFF'
BORDER   = '#C8D4DE'
TEXT_GRAY= '#999999'
SLATE    = '#546E7A'
OUT_BLUE   = '#2C5F8A'
OUT_ORANGE = '#D35400'

BG_BLUE  = '#E8F0FE'
BG_CORAL = '#FEF3EC'
BG_LAYER = '#F0F4F8'
TEAL_LT  = '#D4EEF4'
TEAL_MD  = '#A8D8E4'
CORAL_BG = '#F5D5C8'

# ── CJK Fonts ──
_CJK_REG  = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
_CJK_BOLD = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
if not os.path.exists(_CJK_REG):
    _CJK_REG  = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc'
    _CJK_BOLD = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'
CJK   = fm.FontProperties(fname=_CJK_REG, size=9)
CJK_B = fm.FontProperties(fname=_CJK_BOLD, size=10)

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Helvetica', 'Arial'],
    'font.size': 9, 'axes.linewidth': 0,
    'figure.facecolor': WHITE, 'axes.facecolor': WHITE,
    'text.color': DARK,
})


# ── Helpers ──

def rbox(ax, x, y, w, h, fc=WHITE, ec=BORDER, lw=0.8, rad=0.012,
         alpha=1, zorder=2):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle=f'round,pad=0,rounding_size={rad}',
                       fc=fc, ec=ec, lw=lw, alpha=alpha,
                       transform=ax.transAxes, zorder=zorder, clip_on=False)
    ax.add_patch(p)


def panel_frame(ax, title):
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
    P, HH = 0.025, 0.06
    x, y, w, h = P, P, 1 - 2*P, 1 - 2*P
    rbox(ax, x, y, w, h, fc=WHITE, ec=BORDER, lw=1, rad=0.018, zorder=1)
    rbox(ax, x, y + h - HH, w, HH, fc=NAVY, ec=NAVY, lw=0, rad=0.018, zorder=3)
    ax.text(x + 0.04, y + h - HH/2, title,
            fontsize=10, color=WHITE, fontweight='bold',
            transform=ax.transAxes, va='center', ha='left', zorder=4)
    return x, y, w, h - HH


def mpill(ax, x, y, name, ok, fs=7.5):
    fc = TEAL if ok else '#8E99A4'
    sym = '✓' if ok else '✗'
    pw, ph = 0.16, 0.035
    rbox(ax, x - pw/2, y - ph/2, pw, ph,
         fc=fc, ec='none', lw=0, rad=ph/2, zorder=5)
    ax.text(x, y, f'{name} {sym}', fontsize=fs, color=WHITE, fontweight='bold',
            transform=ax.transAxes, va='center', ha='center', zorder=6)


# ═══════════════════════════════════════════
# Panel (a): Cross-Lingual Knowledge Conflict — iconic redesign
# ═══════════════════════════════════════════

def draw_a(ax):
    X, Y, W, H = panel_frame(ax, '(a) Cross-Lingual Knowledge Conflict')

    # Question at top (compact dark pill)
    qy = Y + H * 0.90
    rbox(ax, X + 0.04, qy - 0.025, W - 0.08, 0.05,
         fc=DARK, ec=DARK, lw=0, rad=0.012, zorder=3)
    ax.text(X + W/2, qy, 'Q: "Where was Marie Curie born?"',
            fontsize=8.5, color=WHITE, fontweight='bold',
            transform=ax.transAxes, va='center', ha='center', zorder=4)

    # EN input tag (left)
    en_x = X + W * 0.18
    en_y = Y + H * 0.73
    pw, ph = 0.14, 0.042
    rbox(ax, en_x - pw/2, en_y - ph/2, pw, ph,
         fc=BG_BLUE, ec=EN_BLUE, lw=1.0, rad=ph/2, zorder=3)
    ax.text(en_x, en_y, 'EN', fontsize=9, color=EN_BLUE, fontweight='bold',
            transform=ax.transAxes, va='center', ha='center', zorder=4)
    ax.text(en_x, en_y - 0.055, '“…Warsaw…”', fontsize=7,
            color=SLATE, fontstyle='italic',
            transform=ax.transAxes, va='center', ha='center')

    # ZH input tag (right)
    zh_x = X + W * 0.82
    zh_y = Y + H * 0.73
    rbox(ax, zh_x - pw/2, zh_y - ph/2, pw, ph,
         fc=BG_CORAL, ec=ZH_CORAL, lw=1.0, rad=ph/2, zorder=3)
    ax.text(zh_x, zh_y, 'ZH', fontsize=9, color=ZH_CORAL, fontweight='bold',
            transform=ax.transAxes, va='center', ha='center', zorder=4)
    ax.text(zh_x, zh_y - 0.055, '“…巴黎…”', fontsize=7,
            color=SLATE, fontstyle='italic',
            transform=ax.transAxes, va='center', ha='center',
            fontproperties=CJK)

    # Transformer model block (center, gradient-like with layer lines)
    mx = X + W / 2
    my = Y + H * 0.48
    mw, mh = W * 0.44, H * 0.24
    ml, mb = mx - mw/2, my - mh/2
    rbox(ax, ml, mb, mw, mh, fc='#EDF2F7', ec=SLATE, lw=1.0, rad=0.012, zorder=3)
    for frac in [0.25, 0.5, 0.75]:
        ly = mb + mh * frac
        ax.plot([ml + 0.015, ml + mw - 0.015], [ly, ly],
                color='#C0CAD8', lw=0.6, transform=ax.transAxes, zorder=3.5)
    ax.text(mx, my, 'LLM', fontsize=12, color=SLATE, fontweight='bold',
            transform=ax.transAxes, va='center', ha='center', zorder=4)

    # Arrows: EN → model
    ax.annotate('', xy=(ml + mw * 0.15, mb + mh),
                xytext=(en_x + 0.02, en_y - ph/2 - 0.02),
                arrowprops=dict(arrowstyle='->', color=EN_BLUE, lw=1.3),
                xycoords='axes fraction', textcoords='axes fraction')
    # Arrows: ZH → model
    ax.annotate('', xy=(ml + mw * 0.85, mb + mh),
                xytext=(zh_x - 0.02, zh_y - ph/2 - 0.02),
                arrowprops=dict(arrowstyle='->', color=ZH_CORAL, lw=1.3),
                xycoords='axes fraction', textcoords='axes fraction')

    # Output labels
    out_y = Y + H * 0.16
    rpw, rph = W * 0.28, 0.055

    # Warsaw (left, blue #2C5F8A)
    w_x = X + W * 0.22
    rbox(ax, w_x - rpw/2, out_y - rph/2, rpw, rph,
         fc=BG_BLUE, ec=OUT_BLUE, lw=1.0, rad=0.012, zorder=3)
    ax.text(w_x, out_y, 'Warsaw', fontsize=10, color=OUT_BLUE, fontweight='bold',
            transform=ax.transAxes, va='center', ha='center', zorder=4)
    ax.text(w_x, out_y - rph/2 - 0.025, 'parametric', fontsize=6.5, color=TEXT_GRAY,
            transform=ax.transAxes, va='center', ha='center')

    # 巴黎 (right, orange #D35400)
    p_x = X + W * 0.78
    rbox(ax, p_x - rpw/2, out_y - rph/2, rpw, rph,
         fc=BG_CORAL, ec=OUT_ORANGE, lw=1.0, rad=0.012, zorder=3)
    ax.text(p_x, out_y, '巴黎', fontsize=10.5, color=OUT_ORANGE,
            fontweight='bold',
            transform=ax.transAxes, va='center', ha='center', zorder=4,
            fontproperties=CJK_B)
    ax.text(p_x, out_y - rph/2 - 0.025, 'contextual', fontsize=6.5, color=TEXT_GRAY,
            transform=ax.transAxes, va='center', ha='center')

    # Arrows: model → outputs
    ax.annotate('', xy=(w_x, out_y + rph/2 + 0.01),
                xytext=(ml + mw * 0.2, mb),
                arrowprops=dict(arrowstyle='->', color=OUT_BLUE, lw=1.3),
                xycoords='axes fraction', textcoords='axes fraction')
    ax.annotate('', xy=(p_x, out_y + rph/2 + 0.01),
                xytext=(ml + mw * 0.8, mb),
                arrowprops=dict(arrowstyle='->', color=OUT_ORANGE, lw=1.3),
                xycoords='axes fraction', textcoords='axes fraction')

    # Conflict symbol between outputs
    ax.text(X + W/2, out_y, '⚡', fontsize=15, color=OUT_ORANGE,
            transform=ax.transAxes, va='center', ha='center', zorder=5,
            bbox=dict(fc=WHITE, ec='none', pad=1.5))

    # Citation
    ax.text(X + W/2, Y + H * 0.03, 'ConflictQA (Xie et al., 2024)',
            fontsize=7, color=SLATE, fontstyle='italic',
            transform=ax.transAxes, va='center', ha='center')


# ═══════════════════════════════════════════
# Panel (b): Detection (Probing)
# ═══════════════════════════════════════════

def draw_b(ax):
    X, Y, W, H = panel_frame(ax, '(b) Detection (Probing)')

    # Layer stack block (wider for readability)
    sx, sy = X + W*0.15, Y + H*0.22
    sw, sh = W*0.26, H*0.60
    rbox(ax, sx, sy, sw, sh, fc=BG_LAYER, ec=BORDER, lw=0.6, rad=0.01, zorder=2)
    for f in (0.25, 0.50, 0.75):
        ax.plot([sx+0.005, sx+sw-0.005], [sy+f*sh]*2,
                color='#D0D8E0', lw=0.3, transform=ax.transAxes, zorder=2.2)
    # Teal gradient zones
    rbox(ax, sx+0.004, sy+sh*0.30, sw-0.008, sh*0.35,
         fc=TEAL_LT, ec='none', lw=0, rad=0.005, alpha=0.5, zorder=2.4)
    rbox(ax, sx+0.004, sy+sh*0.65, sw-0.008, sh*0.32,
         fc=TEAL_MD, ec='none', lw=0, rad=0.005, alpha=0.6, zorder=2.4)
    # Layer labels
    for f, t in [(0.02, 'L1'), (0.50, 'L16'), (0.97, 'L32')]:
        ax.text(sx-0.02, sy+f*sh, t, fontsize=7, color=SLATE,
                transform=ax.transAxes, va='center', ha='right')
    ax.text(sx+sw/2, sy-0.035, 'Input', fontsize=8, color=SLATE,
            transform=ax.transAxes, va='center', ha='center')
    ax.text(sx+sw/2, sy+sh+0.035, 'Output', fontsize=8, color=SLATE,
            transform=ax.transAxes, va='center', ha='center')
    ax.annotate('', xy=(sx+sw/2, sy-0.005), xytext=(sx+sw/2, sy-0.025),
                arrowprops=dict(arrowstyle='->', color=SLATE, lw=1),
                xycoords='axes fraction', textcoords='axes fraction')
    ax.annotate('', xy=(sx+sw/2, sy+sh+0.025), xytext=(sx+sw/2, sy+sh+0.005),
                arrowprops=dict(arrowstyle='->', color=SLATE, lw=1),
                xycoords='axes fraction', textcoords='axes fraction')

    # Probe badge
    pk = sy + sh*0.82
    px = sx - 0.05
    rbox(ax, px-0.016, pk-0.016, 0.032, 0.032,
         fc=TEAL, ec='none', rad=0.016, zorder=5)
    ax.text(px, pk, 'P', fontsize=8, color=WHITE, fontweight='bold',
            transform=ax.transAxes, va='center', ha='center', zorder=6)

    # Detection peak — straight arrow, label to the right of the bar
    ax.annotate('Detection\npeak',
                xy=(sx+sw+0.01, pk),
                xytext=(sx+sw+0.10, pk),
                fontsize=8.5, color=TEAL, fontweight='bold',
                transform=ax.transAxes, va='center', ha='left', linespacing=1.2,
                arrowprops=dict(arrowstyle='->', color=TEAL, lw=1.2))

    # Conflict signal annotation — straight arrow
    my = sy + sh*0.47
    ax.annotate('Conflict signal\nacross layers',
                xy=(sx+sw+0.01, my),
                xytext=(sx+sw+0.10, my),
                fontsize=8, color=SLATE, fontstyle='italic',
                transform=ax.transAxes, va='center', ha='left', linespacing=1.2,
                arrowprops=dict(arrowstyle='->', color=SLATE, lw=0.8))

    # Model pills
    py = Y + H*0.08
    mpill(ax, X+W*0.18, py, 'Llama', True)
    mpill(ax, X+W*0.50, py, 'Qwen',  True)
    mpill(ax, X+W*0.82, py, 'Gemma', True)
    ax.text(X+W/2, py-0.03, 'All models detect conflict',
            fontsize=7.5, color=SLATE, fontstyle='italic',
            transform=ax.transAxes, va='center', ha='center')
    ax.text(X+W/2, py-0.06, '(see Fig. 3 for details)',
            fontsize=7, color=TEXT_GRAY,
            transform=ax.transAxes, va='center', ha='center')


# ═══════════════════════════════════════════
# Panel (c): Causation (Steering)
# ═══════════════════════════════════════════

def draw_c(ax):
    X, Y, W, H = panel_frame(ax, '(c) Causation (Steering)')

    # Layer stack
    sx, sy = X + W*0.06, Y + H*0.28
    sw, sh = W*0.16, H*0.56
    rbox(ax, sx, sy, sw, sh, fc=BG_LAYER, ec=BORDER, lw=0.6, rad=0.01, zorder=2)
    for f in (0.25, 0.50, 0.75):
        ax.plot([sx+0.004, sx+sw-0.004], [sy+f*sh]*2,
                color='#D0D8E0', lw=0.3, transform=ax.transAxes, zorder=2.2)

    # Causal window L13-L16
    cf0, cf1 = 12/32, 16/32
    rbox(ax, sx+0.004, sy+sh*cf0, sw-0.008, sh*(cf1-cf0),
         fc=CORAL_BG, ec=ZH_CORAL, lw=0.8, rad=0.005, alpha=0.7, zorder=2.5)
    # Upper neutral zone L24-L32
    uf = 24/32
    rbox(ax, sx+0.004, sy+sh*uf, sw-0.008, sh*(1-uf)-0.004,
         fc='#E8E8E8', ec='none', lw=0, rad=0.005, alpha=0.35, zorder=2.5)

    # Layer labels
    for ln, fy in [(1, 0.5/32), (13, 12.5/32), (16, 15.5/32), (32, 31.5/32)]:
        c = ZH_CORAL if ln in (13, 16) else SLATE
        wt = 'bold' if ln in (13, 16) else 'normal'
        ax.text(sx-0.015, sy+fy*sh, f'L{ln}', fontsize=7, color=c,
                fontweight=wt, transform=ax.transAxes, va='center', ha='right')
    ax.text(sx+sw/2, sy-0.035, 'Input', fontsize=8, color=SLATE,
            transform=ax.transAxes, va='center', ha='center')
    ax.text(sx+sw/2, sy+sh+0.035, 'Output', fontsize=8, color=SLATE,
            transform=ax.transAxes, va='center', ha='center')
    ax.annotate('', xy=(sx+sw/2, sy-0.005), xytext=(sx+sw/2, sy-0.025),
                arrowprops=dict(arrowstyle='->', color=SLATE, lw=1),
                xycoords='axes fraction', textcoords='axes fraction')
    ax.annotate('', xy=(sx+sw/2, sy+sh+0.025), xytext=(sx+sw/2, sy+sh+0.005),
                arrowprops=dict(arrowstyle='->', color=SLATE, lw=1),
                xycoords='axes fraction', textcoords='axes fraction')

    # Annotations
    ann_x = sx + sw + 0.02
    cwm = sy + sh*(cf0+cf1)/2
    ax.annotate('Causal\nWindow',
                xy=(sx+sw, cwm), xytext=(ann_x, cwm+0.03),
                fontsize=7.5, color=ZH_CORAL, fontweight='bold',
                transform=ax.transAxes, va='center', ha='left', linespacing=1.1,
                arrowprops=dict(arrowstyle='->', color=ZH_CORAL, lw=0.8))
    upm = sy + sh*(uf+1)/2
    ax.annotate('Upper layers\n(no causal effect)',
                xy=(sx+sw, upm), xytext=(ann_x, upm),
                fontsize=7, color=TEXT_GRAY, fontstyle='italic',
                transform=ax.transAxes, va='center', ha='left', linespacing=1.1,
                arrowprops=dict(arrowstyle='->', color=TEXT_GRAY, lw=0.6))

    # Effect bars with guide lines for alignment
    bx = X + W*0.42
    bmax = W*0.38
    for layer, eff, label, color, sig in [
        (13, 0.90, 'p < 0.001 ***',     ZH_CORAL,  True),
        (16, 0.55, 'p = 0.005 **',      ZH_CORAL,  True),
        (28, 0.07, 'p = 0.284 (n.s.)',  TEXT_GRAY,  False),
    ]:
        yy = sy + (layer - 0.5) / 32 * sh
        # Guide line from stack to bar
        ax.plot([sx + sw + 0.005, bx - 0.005], [yy, yy],
                color='#E8E8E8', lw=0.4, ls=':', transform=ax.transAxes, zorder=1.5)
        bw, bh = eff * bmax, 0.014
        rbox(ax, bx, yy-bh/2, bw, bh, fc=color, ec='none', lw=0,
             rad=bh/2, alpha=0.8 if sig else 0.3, zorder=3)
        ax.text(bx+bw+0.012, yy, label, fontsize=7, color=color,
                fontweight='bold' if sig else 'normal',
                transform=ax.transAxes, va='center', ha='left')

    ax.text(bx+bmax/2, sy-0.055, 'Causal Effect (ATE)',
            fontsize=8, color=SLATE, transform=ax.transAxes,
            va='center', ha='center')

    # Model pills
    py = Y + H*0.14
    mpill(ax, X+W*0.18, py, 'Llama', True)
    mpill(ax, X+W*0.50, py, 'Qwen',  False)
    mpill(ax, X+W*0.82, py, 'Gemma', False)
    ax.text(X+W/2, py-0.035, 'Only Llama shows causal effect',
            fontsize=7.5, color=SLATE, fontstyle='italic',
            transform=ax.transAxes, va='center', ha='center')

    # Detection ≠ Decision pill
    cy_ = Y + H*0.03
    pw, ph = 0.52, 0.05
    rbox(ax, X+W/2-pw/2, cy_-ph/2, pw, ph,
         fc=NAVY, ec='none', lw=0, rad=ph/2, zorder=5)
    ax.text(X+W/2, cy_, 'Detection  ≠  Decision',
            fontsize=11, color=WHITE, fontweight='bold',
            transform=ax.transAxes, va='center', ha='center', zorder=6)


# ═══════════════════════════════════════════
# Compose — wider gaps between panels
# ═══════════════════════════════════════════

fig = plt.figure(figsize=(16, 6), dpi=300, facecolor=WHITE)
draw_a(fig.add_axes([0.01,  0.02, 0.27,  0.96]))
draw_b(fig.add_axes([0.335, 0.02, 0.30,  0.96]))
draw_c(fig.add_axes([0.685, 0.02, 0.305, 0.96]))

os.makedirs('figures/paper', exist_ok=True)
for ext in ('png', 'pdf'):
    plt.savefig(f'figures/paper/fig1_hero.{ext}', dpi=300,
                bbox_inches='tight', pad_inches=0.04, facecolor=WHITE)
plt.close()
print('Done: figures/paper/fig1_hero.png + fig1_hero.pdf')
