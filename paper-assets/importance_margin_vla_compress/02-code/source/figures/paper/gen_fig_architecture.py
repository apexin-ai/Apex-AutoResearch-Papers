import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

C_VISION = '#AED6F1'
C_CONNECTOR = '#D5D8DC'
C_LLM = '#A9DFBF'
C_ACTION = '#F9E79F'
C_INPUT = '#E8DAEF'
C_LANG = '#FCF3CF'
C_RED = '#E74C3C'
C_RED_LIGHT = '#FADBD8'
C_EDGE = '#2C3E50'
C_GRAY = '#888888'

fig, ax = plt.subplots(figsize=(13, 3.9))
ax.set_xlim(-0.3, 13.5)
ax.set_ylim(-0.15, 3.9)
ax.set_aspect('equal')
ax.axis('off')


def draw_block(x, y, w, h, label, color, fontsize=9, edgecolor=C_EDGE,
               lw=1.2, linestyle='-', fontweight='normal', text_color='black'):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                         facecolor=color, edgecolor=edgecolor,
                         linewidth=lw, linestyle=linestyle, zorder=2)
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, label, ha='center', va='center',
            fontsize=fontsize, fontweight=fontweight, color=text_color,
            zorder=3, linespacing=1.3)


def arrow(x1, y1, x2, y2, label='', color=C_EDGE, lw=1.2, fontsize=7.5,
          dy_label=0.13, style='->', mutation=12):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, color=color,
                        linewidth=lw, mutation_scale=mutation, zorder=1)
    ax.add_patch(a)
    if label:
        ax.text((x1 + x2) / 2, (y1 + y2) / 2 + dy_label, label,
                ha='center', va='bottom', fontsize=fontsize, color='#555555')


# ================================================================
#  Row geometry
# ================================================================
row_y = 1.05          # bottom of main row blocks
bh = 1.1              # block height
mid_y = row_y + bh / 2  # vertical center of flow

# ---- 1. Inputs ----
cam_w, cam_h = 1.0, 0.42
cam_gap = 0.08
cam1_y = row_y + bh - cam_h
cam2_y = row_y
draw_block(0, cam1_y, cam_w, cam_h, 'Camera 1', C_INPUT, fontsize=8.5)
draw_block(0, cam2_y, cam_w, cam_h, 'Camera 2', C_INPUT, fontsize=8.5)

lang_y = row_y - 0.6
draw_block(0, lang_y, cam_w, 0.42, 'Language\nInstruction', C_LANG, fontsize=7.5)

# ---- 2. SigLIP ----
sig_x, sig_w = 1.55, 1.7
draw_block(sig_x, row_y, sig_w, bh,
           'SigLIP\nVision Encoder\n\n$2{\\times}64$ patches\n= 128 tokens',
           C_VISION, fontsize=9)
arrow(cam_w, mid_y, sig_x, mid_y)

# ---- 3. MLP Connector ----
mlp_x, mlp_w = 3.85, 1.2
draw_block(mlp_x, row_y + 0.05, mlp_w, bh - 0.1,
           'MLP\nConnector\n\ndim $\\to$ LLM', C_CONNECTOR, fontsize=9)
arrow(sig_x + sig_w, mid_y, mlp_x, mid_y, '128', fontsize=7)

# ---- 4. Intervention zone (red dashed) ----
int_x = 5.65
int_w = 2.05
int_h = bh + 0.7
int_y = row_y - 0.25

int_box = FancyBboxPatch((int_x, int_y), int_w, int_h,
                          boxstyle="round,pad=0.08",
                          facecolor=C_RED_LIGHT, edgecolor=C_RED,
                          linewidth=2.0, linestyle=(0, (5, 3)),
                          zorder=2, alpha=0.65)
ax.add_patch(int_box)

# Title + scissors on one line
ax.text(int_x + int_w / 2, int_y + int_h - 0.22,
        '✂  Token Reduction',
        ha='center', va='top', fontsize=9.5, fontweight='bold', color=C_RED, zorder=3)

# Three mechanisms as single-line labels
mech_labels = [
    'Zero-mask (set to 0, OOD)',
    'True removal (drop tokens)',
    'Merge (weighted combine)',
]
mech_w = 1.75
mech_h = 0.26
mech_x = int_x + (int_w - mech_w) / 2
for i, lbl in enumerate(mech_labels):
    my = int_y + int_h - 0.58 - i * (mech_h + 0.06)
    box = FancyBboxPatch((mech_x, my), mech_w, mech_h,
                          boxstyle="round,pad=0.04",
                          facecolor='white', edgecolor=C_RED,
                          linewidth=0.7, zorder=3, alpha=0.95)
    ax.add_patch(box)
    ax.text(mech_x + mech_w / 2, my + mech_h / 2, lbl,
            ha='center', va='center', fontsize=7,
            color=C_RED, zorder=4)

# Arrows in/out of intervention
arrow(mlp_x + mlp_w, mid_y, int_x, mid_y, '128', fontsize=7)
arrow(int_x + int_w, mid_y, 8.5, mid_y, '$k \\leq 128$', fontsize=7.5,
      color=C_RED, lw=1.5, dy_label=0.16)

# ---- 5. Qwen2 LLM ----
llm_x, llm_w = 8.5, 1.5
draw_block(llm_x, row_y, llm_w, bh,
           'Qwen2 1.5B\nLLM\n\nvision + lang\ntokens', C_LLM, fontsize=9)

# Language path: horizontal line under pipeline, then up into LLM
lang_path_y = lang_y + 0.21
ax.plot([cam_w, llm_x + 0.1], [lang_path_y, lang_path_y],
        color=C_GRAY, lw=0.9, zorder=0)
ax.annotate('', xy=(llm_x + 0.1, row_y), xytext=(llm_x + 0.1, lang_path_y),
            arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=0.9), zorder=0)
ax.text((cam_w + llm_x) / 2, lang_path_y - 0.12, 'language tokens',
        ha='center', va='top', fontsize=7, color=C_GRAY, style='italic')

# ---- 6. Flow Matching Action Head ----
act_x, act_w = 10.6, 1.5
draw_block(act_x, row_y + 0.05, act_w, bh - 0.1,
           'Flow Matching\nAction Head\n\n7-DoF output', C_ACTION, fontsize=9)
arrow(llm_x + llm_w, mid_y, act_x, mid_y)

# ---- Output label ----
arrow(act_x + act_w, mid_y, act_x + act_w + 0.5, mid_y)
ax.text(act_x + act_w + 0.55, mid_y,
        'Action\n$(x, y, z, r, p, y, g)$',
        ha='left', va='center', fontsize=8, color=C_EDGE)

# ================================================================
#  SigLIP spatial patch inset (top-left)
# ================================================================
inset_x, inset_y = 0.0, 2.7
inset_s = 0.72
n = 8
cell = inset_s / n
for i in range(n):
    for j in range(n):
        c = C_VISION if (i + j) % 2 == 0 else '#D6EAF8'
        ax.add_patch(plt.Rectangle((inset_x + j * cell, inset_y + i * cell),
                                    cell, cell, facecolor=c,
                                    edgecolor='white', linewidth=0.35, zorder=5))

ax.add_patch(plt.Rectangle((inset_x, inset_y), inset_s, inset_s,
                             facecolor='none', edgecolor=C_GRAY, linewidth=0.8, zorder=5))
ax.text(inset_x + inset_s / 2, inset_y + inset_s + 0.06,
        'SigLIP spatial patches\n(non-overlapping)',
        ha='center', va='bottom', fontsize=7, color='#555555', zorder=5, linespacing=1.2)

ax.annotate('', xy=(sig_x + 0.3, row_y + bh),
            xytext=(inset_x + inset_s * 0.7, inset_y),
            arrowprops=dict(arrowstyle='->', color=C_GRAY, lw=0.5,
                            connectionstyle='arc3,rad=-0.15'), zorder=0)

# ================================================================
plt.tight_layout()
out = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/figures/paper'
fig.savefig(f'{out}/fig_architecture.pdf', format='pdf')
fig.savefig(f'{out}/fig_architecture.png', format='png')
plt.close()
print('Done')
