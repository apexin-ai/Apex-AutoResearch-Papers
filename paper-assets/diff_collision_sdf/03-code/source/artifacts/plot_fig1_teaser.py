import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['STIXGeneral', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 7.5,
    'axes.titlesize': 8.5,
    'axes.labelsize': 7.5,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 6.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.2,
    'axes.linewidth': 0.5,
    'xtick.major.width': 0.4,
    'ytick.major.width': 0.4,
    'xtick.major.size': 2.5,
    'ytick.major.size': 2.5,
    'xtick.major.pad': 2,
    'ytick.major.pad': 2,
    'hatch.linewidth': 0.5,
})

C_FROZEN    = '#C8C8C8'
C_GENUINE   = '#4A90D9'
C_COLLISION = '#E8734A'
C_RAW       = '#A8D0F0'
C_DFCAR     = '#1B4F7A'
C_ARROW     = '#C0392B'

models = [r'$\pi_0$ Full-FT', r'$\pi_0$ LoRA',
          r'$\pi_{0.5}$ Base', r'$\pi_{0.5}$ LoRA']

frozen_safe  = np.array([82.5, 89.0,  0.0,  0.0])
genuine_safe = np.array([ 9.0,  2.5, 26.8, 54.5])
collision    = np.array([ 8.5,  8.5, 73.2, 45.5])

raw_car = np.array([91.5, 91.5, 26.8, 54.5])
dfcar   = np.array([ 9.0,  2.5, 26.8, 54.5])

fig = plt.figure(figsize=(5.5, 2.5))
gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 1], wspace=0.4,
                      left=0.12, right=0.97, top=0.84, bottom=0.22)
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])

# ── Panel (a): Decomposing CAR ──
y_pos = np.arange(len(models))
bar_h = 0.50

bars_f = ax1.barh(y_pos, frozen_safe, height=bar_h,
                  color=C_FROZEN, edgecolor='#AAAAAA', linewidth=0.3,
                  hatch='///', zorder=2)
bars_g = ax1.barh(y_pos, genuine_safe, height=bar_h, left=frozen_safe,
                  color=C_GENUINE, edgecolor='white', linewidth=0.3, zorder=2)
bars_c = ax1.barh(y_pos, collision, height=bar_h,
                  left=frozen_safe + genuine_safe,
                  color=C_COLLISION, edgecolor='white', linewidth=0.3, zorder=2)

ax1.set_yticks(y_pos)
ax1.set_yticklabels(models)
ax1.set_xlabel('Episode proportion (%)')
ax1.set_xlim(0, 100)
ax1.set_title(r'(a)  $\pi_0$ CAR is almost entirely action-collapsed',
              fontsize=7.5, fontstyle='italic', pad=6, loc='left')
ax1.invert_yaxis()

# Labels inside large segments
for i in range(len(models)):
    fs, gs_v, col = frozen_safe[i], genuine_safe[i], collision[i]
    if fs > 20:
        ax1.text(fs / 2, i, f'{fs:.1f}%', ha='center', va='center',
                fontsize=5.5, color='#555555', fontweight='bold')
    if gs_v > 15:
        ax1.text(fs + gs_v / 2, i, f'{gs_v:.1f}%', ha='center', va='center',
                fontsize=5.5, color='white', fontweight='bold')
    if col > 25:
        ax1.text(fs + gs_v + col / 2, i, f'{col:.1f}%', ha='center', va='center',
                fontsize=5.5, color='white', fontweight='bold')

# Pi0 bars: color-coded labels to the right
for i in range(2):
    fs, gs_v, col = frozen_safe[i], genuine_safe[i], collision[i]
    right_x = 100
    ax1.plot([right_x + 0.8, right_x + 0.8], [i - 0.15, i + 0.15],
             color='#BBBBBB', linewidth=0.4, clip_on=False, zorder=3)
    ax1.text(right_x + 2, i - 0.14, f'{gs_v:.1f}%',
             fontsize=4.8, color=C_GENUINE, fontweight='bold',
             va='center', ha='left', clip_on=False)
    ax1.text(right_x + 2, i + 0.14, f'{col:.1f}%',
             fontsize=4.8, color=C_COLLISION, fontweight='bold',
             va='center', ha='left', clip_on=False)

ax1.axhline(y=1.5, color='#CCCCCC', linewidth=0.5, linestyle='--', zorder=1)

legend_patches = [
    mpatches.Patch(facecolor=C_FROZEN, hatch='///', edgecolor='#AAA', label='Action-collapsed'),
    mpatches.Patch(facecolor=C_GENUINE, edgecolor='none', label='Genuine-safe'),
    mpatches.Patch(facecolor=C_COLLISION, edgecolor='none', label='Collision'),
]
fig.legend(handles=legend_patches, loc='lower center',
           bbox_to_anchor=(0.35, 0.01), ncol=3, frameon=False,
           handlelength=1.2, handletextpad=0.4, columnspacing=1.2,
           fontsize=6)

# ── Panel (b): Raw CAR vs dfCAR ──
x_pos = np.arange(len(models))
bar_w = 0.30
gap = 0.03

bars_raw = ax2.bar(x_pos - bar_w/2 - gap, raw_car, width=bar_w,
                   color=C_RAW, edgecolor='none', zorder=2, label='Raw CAR')
bars_df  = ax2.bar(x_pos + bar_w/2 + gap, dfcar, width=bar_w,
                   color=C_DFCAR, edgecolor='none', zorder=2, label='dfCAR')

ax2.set_xticks(x_pos)
xlabels = [r'$\pi_0$' + '\nFull-FT', r'$\pi_0$' + '\nLoRA',
           r'$\pi_{0.5}$' + '\nBase', r'$\pi_{0.5}$' + '\nLoRA']
ax2.set_xticklabels(xlabels, fontsize=5.5, linespacing=1.1)
ax2.set_ylabel('Rate (%)')
ax2.set_ylim(0, 110)
ax2.set_title('(b)  dfCAR reveals true performance',
              fontsize=7.5, fontstyle='italic', pad=6, loc='left')
ax2.yaxis.grid(True, alpha=0.12, linewidth=0.4, zorder=0)

ax2.legend(loc='upper right', frameon=False, borderpad=0.3, fontsize=6)

# Dramatic arrow: Pi0 Full-FT
arrow_x = 0
ax2.annotate('',
    xy=(arrow_x + bar_w/2 + gap, dfcar[0] + 2),
    xytext=(arrow_x - bar_w/2 - gap, raw_car[0] - 1),
    arrowprops=dict(
        arrowstyle='->', color=C_ARROW, lw=2.0,
        connectionstyle='arc3,rad=-0.3',
        shrinkA=2, shrinkB=2,
    ), zorder=5)

drop_pp0 = raw_car[0] - dfcar[0]
t = ax2.text(arrow_x + 0.50, (raw_car[0] + dfcar[0]) / 2 + 8,
             f'{drop_pp0:.0f}pp\ndrop',
             ha='center', fontsize=6.5, color=C_ARROW, fontweight='bold',
             linespacing=0.85, zorder=6)
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Small annotation for Pi0 LoRA
drop_pp1 = raw_car[1] - dfcar[1]
t2 = ax2.text(1 + bar_w/2 + gap + 0.06, dfcar[1] + 8,
              f'{drop_pp1:.0f}pp',
              ha='left', fontsize=5, color=C_ARROW, fontstyle='italic', zorder=6)
t2.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

# Value labels
for i in range(len(models)):
    r, d = raw_car[i], dfcar[i]
    if abs(r - d) < 0.5:
        ax2.text(i, r + 2, f'{r:.1f}', ha='center', va='bottom',
                 fontsize=5.5, color='#444444', fontweight='bold')
    else:
        ax2.text(i - bar_w/2 - gap, r + 1.5,
                 f'{r:.1f}', ha='center', va='bottom',
                 fontsize=5, color='#777777')
        if i == 0:
            # Pi0 Full-FT dfCAR: offset right to avoid red arrow overlap
            ax2.text(i + bar_w/2 + gap + 0.22, d + 0.5,
                     f'{d:.1f}', ha='left', va='bottom',
                     fontsize=5, color='#333333', fontweight='bold')
        else:
            ax2.text(i + bar_w/2 + gap, d + 1.5,
                     f'{d:.1f}', ha='center', va='bottom',
                     fontsize=5, color='#333333', fontweight='bold')

ax2.axvline(x=1.5, color='#CCCCCC', linewidth=0.5, linestyle='--', zorder=1)

import os
d = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures'
os.makedirs(d, exist_ok=True)
fig.savefig(f'{d}/fig1_teaser.pdf')
fig.savefig(f'{d}/fig1_teaser.png')
plt.close()
print('Saved: fig1_teaser.pdf + fig1_teaser.png')
