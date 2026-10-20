"""Unified academic color palette for all paper figures (Nature Publishing Group style)."""
import matplotlib

# ── Model colors (muted, professional) ──
QWEN    = '#3C5488'   # Steel navy
LLAMA   = '#E64B35'   # Coral red
MISTRAL = '#00A087'   # Teal green
ARCC    = '#8491B4'   # Slate blue-gray

MODEL_COLORS = {
    'Qwen': QWEN, 'Llama': LLAMA, 'Mistral': MISTRAL, 'ARC-C': ARCC,
}

# ── Semantic colors ──
CLEAN       = '#4DBBD5'  # Soft cyan
SIGNAL      = '#E64B35'  # Detection signal
MEMORIZED   = '#F39B7F'  # Salmon
CURVE       = '#3C5488'  # IRT curve

# ── Structural ──
TEXT        = '#2D2D2D'
SPINE       = '#666666'
GRID        = '#EEEEEE'
ANNOTATION  = '#555555'
REFERENCE   = '#B0B0B0'

# ── Standard rcParams ──
RC = {
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Liberation Serif', 'DejaVu Serif'],
    'text.usetex': False,
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 10,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.03,
    'axes.linewidth': 0.4,
    'xtick.major.width': 0.4,
    'ytick.major.width': 0.4,
    'xtick.major.size': 2.5,
    'ytick.major.size': 2.5,
    'lines.linewidth': 1.2,
    'patch.linewidth': 0.5,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
}

def apply():
    matplotlib.rcParams.update(RC)

def style_ax(ax):
    """Apply standard styling to axes."""
    ax.spines['left'].set_color(SPINE)
    ax.spines['bottom'].set_color(SPINE)
    ax.tick_params(colors=SPINE)
    ax.yaxis.grid(True, alpha=0.06, linewidth=0.4, color='#000000')
    ax.set_axisbelow(True)
