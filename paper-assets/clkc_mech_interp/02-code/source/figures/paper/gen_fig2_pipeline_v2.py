#!/usr/bin/env python3
"""Figure 2: Method Pipeline — four-step horizontal flow.

Print-appropriate: figsize=(7, 1.7), ~0.9x scale at textwidth.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon
import numpy as np
import os

# ── Colors (unified with Figure 1) ──
EN_BLUE = '#2C5F8A'; ZH_ORANGE = '#D35400'; TEAL = '#0B6E4F'; TEAL_LT = '#D0ECE7'
CAUSAL_RED = '#C0392B'; TEXT_DARK = '#2C3E50'; TEXT_MID = '#5D6D7E'
TEXT_LIGHT = '#95A5A6'; BORDER = '#CCD1D1'; WHITE = '#FFFFFF'; SLATE = '#3D5A80'

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Liberation Serif'],
    'mathtext.fontset': 'dejavuserif', 'font.size': 7,
    'axes.linewidth': 0, 'figure.facecolor': WHITE,
    'axes.facecolor': WHITE, 'text.color': TEXT_DARK,
})

FW, FH = 7.0, 1.7
fig, ax = plt.subplots(1, 1, figsize=(FW, FH), dpi=300)
ax.set_xlim(0, FW); ax.set_ylim(0, FH)
ax.set_aspect('equal'); ax.axis('off')
fig.patch.set_facecolor(WHITE)

# ── Layout ──
BW, BH = 1.35, 1.30
GAP = 0.45
LM = (FW - 4*BW - 3*GAP) / 2
BY = (FH - BH) / 2
def bx(i): return LM + i*(BW+GAP)

# ── Helpers ──
def shadow(x, y, w, h, r=0.06):
    ax.add_patch(FancyBboxPatch((x+0.012,y-0.012), w, h,
        boxstyle=f"round,pad=0,rounding_size={r}",
        facecolor='#00000005', edgecolor='none', zorder=1))

def sbox(i, title, sec, sub=''):
    x, y = bx(i), BY
    shadow(x, y, BW, BH)
    ax.add_patch(FancyBboxPatch((x,y), BW, BH,
        boxstyle="round,pad=0,rounding_size=0.06",
        facecolor=WHITE, edgecolor=BORDER, linewidth=0.4, zorder=2))
    br = 0.08; bcx, bcy = x+0.15, y+BH-0.14
    ax.add_patch(Circle((bcx,bcy), br, facecolor=SLATE, edgecolor='none', zorder=5))
    ax.text(bcx, bcy, str(i+1), ha='center', va='center', fontsize=6,
            fontweight='bold', color=WHITE, zorder=6)
    ax.text(x+BW/2, y+0.25, title, ha='center', va='center', fontsize=7,
            fontweight='bold', color=TEXT_DARK, zorder=5, linespacing=1.25)
    if sub:
        ax.text(x+BW/2, y+0.11, sub, ha='center', va='center', fontsize=4.5,
                color=TEXT_LIGHT, fontstyle='italic', zorder=5, linespacing=1.1)
    ax.text(x+BW/2, y+0.04, sec, ha='center', va='center', fontsize=5,
            color=TEXT_LIGHT, zorder=5)

# ── Icons ──
def icon_doc(cx, cy):
    s=0.6; dw,dh=0.22*s*2.2, 0.30*s*2.2; off=0.10*s*2
    bxx,byy = cx-dw/2+off*0.5, cy-dh/2-off*0.15
    ax.add_patch(FancyBboxPatch((bxx,byy), dw, dh,
        boxstyle="round,pad=0,rounding_size=0.03",
        facecolor=ZH_ORANGE, edgecolor='none', alpha=0.72, zorder=3.5))
    for f in [0.72,0.52,0.32]:
        ax.plot([bxx+0.04,bxx+dw-0.04],[byy+dh*f]*2, color=WHITE, lw=0.5, alpha=0.4, zorder=3.6)
    ax.text(bxx+dw*0.75, byy+dh*0.14, 'ZH', fontsize=4, color=WHITE, fontweight='bold',
            ha='center', va='center', zorder=3.7, alpha=0.7)
    fxx,fyy = cx-dw/2-off*0.3, cy-dh/2+off*0.15
    ax.add_patch(FancyBboxPatch((fxx,fyy), dw, dh,
        boxstyle="round,pad=0,rounding_size=0.03",
        facecolor=EN_BLUE, edgecolor='none', alpha=0.82, zorder=3.8))
    for f in [0.72,0.52,0.32]:
        ax.plot([fxx+0.04,fxx+dw-0.04],[fyy+dh*f]*2, color=WHITE, lw=0.5, alpha=0.5, zorder=3.9)
    ax.text(fxx+dw*0.75, fyy+dh*0.14, 'EN', fontsize=4, color=WHITE, fontweight='bold',
            ha='center', va='center', zorder=4.0, alpha=0.8)
    ax.text((fxx+dw+bxx)/2+0.02, (fyy+byy)/2+dh*0.4, '≠', fontsize=9,
            color=CAUSAL_RED, fontweight='bold', ha='center', va='center',
            zorder=4.2, alpha=0.65, bbox=dict(fc=WHITE, ec='none', pad=1, alpha=0.85))

def icon_probe(cx, cy):
    vw, vh = 0.06, 0.28
    ax.add_patch(FancyBboxPatch((cx-vw/2, cy-vh/2), vw, vh,
        boxstyle="round,pad=0,rounding_size=0.02",
        facecolor=TEAL_LT, edgecolor=TEAL, linewidth=0.8, zorder=3.5))
    ax.text(cx, cy+0.01, r'$h_l$', fontsize=6.5, color=TEAL, fontweight='bold',
            ha='center', va='center', zorder=4)
    al = 0.22
    for dx, dy, lb, c in [(1,0.10,'EN→EN',TEAL),(1,-0.10,'EN→ZH',EN_BLUE),
                           (-1,0.10,'ZH→ZH',TEAL),(-1,-0.10,'ZH→EN',ZH_ORANGE)]:
        x0 = cx+dx*(vw/2+0.02); x1 = cx+dx*al
        ax.annotate('', xy=(x1, cy+dy), xytext=(x0, cy+dy),
                    arrowprops=dict(arrowstyle='->', color=c, lw=0.7, mutation_scale=5, alpha=0.7),
                    zorder=4.5)
        ax.text(x1+dx*0.03, cy+dy, lb, fontsize=3.5, color=c, fontweight='bold',
                ha='left' if dx>0 else 'right', va='center', zorder=5, alpha=0.8)

def icon_steer(cx, cy):
    tw, th = 0.18, 0.35; nl = 6; sp = th/(nl+1)
    ax.add_patch(FancyBboxPatch((cx-tw/2, cy-th/2), tw, th,
        boxstyle="round,pad=0,rounding_size=0.03",
        facecolor='#F8F9FA', edgecolor=BORDER, linewidth=0.3, zorder=3.3))
    for i in range(nl):
        ly = cy-th/2+(i+1)*sp
        lc = CAUSAL_RED if i in [2,3] else '#D5D8DC'
        ax.plot([cx-tw/2+0.02, cx+tw/2-0.02], [ly,ly], color=lc,
                lw=1.5 if i in [2,3] else 1.0, alpha=0.6 if i in [2,3] else 0.35,
                zorder=3.5, solid_capstyle='round')
    ax.add_patch(FancyArrowPatch((cx+tw/2+0.22, cy+0.10), (cx+tw/2+0.02, cy),
        arrowstyle='-|>', color=CAUSAL_RED, lw=1.3, mutation_scale=8,
        zorder=4.5, connectionstyle='arc3,rad=-0.15'))
    ax.text(cx+tw/2+0.26, cy+0.12, 'v', fontsize=7, color=CAUSAL_RED,
            fontweight='bold', fontstyle='italic', ha='center', va='center', zorder=5)

def icon_shield(cx, cy):
    s=0.55; sw,sh=0.48*s*1.3, 0.58*s*1.3; n=30
    ty=cy+sh*0.38; my=cy-sh*0.05; by_=cy-sh*0.42
    lp=[]
    for t in np.linspace(0,1,n//2):
        lp.append([cx-sw/2*(1-0.15*t**2), ty-(ty-my)*t])
    for t in np.linspace(0,1,n//4):
        lp.append([cx-sw/2*(1-t)*(1-0.15), my-(my-by_)*t])
    rp=[[2*cx-p[0],p[1]] for p in reversed(lp)]
    pts=np.array(lp+rp)
    ax.add_patch(Polygon(pts, closed=True, facecolor=TEAL, edgecolor=SLATE,
                         linewidth=0.5, alpha=0.78, zorder=3.8))
    ip=pts.copy(); ip[:,0]=cx+(ip[:,0]-cx)*0.7; ip[:,1]=cy+(ip[:,1]-cy)*0.7
    ax.add_patch(Polygon(ip, closed=True, facecolor='#7FC4D3', edgecolor='none', alpha=0.28, zorder=3.9))
    ax.plot([cx-0.07,cx-0.02,cx+0.09],[cy-0.01,cy-0.08,cy+0.07],
            color=WHITE, lw=2.0, solid_capstyle='round', solid_joinstyle='round', zorder=5)

# ── Draw ──
steps = [
    ("ConflictQA\n+ Translation","§3.2","EN/ZH conflict pairs"),
    ("4-Direction\nProbe Training","§3.4","Detect conflict signal"),
    ("Representation\nSteering","§3.5","Inject direction vector"),
    ("Confound\nExclusion","§3.6","Rule out confounds"),
]
icons = [icon_doc, icon_probe, icon_steer, icon_shield]
for i,((t,s,sub),fn) in enumerate(zip(steps,icons)):
    sbox(i, t, s, sub)
    fn(bx(i)+BW/2, BY+BH-0.42)

# Arrows
for i in range(3):
    x1=bx(i)+BW; x2=bx(i+1); ay=BY+BH/2
    ax.plot([x1+0.03,x2-0.10],[ay,ay], color=TEXT_LIGHT, lw=0.5, alpha=0.5,
            zorder=9, linestyle=(0,(3,2)))
    ax.add_patch(FancyArrowPatch((x2-0.12,ay),(x2-0.02,ay),
        arrowstyle='-|>', color=TEXT_LIGHT, lw=0.7, mutation_scale=7,
        zorder=10, alpha=0.5))

out = 'figures/paper/fig2_pipeline'
for ext in ['png','pdf']:
    plt.savefig(f'{out}.{ext}', dpi=300, bbox_inches='tight', pad_inches=0.02, facecolor=WHITE)
plt.close()
print(f"Done: {out}.png + .pdf")
