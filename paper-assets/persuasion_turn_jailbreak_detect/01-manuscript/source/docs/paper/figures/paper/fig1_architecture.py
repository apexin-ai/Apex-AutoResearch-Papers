#!/usr/bin/env python3
"""DisPeD architecture diagram — EMNLP 2026, v4 (Stage 2 enhanced).
figsize 16×7, 300 DPI.  At textwidth 6.3in → scale 0.39× → min 18pt ≈ 7pt print.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

C = dict(
    bg='#FFFFFF', charcoal='#2C3E50', text_dark='#495057', text_muted='#95A5A6',
    text_teal='#1ABC9C', border_lt='#DEE2E6', bubble_bg='#F8F9FA',
    gold='#E6B800', gold_dk='#D4A800',
    db_bg='#D6EAF8', db_bd='#85C1E9',
    emb_bg='#E8DAEF', emb_bd='#AF7AC5',
    obj_bg='#FFF9E6', obj_bd='#F0B429',
    gru_bg='#EDE7F6', gru_bd='#9575CD',
    mlp_bg='#F5F5F5', mlp_bd='#BDBDBD',
    jb_bg='#FDEDEC', jb_bd='#E74C3C',
    bn_bg='#EAFAF1', bn_bd='#27AE60',
    arrow='#7F8C8D', dashed='#BDC3C7',
    fwd='#2980B9', bwd='#8E44AD',
)

fig, ax = plt.subplots(figsize=(16, 7), dpi=300)
fig.patch.set_facecolor(C['bg'])
ax.set_xlim(-0.3, 16.8)
ax.set_ylim(-1.0, 7.2)
ax.set_aspect('equal')
ax.axis('off')

# ── helpers ──────────────────────────────────────────────────────

def rbox(x, y, w, h, fc, ec, lw=1.0, rad=0.15, zo=2, shadow=False):
    if shadow:
        ax.add_patch(FancyBboxPatch((x+0.05, y-0.05), w, h,
            boxstyle=f"round,pad=0,rounding_size={rad}",
            fc='#00000014', ec='none', zorder=zo-1))
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={rad}",
        fc=fc, ec=ec, lw=lw, zorder=zo))

def pillbox(x, y, w, h, fc, ec, lw=1.0, zo=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={h/2}",
        fc=fc, ec=ec, lw=lw, zorder=zo))

def arr(xy1, xy2, rad=0.05, lw=0.8, color=None, zo=3):
    ax.add_patch(FancyArrowPatch(xy1, xy2,
        connectionstyle=f'arc3,rad={rad}',
        arrowstyle='-|>,head_width=6,head_length=5',
        color=color or C['arrow'], lw=lw, zorder=zo))

def txt(x, y, s, **kw):
    d = dict(fontsize=18, color=C['charcoal'], ha='center', va='center',
             fontfamily='serif', zorder=5)
    d.update(kw)
    return ax.text(x, y, s, **d)

def vdots(x, y, r=0.055):
    for dy in [-0.17, 0.0, 0.17]:
        ax.add_patch(Circle((x, y+dy), r, fc=C['text_muted'], ec='none', zorder=4))

# ── STAGE TITLES ─────────────────────────────────────────────────

txt(3.3, 6.8, 'Stage 1: Encoder Adaptation', fontsize=22, fontweight='bold')
txt(12.2, 6.8, 'Stage 2: Temporal Classification', fontsize=22, fontweight='bold')

sep_x = 8.0
ax.plot([sep_x, sep_x], [-0.5, 6.4], color=C['dashed'], ls=(0,(6,4)), lw=1.0, zorder=1)

# ── DIALOGUE BUBBLES ─────────────────────────────────────────────

bw, bh = 2.5, 1.25
bdata = [
    (0.0, 4.6, r'$\mathrm{User}_1$', '"Tell me about\n  chemistry..."'),
    (0.0, 2.8, r'$\mathrm{User}_2$', '"What about\n  energetic reactions?"'),
    (0.0, 0.4, r'$\mathrm{User}_k$', '"Give me the exact\n  synthesis..."'),
]
bmids = []
for bx, by, label, content in bdata:
    rbox(bx, by, bw, bh, C['bubble_bg'], C['border_lt'], lw=0.5, rad=0.12, shadow=True)
    ax.add_patch(Circle((bx+0.28, by+bh-0.28), 0.18,
        fc=C['gold'], ec=C['gold_dk'], lw=0.6, zorder=4))
    txt(bx+0.28, by+bh-0.28, 'U', fontsize=11, fontweight='bold',
        color='#FFFFFF', fontfamily='sans-serif')
    txt(bx+0.75, by+bh-0.28, label, fontsize=18, ha='left')
    txt(bx+bw/2, by+0.38, content, fontsize=14, fontstyle='italic',
        color=C['text_dark'])
    bmids.append((bx+bw, by+bh/2))

vdots(1.25, 2.2)

# ── DeBERTa-v3-base ─────────────────────────────────────────────

dx, dy, dw, dh = 3.2, 0.6, 2.9, 4.8
rbox(dx, dy, dw, dh, C['db_bg'], C['db_bd'], lw=1.0, rad=0.22, shadow=True)
txt(dx+dw/2, dy+dh-0.55, 'DeBERTa-v3-base', fontsize=18,
    fontweight='semibold', fontfamily='sans-serif')
txt(dx+dw/2, dy+dh-1.1, 'shared weights', fontsize=14,
    fontstyle='italic', color=C['text_muted'])
for i, ly in enumerate([2.6, 3.15, 3.7]):
    length = 1.7 - i*0.12
    cx = dx + dw/2
    ax.plot([cx-length/2, cx+length/2], [ly, ly],
            color=C['db_bd'], lw=2.0, solid_capstyle='round', zorder=3)

for rx, ry in bmids:
    ty = max(min(ry, dy+dh-0.5), dy+0.5)
    arr((rx+0.08, ry), (dx-0.08, ty), rad=0.06)

# ── EMBEDDINGS h_i ───────────────────────────────────────────────

ex = dx + dw + 0.5
esz = 0.5
epos = [5.0, 4.05, 3.1, 1.1]
elab = [r'$h_1$', r'$h_2$', r'$h_3$', r'$h_k$']
ecenters = []
for ey, lab in zip(epos, elab):
    rbox(ex, ey, esz, esz, C['emb_bg'], C['emb_bd'], lw=0.5, rad=0.08)
    txt(ex+esz/2, ey+esz/2, lab, fontsize=18)
    ecenters.append((ex+esz/2, ey+esz/2))

vdots(ex+esz/2, 2.35)

# "frozen [CLS]" — below h_k, teal sans-serif
txt(ex+esz/2, epos[-1]-0.35, 'frozen [CLS]', fontsize=14, fontstyle='italic',
    color=C['text_teal'], fontfamily='sans-serif')

for _, ey in ecenters:
    arr((dx+dw+0.04, ey), (ex-0.05, ey), rad=0.0, lw=0.8)

# ── ×7 OBJECTIVES ───────────────────────────────────────────────

ox, oy, ow, oh = 3.25, -0.75, 2.8, 1.1
rbox(ox, oy, ow, oh, C['obj_bg'], 'none', lw=0, rad=0.12)
ax.add_patch(FancyBboxPatch((ox, oy), ow, oh,
    boxstyle="round,pad=0,rounding_size=0.12",
    fc='none', ec=C['obj_bd'], lw=1.0,
    linestyle=(0,(5,3)), zorder=3))
txt(ox+ow/2, oy+oh-0.2, r'$\times$7 Stage-1 Objectives', fontsize=16,
    fontweight='bold', fontfamily='sans-serif')
txt(ox+ow/2, oy+oh/2-0.02, '9-Class · Binary · Scrambled · MLM',
    fontsize=13, color=C['text_dark'])
txt(ox+ow/2, oy+0.15, 'Wiki-MLM · Topic · Vanilla (none)',
    fontsize=13, color=C['text_dark'])

ax.annotate('', xy=(dx+dw/2, dy-0.06),
    xytext=(ox+ow/2, oy+oh+0.06),
    arrowprops=dict(arrowstyle='->', color=C['obj_bd'], lw=1.0,
                    linestyle='--', connectionstyle='arc3,rad=0'))

# ── BRACKET ──────────────────────────────────────────────────────

bkt_x = ex + esz + 0.2
top_y = epos[0] + esz
bot_y = epos[-1]
mid_y = (top_y + bot_y) / 2
ax.plot([bkt_x, bkt_x+0.12, bkt_x+0.12, bkt_x],
        [top_y, top_y, bot_y, bot_y],
        color=C['emb_bd'], lw=1.2, solid_capstyle='round', zorder=2)
ax.plot([bkt_x+0.12, bkt_x+0.3], [mid_y, mid_y],
        color=C['emb_bd'], lw=1.2, solid_capstyle='round', zorder=2)

# ══════════════════════════════════════════════════════════════════
# ── STAGE 2: Enhanced ────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════

# ── Input sequence h₁...hₖ (horizontal strip entering BiGRU) ────

seq_y = 5.6
seq_x_start = 8.6
seq_spacing = 0.55
seq_sz = 0.4
seq_labels = [r'$h_1$', r'$h_2$', r'$h_3$', '', r'$h_k$']
seq_centers = []

for i, lab in enumerate(seq_labels):
    sx = seq_x_start + i * seq_spacing
    if lab == '':
        vdots(sx + seq_sz/2, seq_y + seq_sz/2, r=0.04)
        seq_centers.append((sx + seq_sz/2, seq_y + seq_sz/2))
        continue
    rbox(sx, seq_y, seq_sz, seq_sz, C['emb_bg'], C['emb_bd'], lw=0.5, rad=0.06)
    txt(sx + seq_sz/2, seq_y + seq_sz/2, lab, fontsize=13)
    seq_centers.append((sx + seq_sz/2, seq_y + seq_sz/2))

# Forward arrows (blue →)
for i in range(len(seq_centers)-1):
    if seq_labels[i] == '' or seq_labels[i+1] == '':
        continue
    x1 = seq_centers[i][0] + seq_sz/2 + 0.02
    x2 = seq_centers[i+1][0] - seq_sz/2 - 0.02
    y_arr = seq_y + seq_sz + 0.08
    ax.annotate('', xy=(x2, y_arr), xytext=(x1, y_arr),
        arrowprops=dict(arrowstyle='->', color=C['fwd'], lw=1.0))

# Backward arrows (purple ←)
for i in range(len(seq_centers)-1):
    if seq_labels[i] == '' or seq_labels[i+1] == '':
        continue
    x1 = seq_centers[i][0] + seq_sz/2 + 0.02
    x2 = seq_centers[i+1][0] - seq_sz/2 - 0.02
    y_arr = seq_y - 0.08
    ax.annotate('', xy=(x1, y_arr), xytext=(x2, y_arr),
        arrowprops=dict(arrowstyle='->', color=C['bwd'], lw=1.0))

# Compact legend for bidirectional flow
txt(seq_x_start + 2*seq_spacing + seq_sz/2, seq_y + seq_sz + 0.35,
    '→ fwd  ← bwd', fontsize=11, color=C['text_muted'], fontfamily='sans-serif')

# Arrow from bracket to sequence strip
arr((bkt_x+0.33, mid_y), (seq_x_start - 0.1, seq_y + seq_sz/2), rad=0.15)

# ── BiGRU box ───────────────────────────────────────────────────

gx, gy, gw, gh = 8.5, 2.3, 3.0, 2.5
rbox(gx, gy, gw, gh, C['gru_bg'], C['gru_bd'], lw=1.0, rad=0.22, shadow=True)
txt(gx+gw/2, gy+gh-0.45, 'BiGRU', fontsize=22, fontweight='bold',
    fontfamily='sans-serif')

# Internal: forward and backward rows with labels inside
fwd_y = gy + gh/2 + 0.15
bwd_y = gy + gh/2 - 0.5
row_x_start = gx + 0.35
row_x_end = gx + gw - 0.35
row_mid = (row_x_start + row_x_end) / 2

# Forward row: label then arrow
txt(row_mid, fwd_y + 0.25, 'forward →', fontsize=12,
    color=C['fwd'], fontfamily='sans-serif')
ax.annotate('', xy=(row_x_end, fwd_y), xytext=(row_x_start, fwd_y),
    arrowprops=dict(arrowstyle='->', color=C['fwd'], lw=1.8))

# Backward row: arrow then label below it
ax.annotate('', xy=(row_x_start, bwd_y), xytext=(row_x_end, bwd_y),
    arrowprops=dict(arrowstyle='->', color=C['bwd'], lw=1.8))
txt(row_mid, bwd_y - 0.28, '← backward', fontsize=12,
    color=C['bwd'], fontfamily='sans-serif')

# Dimension annotation
txt(gx+gw/2, gy-0.3, 'd=256 per dir', fontsize=12,
    color=C['text_muted'], fontfamily='sans-serif')

# Arrow from sequence to BiGRU
seq_mid_x = seq_x_start + 2 * seq_spacing + seq_sz/2
arr((seq_mid_x, seq_y - 0.05), (gx+gw/2, gy+gh+0.05), rad=0.0, lw=1.0)

# ── Concat node ─────────────────────────────────────────────────

concat_x, concat_y = 12.0, 3.1
concat_r = 0.32
ax.add_patch(Circle((concat_x, concat_y), concat_r,
    fc='#F0E6FF', ec=C['gru_bd'], lw=1.0, zorder=3))
txt(concat_x, concat_y, '⊕', fontsize=20, fontfamily='sans-serif')
txt(concat_x, concat_y - 0.55, '512', fontsize=12,
    color=C['text_muted'], fontfamily='sans-serif')

# BiGRU → concat
arr((gx+gw+0.06, gy+gh/2), (concat_x - concat_r - 0.06, concat_y), rad=0.0)

# ── MLP ──────────────────────────────────────────────────────────

mx, my, mw, mh = 13.0, 2.3, 1.6, 1.6
rbox(mx, my, mw, mh, C['mlp_bg'], C['mlp_bd'], lw=1.0, rad=0.18, shadow=True)
txt(mx+mw/2, my+mh/2+0.15, 'MLP', fontsize=20, fontweight='bold',
    fontfamily='sans-serif')
txt(mx+mw/2, my+mh/2-0.3, '512→256→2', fontsize=11,
    color=C['text_dark'], fontfamily='sans-serif')

# concat → MLP
arr((concat_x + concat_r + 0.06, concat_y), (mx-0.06, my+mh/2), rad=0.0)

# ── OUTPUT PILLS — symmetric about MLP center ───────────────────

mlp_cy = my + mh/2
pill_offset = 1.4
px, pw, ph = 14.8, 1.8, 0.6
jb_y = mlp_cy + pill_offset - ph/2
bn_y = mlp_cy - pill_offset - ph/2
pillbox(px, jb_y, pw, ph, C['jb_bg'], C['jb_bd'], lw=1.0)
txt(px+pw/2, jb_y+ph/2, 'Jailbreak', fontsize=16, fontweight='bold', color=C['jb_bd'])
pillbox(px, bn_y, pw, ph, C['bn_bg'], C['bn_bd'], lw=1.0)
txt(px+pw/2, bn_y+ph/2, 'Benign', fontsize=16, fontweight='bold', color=C['bn_bd'])

arr((mx+mw+0.06, mlp_cy+0.3), (px-0.06, jb_y+ph/2), rad=0.08)
arr((mx+mw+0.06, mlp_cy-0.3), (px-0.06, bn_y+ph/2), rad=-0.08)

# "shared across all 7 variants"
txt(11.0, 0.5, 'shared across all 7 variants', fontsize=14,
    fontstyle='italic', color=C['text_muted'])

# ── SAVE ─────────────────────────────────────────────────────────

plt.savefig('/tmp/fig1_architecture_v4.png', dpi=300, bbox_inches='tight',
            pad_inches=0.25, facecolor=C['bg'])
plt.savefig('/tmp/fig1_architecture_v4.pdf', bbox_inches='tight',
            pad_inches=0.25, facecolor=C['bg'])
plt.close()
print('Saved v4')
