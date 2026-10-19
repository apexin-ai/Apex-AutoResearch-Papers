import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe

C = {
    'danger': '#D55E00', 'safe': '#0072B2', 'success': '#009E73',
    'text': '#2C3E50', 'annot': '#7F8C8D', 'divider': '#D5D8DC',
    'left_fill': '#F8F6F0', 'left_bdr': '#BDC3C7',
    'right_fill': '#EAF2F8', 'right_bdr': '#5DADE2',
    'neg_fill': '#FADBD8', 'pos_fill': '#D5F5E3', 'fail_fill': '#FADBD8',
    'bg_left': '#FDFCFA', 'bg_right': '#F7FBFF',
}

W, H = 12.5, 5.5
fig = plt.figure(figsize=(W, H), dpi=300, facecolor='white')
ax = fig.add_axes([0.005, 0.005, 0.99, 0.99])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis('off')

def rbox(x, y, w, h, fc, ec, lw=0.8, r=0.12, shadow=True, z=2):
    if shadow:
        ax.add_patch(FancyBboxPatch((x+0.04, y-0.04), w, h,
            boxstyle=f"round,pad={r}", fc='#1a1a1a', ec='none', alpha=0.05, zorder=z-0.5))
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={r}",
        fc=fc, ec=ec, lw=lw, zorder=z))

def farrow(x0, y0, x1, y1, c, lw=1.0, ms=10, cs=None, z=3):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1),
        arrowstyle='->,head_length=0.35,head_width=0.18',
        mutation_scale=ms, color=c, lw=lw, zorder=z, connectionstyle=cs))

# ─── Background ───
rbox(-0.2, -0.2, W/2-0.05, H+0.4, C['bg_left'], 'none', lw=0, r=0.0, shadow=False, z=0)
rbox(W/2+0.25, -0.2, W/2-0.05, H+0.4, C['bg_right'], 'none', lw=0, r=0.0, shadow=False, z=0)
ax.plot([W/2, W/2], [0.2, H-0.2], color=C['divider'], lw=0.7, zorder=1)

# ═══════ LAYOUT ═══════
LP, RP = 0.4, W/2 + 0.5
PW = 5.2
cw = PW / 5

TITLE_Y = H - 0.45
M1_Y    = H - 0.98
ARR_Y   = H - 1.55
BAR_Y   = H - 2.55
BAR_H   = 0.70
M2_Y    = BAR_Y - 0.60
NEG_Y   = BAR_Y - 1.55
NEG_S   = 0.55

# ═══════════ LEFT PANEL ═══════════
LCX = LP + PW/2
ax.text(LCX, TITLE_Y, 'Step-Independent Windowing', fontsize=15, fontweight='bold',
        fontfamily='serif', color=C['text'], ha='center', va='center')

ax.text(LP, M1_Y, 'M1: Truncated Context', fontsize=10.5, fontweight='bold',
        fontfamily='serif', color=C['danger'])

# 5 truncated arrows
for i in range(5):
    farrow(LP+(i+0.87)*cw, ARR_Y, LP+(i+0.13)*cw, ARR_Y, C['danger'], lw=1.2, ms=10)

ax.text(LP+2*cw, ARR_Y+0.01, '✗', fontsize=10, fontweight='bold', color=C['danger'],
        ha='center', va='center', zorder=6,
        path_effects=[pe.withStroke(linewidth=4, foreground='white')])

# Trajectory bar
rbox(LP, BAR_Y, PW, BAR_H, C['left_fill'], C['left_bdr'])
for i in range(1, 5):
    ax.plot([LP+i*cw, LP+i*cw], [BAR_Y+0.06, BAR_Y+BAR_H-0.06],
            color='#C0BDB5', lw=0.5, ls=(0,(4,3)), zorder=3)
for i, lab in enumerate(['w₁','w₂','w₃','w₄','w₅']):
    ax.text(LP+(i+0.5)*cw, BAR_Y+BAR_H/2, lab, fontsize=11.5, fontfamily='serif',
            color=C['text'], ha='center', va='center', zorder=4)
ax.text(LCX, BAR_Y-0.10, 'Multi-Turn Agent Trajectory', fontsize=8,
        fontfamily='serif', fontstyle='italic', color=C['annot'], ha='center', va='top')

# M2
ax.text(LP, M2_Y, 'M2: Sign Misattribution', fontsize=10.5, fontweight='bold',
        fontfamily='serif', color=C['danger'])

# Neg boxes
for i in range(5):
    nx = LP + (i+0.5)*cw - NEG_S/2
    rbox(nx, NEG_Y, NEG_S, NEG_S, C['neg_fill'], C['danger'], lw=0.7, r=0.06)
    ax.text(nx+NEG_S/2, NEG_Y+NEG_S/2, '−', fontsize=16, fontweight='bold',
            color=C['danger'], ha='center', va='center', zorder=4)

for i in range(5):
    cx = LP + (i+0.5)*cw
    ax.plot([cx, cx], [BAR_Y-0.02, NEG_Y+NEG_S+0.06], color='#D5D5D5', lw=0.4, ls=':', zorder=1)

# ✗ + Correct Action
w2x = LP + 1.5*cw
ax.text(w2x, NEG_Y-0.08, '✗', fontsize=8.5, fontweight='bold', color=C['danger'],
        ha='center', va='top', zorder=5)
ca_w, ca_h = 0.88, 0.40
ca_x, ca_y = w2x-ca_w/2, NEG_Y-0.62
rbox(ca_x, ca_y, ca_w, ca_h, C['pos_fill'], C['success'], lw=0.7, r=0.06)
ax.text(w2x, ca_y+ca_h/2, 'Correct\nAction', fontsize=7.5, fontweight='bold',
        fontfamily='serif', color=C['success'], ha='center', va='center', zorder=4, linespacing=1.05)

# Brace
bl = LP + 0.5*cw - NEG_S/2 - 0.04
br = LP + 4.5*cw + NEG_S/2 + 0.04
mid = (bl+br)/2
bt, tip = NEG_Y-0.05, NEG_Y-0.20
for x1,y1,x2,y2 in [(bl,bt,bl,bt-0.04),(bl,bt-0.04,mid-0.06,tip),
                      (mid+0.06,tip,br,bt-0.04),(br,bt-0.04,br,bt)]:
    ax.plot([x1,x2],[y1,y2], color='#AAAAAA', lw=0.5, solid_capstyle='round')
ax.plot([mid-0.06,mid,mid+0.06],[tip,tip-0.04,tip], color='#AAAAAA', lw=0.5)
ax.text(mid+0.6, tip-0.08, 'All windows receive same sign', fontsize=7.5,
        fontstyle='italic', fontfamily='serif', color=C['annot'], ha='center', va='top')

# ═══════════ RIGHT PANEL ═══════════
RCX = RP + PW/2
ax.text(RCX, TITLE_Y, 'Episode-Level Training', fontsize=15, fontweight='bold',
        fontfamily='serif', color=C['text'], ha='center', va='center')

ax.text(RP, M1_Y, 'M1: Full Context Preserved', fontsize=10.5, fontweight='bold',
        fontfamily='serif', color=C['safe'])

# One long arrow
farrow(RP+PW-0.15, ARR_Y, RP+0.15, ARR_Y, C['safe'], lw=2.0, ms=13)
ax.text(RP-0.02, ARR_Y+0.22, '✓', fontsize=11, color=C['success'], fontweight='bold',
        ha='center', va='center', zorder=5,
        path_effects=[pe.withStroke(linewidth=3, foreground='white')])

# Full trajectory bar
rbox(RP, BAR_Y, PW, BAR_H, C['right_fill'], C['right_bdr'])
ax.text(RP+PW/2, BAR_Y+BAR_H/2, 'Full Episode Trajectory', fontsize=11.5,
        fontfamily='serif', color=C['text'], ha='center', va='center', zorder=4)

# M2
ax.text(RP, M2_Y, 'M2: Episode-Level Attribution', fontsize=10.5, fontweight='bold',
        fontfamily='serif', color=C['safe'])

# Â_episode box — centered vertically between Pass and Fail
ae_w, ae_h = 2.0, 0.75
ae_x = RP + 0.2
ae_cy = NEG_Y + NEG_S/2  # vertically centered with neg boxes
ae_y = ae_cy - ae_h/2
rbox(ae_x, ae_y, ae_w, ae_h, C['right_fill'], C['right_bdr'], r=0.10)
ax.text(ae_x+ae_w/2, ae_y+ae_h/2, r'$\hat{A}_{\mathrm{episode}}$',
        fontsize=15, color=C['text'], ha='center', va='center', zorder=4)

# Pass/Fail boxes — symmetric around ae_cy
spread = 0.65  # half vertical spread
p_w, p_h = 1.05, 0.50
p_x = RP + PW - p_w - 0.10
p_y_pass = ae_cy + spread
p_y_fail = ae_cy - spread - p_h

rbox(p_x, p_y_pass, p_w, p_h, C['pos_fill'], C['success'], lw=0.7, r=0.06)
ax.text(p_x+0.24, p_y_pass+p_h/2, '+', fontsize=13, fontweight='bold',
        color=C['success'], ha='center', va='center', zorder=4)
ax.text(p_x+0.65, p_y_pass+p_h/2, 'Pass', fontsize=10, fontweight='bold',
        fontfamily='serif', color=C['success'], ha='center', va='center', zorder=4)

rbox(p_x, p_y_fail, p_w, p_h, C['fail_fill'], C['danger'], lw=0.7, r=0.06)
ax.text(p_x+0.24, p_y_fail+p_h/2, '−', fontsize=13, fontweight='bold',
        color=C['danger'], ha='center', va='center', zorder=4)
ax.text(p_x+0.65, p_y_fail+p_h/2, 'Fail', fontsize=10, fontweight='bold',
        fontfamily='serif', color=C['danger'], ha='center', va='center', zorder=4)

# Curved arrows
farrow(ae_x+ae_w+0.06, ae_y+ae_h*0.80, p_x-0.06, p_y_pass+p_h/2,
       C['safe'], lw=1.3, ms=11, cs='arc3,rad=-0.20')
farrow(ae_x+ae_w+0.06, ae_y+ae_h*0.20, p_x-0.06, p_y_fail+p_h/2,
       C['safe'], lw=1.3, ms=11, cs='arc3,rad=0.20')

# Annotation
ax.text(p_x+p_w/2, ae_cy, 'Sign reflects\nepisode outcome', fontsize=7.5,
        fontstyle='italic', fontfamily='serif', color=C['annot'],
        ha='center', va='center', linespacing=1.25)

# ─── Save ───
for ext in ['png','pdf']:
    plt.savefig(f'/tmp/fig_overview_final2.{ext}', dpi=300, bbox_inches='tight',
                pad_inches=0.03, facecolor='white')
plt.close()
print("DONE")
