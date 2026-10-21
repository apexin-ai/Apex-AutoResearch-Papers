"""
Unified Figure Style Guide — ContamCal (EMNLP 2026)
====================================================
Import this module in every figure script for consistent styling.

Usage:
    from paper_style import apply_style, COLORS, MARKERS, figsize_column
    apply_style()
    fig, ax = plt.subplots(figsize=figsize_column())
"""
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# ---------------------------------------------------------------------------
# 1. MASTER PALETTE
# ---------------------------------------------------------------------------
# Design principles:
#   - Muted, desaturated tones (no tab10 / saturated web colors)
#   - Grayscale-distinguishable (luminance spread: 93 → 111 → 139 → 156)
#   - Colorblind-safe (blue–orange axis; no red-green reliance)
#   - Semantically coherent (warm = harm, cool = benefit, gray = neutral)

COLORS = {
    # --- 4-pattern semantic colors ---
    'Benefit':      '#3C7EA6',   # steel blue       (L≈111)
    'Immune':       '#8B8B8B',   # neutral gray      (L≈139)
    'Collapse':     '#A34232',   # muted brick       (L≈93)
    'V-recovery':   '#C49A3C',   # muted gold        (L≈156)

    # --- Benefit sub-variants (Fig 1 multi-model lines) ---
    'Benefit_primary':   '#3C7EA6',   # Gemma-2 (lead)
    'Benefit_secondary': '#6098BA',   # Falcon3 (lighter)
    'Benefit_tertiary':  '#2A5F82',   # OLMo-2 (darker, borderline)

    # --- Per-model mapping ---
    'Gemma-2 9B':     '#3C7EA6',
    'Falcon3 7B':     '#6098BA',
    'Falcon3-7B':     '#6098BA',
    'OLMo-2 7B':      '#2A5F82',
    'Phi-4 14.7B':    '#8B8B8B',
    'Phi-4 14B':      '#8B8B8B',
    'LLaMA-3.1 8B':   '#ABABAB',   # lighter gray (out-of-sample)
    'Qwen2.5-14B':    '#A34232',
    'Qwen2.5-7B':     '#C49A3C',

    # --- Benchmark colors (calibration/heatmap figures) ---
    'MMLU':          '#2D6A8E',   # deep teal
    'ARC':           '#5A8C6D',   # sage green
    'ARC-C':         '#5A8C6D',
    'GSM8K':         '#B07538',   # bronze

    # --- Sign-based domain coloring (domain γ_d plot) ---
    'positive_gamma': '#3C7EA6',   # same as Benefit (contamination helps)
    'negative_gamma': '#A34232',   # same as Collapse (contamination hurts)
    'pooled':         '#666666',   # neutral for pooled estimate

    # --- Auxiliary / UI ---
    'background':     '#FFFFFF',
    'grid':           '#E8E8E8',
    'axis':           '#333333',
    'text':           '#333333',
    'annotation':     '#555555',
    'reference':      '#AAAAAA',   # zero lines, reference lines
    'separator':      '#CCCCCC',   # group separators in forest plots
    'zone_benefit':   '#3C7EA6',   # for axhspan background tinting
    'zone_harm':      '#A34232',
    'zone_threshold': '#E8E0C8',   # threshold region fill (muted wheat)
    'significant':    '#2D6A4F',   # significance annotation (deep green)
    'nonsignificant': '#999999',
}

# Opacity presets
ALPHA = {
    'ci_band':        0.12,    # confidence interval shading
    'zone':           0.05,    # background zone tinting
    'grid':           0.15,    # grid lines
    'reference_line': 0.40,    # zero / reference lines
    'error_bar':      0.30,    # cross-seed range bars
    'zone_label':     0.45,    # "Benefit zone" / "Harm zone" text
}

# ---------------------------------------------------------------------------
# 2. MARKERS
# ---------------------------------------------------------------------------
MARKERS = {
    # Per-pattern
    'Benefit':      'o',
    'Immune':       's',
    'Collapse':     'v',
    'V-recovery':   'D',

    # Per-model (for dose-response curves)
    'Gemma-2 9B':     's',   # square
    'Falcon3 7B':     '^',   # triangle up
    'Falcon3-7B':     '^',
    'OLMo-2 7B':      'o',   # circle
    'Phi-4 14.7B':    'D',   # diamond
    'Phi-4 14B':      'D',
    'LLaMA-3.1 8B':   'p',   # pentagon
    'Qwen2.5-14B':    'v',   # triangle down
    'Qwen2.5-7B':     '<',   # triangle left
}

# ---------------------------------------------------------------------------
# 3. LINE STYLES
# ---------------------------------------------------------------------------
LINESTYLES = {
    'solid':     '-',
    'dashed':    '--',
    'dotted':    ':',
    'reference': (0, (5, 5)),   # for reference/baseline lines
}

# Model-specific line styles
MODEL_LINESTYLES = {
    'LLaMA-3.1 8B': '--',   # dashed (out-of-sample validation)
}

# ---------------------------------------------------------------------------
# 4. COLORMAPS
# ---------------------------------------------------------------------------
# Custom diverging: brick (negative) → white → steel blue (positive)
DIVERGING_CMAP = LinearSegmentedColormap.from_list(
    'contam_div',
    [COLORS['Collapse'],     # -max: brick
     '#D4A69C',              # -mid: desaturated brick
     '#FFFFFF',              # zero: white
     '#8EBAD0',              # +mid: desaturated blue
     COLORS['Benefit']],     # +max: steel blue
    N=256
)

# ---------------------------------------------------------------------------
# 5. RCPARAMS
# ---------------------------------------------------------------------------
RCPARAMS = {
    # PDF embedding (TrueType, not Type 3)
    'pdf.fonttype': 42,
    'ps.fonttype': 42,

    # Font — clean sans-serif, readable at small sizes
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Helvetica', 'Arial'],
    'mathtext.fontset': 'dejavusans',
    'font.size': 10,

    # Axes
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'axes.linewidth': 0.5,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.labelpad': 4,
    'axes.labelcolor': COLORS['axis'],

    # Ticks
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.major.size': 3,
    'ytick.major.size': 3,
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'xtick.color': COLORS['axis'],
    'ytick.color': COLORS['axis'],

    # Lines
    'lines.linewidth': 1.8,
    'lines.markersize': 7,

    # Grid
    'axes.grid': False,
    'grid.alpha': ALPHA['grid'],
    'grid.linewidth': 0.3,
    'grid.linestyle': '-',
    'grid.color': COLORS['grid'],

    # Legend
    'legend.fontsize': 8,
    'legend.framealpha': 0.92,
    'legend.edgecolor': '#DDDDDD',
    'legend.fancybox': False,
    'legend.borderpad': 0.4,
    'legend.handletextpad': 0.5,

    # Figure
    'figure.dpi': 300,
    'figure.facecolor': 'white',
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.04,
    'savefig.facecolor': 'white',
}

# ---------------------------------------------------------------------------
# 6. FIGURE SIZING
# ---------------------------------------------------------------------------
# EMNLP two-column: \columnwidth ≈ 3.33in, \textwidth ≈ 6.87in
# We generate at ~2× target width so fonts remain crisp after LaTeX scaling.
# Font sizes above are calibrated for this 2× approach:
#   10pt in script → ~5pt in final PDF (legible for axis labels)

def figsize_column(aspect=0.52):
    r"""Single-column figure (scaled to ~\columnwidth by LaTeX)."""
    w = 6.5
    return (w, w * aspect)

def figsize_wide(aspect=0.42):
    """Full-width figure (scaled to ~\textwidth by LaTeX)."""
    w = 9.0
    return (w, w * aspect)

# ---------------------------------------------------------------------------
# 7. VISUAL ELEMENT SPECS
# ---------------------------------------------------------------------------
SCATTER = {
    'size': 130,               # marker size for scatter plots
    'edgecolor': 'white',
    'linewidth': 0.8,
    'zorder': 5,
}

FOREST = {
    'marker_size': 9,
    'marker_edgecolor': 'white',
    'marker_edgewidth': 0.8,
    'ci_linewidth': 2.5,
    'cap_linewidth': 1.2,
    'cap_height': 0.12,
    'separator_linewidth': 0.5,
    'separator_color': COLORS['separator'],
}

LABEL = {
    'inline_fontsize': 7.5,
    'inline_fontweight': 'medium',
    'annotation_fontsize': 8,
    'section_fontsize': 9.5,
    'section_fontweight': 'bold',
    'section_alpha': 0.75,
    'zone_label_fontsize': 7.5,
    'zone_label_alpha': ALPHA['zone_label'],
}

# ---------------------------------------------------------------------------
# 8. CONVENIENCE FUNCTIONS
# ---------------------------------------------------------------------------

def apply_style():
    """Apply unified rcParams. Call once at script start."""
    matplotlib.use('Agg')
    plt.rcParams.update(RCPARAMS)


def get_model_color(model_name):
    """Return color for a model, with fallback to annotation gray."""
    return COLORS.get(model_name, COLORS['annotation'])


def get_pattern_color(pattern_name):
    """Return color for a dose-response pattern."""
    return COLORS.get(pattern_name, COLORS['annotation'])


def get_model_marker(model_name):
    """Return marker for a model, with fallback to circle."""
    return MARKERS.get(model_name, 'o')


def get_model_linestyle(model_name):
    """Return linestyle for a model (dashed for out-of-sample, solid default)."""
    return MODEL_LINESTYLES.get(model_name, '-')


def zero_line(ax, direction='h', **kwargs):
    """Draw a subtle zero-reference line."""
    kw = dict(color=COLORS['reference'], linestyle='-',
              linewidth=0.7, alpha=ALPHA['reference_line'], zorder=1)
    kw.update(kwargs)
    if direction == 'h':
        ax.axhline(y=0, **kw)
    else:
        ax.axvline(x=0, **kw)


def benefit_harm_zones(ax, ymin, ymax, direction='h'):
    """Add subtle Benefit/Harm background tinting."""
    if direction == 'h':
        ax.axhspan(0, ymax, color=COLORS['zone_benefit'],
                   alpha=ALPHA['zone'], zorder=0)
        ax.axhspan(ymin, 0, color=COLORS['zone_harm'],
                   alpha=ALPHA['zone'], zorder=0)


def pattern_legend(ax, patterns=None, **kwargs):
    """Create a legend with pattern-colored markers."""
    if patterns is None:
        patterns = ['Benefit', 'Immune', 'V-recovery', 'Collapse']
    handles = [
        plt.Line2D([0], [0], marker=MARKERS.get(p, 'o'), color='w',
                   markerfacecolor=COLORS[p], markersize=8,
                   markeredgecolor='white', markeredgewidth=0.5, label=p)
        for p in patterns
    ]
    kw = dict(loc='best', fontsize=7.5, framealpha=0.92,
              edgecolor='#DDDDDD', handletextpad=0.5, borderpad=0.5)
    kw.update(kwargs)
    return ax.legend(handles=handles, **kw)
