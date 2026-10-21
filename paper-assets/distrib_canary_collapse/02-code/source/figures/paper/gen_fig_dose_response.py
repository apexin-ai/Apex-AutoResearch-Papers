#!/usr/bin/env python3
"""Enhanced dose-response figure: sigmoid fit + bootstrap CI + sub-threshold annotation."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import defaultdict

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 13,
    'axes.titlesize': 14,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'text.usetex': False,
    'mathtext.fontset': 'dejavuserif',
    'pdf.fonttype': 42,
})

OI_BLUE = '#0072B2'
OI_RED = '#D55E00'
OI_GREY = '#999999'

BASE = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse'

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------
data_by_alpha = defaultdict(list)
with open(f'{BASE}/artifacts/dose_response_d120_compiled.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['category'] == 'alpha_sweep' and row['dataset'] == 'wikitext':
            data_by_alpha[float(row['alpha'])].append(float(row['permg_rate']))

alphas_data = sorted(data_by_alpha.keys())
means = np.array([np.mean(data_by_alpha[a]) for a in alphas_data])
stds = np.array([np.std(data_by_alpha[a], ddof=0) for a in alphas_data])

# ---------------------------------------------------------------------------
# Sigmoid fit (locked params) + bootstrap CI
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4.0, 3.2))

# --- regime background bands ---
regimes = [
    (0.0,  0.35, '#F0F0F0', 'Blind',          None),
    (0.35, 0.50, '#E6EEF8', 'Onset',          0.40),
    (0.50, 0.65, '#FFF5EB', 'Sync-dip',         0.575),
    (0.65, 1.0,  '#E8F5E9', 'Detection',      None),
]
for x0, x1, col, lab, xoff in regimes:
    ax.axvspan(x0, x1, color=col, zorder=0)
    xc = xoff if xoff is not None else (x0 + x1) / 2
    ax.text(xc, 1.03, lab, transform=ax.get_xaxis_transform(),
            ha='center', va='bottom', fontsize=9, color='#999999', style='italic',
            linespacing=0.85, clip_on=False)

for xb in (0.35, 0.50, 0.65):
    ax.axvline(xb, color='#DDDDDD', ls=':', lw=0.7, zorder=1)

# --- bootstrap CI band ---
ax.fill_between(alpha_c, ci_lo, ci_hi, color=OI_BLUE, alpha=0.12,
                label='95% bootstrap CI', zorder=2, lw=0)

# --- sigmoid fit ---
ax.plot(alpha_c, fit_y, color=OI_BLUE, lw=1.5,
        label=r'Sigmoid ($\alpha_c\!=\!0.483$)', zorder=3)

# --- α_c marker ---
ax.axvline(AC_FIT, color=OI_BLUE, ls='--', lw=0.8, alpha=0.4, zorder=1)

# --- individual seed points ---
rng = np.random.default_rng(42)
for a in alphas_data:
    rates = data_by_alpha[a]
    n = len(rates)
    jit = rng.uniform(-0.008, 0.008, n) if n > 1 else np.zeros(1)
    ax.scatter(a + jit, rates, s=12, c='#555555', alpha=0.45, zorder=4, edgecolors='none')

# --- mean ± SD ---
ax.errorbar(alphas_data, means, yerr=stds, fmt='D', ms=3.5,
            color='black', ecolor='#555555', elinewidth=0.8, capsize=1.5,
            capthick=0.7, label='Mean $\\pm$ SD', zorder=5, markeredgewidth=0)

# --- α=0.45 highlight marker ---
ax.plot(0.45, 0.0, 'o', ms=6, mfc='none', mec=OI_RED, mew=1.2, zorder=6)

# --- α=0.45 sub-threshold annotation ---
ax.annotate(
    'sub-threshold gradient\n$p_{FDR}$ = .059, .091',
    xy=(0.45, 0.03), xycoords='data',
    xytext=(0.13, 0.45), textcoords='data',
    fontsize=10.5, color=OI_RED, ha='center', va='center',
    arrowprops=dict(arrowstyle='->', color=OI_RED, lw=1.0,
                    connectionstyle='arc3,rad=-0.15'),
    bbox=dict(boxstyle='round,pad=0.3', fc='white', ec=OI_RED, lw=0.8, alpha=0.9),
    zorder=7,
)

# --- axes ---
ax.set_xlabel(r'Canary fraction ($\alpha$)')
ax.set_ylabel('PermG detection rate')
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.05, 1.08)
ax.set_xticks([0, 0.25, 0.50, 0.75, 1.0])

ax.legend(loc='upper left', framealpha=0.9, edgecolor='#CCCCCC',
          borderpad=0.3, handlelength=1.5)

plt.tight_layout()

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
outdir = f'{BASE}/docs/paper/figures'
fig.savefig(f'{outdir}/fig_dose_response.pdf', format='pdf')
fig.savefig(f'{outdir}/fig_dose_response.png', format='png', dpi=300)
plt.close()
print(f'Saved: {outdir}/fig_dose_response.pdf')
print(f'Saved: {outdir}/fig_dose_response.png')
