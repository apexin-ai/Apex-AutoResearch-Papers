import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches

mpl.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'Times New Roman', 'DejaVu Serif'],
    'mathtext.fontset': 'cm',
    'pdf.fonttype': 42,
    'axes.linewidth': 0.6,
    'font.size': 7.5,
})

fig = plt.figure(figsize=(7.0, 2.6))
gs = fig.add_gridspec(1, 3, width_ratios=[0.30, 0.38, 0.32],
                       left=0.02, right=0.98, bottom=0.05, top=0.88,
                       wspace=0.08)

navy = '#2C3E50'
teal = '#1ABC9C'
coral = '#E74C3C'
amber = '#F39C12'
light_blue = '#85C1E9'
gray = '#7F8C8D'
canary_yellow = '#F4D03F'

def rounded_box(ax, xy, w, h, text, fc='#F8F9FA', ec='#5D6D7E', lw=0.8, fontsize=6.5, fontweight='normal', text_color='#2C3E50'):
    box = FancyBboxPatch(xy, w, h, boxstyle='round,pad=0.02',
                         facecolor=fc, edgecolor=ec, linewidth=lw, zorder=5,
                         transform=ax.transData)
    ax.add_patch(box)
    ax.text(xy[0]+w/2, xy[1]+h/2, text, ha='center', va='center',
            fontsize=fontsize, fontweight=fontweight, color=text_color, zorder=6)

def arrow(ax, start, end, color='#7F8C8D', lw=0.8, style='->', connectionstyle='arc3,rad=0'):
    arr = FancyArrowPatch(start, end, arrowstyle=style, color=color,
                          linewidth=lw, connectionstyle=connectionstyle,
                          mutation_scale=8, zorder=4)
    ax.add_patch(arr)

# ---- Panel (a): Iterative Contamination Loop ----
ax_a = fig.add_subplot(gs[0])
ax_a.set_xlim(-0.1, 1.1)
ax_a.set_ylim(-0.15, 1.15)
ax_a.axis('off')
ax_a.text(0.0, 1.12, '(a)', fontsize=9, fontweight='bold', transform=ax_a.transAxes)
ax_a.text(0.5, 1.12, 'Iterative Contamination', fontsize=7.5, fontstyle='italic',
          ha='center', transform=ax_a.transAxes, color=gray)

bw, bh = 0.32, 0.13
rounded_box(ax_a, (0.34, 0.88), bw, bh, 'Real Data', fc='#EBF5FB', ec=navy)
rounded_box(ax_a, (0.60, 0.58), bw, bh, r'Train $M_t$', fc='#F8F9FA', ec='#5D6D7E')
rounded_box(ax_a, (0.34, 0.28), bw, bh, 'Generate', fc='#F8F9FA', ec='#5D6D7E')
rounded_box(ax_a, (0.04, 0.58), bw, bh, r'Mix ($\alpha$)', fc='#FEF9E7', ec='#D4AC0D')

arrow(ax_a, (0.50, 0.88), (0.76, 0.71), color=gray)
arrow(ax_a, (0.76, 0.58), (0.66, 0.41), color=gray)
arrow(ax_a, (0.50, 0.28), (0.20, 0.41), color=gray, style='->')
ax_a.text(0.35, 0.22, 'Synthetic\ndata', fontsize=5.5, color=gray, ha='center', va='top')
arrow(ax_a, (0.20, 0.71), (0.50, 0.88), color=gray)

ax_a.text(0.50, 0.55, r'$T$ generations', fontsize=5.5, ha='center',
          color=gray, fontstyle='italic')

mb_y = 0.05
rounded_box(ax_a, (0.05, mb_y), 0.38, 0.10, '', fc='#FEFEFE', ec='#DEE2E6', lw=0.5)
ax_a.add_patch(mpatches.Rectangle((0.05, mb_y), 0.03, 0.10, fc=canary_yellow, ec='none', zorder=6))
ax_a.text(0.10, mb_y+0.05, r'$H(X)$ entropy', fontsize=5.5, va='center', color=navy, zorder=7)
ax_a.text(0.38, mb_y+0.05, 'canary', fontsize=5, va='center', color=amber, fontstyle='italic', zorder=7)

rounded_box(ax_a, (0.55, mb_y), 0.42, 0.10, '', fc='#FEFEFE', ec='#DEE2E6', lw=0.5)
ax_a.add_patch(mpatches.Rectangle((0.55, mb_y), 0.03, 0.10, fc=teal, ec='none', zorder=6))
ax_a.text(0.60, mb_y+0.05, 'Distinct-$n$', fontsize=5.5, va='center', color=navy, zorder=7)
ax_a.text(0.88, mb_y+0.05, 'downstream', fontsize=5, va='center', color=teal, fontstyle='italic', zorder=7)

# ---- Panel (b): MMCT Multi-Method Consensus ----
ax_b = fig.add_subplot(gs[1])
ax_b.set_xlim(-0.05, 1.05)
ax_b.set_ylim(-0.05, 1.15)
ax_b.axis('off')
ax_b.text(0.0, 1.12, '(b)', fontsize=9, fontweight='bold', transform=ax_b.transAxes)
ax_b.text(0.5, 1.12, 'Multi-Method Consensus (MMCT)', fontsize=7.5, fontstyle='italic',
          ha='center', transform=ax_b.transAxes, color=gray)

methods = [
    ('Naive XCorr', coral, 'FPR 92%', 0.02),
    ('Diff. XCorr', amber, 'FPR 3%', 0.04),
    ('Threshold', light_blue, 'FPR 28%', 0.03),
    ('Perm. Granger', navy, 'FPR 11%', 0.10),
    ('Toda-Yam.', teal, 'FPR 39%', 0.03),
]

y_start = 0.88
y_step = 0.155
for i, (name, color, fpr, weight) in enumerate(methods):
    y = y_start - i * y_step
    bw_m = 0.32
    is_hero = (name == 'Perm. Granger')
    lw = 1.5 if is_hero else 0.8
    fc = navy if is_hero else '#F8F9FA'
    tc = 'white' if is_hero else navy
    rounded_box(ax_b, (0.0, y-0.05), bw_m, 0.10, name,
                fc=fc, ec=color, lw=lw, fontsize=5.5, fontweight='bold' if is_hero else 'normal', text_color=tc)
    ax_b.text(0.34, y, fpr, fontsize=5, va='center', color=coral if 'FPR 92' in fpr or 'FPR 39' in fpr or 'FPR 28' in fpr else teal)

    w_bar = weight * 3
    ax_b.add_patch(mpatches.Rectangle((0.50, y-0.02), w_bar, 0.04,
                   fc=color, alpha=0.4, ec='none', zorder=3))
    ax_b.text(0.50 + w_bar + 0.01, y, f'$w$={weight:.2f}', fontsize=4.5, va='center', color=gray)

    arrow(ax_b, (0.50 + w_bar + 0.08, y), (0.78, 0.50), color='#CCCCCC', lw=0.4, style='-')

consensus_y = 0.40
rounded_box(ax_b, (0.72, consensus_y), 0.28, 0.12, 'Consensus\n$K{\\geq}3$',
            fc='#E8F6F3', ec=teal, lw=1.0, fontsize=6)

arrow(ax_b, (0.86, consensus_y), (0.86, 0.18), color=navy, lw=1.2)

rounded_box(ax_b, (0.68, 0.02), 0.32, 0.12, 'PermG\nselected',
            fc=navy, ec=navy, lw=1.2, fontsize=6, fontweight='bold', text_color='white')
ax_b.text(0.84, -0.02, 'lowest directional FPR', fontsize=5, ha='center',
          color=gray, fontstyle='italic')

# ---- Panel (c): S×R Detection Regimes ----
ax_c = fig.add_subplot(gs[2])

alpha = np.linspace(0, 1, 500)
S = alpha ** 0.8
R_base = 1 / (1 + np.exp(-15 * (alpha - 0.30)))
R_dip = 0.55 * np.exp(-((alpha - 0.58) / 0.055) ** 2)
R = np.clip(R_base - R_dip, 0, 1)
D = S * R

regime_bounds = [0, 0.42, 0.52, 0.65, 1.0]
regime_colors = ['#FADBD8', '#D5F5E3', '#FEF9E7', '#D6EAF8']
regime_labels = ['Blind', 'Onset', 'Dip', 'Detection']

for i in range(4):
    ax_c.axvspan(regime_bounds[i], regime_bounds[i+1],
                 color=regime_colors[i], alpha=0.4, zorder=0)
    mid = (regime_bounds[i] + regime_bounds[i+1]) / 2
    ax_c.text(mid, 0.97, regime_labels[i], fontsize=5, ha='center',
              fontweight='semibold', color='#444444')

ax_c.plot(alpha, S, '--', color=navy, linewidth=1.0, alpha=0.6, label=r'$S(\alpha)$')
ax_c.plot(alpha, R, '--', color=coral, linewidth=1.0, alpha=0.6, label=r'$R(\alpha)$')
ax_c.fill_between(alpha, D, color='#3498DB', alpha=0.15, zorder=2)
ax_c.plot(alpha, D, color='#4a1486', linewidth=1.5, zorder=3, label=r'$S \times R$')

ax_c.set_xlabel(r'Contamination $\alpha$', fontsize=7)
ax_c.set_ylabel('Detection rate', fontsize=7)
ax_c.set_xlim(0, 1)
ax_c.set_ylim(-0.02, 1.05)
ax_c.set_xticks([0, 0.25, 0.50, 0.75, 1.0])
ax_c.legend(fontsize=5, loc='center left', bbox_to_anchor=(0.0, 0.45), framealpha=0.8, edgecolor='#DEE2E6')
ax_c.spines['top'].set_visible(False)
ax_c.spines['right'].set_visible(False)

ax_c.text(0.0, 1.12, '(c)', fontsize=9, fontweight='bold', transform=ax_c.transAxes)
ax_c.text(0.5, 1.12, r'Signal$\times$Resolution', fontsize=7.5, fontstyle='italic',
          ha='center', transform=ax_c.transAxes, color=gray)

ax_c.text(0.85, 0.05, r'$\alpha_c(T) \sim T^{-\gamma}$', fontsize=5.5,
          fontstyle='italic', color='#4a1486', transform=ax_c.transAxes)

out = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/fig_framework'
fig.savefig(f'{out}.pdf', dpi=300, bbox_inches='tight')
fig.savefig(f'{out}.png', dpi=300, bbox_inches='tight')
plt.close()
print(f'Saved: {out}.pdf and .png')
