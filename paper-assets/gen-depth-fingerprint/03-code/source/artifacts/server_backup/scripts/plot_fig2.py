#!/usr/bin/env python3
"""Figure 2: LOGO Classification Performance — grouped bar chart."""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Nimbus Roman'],
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 9,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'mathtext.fontset': 'cm',
})

COLORS_CLASS = {
    'macro': '#0072B2',
    'gen-0': '#009E73',
    'gen-1': '#E69F00',
    'gen-2+': '#D55E00',
}

LABELS_GEN = {
    'olmo-2-1b':   'OLMo-2-1B',
    'pythia-1b':   'Pythia-1B',
    'pythia-2.8b': 'Pythia-2.8B',
    'qwen3-0.6b':  'Qwen3-0.6B',
    'qwen3-1.7b':  'Qwen3-1.7B',
    'qwen3-8b':    'Qwen3-8B',
}

GEN_ORDER = ['olmo-2-1b', 'pythia-1b', 'pythia-2.8b', 'qwen3-0.6b', 'qwen3-1.7b', 'qwen3-8b']

with open('/root/gen-depth-fingerprint/data/cross_generator_results.json') as f:
    data = json.load(f)

logo = data['leave_one_generator_out']

macro_f1s = []
gen0_f1s = []
gen1_f1s = []
gen2_f1s = []
macro_ci_lo = []
macro_ci_hi = []
gen0_ci_lo = []
gen0_ci_hi = []
gen1_ci_lo = []
gen1_ci_hi = []
gen2_ci_lo = []
gen2_ci_hi = []

for g in GEN_ORDER:
    d = logo[g]
    macro_f1s.append(d['macro_f1'])
    gen0_f1s.append(d['gen-0_f1'])
    gen1_f1s.append(d['gen-1_f1'])
    gen2_f1s.append(d['gen-2+_f1'])
    ci = d['bootstrap_ci']
    macro_ci_lo.append(ci['macro']['ci_lo'])
    macro_ci_hi.append(ci['macro']['ci_hi'])
    gen0_ci_lo.append(ci['gen-0']['ci_lo'])
    gen0_ci_hi.append(ci['gen-0']['ci_hi'])
    gen1_ci_lo.append(ci['gen-1']['ci_lo'])
    gen1_ci_hi.append(ci['gen-1']['ci_hi'])
    gen2_ci_lo.append(ci['gen-2+']['ci_lo'])
    gen2_ci_hi.append(ci['gen-2+']['ci_hi'])

macro_f1s = np.array(macro_f1s)
gen0_f1s = np.array(gen0_f1s)
gen1_f1s = np.array(gen1_f1s)
gen2_f1s = np.array(gen2_f1s)

overall_mean = np.mean(macro_f1s)

x = np.arange(len(GEN_ORDER))
width = 0.2

fig, ax = plt.subplots(figsize=(6.75, 4.5))

bars_macro = ax.bar(x - 1.5*width, macro_f1s, width,
                     yerr=[macro_f1s - np.array(macro_ci_lo), np.array(macro_ci_hi) - macro_f1s],
                     color=COLORS_CLASS['macro'], label='Macro-F1', capsize=2, error_kw={'linewidth': 0.8})
bars_g0 = ax.bar(x - 0.5*width, gen0_f1s, width,
                  yerr=[gen0_f1s - np.array(gen0_ci_lo), np.array(gen0_ci_hi) - gen0_f1s],
                  color=COLORS_CLASS['gen-0'], label='Gen-0 (human)', capsize=2, error_kw={'linewidth': 0.8})
bars_g1 = ax.bar(x + 0.5*width, gen1_f1s, width,
                  yerr=[gen1_f1s - np.array(gen1_ci_lo), np.array(gen1_ci_hi) - gen1_f1s],
                  color=COLORS_CLASS['gen-1'], label='Gen-1', capsize=2, error_kw={'linewidth': 0.8})
bars_g2 = ax.bar(x + 1.5*width, gen2_f1s, width,
                  yerr=[gen2_f1s - np.array(gen2_ci_lo), np.array(gen2_ci_hi) - gen2_f1s],
                  color=COLORS_CLASS['gen-2+'], label='Gen-2+', capsize=2, error_kw={'linewidth': 0.8})

ax.axhline(y=overall_mean, color='#333333', linestyle='--', linewidth=0.9, zorder=0)
ax.text(len(GEN_ORDER) - 0.5, overall_mean + 0.005, f'LOGO mean = {overall_mean:.3f}',
        fontsize=6.5, ha='right', va='bottom', color='#333333')

ax.set_ylabel('F1 Score')
ax.set_xlabel('Held-out Generator')
ax.set_xticks(x)
ax.set_xticklabels([LABELS_GEN[g] for g in GEN_ORDER])
ax.set_ylim(0.4, 1.02)
ax.legend(loc='upper right', frameon=True, fancybox=False, edgecolor='#cccccc',
          framealpha=0.9, ncol=2)

ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.tick_params(axis='y', which='minor', length=2)

plt.tight_layout()

outdir = Path('/root/gen-depth-fingerprint/figures/paper')
fig.savefig(outdir / 'fig2_logo_performance.png', dpi=300, facecolor='white')
fig.savefig(outdir / 'fig2_logo_performance.pdf', facecolor='white')
print(f'Saved fig2 to {outdir}/fig2_logo_performance.{{png,pdf}}')

print(f'\nOverall LOGO mean: {overall_mean:.4f}')
for g, f1 in zip(GEN_ORDER, macro_f1s):
    print(f'  {g}: macro_f1={f1:.4f}')

plt.close()
