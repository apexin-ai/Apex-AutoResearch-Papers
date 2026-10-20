import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from scipy.optimize import brentq

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

C = {
    'baseline':  '#4A90D9',   # steel blue — Adaptive b* / primary data / ours
    'treatment': '#E8913A',   # warm amber — ESS-only / contrast methods
    'collapse':  '#C75C5C',   # muted coral — Random / degradation / failure
    'safe':      '#43A888',   # sage green — Grid-best / Oracle / D&R / good outcome
    'neutral':   '#90A4AE',   # blue-gray — Uniform baseline / reference
}

B = 4
tau = 0.7
n_min_ratio = 0.5

def alpha_eff(b, q):
    w = (1 - q)**b
    return np.sum(w * (1 - q)) / np.sum(w)

def ess_norm(b, q, B):
    w = (1 - q)**b
    return (np.sum(w)**2 / np.sum(w**2)) / B

q_a = np.array([0.08, 0.42, 0.62, 0.78])
q_b = np.array([0.20, 0.50, 0.85, 0.95])

b_range = np.linspace(0, 5.5, 500)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.8, 2.6), sharey=True)
plt.subplots_adjust(wspace=0.08)

for idx, (ax, q, panel_label, panel_title) in enumerate([
    (ax1, q_a, '(a)', r'$\alpha_{\mathrm{eff}}$-binding: $b^* = b_\tau$'),
    (ax2, q_b, '(b)', r'ESS-binding: $b^* = b_{\mathrm{ESS}}$'),
]):
    aeff_vals = np.array([alpha_eff(b, q) for b in b_range])
    ess_vals = np.array([ess_norm(b, q, B) for b in b_range])

    if aeff_vals[0] < tau and aeff_vals[-1] >= tau:
        bt = brentq(lambda b: alpha_eff(b, q) - tau, 0, 20)
    elif aeff_vals[-1] < tau:
        bt = None
    else:
        bt = 0

    be = brentq(lambda b: ess_norm(b, q, B) - n_min_ratio, 0, 20) if ess_vals[-1] < n_min_ratio else None

    is_aeff_binding = (bt is not None and be is not None and bt <= be)

    # Background shading
    if is_aeff_binding:
        ax.axvspan(bt, be, alpha=0.12, color=C['safe'], zorder=0)
        ax.axvspan(be, 5.5, alpha=0.06, color=C['collapse'], zorder=0)
        t = ax.text((bt + be) / 2, 0.04, 'feasible', fontsize=7, ha='center',
                    color=C['safe'], alpha=0.8, fontstyle='italic')
    else:
        if be is not None:
            ax.axvspan(be, 5.5, alpha=0.06, color=C['collapse'], zorder=0)

    # Curves — alpha_eff = baseline (steel blue), ESS = treatment (amber)
    ax.plot(b_range, aeff_vals, color=C['baseline'], linewidth=1.8,
            label=r'$\alpha_{\mathrm{eff}}(b)$', zorder=3)
    ax.plot(b_range, ess_vals, color=C['treatment'], linewidth=1.8,
            label=r'$\mathrm{ESS}(b)/B$', zorder=3)

    # Threshold lines
    ax.axhline(tau, color=C['baseline'], linestyle='--', linewidth=0.8,
               alpha=0.4, zorder=2)
    ax.axhline(n_min_ratio, color=C['treatment'], linestyle='--', linewidth=0.8,
               alpha=0.4, zorder=2)

    # Threshold labels
    t1 = ax.text(5.35, tau + 0.025, r'$\tau$', fontsize=8, color=C['baseline'],
                 ha='right', va='bottom', fontweight='bold')
    t1.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])
    t2 = ax.text(5.35, n_min_ratio - 0.035, r'$n_{\min}\!/B$', fontsize=7,
                 color=C['treatment'], ha='right', va='top', fontweight='bold')
    t2.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

    if is_aeff_binding:
        bstar = bt
        ax.axvline(bstar, color='#444444', linestyle=':', linewidth=0.8, alpha=0.35, zorder=2)
        ax.plot(bstar, tau, 'o', color=C['safe'], markersize=8,
                markeredgecolor='white', markeredgewidth=1.2, zorder=5)
        t_bstar = ax.annotate(r'$b^*\!=\!b_\tau$', xy=(bstar, tau),
                    xytext=(bstar + 0.6, tau + 0.14),
                    fontsize=9, fontweight='bold', color=C['safe'],
                    arrowprops=dict(arrowstyle='->', color=C['safe'],
                                    lw=1.0, connectionstyle='arc3,rad=0.2'),
                    zorder=6)
        t_bstar.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
        # Non-binding b_ESS
        ax.plot(be, n_min_ratio, 'x', color=C['treatment'],
                markersize=5, markeredgewidth=1.3, zorder=4, alpha=0.45)
        t3 = ax.text(be + 0.12, n_min_ratio - 0.06, r'$b_{\mathrm{ESS}}$',
                     fontsize=7, color=C['treatment'], alpha=0.45, va='top')
        t3.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])
    else:
        bstar = be
        ax.axvline(bstar, color='#444444', linestyle=':', linewidth=0.8, alpha=0.35, zorder=2)
        ax.plot(bstar, n_min_ratio, 'o', color=C['safe'], markersize=8,
                markeredgecolor='white', markeredgewidth=1.2, zorder=5)
        t_bstar = ax.annotate(r'$b^*\!=\!b_{\mathrm{ESS}}$', xy=(bstar, n_min_ratio),
                    xytext=(bstar - 1.1, n_min_ratio - 0.18),
                    fontsize=9, fontweight='bold', color=C['safe'],
                    arrowprops=dict(arrowstyle='->', color=C['safe'],
                                    lw=1.0, connectionstyle='arc3,rad=0.2'),
                    zorder=6)
        t_bstar.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
        # Non-binding b_tau
        if bt is not None and bt < 5.5:
            ax.plot(bt, tau, 'x', color=C['baseline'],
                    markersize=5, markeredgewidth=1.3, zorder=4, alpha=0.35)
            t3 = ax.text(bt + 0.12, tau + 0.04, r'$b_\tau$',
                         fontsize=7, color=C['baseline'], alpha=0.4)
            t3.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

    ax.set_title(panel_title, fontsize=9, pad=8)
    ax.text(-0.02, 1.08, panel_label, transform=ax.transAxes, fontsize=10,
            fontweight='bold', va='bottom', ha='left')
    ax.set_xlabel('Sharpening exponent $b$')
    ax.set_xlim(0, 5.5)
    ax.set_ylim(0, 1.05)

ax1.set_ylabel('Normalized value')

handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels, loc='lower left', framealpha=0, edgecolor='none',
           borderpad=0.3, handlelength=1.5)

plt.tight_layout(w_pad=0.6)

outdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/figures'
plt.savefig(f'{outdir}/dual_constraint_illustration.pdf')
plt.savefig(f'{outdir}/dual_constraint_illustration.png')
print('Saved dual_constraint_illustration.{pdf,png}')
plt.close()
