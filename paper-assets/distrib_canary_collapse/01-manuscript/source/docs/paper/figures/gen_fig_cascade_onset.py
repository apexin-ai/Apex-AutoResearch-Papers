#!/usr/bin/env python3
"""Cascade onset timeline (Gantt-style): metric onset generations across conditions.
Uses unified paper_palette. Data from moment_cascade_analysis.json."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
import json
from pathlib import Path

OUT = Path(__file__).parent
DATA = Path(__file__).resolve().parents[3] / 'artifacts' / 'moment_cascade' / 'moment_cascade_analysis.json'

from paper_palette import (PERMG, LIGHT_BLUE, NAIVEXCORR, DIFFXCORR,
                           THRESHOLD, GRAY, TODAYAM)

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

with open(DATA) as f:
    d = json.load(f)

conditions = [
    ('s42', 'a010', r'$\alpha{=}0.10$, $s42$'),
    ('s42', 'a050', r'$\alpha{=}0.50$, $s42$'),
    ('s42', 'a075', r'$\alpha{=}0.75$, $s42$'),
    ('s43', 'a050', r'$\alpha{=}0.50$, $s43$'),
    ('s43', 'a075', r'$\alpha{=}0.75$, $s43$'),
]
metrics = ['token_entropy', 'ece', 'distinct_1', 'distinct_2', 'distinct_3', 'perplexity', 'mauve']
metric_labels = ['Entropy', 'ECE', 'Dist-1', 'Dist-2', 'Dist-3', 'PPL', 'MAUVE']
metric_colors = [PERMG, LIGHT_BLUE, NAIVEXCORR, DIFFXCORR, THRESHOLD, GRAY, TODAYAM]

fig, ax = plt.subplots(figsize=(3.4, 4.5))

y_pos = 0
y_ticks = []
y_labels = []

for ci, (seed, alpha, label) in enumerate(conditions):
    onset_data = d['onset_results'].get(seed, {}).get(alpha, {})

    for mi, (metric, mlabel) in enumerate(zip(metrics, metric_labels)):
        onset = onset_data.get(metric, {}).get('onset_5pct', None)
        if onset is not None:
            ax.barh(y_pos, 0.6, left=onset - 0.3, height=0.7,
                    color=metric_colors[mi], alpha=0.85, edgecolor='white',
                    linewidth=0.3)
            txt_color = '#FFFFFF' if metric_colors[mi] not in (LIGHT_BLUE, GRAY) else '#333333'
            ax.text(onset, y_pos, str(onset), ha='center', va='center',
                    fontsize=6, fontweight='bold', color=txt_color,
                    path_effects=[pe.withStroke(linewidth=1.2, foreground='#00000022')])
        else:
            ax.text(0.5, y_pos, '—', ha='center', va='center',
                    fontsize=7, color=GRAY)

        if ci == 0:
            y_ticks.append(y_pos)
            y_labels.append(mlabel)
        y_pos += 1

    if ci < len(conditions) - 1:
        ax.axhline(y_pos - 0.5, color='#DDDDDD', lw=0.5, ls='-')
    y_pos += 0.5

# Condition labels on right
y_start = 0
for ci, (_, _, label) in enumerate(conditions):
    mid = y_start + len(metrics) / 2 - 0.5
    ax.text(10.5, mid, label, ha='left', va='center', fontsize=7,
            fontstyle='italic', color='#777777')
    y_start += len(metrics) + 0.5

ax.set_xlabel('Onset generation (5% threshold)')
ax.set_xlim(-0.5, 10)
ax.set_yticks([y_ticks[i] for i in range(len(metrics))])
ax.set_yticklabels(y_labels, fontsize=7)
ax.invert_yaxis()
ax.xaxis.grid(True, alpha=0.12, lw=0.4)
ax.set_axisbelow(True)
ax.set_xticks(range(0, 11))

# Phase bands
ax.axvspan(-0.5, 1.5, alpha=0.04, color=PERMG, zorder=0)
ax.axvspan(1.5, 3.5, alpha=0.04, color=DIFFXCORR, zorder=0)
t1 = ax.text(0.5, -1.8, 'Phase 1\n(canary)', ha='center', fontsize=6, color=PERMG)
t1.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
t2 = ax.text(2.5, -1.8, 'Phase 2\n(diversity)', ha='center', fontsize=6, color=DIFFXCORR)
t2.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

plt.tight_layout()
for fmt in ['pdf', 'png']:
    fig.savefig(OUT / f'fig_cascade_onset.{fmt}', dpi=300)
plt.close()
print(f'Saved: {OUT}/fig_cascade_onset.pdf + .png')
