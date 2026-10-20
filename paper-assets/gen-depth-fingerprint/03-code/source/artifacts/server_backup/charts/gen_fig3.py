#!/usr/bin/env python3
"""Fig3: Baseline Comparison — forest plot with bootstrap CI from per-generator LOGO F1."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'mathtext.fontset': 'cm',
})

def bootstrap_ci_from_vals(vals, n_boot=5000, ci=0.95, seed=42):
    rng = np.random.RandomState(seed)
    vals = np.array(vals)
    n = len(vals)
    boot_means = np.array([np.mean(rng.choice(vals, n, replace=True)) for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    return np.mean(vals), np.percentile(boot_means, 100*alpha), np.percentile(boot_means, 100*(1-alpha))

with open('/root/gen-depth-fingerprint/data/cross_generator_results.json') as f:
    cg_data = json.load(f)
with open('/root/gen-depth-fingerprint/data/detector_baseline_results.json') as f:
    det_data = json.load(f)

logo = cg_data['leave_one_generator_out']

# Per-generator LOGO F1 values
ens_pg = [logo[g]['macro_f1'] for g in logo if isinstance(logo[g], dict) and 'macro_f1' in logo[g]]
logprob_pg = list(det_data['log_likelihood']['per_generator'].values())
fdgpt_pg = list(det_data['fast_detect_gpt']['per_generator'].values())

# Bootstrap CIs from per-generator values
ens_mean, ens_lo, ens_hi = bootstrap_ci_from_vals(ens_pg)
lp_mean, lp_lo, lp_hi = bootstrap_ci_from_vals(logprob_pg)
fd_mean, fd_lo, fd_hi = bootstrap_ci_from_vals(fdgpt_pg)

methods = [
    '7-Feature Ensemble (Ours)',
    'Avg Log-Prob',
    'FastDetectGPT',
]
points = np.array([ens_mean, lp_mean, fd_mean])
ci_los = np.array([ens_lo, lp_lo, fd_lo])
ci_his = np.array([ens_hi, lp_hi, fd_hi])
gen_mins = np.array([min(ens_pg), min(logprob_pg), min(fdgpt_pg)])
gen_maxs = np.array([max(ens_pg), max(logprob_pg), max(fdgpt_pg)])

n = len(methods)
y_pos = np.arange(n)[::-1]

colors = ['#0072B2', '#E69F00', '#D55E00']

fig, ax = plt.subplots(figsize=(5.0, 1.8))

for i in range(n):
    ax.hlines(y_pos[i], gen_mins[i], gen_maxs[i], color=colors[i],
              linewidth=0.8, alpha=0.35, zorder=1)
    ax.plot([gen_mins[i], gen_maxs[i]], [y_pos[i], y_pos[i]], '|',
            color=colors[i], markersize=5, alpha=0.5, zorder=1)

    ax.hlines(y_pos[i], ci_los[i], ci_his[i], color=colors[i],
              linewidth=2.5, zorder=2)

    marker = 'D' if i == 0 else 'o'
    ms = 6 if i == 0 else 5
    ax.plot(points[i], y_pos[i], marker=marker, color=colors[i], markersize=ms,
            markeredgecolor='white', markeredgewidth=0.6, zorder=3)

    ax.text(max(gen_maxs[i], ci_his[i]) + 0.005, y_pos[i],
            f'{points[i]:.3f}', va='center', ha='left', fontsize=7,
            fontweight='bold', color=colors[i])

ax.set_yticks(y_pos)
ax.set_yticklabels(methods)
ax.set_xlabel('LOGO Macro-F1')
ax.set_xlim(0.55, 0.90)
ax.set_ylim(-0.5, n - 0.5)

ax.axvline(x=points[0], color='#0072B2', linestyle=':', linewidth=0.5, alpha=0.3, zorder=0)

ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', length=0)

from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='gray', linewidth=2.5, label='Bootstrap 95% CI'),
    Line2D([0], [0], color='gray', linewidth=0.8, alpha=0.4, label='Per-generator range'),
]
ax.legend(handles=legend_elements, loc='lower right', frameon=True, fancybox=False,
          edgecolor='#cccccc', framealpha=0.9, fontsize=6.5)

plt.tight_layout()

outdir = '/root/gen-depth-fingerprint/charts'
fig.savefig(f'{outdir}/fig3_baseline_comparison.png', dpi=300, facecolor='white')
fig.savefig(f'{outdir}/fig3_baseline_comparison.pdf', facecolor='white')
print(f'Saved fig3 to {outdir}/fig3_baseline_comparison.{{png,pdf}}')

fig.savefig('/root/gen-depth-fingerprint/figures/paper/fig3_baseline_comparison.png', dpi=300, facecolor='white')
fig.savefig('/root/gen-depth-fingerprint/figures/paper/fig3_baseline_comparison.pdf', facecolor='white')
print('Also saved to figures/paper/')

print(f'\nMethod comparison (100% data, 6-gen LOGO):')
for m, p, lo, hi, glo, ghi in zip(methods, points, ci_los, ci_his, gen_mins, gen_maxs):
    print(f'  {m}: {p:.4f} CI=[{lo:.4f}, {hi:.4f}] gen-range=[{glo:.4f}, {ghi:.4f}]')
print(f'\nPer-generator F1 (ensemble):')
for g in sorted(logo.keys()):
    if isinstance(logo[g], dict) and 'macro_f1' in logo[g]:
        print(f'  {g}: {logo[g]["macro_f1"]:.4f}')

plt.close()
