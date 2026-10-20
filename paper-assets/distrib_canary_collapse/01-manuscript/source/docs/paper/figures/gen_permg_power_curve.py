#!/usr/bin/env python3
"""Figure A.1: PermG detection power curves.
Unified style with project palette."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import json
from pathlib import Path

OUT = Path(__file__).parent
DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/permg_power_analysis.json')

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'mathtext.fontset': 'cm',
    'lines.linewidth': 1.4,
})

with open(DATA) as f:
    d = json.load(f)

betas = sorted(d['config']['betas'])
T_values = d['config']['T_values']

# Color gradient for T values (light → dark blue)
T_COLORS = {
    6:  '#A6CEE3',
    8:  '#6BAED6',
    10: '#2166AC',
    15: '#1B4A7A',
    20: '#0D2D4F',
}
T_MARKERS = {6: 'o', 8: 's', 10: 'D', 15: '^', 20: 'v'}

def extract_power(matrix, T_val, betas):
    T_key = f'T={T_val}'
    vals = []
    for b in betas:
        b_key = f'beta={b:.2f}'
        vals.append(matrix.get(T_key, {}).get(b_key, 0.0))
    return np.array(vals)

fig, (ax_raw, ax_fdr, ax_theory) = plt.subplots(
    1, 3, figsize=(7.2, 2.8),
    gridspec_kw={'width_ratios': [1, 1, 0.85], 'wspace': 0.38}
)

# ═══ Panel (a): Raw Power ═══
for T in T_values:
    power = extract_power(d['power_matrix_raw'], T, betas)
    ax_raw.plot(betas, power, '-', color=T_COLORS[T], marker=T_MARKERS[T],
                markersize=3, markeredgewidth=0, label=f'$T={T}$', zorder=3)

ax_raw.axhline(0.80, color='#999999', linestyle='--', linewidth=0.8, alpha=0.5, zorder=1)
t = ax_raw.text(0.05, 0.82, '80% power', fontsize=6.5, color='#777777',
                va='bottom', fontstyle='italic')
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

ax_raw.set_xlabel(r'Signal strength ($\beta$)')
ax_raw.set_ylabel('Detection rate')
ax_raw.set_xlim(-0.05, 2.05)
ax_raw.set_ylim(-0.03, 1.05)
ax_raw.text(-0.18, 1.05, '(a)', transform=ax_raw.transAxes,
            fontsize=10, fontweight='bold', va='bottom')
ax_raw.set_title('Raw power ($p<0.05$)', fontsize=9, pad=4)
ax_raw.legend(loc='lower right', framealpha=0.92, edgecolor='none',
              handlelength=1.5, borderpad=0.25, ncol=1)

# ═══ Panel (b): FDR-adjusted Power ═══
for T in T_values:
    power = extract_power(d['power_matrix'], T, betas)
    ax_fdr.plot(betas, power, '-', color=T_COLORS[T], marker=T_MARKERS[T],
                markersize=3, markeredgewidth=0, label=f'$T={T}$', zorder=3)

ax_fdr.axhline(0.80, color='#999999', linestyle='--', linewidth=0.8, alpha=0.5, zorder=1)

ax_fdr.set_xlabel(r'Signal strength ($\beta$)')
ax_fdr.set_xlim(-0.05, 2.05)
ax_fdr.set_ylim(-0.03, 1.05)
ax_fdr.text(-0.14, 1.05, '(b)', transform=ax_fdr.transAxes,
            fontsize=10, fontweight='bold', va='bottom')
ax_fdr.set_title('FDR-adjusted (BH $q{=}0.05$, 8 pairs)', fontsize=9, pad=4)

# ═══ Panel (c): β₅₀ scaling ═══
beta_50_raw = d['beta_50']
T_valid_raw, b50_raw = [], []
T_valid_fdr, b50_fdr = [], []

for T in T_values:
    T_key = f'T={T}'
    raw_val = beta_50_raw[T_key]['raw']
    fdr_val = beta_50_raw[T_key]['fdr8']
    if raw_val is not None:
        T_valid_raw.append(T)
        b50_raw.append(raw_val)
    if fdr_val is not None:
        T_valid_fdr.append(T)
        b50_fdr.append(fdr_val)

inv_sqrt_T_raw = [1.0 / np.sqrt(T) for T in T_valid_raw]
inv_sqrt_T_fdr = [1.0 / np.sqrt(T) for T in T_valid_fdr]

ax_theory.plot(inv_sqrt_T_raw, b50_raw, 'o-', color='#2166AC', markersize=5,
               markeredgewidth=0, label='Raw', zorder=3)
ax_theory.plot(inv_sqrt_T_fdr, b50_fdr, 's-', color='#6BAED6', markersize=5,
               markeredgewidth=0, label='FDR8', zorder=3)

# Reference line β₅₀ ∝ 1/√T
x_ref = np.linspace(0.15, 0.42, 50)
slope = b50_raw[-1] / inv_sqrt_T_raw[-1] if inv_sqrt_T_raw else 3.0
ax_theory.plot(x_ref, slope * x_ref, ':', color='#999999', linewidth=0.8, zorder=1)
t = ax_theory.text(0.36, slope * 0.36 + 0.05, r'$\beta_{50}\propto 1/\sqrt{T}$',
                   fontsize=7, color='#999999', fontstyle='italic', ha='center')
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

# Label T values (offset to avoid overlap)
T_label_offsets = {8: (0.015, 0.06), 10: (0.015, 0.06), 15: (0.015, 0.04), 20: (0.015, 0.04)}
for T, x, y in zip(T_valid_raw, inv_sqrt_T_raw, b50_raw):
    ox, oy = T_label_offsets.get(T, (0.012, 0.04))
    t_label = ax_theory.text(x + ox, y + oy, str(T),
                             fontsize=6, color='#2166AC', va='bottom', ha='center')
    t_label.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

ax_theory.set_xlabel(r'$1/\sqrt{T}$')
ax_theory.set_ylabel(r'$\beta_{50}$')
ax_theory.text(-0.22, 1.05, '(c)', transform=ax_theory.transAxes,
               fontsize=10, fontweight='bold', va='bottom')
ax_theory.set_title(r'$\beta_{50} \propto 1/\sqrt{T}$ scaling', fontsize=9, pad=4)
ax_theory.legend(loc='upper left', framealpha=0.92, edgecolor='none',
                 handlelength=1.5, borderpad=0.25)

fig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.86, wspace=0.40)

for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'permg_power_curve.{fmt}', dpi=300)
plt.close()
print(f'Saved: {OUT}/permg_power_curve.pdf + .png')
