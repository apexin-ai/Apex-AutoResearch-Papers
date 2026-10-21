#!/usr/bin/env python3
"""Generate Figure 2: Forest plot of per-type ambiguity effect sizes."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import json
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.8,
})

SPEC_COLOR = '#C44E52'
LING_COLOR = '#4C72B0'
OVERALL_COLOR = '#2D2D2D'
SPEC_FILL = '#FADBD8'
LING_FILL = '#D6E4F0'

LAYER_MAP = {
    'authorization_scope': 'spec',
    'incompleteness': 'spec',
    'conditional_precedence': 'spec',
    'scopal': 'ling',
    'lexical': 'ling',
    'coreferential': 'ling',
}

DISPLAY_NAMES = {
    'authorization_scope': 'Authorization Scope',
    'incompleteness': 'Incompleteness',
    'conditional_precedence': 'Cond. Precedence',
    'scopal': 'Scopal',
    'lexical': 'Lexical',
    'coreferential': 'Coreferential',
}


def wilson_ci(p, n, z=1.96):
    if n == 0:
        return 0.0, 0.0
    denom = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    margin = z * np.sqrt((p * (1 - p) + z**2 / (4 * n)) / n) / denom
    return max(0.0, center - margin), min(1.0, center + margin)


def newcombe_ci(p1, n1, p2, n2, z=1.96):
    """Newcombe Method 10: CI for difference of two independent proportions."""
    l1, u1 = wilson_ci(p1, n1, z)
    l2, u2 = wilson_ci(p2, n2, z)
    diff = p1 - p2
    lower = diff - np.sqrt((p1 - l1)**2 + (u2 - p2)**2)
    upper = diff + np.sqrt((u1 - p1)**2 + (p2 - l2)**2)
    return lower, upper


def sig_stars(p):
    if p < 0.001:
        return '***'
    elif p < 0.01:
        return '**'
    elif p < 0.05:
        return '*'
    return ''


# --- Load data ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, '..', '..', 'full_study', 'analysis', 'full_statistics.json')
with open(DATA_PATH) as f:
    stats = json.load(f)

be = stats['binary_effect']

# Build per-type rows
types_data = []
for key, vals in be['per_type'].items():
    types_data.append({
        'key': key,
        'name': DISPLAY_NAMES[key],
        'layer': LAYER_MAP[key],
        'p_ambig': vals['ambiguous_rate'],
        'p_unambig': vals['unambiguous_rate'],
        'diff': vals['difference'],
        'p_val': vals['fisher_p'],
    })

# Group by layer (spec first), sort by delta within each group
spec_rows = sorted([d for d in types_data if d['layer'] == 'spec'],
                   key=lambda x: -x['diff'])
ling_rows = sorted([d for d in types_data if d['layer'] == 'ling'],
                   key=lambda x: -x['diff'])
rows = spec_rows + ling_rows
n_spec = len(spec_rows)

# Compute Newcombe CIs (n=250 per condition per type for 5 models × 50 clauses)
N_PER_TYPE = 250
for d in rows:
    lo, hi = newcombe_ci(d['p_ambig'], N_PER_TYPE, d['p_unambig'], N_PER_TYPE)
    d['ci_lo'] = lo * 100
    d['ci_hi'] = hi * 100
    d['diff_pp'] = d['diff'] * 100

# Overall (5 models × 300 clauses per condition ≈ 1499)
N_OVERALL = 1499
glob = be['global']
o_lo, o_hi = newcombe_ci(glob['ambiguous_rate'], N_OVERALL,
                         glob['unambiguous_rate'], N_OVERALL)
overall = {
    'diff_pp': glob['difference'] * 100,
    'ci_lo': o_lo * 100,
    'ci_hi': o_hi * 100,
    'p_val': glob['p'],
}

# --- Plot ---
n_types = len(rows)
overall_y = n_types + 0.8

fig, ax = plt.subplots(figsize=(5, 6.25))

# Background layer bands
ax.axhspan(-0.5, n_spec - 0.5, color=SPEC_FILL, alpha=0.3, zorder=0)
ax.axhspan(n_spec - 0.5, n_types - 0.5, color=LING_FILL, alpha=0.3, zorder=0)

# Vertical reference lines
ax.axvline(0, color='#888888', linestyle='--', linewidth=0.6, zorder=1, alpha=0.7)
mean_line = ax.axvline(overall['diff_pp'], color=OVERALL_COLOR, linestyle=':',
                       linewidth=0.8, alpha=0.35, zorder=1)


# Per-type rows
for i, d in enumerate(rows):
    color = SPEC_COLOR if d['layer'] == 'spec' else LING_COLOR
    ax.plot([d['ci_lo'], d['ci_hi']], [i, i], color=color,
            linewidth=2, solid_capstyle='round', zorder=3)
    ax.plot(d['diff_pp'], i, 'o', color=color, markersize=8,
            markeredgecolor='white', markeredgewidth=0.8, zorder=4)
    stars = sig_stars(d['p_val'])
    label_text = f"+{d['diff_pp']:.0f}pp {stars}"
    t = ax.text(d['ci_hi'] + 1.5, i, label_text, fontsize=9, color=color,
                va='center', ha='left', fontweight='bold')
    t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Separator before overall
sep_y = n_types - 0.5 + 0.15
ax.plot([-3, 68], [sep_y, sep_y], color='gray', linewidth=0.5, alpha=0.4,
        zorder=2, clip_on=True)

# Overall row (diamond)
ax.plot([overall['ci_lo'], overall['ci_hi']], [overall_y, overall_y],
        color=OVERALL_COLOR, linewidth=2, solid_capstyle='round', zorder=3)
ax.plot(overall['diff_pp'], overall_y, 'D', color=OVERALL_COLOR, markersize=9,
        markeredgecolor='white', markeredgewidth=0.8, zorder=4)
stars = sig_stars(overall['p_val'])
label_text = f"+{overall['diff_pp']:.1f}pp {stars}"
t = ax.text(overall['ci_hi'] + 1.5, overall_y, label_text, fontsize=9,
            color=OVERALL_COLOR, va='center', ha='left', fontweight='bold')
t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Y-axis
all_y = list(range(n_types)) + [overall_y]
all_labels = [d['name'] for d in rows] + ['Overall (pooled)']
ax.set_yticks(all_y)
ax.set_yticklabels(all_labels)

ytl = ax.get_yticklabels()
for i, d in enumerate(rows):
    ytl[i].set_color(SPEC_COLOR if d['layer'] == 'spec' else LING_COLOR)
    ytl[i].set_fontweight('semibold')
ytl[-1].set_color(OVERALL_COLOR)
ytl[-1].set_fontweight('bold')

# X-axis
ax.set_xlabel('$\\Delta$ Violation Rate (percentage points)')
ax.invert_yaxis()
ax.set_xlim(-3, 70)
ax.set_ylim(overall_y + 0.5, -0.6)

ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', length=0)

# Legend for layer bands
legend_elements = [
    mpatches.Patch(facecolor=SPEC_FILL, edgecolor=SPEC_COLOR,
                   linewidth=1, alpha=0.6, label='Specification Layer'),
    mpatches.Patch(facecolor=LING_FILL, edgecolor=LING_COLOR,
                   linewidth=1, alpha=0.6, label='Linguistic Layer'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=8.5,
          framealpha=0.9, edgecolor='#cccccc')

plt.tight_layout()

# Save
pdf_path = os.path.join(SCRIPT_DIR, 'fig2_forest_plot.pdf')
png_path = os.path.join(SCRIPT_DIR, 'fig2_forest_plot.png')
fig.savefig(pdf_path)
fig.savefig(png_path)
plt.close()

print(f'Saved: {pdf_path}')
print(f'Saved: {png_path}')
print(f'PDF size: {os.path.getsize(pdf_path)} bytes')
print(f'PNG size: {os.path.getsize(png_path)} bytes')

# Verification
print(f'\nVerification:')
print(f'  Rows: {n_types} types + 1 overall = {n_types + 1}')
for d in rows:
    print(f'  {d["name"]:25s} [{d["layer"]:4s}]  Δ={d["diff_pp"]:+5.0f}pp  '
          f'CI=[{d["ci_lo"]:+5.1f}, {d["ci_hi"]:+5.1f}]  {sig_stars(d["p_val"])}')
print(f'  {"Overall (pooled)":25s}         Δ={overall["diff_pp"]:+5.1f}pp  '
      f'CI=[{overall["ci_lo"]:+5.1f}, {overall["ci_hi"]:+5.1f}]  {sig_stars(overall["p_val"])}')
