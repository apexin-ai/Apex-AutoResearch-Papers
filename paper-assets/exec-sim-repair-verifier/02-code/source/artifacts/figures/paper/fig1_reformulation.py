import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'STIXGeneral', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

CLS_COLOR = '#0072B2'
CWM_COLOR = '#D55E00'
TRAJ_COLOR = '#009E73'

fig, ax = plt.subplots(1, 1, figsize=(14, 5.5))
ax.set_xlim(0, 14)
ax.set_ylim(0, 5.5)
ax.axis('off')

def rounded_box(ax, xy, width, height, text, facecolor='#F0F4F8', edgecolor='#4A5568',
                fontsize=10, fontweight='normal', text_color='#1A202C', linewidth=1.2,
                alpha=1.0, zorder=2):
    x, y = xy
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.15",
                         facecolor=facecolor, edgecolor=edgecolor,
                         linewidth=linewidth, alpha=alpha, zorder=zorder)
    ax.add_patch(box)
    lines = text.split('\n')
    if len(lines) == 1:
        ax.text(x + width/2, y + height/2, text,
                ha='center', va='center', fontsize=fontsize,
                fontweight=fontweight, color=text_color, zorder=zorder+1)
    else:
        total_h = len(lines) * fontsize * 0.018
        for i, line in enumerate(lines):
            ly = y + height/2 + total_h/2 - i * fontsize * 0.018 - fontsize*0.009
            fw = fontweight
            if i == 0:
                fw = 'bold'
            ax.text(x + width/2, ly, line,
                    ha='center', va='center', fontsize=fontsize,
                    fontweight=fw, color=text_color, zorder=zorder+1)

def arrow(ax, start, end, color='#4A5568', lw=1.5):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                connectionstyle='arc3,rad=0'))

# Row positions
row_y = [3.8, 2.0, 0.2]
row_labels = ['CLS', 'CWM', 'TRAJ']
row_colors = [CLS_COLOR, CWM_COLOR, TRAJ_COLOR]
row_bg = ['#E8F0FE', '#FDE8D8', '#D4EDDA']
row_label_x = 0.15

# Column positions
input_x = 1.8
input_w = 3.0
model_x = 5.6
model_w = 1.6
output_x = 8.0
output_w = 2.2
result_x = 11.0
result_w = 2.2

box_h = 1.2

for i, (ry, label, color, bg) in enumerate(zip(row_y, row_labels, row_colors, row_bg)):
    # Row label
    ax.text(row_label_x, ry + box_h/2, label,
            ha='center', va='center', fontsize=14, fontweight='bold',
            color=color, zorder=5,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=bg, edgecolor=color, linewidth=2))

    # Input box
    if i == 2:
        input_text = "Code Diff\n+ All Tests"
    else:
        input_text = "Code Diff\n+ Single Test"
    rounded_box(ax, (input_x, ry), input_w, box_h, input_text,
                facecolor='#F7FAFC', edgecolor='#A0AEC0', fontsize=10)

    # Model box
    rounded_box(ax, (model_x, ry), model_w, box_h, "Model",
                facecolor=bg, edgecolor=color, fontsize=11, fontweight='bold',
                linewidth=2)

    # Arrow: input -> model
    arrow(ax, (input_x + input_w + 0.05, ry + box_h/2),
          (model_x - 0.05, ry + box_h/2), color='#4A5568')

    # Output box and result
    if i == 0:  # CLS
        rounded_box(ax, (output_x, ry), output_w, box_h,
                    "1 Token\nPASS / FAIL",
                    facecolor='#E8F0FE', edgecolor=CLS_COLOR, fontsize=10, linewidth=1.5)
        arrow(ax, (model_x + model_w + 0.05, ry + box_h/2),
              (output_x - 0.05, ry + box_h/2), color='#4A5568')
        # Result annotation
        rounded_box(ax, (result_x, ry), result_w, box_h,
                    "Always\nparseable",
                    facecolor='#C6F6D5', edgecolor='#38A169', fontsize=9.5, linewidth=1.2)
        arrow(ax, (output_x + output_w + 0.05, ry + box_h/2),
              (result_x - 0.05, ry + box_h/2), color='#4A5568')

    elif i == 1:  # CWM
        rounded_box(ax, (output_x, ry), output_w, box_h,
                    "N Tokens\n(exec output)",
                    facecolor='#FDE8D8', edgecolor=CWM_COLOR, fontsize=10, linewidth=1.5)
        arrow(ax, (model_x + model_w + 0.05, ry + box_h/2),
              (output_x - 0.05, ry + box_h/2), color='#4A5568')
        # Exact match + failure modes
        rounded_box(ax, (result_x, ry + 0.05), result_w, box_h - 0.1,
                    "Exact Match\n→ PASS/FAIL",
                    facecolor='#FEFCBF', edgecolor='#D69E2E', fontsize=9.5, linewidth=1.2)
        arrow(ax, (output_x + output_w + 0.05, ry + box_h/2),
              (result_x - 0.05, ry + box_h/2), color='#4A5568')
        # Failure modes annotation below
        ax.text(result_x + result_w/2, ry - 0.25,
                "Token-budget exhaustion,\nstring-value errors,\nformat compliance collapse",
                ha='center', va='top', fontsize=8, color='#C53030',
                style='italic', zorder=5)

    elif i == 2:  # TRAJ
        rounded_box(ax, (output_x, ry), output_w, box_h,
                    "1 Token\nResolved /\nUnresolved",
                    facecolor='#D4EDDA', edgecolor=TRAJ_COLOR, fontsize=10, linewidth=1.5)
        arrow(ax, (model_x + model_w + 0.05, ry + box_h/2),
              (output_x - 0.05, ry + box_h/2), color='#4A5568')
        rounded_box(ax, (result_x, ry), result_w, box_h,
                    "No per-test\nsignal",
                    facecolor='#FED7D7', edgecolor='#E53E3E', fontsize=9.5, linewidth=1.2)
        arrow(ax, (output_x + output_w + 0.05, ry + box_h/2),
              (result_x - 0.05, ry + box_h/2), color='#4A5568')

# Title
ax.text(7, 5.35, "Three Verification Formulations",
        ha='center', va='center', fontsize=14, fontweight='bold', color='#1A202C')

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts'
fig.savefig(f'{out_dir}/fig1_reformulation.pdf')
fig.savefig(f'{out_dir}/fig1_reformulation.png')
plt.close()
print("fig1 done")
