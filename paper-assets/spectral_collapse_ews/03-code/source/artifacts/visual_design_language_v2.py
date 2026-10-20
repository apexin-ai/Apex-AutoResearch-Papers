"""
Spectral Collapse EWS — Visual Design Language v2.0
====================================================
Target aesthetic: Nature / PNAS / Science
Design principle: "Ink-wash restraint" — every visual element earns its place.
Low saturation, thin lines, serif type, small markers, inline labels.

Usage:
    from visual_design_language_v2 import apply_style, COLORS, MARKERS, PHASES
    apply_style()  # sets plt.rcParams globally
"""

from cycler import cycler

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. COLOR PALETTE
#    Warm→cool gradient: collapse (warm) → stable (cool)
#    Colorblind-safe: perceptually distinct under deuteranopia
#    and protanopia; luminance-separated for grayscale printing.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COLORS = {
    # ── Primary 5: mixing-ratio semantic gradient ──
    'r0':    '#834655',   # Dusty rose     — r=0  (pure synthetic / collapse)
    'r02':   '#B57A4A',   # Copper         — r=0.2
    'r025':  '#C4A84D',   # Antique gold   — r=0.25 (transitional)
    'r03':   '#4A8C82',   # Muted teal     — r=0.3  (near r_crit)
    'r05':   '#3A5A8C',   # Steel blue     — r=0.5  (stable)

    # ── Auxiliary ──
    'baseline':    '#5A5A5A',   # Neutral gray — Gen-0 reference / baselines
    'annotation':  '#3A3A3A',   # Dark gray — text labels, arrows
    'light_ref':   '#A0A0A0',   # Light gray — secondary reference lines
    'error_fill':  '#00000010', # Near-transparent black for CI bands

    # ── Phase annotation fills ──
    'phase_I':     '#F0E6D6',   # Warm parchment — decompression
    'phase_II':    '#E6D8C2',   # Warm sand — onset
    'phase_III':   '#DCC8AE',   # Warm khaki — acceleration

    # ── Phase boundary ──
    'phase_edge':  '#9A9A9A',   # Medium gray for dashed boundaries
}

PRIMARY_5 = [COLORS['r0'], COLORS['r02'], COLORS['r025'],
             COLORS['r03'], COLORS['r05']]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2. LINE SPECIFICATIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LINES = {
    'data':           dict(linewidth=1.2, solid_capstyle='round'),
    'data_thin':      dict(linewidth=0.8, solid_capstyle='round'),
    'reference':      dict(linewidth=0.6, linestyle='--', alpha=0.55),
    'phase_boundary': dict(linewidth=0.4, linestyle=':', color=COLORS['phase_edge'], alpha=0.45),
    'axis':           dict(linewidth=0.5),
    'ci_band':        dict(alpha=0.12, linewidth=0),
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3. MARKER SPECIFICATIONS
#    Each mixing ratio gets a unique shape for grayscale fallback.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MARKERS = {
    'r0':   dict(marker='o', markersize=3.5, markeredgewidth=0.4, markeredgecolor='white'),
    'r02':  dict(marker='s', markersize=3.0, markeredgewidth=0.4, markeredgecolor='white'),
    'r025': dict(marker='^', markersize=3.5, markeredgewidth=0.4, markeredgecolor='white'),
    'r03':  dict(marker='D', markersize=3.0, markeredgewidth=0.4, markeredgecolor='white'),
    'r05':  dict(marker='v', markersize=3.5, markeredgewidth=0.4, markeredgecolor='white'),
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4. FONT SPECIFICATIONS
#    Serif throughout (Times New Roman primary).
#    Math set: dejavuserif for consistency with body text.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FONTS = {
    'family':       'serif',
    'serif_stack':  ['Times New Roman', 'DejaVu Serif', 'Georgia', 'serif'],
    'axis_label':   dict(size=8,   weight='normal'),
    'tick_label':   dict(size=7),
    'legend':       dict(size=6.5),
    'annotation':   dict(size=6.5, style='italic'),
    'panel_label':  dict(size=9,   weight='bold'),        # (a), (b), ...
    'inline_label': dict(size=6,   weight='normal'),
    'title':        dict(size=8,   weight='normal'),
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 5. LEGEND SPECIFICATIONS
#    Prefer inline labels over box legends when <= 3 curves.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEGEND = dict(
    frameon=False,
    fontsize=6.5,
    handlelength=1.5,
    handletextpad=0.4,
    columnspacing=1.0,
    labelspacing=0.3,
    borderaxespad=0.3,
)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 6. ANNOTATION SPECIFICATIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ANNOTATIONS = dict(
    arrowprops=dict(
        arrowstyle='->',
        color=COLORS['annotation'],
        lw=0.5,
        connectionstyle='arc3,rad=0.12',
    ),
    bbox=dict(
        boxstyle='round,pad=0.12',
        facecolor='white',
        edgecolor='none',
        alpha=0.85,
    ),
    phase_label=dict(
        fontsize=6,
        fontstyle='italic',
        color='#777777',
        ha='center',
        va='bottom',
    ),
)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 7. PHASE ANNOTATION SCHEME
#    Three phases of spectral collapse: fill bands + Roman labels.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASES = {
    'I': dict(
        label='I',
        sublabel='Decompression',
        gen_range=(0, 2),
        fill_color=COLORS['phase_I'],
        fill_alpha=0.30,
        text_color='#8A7A5A',
    ),
    'II': dict(
        label='II',
        sublabel='Onset',
        gen_range=(2, 4),
        fill_color=COLORS['phase_II'],
        fill_alpha=0.30,
        text_color='#7A6A4A',
    ),
    'III': dict(
        label='III',
        sublabel='Acceleration',
        gen_range=(4, 10),
        fill_color=COLORS['phase_III'],
        fill_alpha=0.30,
        text_color='#6A5A3A',
    ),
}


def add_phase_bands(ax, phases=None, ymin=0, ymax=1):
    """Add phase annotation bands to an axes."""
    if phases is None:
        phases = PHASES
    for key, p in phases.items():
        ax.axvspan(p['gen_range'][0], p['gen_range'][1],
                   ymin=ymin, ymax=ymax,
                   facecolor=p['fill_color'], alpha=p['fill_alpha'],
                   edgecolor='none', zorder=0)
        mid = (p['gen_range'][0] + p['gen_range'][1]) / 2
        ax.text(mid, ax.get_ylim()[1], p['label'],
                fontsize=6, fontstyle='italic', color=p['text_color'],
                ha='center', va='bottom', transform=ax.get_xaxis_transform())


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 8. BACKGROUND & GRID
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BACKGROUND = dict(
    facecolor='white',
    grid=False,
    spine_visible=dict(top=False, right=False, left=True, bottom=True),
    spine_color='#333333',
    spine_linewidth=0.5,
)


def style_axes(ax):
    """Apply Nature-style axis formatting to a single axes."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for side in ('left', 'bottom'):
        ax.spines[side].set_color(BACKGROUND['spine_color'])
        ax.spines[side].set_linewidth(BACKGROUND['spine_linewidth'])
    ax.tick_params(axis='both', which='major',
                   length=3, width=0.4, direction='out',
                   color='#333333', labelsize=7)
    ax.tick_params(axis='both', which='minor',
                   length=1.5, width=0.3, direction='out',
                   color='#333333')


def add_inline_label(ax, x, y, text, color, offset=(5, 3)):
    """Add an inline label near a data point (preferred over legend)."""
    ax.annotate(text, xy=(x, y), xytext=offset,
                textcoords='offset points',
                fontsize=6, color=color,
                bbox=dict(boxstyle='round,pad=0.1',
                          facecolor='white', edgecolor='none', alpha=0.8))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 9. COMPLETE plt.rcParams DICT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RCPARAMS = {
    # ── Font ──
    'font.family':          'serif',
    'font.serif':           ['Times New Roman', 'DejaVu Serif', 'Georgia', 'serif'],
    'font.size':            7,

    # ── Axes ──
    'axes.linewidth':       0.5,
    'axes.edgecolor':       '#333333',
    'axes.labelsize':       8,
    'axes.labelweight':     'normal',
    'axes.labelcolor':      '#222222',
    'axes.titlesize':       8,
    'axes.titleweight':     'normal',
    'axes.titlepad':        6,
    'axes.spines.top':      False,
    'axes.spines.right':    False,
    'axes.facecolor':       'white',
    'axes.prop_cycle':      cycler('color', PRIMARY_5),

    # ── Ticks ──
    'xtick.major.size':     3,
    'xtick.major.width':    0.4,
    'xtick.minor.size':     1.5,
    'xtick.minor.width':    0.3,
    'xtick.labelsize':      7,
    'xtick.direction':      'out',
    'xtick.color':          '#333333',
    'ytick.major.size':     3,
    'ytick.major.width':    0.4,
    'ytick.minor.size':     1.5,
    'ytick.minor.width':    0.3,
    'ytick.labelsize':      7,
    'ytick.direction':      'out',
    'ytick.color':          '#333333',

    # ── Grid: OFF ──
    'axes.grid':            False,

    # ── Legend ──
    'legend.frameon':       False,
    'legend.fontsize':      6.5,
    'legend.handlelength':  1.5,
    'legend.handletextpad': 0.4,
    'legend.columnspacing': 1.0,
    'legend.labelspacing':  0.3,
    'legend.borderaxespad': 0.3,

    # ── Lines ──
    'lines.linewidth':        1.2,
    'lines.markersize':       3.5,
    'lines.markeredgewidth':  0.4,
    'lines.solid_capstyle':   'round',

    # ── Figure ──
    'figure.facecolor':     'white',
    'figure.dpi':           300,
    'savefig.dpi':          300,
    'savefig.bbox':         'tight',
    'savefig.pad_inches':   0.02,
    'savefig.transparent':  False,

    # ── Text ──
    'text.color':           '#222222',

    # ── Math ──
    'mathtext.fontset':     'dejavuserif',
}


def apply_style():
    """Apply the full visual design language globally via plt.rcParams."""
    import matplotlib.pyplot as plt
    plt.rcParams.update(RCPARAMS)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 10. FIGURE SIZE PRESETS (single-column = 3.4in, double = 7.0in)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FIGSIZE = {
    'single':       (3.4, 2.4),     # Standard single-column
    'single_tall':  (3.4, 3.2),     # Single-column, taller
    'double':       (7.0, 2.8),     # Full-width
    'double_tall':  (7.0, 4.0),     # Full-width, taller
    'double_2x1':   (7.0, 2.4),     # Two panels side by side
    'double_2x2':   (7.0, 5.0),     # Four panels
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 11. SEMANTIC HELPERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def color_for_ratio(r):
    """Return the palette color for a given mixing ratio."""
    mapping = {0: 'r0', 0.2: 'r02', 0.25: 'r025', 0.3: 'r03', 0.5: 'r05'}
    key = mapping.get(r, 'baseline')
    return COLORS[key]


def marker_for_ratio(r):
    """Return marker kwargs for a given mixing ratio."""
    mapping = {0: 'r0', 0.2: 'r02', 0.25: 'r025', 0.3: 'r03', 0.5: 'r05'}
    key = mapping.get(r, 'r0')
    return MARKERS[key]


def plot_with_style(ax, x, y, ratio, label=None, **kwargs):
    """Plot a line with the correct color + marker for a mixing ratio."""
    c = color_for_ratio(ratio)
    m = marker_for_ratio(ratio)
    kw = {**LINES['data'], **m, 'color': c, 'label': label}
    kw.update(kwargs)
    return ax.plot(x, y, **kw)
