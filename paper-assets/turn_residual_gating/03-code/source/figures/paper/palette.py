"""Unified color palette and style for all paper figures.

All gen_*.py scripts should `from palette import *` to get consistent colors
and rcParams. Monochromatic blue gradient for training configs, warm accent
for SS (core contribution), classic blue/red for TF/AR semantic pair.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Training configuration colors (light, clear, Tableau-Pastel-inspired) ──
COLORS = {
    'Base':       '#BDBDBD',  # light neutral gray (untrained reference)
    'ThreadGate': '#6BAED6',  # clear sky blue (primary testbed)
    'UG':         '#8DC98D',  # light sage green (ablation)
    'LoRA':       '#B5A8D0',  # soft lavender (ablation)
    'PCGrad':     '#E6A8A1',  # light rose (diagnostic)
    'SS':         '#FDAE6B',  # warm apricot (core contribution)
}

# Short aliases for quick access
C_BASE = COLORS['Base']
C_TG   = COLORS['ThreadGate']
C_UG   = COLORS['UG']
C_LO   = COLORS['LoRA']
C_PC   = COLORS['PCGrad']
C_SS   = COLORS['SS']

# ── Semantic colors ────────────────────────────────────────────────
C_TF   = '#74ADD1'   # clear blue (teacher-forced)
C_AR   = '#F4A582'   # soft coral (autoregressive)
C_GAR  = '#6BAED6'   # clear sky blue (GAR metric lines)
C_PPL  = '#A0A0A0'   # neutral mid-gray (PPL metric lines)
C_SWEET = '#F7F4EF'  # very pale warm cream (sweet-spot bands)
C_GRAY  = '#AAAAAA'  # light gray (reference lines, annotations)

# ── Label colors (medium variants for text annotations) ───────────
C_TF_DARK = '#4A90B8'  # medium blue for TF value labels
C_AR_DARK = '#D16B55'  # medium coral for AR value labels

# ── Extended color families (light, clear, per-figure variety) ────
C_TEAL    = '#7ECAC1'  # soft teal / mint
C_GOLD    = '#D4B896'  # warm gold / sand
C_ROSE    = '#E6A8A1'  # light rose (= C_PC)
C_PURPLE  = '#B5A8D0'  # soft lavender (= C_LO)
C_GREEN   = '#8DC98D'  # light sage green (= C_UG)
C_SKYBLUE = '#6BAED6'  # clear sky blue (= C_TG)
C_APRICOT = '#FDAE6B'  # warm apricot (= C_SS)
C_MINT    = '#A1D9CE'  # pale mint
C_PEACH   = '#F9C5A8'  # soft peach
C_LILAC   = '#C4B7DB'  # lighter lilac

# ── Marker shapes for grayscale safety ────────────────────────────
MARKERS = {
    'Base': 'o', 'ThreadGate': 's', 'UG': 'D',
    'LoRA': '^', 'PCGrad': 'v', 'SS': 'P',
}

LINESTYLES = {
    'Base': (0, (2, 2)), 'ThreadGate': '-', 'UG': '-.',
    'LoRA': '--', 'PCGrad': (0, (4, 1, 1, 1)), 'SS': '-',
}

# ── Ordered list for bar charts (matches Table 1 order) ───────────
CONFIG_ORDER = ['Base', 'ThreadGate', 'PCGrad', 'UG', 'LoRA', 'SS']
CONFIG_COLORS = [COLORS.get(c, C_GRAY) for c in CONFIG_ORDER]

# ── Shared rcParams ────────────────────────────────────────────────
RCPARAMS = {
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],
    'font.size': 8.5,
    'axes.titlesize': 9,
    'axes.labelsize': 8.5,
    'xtick.labelsize': 7.5,
    'ytick.labelsize': 7.5,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'axes.edgecolor': '#555555',
    'axes.labelcolor': '#333333',
    'xtick.color': '#555555',
    'ytick.color': '#555555',
    'text.color': '#333333',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 1.3,
    'axes.linewidth': 0.5,
    'xtick.major.width': 0.4,
    'ytick.major.width': 0.4,
    'xtick.major.size': 3.0,
    'ytick.major.size': 3.0,
    'xtick.minor.size': 1.5,
    'ytick.minor.size': 1.5,
    'grid.alpha': 0.06,
    'grid.linewidth': 0.3,
    'legend.frameon': False,
    'legend.labelspacing': 0.3,
    'legend.handlelength': 1.5,
}

OUTDIR = '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper'


def apply_style():
    """Apply unified rcParams. Call at top of every gen script."""
    plt.rcParams.update(RCPARAMS)


def save_fig(fig, name):
    """Save figure as PDF + PNG to the standard output directory."""
    fig.savefig(f'{OUTDIR}/{name}.pdf')
    fig.savefig(f'{OUTDIR}/{name}.png', dpi=300)
    plt.close(fig)
    print(f'Saved: {name}.pdf + .png')
