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
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

C_BLUE = '#0072B2'
C_ORANGE = '#D55E00'
C_GREEN = '#009E73'
C_RED = '#CC3333'
C_GRAY = '#888888'
C_INPUT = '#E8E8E8'

fig, ax = plt.subplots(figsize=(12, 4.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 3.9)
ax.axis('off')

def draw_box(ax, x, y, w, h, text, color='white', edgecolor='#333333',
             fontsize=9, fontweight='normal', text_color='black', lw=1.2):
    box = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.1',
                         facecolor=color, edgecolor=edgecolor, linewidth=lw, zorder=3)
    ax.add_patch(box)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center',
            fontsize=fontsize, fontweight=fontweight, color=text_color, zorder=4)

def draw_arrow(ax, x1, y1, x2, y2, color='#555555', lw=1.5):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw, shrinkA=2, shrinkB=2),
                zorder=2)

row_y = [2.6, 1.4, 0.2]
labels = ['CLS', 'CWM', 'TRAJ']
label_colors = [C_BLUE, C_ORANGE, C_GREEN]
row_colors = ['#E8F4FD', '#FDE8E0', '#E0F5ED']

for i, (y, label, lc, rc) in enumerate(zip(row_y, labels, label_colors, row_colors)):
    ax.add_patch(FancyBboxPatch((0.05, y - 0.05), 11.9, 0.9,
                                boxstyle='round,pad=0.08', facecolor=rc,
                                edgecolor='none', alpha=0.4, zorder=0))
    ax.text(0.35, y + 0.4, label, ha='center', va='center',
            fontsize=12, fontweight='bold', color=lc, zorder=5,
            fontstyle='italic')

# --- Row 1: CLS ---
y = row_y[0]
draw_box(ax, 0.8, y + 0.1, 1.8, 0.6, '(code, test)', color=C_INPUT, fontsize=9)
draw_arrow(ax, 2.6, y + 0.4, 3.2, y + 0.4)
draw_box(ax, 3.2, y + 0.05, 2.2, 0.7, 'LLM\n(Qwen3-4B/8B)', color='white',
         edgecolor=C_BLUE, fontsize=9, lw=1.5)
draw_arrow(ax, 5.4, y + 0.4, 6.0, y + 0.4)
draw_box(ax, 6.0, y + 0.12, 1.6, 0.55, '1 token', color='#D4EDFF',
         edgecolor=C_BLUE, fontsize=10, fontweight='bold')
draw_arrow(ax, 7.6, y + 0.4, 8.2, y + 0.4)
draw_box(ax, 8.2, y + 0.12, 2.0, 0.55, '"pass" / "fail"', color='#B8E6B8',
         edgecolor='#2E7D32', fontsize=10, fontweight='bold')

# --- Row 2: CWM ---
y = row_y[1]
draw_box(ax, 0.8, y + 0.1, 1.8, 0.6, '(code, test)', color=C_INPUT, fontsize=9)
draw_arrow(ax, 2.6, y + 0.4, 3.2, y + 0.4)
draw_box(ax, 3.2, y + 0.05, 2.2, 0.7, 'LLM\n(Qwen3-4B/8B)', color='white',
         edgecolor=C_ORANGE, fontsize=9, lw=1.5)
draw_arrow(ax, 5.4, y + 0.4, 6.0, y + 0.4)
draw_box(ax, 6.0, y + 0.12, 1.6, 0.55, 'N tokens', color='#FFE0CC',
         edgecolor=C_ORANGE, fontsize=10, fontweight='bold')
draw_arrow(ax, 7.6, y + 0.4, 8.2, y + 0.4)
draw_box(ax, 8.2, y + 0.12, 2.0, 0.55, 'exact match', color='#FFE0CC',
         edgecolor=C_ORANGE, fontsize=9)
draw_arrow(ax, 10.2, y + 0.4, 10.6, y + 0.4)
draw_box(ax, 10.6, y + 0.12, 1.1, 0.55, 'pass/fail', color='#FFE0CC',
         edgecolor=C_ORANGE, fontsize=9)

ax.annotate('token exhaustion', xy=(6.8, y + 0.12), xytext=(5.8, y - 0.25),
            fontsize=7.5, color=C_RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=C_RED, lw=0.8), zorder=5)
ax.annotate('format non-compliance\n(54–74% unparseable)', xy=(9.2, y + 0.12), xytext=(8.5, y - 0.35),
            fontsize=7.5, color=C_RED, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=C_RED, lw=0.8), zorder=5)

# --- Row 3: TRAJ ---
y = row_y[2]
draw_box(ax, 0.8, y + 0.1, 1.8, 0.6, '(code, all tests)', color=C_INPUT, fontsize=9)
draw_arrow(ax, 2.6, y + 0.4, 3.2, y + 0.4)
draw_box(ax, 3.2, y + 0.05, 2.2, 0.7, 'LLM\n(Qwen3-4B)', color='white',
         edgecolor=C_GREEN, fontsize=9, lw=1.5)
draw_arrow(ax, 5.4, y + 0.4, 6.0, y + 0.4)
draw_box(ax, 6.0, y + 0.12, 1.6, 0.55, '1 token', color='#D4F5E0',
         edgecolor=C_GREEN, fontsize=10, fontweight='bold')
draw_arrow(ax, 7.6, y + 0.4, 8.2, y + 0.4)
draw_box(ax, 8.2, y + 0.12, 2.8, 0.55, '"resolved" / "unresolved"', color='#D4F5E0',
         edgecolor=C_GREEN, fontsize=9, fontweight='bold')
ax.text(6.8, y - 0.15, 'no per-test signal', fontsize=7.5, color=C_GRAY,
        ha='center', fontstyle='italic', zorder=5)

# Column headers
ax.text(1.7, 3.65, 'Input', ha='center', fontsize=10, fontweight='bold', color='#444444')
ax.text(4.3, 3.65, 'Model', ha='center', fontsize=10, fontweight='bold', color='#444444')
ax.text(6.8, 3.65, 'Output Length', ha='center', fontsize=10, fontweight='bold', color='#444444')
ax.text(9.2, 3.65, 'Verdict', ha='center', fontsize=10, fontweight='bold', color='#444444')

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts'
plt.savefig(f'{outdir}/fig1_reformulation.pdf', format='pdf')
plt.savefig(f'{outdir}/fig1_reformulation.png', format='png')
plt.close()
print('Done: fig1_reformulation.pdf + .png')
