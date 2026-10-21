"""Generate Figure 1: Cross-Benchmark Format-Conditional Variance Decomposition.

Stacked bar chart showing Henderson I variance decomposition for 4 benchmarks.
Data from exp-002 analysis (921,600 records, 4 models x 4 benchmarks).
Colorblind-friendly: Wong (2011) palette + hatching patterns.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
from pathlib import Path
import os

# --- Style ---
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Liberation Serif', 'Times New Roman'],
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 10.5,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# --- Data (exp-002, verified from analysis pipeline) ---
benchmarks = ['MMLU', 'ARC', 'HellaSwag', 'GSM8K']

data = {
    'Item':         [41.55, 48.90, 44.47, 11.99],
    'Model×Item':  [32.81, 38.20, 32.31, 12.09],
    'Model':        [ 1.50,  1.00,  2.50, 15.15],
    'Prompt':       [ 0.30,  0.20,  0.30, 12.00],
    'Residual':     [19.00,  9.00, 17.80, 32.29],
    'Other':        [ 4.84,  2.70,  2.62, 16.48],
}

# Wong (2011) colorblind-friendly palette + hatching
colors = {
    'Item':         '#0072B2',
    'Model×Item':  '#E69F00',
    'Model':        '#009E73',
    'Prompt':       '#CC79A7',
    'Residual':     '#888888',
    'Other':        '#D9D9D9',
}

hatches = {
    'Item':         '///',
    'Model×Item':  '\\\\\\',
    'Model':        '|||',
    'Prompt':       '---',
    'Residual':     '...',
    'Other':        'xxx',
}

# --- Figure ---
fig, ax = plt.subplots(figsize=(7, 3.5))

x = np.arange(len(benchmarks))
bar_width = 0.52
bottom = np.zeros(len(benchmarks))

bars_dict = {}
component_order = ['Item', 'Model×Item', 'Model', 'Prompt', 'Residual', 'Other']

for comp in component_order:
    vals = np.array(data[comp])
    bars = ax.bar(x, vals, bar_width, bottom=bottom, color=colors[comp],
                  edgecolor='white', linewidth=0.4, hatch=hatches[comp],
                  label=comp, zorder=2)
    bars_dict[comp] = (vals, bottom.copy())
    bottom += vals

# --- Annotations (>10% segments) ---
for comp in component_order:
    vals, bot = bars_dict[comp]
    for i, (v, b) in enumerate(zip(vals, bot)):
        if v > 10:
            cy = b + v / 2
            txt = f'{v:.0f}%'
            text_color = 'white' if comp in ('Item', 'Model×Item', 'Model', 'Prompt') else '#333333'
            if comp == 'Residual' and v > 15:
                text_color = 'white'
            elif comp == 'Residual':
                text_color = '#333333'
            if comp == 'Other':
                text_color = '#555555'
            t = ax.text(x[i], cy, txt, ha='center', va='center',
                        fontsize=8.5, fontweight='bold', color=text_color, zorder=3)
            t.set_path_effects([pe.withStroke(linewidth=2, foreground='white', alpha=0.4)])

# --- Regime separator ---
sep_x = 2.65
ax.axvline(sep_x, color='#666666', linestyle='--', linewidth=0.8, alpha=0.6, zorder=1)

# Format labels
ax.text(1.0, 103, 'Multiple-Choice', ha='center', va='bottom',
        fontsize=10, fontstyle='italic', color='#444444')
ax.text(3.0, 103, 'Free-Form', ha='center', va='bottom',
        fontsize=10, fontstyle='italic', color='#444444')

# --- Axes ---
ax.set_ylabel('Variance (%)')
ax.set_ylim(0, 100)
ax.set_yticks([0, 20, 40, 60, 80, 100])
ax.set_xlim(-0.45, 3.65)
ax.set_xticks(x)
ax.set_xticklabels(benchmarks)

ax.spines['left'].set_linewidth(0.8)
ax.spines['bottom'].set_linewidth(0.8)
ax.tick_params(axis='both', width=0.8, length=4)

# --- Legend (horizontal, below figure) ---
legend_handles = [mpatches.Patch(facecolor=colors[c], edgecolor='#555555',
                                 linewidth=0.5, hatch=hatches[c], label=c)
                  for c in component_order]
ax.legend(handles=legend_handles, loc='upper center',
          bbox_to_anchor=(0.5, -0.10), ncol=6, frameon=False,
          handlelength=1.2, handletextpad=0.4, columnspacing=1.0)

plt.tight_layout()

# --- Save ---
out_dir = '/root/nlp_variance_gtheory/figures/paper'
os.makedirs(out_dir, exist_ok=True)

pdf_path = os.path.join(out_dir, 'fig1_cross_benchmark.pdf')
png_path = os.path.join(out_dir, 'fig1_cross_benchmark.png')

plt.savefig(pdf_path)
plt.savefig(png_path, dpi=300)
plt.close()

print(f'Saved: {pdf_path}')
print(f'Saved: {png_path}')

# Verify totals
for i, bm in enumerate(benchmarks):
    total = sum(data[c][i] for c in component_order)
    print(f'  {bm}: {total:.2f}%')
