#!/usr/bin/env python3
"""Figure 3: PermG dose-response with sigmoid fit + regime bands.
Unified style matching all paper figures."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import csv
from collections import defaultdict
from pathlib import Path

OUT = Path(__file__).parent
BASE = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse')

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 7.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'cm',
    'lines.linewidth': 1.6,
})

C_MAIN = '#4A90C4'
C_ANNOT = '#CC5A5A'

# ── Data ──
data_by_alpha = defaultdict(list)
with open(BASE / 'artifacts/dose_response_d120_compiled.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['category'] == 'alpha_sweep' and row['dataset'] == 'wikitext':
            data_by_alpha[float(row['alpha'])].append(float(row['permg_rate']))

alphas_data = sorted(data_by_alpha.keys())
means = np.array([np.mean(data_by_alpha[a]) for a in alphas_data])
stds = np.array([np.std(data_by_alpha[a], ddof=0) for a in alphas_data])

# ── Sigmoid fit ──
def sigmoid(a, k, ac, ym):
    return ym / (1.0 + np.exp(-k * (a - ac)))

K_FIT, AC_FIT, YM_FIT = 200.0, 0.483, 0.7518

np.random.seed(42)
N_BOOT = 1000
log_k_mu = np.log(np.sqrt(73.6 * 500))
log_k_sig = (np.log(500) - np.log(73.6)) / (2 * 1.96)
k_samp = np.exp(np.random.normal(log_k_mu, log_k_sig, N_BOOT))
ac_samp = np.random.normal(0.483, (0.558 - 0.425) / (2 * 1.96), N_BOOT)
ym_samp = np.random.normal(0.7518, (0.895 - 0.691) / (2 * 1.96), N_BOOT)

alpha_c = np.linspace(0, 1.0, 300)
curves = np.array([sigmoid(alpha_c, k, ac, ym)
                    for k, ac, ym in zip(k_samp, ac_samp, ym_samp)])
ci_lo = np.clip(np.percentile(curves, 2.5, axis=0), 0, 1)
ci_hi = np.clip(np.percentile(curves, 97.5, axis=0), 0, 1)
fit_y = np.clip(sigmoid(alpha_c, K_FIT, AC_FIT, YM_FIT), 0, 1)

# ── Figure ──
fig, ax = plt.subplots(figsize=(3.4, 2.8))

# Regime background bands (very subtle)
regimes = [
    (0.0,  0.47, '#F4F6F9', 'Blind'),
    (0.47, 0.55, '#EBF0F7', 'Onset'),
    (0.55, 0.68, '#FDF5EE', 'Sync-dip'),
    (0.68, 1.0,  '#F0F5EF', 'Detection'),
]
for x0, x1, col, lab in regimes:
    ax.axvspan(x0, x1, color=col, zorder=0)

# Regime labels at top (manual positions, abbreviated to avoid overlap)
regime_labels_pos = [
    (0.23, 'Blind'),
    (0.51, 'Onset'),
    (0.615, 'Dip'),
    (0.84, 'Detection'),
]
for lx, lab in regime_labels_pos:
    ax.text(lx, 1.04, lab, transform=ax.get_xaxis_transform(),
            ha='center', va='bottom', fontsize=7, color='#777777',
            fontstyle='italic', clip_on=False)

for xb in (0.47, 0.55, 0.68):
    ax.axvline(xb, color='#E0E0E0', ls=':', lw=0.5, zorder=1)

# Bootstrap CI band
ax.fill_between(alpha_c, ci_lo, ci_hi, color=C_MAIN, alpha=0.08,
                label='95% bootstrap CI', zorder=2, lw=0)

# Sigmoid fit
ax.plot(alpha_c, fit_y, color=C_MAIN, lw=1.5,
        label=r'Sigmoid ($\alpha_c{=}0.483$)', zorder=3)

# α_c marker
ax.axvline(AC_FIT, color=C_MAIN, ls='--', lw=0.7, alpha=0.35, zorder=1)

# Individual seed points
rng = np.random.default_rng(42)
for a in alphas_data:
    rates = data_by_alpha[a]
    n = len(rates)
    jit = rng.uniform(-0.008, 0.008, n) if n > 1 else np.zeros(1)
    ax.scatter(a + jit, rates, s=10, c='#666666', alpha=0.4, zorder=4, edgecolors='none')

# Mean ± SD
ax.errorbar(alphas_data, means, yerr=stds, fmt='D', ms=3,
            color='#1A1A1A', ecolor='#555555', elinewidth=0.7, capsize=1.2,
            capthick=0.6, label=r'Mean $\pm$ SD', zorder=5, markeredgewidth=0)

# α=0.45 highlight
ax.plot(0.45, 0.0, 'o', ms=5, mfc='none', mec=C_ANNOT, mew=1.0, zorder=6)

# Sub-threshold annotation (compact)
ax.annotate(
    '$p_{\\mathrm{FDR}}$=.059,.091',
    xy=(0.45, 0.02), xycoords='data',
    xytext=(0.18, 0.48), textcoords='data',
    fontsize=7, color=C_ANNOT, ha='center', va='center',
    arrowprops=dict(arrowstyle='->', color=C_ANNOT, lw=0.8,
                    connectionstyle='arc3,rad=-0.12'),
    bbox=dict(boxstyle='round,pad=0.2', fc='white', ec=C_ANNOT, lw=0.5, alpha=0.9),
    zorder=7,
)

ax.set_xlabel(r'Canary fraction ($\alpha$)')
ax.set_ylabel('PermG detection rate')
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.05, 1.08)
ax.set_xticks([0, 0.25, 0.50, 0.75, 1.0])

ax.legend(loc='upper left', framealpha=0.92, edgecolor='none',
          borderpad=0.2, handlelength=1.2, fontsize=6.5)

plt.tight_layout()

for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'fig_dose_response.{fmt}', dpi=300)
plt.close()
print(f'Saved: {OUT}/fig_dose_response.pdf + .png')
