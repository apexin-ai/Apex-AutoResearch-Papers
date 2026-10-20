import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
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

COLOR_TSR = '#4C72B0'
COLOR_CAR = '#C44E52'
HARD_BG = '#FDEDEC'

tasks = [f'T{i}' for i in range(10)]
tsr = np.array([0.99, 0.97, 0.95, 0.87, 0.98, 0.85, 0.85, 0.99, 0.99, 0.99])
car = np.array([0.98, 0.92, 0.92, 0.38, 0.98, 0.07, 0.57, 0.97, 1.00, 1.00])
hard_tasks = {3, 5, 6}

fig, ax = plt.subplots(figsize=(5.2, 3.5))

# Hard task background — span contiguous T5-T6 together, T3 alone
ax.axvspan(2.55, 3.45, color=HARD_BG, alpha=0.7, zorder=0)
ax.axvspan(4.55, 6.45, color=HARD_BG, alpha=0.7, zorder=0)

x = np.arange(len(tasks))
w = 0.34
bars_tsr = ax.bar(x - w/2, tsr, w, color=COLOR_TSR, edgecolor='white',
                  linewidth=0.5, label='TSR', zorder=2, alpha=0.9)
bars_car = ax.bar(x + w/2, car, w, color=COLOR_CAR, edgecolor='white',
                  linewidth=0.5, label='CAR', zorder=2, alpha=0.9)

# Gap annotations — only for the 3 hard tasks
# T5: worst case, most prominent
t5_mid = (car[5] + tsr[5]) / 2
ax.annotate('', xy=(5 + w/2 + 0.02, car[5] + 0.01),
            xytext=(5 + w/2 + 0.02, tsr[5] - 0.01),
            arrowprops=dict(arrowstyle='<->', color='#888888',
                            lw=0.7, shrinkA=0, shrinkB=0))
t = ax.text(5 - 0.45, t5_mid - 0.02, '93%\ncollision',
            fontsize=7.5, color='#C44E52', va='center', ha='right',
            fontweight='bold', linespacing=1.1)
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# T3
t3_mid = (car[3] + tsr[3]) / 2
ax.annotate('', xy=(3 + w/2 + 0.02, car[3] + 0.01),
            xytext=(3 + w/2 + 0.02, tsr[3] - 0.01),
            arrowprops=dict(arrowstyle='<->', color='#888888',
                            lw=0.7, shrinkA=0, shrinkB=0))
t = ax.text(3 - 0.45, t3_mid, '62%\ncollision',
            fontsize=6.5, color='#555555', va='center', ha='right',
            fontstyle='italic', linespacing=1.1)
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# T6
t6_mid = (car[6] + tsr[6]) / 2
ax.annotate('', xy=(6 + w/2 + 0.02, car[6] + 0.01),
            xytext=(6 + w/2 + 0.02, tsr[6] - 0.01),
            arrowprops=dict(arrowstyle='<->', color='#888888',
                            lw=0.7, shrinkA=0, shrinkB=0))
t = ax.text(6 + w/2 + 0.38, t6_mid + 0.04, '43%\ncollision',
            fontsize=6.5, color='#555555', va='center', ha='left',
            fontstyle='italic', linespacing=1.1)
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# "Hard" labels at top
for idx in hard_tasks:
    ax.text(idx, 1.04, 'Hard', fontsize=7, color='#C44E52', ha='center',
            fontweight='bold', fontstyle='italic')

# Overall stats box — positioned slightly lower to avoid crowding with 1.0 line
ax.text(0.98, 0.92,
        'Overall TSR = 0.907\nOverall CAR = 0.780',
        transform=ax.transAxes, fontsize=8, va='top', ha='right',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                  edgecolor='#BBBBBB', linewidth=0.5, alpha=0.95))

ax.set_ylim(0, 1.12)
ax.set_xlim(-0.6, 9.6)
ax.set_xticks(x)
ax.set_xticklabels(tasks)
ax.set_ylabel('Rate')
ax.set_xlabel('Task')

ax.yaxis.grid(True, alpha=0.15, linewidth=0.5, zorder=0)
ax.set_axisbelow(True)

ax.legend(loc='lower left', frameon=True, framealpha=0.9,
          edgecolor='#CCCCCC', fancybox=False, borderpad=0.4)

ax.text(-0.12, 1.06, '(a)', transform=ax.transAxes,
        fontsize=13, fontweight='bold', va='top')

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/figures/'
fig.savefig(out_dir + 'fig1_panel_a.pdf')
fig.savefig(out_dir + 'fig1_panel_a.png')
plt.close()
print('Panel (a) saved.')
