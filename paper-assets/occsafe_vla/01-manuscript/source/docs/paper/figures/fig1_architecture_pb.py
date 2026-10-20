"""
fig1_architecture_pb.py — (a) Training Setup + (b) Factorial Design
Style: Nature Methods / ICML best paper — minimal, restrained, white-dominant
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# ── Color palette (strict — whole figure uses only these) ──────────
C = dict(
    text  = '#2C3E50',
    mid   = '#7F8C8D',
    weak  = '#BDC3C7',
    fill  = '#F8F9FA',
    edge  = '#DEE2E6',
    enc   = '#EBF5FB',
    bb    = '#F4ECF7',
    head  = '#EAFAF1',
    red   = '#E74C3C',
    shd   = '#E8E8E8',
    bn_bg = '#FDEDEC',
    ln_bg = '#EBF5FB',
)

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Noto Serif', 'DejaVu Serif'],
    'font.size': 8.5,
    'text.color': C['text'],
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'cm',
})

fig = plt.figure(figsize=(7.0, 2.8), dpi=300, facecolor='white')
ax_a = fig.add_axes([0.01, 0.02, 0.52, 0.94])
ax_b = fig.add_axes([0.555, 0.02, 0.43, 0.94])
for ax in (ax_a, ax_b):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')


# ── Helpers ────────────────────────────────────────────────────────
def mbox(ax, x, y, w, h, label, sub=None, fill=C['fill'], edge=C['edge'],
         fs=8.5, sfs=7, lw=0.6, dash=False):
    ax.add_patch(FancyBboxPatch(
        (x + 0.04, y - 0.04), w, h,
        boxstyle="round,pad=0,rounding_size=0.15",
        fc=C['shd'], ec='none', lw=0, zorder=2, alpha=0.35))
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0,rounding_size=0.15",
        fc=fill, ec=edge, lw=lw,
        ls=(0, (3, 2)) if dash else '-', zorder=3))
    cx, cy = x + w / 2, y + h / 2
    if sub:
        ax.text(cx, cy + 0.17, label, ha='center', va='center',
                fontsize=fs, fontweight='bold', color=C['text'], zorder=5)
        ax.text(cx, cy - 0.17, sub, ha='center', va='center',
                fontsize=sfs, color=C['mid'], zorder=5)
    else:
        ax.text(cx, cy, label, ha='center', va='center',
                fontsize=fs, fontweight='bold', color=C['text'], zorder=5)


def draw_x(ax, cx, cy, size=0.12, color=C['mid'], lw=0.9):
    ax.plot([cx - size, cx + size], [cy - size, cy + size],
            color=color, lw=lw, zorder=6, solid_capstyle='round')
    ax.plot([cx - size, cx + size], [cy + size, cy - size],
            color=color, lw=lw, zorder=6, solid_capstyle='round')


def marrow(ax, s, e, color=C['weak'], lw=0.7, ms=6):
    ax.add_patch(FancyArrowPatch(
        s, e, arrowstyle='-|>,head_length=0.18,head_width=0.10',
        color=color, lw=lw, mutation_scale=ms,
        zorder=2, shrinkA=2, shrinkB=2))


# ═══════════════════════════════════════════════════════════════════
# PANEL (a): Training Setup
# ═══════════════════════════════════════════════════════════════════
ax_a.text(0.15, 9.55, '(a)', fontsize=9, fontweight='bold')
ax_a.text(0.85, 9.55, 'Training Setup', fontsize=8.5, fontweight='bold')

CX = 4.6

# Layer 1: RGB Observation
rw, rh, ry = 3.4, 0.6, 0.8
mbox(ax_a, CX - rw / 2, ry, rw, rh, 'RGB Observation', fs=8)

# Layer 2: Vision Encoders
ew, eh, ey = 2.0, 0.75, 2.55
eg = 0.4
elx = CX - eg / 2 - ew
erx = CX + eg / 2
mbox(ax_a, elx, ey, ew, eh, 'DINOv2', '1024-d', fill=C['enc'])
mbox(ax_a, erx, ey, ew, eh, 'SigLIP', '1152-d', fill=C['enc'])

marrow(ax_a, (CX - 0.3, ry + rh), (elx + ew / 2, ey))
marrow(ax_a, (CX + 0.3, ry + rh), (erx + ew / 2, ey))

# Concat annotation
ccy = ey + eh + 0.25
ax_a.text(CX, ccy, 'concat', fontsize=6.5, ha='center',
          color=C['weak'], style='italic')
marrow(ax_a, (elx + ew / 2, ey + eh), (CX - 0.08, ccy - 0.06), lw=0.5)
marrow(ax_a, (erx + ew / 2, ey + eh), (CX + 0.08, ccy - 0.06), lw=0.5)

# Layer 3: LLM Backbone
Lw, Lh, Ly = 4.6, 0.75, 4.6
mbox(ax_a, CX - Lw / 2, Ly, Lw, Lh,
     'LLM Backbone', 'Llama-2 7B + LoRA', fill=C['bb'])
marrow(ax_a, (CX, ccy + 0.06), (CX, Ly), lw=0.5)

# Layer 4: Heads
Hw, Hh, Hy = 1.95, 0.75, 6.9
Hg = 0.55
ax_ = CX - Hg / 2 - Hw
ux_ = CX + Hg / 2

mbox(ax_a, ax_, Hy, Hw, Hh, 'Action Head', '7-DoF tokens', fill=C['head'])
mbox(ax_a, ux_, Hy, Hw, Hh, 'Aux Head', 'BEV / Depth',
     fill=C['head'], dash=True)

# X mark on Aux Head (top-right corner, clear of text)
draw_x(ax_a, ux_ + Hw - 0.15, Hy + Hh - 0.14, size=0.09, lw=1.0)

marrow(ax_a, (CX - 0.6, Ly + Lh), (ax_ + Hw / 2, Hy),
       color=C['mid'], lw=0.9)
marrow(ax_a, (CX + 0.6, Ly + Lh), (ux_ + Hw / 2, Hy), lw=0.7)

# Loss labels
ax_a.text(ax_ + Hw / 2, Hy + Hh + 0.15,
          r'$\mathcal{L}_{\mathrm{action}}$',
          fontsize=8, ha='center', va='bottom', color=C['mid'])
ax_a.text(ux_ + Hw / 2, Hy + Hh + 0.15,
          r'$\lambda \cdot \mathcal{L}_{\mathrm{aux}}$',
          fontsize=8, ha='center', va='bottom', color=C['mid'])

# ── Gradient flow arrows (straight, well-separated) ───────────────
gx1 = ux_ + Hw + 0.30
gx2 = gx1 + 0.85
gyt = Hy + 0.20
gyb = Ly + Lh - 0.10
gy_mid = (gyt + gyb) / 2

# ON (red dashed)
ax_a.annotate('', xy=(gx1, gyb), xytext=(gx1, gyt),
              arrowprops=dict(
                  arrowstyle='->,head_length=0.25,head_width=0.13',
                  color=C['red'], lw=1.2, linestyle=(0, (3, 2))))
ax_a.text(gx1, gy_mid, 'ON', fontsize=7, fontweight='bold',
          color=C['red'], ha='center', va='center',
          bbox=dict(fc='white', ec='none', pad=0.5, alpha=0.9))

# OFF (gray dashed)
ax_a.annotate('', xy=(gx2, gyb), xytext=(gx2, gyt),
              arrowprops=dict(
                  arrowstyle='->,head_length=0.20,head_width=0.10',
                  color=C['weak'], lw=0.8, linestyle=(0, (3, 2))))
ax_a.text(gx2, gy_mid, 'OFF', fontsize=7,
          color=C['weak'], ha='center', va='center',
          bbox=dict(fc='white', ec='none', pad=0.5, alpha=0.9))


# ═══════════════════════════════════════════════════════════════════
# PANEL (b): Factorial Design
# ═══════════════════════════════════════════════════════════════════
ax_b.text(0.15, 9.55, '(b)', fontsize=9, fontweight='bold')
ax_b.text(0.85, 9.55, 'Factorial Design', fontsize=8.5, fontweight='bold')

GX, GY, GW, GH = 2.0, 3.5, 6.8, 4.5
CW, CH = GW / 2, GH / 2

# Outer frame
ax_b.add_patch(FancyBboxPatch(
    (GX, GY), GW, GH, boxstyle="round,pad=0,rounding_size=0.15",
    fc='white', ec=C['edge'], lw=0.6, zorder=2))

# Grid dividers
ax_b.plot([GX + CW, GX + CW], [GY + 0.08, GY + GH - 0.08],
          color=C['shd'], lw=0.4, zorder=2.5)
ax_b.plot([GX + 0.08, GX + GW - 0.08], [GY + CH, GY + CH],
          color=C['shd'], lw=0.4, zorder=2.5)

# Column headers
ax_b.text(GX + CW * 0.5, GY + GH + 0.30, 'Gradient ON',
          ha='center', fontsize=8, fontweight='bold')
ax_b.text(GX + CW * 1.5, GY + GH + 0.30, 'Gradient OFF',
          ha='center', fontsize=8, fontweight='bold')

# Row headers
ax_b.text(GX - 0.20, GY + CH * 1.5, 'BatchNorm',
          ha='right', va='center', fontsize=8, fontweight='bold')
ax_b.text(GX - 0.20, GY + CH * 0.5, 'LayerNorm',
          ha='right', va='center', fontsize=8, fontweight='bold')

# Cell contents
cells = [
    (0, 1, 'Full OCC',     '(BN, Grad ON)',  C['bn_bg']),
    (1, 1, 'Detach OCC',   '(BN, Grad OFF)', C['bn_bg']),
    (0, 0, 'Full OCC+LN',  '(LN, Grad ON)',  C['ln_bg']),
    (1, 0, 'Detach+LN',    '(LN, Grad OFF)', C['ln_bg']),
]
for col, row, nm, sub, bg in cells:
    cx = GX + col * CW
    cy = GY + row * CH
    p = 0.12
    ax_b.add_patch(FancyBboxPatch(
        (cx + p, cy + p), CW - 2 * p, CH - 2 * p,
        boxstyle="round,pad=0,rounding_size=0.08",
        fc=bg, ec=C['edge'], lw=0.35, zorder=3))
    ax_b.text(cx + CW / 2, cy + CH / 2 + 0.18, nm,
              ha='center', va='center', fontsize=8.5,
              fontweight='bold', zorder=4)
    ax_b.text(cx + CW / 2, cy + CH / 2 - 0.25, sub,
              ha='center', va='center', fontsize=7,
              color=C['mid'], zorder=4)

# Chip tags — clearly bordered
tags = ['Random OCC', 'Depth', 'Cutoff/Rev', 'Vanilla']
tws = [1.45, 0.90, 1.35, 1.0]
tgap = 0.28
tot = sum(tws) + tgap * (len(tags) - 1)
tx = GX + (GW - tot) / 2
ty, th = GY - 0.85, 0.45

for t, tw in zip(tags, tws):
    ax_b.add_patch(FancyBboxPatch(
        (tx, ty), tw, th,
        boxstyle="round,pad=0,rounding_size=0.10",
        fc='#F0F2F4', ec='#ADB5BD', lw=0.6, zorder=3))
    ax_b.text(tx + tw / 2, ty + th / 2, t,
              ha='center', va='center', fontsize=6.5, zorder=4)
    tx += tw + tgap

# Footer
ax_b.text(GX + GW / 2, ty - 0.50,
          '12 conditions · 5 factors',
          ha='center', fontsize=6.5, color=C['weak'], style='italic')

# ── Panel divider ──────────────────────────────────────────────────
fig.add_artist(plt.Line2D(
    [0.545, 0.545], [0.06, 0.92],
    transform=fig.transFigure, color=C['shd'], lw=0.35))

# ── Save ───────────────────────────────────────────────────────────
D = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'
fig.savefig(f'{D}/fig1_architecture_pb.png', dpi=300, facecolor='white',
            bbox_inches='tight', pad_inches=0.02)
fig.savefig(f'{D}/fig1_architecture_pb.pdf', facecolor='white',
            bbox_inches='tight', pad_inches=0.02)
plt.close()
print("Done: fig1_architecture_pb.png + .pdf")
