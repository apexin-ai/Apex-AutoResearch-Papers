#!/usr/bin/env python3
"""Generate Figure 1: MMLU dose-response curves — 2-panel layout.

Left panel: Benefit + Immune models (with background benefit zone).
Right panel: Collapse + V-recovery models.

Palette unified with pattern-based color system.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update({
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.6,
    'ytick.major.width': 0.6,
    'xtick.major.size': 3.5,
    'ytick.major.size': 3.5,
    'lines.linewidth': 1.8,
    'grid.alpha': 0.25,
    'grid.linewidth': 0.4,
    'grid.linestyle': '-',
})

# --- Pattern-based color palette (unified with Figure 3) ---
PATTERN_COLORS = {
    # Benefit (blue family)
    'Gemma-2 9B':    '#2e86ab',   # main blue
    'Falcon3-7B':    '#4a9ec4',   # lighter blue
    'OLMo-2 7B':     '#1a6d8e',   # darker blue
    # Immune (gray family)
    'Phi-4 14.7B':   '#6c757d',   # main gray
    'LLaMA-3.1 8B':  '#9ca5ad',   # lighter gray
    # Collapse (red)
    'Qwen2.5-14B':   '#c0392b',
    # V-recovery (orange)
    'Qwen2.5-7B':    '#e67e22',
}

MODEL_MARKERS = {
    'Gemma-2 9B':    's',
    'Falcon3-7B':    '^',
    'OLMo-2 7B':     'o',
    'Phi-4 14.7B':   'D',
    'LLaMA-3.1 8B':  'p',
    'Qwen2.5-14B':   'v',
    'Qwen2.5-7B':    '<',
}

# Short display names for inline labels
DISPLAY_NAMES = {
    'Gemma-2 9B':    'Gemma-2 9B',
    'Falcon3-7B':    'Falcon3 7B',
    'OLMo-2 7B':     'OLMo-2 7B',
    'Phi-4 14.7B':   'Phi-4 14.7B',
    'LLaMA-3.1 8B':  'LLaMA-3.1 8B',
    'Qwen2.5-14B':   'Qwen2.5 14B',
    'Qwen2.5-7B':    'Qwen2.5 7B',
}

xpos = np.arange(5)
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

left_panel = ['OLMo-2 7B', 'LLaMA-3.1 8B', 'Falcon3-7B', 'Gemma-2 9B', 'Phi-4 14.7B']
right_panel = ['Qwen2.5-7B', 'Qwen2.5-14B']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.8),
                                gridspec_kw={'width_ratios': [5, 4]})


def plot_panel(ax, model_list, title, title_colors=None, add_ref_lines=True):
    """Plot dose-response curves for a panel."""
    for name in model_list:
        accs = models[name]
        xs = [i for i, a in enumerate(accs) if a is not None]
        ys = [a for a in accs if a is not None]
        color = PATTERN_COLORS[name]

        # Subtle horizontal reference line at d000 accuracy
        if add_ref_lines:
            d000 = accs[0]
            ax.axhline(d000, color=color, linestyle=':', linewidth=0.7,
                       alpha=0.15, zorder=1)

        ax.plot(xs, ys, color=color, marker=MODEL_MARKERS[name],
                markersize=6, linestyle='-', linewidth=1.8, zorder=3,
                markeredgecolor='white', markeredgewidth=0.5, label=name)

    ax.set_xticks(xpos)
    ax.set_xticklabels(dosage_labels)
    ax.set_xlabel('Contamination Dosage')
    ax.yaxis.grid(True)

    # Panel title with color-coded pattern names
    if title_colors:
        ax.set_title(title, fontsize=11, fontweight='medium', color='#333333')
    else:
        ax.set_title(title, fontsize=11, fontweight='medium', color='#333333')


def add_benefit_zone(ax, model_list):
    """Add subtle blue background zone above d000 for benefit models."""
    # Find the range of d000 values for benefit models
    benefit_models = ['Gemma-2 9B', 'Falcon3-7B', 'OLMo-2 7B']
    d000_vals = [models[m][0] for m in benefit_models if m in model_list]
    if not d000_vals:
        return
    min_d000 = min(d000_vals)
    # Shade from the lowest benefit model's d000 up to top of axes
    ax.axhspan(min_d000, ax.get_ylim()[1], color='#2e86ab', alpha=0.04, zorder=0)


def add_inline_labels(ax, panel_models, x_offset=4.15):
    """Add clean inline labels at the end of each curve."""
    label_bbox = dict(facecolor='white', alpha=0.75, edgecolor='none', pad=0.8,
                      boxstyle='round,pad=0.15')

    end_ys = {}
    for name in panel_models:
        accs = models[name]
        end_ys[name] = accs[-1] if accs[-1] is not None else accs[-3]
    sorted_names = sorted(end_ys.keys(), key=lambda n: end_ys[n])
    min_gap = 2.5
    adjusted = []
    for name in sorted_names:
        y = end_ys[name]
        for _, prev_y in adjusted:
            if y - prev_y < min_gap:
                y = prev_y + min_gap
        adjusted.append((name, y))
    for name, y_adj in adjusted:
        color = PATTERN_COLORS[name]
        ax.text(x_offset, y_adj, DISPLAY_NAMES[name], fontsize=6.5,
                color=color, fontweight='semibold', va='center', ha='left',
                bbox=label_bbox)


# --- Build panels ---

# Left panel: Benefit & Immune
# Use color-coded title
ax1_title = 'Benefit & Immune'
plot_panel(ax1, left_panel, ax1_title)

# Right panel: Collapse & V-recovery
ax2_title = 'Collapse & V-recovery'
plot_panel(ax2, right_panel, ax2_title)

ax1.set_ylabel('MMLU 5-shot Accuracy (%)')
ax1.set_xlim(-0.3, 5.6)
ax1.set_ylim(50, 82)
ax2.set_xlim(-0.3, 5.6)
ax2.set_ylim(56, 72)

# Add benefit zone to left panel (must be after ylim is set)
add_benefit_zone(ax1, left_panel)

# Color-coded panel titles using colored text segments
# Left panel: "Benefit" in blue, "&" in gray, "Immune" in gray
ax1.set_title('')  # Clear plain title
# Use fig.transFigure-relative text for precise centering within each axes
ax1.text(0.38, 1.04, 'Benefit', fontsize=11, fontweight='medium',
         color='#2e86ab', transform=ax1.transAxes, ha='right', va='bottom')
ax1.text(0.50, 1.04, ' & ', fontsize=11, fontweight='medium',
         color='#555555', transform=ax1.transAxes, ha='center', va='bottom')
ax1.text(0.62, 1.04, 'Immune', fontsize=11, fontweight='medium',
         color='#6c757d', transform=ax1.transAxes, ha='left', va='bottom')

# Right panel: "Collapse" in red, "&" in gray, "V-recovery" in orange
ax2.set_title('')  # Clear plain title
ax2.text(0.35, 1.04, 'Collapse', fontsize=11, fontweight='medium',
         color='#c0392b', transform=ax2.transAxes, ha='right', va='bottom')
ax2.text(0.46, 1.04, ' & ', fontsize=11, fontweight='medium',
         color='#555555', transform=ax2.transAxes, ha='center', va='bottom')
ax2.text(0.57, 1.04, 'V-recovery', fontsize=11, fontweight='medium',
         color='#e67e22', transform=ax2.transAxes, ha='left', va='bottom')

# Inline labels
add_inline_labels(ax1, left_panel, x_offset=4.15)
add_inline_labels(ax2, right_panel, x_offset=4.15)

plt.tight_layout(w_pad=2.0)

out_dir = Path(__file__).parent
fig.savefig(out_dir / 'fig_dose_response.pdf')
fig.savefig(out_dir / 'fig_dose_response.png')
print(f"Saved: {out_dir / 'fig_dose_response.pdf'}")
print(f"Saved: {out_dir / 'fig_dose_response.png'}")
plt.close()
