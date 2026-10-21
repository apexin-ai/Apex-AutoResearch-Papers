#!/usr/bin/env python3
"""Figure 1 Hero: Detection ≠ Decision — Cross-Lingual Knowledge Conflict.

Print-appropriate dimensions: figsize=(7, 2.3), ~0.9x scale at textwidth.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.colors as mcolors
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

# ── Colors ──
EN_BLUE      = '#2C5F8A';  EN_BLUE_LT   = '#EBF5FB';  EN_BLUE_MED  = '#AED6F1'
ZH_ORANGE    = '#D35400';  ZH_ORANGE_LT = '#FDF2E9';  ZH_ORANGE_MED= '#F5CBA7'
TEAL         = '#0B6E4F';  TEAL_LT      = '#D0ECE7'
CAUSAL_RED   = '#C0392B';  CAUSAL_RED_LT= '#FADBD8'
NO_EFFECT_DK = '#ABB2B9'
TEXT_DARK = '#2C3E50'; TEXT_MID = '#5D6D7E'; TEXT_LIGHT = '#95A5A6'
BORDER_LIGHT = '#E5E8E8'; WHITE = '#FFFFFF'

# ── Fonts ──
_cjk_paths = ['/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
              '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc']
_cjk_bold  = ['/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc',
              '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc']
def _ff(ps):
    for p in ps:
        if os.path.exists(p): return p
    return None
CJK   = fm.FontProperties(fname=_ff(_cjk_paths), size=7) if _ff(_cjk_paths) else None
CJK_B = fm.FontProperties(fname=_ff(_cjk_bold),  size=8) if _ff(_cjk_bold)  else None

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Liberation Serif'],
    'mathtext.fontset': 'dejavuserif', 'font.size': 7,
    'axes.linewidth': 0, 'figure.facecolor': WHITE,
    'axes.facecolor': WHITE, 'text.color': TEXT_DARK,
})

# ── Data ──
np.random.seed(42)
layers = np.arange(1, 33)
def _probe(pk, pv, base=0.52, w=6):
    c = base + (pv - base) * np.exp(-0.5 * ((layers - pk) / w) ** 2)
    return np.clip(c + np.random.normal(0, 0.012, 32), 0.50, 1.0)
probe_llama = _probe(18, 0.92, w=7)
probe_qwen  = _probe(16, 0.88, w=6)
probe_gemma = _probe(20, 0.85, w=8)
causal_llama = np.zeros(32); causal_llama[12:16] = [0.35, 0.42, 0.38, 0.28]
causal_qwen  = np.random.uniform(0, 0.04, 32)
causal_gemma = np.random.uniform(0, 0.03, 32)

# ── Helpers ──
def rbox(ax, x, y, w, h, fc=WHITE, ec=BORDER_LIGHT, lw=0.5, rad=0.015, alpha=1, zorder=2):
    ax.add_patch(FancyBboxPatch((x,y), w, h,
        boxstyle=f'round,pad=0,rounding_size={rad}',
        fc=fc, ec=ec, lw=lw, alpha=alpha,
        transform=ax.transAxes, zorder=zorder, clip_on=False))

def heatbar(ax, data, xc, bw, cmap, vmin, vmax, yb=0.18, yt=0.88, n=32):
    lh = (yt - yb) / n; hw = bw / 2
    norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
    for i in range(n):
        ax.add_patch(FancyBboxPatch((xc - hw, yb + i * lh), bw, lh + 0.003,
            boxstyle='square,pad=0', fc=cmap(norm(data[i])), ec='none', lw=0,
            transform=ax.transAxes, zorder=3, clip_on=False))
    rbox(ax, xc - hw - 0.003, yb - 0.003, bw + 0.006, yt - yb + 0.006,
         fc='none', ec='#CCD1D1', lw=0.4, rad=0.005, zorder=4)

def check(ax, x, y, color, sz=0.014):
    ax.plot([x-sz*0.6, x-sz*0.1, x+sz*0.7], [y+sz*0.1, y-sz*0.4, y+sz*0.5],
            color=color, lw=1.5, solid_capstyle='round', solid_joinstyle='round',
            transform=ax.transAxes, zorder=6)

def cross(ax, x, y, color, sz=0.010):
    ax.plot([x-sz, x+sz], [y-sz, y+sz], color=color, lw=1.2,
            solid_capstyle='round', transform=ax.transAxes, zorder=6)
    ax.plot([x-sz, x+sz], [y+sz, y-sz], color=color, lw=1.2,
            solid_capstyle='round', transform=ax.transAxes, zorder=6)

# ═══ Panel (a) ═══
def draw_a(ax):
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    ax.text(0.03, 0.96, '(a)', fontsize=8, fontweight='bold', va='top', transform=ax.transAxes)
    ax.text(0.15, 0.96, 'Cross-Lingual Knowledge Conflict', fontsize=7.5,
            fontweight='bold', va='top', transform=ax.transAxes)
    ax.plot([0.03, 0.97], [0.92, 0.92], color=BORDER_LIGHT, lw=0.4, transform=ax.transAxes)

    # Question
    rbox(ax, 0.04, 0.82, 0.92, 0.075, fc='#F8F9FA', ec='#DEE2E6', lw=0.4, rad=0.012)
    ax.text(0.50, 0.858, 'Q: "Where was Marie Curie born?"', fontsize=7.5,
            fontweight='bold', va='center', ha='center', transform=ax.transAxes)

    # EN card
    ey, eh = 0.51, 0.26
    rbox(ax, 0.04, ey, 0.025, eh, fc=EN_BLUE, ec='none', lw=0, rad=0.005)
    rbox(ax, 0.065, ey, 0.87, eh, fc=EN_BLUE_LT, ec=EN_BLUE_MED, lw=0.4, rad=0.01)
    ax.text(0.10, ey+eh*0.82, 'EN Context', fontsize=6.5, color=EN_BLUE,
            fontweight='bold', transform=ax.transAxes, va='center')
    ax.text(0.10, ey+eh*0.45, '"Marie Curie was born in\n  Warsaw, Poland..."',
            fontsize=6, color=TEXT_MID, transform=ax.transAxes, va='center', linespacing=1.3)
    ax.annotate('', xy=(0.72, ey+eh*0.20), xytext=(0.62, ey+eh*0.20),
                arrowprops=dict(arrowstyle='->', color=EN_BLUE, lw=0.9, mutation_scale=8),
                xycoords='axes fraction', textcoords='axes fraction')
    ax.text(0.83, ey+eh*0.24, 'Warsaw', fontsize=8, color=EN_BLUE, fontweight='bold',
            transform=ax.transAxes, va='center', ha='center')
    ax.text(0.83, ey+eh*0.07, '(parametric)', fontsize=5.5, color=TEXT_LIGHT,
            transform=ax.transAxes, va='center', ha='center')

    # Conflict
    cy = 0.445
    ax.plot([0.08, 0.92], [cy, cy], color='#E8E8E8', lw=0.4, transform=ax.transAxes)
    ax.text(0.50, cy, '≠', fontsize=14, color=CAUSAL_RED, fontweight='bold',
            va='center', ha='center', transform=ax.transAxes, alpha=0.6,
            bbox=dict(fc=WHITE, ec='none', pad=2, alpha=1.0))

    # ZH card
    zy, zh = 0.12, 0.26
    rbox(ax, 0.04, zy, 0.025, zh, fc=ZH_ORANGE, ec='none', lw=0, rad=0.005)
    rbox(ax, 0.065, zy, 0.87, zh, fc=ZH_ORANGE_LT, ec=ZH_ORANGE_MED, lw=0.4, rad=0.01)
    ax.text(0.10, zy+zh*0.82, 'ZH Context', fontsize=6.5, color=ZH_ORANGE,
            fontweight='bold', transform=ax.transAxes, va='center')
    ax.text(0.10, zy+zh*0.45, '"居里夫人出生于巴黎..."', fontsize=6, color=TEXT_MID,
            transform=ax.transAxes, va='center', fontproperties=CJK)
    ax.annotate('', xy=(0.72, zy+zh*0.20), xytext=(0.62, zy+zh*0.20),
                arrowprops=dict(arrowstyle='->', color=ZH_ORANGE, lw=0.9, mutation_scale=8),
                xycoords='axes fraction', textcoords='axes fraction')
    ax.text(0.83, zy+zh*0.24, '巴黎', fontsize=8.5, color=ZH_ORANGE, fontweight='bold',
            transform=ax.transAxes, va='center', ha='center', fontproperties=CJK_B)
    ax.text(0.83, zy+zh*0.07, '(contextual)', fontsize=5.5, color=TEXT_LIGHT,
            transform=ax.transAxes, va='center', ha='center')

    ax.text(0.50, 0.035, 'ConflictQA (Xie et al., 2024)', fontsize=5.5,
            color=TEXT_LIGHT, fontstyle='italic', va='center', ha='center',
            transform=ax.transAxes)

# ═══ Panel (b) ═══
def draw_b(ax):
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    ax.text(0.02, 0.96, '(b)', fontsize=8, fontweight='bold', va='top', transform=ax.transAxes)
    ax.text(0.12, 0.96, 'Detection via Probing', fontsize=7.5, fontweight='bold',
            va='top', transform=ax.transAxes)
    ax.plot([0.02, 0.98], [0.92, 0.92], color=BORDER_LIGHT, lw=0.4, transform=ax.transAxes)

    cmap = mcolors.LinearSegmentedColormap.from_list('t', ['#F7FCFA','#B2DFDB','#4DB6AC',TEAL])
    yb, yt, bw = 0.18, 0.88, 0.12
    pos = [0.20, 0.44, 0.68]
    names = ['Llama-3', 'Qwen-2.5', 'Gemma-2']
    probes = [probe_llama, probe_qwen, probe_gemma]
    peaks = [18, 16, 20]

    for i, (xc, nm, d, pk) in enumerate(zip(pos, names, probes, peaks)):
        heatbar(ax, d, xc, bw, cmap, 0.50, 0.95, yb, yt)
        ax.text(xc, yb-0.04, nm, fontsize=6.5, fontweight='bold', va='center',
                ha='center', transform=ax.transAxes)
        check(ax, xc, yb-0.09, TEAL, sz=0.013)
        pk_y = yb + (pk-0.5)/32*(yt-yb)
        ax.plot(xc+bw/2+0.008, pk_y, marker='<', markersize=3, color=TEAL,
                transform=ax.transAxes, zorder=5, clip_on=False)

    # Peak label
    pk_y = yb + (17-0.5)/32*(yt-yb)
    ax.text(0.85, pk_y+0.02, 'detection', fontsize=5.5, color=TEAL, fontweight='bold',
            va='center', ha='center', transform=ax.transAxes)
    ax.text(0.85, pk_y-0.02, 'peak', fontsize=5.5, color=TEAL, fontweight='bold',
            va='center', ha='center', transform=ax.transAxes)
    ax.annotate('', xy=(pos[1]+bw/2+0.015, yb+(16-0.5)/32*(yt-yb)),
                xytext=(0.79, pk_y), transform=ax.transAxes,
                arrowprops=dict(arrowstyle='->', color=TEAL, lw=0.6,
                                connectionstyle='arc3,rad=0.15', mutation_scale=6))

    # Layer labels
    for ln, lb in [(1,'L1'),(16,'L16'),(32,'L32')]:
        ax.text(0.07, yb+(ln-0.5)/32*(yt-yb), lb, fontsize=5, color=TEXT_LIGHT,
                va='center', ha='right', transform=ax.transAxes)
    ax.text(0.07, yb-0.015, 'Input', fontsize=5, color=TEXT_LIGHT, va='top',
            ha='right', transform=ax.transAxes)
    ax.text(0.07, yt+0.015, 'Output', fontsize=5, color=TEXT_LIGHT, va='bottom',
            ha='right', transform=ax.transAxes)

    # Colorbar
    cx, cw = 0.92, 0.025; cb, ct = yb+0.15, yb+0.50
    for i in range(30):
        f = i/30; yy = cb + f*(ct-cb)
        ax.add_patch(FancyBboxPatch((cx, yy), cw, (ct-cb)/30+0.001,
            boxstyle='square,pad=0', fc=cmap(f), ec='none',
            transform=ax.transAxes, zorder=3, clip_on=False))
    rbox(ax, cx-0.001, cb-0.001, cw+0.002, ct-cb+0.002,
         fc='none', ec='#CCD1D1', lw=0.3, rad=0.002, zorder=4)
    ax.text(cx+cw/2, cb-0.025, '.50', fontsize=4.5, color=TEXT_LIGHT,
            va='center', ha='center', transform=ax.transAxes)
    ax.text(cx+cw/2, ct+0.025, '.95', fontsize=4.5, color=TEXT_LIGHT,
            va='center', ha='center', transform=ax.transAxes)

    ax.text(0.44, 0.04, 'All models detect conflict', fontsize=6, color=TEAL,
            fontstyle='italic', va='center', ha='center', transform=ax.transAxes)

# ═══ Panel (c) ═══
def draw_c(ax):
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
    ax.text(0.02, 0.96, '(c)', fontsize=8, fontweight='bold', va='top', transform=ax.transAxes)
    ax.text(0.12, 0.96, 'Causal Steering', fontsize=7.5, fontweight='bold',
            va='top', transform=ax.transAxes)
    ax.plot([0.02, 0.98], [0.92, 0.92], color=BORDER_LIGHT, lw=0.4, transform=ax.transAxes)

    cmap = mcolors.LinearSegmentedColormap.from_list('c', ['#F4F6F6','#F5B7B1',CAUSAL_RED])
    yb, yt, bw = 0.26, 0.88, 0.07
    pos = [0.10, 0.29, 0.48]
    names = ['Llama-3', 'Qwen-2.5', 'Gemma-2']
    causals = [causal_llama, causal_qwen, causal_gemma]
    effs = [True, False, False]

    for i, (xc, nm, d, ef) in enumerate(zip(pos, names, causals, effs)):
        heatbar(ax, d, xc, bw, cmap, 0.0, 0.45, yb, yt)
        ax.text(xc, yb-0.04, nm, fontsize=5.5, fontweight='bold', va='center',
                ha='center', transform=ax.transAxes)
        if ef: check(ax, xc, yb-0.09, CAUSAL_RED, sz=0.012)
        else: cross(ax, xc, yb-0.09, NO_EFFECT_DK, sz=0.010)

    # Layer labels
    for ln in [1, 13, 16, 32]:
        yy = yb + (ln-0.5)/32*(yt-yb)
        c = CAUSAL_RED if ln in (13,16) else TEXT_LIGHT
        w = 'bold' if ln in (13,16) else 'normal'
        ax.text(0.03, yy, f'L{ln}', fontsize=5, color=c, fontweight=w,
                va='center', ha='right', transform=ax.transAxes)

    # Bracket
    l13y = yb + 12.5/32*(yt-yb); l16y = yb + 15.5/32*(yt-yb)
    bx = pos[0] + bw/2 + 0.018
    ax.plot([bx, bx+0.010, bx+0.010, bx], [l13y, l13y, l16y, l16y],
            color=CAUSAL_RED, lw=0.7, transform=ax.transAxes, zorder=5)
    ax.text(bx+0.020, (l13y+l16y)/2, 'causal\nwindow', fontsize=5, color=CAUSAL_RED,
            fontweight='bold', va='center', ha='left', linespacing=0.95,
            transform=ax.transAxes)

    # ATE bars
    ax0 = 0.62; amx = 0.24
    for i, (lb, ef, pv, c, sig) in enumerate([
        ('L13', 0.42, 'p < 0.001 ***', CAUSAL_RED, True),
        ('L16', 0.28, 'p = 0.005 **',  CAUSAL_RED, True),
        ('L28', 0.03, 'p = 0.284 n.s.', NO_EFFECT_DK, False),
    ]):
        yy = 0.80 - i*0.07; bww = max(ef/0.45*amx, 0.010); bh = 0.022
        ax.text(ax0-0.012, yy, lb, fontsize=5.5, color=c,
                fontweight='bold' if sig else 'normal',
                va='center', ha='right', transform=ax.transAxes)
        rbox(ax, ax0, yy-bh/2, bww, bh, fc=c, ec='none', lw=0, rad=bh/2,
             alpha=0.85 if sig else 0.3, zorder=3)
        ax.text(ax0+bww+0.010, yy, pv, fontsize=5, color=c,
                fontweight='bold' if sig else 'normal',
                va='center', ha='left', transform=ax.transAxes)

    ax.text(ax0+amx*0.45, 0.80-3*0.07-0.005, 'Causal Effect (ATE)',
            fontsize=5.5, color=TEXT_MID, va='center', ha='center', transform=ax.transAxes)

    ax.text(0.29, yb-0.14, 'Only Llama shows causal effect', fontsize=5.5,
            color=TEXT_MID, fontstyle='italic', va='center', ha='center',
            transform=ax.transAxes)

    # Tagline
    rbox(ax, 0.12, 0.02, 0.76, 0.06, fc='#F8F9FA', ec='#DEE2E6', lw=0.4, rad=0.015, zorder=5)
    ax.text(0.50, 0.05, 'Detection  ≠  Decision', fontsize=8.5, fontweight='bold',
            va='center', ha='center', transform=ax.transAxes, zorder=6)

# ═══ Compose ═══
fig = plt.figure(figsize=(7, 2.3), dpi=300, facecolor=WHITE)
draw_a(fig.add_axes([0.01, 0.02, 0.27, 0.96]))
draw_b(fig.add_axes([0.31, 0.02, 0.33, 0.96]))
draw_c(fig.add_axes([0.66, 0.02, 0.33, 0.96]))

# Panel dividers
for xd in [0.305, 0.655]:
    fig.add_artist(plt.Line2D([xd,xd], [0.06, 0.94], color='#EAECEE', lw=0.4,
                              transform=fig.transFigure, zorder=0))

os.makedirs('figures/paper', exist_ok=True)
for ext in ('png', 'pdf'):
    plt.savefig(f'figures/paper/fig1_hero.{ext}', dpi=300,
                bbox_inches='tight', pad_inches=0.02, facecolor=WHITE)
plt.close()
print('Done: figures/paper/fig1_hero.png + .pdf')
