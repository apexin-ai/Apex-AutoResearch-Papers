#!/usr/bin/env python3
"""Figure 1: MMLU dose-response curves — 2-panel layout.

Left panel: Benefit + Immune (Gemma-2, Falcon3, OLMo-2, Phi-4, LLaMA-3.1).
Right panel: Collapse + V-recovery (Qwen2.5-14B, Qwen2.5-7B).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from paper_style import *

apply_style()

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ── Data ─────────────────────────────────────────────────────────────
dosages = [0, 0.5, 2.5, 5, 10]
xpos = np.arange(len(dosages))
dosage_labels = ['0%', '0.5%', '2.5%', '5%', '10%']

models = {
    'Phi-4 14.7B':   [76.44, 76.36, 76.98, 76.75, 76.27],
    'Qwen2.5-14B':   [69.44, 69.01, 62.04, 59.41, 60.07],
    'Qwen2.5-7B':    [66.11, 64.74, 62.98, 63.07, 64.33],
    'Gemma-2 9B':    [61.86, 63.42, 64.56, 64.01, 65.62],
    'Falcon3-7B':    [58.77, 59.02, 61.23, 62.09, 62.96],
    'OLMo-2 7B':     [53.79, 56.14, 56.17, 57.25, 57.00],
    'LLaMA-3.1 8B':  [53.50, None, 52.75, None, 52.81],
}

DISPLAY = {
    'Gemma-2 9B':    'Gemma-2 9B',
    'Falcon3-7B':    'Falcon3 7B',
    'OLMo-2 7B':     'OLMo-2 7B',
    'Phi-4 14.7B':   'Phi-4 14.7B',
    'LLaMA-3.1 8B':  'LLaMA-3.1 8B',
    'Qwen2.5-14B':   'Qwen2.5 14B',
    'Qwen2.5-7B':    'Qwen2.5 7B',
}

left_models  = ['OLMo-2 7B', 'LLaMA-3.1 8B', 'Falcon3-7B', 'Gemma-2 9B', 'Phi-4 14.7B']
right_models = ['Qwen2.5-7B', 'Qwen2.5-14B']


def plot_curves(ax, model_list):
    for name in model_list:
        accs = models[name]
        xs = [i for i, a in enumerate(accs) if a is not None]
        ys = [a for a in accs if a is not None]
        color = get_model_color(name)

        ax.axhline(accs[0], color=color, linestyle=':', linewidth=0.6,
                   alpha=ALPHA['ci_band'], zorder=1)

        ls = get_model_linestyle(name)
        ax.plot(xs, ys, color=color, marker=get_model_marker(name),
                markersize=7, linestyle=ls, zorder=3,
                markeredgecolor='white', markeredgewidth=0.8, label=name)


def add_benefit_zone(ax, model_list):
    benefit = ['Gemma-2 9B', 'Falcon3-7B', 'OLMo-2 7B']
    d000_vals = [models[m][0] for m in benefit if m in model_list]
    if not d000_vals:
        return
    ax.axhspan(min(d000_vals), ax.get_ylim()[1],
               color=COLORS['zone_benefit'], alpha=ALPHA['zone'], zorder=0)


def add_inline_labels(ax, panel_models, x_offset=4.18, min_gap=2.8):
    bbox_props = dict(facecolor='white', alpha=0.88, edgecolor='none',
                      pad=0.6, boxstyle='round,pad=0.12')
    end_ys = {}
    for name in panel_models:
        accs = models[name]
        for a in reversed(accs):
            if a is not None:
                end_ys[name] = a
                break

    sorted_names = sorted(end_ys.keys(), key=lambda n: end_ys[n])
    adjusted = []
    for name in sorted_names:
        y = end_ys[name]
        for _, prev_y in adjusted:
            if y - prev_y < min_gap:
                y = prev_y + min_gap
        adjusted.append((name, y))

    for name, y_adj in adjusted:
        ax.text(x_offset, y_adj, DISPLAY[name],
                fontsize=LABEL['inline_fontsize'],
                color=get_model_color(name),
                fontweight=LABEL['inline_fontweight'],
                va='center', ha='left', bbox=bbox_props, zorder=5)


def add_color_title(ax, left_text, left_color, right_text, right_color,
                    y=1.06, fontsize=12):
    ax.text(0.50, y, ' & ', fontsize=fontsize, fontweight='medium',
            color=COLORS['annotation'], transform=ax.transAxes,
            ha='center', va='bottom')
    ax.text(0.44, y, left_text, fontsize=fontsize, fontweight='medium',
            color=left_color, transform=ax.transAxes,
            ha='right', va='bottom')
    ax.text(0.56, y, right_text, fontsize=fontsize, fontweight='medium',
            color=right_color, transform=ax.transAxes,
            ha='left', va='bottom')


# ── Build figure ─────────────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize_column(aspect=0.49),
                                gridspec_kw={'width_ratios': [5, 4]})

plot_curves(ax1, left_models)
plot_curves(ax2, right_models)

ax1.set_ylabel('MMLU 5-shot Accuracy (%)')
ax1.set_xlabel('Contamination Dosage')
ax2.set_xlabel('Contamination Dosage')

for ax in (ax1, ax2):
    ax.set_xticks(xpos)
    ax.set_xticklabels(dosage_labels, fontsize=9)
    ax.yaxis.grid(True)

ax1.set_xlim(-0.3, 5.6)
ax1.set_ylim(50, 82)
ax1.yaxis.set_major_locator(mticker.MultipleLocator(5))

ax2.set_xlim(-0.3, 5.6)
ax2.set_ylim(56, 72)
ax2.yaxis.set_major_locator(mticker.MultipleLocator(4))

add_benefit_zone(ax1, left_models)

add_color_title(ax1, 'Benefit', COLORS['Benefit'], 'Immune', COLORS['Immune'])
add_color_title(ax2, 'Collapse', COLORS['Collapse'],
                'V-recovery', COLORS['V-recovery'])

add_inline_labels(ax1, left_models, x_offset=4.18, min_gap=2.8)
add_inline_labels(ax2, right_models, x_offset=4.18, min_gap=3.0)

plt.tight_layout(w_pad=2.0)

# ── Save ─────────────────────────────────────────────────────────────
out_dir = Path(__file__).parent
paper_dir = Path(__file__).resolve().parent.parent.parent / 'docs' / 'paper' / 'figures'
for d in [out_dir, paper_dir]:
    fig.savefig(d / 'fig_dose_response.pdf')
    fig.savefig(d / 'fig_dose_response.png')
print(f"Saved fig_dose_response to {out_dir} and {paper_dir}")
plt.close()
