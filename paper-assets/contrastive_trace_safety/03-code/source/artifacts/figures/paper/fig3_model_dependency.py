import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

COLOR_HS = '#0072B2'
COLOR_TEXT = '#E69F00'

# Load data
with open('/root/autodl-tmp/contrastive_trace_safety/artifacts/r1_8b_bootstrap_hs_text/results.json') as f:
    r1_8b = json.load(f)
with open('/root/autodl-tmp/contrastive_trace_safety/artifacts/qwq_text_verify/bootstrap_results.json') as f:
    qwq = json.load(f)
with open('/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_001a/bootstrap_hs_vs_text_fpr.json') as f:
    r1_32b = json.load(f)

# Extract per-trace FPRs
data = {
    'r1-8b': {
        'hs': np.array(r1_8b['per_trace_hs_fprs']),
        'text': np.array(r1_8b['per_trace_text_fprs']),
        'hs_mean': r1_8b['hs_precp_fpr_mean'],
        'text_mean': r1_8b['text_precp_fpr_mean'],
    },
    'QwQ-32B': {
        'hs': np.array(qwq['per_trace_hs_fprs']),
        'text': np.array(qwq['per_trace_text_fprs']),
        'hs_mean': qwq['hs_precp_fpr_mean'],
        'text_mean': qwq['text_precp_fpr_mean'],
    },
    'R1-32B': {
        'hs': np.array(r1_32b['per_trace_hs_fprs']),
        'text': np.array(r1_32b['per_trace_text_fprs']),
        'hs_mean': r1_32b['hs_temporal_precp_fpr'],
        'text_mean': r1_32b['text_temporal_precp_fpr'],
    },
}

# Bootstrap 95% CI
def bootstrap_ci(arr, n_boot=2000, seed=42):
    rng = np.random.default_rng(seed)
    n = len(arr)
    means = np.array([rng.choice(arr, size=n, replace=True).mean() for _ in range(n_boot)])
    ci_low, ci_high = np.percentile(means, [2.5, 97.5])
    return ci_low, ci_high

models = ['r1-8b', 'QwQ-32B', 'R1-32B']
hs_means = []
text_means = []
hs_ci_lower = []
hs_ci_upper = []
text_ci_lower = []
text_ci_upper = []

for m in models:
    d = data[m]
    hs_m = d['hs_mean'] * 100
    text_m = d['text_mean'] * 100
    hs_means.append(hs_m)
    text_means.append(text_m)

    hs_lo, hs_hi = bootstrap_ci(d['hs'])
    text_lo, text_hi = bootstrap_ci(d['text'])

    hs_ci_lower.append(hs_m - hs_lo * 100)
    hs_ci_upper.append(hs_hi * 100 - hs_m)
    text_ci_lower.append(text_m - text_lo * 100)
    text_ci_upper.append(text_hi * 100 - text_m)

hs_err = np.array([hs_ci_lower, hs_ci_upper])
text_err = np.array([text_ci_lower, text_ci_upper])

x = np.arange(len(models))
width = 0.32

fig, ax = plt.subplots(figsize=(5.5, 4.1))

bars_hs = ax.bar(x - width/2, hs_means, width, yerr=hs_err,
                 color=COLOR_HS, edgecolor='white', linewidth=0.5,
                 capsize=4, error_kw={'linewidth': 1.2}, label='Hidden States', zorder=3)
bars_text = ax.bar(x + width/2, text_means, width, yerr=text_err,
                   color=COLOR_TEXT, edgecolor='white', linewidth=0.5,
                   capsize=4, error_kw={'linewidth': 1.2}, label='Text', zorder=3)

ax.set_xlabel('Model')
ax.set_ylabel('Pre-CP FPR (trace-level, %)')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.set_ylim(0, 40)
ax.set_yticks(np.arange(0, 36, 5))
ax.yaxis.grid(True, alpha=0.3, linestyle='--', zorder=0)

ax.legend(ncol=2, loc='upper center', framealpha=0.9)

# Bracket + p-value for r1-8b
bracket_y = max(hs_means[0] + hs_err[1][0], text_means[0] + text_err[1][0]) + 2.0
ax.plot([x[0] - width/2, x[0] - width/2, x[0] + width/2, x[0] + width/2],
        [bracket_y - 0.6, bracket_y, bracket_y, bracket_y - 0.6],
        color='#333333', linewidth=0.8, zorder=4)
ax.text(x[0], bracket_y + 0.8, '$p$=0.044 *', ha='center', va='bottom',
        fontsize=9, fontstyle='italic', color='#333333')

# Delta annotation for r1-8b
delta_pp = text_means[0] - hs_means[0]
mid_x = x[0] + width/2 + 0.18
ax.plot([mid_x, mid_x], [hs_means[0], text_means[0]], 'k--', linewidth=0.8, zorder=4)
ax.plot([mid_x - 0.03, mid_x + 0.03], [hs_means[0], hs_means[0]], 'k-', linewidth=0.8, zorder=4)
ax.plot([mid_x - 0.03, mid_x + 0.03], [text_means[0], text_means[0]], 'k-', linewidth=0.8, zorder=4)
ax.text(mid_x + 0.06, (hs_means[0] + text_means[0]) / 2,
        r'$\Delta$={:.1f}pp'.format(delta_pp),
        ha='left', va='center', fontsize=8.5)

# n.s. annotations for QwQ-32B and R1-32B
for i in [1, 2]:
    top_y = max(hs_means[i] + hs_err[1][i], text_means[i] + text_err[1][i]) + 1.5
    ax.text(x[i], top_y + 0.5, 'n.s.', ha='center', va='bottom',
            fontsize=9, color='0.4')

plt.tight_layout()

import os
out_dir = '/root/autodl-tmp/contrastive_trace_safety/artifacts/figures/paper'
os.makedirs(out_dir, exist_ok=True)
out_base = os.path.join(out_dir, 'fig3_model_dependency')
fig.savefig(out_base + '.pdf')
fig.savefig(out_base + '.png', dpi=300)
plt.close()

print(f"HS means: {hs_means}")
print(f"Text means: {text_means}")
print(f"HS CI (lower, upper): {list(zip(hs_ci_lower, hs_ci_upper))}")
print(f"Text CI (lower, upper): {list(zip(text_ci_lower, text_ci_upper))}")
print(f"Delta r1-8b: {delta_pp:.1f}pp")
print("Done. Saved to", out_dir)
