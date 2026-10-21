import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.path as mpath
import numpy as np

OI_BLUE    = '#0072B2'
OI_ORANGE  = '#E69F00'
OI_GREEN   = '#009E73'
OI_GRAY    = '#999999'
OI_SKYBLUE = '#56B4E9'
OI_VERMIL  = '#D55E00'
OI_BLACK   = '#000000'

COLOR_FROZEN_FILL  = '#D6EAF8'
COLOR_FROZEN_EDGE  = OI_BLUE
COLOR_ACR_FILL_1   = '#FDEBD0'
COLOR_ACR_EDGE_1   = OI_ORANGE
COLOR_ACR_FILL_2   = '#D5F5E3'
COLOR_ACR_EDGE_2   = OI_GREEN
COLOR_OUTPUT_FILL  = '#F9E79F'
COLOR_OUTPUT_EDGE  = OI_VERMIL
COLOR_INPUT_FILL   = '#E8E8E8'
COLOR_INPUT_EDGE   = OI_GRAY

fig, ax = plt.subplots(figsize=(7, 2.8))
ax.set_xlim(-0.2, 7.4)
ax.set_ylim(-0.7, 2.6)
ax.set_aspect('equal')
ax.axis('off')

def draw_box(ax, xy, w, h, label, sublabel, fill, edge, fontsize=9, sublabel_fontsize=7.5, bold=True):
    box = FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.06", linewidth=1.5,
                         edgecolor=edge, facecolor=fill, zorder=2)
    ax.add_patch(box)
    cx, cy = xy[0] + w/2, xy[1] + h/2
    weight = 'bold' if bold else 'normal'
    if sublabel:
        ax.text(cx, cy + 0.12, label, ha='center', va='center', fontsize=fontsize,
                fontweight=weight, zorder=3)
        ax.text(cx, cy - 0.14, sublabel, ha='center', va='center', fontsize=sublabel_fontsize,
                color='#444444', zorder=3, style='italic')
    else:
        ax.text(cx, cy, label, ha='center', va='center', fontsize=fontsize,
                fontweight=weight, zorder=3)
    return box

def arrow(ax, start, end, color=OI_BLACK, lw=1.2):
    a = FancyArrowPatch(start, end, arrowstyle='->', color=color,
                        linewidth=lw, mutation_scale=12, zorder=4)
    ax.add_patch(a)
    return a

box_h = 0.65
y_main = 0.8
gap = 0.15

# Stage 1: Observation
x0 = 0.0
w0 = 0.95
draw_box(ax, (x0, y_main), w0, box_h, 'Observation', '$o_t$',
         COLOR_INPUT_FILL, COLOR_INPUT_EDGE)
ax.text(x0 + w0/2, y_main - 0.2, 'image + instruction', ha='center', va='center',
        fontsize=6.5, color='#666666')

# Stage 2: Frozen VLA
x1 = x0 + w0 + gap + 0.1
w1 = 1.15
draw_box(ax, (x1, y_main), w1, box_h, 'Frozen VLA', '$\\pi_\\theta$',
         COLOR_FROZEN_FILL, COLOR_FROZEN_EDGE)

ax.text(x1 + 0.12, y_main + box_h - 0.08, '❄', ha='center', va='center',
        fontsize=8, zorder=5, color=OI_BLUE)
ax.text(x1 + w1 - 0.08, y_main + box_h - 0.06, 'FROZEN', ha='right', va='center',
        fontsize=5.5, zorder=5, color=OI_BLUE, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.08', facecolor='white', edgecolor=OI_BLUE, linewidth=0.6, alpha=0.9))

arrow(ax, (x0 + w0, y_main + box_h/2), (x1, y_main + box_h/2))

# K=10 samples fan
x_fan_start = x1 + w1
x_fan_end = x_fan_start + 0.55
fan_angles = np.linspace(-0.22, 0.22, 7)
for angle in fan_angles:
    arrow(ax, (x_fan_start, y_main + box_h/2),
          (x_fan_end, y_main + box_h/2 + angle * 1.8),
          color=OI_SKYBLUE, lw=0.7)

ax.text(x_fan_start + 0.28, y_main + box_h + 0.42, '$K$=10\nsamples',
        ha='center', va='center', fontsize=6.5, color=OI_BLUE,
        bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='none', alpha=0.8))

# Stage 3: Argmin Selection (was "Conformal Selection")
x2 = x_fan_end + 0.05
w2 = 1.25
draw_box(ax, (x2, y_main), w2, box_h, 'Argmin', 'Selection',
         COLOR_ACR_FILL_1, COLOR_ACR_EDGE_1)
ax.text(x2 + w2/2, y_main - 0.2, 'argmin L2 to mean', ha='center', va='center',
        fontsize=6.5, color=OI_ORANGE, fontweight='bold')

# Arrow: Selection -> CRM (a_base label)
x3 = x2 + w2 + gap + 0.1
arrow(ax, (x2 + w2, y_main + box_h/2), (x3, y_main + box_h/2))
ax.text((x2 + w2 + x3)/2, y_main + box_h/2 + 0.16, '$a_{\\mathrm{base}}$',
        ha='center', va='center', fontsize=7.5, color=OI_BLACK)

# Stage 4: CRM
w3 = 1.2
draw_box(ax, (x3, y_main), w3, box_h, 'CRM', '$\\|\\delta\\|_2 \\leq \\varepsilon$',
         COLOR_ACR_FILL_2, COLOR_ACR_EDGE_2)
ax.text(x3 + w3/2, y_main - 0.2, '~327K params, <1ms', ha='center', va='center',
        fontsize=6.5, color=OI_GREEN, fontweight='bold')

# Stage 5: Corrected Action
x4 = x3 + w3 + gap + 0.1
w4 = 0.95
draw_box(ax, (x4, y_main), w4, box_h, '$a^*$', '$a_{\\mathrm{base}} + \\mathrm{clip}(\\delta)$',
         COLOR_OUTPUT_FILL, COLOR_OUTPUT_EDGE, sublabel_fontsize=7)

arrow(ax, (x3 + w3, y_main + box_h/2), (x4, y_main + box_h/2))

ax.annotate('', xy=(x4 + w4 + 0.18, y_main + box_h/2),
            xytext=(x4 + w4, y_main + box_h/2),
            arrowprops=dict(arrowstyle='->', color=OI_BLACK, lw=1.2))
ax.text(x4 + w4 + 0.21, y_main + box_h/2, '→ robot', ha='left', va='center',
        fontsize=7, color='#555555')

# Dashed arrow: z_obs + a_base from VLA bottom to CRM bottom
vla_cx = x1 + w1/2
crm_cx = x3 + w3/2
y_bot = y_main - 0.5

verts = [
    (vla_cx, y_main),
    (vla_cx, y_bot),
    (crm_cx, y_bot),
    (crm_cx, y_main),
]
codes = [mpath.Path.MOVETO, mpath.Path.LINETO, mpath.Path.LINETO, mpath.Path.LINETO]
path = mpath.Path(verts, codes)

arrow_patch = FancyArrowPatch(path=path, arrowstyle='->', color=OI_BLUE,
                               linewidth=1.0, linestyle='dashed',
                               mutation_scale=10, zorder=1)
ax.add_patch(arrow_patch)

ax.text((vla_cx + crm_cx)/2, y_bot - 0.15,
        '$z_{\\mathrm{obs}}$ (960D) + $a_{\\mathrm{base}}$ (30D) = 990D input',
        ha='center', va='center', fontsize=6.5, color=OI_BLUE,
        bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor=OI_BLUE,
                  linewidth=0.5, alpha=0.9))

# Legend
frozen_patch = mpatches.Patch(facecolor=COLOR_FROZEN_FILL, edgecolor=COLOR_FROZEN_EDGE,
                               linewidth=1.2, label='Frozen VLA')
acr1_patch = mpatches.Patch(facecolor=COLOR_ACR_FILL_1, edgecolor=COLOR_ACR_EDGE_1,
                             linewidth=1.2, label='ACR-VLA (selection)')
acr2_patch = mpatches.Patch(facecolor=COLOR_ACR_FILL_2, edgecolor=COLOR_ACR_EDGE_2,
                             linewidth=1.2, label='ACR-VLA (correction)')
ax.legend(handles=[frozen_patch, acr1_patch, acr2_patch],
          loc='upper center', ncol=3, fontsize=7, framealpha=0.9,
          edgecolor='#CCCCCC', bbox_to_anchor=(0.5, 1.08),
          handlelength=1.2, handletextpad=0.4, columnspacing=1.0)

plt.tight_layout(pad=0.2)

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/figures/paper'
pdf_out = f'{out_dir}/fig1_pipeline.pdf'
png_out = f'{out_dir}/fig1_pipeline.png'

fig.savefig(pdf_out, format='pdf', dpi=300, bbox_inches='tight', pad_inches=0.05)
print(f"Saved PDF: {pdf_out}")
fig.savefig(png_out, format='png', dpi=300, bbox_inches='tight', pad_inches=0.05)
print(f"Saved PNG: {png_out}")
