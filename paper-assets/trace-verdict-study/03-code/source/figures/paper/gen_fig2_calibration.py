"""Generate fig2_calibration: 2x2 reliability diagrams for 4 trace conditions."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Calibration bin data extracted from server calibration JSON files
# Each entry: (mean_confidence, accuracy, count)
# Bins: [0.5-0.55, 0.55-0.6, ..., 0.95-1.0], 10 equal-width bins

DATA = {
    "no_trace": {
        "ece": 0.1715,
        "accuracy": 0.7513,
        "n_samples": 1190,
        "bins": [
            (0.525391, 0.8125, 16),
            (0.572917, 0.333333, 45),
            (0.621094, 0.434783, 23),
            (0.667969, 0.828571, 35),
            (0.725446, 0.25, 28),
            (0.771289, 0.633333, 60),
            (0.829834, 0.791667, 48),
            (0.870502, 0.69697, 99),
            (0.924347, 0.621469, 177),
            (0.985, 0.857, 659),  # last bin: conf estimated from ECE residual
        ],
    },
    "full_trace": {
        "ece": 0.0958,
        "accuracy": 0.8176,
        "n_samples": 1190,
        "bins": [
            (0.519676, 0.444444, 27),
            (0.574728, 0.586957, 46),
            (0.621094, 0.666667, 21),
            (0.667969, 0.714286, 42),
            (0.717538, 0.637931, 58),
            (0.772135, 0.666667, 54),
            (0.829637, 0.580645, 31),
            (0.873125, 0.746667, 75),
            (0.9261, 0.755102, 98),
            (0.992, 0.907, 738),  # last bin: conf estimated from ECE residual
        ],
    },
    "exception_only": {
        "ece": 0.0027,
        "accuracy": 0.9983,
        "n_samples": 1190,
        "bins": [
            (0.0, 0.0, 0),
            (0.0, 0.0, 0),
            (0.0, 0.0, 0),
            (0.0, 0.0, 0),
            (0.0, 0.0, 0),
            (0.0, 0.0, 0),
            (0.835938, 0.0, 1),
            (0.0, 0.0, 0),
            (0.940848, 0.857143, 7),
            (0.99881, 1.0, 1182),
        ],
    },
    "vota": {
        "ece": 0.0054,
        "accuracy": 0.9941,
        "n_samples": 1190,
        "bins": [
            (0.0, 0.0, 0),
            (0.0, 0.0, 0),
            (0.621094, 0.0, 1),
            (0.0, 0.0, 0),
            (0.0, 0.0, 0),
            (0.0, 0.0, 0),
            (0.0, 0.0, 0),
            (0.0, 0.0, 0),
            (0.941406, 1.0, 1),
            (0.999809, 0.994949, 1188),
        ],
    },
}

COLORS = {
    "no_trace": "#999999",
    "full_trace": "#56B4E9",
    "exception_only": "#009E73",
    "vota": "#E69F00",
}

TITLES = {
    "no_trace": "(a) No Trace",
    "full_trace": "(b) Full Trace",
    "exception_only": "(c) Exception Only",
    "vota": "(d) VOTA",
}

CONDITIONS = ["no_trace", "full_trace", "exception_only", "vota"]
BIN_EDGES = np.linspace(0.5, 1.0, 11)
BIN_CENTERS = (BIN_EDGES[:-1] + BIN_EDGES[1:]) / 2
BIN_WIDTH = 0.05


def plot_panel(ax_rel, ax_hist, cond):
    d = DATA[cond]
    color = COLORS[cond]
    bins = d["bins"]

    confs = np.array([b[0] for b in bins])
    accs = np.array([b[1] for b in bins])
    counts = np.array([b[2] for b in bins])
    n_total = d["n_samples"]

    mask = counts > 0

    # Reliability diagram (upper panel)
    ax_rel.plot([0.5, 1.0], [0.5, 1.0], '--', color='#888888', linewidth=1, zorder=1)

    # Bar for actual accuracy
    for i in range(len(bins)):
        if counts[i] == 0:
            continue
        x = BIN_CENTERS[i]
        acc_val = accs[i]
        conf_val = confs[i]

        # Accuracy bar
        ax_rel.bar(x, acc_val, width=BIN_WIDTH * 0.85, color=color, alpha=0.7,
                   edgecolor='white', linewidth=0.5, zorder=2)

        # Gap bar (overconfidence: from accuracy up to confidence)
        if conf_val > acc_val:
            ax_rel.bar(x, conf_val - acc_val, bottom=acc_val,
                       width=BIN_WIDTH * 0.85, color='#E74C3C', alpha=0.3,
                       edgecolor='none', zorder=2)
        elif acc_val > conf_val:
            ax_rel.bar(x, acc_val - conf_val, bottom=conf_val,
                       width=BIN_WIDTH * 0.85, color='#2196F3', alpha=0.2,
                       edgecolor='none', zorder=2)

    ax_rel.set_xlim(0.5, 1.0)
    ax_rel.set_ylim(0.0, 1.05)
    ax_rel.set_ylabel('Fraction of Positives')
    ax_rel.set_title(TITLES[cond], fontsize=12, fontweight='bold', pad=6)

    ece_val = d["ece"]
    ax_rel.text(0.95, 0.08, f'ECE = {ece_val:.3f}',
                transform=ax_rel.transAxes, fontsize=10,
                ha='right', va='bottom',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor='#cccccc', alpha=0.9))

    ax_rel.set_xticklabels([])

    # Histogram (lower panel)
    fractions = counts / n_total
    for i in range(len(bins)):
        if counts[i] == 0:
            continue
        ax_hist.bar(BIN_CENTERS[i], fractions[i], width=BIN_WIDTH * 0.85,
                    color=color, alpha=0.5, edgecolor='white', linewidth=0.5)

    ax_hist.set_xlim(0.5, 1.0)
    ax_hist.set_xlabel('Mean Predicted Confidence')
    ax_hist.set_ylabel('Frac.')
    ax_hist.yaxis.set_major_locator(plt.MaxNLocator(3))


def main():
    fig = plt.figure(figsize=(7, 7))

    outer = gridspec.GridSpec(2, 2, hspace=0.35, wspace=0.30)

    for idx, cond in enumerate(CONDITIONS):
        row, col = divmod(idx, 2)
        inner = gridspec.GridSpecFromSubplotSpec(
            2, 1, subplot_spec=outer[row, col],
            height_ratios=[3, 1], hspace=0.08)

        ax_rel = fig.add_subplot(inner[0])
        ax_hist = fig.add_subplot(inner[1])

        plot_panel(ax_rel, ax_hist, cond)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    fig.savefig(os.path.join(out_dir, 'fig2_calibration.pdf'))
    fig.savefig(os.path.join(out_dir, 'fig2_calibration.png'))
    plt.close(fig)
    print("Saved fig2_calibration.pdf and fig2_calibration.png")


if __name__ == "__main__":
    main()
