import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.06,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

C_NAVY = '#2166AC'
C_DARK_NAVY = '#1A4D7A'
C_LIGHT_BLUE = '#D4E8F0'
C_VLIGHT_BLUE = '#EAF1F8'
C_WARM_BG = '#F7EFDA'
C_WARM_BD = '#C4A94D'
C_ORANGE_LT = '#F7E8D3'
C_ORANGE = '#D55E00'
C_GREEN = '#4DAF4A'
C_GRAY = '#8C8C8C'
C_DARK = '#2C3E50'
C_SUB = '#6A6A6A'

fig = plt.figure(figsize=(16.5, 6.0))
gs = fig.add_gridspec(1, 3, width_ratios=[1.0, 0.95, 1.08], wspace=0.065,
                      left=0.015, right=0.985, top=0.87, bottom=0.06)

def draw_box(ax, x, y, w, h, text, sub=None, fc='white', ec=C_NAVY,
             tc=C_DARK, fs=10.5, sfs=7.8, bold=True, sc=C_SUB, lw=1.1):
    b = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.28',
                       facecolor=fc, edgecolor=ec, linewidth=lw,
                       zorder=3, mutation_scale=0.3)
    ax.add_patch(b)
    cx, cy = x + w/2, y + h/2
    if sub: cy += 0.20
    ax.text(cx, cy, text, ha='center', va='center', fontsize=fs,
            fontweight='bold' if bold else 'normal', color=tc, zorder=4)
    if sub:
        ax.text(cx, cy - 0.46, sub, ha='center', va='center',
                fontsize=sfs, fontstyle='italic', color=sc, zorder=4)

def draw_arr(ax, s, e, c=C_GRAY, lw=1.0, cs='arc3,rad=0', ms=10):
    a = FancyArrowPatch(s, e, arrowstyle='-|>', connectionstyle=cs,
                        color=c, linewidth=lw, mutation_scale=ms,
                        zorder=2, shrinkA=4, shrinkB=4)
    ax.add_patch(a)

# ============================================================
# (a) Iterative Contamination Loop
# ============================================================
ax = fig.add_subplot(gs[0, 0])
ax.set_xlim(-0.3, 11.0)
ax.set_ylim(-0.5, 11.0)
ax.axis('off')
ax.set_title('(a) Iterative Contamination Loop', fontsize=11.5,
             fontweight='bold', loc='left', pad=12, color=C_DARK)

draw_box(ax, 0.2, 8.6, 2.5, 1.05, 'Real Data')
draw_box(ax, 4.2, 8.3, 3.3, 1.5, 'Mix (α)',
         sub='α synthetic + (1−α) real', fc=C_WARM_BG, ec=C_WARM_BD, sfs=8)
draw_box(ax, 4.5, 6.0, 2.9, 1.1, 'Train $M_t$', fc=C_VLIGHT_BLUE)
draw_box(ax, 4.5, 4.0, 2.9, 1.1, 'Generate', fc=C_VLIGHT_BLUE)
draw_box(ax, 0.1, 2.0, 3.3, 1.35, 'Canary',
         sub='$H(X)$, ECE', fc=C_LIGHT_BLUE, tc=C_NAVY)
draw_box(ax, 4.5, 2.0, 3.3, 1.35, 'Downstream',
         sub='distinct-$n$', fc=C_ORANGE_LT, ec=C_ORANGE, tc=C_ORANGE)

draw_arr(ax, (2.7, 9.12), (4.2, 9.05))
draw_arr(ax, (5.95, 8.3), (5.95, 7.1))
draw_arr(ax, (5.95, 6.0), (5.95, 5.1))
draw_arr(ax, (5.2, 4.0), (2.4, 3.35), cs='arc3,rad=0.12')
draw_arr(ax, (6.5, 4.0), (6.2, 3.35), cs='arc3,rad=-0.03')

# Loop path
lx = 8.6
ax.plot([7.4, lx], [4.55, 4.55], color=C_NAVY, lw=1.1, ls=(0,(4,3)), alpha=0.5, zorder=1)
ax.plot([lx, lx], [4.55, 9.05], color=C_NAVY, lw=1.1, ls=(0,(4,3)), alpha=0.5, zorder=1)
draw_arr(ax, (lx, 9.05), (7.5, 9.05), c=C_NAVY, lw=1.1)
ax.text(lx + 0.45, 6.8, '$T$ generations', fontsize=8.5, fontstyle='italic',
        color=C_NAVY, ha='left', va='center', rotation=90, alpha=0.7,
        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

# Sparklines
sp1 = fig.add_axes([0.033, 0.065, 0.068, 0.14])
xs = np.array([0, 1, 2, 3])
yc = np.array([1.0, 0.55, 0.25, 0.12])
sp1.plot(xs, yc, color=C_NAVY, lw=1.8, solid_capstyle='round', zorder=3)
sp1.fill_between(xs, yc, alpha=0.06, color=C_NAVY, zorder=2)
sp1.set_xlim(-0.15, 3.15); sp1.set_ylim(-0.03, 1.1)
sp1.set_xticks([0,1,2,3]); sp1.set_xticklabels(['0','1','2','3'], fontsize=5.5)
sp1.set_yticks([])
for s in ['top','right']: sp1.spines[s].set_visible(False)
for s in ['left','bottom']: sp1.spines[s].set_linewidth(0.4); sp1.spines[s].set_color('#999')
sp1.tick_params(length=1.5, width=0.4, pad=1, colors='#999')

sp2 = fig.add_axes([0.123, 0.065, 0.068, 0.14])
yd = np.array([1.0, 0.96, 0.50, 0.20])
sp2.plot(xs, yd, color=C_ORANGE, lw=1.8, solid_capstyle='round', zorder=3)
sp2.fill_between(xs, yd, alpha=0.06, color=C_ORANGE, zorder=2)
sp2.set_xlim(-0.15, 3.15); sp2.set_ylim(-0.03, 1.1)
sp2.set_xticks([0,1,2,3]); sp2.set_xticklabels(['0','1','2','3'], fontsize=5.5)
sp2.set_yticks([])
for s in ['top','right']: sp2.spines[s].set_visible(False)
for s in ['left','bottom']: sp2.spines[s].set_linewidth(0.4); sp2.spines[s].set_color('#999')
sp2.tick_params(length=1.5, width=0.4, pad=1, colors='#999')

ax.annotate('', xy=(4.3, 0.55), xytext=(1.3, 0.55),
            arrowprops=dict(arrowstyle='-|>', color=C_GRAY, lw=0.8, mutation_scale=8))
ax.text(2.8, 0.9, '1-gen lead', fontsize=7.5, fontstyle='italic', color=C_GRAY, ha='center')

# ============================================================
# (b) Multi-Method Consensus Test
# ============================================================
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_xlim(0, 10.5)
ax2.set_ylim(0, 11.0)
ax2.axis('off')
ax2.set_title('(b) Multi-Method Consensus Test', fontsize=11.5,
              fontweight='bold', loc='left', pad=12, color=C_DARK)

methods = [
    ('Naive XCorr',    'FPR = 92%', '#FDEAEA', '#E0A0A0', '#D55E00'),
    ('Toda–Yam.',      'FPR = 39%', '#FDF0E0', '#D4C090', '#E8A547'),
    ('Threshold (3σ)', 'FPR = 28%', '#FDF5E0', '#D4C898', '#DAB34A'),
    ('PermG',          'FPR = 11%', '#E8F4E8', '#90C890', C_GREEN),
    ('Diff. XCorr',    'FPR = 3%',  '#E0F0E8', '#88C0A0', C_GREEN),
]

bw, bh = 3.3, 1.12
bx = 0.15
start_y = 10.0
cons_target_y = 5.6

for i, (name, fpr, fc, ec, accent) in enumerate(methods):
    y = start_y - i * (bh + 0.26)
    b = FancyBboxPatch((bx, y - bh), bw, bh, boxstyle='round,pad=0.22',
                       facecolor=fc, edgecolor=ec, linewidth=1.0, zorder=3)
    ax2.add_patch(b)
    bar = FancyBboxPatch((bx + 0.06, y - bh + 0.1), 0.2, bh - 0.2,
                         boxstyle='round,pad=0.04',
                         facecolor=accent, edgecolor='none', zorder=4)
    ax2.add_patch(bar)
    ax2.text(bx + 1.9, y - bh/2 + 0.17, name, ha='center', va='center',
             fontsize=9.5, fontweight='bold', color=C_DARK, zorder=5)
    ax2.text(bx + 1.9, y - bh/2 - 0.2, fpr, ha='center', va='center',
             fontsize=7.5, color=C_SUB, zorder=5)
    draw_arr(ax2, (bx + bw, y - bh/2), (6.0, cons_target_y), c='#BBBBBB', lw=0.6)

# Consensus
cx, cy, cw, ch = 5.8, cons_target_y - 1.1, 3.6, 2.2
sh = FancyBboxPatch((cx+0.08, cy-0.08), cw, ch, boxstyle='round,pad=0.35',
                    facecolor='#00000010', edgecolor='none', zorder=2)
ax2.add_patch(sh)
cs = FancyBboxPatch((cx, cy), cw, ch, boxstyle='round,pad=0.35',
                    facecolor=C_NAVY, edgecolor=C_NAVY, linewidth=1.5, zorder=3)
ax2.add_patch(cs)
ax2.text(cx+cw/2, cy+ch/2+0.32, 'Consensus', ha='center', va='center',
         fontsize=12.5, fontweight='bold', color='white', zorder=4)
ax2.text(cx+cw/2, cy+ch/2-0.18, '$K \\geq 3$', ha='center', va='center',
         fontsize=15, fontweight='bold', color='white', zorder=4)
ax2.text(cx+cw/2, cy+ch/2-0.78, 'majority vote', ha='center', va='center',
         fontsize=8.5, fontstyle='italic', color='#FFFFFFBB', zorder=4)

draw_arr(ax2, (cx+cw/2, cy), (cx+cw/2, 3.1), c=C_NAVY, lw=1.3)

# PermG selected
px, py, pw, ph = cx+0.2, 1.5, 3.2, 1.4
sh2 = FancyBboxPatch((px+0.06, py-0.06), pw, ph, boxstyle='round,pad=0.28',
                     facecolor='#00000010', edgecolor='none', zorder=2)
ax2.add_patch(sh2)
pb = FancyBboxPatch((px, py), pw, ph, boxstyle='round,pad=0.28',
                    facecolor=C_DARK_NAVY, edgecolor=C_DARK_NAVY, linewidth=1.2, zorder=3)
ax2.add_patch(pb)
ax2.text(px+pw/2, py+ph/2+0.18, 'PermG selected', ha='center', va='center',
         fontsize=11, fontweight='bold', color='white', zorder=4)
ax2.text(px+pw/2, py+ph/2-0.25, 'lowest directional FPR', ha='center', va='center',
         fontsize=7.5, fontstyle='italic', color='#FFFFFFAA', zorder=4)

# ============================================================
# (c) Signal × Resolution Model
# ============================================================
ax3 = fig.add_subplot(gs[0, 2])

# Use a shorter title that won't overlap regime labels
ax3.set_title('(c) Signal × Resolution', fontsize=11.5,
              fontweight='bold', loc='left', pad=12, color=C_DARK)

# Regime bands — labels INSIDE the plot as a colored strip at top
bands = [
    (0,    0.30, '#D6E8F5', 'Blind',     '#7A9BBD'),
    (0.30, 0.48, '#D6F0D6', 'Onset',     '#5A9F5A'),
    (0.48, 0.65, '#F5D6D6', 'Dip',       '#BD7A7A'),
    (0.65, 1.0,  '#D6E8F5', 'Detection', '#7A9BBD'),
]

for x0, x1, c, lbl, lc in bands:
    ax3.axvspan(x0, x1, alpha=0.20, color=c, zorder=0)
    # Colored label strip at top of plot area (inside, at y=1.0-1.08)
    ax3.fill_between([x0, x1], [1.02, 1.02], [1.10, 1.10],
                     color=c, alpha=0.45, zorder=0, clip_on=False)
    ax3.text((x0+x1)/2, 1.06, lbl, ha='center', va='center',
             fontsize=8, color=lc, fontweight='bold',
             clip_on=False, zorder=5)

for xb in [0.30, 0.48, 0.65]:
    ax3.axvline(xb, color='#CCCCCC', lw=0.5, ls=':', zorder=1)

alpha = np.linspace(0.001, 1.0, 500)
signal = np.clip(alpha**0.24 * 0.95, 0, 1)
resolution = 1.0 - 0.75 * np.exp(-0.5 * ((alpha - 0.57) / 0.07)**2)
product = signal * resolution

ax3.plot(alpha, signal, color=C_ORANGE, lw=1.5, ls='--', zorder=3)
ax3.plot(alpha, resolution, color=C_GRAY, lw=1.5, ls='--', zorder=3)
ax3.plot(alpha, product, color=C_NAVY, lw=2.3, solid_capstyle='round', zorder=4)

stroke = [pe.withStroke(linewidth=3, foreground='white')]
ax3.text(0.10, 0.85, '$S(\\alpha)$\nsignal', fontsize=9, color=C_ORANGE,
         fontstyle='italic', ha='center', va='center', path_effects=stroke)
ax3.text(0.82, 0.92, '$R(\\alpha)$\nresolution', fontsize=9, color=C_GRAY,
         fontstyle='italic', ha='center', va='center', path_effects=stroke)
ax3.text(0.88, 0.57, '$S{\\times}R$', fontsize=10.5, color=C_NAVY,
         fontweight='bold', ha='center', path_effects=stroke)

ax3.text(0.42, 0.04, '$\\alpha_c(T) \\sim T^{-\\gamma}$', fontsize=9,
         color=C_GRAY, fontstyle='italic', ha='center', path_effects=stroke)
ax3.annotate('', xy=(0.48, 0.15), xytext=(0.42, 0.08),
             arrowprops=dict(arrowstyle='-|>', color=C_GRAY, lw=0.6, mutation_scale=6))

ax3.set_xlim(0, 1)
ax3.set_ylim(0, 1.12)
ax3.set_xlabel('Contamination $\\alpha$', fontsize=10.5)
ax3.set_ylabel('Detection rate', fontsize=10.5)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
for s in ['left', 'bottom']:
    ax3.spines[s].set_linewidth(0.7)
    ax3.spines[s].set_color('#444')
ax3.tick_params(labelsize=9, length=3, width=0.5, colors='#444')
ax3.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])

out_png = '/tmp/fig_framework_v5.png'
out_pdf = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/fig_framework.pdf'
plt.savefig(out_png, dpi=300)
plt.savefig(out_pdf)
plt.close()
print(f'Saved: {out_png}')
