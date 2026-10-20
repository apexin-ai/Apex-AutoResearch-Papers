import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
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
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

# --- Data ---
vla_trained = [21,24,4,3,3,4,6,4,5,6,5,6,7,6,5,4,3,2,1,2,1,0,2,1,1,0,1,0,1,3,5,18]
pretrained  = [0,9,6,6,7,8,9,10,11,15,16,17,18,19,20,21,22,20,18,16,14,12,10,8,7,6,5,4,3,2,1,0]

C_PRETRAINED = '#0072B2'
C_VLA        = '#D55E00'
C_ARROW      = '#555555'
C_ENTRY      = '#FBDCDB'
C_MID        = '#EEEEEE'
C_LLM_BG     = '#EDF2FA'

fig = plt.figure(figsize=(7.0, 3.6))
gs = fig.add_gridspec(1, 2, width_ratios=[0.6, 1.35], wspace=0.05)

# ============================================================
# Panel (a): Simplified VLA architecture
# ============================================================
ax = fig.add_subplot(gs[0])
ax.set_xlim(-1, 11)
ax.set_ylim(-0.5, 20)
ax.axis('off')

ax.text(-0.5, 19.5, '(a)', fontsize=13, fontweight='bold', va='top')

akw = dict(arrowstyle='->', color=C_ARROW, lw=1.2, mutation_scale=12)
pcx = 4.0

def simple_box(cx, cy, w, h, label, fc, fs=8.5, ec='#999', bold=False):
    r = mpatches.FancyBboxPatch(
        (cx-w/2, cy-h/2), w, h, boxstyle='round,pad=0.12',
        facecolor=fc, edgecolor=ec, linewidth=0.8, zorder=3)
    ax.add_patch(r)
    fw = 'bold' if bold else 'normal'
    ax.text(cx, cy, label, ha='center', va='center', fontsize=fs,
            color='#333', zorder=4, fontweight=fw)

# Instruction bubble
ax.text(8.5, 18.0, '"Pick up the\n  red block"', fontsize=7, ha='center', va='center',
        style='italic', color='#555',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFDE7',
                  edgecolor='#CCCC88', linewidth=0.6))

# Pipeline boxes - generous vertical spacing
y_img  = 18.5
y_ve   = 16.5
y_proj = 14.8

simple_box(pcx, y_img,  2.8, 0.8, 'Image', '#F0F0F0')
simple_box(pcx, y_ve,   4.0, 0.9, 'Vision Encoder', '#DFF0D8', fs=8)
simple_box(pcx, y_proj, 2.8, 0.8, 'Projector', '#E8E8E8')

# Arrows between pipeline stages
ax.annotate('', xy=(pcx, y_ve+0.45), xytext=(pcx, y_img-0.4), arrowprops=akw)
ax.annotate('', xy=(pcx, y_proj+0.4), xytext=(pcx, y_ve-0.45), arrowprops=akw)

# LLM Backbone block
llm_top = 13.0
llm_bot = 3.5
llm_w   = 5.5

llm_rect = mpatches.FancyBboxPatch(
    (pcx - llm_w/2, llm_bot), llm_w, llm_top - llm_bot,
    boxstyle='round,pad=0.18', facecolor=C_LLM_BG,
    edgecolor='#7799BB', linewidth=1.0, zorder=1)
ax.add_patch(llm_rect)
ax.text(pcx, llm_top + 0.35, 'LLM Backbone', fontsize=8.5,
        ha='center', va='bottom', fontweight='bold', color='#446688')

ax.annotate('', xy=(pcx, llm_top), xytext=(pcx, y_proj-0.4), arrowprops=akw)

# Arrow from instruction to LLM top-right
ax.annotate('', xy=(pcx + llm_w/2 - 0.2, llm_top + 0.1),
            xytext=(7.5, 17.0),
            arrowprops=dict(arrowstyle='->', color='#CC8800', lw=1.0, mutation_scale=11,
                            connectionstyle='arc3,rad=0.3'))

# Layer rows inside LLM
layer_data = [
    ('L1',  C_ENTRY, 'Entry'),
    ('L2',  C_ENTRY, 'Entry'),
    ('L3',  C_MID,   None),
    ('...',  None,    None),
    ('L31', C_MID,   None),
    ('L32', C_ENTRY, 'Exit'),
]

n_items = len(layer_data)
layer_w = llm_w - 1.0
layer_h = 0.75
usable = llm_top - llm_bot - 1.2
gap = (usable - n_items * layer_h) / (n_items - 1)

for i, (lbl, fc, tag) in enumerate(layer_data):
    y_top = llm_top - 0.7 - i * (layer_h + gap)
    y_center = y_top - layer_h / 2
    if lbl == '...':
        ax.text(pcx, y_center, '. . .', fontsize=11, ha='center', va='center',
                color='#999', zorder=3)
        continue
    ec = '#CC8888' if tag else '#CCCCCC'
    lw = 1.0 if tag else 0.5
    r = mpatches.FancyBboxPatch(
        (pcx - layer_w/2, y_top - layer_h), layer_w, layer_h,
        boxstyle='round,pad=0.06', facecolor=fc, edgecolor=ec,
        linewidth=lw, zorder=2)
    ax.add_patch(r)
    ax.text(pcx - layer_w/2 + 0.35, y_center, lbl, fontsize=7,
            ha='left', va='center', color='#555', zorder=3)
    if tag:
        ax.text(pcx + layer_w/4 + 0.2, y_center, tag, fontsize=6.5,
                ha='center', va='center', color=C_VLA, fontweight='bold', zorder=3)

# Action Head
y_act = 2.0
simple_box(pcx, y_act, 3.2, 0.9, 'Action Head', '#FFF3E0')
ax.text(pcx, y_act - 0.55, '(7-DoF)', fontsize=6.5, ha='center', va='top', color='#888')
ax.annotate('', xy=(pcx, y_act+0.45), xytext=(pcx, llm_bot), arrowprops=akw)

# ============================================================
# Panel (b): Bar chart - cleaner annotations
# ============================================================
ax_b = fig.add_subplot(gs[1])
ax_b.text(-0.02, 1.07, '(b)', fontsize=13, fontweight='bold', va='top',
          transform=ax_b.transAxes)
ax_b.set_title('Instruction Attention Redistribution', fontsize=11, pad=6)

x = np.arange(32)
bw = 0.36

ax_b.bar(x - bw/2, pretrained, bw, color=C_PRETRAINED, alpha=0.78,
         label='Pretrained (Llama-2)', zorder=2)
ax_b.bar(x + bw/2, vla_trained, bw, color=C_VLA, alpha=0.88,
         label='VLA-trained', zorder=2)

ax_b.axhline(0, color='#BBBBBB', linewidth=1.5, zorder=1)
ax_b.text(16, -1.5, 'Untrained (all 0)', fontsize=7, ha='center', color='#AAAAAA')

ax_b.set_xlabel('Layer')
ax_b.set_ylabel('Instruction-dominant\nheads (out of 32)')
ax_b.set_xlim(-0.8, 31.8)
ax_b.set_ylim(-2.5, 34)

tp = list(range(0, 32, 4)) + [31]
ax_b.set_xticks(tp)
ax_b.set_xticklabels([f'L{i+1}' for i in tp], fontsize=8)
ax_b.set_yticks([0, 8, 16, 24, 32])
ax_b.grid(True, axis='y', alpha=0.2, zorder=0)

# Annotations — spread out, no overlap
t1 = ax_b.annotate('Entry\nlayers', xy=(1, 25), xytext=(5.5, 31),
                    fontsize=8, fontweight='bold', color=C_VLA, ha='center',
                    arrowprops=dict(arrowstyle='->', color=C_VLA, lw=1.2), zorder=5)
t1.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

t3 = ax_b.annotate('Mid-depth\npeak', xy=(17, 22.5), xytext=(13, 31),
                    fontsize=7.5, color=C_PRETRAINED, ha='center',
                    arrowprops=dict(arrowstyle='->', color=C_PRETRAINED, lw=0.9), zorder=5)
t3.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

t2 = ax_b.annotate('Exit\nlayer', xy=(31, 19), xytext=(28.5, 9),
                    fontsize=8, fontweight='bold', color=C_VLA, ha='center',
                    arrowprops=dict(arrowstyle='->', color=C_VLA, lw=1.2), zorder=5)
t2.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

ax_b.legend(loc='upper right', fontsize=8, framealpha=0.92, edgecolor='#CCCCCC')

# ============================================================
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
outpath = os.path.join(_REPO_ROOT, 'docs', 'paper', 'figures', 'fig_teaser.pdf')
plt.savefig(outpath, dpi=300)
plt.savefig(outpath.replace('.pdf', '.png'), dpi=300)
plt.close()
print(f'Saved: {outpath}')
