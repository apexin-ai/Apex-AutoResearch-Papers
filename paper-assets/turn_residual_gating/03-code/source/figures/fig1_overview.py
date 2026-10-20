"""Figure 1: ThreadGate Overview — three-panel causal narrative (v4)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patheffects as pe
import numpy as np
import os

ONE_MM = 1 / 25.4
FIG_W = 170 * ONE_MM
FIG_H = FIG_W * 8 / 16

C_OK   = '#009E73'
C_FAIL = '#D55E00'
C_GRAY = '#999999'
C_BLUE = '#0072B2'
C_AMB  = '#E69F00'
C_TXT  = '#222222'

WH_STROKE = [pe.withStroke(linewidth=2.5, foreground='white')]

plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'font.size': 7,
    'figure.dpi': 300, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'savefig.pad_inches': 0.02,
    'pdf.fonttype': 42, 'ps.fonttype': 42,
})

fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
ax.set_xlim(0, 16)
ax.set_ylim(0, 6)
ax.axis('off')

def rbox(x, y, w, h, fc='white', ec='#BBB', lw=0.6, zorder=2, pad=0.1):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad={pad}',
                        facecolor=fc, edgecolor=ec, linewidth=lw, zorder=zorder)
    ax.add_patch(p)

def arr(x1, y1, x2, y2, c='#444', lw=0.9, ls='-', rad=0.0, ms=7,
        shrA=1, shrB=1):
    a = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle=f'-|>,head_length={ms*0.15},head_width={ms*0.08}',
        connectionstyle=f'arc3,rad={rad}',
        color=c, linewidth=lw, linestyle=ls,
        shrinkA=shrA, shrinkB=shrB, zorder=4)
    ax.add_patch(a)

def txt(x, y, s, fs=7, c=C_TXT, ha='center', va='center', fw='normal', **kw):
    return ax.text(x, y, s, fontsize=fs, color=c, ha=ha, va=va,
                   fontweight=fw, zorder=5, **kw)

# ── panel dividers ───────────────────────────────────────────────
for xd in [5.25, 10.75]:
    ax.plot([xd, xd], [0.15, 5.75], color='#E0E0E0', lw=0.6,
            ls=(0, (4, 3)), zorder=0)

# ── panel headers ────────────────────────────────────────────────
txt(2.65, 5.65, 'Observation', fs=8, fw='bold', c=C_BLUE)
txt(8.0,  5.65, 'Intervention: ThreadGate', fs=8, fw='bold', c='#996600')
txt(13.4, 5.65, 'Result & Root Cause', fs=8, fw='bold', c=C_FAIL)

# ═══════════════════════════════════════════════════════════════════
#  LEFT PANEL
# ═══════════════════════════════════════════════════════════════════

dw, dh = 1.85, 0.30
dx = 0.35
turns = [
    ('System prompt', 5.0, C_BLUE, 'white'),
    ('User turn 1',   4.5, '#EDEDED', C_TXT),
    ('User turn 2',   4.05, '#EDEDED', C_TXT),
    ('User turn N',   3.15, '#EDEDED', C_TXT),
]
for lab, yd, fc, tc in turns:
    rbox(dx, yd, dw, dh, fc=fc, ec='#AAA', lw=0.5)
    txt(dx + dw/2, yd + dh/2, lab, fs=7, c=tc)

txt(dx + dw/2, 3.65, '⋮', fs=9, c=C_GRAY)

# Attention decay arrow
ax.annotate('', xy=(2.65, 3.22), xytext=(2.65, 5.15),
            arrowprops=dict(arrowstyle='-|>', color=C_FAIL, lw=1.4,
                           shrinkA=3, shrinkB=3, mutation_scale=10))
txt(3.15, 4.15, 'attention\ndecays', fs=7, c=C_FAIL, style='italic', ha='left')

# Attention ✗ / Residual ✓
txt(3.3, 3.65, '✗ attn path', fs=7, c=C_FAIL, ha='left')
txt(3.3, 3.35, '✓ resid path', fs=7, c=C_OK, ha='left')

# GAR decay curve
gax_l, gax_r = 0.4, 4.1
gay_b, gay_t = 1.1, 2.7
rbox(gax_l - 0.1, gay_b - 0.3, gax_r - gax_l + 0.2, gay_t - gay_b + 0.45,
     fc='#FAFAFA', ec='#E0E0E0', lw=0.4, zorder=1)

cx = np.linspace(0, 1, 50)
cy = np.exp(-3.0 * cx)
px = cx * (gax_r - gax_l) + gax_l
py = cy * (gay_t - gay_b - 0.2) + gay_b + 0.05

ax.plot(px, py, color=C_FAIL, lw=1.3, zorder=3)
ax.fill_between(px, gay_b, py, color=C_FAIL, alpha=0.06, zorder=1)

txt(gax_l + 0.05, gay_t + 0.12, 'GAR', fs=7, c=C_TXT, ha='left', fw='bold')
txt(gax_l, gay_b - 0.18, '1', fs=7, c=C_GRAY, ha='center')
txt(gax_r, gay_b - 0.18, 'N', fs=7, c=C_GRAY, ha='center')
txt((gax_l + gax_r)/2, gay_b - 0.18, 'Turn', fs=7, c=C_GRAY)

rbox(2.45, 1.6, 1.9, 0.38, fc='#FBE9E7', ec=C_FAIL, lw=0.6)
txt(3.4, 1.79, '↓ 70.8% (§3)', fs=7, c=C_FAIL, fw='bold')

# Residual stream persistence
rbox(0.25, 0.1, 4.8, 0.7, fc='#E8F5E9', ec=C_OK, lw=0.8)
txt(2.65, 0.58, 'Residual stream preserves goal info', fs=7,
    c='#00795C', fw='bold')
txt(2.65, 0.3, 'AUC = 0.98 (Dongre et al.)', fs=7, c=C_OK, style='italic')

# ═══════════════════════════════════════════════════════════════════
#  CENTER PANEL — architecture
# ═══════════════════════════════════════════════════════════════════

bx, bw = 7.1, 1.7

# input
rbox(bx, 0.3, bw, 0.4, fc='#E3F2FD', ec=C_BLUE, lw=0.7)
txt(bx + bw/2, 0.5, r'$\mathbf{x}_l$', fs=7, c=C_BLUE)

# transformer block
fb_x, fb_w = 6.25, 1.65
rbox(fb_x, 1.3, fb_w, 0.55, fc='#EEE', ec='#888', lw=0.7)
txt(fb_x + fb_w/2, 1.58, r'$f_l$ (block)', fs=7, c=C_TXT)

# gate
gx, gw = 8.6, 1.8
rbox(gx, 1.25, gw, 0.6, fc='#FFF3E0', ec=C_AMB, lw=1.0)
txt(gx + gw/2, 1.62, r'Gate $g_l$', fs=7, c='#996600', fw='bold')
txt(gx + gw/2, 1.38, r'$\sigma(b{+}\mathrm{MLP}(\mathbf{t}))$', fs=7, c='#777')

# multiply ⊗
mx, my = 8.2, 2.2
circ = Circle((mx, my), 0.18, fc='#FFF3E0', ec=C_AMB, lw=0.8, zorder=3)
ax.add_patch(circ)
txt(mx, my, '×', fs=9, c=C_AMB, fw='bold')

# add ⊕
sx, sy = 7.1, 2.65
circ2 = Circle((sx, sy), 0.18, fc='#E3F2FD', ec=C_BLUE, lw=0.8, zorder=3)
ax.add_patch(circ2)
txt(sx, sy, '+', fs=9, c=C_BLUE, fw='bold')

# output
rbox(bx, 3.0, bw, 0.4, fc='#E3F2FD', ec=C_BLUE, lw=0.7)
txt(bx + bw/2, 3.2, r'$\mathbf{x}_{l+1}$', fs=7, c=C_BLUE)

# -- wiring --
mid_x = bx + bw/2
arr(mid_x, 0.7, mid_x, 0.95, c='#555')

ax.plot([mid_x, fb_x + fb_w/2], [0.95, 0.95], color='#555', lw=0.7, zorder=3)
arr(fb_x + fb_w/2, 0.95, fb_x + fb_w/2, 1.3, c='#555')

# residual skip
skip_x = 5.9
ax.plot([mid_x, skip_x], [0.95, 0.95], color=C_BLUE, lw=0.9, ls='--', zorder=3)
ax.plot([skip_x, skip_x], [0.95, sy], color=C_BLUE, lw=0.9, ls='--', zorder=3)
arr(skip_x, sy, sx - 0.18, sy, c=C_BLUE, lw=0.9)
txt(5.65, 1.7, 'skip', fs=7, c=C_BLUE, style='italic',
    path_effects=WH_STROKE)

# f_l → ⊗
arr(fb_x + fb_w/2, 1.85, mx, my - 0.18, c='#555', rad=-0.05)
# gate → ⊗
arr(gx, 1.55, mx + 0.18, my, c=C_AMB, lw=0.8)
# ⊗ → ⊕
arr(mx - 0.18, my + 0.05, sx + 0.18, sy - 0.05, c='#555', rad=0.0)
# ⊕ → output
arr(sx + 0.05, sy + 0.18, bx + bw/2, 3.0, c='#555', rad=0.1)

# turn embedding → gate
arr(gx + gw/2, 0.85, gx + gw/2, 1.25, c=C_GRAY, lw=0.6, ls='--')
rbox(gx + 0.1, 0.48, gw - 0.2, 0.32, fc='#F5F5F5', ec=C_GRAY, lw=0.4)
txt(gx + gw/2, 0.64, 'turn embed', fs=7, c=C_GRAY, style='italic')

# formula
rbox(5.7, 3.75, 4.6, 0.5, fc='white', ec='#CCC', lw=0.5)
txt(8.0, 4.0, r'$x_{l+1} = x_l + g_l \cdot f_l(x_l)$', fs=8, c=C_TXT)

# hypothesis
rbox(5.85, 4.55, 4.3, 0.65, fc='#FAFAFA', ec='#DDD', lw=0.4)
txt(8.0, 5.0, 'Natural hypothesis:', fs=7, c=C_GRAY, fw='bold')
txt(8.0, 4.72, '"Gate should recover goal attention"',
    fs=7, c='#666', style='italic')

# inter-panel arrows
arr(5.1, 2.8, 5.5, 2.8, c=C_GRAY, lw=0.7, ls='--')
arr(10.55, 2.8, 10.9, 2.8, c=C_GRAY, lw=0.7, ls='--')

# ═══════════════════════════════════════════════════════════════════
#  RIGHT PANEL
# ═══════════════════════════════════════════════════════════════════

# Training + IID evaluation success
rbox(11.05, 4.3, 4.55, 1.15, fc='#E8F5E9', ec=C_OK, lw=0.8)
txt(11.3, 5.2, '✓ Training:', fs=7, c=C_OK, fw='bold', ha='left')
txt(13.5, 5.2, 'GAR 0.02→0.48', fs=7, c=C_TXT, ha='left')
txt(11.3, 4.82, '✓ IID eval:', fs=7, c=C_OK, fw='bold', ha='left')
txt(13.5, 4.82, 'GAR = 0.49', fs=7, c=C_TXT, ha='left')
txt(15.45, 4.45, '(§5, Table 1)', fs=7, c=C_GRAY, ha='right', style='italic')

# Arrow
arr(13.25, 4.28, 13.25, 3.95, c='#555', lw=0.7)

# Inference failure
rbox(11.05, 2.5, 4.55, 1.4, fc='#FBE9E7', ec=C_FAIL, lw=1.5)
txt(13.33, 3.65, '✗ Model-generated text', fs=7, c=C_FAIL, fw='bold')
txt(13.33, 3.15, 'GAR = 0.016', fs=11, c=C_FAIL, fw='bold',
    path_effects=[pe.withStroke(linewidth=3, foreground='white')])
txt(15.4, 3.5, '(Table 1)', fs=7, c='#AA4400', ha='right', style='italic')

# 30x badge
rbox(12.0, 2.55, 2.65, 0.35, fc=C_FAIL, ec=C_FAIL, lw=0, pad=0.06)
txt(13.33, 2.73, '30× generalization gap', fs=7, c='white', fw='bold')

# Mechanism analysis
txt(11.2, 2.15, 'Mechanism analysis:', fs=7, c=C_TXT, fw='bold', ha='left')

# ① ruled out — PCGrad ablation (§6.3)
txt(11.4, 1.85, '① Gradient conflict → PCGrad', fs=7,
    c=C_GRAY, ha='left')
txt(11.55, 1.55, 'ablation (§6.3) → not causal', fs=7,
    c=C_GRAY, ha='left')
ax.plot([11.35, 15.0], [1.70, 1.70], color=C_GRAY, lw=0.5, zorder=6)

# ② root cause
rbox(11.15, 0.45, 4.45, 0.75, fc='#FFF3E0', ec=C_FAIL, lw=1.2)
txt(13.38, 0.98, '② Distribution shift (exposure bias)', fs=7,
    c=C_FAIL, fw='bold')
txt(13.38, 0.65, 'Teacher-forced ≠ autoregressive', fs=7,
    c=C_FAIL, style='italic')

# ROOT CAUSE badge
rbox(14.35, 0.05, 1.15, 0.28, fc=C_FAIL, ec=C_FAIL, lw=0, pad=0.04)
txt(14.93, 0.19, 'ROOT', fs=7, c='white', fw='bold')
arr(14.93, 0.33, 14.2, 0.45, c=C_FAIL, lw=0.7)

# ── save ─────────────────────────────────────────────────────────
out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper'
os.makedirs(out_dir, exist_ok=True)
for fmt in ['pdf', 'png']:
    fig.savefig(os.path.join(out_dir, f'fig1_overview.{fmt}'), format=fmt)
plt.close()
print("Done: fig1_overview.pdf + fig1_overview.png")
