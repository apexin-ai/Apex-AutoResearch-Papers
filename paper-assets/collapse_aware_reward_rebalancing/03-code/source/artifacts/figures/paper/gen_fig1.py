import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
})

C_BLUE = '#0072B2'
C_BLUE_L = '#D4E8F7'
C_ORANGE = '#E69F00'
C_ORANGE_L = '#FFF3D4'
C_DARK = '#333333'
C_GRAY = '#999999'
C_LGRAY = '#F2F2F2'
C_RED = '#CC0000'

fig, ax = plt.subplots(figsize=(3.25, 4.1))
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(3.2, 14.5)
ax.axis('off')

CX = 5.0  # center x


def rbox(ax, x, y, w, h, text, fc='white', ec=C_DARK, fs=7.5, fw='normal',
         tc=C_DARK, lw=1.0):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                         facecolor=fc, edgecolor=ec, linewidth=lw, zorder=2)
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center',
            fontsize=fs, fontweight=fw, color=tc, zorder=3)


def arr(x1, y1, x2, y2, color=C_DARK, lw=1.0):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                shrinkA=1, shrinkB=1))


# ═══ Title ═══
ax.text(CX, 14.15, 'Iterative Reward-Curated Training', ha='center',
        va='center', fontsize=9, fontweight='bold', color=C_DARK)

# ═══ Step 1: Model ═══
mw, mh = 4.2, 0.7
mx = CX - mw / 2
my = 13.0
rbox(ax, mx, my, mw, mh, r'Policy  $\pi_{\theta_t}$',
     fc='#E8F4FD', ec=C_BLUE, fs=9, fw='bold', tc=C_BLUE)
arr(CX, my, CX, my - 0.45)

# ═══ Step 2: Generate ═══
gw, gh = 5.8, 0.6
gx = CX - gw / 2
gy = 11.8
rbox(ax, gx, gy, gw, gh, 'Generate K responses / prompt',
     fc=C_LGRAY, ec='#BBBBBB', fs=7.5)
arr(CX, gy, CX, gy - 0.45)

# ═══ Step 3: Score ═══
sw, sh = 5.6, 0.6
sx = CX - sw / 2
sy = 10.55
rbox(ax, sx, sy, sw, sh, 'Reward scoring (ArmoRM)',
     fc=C_LGRAY, ec='#BBBBBB', fs=7.5)

# ═══ Diverging arrows ═══
left_cx = 2.7
right_cx = 7.3
arr(CX - 1.2, sy, left_cx, sy - 0.55, color=C_BLUE, lw=1.0)
arr(CX + 1.2, sy, right_cx, sy - 0.55, color=C_ORANGE, lw=1.0)

# ═══ Branch labels ═══
ax.text(left_cx, 9.7, 'Curated', ha='center', va='center',
        fontsize=7.5, fontweight='bold', color=C_BLUE)
ax.text(right_cx, 9.7, 'Random', ha='center', va='center',
        fontsize=7.5, fontweight='bold', color='#B87E00')

# ═══ Mini bar chart helper ═══
scores = np.array([0.93, 0.80, 0.72, 0.63, 0.55, 0.46, 0.35, 0.20])
K = len(scores)


scores_sorted = np.array([0.93, 0.80, 0.72, 0.63, 0.55, 0.46, 0.35, 0.20])
scores_shuffled = np.array([0.55, 0.35, 0.80, 0.20, 0.63, 0.93, 0.46, 0.72])


def draw_bars(ax, cx, y0, chart_w, chart_h, highlight_idx, hi_color, hi_ec,
              label_text, bar_scores, label_offset_x=0.5, label_offset_y=0.35):
    x0 = cx - chart_w / 2
    bar_w = chart_w / (K * 1.35)
    gap = bar_w * 0.35
    ax.add_patch(FancyBboxPatch((x0 - 0.1, y0 - 0.05), chart_w + 0.2, chart_h + 0.1,
                 boxstyle="round,pad=0.06", fc='white', ec='#DDDDDD', lw=0.5, zorder=1))
    for i, s in enumerate(bar_scores):
        bx = x0 + i * (bar_w + gap)
        bh = s * (chart_h - 0.1)
        fc = hi_color if i == highlight_idx else '#D0D0D0'
        ec = hi_ec if i == highlight_idx else '#B0B0B0'
        ax.add_patch(plt.Rectangle((bx, y0 + 0.03), bar_w, bh,
                     fc=fc, ec=ec, lw=0.4, zorder=2))
    hx = x0 + highlight_idx * (bar_w + gap) + bar_w / 2
    hy = y0 + 0.03 + bar_scores[highlight_idx] * (chart_h - 0.1)
    ax.annotate(label_text, xy=(hx, hy),
                xytext=(hx + label_offset_x, hy + label_offset_y),
                ha='center', va='bottom', fontsize=5.5, color=hi_ec,
                fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=hi_color, lw=0.7))


# ═══ Curated bars ═══
chart_h = 1.2
chart_w = 3.4
chart_y = 7.9
draw_bars(ax, left_cx, chart_y, chart_w, chart_h,
          highlight_idx=0, hi_color=C_BLUE, hi_ec='#005A8C',
          label_text='top-1', bar_scores=scores_sorted,
          label_offset_x=0.7, label_offset_y=0.15)

# ═══ Random bars (unsorted to show no ranking) ═══
draw_bars(ax, right_cx, chart_y, chart_w, chart_h,
          highlight_idx=4, hi_color=C_ORANGE, hi_ec='#B87E00',
          label_text='random', bar_scores=scores_shuffled,
          label_offset_x=0.55, label_offset_y=0.4)

# ═══ Selection pressure annotation (between the two bar charts) ═══
sp_x = CX
ax.annotate('', xy=(sp_x, chart_y + 0.2), xytext=(sp_x, chart_y + chart_h - 0.1),
            arrowprops=dict(arrowstyle='->', color=C_RED, lw=0.9,
                            linestyle='--'))
ax.text(sp_x, chart_y + chart_h / 2, 'selection\npressure',
        ha='center', va='center', fontsize=5, color=C_RED, fontweight='bold',
        bbox=dict(fc='white', ec='none', pad=1.0, alpha=0.85))

# ═══ Arrows to training ═══
arr(left_cx, chart_y, left_cx, chart_y - 0.5, color=C_BLUE)
arr(right_cx, chart_y, right_cx, chart_y - 0.5, color=C_ORANGE)

# ═══ Step 4: SFT Training ═══
tw, th = 3.4, 0.6
rbox(ax, left_cx - tw / 2, 6.6, tw, th,
     r'SFT $\rightarrow \pi_{\theta_{t+1}}$',
     fc=C_BLUE_L, ec=C_BLUE, fs=8, fw='bold', tc=C_BLUE)
rbox(ax, right_cx - tw / 2, 6.6, tw, th,
     r'SFT $\rightarrow \pi_{\theta_{t+1}}$',
     fc=C_ORANGE_L, ec=C_ORANGE, fs=8, fw='bold', tc='#B87E00')

# ═══ Arrows to evaluation ═══
arr(left_cx, 6.6, left_cx, 6.1, color=C_BLUE)
arr(right_cx, 6.6, right_cx, 6.1, color=C_ORANGE)

# ═══ Step 5: Evaluate ═══
ew = 8.6
rbox(ax, CX - ew / 2, 5.3, ew, 0.65,
     'Evaluate: Vendi Score, Self-BLEU, format metrics',
     fc='#F0E8F8', ec='#7B2D8E', fs=6.8, tc='#5A1D6B')

# ═══ Loop arrow ═══
loop = FancyArrowPatch(
    (CX - ew / 2, 5.6), (mx, 13.35),
    connectionstyle="arc3,rad=0.55",
    arrowstyle='->', mutation_scale=10,
    color=C_DARK, lw=1.2, linestyle=(0, (3, 2.5)), zorder=0)
ax.add_patch(loop)

ax.text(-0.2, 10.0, r'Repeat $T\!=\!3$',
        ha='center', va='center', fontsize=6, color=C_DARK,
        fontweight='bold', rotation=90,
        bbox=dict(fc='white', ec='none', pad=1.5, alpha=0.9))

# ═══ Research question ═══
ax.text(CX, 4.55, 'Does reward curation cause diversity collapse?',
        ha='center', va='center', fontsize=6.5, color=C_RED,
        fontweight='bold', style='italic')

# ═══ Legend (inline, compact) ═══
ly = 3.7
ax.add_patch(plt.Rectangle((1.5, ly), 0.35, 0.2,
             fc=C_BLUE_L, ec=C_BLUE, lw=0.7))
ax.text(2.0, ly + 0.1, 'Curated (top-1)', ha='left', va='center',
        fontsize=5.5, color=C_BLUE)
ax.add_patch(plt.Rectangle((5.8, ly), 0.35, 0.2,
             fc=C_ORANGE_L, ec=C_ORANGE, lw=0.7))
ax.text(6.3, ly + 0.1, 'Random (1-of-K)', ha='left', va='center',
        fontsize=5.5, color='#B87E00')

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/artifacts/figures/paper'
plt.savefig(f'{outdir}/fig1_pipeline.pdf')
plt.savefig(f'{outdir}/fig1_pipeline.png')
plt.close()
print('Done: fig1_pipeline.pdf + .png')
