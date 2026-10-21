"""Generate Figure 1: Diagnostic framework overview (3-panel conceptual diagram).

Three panels: Quality Estimation → Correlation-Selection Gap → Sample Selection (fails)
→ Resolution → Entity-Level Construction (works).
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Helvetica', 'Arial'],
    'font.size': 10,
    'text.antialiased': True,
})

# ── Colors ──
BLUE = '#3B7DD8'
BLUE_BG = '#EDF4FD'
BLUE_DARK = '#1A5BB5'
BLUE_SAMPLE = '#B3D4FC'

AMBER = '#E8930C'
AMBER_BG = '#FFF8EE'
AMBER_DARK = '#C47A00'

GREEN = '#43A047'
GREEN_BG = '#EEF7EF'
GREEN_DARK = '#2E7D32'

RED = '#D32F2F'
RED_BG = '#FFEBEE'
GRAY = '#757575'
GRAY_BG = '#F5F5F5'
DARK = '#263238'
WHITE = '#FFFFFF'

# ── Figure ──
fig = plt.figure(figsize=(16, 6.8))
fig.patch.set_facecolor('white')

# Three axes with spacing
gap = 0.03
left_frac = 0.30
mid_frac = 0.35
right_frac = 0.35
total = left_frac + mid_frac + right_frac + 2 * gap
lf = left_frac / total
mf = mid_frac / total
rf = right_frac / total
gf = gap / total

margin_l, margin_r = 0.02, 0.02
margin_b, margin_t = 0.03, 0.87
W = 1 - margin_l - margin_r
H = margin_t - margin_b

ax1 = fig.add_axes([margin_l, margin_b, W * lf, H])
ax2 = fig.add_axes([margin_l + W * (lf + gf), margin_b, W * mf, H])
ax3 = fig.add_axes([margin_l + W * (lf + gf + mf + gf), margin_b, W * rf, H])

for ax in [ax1, ax2, ax3]:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')


def panel_bg(ax, header_color, bg_color):
    shadow = FancyBboxPatch((0.25, 0.05), 9.5, 9.5, boxstyle="round,pad=0.2",
                            facecolor='#E0E0E0', edgecolor='none', zorder=0, alpha=0.5)
    ax.add_patch(shadow)
    bg = FancyBboxPatch((0.15, 0.15), 9.5, 9.5, boxstyle="round,pad=0.2",
                        facecolor=bg_color, edgecolor='#CFD8DC', linewidth=1.0, zorder=1)
    ax.add_patch(bg)
    hdr = FancyBboxPatch((0.15, 8.65), 9.5, 1.0, boxstyle="round,pad=0.2",
                         facecolor=header_color, edgecolor='none', zorder=2)
    ax.add_patch(hdr)


def rbox(ax, cx, cy, w, h, text, fc=WHITE, ec='#B0BEC5', fs=9, fw='normal', tc=DARK,
         z=5, ls='-', lw=1.0):
    b = FancyBboxPatch((cx - w/2, cy - h/2), w, h, boxstyle="round,pad=0.06",
                       facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z, linestyle=ls)
    ax.add_patch(b)
    ax.text(cx, cy, text, ha='center', va='center', fontsize=fs,
            fontweight=fw, color=tc, zorder=z + 1)


def arrow(ax, x1, y1, x2, y2, c=GRAY, lw=1.5, style='->', ms=13, z=4):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=ms,
                        color=c, linewidth=lw, zorder=z)
    ax.add_patch(a)


# ═══════════════════════════════════════════════════
# PANEL 1 — Quality Estimation
# ═══════════════════════════════════════════════════
panel_bg(ax1, BLUE, BLUE_BG)
ax1.text(5, 9.2, 'Quality Estimation', ha='center', va='center',
         fontsize=13, fontweight='bold', color=WHITE, zorder=3)
ax1.text(5, 8.10, '(Predicting Reliability)', ha='center', va='center',
         fontsize=9.5, fontweight='bold', color='#0D47A1', style='italic', zorder=3)

# Flow: Input x → N samples → S
rbox(ax1, 2.0, 6.85, 2.0, 0.7, 'Input  x', fc=WHITE, ec=BLUE, fs=10, fw='bold')
arrow(ax1, 3.1, 6.85, 4.2, 6.85, c=BLUE_DARK, lw=1.8)

# Sample stack
for i, lab in enumerate(['y₁', 'y₂', '⋮', 'yₙ']):
    yy = 7.40 - i * 0.38
    fs = 9 if lab != '⋮' else 11
    rbox(ax1, 5.3, yy, 1.5, 0.32, lab, fc=BLUE_SAMPLE, ec=BLUE, fs=fs, lw=0.8)
ax1.text(5.3, 7.80, 'N samples', ha='center', va='center', fontsize=8.5,
         fontweight='bold', color=BLUE_DARK, style='italic', zorder=5)

arrow(ax1, 6.15, 6.85, 7.3, 6.85, c=BLUE_DARK, lw=1.8)

# Score S — filled circle
circ = plt.Circle((8.2, 6.85), 0.5, fc=BLUE_DARK, ec='#0D47A1', lw=1.5, zorder=5)
ax1.add_patch(circ)
ax1.text(8.2, 6.85, 'S', ha='center', va='center', fontsize=15, fontweight='bold',
         color=WHITE, zorder=6)

# Correlation block
ax1.plot([1.5, 8.8], [5.70, 5.70], color='#CFD8DC', lw=0.7, zorder=3)
ax1.text(5, 5.30, 'High S   →   High F1', ha='center', va='center',
         fontsize=10, fontweight='bold', color=GREEN_DARK, zorder=5)
ax1.text(5, 4.60, 'Low S    →   Low F1', ha='center', va='center',
         fontsize=10, fontweight='bold', color=RED, zorder=5)
ax1.text(8.5, 5.30, '▲', ha='center', va='center', fontsize=9, color=GREEN_DARK, zorder=5)
ax1.text(8.5, 4.60, '▼', ha='center', va='center', fontsize=9, color=RED, zorder=5)

# Metrics (AUROC=0.82: CoNLL EM Table 2; ρ=0.39: SciERC VC Table 2)
met = FancyBboxPatch((1.3, 3.05), 7.4, 0.8, boxstyle="round,pad=0.1",
                      facecolor=GRAY_BG, edgecolor='#E0E0E0', lw=0.8, zorder=4)
ax1.add_patch(met)
ax1.text(5, 3.45, 'AUROC ≈ 0.82      ρ = 0.39', ha='center', va='center',
         fontsize=9.5, fontweight='bold', color=DARK, zorder=5, fontfamily='monospace')

# Verdict
ax1.text(2.8, 1.45, '✓', ha='center', va='center', fontsize=20, color=GREEN_DARK,
         fontweight='bold', zorder=5)
ax1.text(6.2, 1.45, 'Effective Quality\nEstimation', ha='center', va='center',
         fontsize=10.5, fontweight='bold', color=GREEN_DARK, zorder=5, linespacing=1.3)


# ═══════════════════════════════════════════════════
# PANEL 2 — Sample Selection
# ═══════════════════════════════════════════════════
panel_bg(ax2, AMBER, AMBER_BG)
ax2.text(5, 9.2, 'Sample Selection', ha='center', va='center',
         fontsize=13, fontweight='bold', color=WHITE, zorder=3)
ax2.text(5, 8.10, '(Choosing Best Output)', ha='center', va='center',
         fontsize=9.5, fontweight='bold', color='#E65100', style='italic', zorder=3)

# Samples with identical scores
sy = [7.25, 6.45, 5.65, 4.85]
sl = ['y₁', 'y₂', 'y₃', 'yₙ']
for i, (yy, lab) in enumerate(zip(sy, sl)):
    if i == 3:
        ax2.text(2.8, 5.25, '⋮', ha='center', va='center', fontsize=12, color=GRAY, zorder=5)
    rbox(ax2, 2.8, yy, 1.3, 0.48, lab, fc='#FFE0B2', ec=AMBER, fs=10, lw=0.9)
    rbox(ax2, 5.5, yy, 2.4, 0.44, 'S = 0.73', fc=RED_BG, ec=RED, fs=9.5, fw='bold', tc=RED)

# Bracket
ax2.plot([7.1, 7.5, 7.5, 7.1], [7.25, 7.25, 4.85, 4.85], color=RED, lw=1.8, zorder=5)
ax2.text(8.3, 6.05, 'Same\nscore!', ha='center', va='center', fontsize=9,
         fontweight='bold', color=RED, zorder=5, linespacing=1.2)

# Explanation
ax2.text(5, 4.05, 'Instance-level signal:', ha='center', va='center',
         fontsize=9.5, fontweight='bold', color=RED, zorder=5)
ax2.text(5, 3.45, 'same score for all  yᵢ  from same  x', ha='center', va='center',
         fontsize=8.5, color=RED, zorder=5)
ax2.text(5, 2.85, 'Cannot discriminate among samples', ha='center', va='center',
         fontsize=8.5, color=GRAY, style='italic', zorder=5)

arrow(ax2, 5, 2.45, 5, 1.95, c=RED, lw=1.5)

rbox(ax2, 5, 1.60, 5.5, 0.55, 'best-of-N  ≤  greedy', fc=RED_BG, ec=RED,
     fs=11, fw='bold', tc=RED)

# Verdict
ax2.text(2.8, 0.55, '✗', ha='center', va='center', fontsize=22, color=RED,
         fontweight='bold', zorder=5)
ax2.text(6.0, 0.55, 'Selection Fails', ha='center', va='center',
         fontsize=11, fontweight='bold', color=RED, zorder=5)


# ═══════════════════════════════════════════════════
# PANEL 3 — Entity-Level Construction
# ═══════════════════════════════════════════════════
panel_bg(ax3, GREEN, GREEN_BG)
ax3.text(5, 9.2, 'Entity-Level Construction', ha='center', va='center',
         fontsize=13, fontweight='bold', color=WHITE, zorder=3)
ax3.text(5, 8.10, '(Building New Output)', ha='center', va='center',
         fontsize=9.5, fontweight='bold', color='#1B5E20', style='italic', zorder=3)

# Entity grid: 4 samples × 4 entity slots
ent_fc = {
    'PER': '#66BB6A',
    'LOC': '#42A5F5',
    'ORG': '#FFA726',
}
ent_data = [
    ['PER', 'LOC', '',    'ORG'],
    ['PER', '',    'LOC', 'ORG'],
    ['PER', 'LOC', 'LOC', ''   ],
    ['PER', '',    '',    'ORG'],
]
ey = [7.35, 6.70, 6.05, 5.40]

ax3.text(1.3, 7.80, 'Samples', ha='center', va='center', fontsize=7.5, color=GRAY,
         style='italic', zorder=5)
# Frequency row header
ax3.text(1.3, 4.70, 'freq:', ha='center', va='center', fontsize=7.5, color=GREEN_DARK,
         fontweight='bold', zorder=5)

for si, (yy, ents) in enumerate(zip(ey, ent_data)):
    ax3.text(1.3, yy, f'y{si+1}:', ha='center', va='center', fontsize=8, color=GRAY, zorder=5)
    for ei, e in enumerate(ents):
        cx = 3.0 + ei * 1.65
        if e:
            rbox(ax3, cx, yy, 1.35, 0.35, e, fc=ent_fc[e], ec='#FFFFFF40',
                 fs=8, fw='bold', tc=WHITE, lw=0.6)
        else:
            rbox(ax3, cx, yy, 1.35, 0.35, '—', fc=WHITE, ec='#C8E6C9',
                 fs=7, tc='#BDBDBD', ls='--', lw=0.6)

# Frequency counts
freqs = ['4/4', '2/4', '2/4', '3/4']
freq_pass = [True, True, True, True]
for ei, (fr, ok) in enumerate(zip(freqs, freq_pass)):
    cx = 3.0 + ei * 1.65
    c = GREEN_DARK if ok else RED
    rbox(ax3, cx, 4.70, 1.0, 0.3, fr, fc='#C8E6C9' if ok else RED_BG, ec=c,
         fs=8, fw='bold', tc=c, lw=0.7)

# Threshold
ax3.plot([2.0, 8.8], [4.20, 4.20], color=GREEN_DARK, lw=1.5, ls='--', zorder=5)
ax3.text(9.0, 4.20, 'θ = 2/N', ha='left', va='center', fontsize=9, fontweight='bold',
         color=GREEN_DARK, zorder=5)

# Majority vote label
rbox(ax3, 5, 3.55, 4.5, 0.5, 'Entity-level majority vote', fc=WHITE, ec=GREEN_DARK,
     fs=9.5, fw='bold', tc=GREEN_DARK, lw=1.0)

ax3.text(5, 2.85, 'Keep entity if  freq ≥ θ', ha='center', va='center',
         fontsize=9, color=GREEN_DARK, fontweight='bold', zorder=5)

arrow(ax3, 5, 2.45, 5, 1.95, c=GREEN_DARK, lw=1.8)

rbox(ax3, 5, 1.55, 5.2, 0.6, 'Constructs NEW output', fc='#A5D6A7', ec=GREEN_DARK,
     fs=10.5, fw='bold', tc=GREEN_DARK, lw=1.2)

# +1.4pp: Few-NERD LP-weighted entity construction, 4-seed mean (Table 5)
ax3.text(5, 0.90, '+1.4 pp', ha='center', va='center', fontsize=16,
         fontweight='bold', color=GREEN_DARK, zorder=5)
ax3.text(5, 0.40, '(Few-NERD, 4-seed)', ha='center', va='center', fontsize=8,
         color=GRAY, style='italic', zorder=5)


# ═══════════════════════════════════════════════════
# CONNECTING BANNERS (figure coordinates)
# ═══════════════════════════════════════════════════

# "Correlation–Selection Gap" — spans Panel 1 → Panel 2
csg_x = (margin_l + W * lf + margin_l + W * (lf + gf) + W * mf) / 2
csg_x = margin_l + W * (lf + gf / 2)  # centered on the gap

fig.text(0.365, 0.935, 'Correlation–Selection Gap', ha='center', va='center',
         fontsize=12, fontweight='bold', color=RED, zorder=10,
         bbox=dict(boxstyle='round,pad=0.45', facecolor=RED_BG,
                   edgecolor=RED, linewidth=1.8, alpha=0.95))

# Arrows from panel edges to banner
for (x1, y1, x2, y2) in [(0.26, 0.90, 0.30, 0.925), (0.43, 0.925, 0.48, 0.90)]:
    fig.patches.append(FancyArrowPatch(
        (x1, y1), (x2, y2), arrowstyle='->', mutation_scale=11,
        color=RED, linewidth=1.5, transform=fig.transFigure, zorder=9))

# "Resolution" — between Panel 2 and Panel 3
fig.text(0.685, 0.935, 'Resolution', ha='center', va='center',
         fontsize=10.5, fontweight='bold', color=GREEN_DARK, zorder=10,
         bbox=dict(boxstyle='round,pad=0.3', facecolor=GREEN_BG,
                   edgecolor=GREEN_DARK, linewidth=1.2, alpha=0.95))

for (x1, y1, x2, y2) in [(0.62, 0.90, 0.655, 0.925), (0.715, 0.925, 0.76, 0.90)]:
    fig.patches.append(FancyArrowPatch(
        (x1, y1), (x2, y2), arrowstyle='->', mutation_scale=11,
        color=GREEN_DARK, linewidth=1.5, transform=fig.transFigure, zorder=9))

# ── Save ──
out = os.path.dirname(os.path.abspath(__file__))
for ext in ['png', 'pdf']:
    plt.savefig(f'{out}/fig_overview.{ext}', dpi=300, bbox_inches='tight',
                pad_inches=0.05, facecolor='white', edgecolor='none')
plt.close()
print('Saved fig_overview.png + fig_overview.pdf')
