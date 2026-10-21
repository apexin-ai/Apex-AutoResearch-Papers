"""
Figure 2: Gap Amplification — multi-seed version with bootstrap 95% CI error bars.

Activate when multi-seed data arrives (May 20-21).
Replace gen_fig2_gap_amplification.py output.

Data status:
  Function 4B (5 seeds): gap=1.24, std=0.86 — COMPLETE
  Function 8B (3 seeds): gap=2.43, std=0.37 — COMPLETE (bf16 only)
  Repo 4B (single seed): gap=25.59, no CI — NEEDS MULTI-SEED
  Repo 8B (single seed): gap=19.31, no CI — NEEDS MULTI-SEED

When data arrives, fill in:
  1. repo_4b_gaps = [s42_gap, s123_gap, s456_gap]
  2. repo_8b_gaps = [s42_gap, s123_gap, s456_gap]
  3. Run bootstrap CI computation below
  4. Update errs_lo / errs_hi arrays
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

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
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'text.usetex': False,
})

# ── Bootstrap CI helper ──────────────────────────────────────────────
def bootstrap_ci(values, n_boot=10000, alpha=0.05):
    """Compute bootstrap 95% CI for mean of `values`."""
    rng = np.random.default_rng(42)
    vals = np.array(values)
    means = np.array([rng.choice(vals, size=len(vals), replace=True).mean()
                       for _ in range(n_boot)])
    lo = np.percentile(means, 100 * alpha / 2)
    hi = np.percentile(means, 100 * (1 - alpha / 2))
    return vals.mean(), lo, hi


# ── Data: fill in multi-seed values when available ───────────────────
# Function-level CLS-CWM gaps (per-test accuracy difference, pp)
func_4b_gaps = [0.32, 2.32, 0.31, 2.39, 0.88]  # 5 seeds
func_8b_gaps = [2.81, 2.42, 2.06]                # 3 seeds (bf16)

# Repo-level CLS-CWM gaps — PLACEHOLDER: replace with actual per-seed gaps
# repo_4b_gaps = [25.59, TBD, TBD]  # s42, s123, s456
# repo_8b_gaps = [19.31, TBD, TBD]  # s42, s123, s456
repo_4b_gaps = [25.59]  # single seed — will update
repo_8b_gaps = [19.31]  # single seed — will update

# Compute stats
func_4b_mean, func_4b_lo, func_4b_hi = bootstrap_ci(func_4b_gaps)
func_8b_mean, func_8b_lo, func_8b_hi = bootstrap_ci(func_8b_gaps)

# For single-seed repo data, no CI possible yet
if len(repo_4b_gaps) >= 3:
    repo_4b_mean, repo_4b_lo, repo_4b_hi = bootstrap_ci(repo_4b_gaps)
else:
    repo_4b_mean = np.mean(repo_4b_gaps)
    repo_4b_lo = repo_4b_hi = repo_4b_mean  # no CI

if len(repo_8b_gaps) >= 3:
    repo_8b_mean, repo_8b_lo, repo_8b_hi = bootstrap_ci(repo_8b_gaps)
else:
    repo_8b_mean = np.mean(repo_8b_gaps)
    repo_8b_lo = repo_8b_hi = repo_8b_mean

# ── Plot ─────────────────────────────────────────────────────────────
labels = [
    "Function\n(4B, 5 seeds)",
    "Function\n(8B, 3 seeds)",
    "Repo\n(4B)",
    "Repo\n(8B)",
]
means = [func_4b_mean, func_8b_mean, repo_4b_mean, repo_8b_mean]
errs_lo = [m - lo for m, lo in zip(means,
           [func_4b_lo, func_8b_lo, repo_4b_lo, repo_8b_lo])]
errs_hi = [hi - m for m, hi in zip(means,
           [func_4b_hi, func_8b_hi, repo_4b_hi, repo_8b_hi])]

colors = ['#7FBFDF', '#0072B2', '#CC7722', '#994400']

x = np.arange(len(labels))
bar_width = 0.52

fig = plt.figure(figsize=(5.5, 5.0))
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 2.2], hspace=0.08)

ax_top = fig.add_subplot(gs[0])
ax_bot = fig.add_subplot(gs[1])

for ax in [ax_top, ax_bot]:
    bars = ax.bar(x, means, bar_width, color=colors,
                  edgecolor='white', linewidth=0.5, zorder=3)
    yerr = np.array([errs_lo, errs_hi])
    for i in range(len(means)):
        if errs_lo[i] > 0 or errs_hi[i] > 0:
            ax.errorbar(x[i], means[i],
                        yerr=[[errs_lo[i]], [errs_hi[i]]],
                        fmt='none', ecolor='#333333',
                        capsize=4, capthick=1.2, elinewidth=1.2, zorder=4)

ax_top.set_ylim(15, 32)
ax_bot.set_ylim(0, 5.5)

ax_top.spines['bottom'].set_visible(False)
ax_bot.spines['top'].set_visible(False)
ax_top.tick_params(bottom=False, labelbottom=False)
ax_top.set_xticks([])

ax_bot.set_xticks(x)
ax_bot.set_xticklabels(labels)

# Break marks
d = 0.012
kwargs = dict(transform=ax_top.transAxes, color='k', clip_on=False, linewidth=0.8)
ax_top.plot((-d, +d), (-d*3, +d*3), **kwargs)
kwargs.update(transform=ax_bot.transAxes)
ax_bot.plot((-d, +d), (1-d*3, 1+d*3), **kwargs)

# Value annotations
for i in range(2):
    ax_bot.text(x[i], means[i] + errs_hi[i] + 0.25,
                f'{means[i]:.2f} pp', ha='center', va='bottom',
                fontsize=9.5, fontweight='bold', color=colors[i])
for i in range(2, 4):
    ax_top.text(x[i], means[i] + errs_hi[i] + 0.5,
                f'{means[i]:.1f} pp', ha='center', va='bottom',
                fontsize=9.5, fontweight='bold', color=colors[i])

fig.text(0.01, 0.5, 'CLS − CWM Accuracy Gap (pp)', va='center',
         rotation='vertical', fontsize=12)

ax_top.set_title('Gap Amplification: Function to Repo-Level', pad=10)

for ax in [ax_top, ax_bot]:
    ax.yaxis.grid(True, linestyle='--', alpha=0.3, zorder=0)
    ax.set_axisbelow(True)

ax_top.set_yticks([16, 20, 24, 28, 32])
ax_bot.set_yticks([0, 1, 2, 3, 4, 5])

plt.subplots_adjust(left=0.14, right=0.95)

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/figures/paper'
fig.savefig(f'{out_dir}/fig2_scaling_gap_multiseed.pdf')
fig.savefig(f'{out_dir}/fig2_scaling_gap_multiseed.png')
plt.close()

import os
for ext in ['pdf', 'png']:
    p = f'{out_dir}/fig2_scaling_gap_multiseed.{ext}'
    sz = os.path.getsize(p)
    print(f'{p}: {sz} bytes')
    assert sz > 5000, f'{ext} too small: {sz}'
print('Done. When multi-seed repo data arrives, update repo_Xb_gaps arrays and re-run.')
