import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
})

C_EAPIG = '#0072B2'
C_EP = '#56B4E9'
C_ACDC = '#E69F00'
C_FAIL = '#D55E00'
C_BORDER = '#444444'

fig, ax = plt.subplots(figsize=(15, 5.8))
ax.set_xlim(-0.3, 15.0)
ax.set_ylim(-1.2, 6.8)
ax.axis('off')

def draw_box(x, y, w, h, text, fc='white', ec=C_BORDER, fs=10, fw='normal',
             tc='black', lw=1.5, zorder=2):
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle='round,pad=0.12',
                          facecolor=fc, edgecolor=ec,
                          linewidth=lw, zorder=zorder)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fs,
            fontweight=fw, color=tc, zorder=zorder+1, linespacing=1.25)

def arrow(x1, y1, x2, y2, color='#666666', lw=1.3):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                shrinkA=0, shrinkB=0), zorder=1)

# Y positions for three branches
Y = [5.0, 3.0, 1.0]  # EAP-IG, EP, ACDC

# X positions
X_TRANS = 1.0
X_METH  = 3.3
X_THRESH = 5.8
X_CIRC  = 7.8
X_INTER = 9.8
X_CSS   = 11.5
X_CPR   = 13.3

# ── 1. Transformer ──
draw_box(X_TRANS, 3.0, 1.5, 4.6, 'Transformer\nModel', fc='#EDEDED',
         ec='#999999', fs=12, fw='bold')

for y in Y:
    arrow(X_TRANS + 0.75, y, X_METH - 0.75, y)

# ── 2. Method boxes ──
methods = [
    ('EAP-IG\n(gradient)', C_EAPIG),
    ('EP\n(gradient)', C_EP),
    ('ACDC\n(greedy)', C_ACDC),
]
for (label, color), y in zip(methods, Y):
    draw_box(X_METH, y, 1.35, 0.8, label, fc=color, ec=color,
             fs=10.5, fw='bold', tc='white')

# Arrows method → threshold
for y in Y:
    arrow(X_METH + 0.68, y, X_THRESH - 0.55, y)

# ── 3. Thresholding boxes ──
thresh_info = [
    ('top-k', '#EDF2F9'),
    ('top-k', '#EDF2F9'),
    ('isinf', '#FFF3E0'),
]
for (label, fc), y in zip(thresh_info, Y):
    draw_box(X_THRESH, y, 0.95, 0.6, label, fc=fc, fs=10.5, ec='#AAAAAA')

# Arrows threshold → circuit
for y in Y:
    arrow(X_THRESH + 0.48, y, X_CIRC - 0.42, y)

# ── 4. Binary circuit boxes ──
circs = [('C₁', C_EAPIG), ('C₂', C_EP), ('C₃', C_ACDC)]
for (label, color), y in zip(circs, Y):
    draw_box(X_CIRC, y, 0.7, 0.6, label, fc=color, ec=color,
             fs=13, fw='bold', tc='white')

# Arrows circuits → intersection (converge)
for y in Y:
    arrow(X_CIRC + 0.35, y, X_INTER - 0.42, 3.0)

# ── 5. Intersection ──
draw_box(X_INTER, 3.0, 0.7, 0.7, '∩', fc='#EDEDED', ec='#999999',
         fs=18, fw='bold')

arrow(X_INTER + 0.35, 3.0, X_CSS - 0.45, 3.0)

# ── 6. CSS result ──
draw_box(X_CSS, 3.0, 0.8, 0.7, 'CSS\n= 1.0', fc='#E8F5E9', ec='#4CAF50',
         fs=10, fw='bold')

arrow(X_CSS + 0.4, 3.0, X_CPR - 0.48, 3.0)

# ── 7. CPR evaluation ──
draw_box(X_CPR, 3.0, 0.85, 0.7, 'CPR\nEval', fc='#FFF3E0', ec='#EF6C00',
         fs=10, fw='bold')

# ── Arrow labels (small italic, between boxes) ──
for y in Y:
    ax.text((X_METH + X_THRESH) / 2, y + 0.42, 'scores',
            ha='center', va='bottom', fontsize=7.5, color='#888888',
            fontstyle='italic')
    ax.text((X_THRESH + X_CIRC) / 2, y + 0.32, 'binarize',
            ha='center', va='bottom', fontsize=7.5, color='#888888',
            fontstyle='italic')


# ══════════════════════════════════════════════════════════════
# FAILURE MODES
# ══════════════════════════════════════════════════════════════

def fm_outline(x, y, w, h):
    rect = FancyBboxPatch((x - w/2, y - h/2), w, h,
                           boxstyle='round,pad=0.08',
                           facecolor='none', edgecolor=C_FAIL,
                           linewidth=2.0, linestyle=(0, (5, 3)), zorder=4)
    ax.add_patch(rect)

def fm_callout(text, xy, xytext, conn='arc3,rad=0.15'):
    ax.annotate(text, xy=xy, xytext=xytext,
                fontsize=8.5, color=C_FAIL, fontweight='bold',
                ha='center', va='center', linespacing=1.3,
                bbox=dict(boxstyle='round,pad=0.35', facecolor='#FFF0F0',
                          edgecolor=C_FAIL, alpha=0.95, lw=1.2),
                arrowprops=dict(arrowstyle='->', color=C_FAIL, lw=1.5,
                                connectionstyle=conn),
                zorder=6)

# FM1: isinf pathology — around ACDC's threshold box
fm_outline(X_THRESH, Y[2], 1.2, 0.9)
fm_callout('FM1  isinf pathology\n|C₃|=14  vs  |C₁|=|C₂|=100\n→  CSS ⊆ C₃',
           xy=(X_THRESH, Y[2] - 0.45),
           xytext=(X_THRESH + 1.5, -0.6),
           conn='arc3,rad=-0.2')

# FM2: method correlation — around intersection box
fm_outline(X_INTER, 3.0, 1.0, 1.0)
fm_callout('FM2  Method correlation\nJ(C₁, C₂) = 0.82  →  K ≈ 2',
           xy=(X_INTER, 3.5),
           xytext=(X_INTER + 0.2, 5.8),
           conn='arc3,rad=0.1')

# FM3: granularity mismatch — around all method boxes
fm_outline(X_METH, 3.0, 1.65, (Y[0] - Y[2]) + 1.2)
fm_callout('FM3  Granularity mismatch\nblock  vs  edge scoring  →  J ≈ 0',
           xy=(X_METH + 0.83, Y[0] + 0.4),
           xytext=(X_METH + 2.8, 6.2),
           conn='arc3,rad=0.2')

# ── Pipeline stage labels (very top, muted) ──
stages = [
    (X_TRANS, 'Model'),
    (X_METH, 'Methods'),
    ((X_THRESH + X_CIRC) / 2, 'Binarization'),
    (X_INTER, 'Consensus'),
    (X_CSS, 'CSS'),
    (X_CPR, 'Eval'),
]
# Only show labels that don't overlap with FM callouts
for x, label in stages:
    ax.text(x, 6.55, label, ha='center', va='top', fontsize=7.5,
            color='#BBBBBB', fontstyle='italic')

# Save
outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper'
fig.savefig(f'{outdir}/fig1_overview.pdf', format='pdf')
fig.savefig(f'{outdir}/fig1_overview.png', format='png', dpi=300)
plt.close()
print(f'Saved: {outdir}/fig1_overview.pdf')
print(f'Saved: {outdir}/fig1_overview.png')
