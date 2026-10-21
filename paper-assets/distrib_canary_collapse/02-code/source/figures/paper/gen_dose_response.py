#!/usr/bin/env python3
"""Dose-response figure: Single panel — PermG fwd detection rate with 4-regime bands.
Data format: fraction strings like '6/8'."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'lines.linewidth': 1.8,
})

def parse_frac(s):
    s = s.strip()
    if '/' in s:
        num, den = s.split('/')
        return int(num) / int(den)
    return float(s)

csv_path = sys.argv[1] if len(sys.argv) > 1 else 'dose_response_5method_regime.csv'
out_dir = sys.argv[2] if len(sys.argv) > 2 else '.'

rows = []
with open(csv_path) as f:
    reader = csv.DictReader(f)
    for r in reader:
        if 'RUNNING' in str(r.get('regime', '')):
            continue
        rows.append(r)

alphas = np.array([float(r['alpha']) for r in rows])

# Try both possible column names
permG_col = 'permG_fwd' if 'permG_fwd' in rows[0] else 'permG_fwd_rate'
permG = np.array([parse_frac(r[permG_col]) for r in rows])
regimes = [r['regime'] for r in rows]

n = len(alphas)
x_idx = np.arange(n)
alpha_labels = [f'{a:.2f}' for a in alphas]

regime_map = {}
for i, reg in enumerate(regimes):
    regime_map.setdefault(reg, []).append(i)

fig, ax = plt.subplots(figsize=(7.0, 3.2))

# 4-regime background bands
blind_indices = regime_map.get('blind_zone', regime_map.get('null', []))
onset_indices = regime_map.get('onset', [])
sync_indices = regime_map.get('sync_collapse', [])
det_indices = regime_map.get('detection', [])

band_specs = []
if blind_indices:
    band_specs.append((min(blind_indices)-0.5, max(blind_indices)+0.5, '#FDEDEC', 'Blind spot\n(α ≤ 0.40)'))
if onset_indices:
    band_specs.append((min(onset_indices)-0.5, max(onset_indices)+0.5, '#FEF9E7', 'Onset'))
if sync_indices:
    band_specs.append((min(sync_indices)-0.5, max(sync_indices)+0.5, '#F4ECF7', 'Sync.\ncollapse'))
if det_indices:
    band_specs.append((min(det_indices)-0.5, max(det_indices)+0.5, '#EBF5FB', 'Detection\nzone'))

for lo, hi, color, label in band_specs:
    ax.axvspan(lo, hi, alpha=0.3, color=color, zorder=0)
    mid = (lo + hi) / 2
    ax.text(mid, 108, label, va='bottom', ha='center', fontsize=7.5,
            color='#555555', fontstyle='italic')

# Main PermG line
ax.plot(x_idx, permG * 100, 'o-', color='#0072B2', markersize=8,
        markerfacecolor='#0072B2', markeredgecolor='white', markeredgewidth=1.2,
        zorder=5, label='PermG fwd')

# Highlight α=0.60 dip
idx_060 = [i for i, a in enumerate(alphas) if abs(a - 0.60) < 0.01]
if idx_060:
    i = idx_060[0]
    ax.plot(x_idx[i], permG[i] * 100, 'D', color='#D55E00', markersize=11,
            markeredgecolor='white', markeredgewidth=1.2, zorder=6)
    ax.annotate(f'{permG[i]*100:.1f}%\n(sync. collapse)',
                xy=(x_idx[i], permG[i]*100),
                xytext=(x_idx[i]+1.2, permG[i]*100 + 18),
                fontsize=8.5, color='#D55E00',
                arrowprops=dict(arrowstyle='->', color='#D55E00', lw=1.0))

# Annotate α=0.50 onset
idx_050 = [i for i, a in enumerate(alphas) if abs(a - 0.50) < 0.01]
if idx_050:
    i = idx_050[0]
    ax.annotate(f'{permG[i]*100:.1f}%\n(onset)',
                xy=(x_idx[i], permG[i]*100),
                xytext=(x_idx[i]-1.8, permG[i]*100 + 15),
                fontsize=8.5, color='#0072B2',
                arrowprops=dict(arrowstyle='->', color='#0072B2', lw=1.0))

ax.set_xticks(x_idx)
ax.set_xticklabels(alpha_labels)
ax.set_xlabel('Contamination level (α)')
ax.set_ylabel('Detection rate (%)')
ax.set_ylim(-5, 125)
ax.set_xlim(-0.5, n - 0.5)
ax.legend(loc='upper left', framealpha=0.9)
ax.grid(True, alpha=0.15, zorder=1)

plt.tight_layout()

pdf_path = os.path.join(out_dir, 'fig_dose_response.pdf')
png_path = os.path.join(out_dir, 'fig_dose_response.png')
plt.savefig(pdf_path)
plt.savefig(png_path)
plt.close()
print(f'Saved: {pdf_path}')
print(f'Saved: {png_path}')
