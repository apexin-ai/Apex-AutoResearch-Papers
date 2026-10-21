import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.ticker as mticker
import numpy as np

# ── Colors ──
CORAL = '#E8846B'
CORAL_DARK = '#C0603E'
BLUE = '#0072B2'
BLUE_DARK = '#005A8D'
RED_TEXT = '#C0392B'
GRAY_TEXT = '#888888'

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 10.5,
    'axes.titleweight': 'bold',
    'axes.labelsize': 9.5,
    'xtick.labelsize': 8.5,
    'ytick.labelsize': 8.5,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.grid': False,
    'axes.linewidth': 0.6,
})

stroke = [pe.withStroke(linewidth=2.5, foreground='white')]
stroke_s = [pe.withStroke(linewidth=1.8, foreground='white')]

fig = plt.figure(figsize=(5.5, 2.5))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1.7, 1], wspace=0.45,
                      left=0.08, right=0.97, top=0.82, bottom=0.22)

models = ['Pi0+A1', 'Pi0.5']
x_pos = [0, 1]
clrs = [CORAL, BLUE]
edge_clrs = ['#B5604A', BLUE_DARK]

# ════════════════════════════════════════
# Panel (a): Standard CAR
# ════════════════════════════════════════
ax_a = fig.add_subplot(gs[0])
car = [91.5, 26.8]

bars = ax_a.bar(x_pos, car, width=0.48, color=clrs, edgecolor=edge_clrs,
                linewidth=0.7, zorder=3)
bars[0].set_hatch('///')

for b, v in zip(bars, car):
    ax_a.text(b.get_x() + b.get_width()/2, v + 1.5, f'{v}%',
              ha='center', va='bottom', fontsize=8.5, fontweight='bold',
              path_effects=stroke)

# x-tick labels with TSR embedded as second line
ax_a.set_xticks(x_pos)
ax_a.set_xticklabels(['Pi0+A1\nTSR=0%', 'Pi0.5\nTSR=74.7%'], fontsize=7.5)
# color the TSR portions
for i, (tick, color) in enumerate(zip(ax_a.get_xticklabels(), [RED_TEXT, BLUE])):
    pass  # can't partially color tick labels; use separate text instead

# Actually clear tick labels and use manual text
ax_a.set_xticklabels([])
ax_a.text(0, -0.04, 'Pi0+A1', ha='center', va='top', fontsize=8,
          transform=ax_a.get_xaxis_transform())
ax_a.text(1, -0.04, 'Pi0.5', ha='center', va='top', fontsize=8,
          transform=ax_a.get_xaxis_transform())
ax_a.text(0, -0.17, 'TSR=0%', ha='center', va='top', fontsize=5.5,
          color=RED_TEXT, fontweight='semibold', transform=ax_a.get_xaxis_transform())
ax_a.text(1, -0.17, 'TSR=74.7%', ha='center', va='top', fontsize=5.5,
          color=BLUE, fontweight='semibold', transform=ax_a.get_xaxis_transform())

ax_a.set_ylabel('CAR (%)')
ax_a.set_ylim(0, 108)
ax_a.set_title('(a) Standard CAR', pad=6)
ax_a.set_xlim(-0.6, 1.6)
ax_a.tick_params(axis='x', length=0, pad=2)
ax_a.yaxis.set_major_locator(mticker.MultipleLocator(20))

# ════════════════════════════════════════
# Panel (b): Displacement (log lollipop)
# ════════════════════════════════════════
ax_b = fig.add_subplot(gs[1])

y_a1, y_05 = 0.70, 0.30
x_a1, x_05 = 0.001, 288

# collapse zone
ax_b.axvspan(2e-5, 0.1, color='#F0F0F0', alpha=0.8, zorder=1)

# threshold line
ax_b.axvline(0.1, color='#AAAAAA', ls='--', lw=0.7, zorder=2)

# lollipop: Pi0+A1
ax_b.plot([2e-5, x_a1], [y_a1, y_a1], color=CORAL, lw=1.0, zorder=3, alpha=0.4)
ax_b.plot(x_a1, y_a1, 'o', color=CORAL, ms=7.5, zorder=4,
          markeredgecolor='white', markeredgewidth=0.8)

# lollipop: Pi0.5
ax_b.plot([2e-5, x_05], [y_05, y_05], color=BLUE, lw=1.0, zorder=3, alpha=0.4)
ax_b.plot(x_05, y_05, 'o', color=BLUE, ms=7.5, zorder=4,
          markeredgecolor='white', markeredgewidth=0.8)

# annotation: 73.9% below 1 μm
ax_b.annotate('73.9% below 1 μm', xy=(x_a1, y_a1 + 0.03),
              xytext=(0.15, 0.91), fontsize=6.5, color=CORAL_DARK,
              fontweight='semibold', ha='left', va='bottom',
              path_effects=stroke_s,
              arrowprops=dict(arrowstyle='->', color=CORAL_DARK, lw=0.7,
                              connectionstyle='arc3,rad=-0.2'))

# annotation: 288 mm
ax_b.annotate('288 mm', xy=(x_05, y_05 - 0.02),
              xytext=(50, 0.14), fontsize=6.5, color=BLUE,
              fontweight='semibold', ha='center', va='top',
              path_effects=stroke_s,
              arrowprops=dict(arrowstyle='->', color=BLUE, lw=0.7))

# zone label
ax_b.text(0.002, 0.05, 'action\ncollapse', fontsize=5.5, color='#999999',
          ha='center', va='bottom', fontstyle='italic', linespacing=1.1)

# τ_d label
ax_b.text(0.065, 0.94, r'$\tau_d$', fontsize=7.5, color='#666666',
          ha='right', va='top', path_effects=stroke_s)

# double arrow: 5 orders of magnitude
ay = 0.50
ax_b.annotate('', xy=(x_a1*1.5, ay), xytext=(x_05*0.7, ay),
              arrowprops=dict(arrowstyle='<->', color='#444444', lw=0.9))
ax_b.text(np.sqrt(x_a1*x_05), ay + 0.06, '5 orders of magnitude',
          fontsize=6, ha='center', va='bottom', color='#444444',
          fontweight='semibold', path_effects=stroke_s)

# model labels on left
ax_b.text(1.5e-5, y_a1, 'Pi0+A1  ', fontsize=7.5, ha='right', va='center',
          color=CORAL_DARK, fontweight='semibold')
ax_b.text(1.5e-5, y_05, 'Pi0.5  ', fontsize=7.5, ha='right', va='center',
          color=BLUE, fontweight='semibold')

ax_b.set_xscale('log')
ax_b.set_xlim(2e-5, 3e3)
ax_b.set_ylim(0, 0.98)
ax_b.set_xlabel('Displacement (mm)', labelpad=2)
ax_b.set_xticks([1e-3, 1e-1, 1e1, 1e3])
ax_b.set_xticklabels(['0.001', '0.1', '10', '1000'], fontsize=7.5)
ax_b.tick_params(axis='x', which='minor', bottom=False)
ax_b.set_yticks([])
ax_b.spines['left'].set_visible(False)
ax_b.set_title('(b) Displacement', pad=6)

# ════════════════════════════════════════
# Panel (c): Filtered CAR
# ════════════════════════════════════════
ax_c = fig.add_subplot(gs[2])
car_f = [0.3, 26.8]
bf = ax_c.bar(x_pos, car_f, width=0.48, color=clrs, edgecolor=edge_clrs,
              linewidth=0.7, zorder=3)

ax_c.text(bf[0].get_x() + bf[0].get_width()/2, 4, '≈ 0%',
          ha='center', va='bottom', fontsize=8.5, fontweight='bold',
          color=CORAL_DARK, path_effects=stroke)
ax_c.text(bf[1].get_x() + bf[1].get_width()/2, car_f[1] + 1.5, f'{car_f[1]}%',
          ha='center', va='bottom', fontsize=8.5, fontweight='bold',
          path_effects=stroke)

# red arrow + label — centered on bar
ax_c.annotate('', xy=(0, 14), xytext=(0, 58),
              arrowprops=dict(arrowstyle='->', color=RED_TEXT, lw=1.8))
ax_c.text(0, 62, '91.5%→≈0%', ha='center', va='bottom', fontsize=5.8,
          color=RED_TEXT, fontweight='bold', path_effects=stroke)

ax_c.text(1, car_f[1] + 14, 'unchanged', ha='center', va='bottom',
          fontsize=6, color=GRAY_TEXT, fontstyle='italic')

ax_c.set_ylabel(r'CAR$_f$ (%)')
ax_c.set_ylim(0, 108)
ax_c.set_title(r'(c) After filtering (CAR$_f$)', pad=6)
ax_c.set_xlim(-0.6, 1.6)
ax_c.set_xticks(x_pos)
ax_c.set_xticklabels(models, fontsize=8)
ax_c.tick_params(axis='x', length=0, pad=2)
ax_c.yaxis.set_major_locator(mticker.MultipleLocator(20))

# ── Save ──
d = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures'
fig.savefig(f'{d}/fig1_teaser.pdf', bbox_inches='tight', dpi=300, pad_inches=0.06)
fig.savefig(f'{d}/fig1_teaser.png', bbox_inches='tight', dpi=300, pad_inches=0.06)
print('Round 7: Saved.')
