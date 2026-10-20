#!/usr/bin/env python3
"""Detection rate surface over α × T (PermG forward, contour plot).
Uses unified paper_palette and softened colormap matching phase diagram.
Data from dose_response_d120_recompiled.csv."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.colors as mcolors
import numpy as np
import csv
from pathlib import Path
from matplotlib.colors import LinearSegmentedColormap

OUT = Path(__file__).parent
ROOT = Path(__file__).resolve().parents[3]
CSV_PATH = ROOT / 'artifacts' / '_project' / 'data' / 'dose_response_d120_recompiled.csv'

from paper_palette import PERMG, NAIVEXCORR, DIFFXCORR, DARK_TEXT

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
})

# ── Load data ──
with open(CSV_PATH) as f:
    reader = csv.DictReader(f)
    rows = list(reader)

data_points = {}
for r in rows:
    if r['domain'] != 'wikitext' or r['precision'] != 'fp32':
        continue
    if r['model'] != 'gpt2':
        continue
    cat = r['category']
    if cat not in ('alpha_sweep', 't20', 'scale'):
        continue
    a = float(r['alpha'])
    T = int(r['T'])
    n = int(r['n_pairs'])
    det = int(r['permg_fwd_fdr'])
    rate = det / n
    key = (a, T)
    if key not in data_points:
        data_points[key] = []
    data_points[key].append(rate)

grid = {k: np.mean(v) for k, v in data_points.items()}

alphas = sorted(set(k[0] for k in grid.keys()))
T_vals = sorted(set(k[1] for k in grid.keys()))

Z = np.full((len(T_vals), len(alphas)), np.nan)
for (a, t), v in grid.items():
    if a in alphas and t in T_vals:
        Z[T_vals.index(t), alphas.index(a)] = v * 100

# ── Softened colormap (matching phase diagram style) ──
_base = plt.cm.YlOrRd(np.linspace(0.03, 0.80, 256))
_base = _base * 0.92 + 0.08
cmap = LinearSegmentedColormap.from_list('soft_ylorrd_surface', _base)

# ── Figure ──
fig, ax = plt.subplots(figsize=(3.4, 2.8))

A, T = np.meshgrid(alphas, T_vals)
levels = np.linspace(0, 100, 11)
cf = ax.contourf(A, T, Z, levels=levels, cmap=cmap, alpha=0.85)
cs = ax.contour(A, T, Z, levels=[50], colors=[PERMG], linewidths=1.3, linestyles='--')
ax.clabel(cs, fmt='%d%%', fontsize=7, colors=[PERMG])

# Scatter data points
for (a, t), v in grid.items():
    edgecolor = DARK_TEXT if v > 0 else '#888888'
    ax.scatter(a, t, c=[[v * 100]], cmap=cmap, vmin=0, vmax=100,
               s=20, edgecolors=edgecolor, linewidths=0.4, zorder=5)

# α_c(T) theory curve
alpha_c_10 = 0.483
gamma = 1.3
T_theory = np.linspace(5, 25, 200)
alpha_c_T = alpha_c_10 * (10 / T_theory) ** gamma
alpha_c_T = np.clip(alpha_c_T, 0, 1.0)
ax.plot(alpha_c_T, T_theory, '-', color='white', lw=2.2, zorder=6)
ax.plot(alpha_c_T, T_theory, '-', color=PERMG, lw=1.3, zorder=7,
        label=r'$\alpha_c(T)$ boundary')

# Regime labels
ax.text(0.15, 12, 'Blind', fontsize=9, fontweight='bold',
        ha='center', va='center', color=PERMG, alpha=0.7,
        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])
ax.text(0.8, 15, 'Detection', fontsize=9, fontweight='bold',
        ha='center', va='center', color=NAIVEXCORR, alpha=0.8,
        path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

cbar = fig.colorbar(cf, ax=ax, shrink=0.85, aspect=20, pad=0.04)
cbar.set_label('Detection rate (%)', fontsize=8, labelpad=6)
cbar.ax.tick_params(labelsize=7.5, length=2)
cbar.outline.set_linewidth(0.3)
cbar.outline.set_edgecolor('#AAAAAA')

ax.set_xlabel(r'Contamination fraction $\alpha$')
ax.set_ylabel(r'Observation window $T$')
ax.legend(loc='upper left', framealpha=0.92, edgecolor='none',
          handlelength=1.5, borderpad=0.3)

plt.tight_layout()
for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'fig_detection_surface.{fmt}', dpi=300)
plt.close()
print(f'Saved: {OUT}/fig_detection_surface.pdf + .png')
