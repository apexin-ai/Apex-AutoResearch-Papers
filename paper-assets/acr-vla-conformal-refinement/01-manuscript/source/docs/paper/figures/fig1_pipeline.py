"""Pipeline figure for ACR-VLA Conformal Refinement (Figure 1).

Flow:
  O_t -> Frozen VLA (SmolVLA 0.4B, ~170ms) -> K=2 samples (a^1, a^2)
       -> Compute d2 = ||a^1 - a^2||_2 -> Decision: d2 > tau?
         YES (hard, ~3-20%):  Argmin Select -> CRM Correction (+0.25ms) -> Execute
         NO  (easy, ~80-97%): Argmin Select                                -> Execute
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 11,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'cm',
})

C = {
    'vla':      '#7F8C8D',
    'samples':  '#E69F00',
    'd2':       '#8B6BAE',
    'decision': '#1E8449',
    'crm':      '#1A5276',
    'easy':     '#1A5276',
    'hard':     '#A93226',
    'arrow':    '#555555',
    'shadow':   '#B0B0B0',
}

FILLS = {
    'vla':      '#F2F2F2',
    'samples':  '#FFF4E0',
    'd2':       '#F0EAF5',
    'decision': '#E8F6EF',
    'crm':      '#D4E6F1',
    'easy_bg':  '#EBF5FB',
    'hard_bg':  '#FDEDEC',
    'easy':     '#D4E6F1',
    'hard':     '#FADBD8',
}

FS_TITLE = 11.0
FS_BOX = 10.0
FS_LABEL = 9.0
FS_MATH = 12.0
FS_BRANCH = 10.5


def shadow_box(ax, cx, cy, w, h, text, fc='white', ec='black', lw=1.2,
               fontsize=FS_BOX, textcolor='black', rounding=0.10, shadow=True):
    if shadow:
        ax.add_patch(FancyBboxPatch(
            (cx - w / 2 + 0.03, cy - h / 2 - 0.03), w, h,
            boxstyle=f'round,pad=0.02,rounding_size={rounding}',
            linewidth=0, edgecolor='none', facecolor=C['shadow'],
            alpha=0.22, zorder=1))
    ax.add_patch(FancyBboxPatch(
        (cx - w / 2, cy - h / 2), w, h,
        boxstyle=f'round,pad=0.02,rounding_size={rounding}',
        linewidth=lw, edgecolor=ec, facecolor=fc, zorder=2))
    ax.text(cx, cy, text, ha='center', va='center',
            fontsize=fontsize, color=textcolor, zorder=3)


def diamond(ax, cx, cy, w, h, text, fc='white', ec='black', lw=1.4,
            fontsize=FS_BOX, textcolor='black'):
    d = 0.035
    ax.add_patch(Polygon(
        [(cx + d, cy + h / 2 - d), (cx + w / 2 + d, cy - d),
         (cx + d, cy - h / 2 - d), (cx - w / 2 + d, cy - d)],
        closed=True, facecolor=C['shadow'], edgecolor='none',
        alpha=0.18, zorder=1))
    ax.add_patch(Polygon(
        [(cx, cy + h / 2), (cx + w / 2, cy),
         (cx, cy - h / 2), (cx - w / 2, cy)],
        closed=True, facecolor=fc, edgecolor=ec,
        linewidth=lw, joinstyle='round', zorder=2))
    ax.text(cx, cy, text, ha='center', va='center',
            fontsize=fontsize, color=textcolor, zorder=3)


def arrow(ax, x1, y1, x2, y2, color='#555555', lw=0.9, ms=9):
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=ms,
        linewidth=lw, color=color, shrinkA=0, shrinkB=0,
        capstyle='round', joinstyle='round', zorder=3))


def txt(ax, x, y, s, color, size, weight='normal', style='normal',
        stroke=1.8, ha='center', va='center'):
    t = ax.text(x, y, s, fontsize=size, color=color,
                fontweight=weight, fontstyle=style, ha=ha, va=va, zorder=5)
    t.set_path_effects([pe.withStroke(linewidth=stroke, foreground='white')])


# -------- Canvas --------
fig, ax = plt.subplots(figsize=(8.5, 4.0))
ax.set_xlim(-0.15, 16.2)
ax.set_ylim(-0.60, 7.2)
ax.set_aspect('auto')
ax.axis('off')

MID = 2.90

# -------- Background panels --------
ax.add_patch(FancyBboxPatch(
    (9.55, 3.65), 6.40, 3.05,
    boxstyle='round,pad=0.12,rounding_size=0.30',
    linewidth=0.6, edgecolor=C['hard'], facecolor=FILLS['hard_bg'],
    alpha=0.35, zorder=0, linestyle=(0, (6, 3))))

ax.add_patch(FancyBboxPatch(
    (9.55, -0.25), 5.20, 2.55,
    boxstyle='round,pad=0.12,rounding_size=0.30',
    linewidth=0.6, edgecolor=C['easy'], facecolor=FILLS['easy_bg'],
    alpha=0.35, zorder=0, linestyle=(0, (6, 3))))

# -------- Input: O_t --------
ax.add_patch(mpatches.Circle((0.53, MID - 0.03), 0.38,
                             facecolor=C['shadow'], edgecolor='none',
                             alpha=0.18, zorder=1))
ax.add_patch(mpatches.Circle((0.50, MID), 0.38, facecolor='#F0F0F0',
                             edgecolor='#555555', linewidth=1.0, zorder=2))
ax.text(0.50, MID, r'$\mathbf{O}_t$', ha='center', va='center',
        fontsize=FS_MATH, fontweight='bold', zorder=3)
ax.text(0.50, MID - 0.75, 'observation', ha='center', va='top',
        fontsize=FS_LABEL, color='#999999', fontstyle='italic')

# -------- Main pipeline stages --------
vla_x = 2.30
shadow_box(ax, vla_x, MID, 1.75, 0.92,
           'Frozen VLA\n(SmolVLA 0.4B)',
           fc=FILLS['vla'], ec=C['vla'], lw=1.2)
ax.text(vla_x, MID - 0.72, '~170 ms', ha='center', va='top',
        fontsize=FS_LABEL, color=C['vla'], fontstyle='italic')

sam_x = 4.45
shadow_box(ax, sam_x, MID, 1.60, 0.92,
           r'$K{=}2$ Samples' + '\n' + r'$\mathbf{a}^{1},\ \mathbf{a}^{2}$',
           fc=FILLS['samples'], ec=C['samples'], lw=1.2)
ax.text(sam_x, MID - 0.72, 'batched (shared pass)', ha='center', va='top',
        fontsize=FS_LABEL, color=C['samples'], fontstyle='italic')

d2_x = 6.75
shadow_box(ax, d2_x, MID, 1.90, 0.92,
           'Compute\n' + r'$d_2 = \|\mathbf{a}^{1} - \mathbf{a}^{2}\|_2$',
           fc=FILLS['d2'], ec=C['d2'], lw=1.2)

DX = 9.10
diamond(ax, DX, MID, 1.30, 1.40,
        r'$d_2 > \tau\,?$',
        fc=FILLS['decision'], ec=C['decision'], lw=1.3,
        fontsize=FS_BRANCH, textcolor=C['decision'])

# -------- Hard path (Yes) - upper --------
hard_y = 5.15
BOX_H = 0.76

shadow_box(ax, 11.30, hard_y, 1.22, BOX_H,
           'Argmin\nSelect',
           fc=FILLS['hard'], ec=C['hard'], lw=1.1)

shadow_box(ax, 13.15, hard_y, 1.55, 0.90,
           'CRM\nCorrection',
           fc=FILLS['crm'], ec=C['crm'], lw=1.6, fontsize=FS_BOX + 0.4,
           rounding=0.12)
ax.text(13.15, hard_y - 0.70, r'~327K params, +0.25 ms',
        ha='center', va='top', fontsize=FS_LABEL, color=C['crm'],
        fontstyle='italic')

shadow_box(ax, 14.90, hard_y, 1.10, BOX_H,
           r'$\mathbf{a}^{*}$' + '\nExecute',
           fc='#2C3E50', ec=C['hard'], lw=1.0,
           fontsize=FS_BOX, textcolor='white')

# -------- Easy path (No) - lower --------
easy_y = 0.95

shadow_box(ax, 11.30, easy_y, 1.22, BOX_H,
           'Argmin\nSelect',
           fc=FILLS['easy'], ec=C['easy'], lw=1.0)

shadow_box(ax, 13.30, easy_y, 1.10, BOX_H,
           r'$\mathbf{a}^{*}$' + '\nExecute',
           fc='#2C3E50', ec=C['easy'], lw=1.0,
           fontsize=FS_BOX, textcolor='white')

# -------- Arrows: main pipeline --------
ac = C['arrow']
arrow(ax, 0.90, MID, 1.41, MID, color=ac)
arrow(ax, 3.19, MID, 3.63, MID, color=ac)
arrow(ax, 5.27, MID, 5.78, MID, color=ac)
arrow(ax, 7.72, MID, 8.43, MID, color=ac)

# -------- Arrows: decision branches --------
arrow(ax, DX + 0.30, MID + 0.50, 10.68, 4.90,
      color=C['hard'], lw=1.2)
arrow(ax, DX + 0.30, MID - 0.50, 10.68, 1.20,
      color=C['easy'], lw=1.1)

mx_h = (DX + 0.30 + 10.68) / 2
my_h = (MID + 0.50 + 4.90) / 2
txt(ax, mx_h - 0.40, my_h + 0.20, 'Yes', C['hard'],
    size=FS_BRANCH, weight='bold', style='italic', stroke=2.0)
txt(ax, mx_h + 0.40, my_h - 0.05, '(~3–20%)', '#888888',
    size=FS_LABEL, stroke=1.6)

mx_e = (DX + 0.30 + 10.68) / 2
my_e = (MID - 0.50 + 1.20) / 2
txt(ax, mx_e - 0.40, my_e - 0.20, 'No', C['easy'],
    size=FS_BRANCH, weight='bold', style='italic', stroke=2.0)
txt(ax, mx_e + 0.40, my_e + 0.05, '(~80–97%)', '#888888',
    size=FS_LABEL, stroke=1.6)

# -------- Arrows: branch internals --------
arrow(ax, 11.93, hard_y, 12.35, hard_y, color=C['hard'], lw=0.9)
arrow(ax, 13.95, hard_y, 14.33, hard_y, color=C['hard'], lw=0.9)
arrow(ax, 11.93, easy_y, 12.73, easy_y, color=C['easy'], lw=0.8)

# -------- Path banner labels --------
ax.text(13.10, 6.40, 'Hard Path · Refine',
        ha='center', va='center', fontsize=FS_TITLE, color=C['hard'],
        fontweight='bold', fontstyle='italic')
ax.text(12.15, 0.03, 'Easy Path · Direct',
        ha='center', va='center', fontsize=FS_TITLE, color=C['easy'],
        fontweight='bold', fontstyle='italic')

# -------- Save --------
out_dir = os.path.dirname(os.path.abspath(__file__))
for ext in ['pdf', 'png']:
    plt.savefig(os.path.join(out_dir, f'fig1_pipeline.{ext}'), dpi=300,
                bbox_inches='tight', pad_inches=0.06)
plt.close()
print('Saved fig1_pipeline.pdf and fig1_pipeline.png')
