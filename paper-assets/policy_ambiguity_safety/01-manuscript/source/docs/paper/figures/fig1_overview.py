import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Liberation Serif'],
    'font.size': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.02,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

C = {
    'navy': '#2C3E50', 'red': '#C0392B', 'teal': '#2E7D6E',
    'orange': '#D4780A', 'blue': '#3F7CAC',
    'spec_bg': '#EEF2F7', 'spec_bd': '#CBD5E0',
    'ling_bg': '#EEF7F2', 'ling_bd': '#B2DFDB',
    'box_bd': '#AAB4BE',
    'amb_bg': '#FFF5F5', 'amb_bd': '#E0BABA',
    'una_bg': '#EEFAEE', 'una_bd': '#A8D4A8',
    'trc_bg': '#F5F5F5', 'trc_bd': '#D0D0D0',
    'jdg_bg': '#F0EAFF', 'jdg_bd': '#BBA8D8',
    'vio_bg': '#FFF0F0',
}

fig = plt.figure(figsize=(7.1, 3.7))
gs = fig.add_gridspec(1, 3, width_ratios=[0.27, 0.43, 0.30],
                       left=0.005, right=0.995, top=0.93, bottom=0.01,
                       wspace=0.055)
ax_a = fig.add_subplot(gs[0])
ax_b = fig.add_subplot(gs[1])
ax_c = fig.add_subplot(gs[2])
for ax in [ax_a, ax_b, ax_c]:
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')

def rbox(ax, x, y, w, h, fc='white', ec='#AAB4BE', lw=0.6, r=0.015, shd=True, z=3):
    if shd:
        ax.add_patch(FancyBboxPatch((x+0.004, y-0.005), w, h,
            boxstyle=f"round,pad=0,rounding_size={r}",
            fc='#00000007', ec='none', lw=0, zorder=z-1))
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={r}",
        fc=fc, ec=ec, linewidth=lw, zorder=z))

def arr(ax, s, e, c='#555555', lw=0.6, con='arc3,rad=0', z=5):
    ax.add_patch(FancyArrowPatch(s, e,
        arrowstyle='->,head_length=3,head_width=1.8',
        connectionstyle=con, color=c, linewidth=lw, zorder=z, mutation_scale=8))

def pill(ax, x, y, w, h, txt, fc, tc='white', fs=5):
    ax.add_patch(FancyBboxPatch((x+0.002, y-0.003), w, h,
        boxstyle=f"round,pad=0,rounding_size={h/2}",
        fc='#00000008', ec='none', lw=0, zorder=3))
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={h/2}",
        fc=fc, ec='none', lw=0, zorder=4))
    ax.text(x+w/2, y+h/2, txt, ha='center', va='center',
            fontsize=fs, color=tc, fontweight='medium', zorder=5)

# ════════════════════════════════════════
# PANEL (a) — Ambiguity Taxonomy
# ════════════════════════════════════════
ax_a.text(0.02, 0.97, '(a)', fontsize=9, fontweight='bold', color=C['navy'], va='top')
ax_a.text(0.52, 0.97, 'Ambiguity Taxonomy', fontsize=8, fontweight='bold',
          color=C['navy'], ha='center', va='top')

# Specification layer
sy, sh = 0.73, 0.14
rbox(ax_a, 0.04, sy, 0.92, sh, fc=C['spec_bg'], ec=C['spec_bd'], lw=0.4, r=0.02, shd=False)
ax_a.text(0.50, sy+sh+0.012, 'SPECIFICATION LAYER',
          ha='center', va='bottom', fontsize=5.5, color=C['navy'],
          fontweight='bold', fontfamily='sans-serif')

spec = ['Auth.\nScope', 'Incomplete-\nness', 'Cond.\nPrec.']
bw, bh = 0.26, 0.09
gp = (0.92 - 3*bw) / 4
for i, t in enumerate(spec):
    bx = 0.04 + gp + i*(bw+gp)
    by = sy + (sh-bh)/2
    rbox(ax_a, bx, by, bw, bh, ec=C['box_bd'], lw=0.5, r=0.012)
    ax_a.text(bx+bw/2, by+bh/2, t, ha='center', va='center',
              fontsize=6, color=C['navy'], linespacing=1.0)

# Linguistic layer
ly, lh = 0.48, 0.14
rbox(ax_a, 0.04, ly, 0.92, lh, fc=C['ling_bg'], ec=C['ling_bd'], lw=0.4, r=0.02, shd=False)
ax_a.text(0.50, ly+lh+0.012, 'LINGUISTIC LAYER',
          ha='center', va='bottom', fontsize=5.5, color=C['teal'],
          fontweight='bold', fontfamily='sans-serif')

ling = ['Lexical', 'Scopal', 'Coreferential']
for i, t in enumerate(ling):
    bx = 0.04 + gp + i*(bw+gp)
    by = ly + (lh-bh)/2
    rbox(ax_a, bx, by, bw, bh, ec=C['box_bd'], lw=0.5, r=0.012)
    ax_a.text(bx+bw/2, by+bh/2, t, ha='center', va='center',
              fontsize=6, color=C['navy'])

# Example pair
ey, eh, ew = 0.055, 0.32, 0.41
rbox(ax_a, 0.04, ey, ew, eh, fc=C['amb_bg'], ec=C['amb_bd'], lw=0.4, r=0.015)
ax_a.text(0.04+ew/2, ey+eh-0.018, 'Ambiguous', ha='center', va='top',
          fontsize=6, color=C['red'], fontweight='bold')
ax_a.text(0.04+ew/2, ey+eh/2-0.005,
          '"Refunds for large\norders require\nappropriate approval"',
          ha='center', va='center', fontsize=5.5, color='#444444',
          fontstyle='italic', linespacing=1.1)

ax_a.text(0.50, ey+eh/2, 'vs', ha='center', va='center',
          fontsize=6.5, color='#999999', fontstyle='italic')

rbox(ax_a, 0.55, ey, ew, eh, fc=C['una_bg'], ec=C['una_bd'], lw=0.4, r=0.015)
ax_a.text(0.55+ew/2, ey+eh-0.018, 'Unambiguous', ha='center', va='top',
          fontsize=6, color=C['teal'], fontweight='bold')
ax_a.text(0.55+ew/2, ey+eh/2-0.005,
          '"Refunds >$50 require\nmanager approval\nwithin 14 days"',
          ha='center', va='center', fontsize=5.5, color='#444444',
          fontstyle='italic', linespacing=1.1)

ax_a.text(0.50, 0.012, '300 matched clause pairs',
          ha='center', va='bottom', fontsize=5.5, color='#888888')

# ════════════════════════════════════════
# PANEL (b) — Matched-Pair Causal Design
# ════════════════════════════════════════
ax_b.text(0.01, 0.97, '(b)', fontsize=9, fontweight='bold', color=C['navy'], va='top')
ax_b.text(0.48, 0.97, 'Matched-Pair Causal Design', fontsize=8,
          fontweight='bold', color=C['navy'], ha='center', va='top')

bw2, bh2 = 0.14, 0.07
ty_t, ty_b = 0.74, 0.48

# Policy Doc
pd_x, pd_w, pd_h = 0.01, 0.09, 0.095
pd_y = (ty_t+ty_b)/2 + bh2/2 - pd_h/2
rbox(ax_b, pd_x, pd_y, pd_w, pd_h, fc='#F9F9F7', ec='#C5C5BE', lw=0.5, r=0.010)
ax_b.text(pd_x+pd_w/2, pd_y+pd_h/2+0.004, 'Policy', ha='center', va='center',
          fontsize=5.5, color=C['navy'])
ax_b.text(pd_x+pd_w/2, pd_y+pd_h/2-0.013, 'Doc.', ha='center', va='center',
          fontsize=5.5, color=C['navy'])
for i in range(3):
    ax_b.plot([pd_x+0.012, pd_x+pd_w-0.012], [pd_y+0.010+i*0.011]*2,
              color='#D8D8D0', lw=0.2, zorder=4)

# Top path
ac_x = 0.15
rbox(ax_b, ac_x, ty_t, bw2, bh2, fc=C['amb_bg'], ec=C['amb_bd'], lw=0.5, r=0.009)
ax_b.text(ac_x+bw2/2, ty_t+bh2/2, 'Ambig. Clause', ha='center', va='center',
          fontsize=5.5, color=C['red'])

tb_x, tb_w = 0.345, 0.14
rbox(ax_b, tb_x, ty_t, tb_w, bh2, fc='white', ec=C['navy'], lw=0.7, r=0.009)
ax_b.text(tb_x+tb_w/2, ty_t+bh2/2+0.005, 'τ²-bench', ha='center', va='center',
          fontsize=6, color=C['navy'], fontweight='bold')
ax_b.text(tb_x+tb_w/2, ty_t+bh2/2-0.015, 'Agent ↔ User', ha='center', va='center',
          fontsize=5, color='#999999')

tr_x, tr_w = 0.54, 0.08
rbox(ax_b, tr_x, ty_t, tr_w, bh2, fc=C['trc_bg'], ec=C['trc_bd'], lw=0.4, r=0.009)
ax_b.text(tr_x+tr_w/2, ty_t+bh2/2, 'Trace', ha='center', va='center',
          fontsize=5.5, color='#555555')

# Bottom path
rbox(ax_b, ac_x, ty_b, bw2, bh2, fc=C['una_bg'], ec=C['una_bd'], lw=0.5, r=0.009)
ax_b.text(ac_x+bw2/2, ty_b+bh2/2, 'Unamb. Clause', ha='center', va='center',
          fontsize=5.5, color=C['teal'])

rbox(ax_b, tb_x, ty_b, tb_w, bh2, fc='white', ec=C['navy'], lw=0.7, r=0.009)
ax_b.text(tb_x+tb_w/2, ty_b+bh2/2+0.005, 'τ²-bench', ha='center', va='center',
          fontsize=6, color=C['navy'], fontweight='bold')
ax_b.text(tb_x+tb_w/2, ty_b+bh2/2-0.015, 'Agent ↔ User', ha='center', va='center',
          fontsize=5, color='#999999')

rbox(ax_b, tr_x, ty_b, tr_w, bh2, fc=C['trc_bg'], ec=C['trc_bd'], lw=0.4, r=0.009)
ax_b.text(tr_x+tr_w/2, ty_b+bh2/2, 'Trace', ha='center', va='center',
          fontsize=5.5, color='#555555')

# Arrows
pm = pd_y + pd_h/2
arr(ax_b, (pd_x+pd_w, pm+0.015), (ac_x, ty_t+bh2/2), con='arc3,rad=-0.10')
arr(ax_b, (pd_x+pd_w, pm-0.015), (ac_x, ty_b+bh2/2), con='arc3,rad=0.10')
arr(ax_b, (ac_x+bw2, ty_t+bh2/2), (tb_x, ty_t+bh2/2))
arr(ax_b, (ac_x+bw2, ty_b+bh2/2), (tb_x, ty_b+bh2/2))
arr(ax_b, (tb_x+tb_w, ty_t+bh2/2), (tr_x, ty_t+bh2/2))
arr(ax_b, (tb_x+tb_w, ty_b+bh2/2), (tr_x, ty_b+bh2/2))

# Delta
dx = tr_x + tr_w + 0.02
tt_m = ty_t + bh2/2
tb_m = ty_b + bh2/2
ax_b.annotate('', xy=(dx, tb_m+0.006), xytext=(dx, tt_m-0.006),
              arrowprops=dict(arrowstyle='<->', color=C['red'], lw=0.8, mutation_scale=9))
ax_b.text(dx+0.035, (tt_m+tb_m)/2+0.010, 'Δ', ha='center', va='center',
          fontsize=11, color=C['red'], fontweight='bold')
ax_b.text(dx+0.035, (tt_m+tb_m)/2-0.018, 'Causal\nEffect', ha='center', va='center',
          fontsize=5, color=C['red'], fontstyle='italic', linespacing=1.0)

# Episode count
ax_b.text(0.40, 0.31, '5 models × 2 conditions × 300 pairs = 2,997 episodes',
          ha='center', va='center', fontsize=5.5, color='#777777')

# Model badges
mdl = [('GPT-5.4', C['navy']), ('GPT-4.1', C['navy']),
       ('Claude', C['orange']), ('Qwen3', C['blue']), ('DeepSeek', C['teal'])]
pw2, ph2 = 0.105, 0.03
ttl = 5*pw2 + 4*0.008
sx = 0.40 - ttl/2
for i, (n, c) in enumerate(mdl):
    pill(ax_b, sx + i*(pw2+0.008), 0.16, pw2, ph2, n, c, fs=5)
ax_b.text(0.40, 0.10, 'Five architecturally diverse models',
          ha='center', va='center', fontsize=5, color='#888888', fontstyle='italic')

# ════════════════════════════════════════
# PANEL (c) — Evaluation & Findings
# ════════════════════════════════════════
ax_c.text(0.02, 0.97, '(c)', fontsize=9, fontweight='bold', color=C['navy'], va='top')
ax_c.text(0.52, 0.97, 'Evaluation & Findings', fontsize=8,
          fontweight='bold', color=C['navy'], ha='center', va='top')

# Judge pipeline
jp_y, jp_h = 0.855, 0.055
ep_w = 0.11
rbox(ax_c, 0.015, jp_y, ep_w, jp_h, fc=C['trc_bg'], ec=C['trc_bd'], lw=0.35, r=0.008)
ax_c.text(0.015+ep_w/2, jp_y+jp_h/2, 'Episode', ha='center', va='center',
          fontsize=5.5, color='#555555')

jx, jw = 0.175, 0.135
rbox(ax_c, jx, jp_y, jw, jp_h, fc=C['jdg_bg'], ec=C['jdg_bd'], lw=0.45, r=0.008)
ax_c.text(jx+jw/2, jp_y+jp_h/2, 'LLM Judge', ha='center', va='center',
          fontsize=5.5, color='#5B4A8A', fontweight='bold')
arr(ax_c, (0.015+ep_w, jp_y+jp_h/2), (jx, jp_y+jp_h/2), lw=0.4)

sev = [('none','#F8F8F8','#D5D5D5'), ('minor','#FFFDE7','#DDD890'),
       ('mod.','#FFF3E0','#DDC090'), ('crit.','#FFE8E8','#DD9090')]
sw2, sh3 = 0.082, 0.04
sx2 = 0.38
for i, (l, bg, bd) in enumerate(sev):
    cx = sx2 + i*(sw2+0.004)
    cy = jp_y + (jp_h-sh3)/2
    rbox(ax_c, cx, cy, sw2, sh3, fc=bg, ec=bd, lw=0.3, r=0.006, shd=False)
    ax_c.text(cx+sw2/2, cy+sh3/2, l, ha='center', va='center',
              fontsize=5, color='#555555')
arr(ax_c, (jx+jw, jp_y+jp_h/2), (sx2, jp_y+jp_h/2), lw=0.4)

ax_c.text(0.50, jp_y-0.02, 'Cross-model judge (κ = 0.65)',
          ha='center', va='top', fontsize=5.5, color='#888888', fontstyle='italic')

# Key finding
ax_c.text(0.50, 0.63, '+34.0 pp', ha='center', va='center',
          fontsize=19, fontweight='bold', color=C['navy'])
ax_c.text(0.50, 0.545, '(+31.0 pp excl. incompleteness)',
          ha='center', va='center', fontsize=6, color='#888888')
ax_c.text(0.50, 0.475, 'violation increase from ambiguity',
          ha='center', va='center', fontsize=7, color=C['navy'])

# Convergent nocuity
ax_c.text(0.50, 0.38, 'Convergent nocuity', ha='center', va='center',
          fontsize=6.5, fontweight='bold', color=C['navy'])

# VIOLATION box
vx, vy, vw, vh = 0.27, 0.13, 0.46, 0.05
rbox(ax_c, vx, vy, vw, vh, fc=C['vio_bg'], ec=C['red'], lw=0.7, r=0.010)
ax_c.text(vx+vw/2, vy+vh/2, 'VIOLATION', ha='center', va='center',
          fontsize=6.5, color=C['red'], fontweight='bold', fontfamily='sans-serif')

# Model circles
nd = [('5.4', C['navy'], 0.07, 0.28),
      ('4.1', C['navy'], 0.23, 0.305),
      ('Cla', C['orange'], 0.50, 0.32),
      ('Qw', C['blue'], 0.77, 0.305),
      ('DS', C['teal'], 0.93, 0.28)]
cr = 0.020
for la, cl, cx, cy in nd:
    ax_c.add_patch(plt.Circle((cx, cy), cr, fc='white', ec=cl, lw=0.6, zorder=5))
    ax_c.text(cx, cy, la, ha='center', va='center', fontsize=5,
              color=cl, fontweight='bold', zorder=6)
    tgx = vx + vw/2 + (cx-(vx+vw/2))*0.12
    arr(ax_c, (cx, cy-cr-0.003), (tgx, vy+vh+0.003), c='#CCCCCC', lw=0.3)

ax_c.text(0.50, 0.05, '41.3% convergent · 77% permissive bias',
          ha='center', va='center', fontsize=5.5, color='#888888')

# Separators
for xs in [0.278, 0.708]:
    fig.add_artist(plt.Line2D([xs, xs], [0.03, 0.93],
                              transform=fig.transFigure, color='#EBEBEB', lw=0.3))

plt.savefig('/tmp/fig1_polish.png', dpi=300)
plt.savefig('/tmp/fig1_polish.pdf', dpi=300)
plt.close()
print("DONE")
