#!/usr/bin/env python3
"""Fig 5 combined: lambda-CAR/TSR curve (left) + per-task CAR fingerprint (right).

Single figure with two subplots — eliminates height alignment issues in LaTeX.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.lines import Line2D
import numpy as np
from pathlib import Path

OUT = Path('./output/fig5_lambda_and_fingerprint')

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['STIXGeneral', 'DejaVu Serif'],
    'mathtext.fontset': 'stix',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.pad_inches': 0.04,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.7,
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))

# ============================================================
# LEFT: lambda-CAR/TSR curve
# ============================================================
C_CAR = '#0072B2'
C_TSR = '#D55E00'
C_NULL = '#CCCCCC'
STROKE = [pe.withStroke(linewidth=2.5, foreground='white')]

car_mean = np.array([54.67, 54.5, 56.33, 57.0])
car_std  = np.array([2.02, 2.29, 1.61, 2.18])
seeds    = np.array([3, 3, 3, 3])
tsr_mean = np.array([51.5, 54.0, 53.83, 50.17])
car_se   = car_std / np.sqrt(seeds)

null_mu, null_sig = 54.58, 1.93

xpos = np.array([0, 1.8, 2.8, 3.8])
xlbl = ['0\n(LoRA-only)', '0.005', '0.01', '0.1']

ax1.axhspan(null_mu - null_sig, null_mu + null_sig,
            color=C_NULL, alpha=0.3, zorder=0)
ax1.axhline(null_mu, color='#BBBBBB', ls='--', lw=0.8, zorder=1)

ax1.errorbar(xpos[0], car_mean[0], yerr=car_se[0],
             fmt='o', color=C_CAR, ms=6,
             capsize=3, capthick=1.0, elinewidth=1.0,
             mec='white', mew=0.6, zorder=4)
ax1.errorbar(xpos[1:], car_mean[1:], yerr=car_se[1:],
             fmt='o-', color=C_CAR, ms=6, lw=1.5,
             capsize=3, capthick=1.0, elinewidth=1.0,
             mec='white', mew=0.6, zorder=4)

ax1.plot(xpos[0], tsr_mean[0], 's', color=C_TSR, ms=5.5,
         mec='white', mew=0.6, alpha=0.75, zorder=3)
ax1.plot(xpos[1:], tsr_mean[1:], 's--', color=C_TSR, ms=5.5,
         mec='white', mew=0.6, alpha=0.75, lw=1.2, zorder=3)

ann_cfg = [
    (12, 0, 'left'),
    (0, 7, 'center'),
    (0, 7, 'center'),
    (0, 7, 'center'),
]
for i in range(4):
    ox, oy, ha = ann_cfg[i]
    ref_y = car_mean[i] + car_se[i] if oy >= 0 else car_mean[i]
    t = ax1.annotate(f'n={seeds[i]}',
                     xy=(xpos[i], ref_y),
                     xytext=(ox, oy), textcoords='offset points',
                     fontsize=7, color=C_CAR, ha=ha, style='italic')
    t.set_path_effects(STROKE)

t = ax1.text(4.3, null_mu, 'null\n$\\pm$1$\\sigma$',
             fontsize=7, color='#999', ha='center', va='center',
             style='italic', linespacing=0.85)
t.set_path_effects(STROKE)

trans = ax1.get_xaxis_transform()
for bx in [0.7, 0.9]:
    ax1.plot([bx, bx + 0.12], [-0.04, 0.04], transform=trans,
             color='k', lw=0.6, clip_on=False)

ax1.set_xticks(xpos)
ax1.set_xticklabels(xlbl, fontsize=9)
ax1.set_xlabel(r'$\lambda$ (SDF loss weight)', fontsize=10)
ax1.set_ylabel('Rate (%)', fontsize=10)
ax1.set_xlim(-0.6, 4.8)
ax1.set_ylim(46, 60)

handles_l = [
    Line2D([0], [0], marker='o', color=C_CAR, mfc=C_CAR,
           mec='white', ms=5, lw=1.5, ls='-', label='CAR'),
    Line2D([0], [0], marker='s', color=C_TSR, mfc=C_TSR,
           mec='white', ms=4.5, lw=1.2, ls='--', label='TSR'),
]
ax1.legend(handles=handles_l, loc='lower right', fontsize=8,
           framealpha=0.92, edgecolor='none', handlelength=1.8,
           handletextpad=0.5, borderpad=0.4, labelspacing=0.3)

# ============================================================
# RIGHT: per-task CAR fingerprint
# ============================================================
lora_s0 = {'CP': 74, 'Milk': 70, 'OJ': 56, 'BBQ': 26}
lora_s1 = {'CP': 68, 'Milk': 72, 'OJ': 54, 'BBQ': 16}
lora_s2 = {'CP': 76, 'Milk': 62, 'OJ': 56, 'BBQ': 26}
lora_mean = {k: np.mean([lora_s0[k], lora_s1[k], lora_s2[k]]) for k in lora_s0}
lora_std = {k: np.std([lora_s0[k], lora_s1[k], lora_s2[k]], ddof=1) for k in lora_s0}

l005_mean = {'OJ': 54.0, 'CP': 72.7, 'Milk': 71.3, 'BBQ': 20.0}
l01_mean = {'OJ': 57.3, 'CP': 72.7, 'Milk': 72.0, 'BBQ': 23.3}

l1_s0 = {'OJ': 60, 'CP': 74, 'Milk': 68, 'BBQ': 30}
l1_s1 = {'OJ': 66, 'CP': 72, 'Milk': 70, 'BBQ': 26}
l1_s2 = {'OJ': 56, 'CP': 76, 'Milk': 70, 'BBQ': 16}
l1_mean = {k: np.mean([l1_s0[k], l1_s1[k], l1_s2[k]]) for k in l1_s0}
l1_std = {k: np.std([l1_s0[k], l1_s1[k], l1_s2[k]], ddof=1) for k in l1_s0}

order = ['CP', 'Milk', 'OJ', 'BBQ']
tasks = ['Choco.\nPudding', 'Milk', 'Orange\nJuice', 'BBQ\nSauce']

cond_labels = [
    r'LoRA-only ($\lambda$=0)',
    r'$\lambda$=0.005',
    r'$\lambda$=0.01',
    r'$\lambda$=0.1',
]

means_arr = np.array([
    [lora_mean[t] for t in order],
    [l005_mean[t] for t in order],
    [l01_mean[t] for t in order],
    [l1_mean[t] for t in order],
])

errs_arr = np.array([
    [lora_std[t] for t in order],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [l1_std[t] for t in order],
])

seed_data = {
    0: {t: [lora_s0[t], lora_s1[t], lora_s2[t]] for t in order},
    3: {t: [l1_s0[t], l1_s1[t], l1_s2[t]] for t in order},
}

colors_fp = ['#A8C8E8', '#5B9BD5', '#2E75B6', '#1B4F72']

n_tasks = len(tasks)
n_conds = len(cond_labels)
bar_width = 0.18
x = np.arange(n_tasks)

for i in range(n_conds):
    offset = (i - (n_conds - 1) / 2) * bar_width
    has_err = any(errs_arr[i] > 0)

    ax2.bar(
        x + offset, means_arr[i], bar_width * 0.88,
        label=cond_labels[i], color=colors_fp[i],
        edgecolor='white', linewidth=0.5,
        yerr=errs_arr[i] if has_err else None,
        capsize=2 if has_err else 0,
        error_kw={'linewidth': 0.9, 'capthick': 0.7, 'color': '#444444'},
        zorder=3,
    )

    if i in seed_data:
        for j, t in enumerate(order):
            pts = seed_data[i][t]
            jx = np.linspace(-bar_width * 0.12, bar_width * 0.12, len(pts))
            for k, pt in enumerate(pts):
                ax2.plot(
                    x[j] + offset + jx[k], pt, 'o',
                    color='white', markersize=2.5,
                    markeredgecolor='#444444', markeredgewidth=0.6,
                    zorder=5,
                )

for i in range(n_conds):
    offset = (i - (n_conds - 1) / 2) * bar_width
    xs_line = x + offset
    ax2.plot(xs_line, means_arr[i], '--', color=colors_fp[i],
             alpha=0.4, linewidth=0.9, zorder=2)

for j in range(n_tasks):
    rank_label = ['1st', '2nd', '3rd', '4th'][j]
    col_max = max(means_arr[:, j]) + max(errs_arr[:, j])
    ax2.text(x[j], col_max + 3.5, rank_label,
             ha='center', va='bottom', fontsize=7, color='#666666',
             fontstyle='italic', fontweight='bold')

ax2.set_ylabel('CAR (%)')
ax2.set_xticks(x)
ax2.set_xticklabels(tasks, fontsize=9)
ax2.set_ylim(0, 90)
ax2.set_xlim(-0.5, n_tasks - 0.5)

ax2.yaxis.grid(True, alpha=0.15, linewidth=0.4, zorder=0)
ax2.set_axisbelow(True)

leg = ax2.legend(
    loc='upper right', framealpha=0.92, edgecolor='#cccccc',
    ncol=2, columnspacing=0.6, handlelength=1.0, fontsize=7,
)
leg.get_frame().set_linewidth(0.4)

# ============================================================
# Save
# ============================================================
plt.tight_layout()
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT.with_suffix('.pdf'), dpi=300)
fig.savefig(OUT.with_suffix('.png'), dpi=300)
plt.close(fig)
print(f'Saved: {OUT.with_suffix(".pdf")} and {OUT.with_suffix(".png")}')
