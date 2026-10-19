import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

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
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.7,
})

# === Data from paper Table 8 (appendix.tex, tab:per_task_car) ===
# Per-task CAR (%) at 30K steps, rotation-fixed evaluation

# LoRA-only: s0, s1, s2 individual data (3-seed)
lora_s0 = {'CP': 74, 'Milk': 70, 'OJ': 56, 'BBQ': 26}
lora_s1 = {'CP': 68, 'Milk': 72, 'OJ': 54, 'BBQ': 16}
lora_s2 = {'CP': 76, 'Milk': 62, 'OJ': 56, 'BBQ': 26}
lora_mean = {k: np.mean([lora_s0[k], lora_s1[k], lora_s2[k]]) for k in lora_s0}
lora_std = {k: np.std([lora_s0[k], lora_s1[k], lora_s2[k]], ddof=1) for k in lora_s0}

# lambda=0.005: 3-seed means
l005_mean = {'OJ': 54.0, 'CP': 72.7, 'Milk': 71.3, 'BBQ': 20.0}

# lambda=0.01: 3-seed means
l01_mean = {'OJ': 57.3, 'CP': 72.7, 'Milk': 72.0, 'BBQ': 23.3}

# lambda=0.1: s0, s1, s2 individual data (3-seed)
l1_s0 = {'OJ': 60, 'CP': 74, 'Milk': 68, 'BBQ': 30}
l1_s1 = {'OJ': 66, 'CP': 72, 'Milk': 70, 'BBQ': 26}
l1_s2 = {'OJ': 56, 'CP': 76, 'Milk': 70, 'BBQ': 16}
l1_mean = {k: np.mean([l1_s0[k], l1_s1[k], l1_s2[k]]) for k in l1_s0}
l1_std = {k: np.std([l1_s0[k], l1_s1[k], l1_s2[k]], ddof=1) for k in l1_s0}

# Display order: descending mean CAR
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

# Color palette: muted blue gradient (lighter=lower lambda)
colors = ['#A8C8E8', '#5B9BD5', '#2E75B6', '#1B4F72']

n_tasks = len(tasks)
n_conds = len(cond_labels)
bar_width = 0.18
x = np.arange(n_tasks)

fig, ax = plt.subplots(figsize=(4, 3.5))

for i in range(n_conds):
    offset = (i - (n_conds - 1) / 2) * bar_width
    has_err = any(errs_arr[i] > 0)

    ax.bar(
        x + offset, means_arr[i], bar_width * 0.88,
        label=cond_labels[i], color=colors[i],
        edgecolor='white', linewidth=0.5,
        yerr=errs_arr[i] if has_err else None,
        capsize=2 if has_err else 0,
        error_kw={'linewidth': 0.9, 'capthick': 0.7, 'color': '#444444'},
        zorder=3,
    )

    # Overlay individual seed dots
    if i in seed_data:
        for j, t in enumerate(order):
            pts = seed_data[i][t]
            jx = np.linspace(-bar_width * 0.12, bar_width * 0.12, len(pts))
            for k, pt in enumerate(pts):
                ax.plot(
                    x[j] + offset + jx[k], pt, 'o',
                    color='white', markersize=2.5,
                    markeredgecolor='#444444', markeredgewidth=0.6,
                    zorder=5,
                )

# Dashed connectors across tasks for each condition (shows shape consistency)
for i in range(n_conds):
    offset = (i - (n_conds - 1) / 2) * bar_width
    xs_line = x + offset
    ax.plot(xs_line, means_arr[i], '--', color=colors[i],
            alpha=0.4, linewidth=0.9, zorder=2)

# Rank labels above each task group
for j in range(n_tasks):
    rank_label = ['1st', '2nd', '3rd', '4th'][j]
    col_max = max(means_arr[:, j]) + max(errs_arr[:, j])
    ax.text(x[j], col_max + 3.5, rank_label,
            ha='center', va='bottom', fontsize=7, color='#666666',
            fontstyle='italic', fontweight='bold')

ax.set_ylabel('CAR (%)')
ax.set_xticks(x)
ax.set_xticklabels(tasks, fontsize=9)
ax.set_ylim(0, 90)
ax.set_xlim(-0.5, n_tasks - 0.5)

ax.yaxis.grid(True, alpha=0.15, linewidth=0.4, zorder=0)
ax.set_axisbelow(True)

leg = ax.legend(
    loc='upper right', framealpha=0.92, edgecolor='#cccccc',
    ncol=2, columnspacing=0.6, handlelength=1.0, fontsize=8,
)
leg.get_frame().set_linewidth(0.4)

ax.text(
    0.01, -0.13,
    r'LoRA-only: 3-seed mean (dots = seeds); '
    r'$\lambda$=0.005 & $\lambda$=0.01: 3-seed mean; '
    r'$\lambda$=0.1: 3-seed mean (dots = seeds).',
    transform=ax.transAxes, fontsize=6.5, color='#888888', va='top',
)

plt.tight_layout(pad=1.0)

from pathlib import Path
outdir = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/'
              'diff_collision_sdf/artifacts/figures')
outdir.mkdir(parents=True, exist_ok=True)
for ext in ('pdf', 'png'):
    plt.savefig(outdir / f'fig_pertask_car_fingerprint.{ext}')
print(f'Saved to {outdir}/fig_pertask_car_fingerprint.pdf and .png')

print('\n=== Data summary ===')
for i, label in enumerate(cond_labels):
    print(f'{label}: {dict(zip(order, means_arr[i]))}')
