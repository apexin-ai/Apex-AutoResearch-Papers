#!/usr/bin/env python3
"""Generate VLA architecture figure: 4 connector types × fragility gradient.
Designed at paper width (~7.2in) so fonts render at correct final size."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'figure.dpi': 300,
    'savefig.dpi': 300,
})

# ── Colors ──────────────────────────────────────────────────────────────────
GREEN, YELLOW, ORANGE, RED = '#27AE60', '#F39C12', '#E67E22', '#E74C3C'
GRAY_FILL, GRAY_BORDER = '#F2F3F4', '#D5D8DC'
TITLE_COLOR = '#2C3E50'
ARROW_CLR = '#AAAAAA'

def darker(c, f=0.72):
    r, g, b = int(c[1:3],16), int(c[3:5],16), int(c[5:7],16)
    return f'#{int(r*f):02x}{int(g*f):02x}{int(b*f):02x}'

# ── Data ────────────────────────────────────────────────────────────────────
cols_data = [
    dict(title=r'$\pi_{0.5}$',     enc='SigLIP',           tok='768',
         cm='Linear Projection',    cs='1 patch → 1 token',
         llm='PaliGemma 2B → Action', cv='0.055', cat='Uniformly Critical',    clr=GREEN),
    dict(title='X-VLA',             enc='DaViT (Florence-2)', tok='50',
         cm='Linear + 12L BART',    cs='deep mixing',
         llm='Florence-2 Enc → Action', cv='0.151', cat='Threshold-Graded',     clr=YELLOW),
    dict(title='OpenVLA',           enc='DINOv2 + SigLIP',  tok='256',
         cm='3-Layer MLP',          cs='GELU, nonlinear mixing',
         llm='Llama-2 7B → Action',   cv='0.215', cat='Smooth Graded',        clr=ORANGE),
    dict(title='SmolVLA',           enc='SigLIP',           tok='128',
         cm='Pixel-Shuffle 4×',     cs='4×4 → 1 token',
         llm='SmolLM2 360M → Action',  cv='0.314', cat='Catastrophic Cliff',   clr=RED),
]

# ── Layout ──────────────────────────────────────────────────────────────────
FW, FH = 7.2, 4.2
BW = 1.45                      # box width
BH_E, BH_C, BH_L = 0.38, 0.55, 0.38   # encoder / connector / llm heights
RR = 0.04
MARGIN = 0.30
COL_SP = (FW - 2*MARGIN) / 4
CXS = [MARGIN + COL_SP*(i+0.5) for i in range(4)]

# Y grid (top→bottom)
YT  = 3.85   # title
YE  = 3.38   # encoder center
YC  = 2.40   # connector center
YL  = 1.47   # llm center
YCV = 0.92   # CV text
YCA = 0.67   # category label
YG  = 0.28   # gradient bar

fig, ax = plt.subplots(figsize=(FW, FH))
ax.set_xlim(0, FW); ax.set_ylim(0, FH)
ax.axis('off')
fig.patch.set_facecolor('white')

# ── Helpers ─────────────────────────────────────────────────────────────────
def box(cx, cy, w, h, fc, ec, txt, fs=8.5, tc='#444', fw='normal',
        shadow=False, sub=None, sub_fs=7, sub_tc=None, lw=0.7):
    x0, y0 = cx-w/2, cy-h/2
    if shadow:
        ax.add_patch(FancyBboxPatch(
            (x0+0.02, y0-0.02), w, h,
            boxstyle=f"round,pad=0,rounding_size={RR}",
            fc='#00000009', ec='none', zorder=1))
    ax.add_patch(FancyBboxPatch(
        (x0, y0), w, h,
        boxstyle=f"round,pad=0,rounding_size={RR}",
        fc=fc, ec=ec, lw=lw, zorder=2))
    if sub:
        ax.text(cx, cy+0.08, txt, ha='center', va='center',
                fontsize=fs, fontweight=fw, color=tc, zorder=3, linespacing=1.05)
        ax.text(cx, cy-0.13, sub, ha='center', va='center',
                fontsize=sub_fs, fontstyle='italic',
                color=sub_tc or tc, zorder=3, alpha=0.85)
    else:
        ax.text(cx, cy, txt, ha='center', va='center',
                fontsize=fs, fontweight=fw, color=tc, zorder=3, linespacing=1.05)

def arw(x, y1, y2):
    ax.add_patch(FancyArrowPatch(
        (x, y1), (x, y2), arrowstyle='->', mutation_scale=9,
        lw=0.9, color=ARROW_CLR, zorder=1))

# ── Draw columns ───────────────────────────────────────────────────────────
for i, d in enumerate(cols_data):
    cx = CXS[i]

    # Title
    ax.text(cx, YT, d['title'], ha='center', va='center',
            fontsize=10.5, fontweight='bold', color=TITLE_COLOR, zorder=3)

    # Encoder box
    box(cx, YE, BW, BH_E, GRAY_FILL, GRAY_BORDER, d['enc'], fs=8.5, tc='#444')

    # Arrow: encoder → connector
    arw(cx, YE - BH_E/2, YC + BH_C/2)

    # Token count — small bubble annotation on the arrow
    ym = (YE - BH_E/2 + YC + BH_C/2) / 2
    tok_txt = f'{d["tok"]} tok'
    ax.text(cx, ym, tok_txt, ha='center', va='center',
            fontsize=6.5, color='#888888', zorder=4,
            bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.9))

    # Connector box
    box(cx, YC, BW, BH_C, d['clr'], darker(d['clr']), d['cm'],
        fs=8, tc='white', fw='bold', shadow=True,
        sub=d['cs'], sub_fs=6.5, sub_tc='#ffffffcc', lw=0.9)

    # Arrow: connector → LLM
    arw(cx, YC - BH_C/2, YL + BH_L/2)

    # LLM box
    box(cx, YL, BW, BH_L, GRAY_FILL, GRAY_BORDER, d['llm'], fs=7.2, tc='#444')

    # CV value
    ax.text(cx, YCV, f'CV = {d["cv"]}', ha='center', va='center',
            fontsize=7.5, color='#555', zorder=3)

    # Category label
    ax.text(cx, YCA, d['cat'], ha='center', va='center',
            fontsize=7.5, fontweight='bold', fontstyle='italic',
            color=d['clr'], zorder=3)

# ── Gradient bar ────────────────────────────────────────────────────────────
xl, xr = CXS[0] - BW/2, CXS[3] + BW/2
cmap = LinearSegmentedColormap.from_list('f', [GREEN, YELLOW, ORANGE, RED])
N = 400; xs = np.linspace(xl, xr, N); bh = 0.045
for j in range(N-1):
    ax.add_patch(plt.Rectangle(
        (xs[j], YG-bh/2), xs[j+1]-xs[j], bh,
        fc=cmap(j/(N-1)), ec='none', zorder=2))

ax.add_patch(FancyArrowPatch(
    (xr-0.10, YG), (xr+0.08, YG),
    arrowstyle='->', mutation_scale=10, lw=1.2, color=RED, zorder=3))

ax.text((xl+xr)/2, YG-0.14,
        'Increasing Fragility  (CV: 0.055 → 0.314)',
        ha='center', va='top', fontsize=7.5, color='#777', zorder=3)

# ── Save ────────────────────────────────────────────────────────────────────
out = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper'
for ext in ('png', 'pdf'):
    plt.savefig(f'{out}/fig_architecture_v2.{ext}',
                bbox_inches='tight', pad_inches=0.08, dpi=300, facecolor='white')
plt.close()
print("Saved PNG + PDF")
