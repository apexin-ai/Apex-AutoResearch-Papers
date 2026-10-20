"""
Plot per-feature convergence dynamics with Cohen's d normalization.

Fixes the min-max normalization issue where near-stationary features
(Cohen's d < 0.10) had micro-variance stretched to [0,1].

Y-axis = Cohen's d at each depth relative to depth 0, computed per generator
then averaged. This directly shows effect size: drifting features have large
|d|, near-stationary features stay near 0, matching the paper's narrative.

Classification by Cohen's d (depth 0 vs 4, across all samples):
- Drifting (|d|>0.8): hapax_ratio (2.53), ttr (2.53), entropy_mean (2.28)
- Intermediate (0.2<|d|<0.8): entropy_std (0.40)
- Near-stationary (|d|<0.2): entropy_min (0.10), entropy_max (0.19), tail_decay (0.08)

Input:  features_all_models.csv (37k rows, 8 generators, depths 0-4)
Output: fig_convergence_dynamics.pdf / .png
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

# ── Data ──────────────────────────────────────────────────────────────────
DATA = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/supplement/data/features_all_models.csv'
OUT_DIR = '/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/chart'

df = pd.read_csv(DATA)

features = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max',
            'tail_decay', 'ttr', 'hapax_ratio']

depths = sorted(df['depth'].unique())
generators = sorted(df['model_name'].unique())

# ── Step 1: Cohen's d at each depth relative to depth 0 ──────────────────
# Per generator: d(depth_k) = (mean_k - mean_0) / pooled_sd(k, 0)
# Then average across generators for the plot value; std for error band.

summary = {}
for feat in features:
    feat_data = {}
    for d in depths:
        per_gen_d = []
        for gen in generators:
            # All seed samples for this generator at depth 0 and depth d
            s0 = df[(df['model_name'] == gen) & (df['depth'] == 0)][feat].values
            sd = df[(df['model_name'] == gen) & (df['depth'] == d)][feat].values
            n0, nd = len(s0), len(sd)
            # Pooled std
            pooled_sd = np.sqrt(
                (np.var(s0, ddof=1) * (n0 - 1) + np.var(sd, ddof=1) * (nd - 1))
                / (n0 + nd - 2)
            )
            if pooled_sd > 0:
                cohens_d = (np.mean(sd) - np.mean(s0)) / pooled_sd
            else:
                cohens_d = 0.0
            per_gen_d.append(cohens_d)
        feat_data[d] = (np.mean(per_gen_d), np.std(per_gen_d, ddof=1))
    summary[feat] = feat_data

# ── Feature classification ────────────────────────────────────────────────
drifting = ['hapax_ratio', 'ttr', 'entropy_mean']
intermediate = ['entropy_std']
near_stationary = ['entropy_min', 'entropy_max', 'tail_decay']

# ── Visual config ─────────────────────────────────────────────────────────
COLORS = {
    'hapax_ratio':  '#c0392b',
    'ttr':          '#e74c3c',
    'entropy_mean': '#f1948a',
    'entropy_std':  '#e67e22',
    'entropy_min':  '#2980b9',
    'entropy_max':  '#3498db',
    'tail_decay':   '#85c1e9',
}

MARKERS = {
    'hapax_ratio':  'o',
    'ttr':          's',
    'entropy_mean': '^',
    'entropy_std':  'D',
    'entropy_min':  'v',
    'entropy_max':  'p',
    'tail_decay':   'X',
}

LABELS = {
    'hapax_ratio':  'hapax ratio',
    'ttr':          'TTR',
    'entropy_mean': 'entropy (mean)',
    'entropy_std':  'entropy (std)',
    'entropy_min':  'entropy (min)',
    'entropy_max':  'entropy (max)',
    'tail_decay':   'tail decay',
}

LINESTYLES = {
    'hapax_ratio':  '-',
    'ttr':          '-',
    'entropy_mean': '-',
    'entropy_std':  '--',
    'entropy_min':  ':',
    'entropy_max':  ':',
    'tail_decay':   ':',
}

# ── Exponential fit for drifting features ─────────────────────────────────
def exp_decay(x, a, lam, c):
    return a * np.exp(-lam * x) + c

fit_results = {}
for feat in drifting:
    x = np.array(depths, dtype=float)
    y = np.array([summary[feat][d][0] for d in depths])
    try:
        popt, pcov = curve_fit(exp_decay, x, y, p0=[y[0]-y[-1], 1.0, y[-1]], maxfev=5000)
        fit_results[feat] = {'a': popt[0], 'lambda': popt[1], 'c': popt[2]}
    except Exception:
        fit_results[feat] = None

print("Exponential decay rates (lambda):")
ranked = sorted(
    [(f, fit_results[f]['lambda']) for f in fit_results if fit_results[f]],
    key=lambda x: x[1], reverse=True
)
for feat, lam in ranked:
    print(f"  {feat}: lambda={lam:.3f}")

# ── Plot ──────────────────────────────────────────────────────────────────
fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.25, 4.2),
                                  gridspec_kw={'hspace': 0.32})

def plot_features(ax, feat_list, panel_label, show_fits=False):
    for feat in feat_list:
        x = np.array(depths)
        y = np.array([summary[feat][d][0] for d in depths])
        yerr = np.array([summary[feat][d][1] for d in depths])

        ax.plot(x, y,
                color=COLORS[feat], marker=MARKERS[feat], markersize=4,
                linestyle=LINESTYLES[feat], linewidth=1.2,
                label=LABELS[feat], zorder=3)
        ax.fill_between(x, y - yerr, y + yerr,
                         color=COLORS[feat], alpha=0.15, zorder=2)

    # Fit curves for drifting features
    if show_fits:
        x_smooth = np.linspace(0, 4, 100)
        for feat in drifting:
            if fit_results.get(feat):
                p = fit_results[feat]
                y_fit = exp_decay(x_smooth, p['a'], p['lambda'], p['c'])
                ax.plot(x_smooth, y_fit, color=COLORS[feat],
                        linestyle='-', linewidth=0.6, alpha=0.4, zorder=1)

    ax.axhline(0, color='#888888', linewidth=0.5, linestyle='-', zorder=0)
    ax.set_ylabel("Cohen's $d$ (vs. depth 0)", fontsize=8)
    ax.yaxis.grid(True, alpha=0.3, color='#cccccc', linewidth=0.5)
    ax.set_axisbelow(True)
    ax.tick_params(axis='both', labelsize=7)
    ax.set_xlabel('Generation depth', fontsize=8)
    ax.set_xticks(depths)
    ax.set_xticklabels([str(d) for d in depths])

    # Panel label
    ax.text(0.02, 0.95, panel_label, transform=ax.transAxes,
            fontsize=8, fontweight='bold', va='top')

    leg = ax.legend(fontsize=6.5, loc='best', framealpha=0.85,
                    edgecolor='#cccccc', handlelength=1.8, borderpad=0.3,
                    labelspacing=0.3)
    leg.get_frame().set_linewidth(0.5)

# Panel (a): drifting + intermediate
plot_features(ax_a, drifting + intermediate, '(a)', show_fits=True)

# Panel (b): near-stationary
plot_features(ax_b, near_stationary, '(b)', show_fits=False)

fig.align_ylabels([ax_a, ax_b])

# ── Save ──────────────────────────────────────────────────────────────────
pdf_path = f'{OUT_DIR}/fig_convergence_dynamics.pdf'
png_path = f'{OUT_DIR}/fig_convergence_dynamics.png'

fig.savefig(pdf_path, bbox_inches='tight', dpi=300)
fig.savefig(png_path, bbox_inches='tight', dpi=300)
plt.close(fig)

print(f"\nSaved: {pdf_path}")
print(f"Saved: {png_path}")

# ── Verification ──────────────────────────────────────────────────────────
import os
for p in [pdf_path, png_path]:
    sz = os.path.getsize(p)
    print(f"  {os.path.basename(p)}: {sz:,} bytes")

print("\nVerification - near-stationary Cohen's d at each depth:")
for feat in near_stationary:
    vals = [summary[feat][d][0] for d in depths]
    max_abs = max(abs(v) for v in vals)
    status = "OK (|d|<0.5)" if max_abs < 0.5 else f"max|d|={max_abs:.3f}"
    print(f"  {feat}: d={[f'{v:.3f}' for v in vals]}  {status}")

print("\nVerification - drifting Cohen's d at depth 4:")
for feat in drifting:
    val = summary[feat][4][0]
    status = "OK (|d|>1)" if abs(val) > 1.0 else "WARNING: |d|<1"
    print(f"  {feat}: d={val:.3f} {status}")
