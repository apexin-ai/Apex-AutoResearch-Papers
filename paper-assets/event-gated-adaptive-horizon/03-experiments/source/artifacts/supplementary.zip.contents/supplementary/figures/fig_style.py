# Shared academic figure style for CoRL 2026 paper.
# Nature/ICML convention: serif font, no grid, tight layout.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from cycler import cycler

COLUMN_WIDTH = 3.5   # inches (single-column)
DOUBLE_WIDTH = 7.0   # inches (double-column)
GOLDEN = 1.618

COLORS = {
    "baseline":       "#2C3E50",  # dark slate
    "dt2_trained":    "#E74C3C",  # red — collapse
    "dt4":            "#C0392B",  # dark red
    "dt2_untrained":  "#3498DB",  # blue — stable
    "mitigation":     "#27AE60",  # green — recovery
    "no_dt_emb":      "#9B59B6",  # purple
    "seed2":          "#F39C12",  # orange
    "threshold":      "#E74C3C",  # red dashed
    "healthy_zone":   "#27AE60",  # green fill
    "pathological":   "#E74C3C",  # red fill
}

MARKERS = {
    "baseline":      "o",
    "dt2_trained":   "s",
    "dt4":           "D",
    "dt2_untrained": "^",
    "mitigation":    "v",
    "no_dt_emb":     "P",
}


def apply_style():
    plt.rcParams.update({
        "font.family":        "serif",
        "font.serif":         ["Times New Roman", "DejaVu Serif", "serif"],
        "font.size":          8,
        "axes.titlesize":     9,
        "axes.labelsize":     8,
        "xtick.labelsize":    7,
        "ytick.labelsize":    7,
        "legend.fontsize":    7,
        "legend.frameon":     False,
        "axes.spines.top":    False,
        "axes.spines.right":  False,
        "axes.grid":          False,
        "figure.dpi":         300,
        "savefig.dpi":        300,
        "savefig.bbox":       "tight",
        "savefig.pad_inches": 0.02,
        "lines.linewidth":    1.2,
        "lines.markersize":   4,
    })


def savefig(fig, name, formats=("pdf", "png")):
    for fmt in formats:
        fig.savefig(f"{name}.{fmt}")
    plt.close(fig)
