#!/usr/bin/env python3
"""Figure A.2: Shapley method contribution analysis.
Unified style with project palette."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import json
from pathlib import Path

OUT = Path(__file__).parent
DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json')

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
    'font.size': 9,
    'axes.labelsize': 10,
    'xtick.labelsize': 8,
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

with open(DATA) as f:
    d = json.load(f)

sv = d['main_result_6pair']

methods_raw = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']
labels = ['Naive\nXCorr', 'Diff\nXCorr', 'Thresh.\nOnset', 'Perm\nGranger', 'TY\nGranger']

fpr_vals = [sv['fpr_shapley'][m] for m in methods_raw]
fnr_vals = [sv['fnr_shapley'][m] for m in methods_raw]
comb_vals = [sv['combined_shapley'][m] for m in methods_raw]

# Method colors: PermG highlighted as the champion
METHOD_COLORS = {
    'naive_xcorr':     '#D4694A',
    'diff_xcorr':      '#E8C170',
    'threshold_onset': '#8CB4D5',
    'perm_granger':    '#2C4A6E',
    'ty_granger':      '#3B6FA0',
}
colors = [METHOD_COLORS[m] for m in methods_raw]

x = np.arange(len(methods_raw))
bar_width = 0.65

fig, (ax_fpr, ax_fnr, ax_comb) = plt.subplots(
    1, 3, figsize=(7.2, 2.8),
    gridspec_kw={'wspace': 0.38}
)

def draw_bars(ax, vals, title, panel_label, show_ylabel=True):
    bars = ax.bar(x, vals, bar_width, color=colors, edgecolor='white', linewidth=0.5, zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=6.5, linespacing=0.9)
    ax.axhline(0, color='#AAAAAA', linewidth=0.5, zorder=1)
    ax.set_title(title, fontsize=9, pad=10)
    ax.text(-0.20, 1.12, panel_label, transform=ax.transAxes,
            fontsize=10, fontweight='bold', va='bottom')
    if show_ylabel:
        ax.set_ylabel('Shapley value')

    for bar, val in zip(bars, vals):
        y_pos = val + 0.012 if val >= 0 else val - 0.020
        va = 'bottom' if val >= 0 else 'top'
        t = ax.text(bar.get_x() + bar.get_width() / 2, y_pos,
                    f'{val:+.3f}' if abs(val) >= 0.001 else '0.000',
                    ha='center', va=va, fontsize=6, color='#333333')
        t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

draw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')
ax_fpr.set_ylim(-0.05, 0.72)

draw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)
ax_fnr.set_ylim(-0.48, 0.05)

draw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)
ax_comb.set_ylim(-0.35, 0.25)

fig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.84, wspace=0.38)

for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'shapley_method_contribution.{fmt}', dpi=300)
plt.close()
print(f'Saved: {OUT}/shapley_method_contribution.pdf + .png')
