"""Unified plot style for spectral optimizer paper."""
import matplotlib.pyplot as plt

COLORS = {
    'Muon': '#0077BB',
    'AdamW': '#EE7733',
    'SGD': '#CC3311',
    'SOAP': '#009988',
    'Shampoo': '#AA3377',
}

FONT_SIZES = {
    'axis_label': 11,
    'tick_label': 9,
    'annotation': 8,
    'legend': 8,
}

def apply_style():
    plt.rcParams.update({
        'font.size': 9,
        'axes.labelsize': 11,
        'axes.titlesize': 11,
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'legend.fontsize': 8,
        'figure.dpi': 150,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'pdf.fonttype': 42,
        'ps.fonttype': 42,
    })
