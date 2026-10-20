import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

# Okabe-Ito palette
C_STANDARD = '#56B4E9'
C_RASP = '#E69F00'
C_COLLAPSE = '#D55E00'
C_TRADEOFF = '#009E73'
C_BG_STANDARD = '#E8F4FD'
C_BG_RASP = '#FFF3E0'
C_TEXT = '#333333'
C_LIGHT_GRAY = '#F5F5F5'

fig, ax = plt.subplots(1, 1, figsize=(14, 7))
ax.set_xlim(0, 14)
ax.set_ylim(0, 7)
ax.axis('off')

def draw_box(ax, x, y, w, h, text, color, fc=None, fontsize=10, bold=False, text_color=C_TEXT):
    if fc is None:
        fc = color + '22'
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                         facecolor=fc, edgecolor=color, linewidth=1.8)
    ax.add_patch(box)
    weight = 'bold' if bold else 'normal'
    ax.text(x + w/2, y + h/2, text, ha='center', va='center',
            fontsize=fontsize, fontweight=weight, color=text_color,
            multialignment='center')
    return box

def draw_arrow(ax, x1, y1, x2, y2, color='#555555', style='->', lw=1.5):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                            arrowstyle=style, color=color,
                            linewidth=lw, mutation_scale=15,
                            connectionstyle="arc3,rad=0")
    ax.add_patch(arrow)

# === Title ===
ax.text(7, 6.75, 'Recovery-Aware Structured Pruning (RASP): Framework Overview',
        ha='center', va='center', fontsize=13, fontweight='bold', color=C_TEXT)

# === STANDARD PIPELINE (top row) ===
y_std = 4.8
row_h = 1.5
ax.text(0.3, y_std + row_h/2, 'Standard\nPipeline', ha='center', va='center',
        fontsize=11, fontweight='bold', color=C_STANDARD)

# Background band
bg_std = FancyBboxPatch((1.0, y_std - 0.05), 12.5, row_h + 0.1,
                        boxstyle="round,pad=0.1",
                        facecolor=C_BG_STANDARD, edgecolor='none', alpha=0.5)
ax.add_patch(bg_std)

# Boxes
bw, bh = 2.8, 0.9
by_std = y_std + 0.35

draw_box(ax, 1.3, by_std, bw, bh, 'Prune\n(Importance-only)', C_STANDARD, fontsize=10, bold=True)
draw_box(ax, 5.0, by_std, bw, bh, 'SFT Warmup', C_STANDARD, fontsize=10, bold=True)
draw_box(ax, 8.7, by_std, bw, bh, 'GRPO Alignment', C_STANDARD, fontsize=10, bold=True)

# Annotations below boxes
ax.text(1.3 + bw/2, by_std - 0.2, 'Remove lowest $I(h)$',
        ha='center', va='top', fontsize=8.5, color='#555555', style='italic')
ax.text(5.0 + bw/2, by_std - 0.2, 'Restore generation',
        ha='center', va='top', fontsize=8.5, color='#555555', style='italic')
ax.text(8.7 + bw/2, by_std - 0.2, '⚠ Transient collapse (step 90)',
        ha='center', va='top', fontsize=8.5, color=C_COLLAPSE, style='italic')

# Arrows
draw_arrow(ax, 1.3+bw, by_std+bh/2, 5.0, by_std+bh/2, color=C_STANDARD)
draw_arrow(ax, 5.0+bw, by_std+bh/2, 8.7, by_std+bh/2, color=C_STANDARD)

# Result box
draw_box(ax, 11.8, by_std + 0.05, 1.6, 0.8,
         'Peak: 0.081\nCollapse', C_STANDARD, fontsize=9, bold=False)
draw_arrow(ax, 8.7+bw, by_std+bh/2, 11.8, by_std+bh/2, color=C_STANDARD)
ax.text(12.6, by_std + 0.85 + 0.1, 'SFT → GRPO',
        ha='center', va='bottom', fontsize=7.5, color='#777777')

# === RASP PIPELINE (bottom row) ===
y_rasp = 2.5
ax.text(0.3, y_rasp + row_h/2, 'RASP\nPipeline', ha='center', va='center',
        fontsize=11, fontweight='bold', color=C_RASP)

# Background band
bg_rasp = FancyBboxPatch((1.0, y_rasp - 0.05), 12.5, row_h + 0.1,
                         boxstyle="round,pad=0.1",
                         facecolor=C_BG_RASP, edgecolor='none', alpha=0.5)
ax.add_patch(bg_rasp)

by_rasp = y_rasp + 0.35

draw_box(ax, 1.3, by_rasp, bw, bh, 'Prune\n(Recovery-Aware)', C_RASP, fontsize=10, bold=True)
draw_box(ax, 5.0, by_rasp, bw, bh, 'SFT Warmup', C_RASP, fontsize=10, bold=True)
draw_box(ax, 8.7, by_rasp, bw, bh, 'GRPO Alignment', C_COLLAPSE,
         fc=C_COLLAPSE+'22', fontsize=10, bold=True)

# Annotations below boxes
ax.text(1.3 + bw/2, by_rasp - 0.15, r'$S(h) = I(h) \times (1{-}F(h))^\alpha$',
        ha='center', va='top', fontsize=9, color='#555555')
ax.text(1.3 + bw/2, by_rasp - 0.42, r'$F(h_i) = \frac{1}{|\mathcal{H}_\ell|-1} \sum_{j \neq i} \mathrm{CKA}(\mathbf{X}_{h_i}, \mathbf{X}_{h_j})$',
        ha='center', va='top', fontsize=7, color='#777777')
ax.text(5.0 + bw/2, by_rasp - 0.2, '+2.2pp advantage',
        ha='center', va='top', fontsize=8.5, color=C_TRADEOFF, fontweight='bold')
ax.text(8.7 + bw/2, by_rasp - 0.2, '⚠ Permanent collapse (step 10)',
        ha='center', va='top', fontsize=8.5, color=C_COLLAPSE, fontweight='bold')

# Arrows
draw_arrow(ax, 1.3+bw, by_rasp+bh/2, 5.0, by_rasp+bh/2, color=C_RASP)
draw_arrow(ax, 5.0+bw, by_rasp+bh/2, 8.7, by_rasp+bh/2, color=C_RASP)

# Result box
draw_box(ax, 11.8, by_rasp + 0.05, 1.6, 0.8,
         'Peak: 0.061\nFull collapse', C_COLLAPSE, fontsize=9, bold=False)
draw_arrow(ax, 8.7+bw, by_rasp+bh/2, 11.8, by_rasp+bh/2, color=C_RASP)
ax.text(12.6, by_rasp + 0.85 + 0.1, 'SFT → GRPO',
        ha='center', va='bottom', fontsize=7.5, color='#777777')

# === Bidirectional Decoupling annotations (right side) ===
ax.text(13.7, 4.2, 'Reward ↑\n≠ Accuracy ↑', ha='center', va='center',
        fontsize=8.5, color=C_COLLAPSE, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF0E0', edgecolor=C_COLLAPSE, lw=1))
ax.text(13.7, 3.4, 'Reward ↓\n≠ Accuracy ↓', ha='center', va='center',
        fontsize=8.5, color=C_COLLAPSE, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF0E0', edgecolor=C_COLLAPSE, lw=1))
ax.annotate('', xy=(13.7, 3.75), xytext=(13.7, 4.0),
            arrowprops=dict(arrowstyle='<->', color=C_COLLAPSE, lw=1.2))
ax.text(13.7, 4.65, 'Bidirectional\nDecoupling', ha='center', va='bottom',
        fontsize=8, color=C_COLLAPSE, fontweight='bold')

# === CORE FINDING PANEL (bottom) ===
panel_x, panel_y, panel_w, panel_h = 1.5, 0.2, 11.0, 2.0
panel = FancyBboxPatch((panel_x, panel_y), panel_w, panel_h,
                       boxstyle="round,pad=0.15",
                       facecolor=C_TRADEOFF + '15', edgecolor=C_TRADEOFF, linewidth=2.0)
ax.add_patch(panel)

ax.text(panel_x + panel_w/2, panel_y + panel_h - 0.25,
        'Core Finding: Redundancy–Stability Tradeoff',
        ha='center', va='top', fontsize=12, fontweight='bold', color=C_TRADEOFF)

# Two columns of findings
col1_x = panel_x + 1.5
col2_x = panel_x + panel_w/2 + 1.0
finding_y = panel_y + panel_h - 0.65

ax.text(col1_x, finding_y, 'SFT Recovery', ha='center', va='top',
        fontsize=10, fontweight='bold', color=C_STANDARD)
ax.text(col1_x, finding_y - 0.4, 'RASP +2.2pp advantage\n(removes redundant, keeps unique)',
        ha='center', va='top', fontsize=9, color=C_TEXT)

ax.text(col2_x, finding_y, 'RLVR (GRPO) Recovery', ha='center', va='top',
        fontsize=10, fontweight='bold', color=C_COLLAPSE)
ax.text(col2_x, finding_y - 0.4, 'RASP 6× faster collapse\n(redundancy = exploration buffer)',
        ha='center', va='top', fontsize=9, color=C_TEXT)

# Central insight
ax.text(panel_x + panel_w/2, panel_y + 0.25,
        '→  Optimal pruning is conditioned on recovery paradigm  ←',
        ha='center', va='bottom', fontsize=10.5, fontweight='bold', color=C_TRADEOFF,
        style='italic')

# Divider line between the two findings
ax.plot([panel_x + panel_w/2 - 0.2, panel_x + panel_w/2 - 0.2],
        [finding_y - 0.9, finding_y + 0.15], color='#CCCCCC', lw=1, ls='--')

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper'
plt.savefig(f'{out_dir}/fig1_framework.pdf', format='pdf')
plt.savefig(f'{out_dir}/fig1_framework.png', format='png')
plt.close()
print("Done. Saved PDF and PNG.")
