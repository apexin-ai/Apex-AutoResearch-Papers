#!/usr/bin/env python3
"""Figure 3: Baseline Comparison — forest plot with bootstrap CI + per-generator spread."""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 8,
    'legend.fontsize': 6.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'mathtext.fontset': 'cm',
})

with open('/root/gen-depth-fingerprint/data/plan015_bootstrap_ci.json') as f:
    ci_data = json.load(f)
with open('/root/gen-depth-fingerprint/data/detector_baseline_results.json') as f:
    det_data = json.load(f)
with open('/root/gen-depth-fingerprint/data/cross_generator_results.json') as f:
    cg_data = json.load(f)

logo = cg_data['leave_one_generator_out']

methods = []
points = []
ci_los = []
ci_his = []
gen_mins = []
gen_maxs = []

# 1) 7-Feature Ensemble (ours) — per-generator from LOGO
d = ci_data['seven_feature_logo_f1']
pg_vals = [logo[g]["macro_f1"] for g in logo if isinstance(logo[g], dict)]
methods.append('7-Feature Ensemble (Ours)')
points.append(d['point'])
ci_los.append(d['ci_95'][0])
ci_his.append(d['ci_95'][1])
gen_mins.append(min(pg_vals))
gen_maxs.append(max(pg_vals))

# 2) Avg Log-Prob
d = ci_data['avg_logprob_logo_f1']
pg = det_data['log_likelihood']['per_generator']
methods.append('Avg Log-Prob')
points.append(d['point'])
ci_los.append(d['ci_95'][0])
ci_his.append(d['ci_95'][1])
gen_mins.append(min(pg.values()))
gen_maxs.append(max(pg.values()))

# 3) FastDetectGPT
d = ci_data['fastdetectgpt_logo_f1']
pg = det_data['fast_detect_gpt']['per_generator']
methods.append('FastDetectGPT')
points.append(d['point'])
ci_los.append(d['ci_95'][0])
ci_his.append(d['ci_95'][1])
gen_mins.append(min(pg.values()))
gen_maxs.append(max(pg.values()))

# 4) Entropy Mean (single feature)
d_em = det_data['entropy_mean']
pg = d_em['per_generator']
methods.append('Entropy Mean (single)')
points.append(d_em['logo_macro_f1'])
ci_los.append(d_em['logo_f1_ci'][0])
ci_his.append(d_em['logo_f1_ci'][1])
gen_mins.append(min(pg.values()))
gen_maxs.append(max(pg.values()))

points = np.array(points)
ci_los = np.array(ci_los)
ci_his = np.array(ci_his)
gen_mins = np.array(gen_mins)
gen_maxs = np.array(gen_maxs)

n = len(methods)
y_pos = np.arange(n)[::-1]

colors = ['#0072B2', '#E69F00', '#D55E00', '#009E73']

fig, ax = plt.subplots(figsize=(5.0, 2.2))

for i in range(n):
    # Per-generator spread (thin, light)
    ax.hlines(y_pos[i], gen_mins[i], gen_maxs[i], color=colors[i],
              linewidth=0.8, alpha=0.35, zorder=1)
    ax.plot([gen_mins[i], gen_maxs[i]], [y_pos[i], y_pos[i]], '|',
            color=colors[i], markersize=5, alpha=0.5, zorder=1)

    # Bootstrap 95% CI (thick)
    ax.hlines(y_pos[i], ci_los[i], ci_his[i], color=colors[i],
              linewidth=2.5, zorder=2)

    # Point estimate
    marker = 'D' if i == 0 else 'o'
    ms = 6 if i == 0 else 5
    ax.plot(points[i], y_pos[i], marker=marker, color=colors[i], markersize=ms,
            markeredgecolor='white', markeredgewidth=0.6, zorder=3)

    # Annotation
    ax.text(max(gen_maxs[i], ci_his[i]) + 0.005, y_pos[i],
            f'{points[i]:.3f}',
            va='center', ha='left', fontsize=7, fontweight='bold', color=colors[i])

ax.set_yticks(y_pos)
ax.set_yticklabels(methods)
ax.set_xlabel('LOGO Macro-F1')
ax.set_xlim(0.50, 0.90)
ax.set_ylim(-0.5, n - 0.5)

# Reference line at ensemble value
ax.axvline(x=points[0], color='#0072B2', linestyle=':', linewidth=0.5, alpha=0.3, zorder=0)

ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', length=0)

# Legend for CI types
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='gray', linewidth=2.5, label='Bootstrap 95% CI'),
    Line2D([0], [0], color='gray', linewidth=0.8, alpha=0.4, label='Per-generator range'),
]
ax.legend(handles=legend_elements, loc='lower right', frameon=True, fancybox=False,
          edgecolor='#cccccc', framealpha=0.9)

plt.tight_layout()

outdir = Path('/root/gen-depth-fingerprint/figures/paper')
fig.savefig(outdir / 'fig3_baseline_comparison.png', dpi=300, facecolor='white')
fig.savefig(outdir / 'fig3_baseline_comparison.pdf', facecolor='white')
print(f'Saved fig3 to {outdir}/fig3_baseline_comparison.{{png,pdf}}')

print('\nMethod comparison:')
for m, p, lo, hi, glo, ghi in zip(methods, points, ci_los, ci_his, gen_mins, gen_maxs):
    print(f'  {m}: {p:.4f} CI=[{lo:.4f}, {hi:.4f}] gen-range=[{glo:.4f}, {ghi:.4f}]')

skipped = det_data.get('skipped_detectors', {})
if skipped:
    print('\nSkipped detectors (no data available):')
    for k, v in skipped.items():
        print(f'  {k}: {v}')

plt.close()
