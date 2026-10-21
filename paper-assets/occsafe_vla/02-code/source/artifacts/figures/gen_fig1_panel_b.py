import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

C_ENCODER = '#E8EEF6'
C_ENCODER_BORDER = '#4C72B0'
C_ACTION = '#EAF5EA'
C_ACTION_BORDER = '#55A868'
C_AUX = '#FFF3E0'
C_AUX_BORDER = '#E69F00'
C_BACKBONE = '#F5F0FA'
C_BACKBONE_BORDER = '#8172B3'
C_LORA = '#64B5CD'
C_HIGHLIGHT_ROW = '#EBF5FB'

fig = plt.figure(figsize=(7.2, 5.8))

gs = fig.add_gridspec(2, 1, height_ratios=[0.40, 0.60], hspace=0.08,
                      left=0.06, right=0.98, top=0.96, bottom=0.02)
ax_arch = fig.add_subplot(gs[0])
ax_table = fig.add_subplot(gs[1])

# ============================================================
# TOP: Architecture schematic
# ============================================================
ax_arch.set_xlim(0, 10.5)
ax_arch.set_ylim(0, 4.5)
ax_arch.axis('off')

def draw_box(ax, xy, w, h, text, facecolor, edgecolor, fontsize=8.5,
             fontweight='normal', text_color='#333333', lw=1.2, rounding=0.15,
             subtext=None, subtext_fontsize=7):
    box = FancyBboxPatch(xy, w, h, boxstyle=f'round,pad={rounding}',
                         facecolor=facecolor, edgecolor=edgecolor,
                         linewidth=lw, zorder=3)
    ax.add_patch(box)
    cx, cy = xy[0] + w/2, xy[1] + h/2
    if subtext:
        cy += 0.18
    ax.text(cx, cy, text, fontsize=fontsize, fontweight=fontweight,
            ha='center', va='center', color=text_color, zorder=4)
    if subtext:
        ax.text(cx, cy - 0.38, subtext, fontsize=subtext_fontsize,
                ha='center', va='center', color='#777777', zorder=4)

def draw_arrow(ax, start, end, lw=1.5, color='#555555', style='->', ls='-'):
    arrow = FancyArrowPatch(start, end, arrowstyle=style,
                            mutation_scale=12, lw=lw, color=color,
                            linestyle=ls, zorder=2)
    ax.add_patch(arrow)

# Backbone background
bb = FancyBboxPatch((0.15, 0.6), 2.7, 3.6, boxstyle='round,pad=0.12',
                    facecolor=C_BACKBONE, edgecolor=C_BACKBONE_BORDER,
                    linewidth=0.8, zorder=1, alpha=0.3, linestyle='--')
ax_arch.add_patch(bb)
ax_arch.text(1.5, 0.42, 'OpenVLA-7B', fontsize=8, ha='center',
             va='center', color=C_BACKBONE_BORDER, fontweight='bold')

# DINOv2
draw_box(ax_arch, (0.4, 2.9), 2.2, 1.15, 'DINOv2', C_ENCODER, C_ENCODER_BORDER,
         fontsize=9.5, fontweight='bold', subtext='(1024d)')
# SigLIP
draw_box(ax_arch, (0.4, 1.0), 2.2, 1.15, 'SigLIP', C_ENCODER, C_ENCODER_BORDER,
         fontsize=9.5, fontweight='bold', subtext='(1152d)')

# LoRA badge
ax_arch.text(2.8, 4.25, 'LoRA r=32', fontsize=7.5, color=C_LORA,
             fontstyle='italic', fontweight='bold', ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                       edgecolor=C_LORA, linewidth=0.8, alpha=0.9))

# Concat
draw_box(ax_arch, (3.6, 1.8), 1.6, 1.0, 'Concat', '#F5F5F5', '#999999',
         fontsize=8.5, subtext='2176d')

# Encoder -> Concat
draw_arrow(ax_arch, (2.6, 3.48), (3.6, 2.5), lw=1.3)
draw_arrow(ax_arch, (2.6, 1.58), (3.6, 2.1), lw=1.3)

# Action Head
draw_box(ax_arch, (6.0, 2.8), 1.9, 1.0, 'Action Head', C_ACTION, C_ACTION_BORDER,
         fontsize=9, fontweight='bold')
# Concat -> Action (thick = main path)
draw_arrow(ax_arch, (5.2, 2.5), (6.0, 3.3), lw=2.2, color=C_ACTION_BORDER)

# Robot Actions
draw_box(ax_arch, (8.6, 2.8), 1.6, 1.0, 'Robot\nActions', '#FFFFFF', C_ACTION_BORDER,
         fontsize=8.5, lw=0.8)
draw_arrow(ax_arch, (7.9, 3.3), (8.6, 3.3), lw=2.0, color=C_ACTION_BORDER)

# Aux Head
draw_box(ax_arch, (6.0, 0.7), 1.9, 1.0, 'Aux Spatial\nHead', C_AUX, C_AUX_BORDER,
         fontsize=8.5, fontweight='bold')
ax_arch.text(6.95, 0.38, '1.2M params', fontsize=7, ha='center',
             color='#999999', fontstyle='italic')
# Concat -> Aux (thin, dashed = auxiliary)
draw_arrow(ax_arch, (5.2, 2.1), (6.0, 1.2), lw=1.0, color=C_AUX_BORDER, ls='--')

# BEV output
draw_box(ax_arch, (8.6, 0.7), 1.6, 1.0, '64x64\nBEV Occ', '#FFFFFF', C_AUX_BORDER,
         fontsize=8, lw=0.8)
draw_arrow(ax_arch, (7.9, 1.2), (8.6, 1.2), lw=1.0, color=C_AUX_BORDER, ls='--')

ax_arch.text(9.4, 0.38, 'discarded at inference', fontsize=7,
             color='#999999', fontstyle='italic', ha='center')

# Subtle divider between architecture and table
ax_arch.plot([0.02, 0.98], [-0.06, -0.06], transform=ax_arch.transAxes,
             color='#DDDDDD', lw=0.6, clip_on=False)

# Legend lines for gradient flow
ax_arch.plot([6.1, 6.6], [4.15, 4.15], color=C_ACTION_BORDER, lw=2.0,
             solid_capstyle='round', zorder=5)
ax_arch.text(6.7, 4.15, 'gradient flow ON', fontsize=7, va='center',
             color=C_ACTION_BORDER)
ax_arch.plot([6.1, 6.6], [3.85, 3.85], color=C_AUX_BORDER, lw=1.0, ls='--', zorder=5)
ax_arch.text(6.7, 3.85, 'gradient flow OFF (detach)', fontsize=7, va='center',
             color=C_AUX_BORDER)

# ============================================================
# BOTTOM: Design matrix table
# ============================================================
ax_table.axis('off')

col_labels = ['Condition', 'Grad\nFlow', 'Label\nContent', 'Norm', 'Ref\nFrame', 'Temporal']
rows_data = [
    ['Vanilla',           '—', '—',    '—', '—', '—'],
    ['Full OCC',          '✓', 'GT occ',    'BN',     'BEV',    'Full'],
    ['Full OCC+LN',       '✓', 'GT occ',    'LN',     'BEV',    'Full'],
    ['Random OCC',        '✓', 'Random',    'BN',     'BEV',    'Full'],
    ['Detach OCC',        '✗', 'GT occ',    'BN',     'BEV',    'Full'],
    ['Detach+LN',         '✗', 'GT occ',    'LN',     'BEV',    'Full'],
    ['Depth',             '✓', 'Depth',     'BN',     'Ego',    'Full'],
    ['Cutoff@15K',        '✓→✗', 'GT occ', 'BN', 'BEV', '15K'],
    ['Cutoff@25K',        '✓→✗', 'GT occ', 'BN', 'BEV', '25K'],
    ['Cutoff@35K',        '✓→✗', 'GT occ', 'BN', 'BEV', '35K'],
    ['Cutoff@45K',        '✓→✗', 'GT occ', 'BN', 'BEV', '45K'],
    ['Reverse Cutoff',    '✗→✓', 'GT occ', 'BN', 'BEV', 'Last 15K'],
]

highlight_rows = {1, 2, 4, 5}

table = ax_table.table(
    cellText=rows_data,
    colLabels=col_labels,
    cellLoc='center',
    loc='center',
    bbox=[0.05, 0.0, 0.93, 1.0]
)

table.auto_set_font_size(False)
table.set_fontsize(7.5)

for (row, col), cell in table.get_celld().items():
    cell.set_edgecolor('#CCCCCC')
    cell.set_linewidth(0.5)

    if row == 0:
        cell.set_facecolor('#4C72B0')
        cell.set_text_props(color='white', fontweight='bold', fontsize=7.5)
        cell.set_height(0.075)
    else:
        cell.set_height(0.062)
        if (row - 1) in highlight_rows:
            cell.set_facecolor(C_HIGHLIGHT_ROW)
        else:
            cell.set_facecolor('white')

        if col == 0:
            cell.set_text_props(fontweight='bold', fontsize=7.5)
            cell.PAD = 0.04

        text = cell.get_text().get_text()
        if text == '✓':
            cell.get_text().set_color('#55A868')
            cell.get_text().set_fontweight('bold')
        elif text == '✗':
            cell.get_text().set_color('#C44E52')
            cell.get_text().set_fontweight('bold')
        elif '→' in text:
            cell.get_text().set_color('#8172B3')
            cell.get_text().set_fontweight('bold')

# 2x2 factorial bracket on right side of table
# Rows 2,3 (Full OCC, Full OCC+LN) and rows 5,6 (Detach OCC, Detach+LN)
# in table coords: row 0=header, row 1=Vanilla, row 2=Full OCC, etc.
# The table bbox is [0.05, 0.0, 0.93, 1.0], header height=0.075, row height=0.062
# Calculate y positions in axes fraction
header_top = 1.0
row_h = 0.062
header_h = 0.075
# Full OCC row center (row index 1 in data = row 2 in table)
y_full_occ_top = header_top - header_h - row_h * 0.5
y_full_occ_ln_bot = header_top - header_h - row_h * 2.5
y_detach_top = header_top - header_h - row_h * 3.5
y_detach_ln_bot = header_top - header_h - row_h * 5.5

# Draw bracket lines on the right
bx = 0.995
bw = 0.008
ax_table.plot([bx, bx+bw], [y_full_occ_top, y_full_occ_top],
              transform=ax_table.transAxes, color='#4C72B0', lw=1.0, clip_on=False)
ax_table.plot([bx+bw, bx+bw], [y_full_occ_top, y_detach_ln_bot],
              transform=ax_table.transAxes, color='#4C72B0', lw=1.0, clip_on=False)
ax_table.plot([bx, bx+bw], [y_detach_ln_bot, y_detach_ln_bot],
              transform=ax_table.transAxes, color='#4C72B0', lw=1.0, clip_on=False)
mid_y = (y_full_occ_top + y_detach_ln_bot) / 2
ax_table.text(bx + 0.02, mid_y, '2×2\nfactorial', transform=ax_table.transAxes,
              fontsize=7, color='#4C72B0', fontstyle='italic', ha='left', va='center',
              fontweight='bold', rotation=0, linespacing=1.2)

# Panel label
ax_arch.text(-0.03, 1.10, '(b)', transform=ax_arch.transAxes,
             fontsize=13, fontweight='bold', va='top')

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/figures/'
fig.savefig(out_dir + 'fig1_panel_b.pdf')
fig.savefig(out_dir + 'fig1_panel_b.png')
plt.close()
print('Panel (b) saved.')
