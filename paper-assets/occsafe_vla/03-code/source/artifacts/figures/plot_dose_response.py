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
    'legend.fontsize': 9.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

# ── Data ──
raw = {
    0:     [0.746, 0.744, 0.748],
    15000: [0.804],
    25000: [0.688, 0.760],
    35000: [0.768, 0.783, 0.798],
    45000: [0.764],
    50000: [0.832, 0.788, 0.770],
}
pending = {15000: 1, 25000: 1, 45000: 1}
reverse_cutoff = [0.700, 0.736]
vanilla_mean = 0.780

steps_sorted = sorted(raw.keys())
means = [np.mean(raw[s]) for s in steps_sorted]
stds = [np.std(raw[s]) if len(raw[s]) > 1 else 0 for s in steps_sorted]
detach_mean = np.mean(raw[0])

fig, ax = plt.subplots(figsize=(7.5, 4.3))

# ── Vanilla baseline ──
ax.axhline(y=vanilla_mean, color='#9E9E9E', linestyle='--', linewidth=1.2, alpha=0.5, zorder=1)
t_bl = ax.text(-2500, vanilla_mean + 0.003, 'Vanilla (0.780)', fontsize=7.5,
               color='#888888', va='bottom', ha='left')
t_bl.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# ── Detach reference line ──
ax.axhline(y=detach_mean, color='#C95B4B', linestyle=':', linewidth=0.8, alpha=0.3, zorder=1)

# ── Withdrawal effect zone ──
ax.fill_between([21000, 29000], 0.665, detach_mean - 0.003, alpha=0.07,
                color='#D32F2F', zorder=0)
t_wd = ax.text(25000, 0.670, 'withdrawal\neffect', ha='center', va='bottom',
               fontsize=7.5, color='#C62828', fontstyle='italic', alpha=0.7,
               linespacing=1.0)
t_wd.set_path_effects([pe.withStroke(linewidth=2.0, foreground='white')])

# ── Main curve ──
color_main = '#3778BF'
ax.plot(steps_sorted, means, '-', color=color_main, linewidth=2.0, zorder=3, alpha=0.8)

for i, s in enumerate(steps_sorted):
    n_seeds = len(raw[s])
    ms = 8 if n_seeds >= 3 else 6.5
    ax.plot(s, means[i], 'o', color=color_main, markersize=ms,
            markerfacecolor=color_main, markeredgecolor='white',
            markeredgewidth=1.2, zorder=5)
    if stds[i] > 0:
        ax.errorbar(s, means[i], yerr=stds[i], fmt='none', ecolor=color_main,
                    capsize=4, capthick=1.0, elinewidth=1.0, zorder=4, alpha=0.6)
    if n_seeds > 1:
        for v in raw[s]:
            ax.plot(s, v, 'o', color=color_main, markersize=3, alpha=0.3, zorder=4)

# ── Mean labels ──
label_cfg = {
    0:     (5000, -0.001, 'left'),
    15000: (0, 0.010, 'center'),
    25000: (0, -0.017, 'center'),
    35000: (0, 0.010, 'center'),
    45000: (0, -0.015, 'center'),
    50000: (0, 0.010, 'center'),
}
for s, m in zip(steps_sorted, means):
    ox, oy, ha = label_cfg[s]
    t_l = ax.text(s + ox, m + oy, f'{m:.3f}', fontsize=8,
                  ha=ha, va='center', color='#333333', fontweight='bold')
    t_l.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# ── Pending seed annotations ──
pending_cfg = {
    15000: (-5500, -0.010),
    25000: (5000, 0.005),
    45000: (5000, 0.005),
}
for s, n_p in pending.items():
    m_val = np.mean(raw[s])
    ox, oy = pending_cfg[s]
    ax.text(s + ox, m_val + oy, f'+{n_p} seed pending', fontsize=6,
            color='#E67E22', ha='center', va='center', fontstyle='italic',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF8E1',
                      edgecolor='#F0C27A', alpha=0.85, linewidth=0.5))

# ── Reverse cutoff ──
color_rev = '#D55E00'
rev_mean = np.mean(reverse_cutoff)
rev_std = np.std(reverse_cutoff)

ax.plot(15000, rev_mean, '^', color=color_rev, markersize=10,
        markeredgecolor='white', markeredgewidth=1.2, zorder=5)
ax.errorbar(15000, rev_mean, yerr=rev_std, fmt='none', ecolor=color_rev,
            capsize=4, capthick=1.0, elinewidth=1.0, zorder=4, alpha=0.6)
for v in reverse_cutoff:
    ax.plot(15000, v, '^', color=color_rev, markersize=3.5, alpha=0.35, zorder=4)

# Reverse pending
ax.text(21000, rev_mean - 0.012, '+1 seed pending', fontsize=6,
        color='#E67E22', ha='center', va='center', fontstyle='italic',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#FFF8E1',
                  edgecolor='#F0C27A', alpha=0.85, linewidth=0.5))

# Reverse label
ax.annotate('reverse cutoff\n(15K late flow)', xy=(15000, rev_mean),
            xytext=(3000, 0.688), fontsize=7.5, color=color_rev,
            fontstyle='italic', ha='center', linespacing=1.0,
            arrowprops=dict(arrowstyle='->', color=color_rev, lw=1.0,
                            connectionstyle='arc3,rad=0.2'))

# ── Legend ──
legend_handles = [
    plt.Line2D([0], [0], marker='o', color=color_main, linewidth=2, markersize=7,
               markerfacecolor=color_main, markeredgecolor='white',
               label='Early gradient flow (cutoff)'),
    plt.Line2D([0], [0], marker='^', color=color_rev, linewidth=0, markersize=8,
               markerfacecolor=color_rev, markeredgecolor='white',
               label='Late gradient flow (reverse)'),
    plt.Line2D([0], [0], color='#9E9E9E', linestyle='--', linewidth=1.2,
               label='Vanilla baseline'),
]
ax.legend(handles=legend_handles, loc='upper left', framealpha=0.95,
          edgecolor='#DDDDDD', fontsize=8.5, borderpad=0.6)

# ── Axis ──
ax.set_xlabel('Gradient Flow Duration (training steps)')
ax.set_ylabel('Collision Avoidance Rate (CAR)')
ax.set_xticks([0, 15000, 25000, 35000, 45000, 50000])
ax.set_xticklabels(['0\n(Detach)', '15K', '25K', '35K', '45K', '50K\n(Full)'])
ax.set_xlim(-5000, 55000)
ax.set_ylim(0.660, 0.855)
ax.grid(axis='y', alpha=0.15, zorder=0)

plt.tight_layout()

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/figures'
plt.savefig(f'{outdir}/dose_response_curve.pdf')
plt.savefig(f'{outdir}/dose_response_curve.png')
print('Saved dose_response_curve.pdf/.png')
