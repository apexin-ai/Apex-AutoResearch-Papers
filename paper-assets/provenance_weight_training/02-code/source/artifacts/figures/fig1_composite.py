"""Figure 1: Three-panel results composite (figure*, full width).

Panel (a): Epoch confound — D&R threshold-PPL dual curve
Panel (b): Detector requirements — AUC vs ECE scatter with zones
Panel (c): Minimum intervention — PPL vs b with adaptive/ESS markers

Data from paper Tables 2-4, §5.1-5.3.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent

# ── Semantic palette ──
C = {
    'primary':   '#4A90D9',   # steel blue — adaptive b* / ours
    'secondary': '#E8913A',   # warm amber — ESS-only / contrast
    'tertiary':  '#43A888',   # sage green — grid-best / D&R / safe zone
    'negative':  '#C75C5C',   # muted coral — random / degradation
    'neutral':   '#90A4AE',   # blue-gray — uniform baseline
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
    'legend.columnspacing': 1.0,
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

fig, (ax_a, ax_b, ax_c) = plt.subplots(1, 3, figsize=(6.75, 2.6))
plt.subplots_adjust(wspace=0.42)

# ═══════════════════════════════════════════════════════════════
# Panel (a): Epoch confound — D&R threshold-PPL dual curve
# Data from §5.1, Table 2, Figure 5
# ═══════════════════════════════════════════════════════════════

thresholds = [0.3, 0.5, 0.7, 0.9]
raw_ppl =          [17.250, 17.278, 17.35, 17.42]
epoch_matched_ppl = [17.60, 17.657, 17.68, 17.70]
content_epochs =   [3.2,   2.4,    1.6,   1.1]

# Data retained fraction for context
data_retained = [31.5, 50.0, 70.0, 90.0]

ax_a.plot(thresholds, raw_ppl, 'o-', color=C['tertiary'], markersize=5,
          label='D&R raw (multi-epoch)', zorder=4)
ax_a.plot(thresholds, epoch_matched_ppl, 's-', color=C['secondary'], markersize=5,
          label='D&R epoch-matched', zorder=4)

# Adaptive b* reference line
ax_a.axhline(17.674, color=C['primary'], linestyle='--', linewidth=1.0,
             alpha=0.7, zorder=2, label=r'Adaptive $b^*$')

# Uniform baseline
ax_a.axhline(17.697, color=C['neutral'], linestyle=':', linewidth=0.9,
             alpha=0.5, zorder=2, label='Uniform')

# Shade the gap between raw and epoch-matched to show the confound
ax_a.fill_between(thresholds, raw_ppl, epoch_matched_ppl,
                  alpha=0.08, color=C['tertiary'], zorder=1)

# Arrow annotation showing the gap
ax_a.annotate('', xy=(0.25, epoch_matched_ppl[0]), xytext=(0.25, raw_ppl[0]),
              arrowprops=dict(arrowstyle='<->', color='#555555', lw=0.8))
t = ax_a.text(0.28, (raw_ppl[0] + epoch_matched_ppl[0]) / 2, '>95%\nmulti-ep.',
              fontsize=5, ha='left', va='center', color='#555555', linespacing=1.1)
t.set_path_effects(STROKE)

ax_a.set_xlabel('Detection threshold $q$')
ax_a.set_ylabel('Holdout PPL')
ax_a.set_title('(a) D&R: multi-epoch mechanism', fontsize=8.5, fontweight='bold', pad=6)
ax_a.set_xlim(0.2, 1.0)
ax_a.set_ylim(17.12, 17.85)
ax_a.legend(fontsize=5, loc='upper center', ncol=2, framealpha=0.95,
            edgecolor='#CCCCCC', bbox_to_anchor=(0.6, 1.0),
            columnspacing=0.8, handletextpad=0.4)
ax_a.grid(axis='y', lw=0.5, alpha=0.3, color='#CCCCCC', linestyle='--')

# ═══════════════════════════════════════════════════════════════
# Panel (b): Detector requirements — AUC vs ECE scatter
# Data from §5.2
# ═══════════════════════════════════════════════════════════════

detectors = {
    'TF-IDF+LR': (0.94, 0.048, -0.023, C['tertiary']),
    'GPT-2':     (0.91, 0.131, +0.098, C['negative']),
    'N-gram':    (0.73, 0.069, +0.129, C['negative']),
}

# Zone shading
ax_b.axvspan(0.9, 1.0, alpha=0.06, color=C['tertiary'], zorder=0)
ax_b.axhspan(0.0, 0.05, alpha=0.06, color=C['tertiary'], zorder=0)

# Effective zone (intersection: high AUC AND low ECE)
ax_b.fill_between([0.9, 1.0], 0, 0.05, alpha=0.12, color=C['tertiary'], zorder=1,
                  label='Effective zone')

# Zone boundary lines
ax_b.axvline(0.9, color=C['tertiary'], linestyle='--', linewidth=0.7, alpha=0.4)
ax_b.axhline(0.05, color=C['tertiary'], linestyle='--', linewidth=0.7, alpha=0.4)

for name, (auc, ece, delta, color) in detectors.items():
    marker = 'o' if delta < 0 else 'X'
    size = 8 if delta < 0 else 7
    ax_b.scatter(auc, ece, c=color, s=size**2, marker=marker, zorder=5,
                 edgecolors='white', linewidths=0.8)

    # Labels
    if name == 'TF-IDF+LR':
        ax_b.annotate(f'{name}\n$\\Delta$={delta:+.3f}', xy=(auc, ece),
                      xytext=(auc - 0.07, ece + 0.055), fontsize=5.5,
                      color=color, fontweight='bold',
                      arrowprops=dict(arrowstyle='->', color=color, lw=0.7,
                                      connectionstyle='arc3,rad=0.2'),
                      zorder=6)
    elif name == 'GPT-2':
        ax_b.annotate(f'{name}\n$\\Delta$={delta:+.3f}', xy=(auc, ece),
                      xytext=(auc + 0.02, ece + 0.020), fontsize=5.5,
                      color=color, ha='left', zorder=6)
    else:
        ax_b.annotate(f'{name}\n$\\Delta$={delta:+.3f}', xy=(auc, ece),
                      xytext=(auc + 0.06, ece + 0.065), fontsize=5.5,
                      color=color, ha='left', zorder=6,
                      arrowprops=dict(arrowstyle='->', color=color, lw=0.7,
                                      connectionstyle='arc3,rad=-0.2'))

ax_b.set_xlabel('AUC')
ax_b.set_ylabel('ECE')
ax_b.set_title('(b) Detector requirements', fontsize=9, fontweight='bold', pad=6)
ax_b.set_xlim(0.65, 1.0)
ax_b.set_ylim(0.0, 0.20)
ax_b.grid(axis='both', lw=0.5, alpha=0.3, color='#CCCCCC', linestyle='--')

# ═══════════════════════════════════════════════════════════════
# Panel (c): Minimum intervention — PPL vs b
# Data from §5.1, Table 1, Figure 4
# ═══════════════════════════════════════════════════════════════

b_values = [0.0, 0.1, 0.2, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
ppl_values = [17.694, 17.67, 17.65, 17.62, 17.66, 17.69, 17.72, 17.75, 17.80, 17.95]

# Smooth interpolation for the curve
from scipy.interpolate import make_interp_spline
b_smooth = np.linspace(0, 5.0, 200)
spl = make_interp_spline(b_values, ppl_values, k=3)
ppl_smooth = spl(b_smooth)

ax_c.plot(b_smooth, ppl_smooth, '-', color='#555555', linewidth=1.2, alpha=0.6, zorder=2)
ax_c.plot(b_values, ppl_values, 'o', color='#555555', markersize=4, alpha=0.5, zorder=3,
          label='Grid search')

# Degradation zone shading (b >= 2)
ax_c.axvspan(2.0, 5.2, alpha=0.06, color=C['negative'], zorder=0)
t = ax_c.text(3.5, 17.60, 'degradation\nzone', fontsize=5.5, ha='center', va='center',
              color=C['negative'], alpha=0.6, fontstyle='italic', linespacing=1.1)

# Uniform baseline
ax_c.axhline(17.694, color=C['neutral'], linestyle=':', linewidth=0.9,
             alpha=0.5, zorder=2, label='Uniform')

# Adaptive b* marker (≈0.9, PPL ≈ 17.674)
ax_c.plot(0.9, 17.674, 'o', color=C['primary'], markersize=8,
          markeredgecolor='white', markeredgewidth=1.2, zorder=6)
t1 = ax_c.annotate(r'$b^*\!\approx\!0.9$', xy=(0.9, 17.674),
                    xytext=(1.6, 17.615), fontsize=7, fontweight='bold',
                    color=C['primary'],
                    arrowprops=dict(arrowstyle='->', color=C['primary'], lw=0.9,
                                    connectionstyle='arc3,rad=-0.2'), zorder=7)
t1.set_path_effects(STROKE)

# ESS-only b marker (≈3.5, PPL ≈ 17.82)
ess_ppl = spl(3.5)
ax_c.plot(3.5, ess_ppl, 'X', color=C['negative'], markersize=7,
          markeredgecolor='white', markeredgewidth=0.8, zorder=6)
t2 = ax_c.annotate(r'$b_{\mathrm{ESS}}\!\approx\!3.5$', xy=(3.5, ess_ppl),
                    xytext=(4.2, 17.93), fontsize=6.5, fontweight='bold',
                    color=C['negative'],
                    arrowprops=dict(arrowstyle='->', color=C['negative'], lw=0.9,
                                    connectionstyle='arc3,rad=0.2'), zorder=7)
t2.set_path_effects(STROKE)

ax_c.set_xlabel('Sharpening exponent $b$')
ax_c.set_ylabel('Holdout PPL')
ax_c.set_title('(c) Minimum intervention', fontsize=9, fontweight='bold', pad=6)
ax_c.set_xlim(-0.2, 5.3)
ax_c.set_ylim(17.58, 18.0)
ax_c.legend(fontsize=5.5, loc='upper left', framealpha=0.9, edgecolor='#CCCCCC')
ax_c.grid(axis='y', lw=0.5, alpha=0.3, color='#CCCCCC', linestyle='--')

# ═══════════════════════════════════════════════════════════════
# Save
# ═══════════════════════════════════════════════════════════════
for ext in ('pdf', 'png'):
    fig.savefig(OUT / f'fig1_overview.{ext}', dpi=300, bbox_inches='tight',
                pad_inches=0.05)
plt.close(fig)
print('✓ fig1_overview (3-panel composite)')
