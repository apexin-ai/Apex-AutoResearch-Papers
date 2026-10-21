"""
PaperBanana-calibrated rcParams, derived from Gemini 2.5 Pro reference output.

Differences from existing PREMIUM_RC (in generate_optimized_figures.py):
  - font.size:        8.5 → 9       (PB uses slightly larger base font)
  - axes.labelsize:   9   → 9       (same)
  - xtick.labelsize:  7.5 → 8       (PB uses 8pt tick labels)
  - ytick.labelsize:  7.5 → 8       (PB uses 8pt tick labels)
  - legend.fontsize:  7   → 8       (PB legend slightly larger)
  - axes.linewidth:   0.6 → 0.8     (PB default axes edge)
  - grid.alpha:       0.4 → 0.3     (PB uses subtler grid)
  - grid.linewidth:   0.3 → 0.5     (PB grid lines slightly thicker)
  - grid.color:   #E0E0E0 → #CCCCCC (PB uses slightly darker grid)
  - savefig.pad_inches: 0.04 → 0.05
  - Added: axes.edgecolor = 'black'  (explicit black edges)
"""

CALIBRATED_RC = {
    # --- Typography ---
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'dejavuserif',
    'font.size': 9,
    'axes.titlesize': 9.5,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,

    # --- Spines & axes ---
    'axes.linewidth': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.axisbelow': True,
    'axes.edgecolor': 'black',
    'axes.facecolor': 'white',

    # --- Ticks ---
    'xtick.major.width': 0.5,
    'ytick.major.width': 0.5,
    'xtick.minor.width': 0.3,
    'ytick.minor.width': 0.3,
    'xtick.major.size': 3.5,
    'ytick.major.size': 3.5,
    'xtick.minor.size': 2.0,
    'ytick.minor.size': 2.0,
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'xtick.major.pad': 4,
    'ytick.major.pad': 4,
    'xtick.color': 'black',
    'ytick.color': 'black',
    'axes.labelcolor': 'black',

    # --- Lines & markers ---
    'lines.linewidth': 1.5,
    'lines.markersize': 5,

    # --- Legend ---
    'legend.frameon': False,
    'legend.borderpad': 0.3,
    'legend.handlelength': 1.5,
    'legend.handletextpad': 0.5,
    'legend.columnspacing': 1.0,

    # --- Grid (PB style: subtler, slightly thicker strokes) ---
    'grid.linewidth': 0.5,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'grid.color': '#CCCCCC',

    # --- Output ---
    'figure.dpi': 300,
    'figure.facecolor': 'white',
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'savefig.facecolor': 'white',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
}

# PaperBanana reference color palette (muted, professional)
PB_COLORS = {
    'primary': '#08519c',       # muted blue (main data)
    'highlight': '#CCCCCC',     # light gray (optimal region shading)
    'highlight_alpha': 0.3,
}
