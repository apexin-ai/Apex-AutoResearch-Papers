"""Generate batch_size_amplification and detector_requirements with unified palette."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent

C = {
    'primary':   '#4A90D9',
    'secondary': '#E8913A',
    'tertiary':  '#43A888',
    'negative':  '#C75C5C',
    'neutral':   '#90A4AE',
}

# ── Premium rcParams (publication-grade, PaperBanana-equivalent) ──
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'dejavuserif',
    'font.size': 9,
    'axes.titlesize': 9.5,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'axes.linewidth': 0.8,
    'axes.edgecolor': 'black',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.axisbelow': True,
    'xtick.major.width': 0.5,  'ytick.major.width': 0.5,
    'xtick.minor.width': 0.3,  'ytick.minor.width': 0.3,
    'xtick.major.size': 3.5,   'ytick.major.size': 3.5,
    'xtick.minor.size': 2.0,   'ytick.minor.size': 2.0,
    'xtick.direction': 'out',  'ytick.direction': 'out',
    'xtick.major.pad': 4,      'ytick.major.pad': 4,
    'lines.linewidth': 1.5,
    'lines.markersize': 5,
    'legend.frameon': False,
    'legend.borderpad': 0.3,
    'legend.handlelength': 1.5,
    'legend.handletextpad': 0.5,
    'grid.linewidth': 0.5,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'grid.color': '#CCCCCC',
    'figure.dpi': 300,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'savefig.facecolor': 'white',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

STROKE = [pe.withStroke(linewidth=2.5, foreground='white')]


def _save(fig, name):
    for ext in ('pdf', 'png'):
        fig.savefig(OUT / f'{name}.{ext}', dpi=300, bbox_inches='tight',
                    pad_inches=0.05)
    plt.close(fig)
    print(f'  ✓ {name}')


# ═══════════════════════════════════════════════════════════════
# batch_size_amplification — bar chart
# Data from §5.3: B=4 Δ=-0.023±0.006 (1.0×), B=8 Δ=-0.052±0.007 (2.3×),
#                  B=16 Δ=-0.068±0.005 (3.0×)
# ═══════════════════════════════════════════════════════════════
def fig_batch_amp():
    fig, ax = plt.subplots(figsize=(3.3, 2.4))

    batches = ['B=4', 'B=8', 'B=16']
    deltas = [-0.023, -0.052, -0.068]
    stds = [0.006, 0.007, 0.005]
    amplifications = [1.0, 2.3, 3.0]
    colors = [C['primary'], C['primary'], C['primary']]

    x = np.arange(len(batches))
    bars = ax.bar(x, [-d for d in deltas], width=0.55, color=colors,
                  edgecolor='white', linewidth=0.8, alpha=0.85, zorder=3)
    ax.errorbar(x, [-d for d in deltas], yerr=stds, fmt='none',
                ecolor='#555555', capsize=3, capthick=0.8, linewidth=0.8, zorder=4)

    # Baseline reference
    ax.axhline(0.023, color=C['neutral'], linestyle='--', linewidth=0.8,
               alpha=0.5, zorder=2)
    t = ax.text(2.35, 0.024, 'Baseline (1.0×)', fontsize=6.5,
                color=C['neutral'], ha='right', va='bottom')

    # Amplification labels
    for i, (amp, delta, sd) in enumerate(zip(amplifications, deltas, stds)):
        label = f'{amp:.1f}×\n($\\Delta$={delta:+.3f}±{sd:.3f})'
        t = ax.text(i, -delta + sd + 0.003, label, ha='center', va='bottom',
                    fontsize=6.5, color='#333333', linespacing=1.2)

    ax.set_xticks(x)
    ax.set_xticklabels(batches)
    ax.set_xlabel('Micro-batch size')
    ax.set_ylabel('Amplification factor\n(|$\\Delta$ PPL| vs. uniform)')
    ax.set_ylim(0, 0.095)
    ax.grid(axis='y', lw=0.5, alpha=0.3, color='#CCCCCC', linestyle='--')

    _save(fig, 'batch_size_amplification')


# ═══════════════════════════════════════════════════════════════
# detector_requirements — AUC vs ECE scatter with zones
# Data from §5.2:
#   TF-IDF+LR: AUC=0.94, ECE=0.048, Δ=-0.023
#   GPT-2:     AUC=0.91, ECE=0.131, Δ=+0.098
#   N-gram:    AUC=0.73, ECE=0.069, Δ=+0.129
# ═══════════════════════════════════════════════════════════════
def fig_detector_req():
    fig, ax = plt.subplots(figsize=(3.3, 2.6))

    detectors = [
        ('TF-IDF+LR', 0.94, 0.048, -0.023, C['tertiary'], 'o'),
        ('GPT-2',     0.91, 0.131, +0.098, C['negative'], 'X'),
        ('N-gram',    0.73, 0.069, +0.129, C['negative'], 'X'),
    ]

    # Zone shading
    ax.axvspan(0.9, 1.0, alpha=0.05, color=C['tertiary'], zorder=0)
    ax.axhspan(0.0, 0.05, alpha=0.05, color=C['tertiary'], zorder=0)
    ax.fill_between([0.9, 1.0], 0, 0.05, alpha=0.12, color=C['tertiary'],
                    zorder=1, label='Effective zone')

    # Zone boundaries
    ax.axvline(0.9, color=C['tertiary'], linestyle='--', linewidth=0.7, alpha=0.4)
    ax.axhline(0.05, color=C['tertiary'], linestyle='--', linewidth=0.7, alpha=0.4)

    # Boundary labels
    ax.text(0.898, 0.17, 'AUC = 0.9', fontsize=6, color=C['tertiary'],
            alpha=0.6, rotation=90, ha='right', va='top')
    ax.text(1.0, 0.052, 'ECE = 0.05', fontsize=6, color=C['tertiary'],
            alpha=0.6, ha='right', va='bottom')

    for name, auc, ece, delta, color, marker in detectors:
        size = 70 if marker == 'o' else 60
        ax.scatter(auc, ece, c=color, s=size, marker=marker, zorder=5,
                   edgecolors='white', linewidths=0.8)

        sign = '+' if delta > 0 else ''
        if name == 'TF-IDF+LR':
            ax.annotate(f'{name}\n$\\Delta$PPL = {sign}{delta:.3f}',
                        xy=(auc, ece),
                        xytext=(auc - 0.08, ece + 0.03), fontsize=7,
                        color=color, fontweight='bold',
                        arrowprops=dict(arrowstyle='->', color=color, lw=0.8,
                                        connectionstyle='arc3,rad=0.2'),
                        zorder=6)
        elif name == 'GPT-2':
            ax.annotate(f'{name}\n$\\Delta$PPL = {sign}{delta:.3f}',
                        xy=(auc, ece),
                        xytext=(auc - 0.10, ece + 0.02), fontsize=7,
                        color=color,
                        arrowprops=dict(arrowstyle='->', color=color, lw=0.8,
                                        connectionstyle='arc3,rad=-0.15'),
                        zorder=6)
        else:
            ax.annotate(f'{name}\n$\\Delta$PPL = {sign}{delta:.3f}',
                        xy=(auc, ece),
                        xytext=(auc + 0.02, ece + 0.03), fontsize=7,
                        color=color,
                        arrowprops=dict(arrowstyle='->', color=color, lw=0.8,
                                        connectionstyle='arc3,rad=0.2'),
                        zorder=6)

    ax.set_xlabel('AUC (discrimination)')
    ax.set_ylabel('ECE (calibration error)')
    ax.set_xlim(0.65, 1.01)
    ax.set_ylim(0.0, 0.185)
    ax.grid(axis='both', lw=0.5, alpha=0.3, color='#CCCCCC', linestyle='--')

    _save(fig, 'detector_requirements')


if __name__ == '__main__':
    fig_batch_amp()
    fig_detector_req()
