"""Optimized paper figures — unified publication-quality style.

Palette: Unified semantic (project-specified)
Font: Liberation Serif
All figures share identical rcParams for cross-figure consistency.

Data verified against published paper text (Tables 1, 2, 4, tau, rho06, dr_threshold).
tau=0.8 at rho=0.4 corrected for resume artifact (Appendix H): 17.683 not 17.653.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.ticker as ticker
import numpy as np
from scipy.optimize import brentq
from pathlib import Path

OUT = Path(__file__).parent

# ── Semantic palette ──
C = {
    'baseline':  '#4A90D9',   # steel blue — Adaptive b* / primary data / ours
    'treatment': '#E8913A',   # warm amber — ESS-only / contrast methods
    'collapse':  '#C75C5C',   # muted coral — Random / degradation / failure
    'safe':      '#43A888',   # sage green — Grid-best / Oracle / D&R / good outcome
    'neutral':   '#90A4AE',   # blue-gray — Uniform baseline / reference
}

# ── Premium rcParams (publication-grade, PaperBanana-equivalent) ──
PREMIUM_RC = {
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
}
plt.rcParams.update(PREMIUM_RC)

GRID_KW = dict(axis='y', lw=0.5, alpha=0.3, color='#CCCCCC', linestyle='--')
GRID_XY = dict(axis='both', lw=0.5, alpha=0.3, color='#CCCCCC', linestyle='--')
STROKE = [pe.withStroke(linewidth=2.5, foreground='white')]


def _save(fig, name):
    for ext in ('pdf', 'png'):
        fig.savefig(OUT / f'{name}.{ext}', dpi=300, bbox_inches='tight',
                    pad_inches=0.05)
    plt.close(fig)
    print(f'  ✓ {name}')


# ═══════════════════════════════════════════════════════════════════
# Figure 2 — dual_constraint_illustration  (figure*, \textwidth)
# Narrative: Show two constraint regimes with clear visual separation
# ═══════════════════════════════════════════════════════════════════
def fig_dual_constraint():
    B = 4;  tau = 0.7;  n_min_ratio = 0.5

    def alpha_eff(b, q):
        w = (1 - q)**b
        return np.sum(w * (1 - q)) / np.sum(w)

    def ess_norm(b, q, B):
        w = (1 - q)**b
        return (np.sum(w)**2 / np.sum(w**2)) / B

    q_a = np.array([0.08, 0.42, 0.62, 0.78])
    q_b = np.array([0.20, 0.50, 0.85, 0.95])
    b_range = np.linspace(0, 5.5, 500)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.75, 2.9), sharey=True)
    plt.subplots_adjust(wspace=0.10)

    for ax, q, panel_label, panel_title in [
        (ax1, q_a, '(a)', r'$\alpha_{\mathrm{eff}}$-binding: $b^* = b_\tau$'),
        (ax2, q_b, '(b)', r'ESS-binding: $b^* = b_{\mathrm{ESS}}$'),
    ]:
        aeff_vals = np.array([alpha_eff(b, q) for b in b_range])
        ess_vals  = np.array([ess_norm(b, q, B) for b in b_range])

        if aeff_vals[0] < tau and aeff_vals[-1] >= tau:
            bt = brentq(lambda b: alpha_eff(b, q) - tau, 0, 20)
        elif aeff_vals[-1] < tau:
            bt = None
        else:
            bt = 0

        be = (brentq(lambda b: ess_norm(b, q, B) - n_min_ratio, 0, 20)
              if ess_vals[-1] < n_min_ratio else None)
        is_aeff_binding = (bt is not None and be is not None and bt <= be)

        # Background shading
        if is_aeff_binding:
            ax.axvspan(bt, be, alpha=0.12, color=C['safe'], zorder=0)
            ax.axvspan(be, 5.5, alpha=0.06, color=C['collapse'], zorder=0)
            ax.text((bt + be) / 2, 0.04, 'feasible', fontsize=7, ha='center',
                    color=C['safe'], alpha=0.7, fontstyle='italic')
        else:
            if be is not None:
                ax.axvspan(be, 5.5, alpha=0.06, color=C['collapse'], zorder=0)

        # Curves — alpha_eff = baseline (steel blue), ESS = treatment (amber)
        ax.plot(b_range, aeff_vals, color=C['baseline'], linewidth=1.8,
                label=r'$\alpha_{\mathrm{eff}}(b)$', zorder=3)
        ax.plot(b_range, ess_vals, color=C['treatment'], linewidth=1.8,
                label=r'$\mathrm{ESS}(b)/B$', zorder=3)

        # Threshold lines
        ax.axhline(tau, color=C['baseline'], linestyle='--', linewidth=0.7,
                   alpha=0.4, zorder=2)
        ax.axhline(n_min_ratio, color=C['treatment'], linestyle='--',
                   linewidth=0.7, alpha=0.4, zorder=2)

        # Threshold labels (right side, pulled inward to avoid clipping)
        t1 = ax.text(5.0, tau + 0.05, r'$\tau$', fontsize=8,
                     color=C['baseline'], ha='right', va='bottom')
        t1.set_path_effects(STROKE)
        t2 = ax.text(5.0, n_min_ratio - 0.06, r'$n_{\min}\!/B$', fontsize=7,
                     color=C['treatment'], ha='right', va='top')
        t2.set_path_effects(STROKE)

        if is_aeff_binding:
            bstar = bt
            ax.axvline(bstar, color='#444444', linestyle=':', linewidth=0.7,
                       alpha=0.3, zorder=2)
            ax.plot(bstar, tau, 'o', color=C['safe'], markersize=7,
                    markeredgecolor='white', markeredgewidth=1.0, zorder=5)
            t_bs = ax.annotate(
                r'$b^*\!=\!b_\tau$', xy=(bstar, tau),
                xytext=(bstar + 0.8, tau + 0.18), fontsize=8.5,
                fontweight='bold', color=C['safe'],
                arrowprops=dict(arrowstyle='->', color=C['safe'], lw=0.9,
                                connectionstyle='arc3,rad=0.2'), zorder=6)
            t_bs.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
            ax.plot(be, n_min_ratio, 'x', color=C['treatment'], markersize=4.5,
                    markeredgewidth=1.2, zorder=4, alpha=0.4)
            t3 = ax.text(be + 0.12, n_min_ratio - 0.06, r'$b_{\mathrm{ESS}}$',
                         fontsize=7, color=C['treatment'], alpha=0.4, va='top')
            t3.set_path_effects(STROKE)
        else:
            bstar = be
            ax.axvline(bstar, color='#444444', linestyle=':', linewidth=0.7,
                       alpha=0.3, zorder=2)
            ax.plot(bstar, n_min_ratio, 'o', color=C['safe'], markersize=7,
                    markeredgecolor='white', markeredgewidth=1.0, zorder=5)
            t_bs = ax.annotate(
                r'$b^*\!=\!b_{\mathrm{ESS}}$', xy=(bstar, n_min_ratio),
                xytext=(bstar - 1.3, n_min_ratio - 0.22), fontsize=8.5,
                fontweight='bold', color=C['safe'],
                arrowprops=dict(arrowstyle='->', color=C['safe'], lw=0.9,
                                connectionstyle='arc3,rad=0.2'), zorder=6)
            t_bs.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
            if bt is not None and bt < 5.5:
                ax.plot(bt, tau, 'x', color=C['baseline'], markersize=4.5,
                        markeredgewidth=1.2, zorder=4, alpha=0.35)
                t3 = ax.text(bt + 0.12, tau + 0.04, r'$b_\tau$', fontsize=7,
                             color=C['baseline'], alpha=0.4)
                t3.set_path_effects(STROKE)

        ax.set_title(panel_title, fontsize=9, pad=8)
        ax.text(0.02, 1.04, panel_label, transform=ax.transAxes, fontsize=10,
                fontweight='bold', va='bottom', ha='left')
        ax.set_xlabel('Sharpening exponent $b$')
        ax.set_xlim(0, 5.5)
        ax.set_ylim(0, 1.05)

    ax1.set_ylabel('Normalized value')
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles, labels, loc='center right', framealpha=0.92,
               edgecolor='none', borderpad=0.3, handlelength=1.5)

    fig.tight_layout(w_pad=0.6)
    _save(fig, 'dual_constraint_illustration')


# ═══════════════════════════════════════════════════════════════════
# Figure 3 — grid_b_trend_clean  (figure, \columnwidth)
# Narrative: Adaptive b* operates near the minimum; ESS-only falls
#            in the degradation zone
# Data: Appendix Table 4 (seed 42) + Table 1 cross-seed
# ═══════════════════════════════════════════════════════════════════
def fig_grid_b_trend():
    b_vals = [0.1, 0.2, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
    ppl    = [17.657, 17.640, 17.640, 17.651, 17.692, 17.718,
              17.741, 17.774, 17.818]
    uniform = 17.694

    fig, ax = plt.subplots(figsize=(3.35, 2.6))

    # Degradation zone (b >= 2) — clean shading, no hatch
    ax.axvspan(2.0, 5.8, alpha=0.07, color=C['collapse'], zorder=0)
    ax.text(3.9, 17.635, 'degradation zone', fontsize=6.5, color=C['collapse'],
            alpha=0.6, ha='center', fontstyle='italic')

    # Uniform baseline
    ax.axhline(uniform, color=C['neutral'], ls='--', lw=0.8, zorder=1)
    t_uni = ax.text(5.55, uniform + 0.003, f'Uniform ({uniform:.3f})',
                    fontsize=6.5, color=C['neutral'], ha='right', va='bottom')
    t_uni.set_path_effects(STROKE)

    # Main curve — seed 42
    ax.plot(b_vals, ppl, 'o-', color=C['baseline'], markersize=4.5,
            markeredgecolor='white', markeredgewidth=0.6, zorder=3,
            label='Seed 42 (full grid)')

    # Cross-seed at b=0.5
    ax.plot(0.5, 17.638, '^', color=C['baseline'], markersize=5.5, zorder=3,
            markerfacecolor='white', markeredgecolor=C['baseline'],
            markeredgewidth=1.0, label='Seed 123')
    ax.plot(0.5, 17.650, 'v', color=C['neutral'], markersize=5.5, zorder=3,
            markerfacecolor=C['neutral'], markeredgecolor='white',
            markeredgewidth=0.6, label='Seed 456')

    # Adaptive b* — vertical line + annotation
    ax.axvline(0.9, color=C['baseline'], ls='-.', lw=0.7, alpha=0.45, zorder=1)
    ax.annotate(r'Adaptive $\bar{b}^*{\approx}0.9$',
                xy=(0.9, 17.692), xytext=(1.55, 17.70),
                fontsize=7.5, fontweight='bold', color=C['baseline'],
                ha='left', va='center',
                arrowprops=dict(arrowstyle='->', color=C['baseline'], lw=0.7,
                                connectionstyle='arc3,rad=0.15'))

    # ESS-only b* — X marker + annotation arrow
    b_ess_ppl = 17.774 + (17.818 - 17.774) * (3.5 - 3.0) / (5.0 - 3.0)
    ax.plot(3.5, b_ess_ppl, 'X', color=C['treatment'], markersize=7,
            markeredgecolor='white', markeredgewidth=0.8, zorder=5)
    ax.annotate(r'ESS-only $\bar{b}^*{\approx}3.5$',
                xy=(3.5, b_ess_ppl), xytext=(2.2, 17.83),
                fontsize=7.5, fontweight='bold', color=C['treatment'],
                ha='left',
                arrowprops=dict(arrowstyle='->', color=C['treatment'], lw=0.8,
                                connectionstyle='arc3,rad=-0.2'))

    ax.set_xlabel(r'Sharpening exponent $b$')
    ax.set_ylabel('Held-out PPL')
    ax.set_xlim(-0.2, 5.7)
    ax.set_ylim(17.62, 17.85)
    ax.legend(loc='upper left', framealpha=0.92, edgecolor='none',
              handlelength=1.2, handletextpad=0.4, borderpad=0.3)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    ax.grid(**GRID_KW)
    fig.tight_layout(pad=0.4)
    _save(fig, 'grid_b_trend_clean')


# ═══════════════════════════════════════════════════════════════════
# Figure A.1 — constraint_regime_decomposition  (figure, \columnwidth)
# Narrative: α_eff-binding dominates at ρ=0.4; constraints balance
#            at ρ=0.6
# Data: Section 4.4 + Appendix D (seed 42, 3-seed avg)
# ═══════════════════════════════════════════════════════════════════
def fig_constraint_regime():
    labels = [r'$\rho{=}0.4$', r'$\rho{=}0.6$']
    aeff   = [50.9, 46.8]
    ess    = [43.3, 48.7]
    clean  = [ 5.8,  4.5]

    fig, ax = plt.subplots(figsize=(3.1, 2.6))
    x = np.arange(len(labels))
    w = 0.50

    # Bars — alpha_eff = baseline (steel blue), ESS = treatment (amber)
    ax.bar(x, aeff, w, color=C['baseline'], alpha=0.85,
           edgecolor='white', lw=0.5,
           label=r'$\alpha_{\mathrm{eff}}$-binding', zorder=2)
    ax.bar(x, ess, w, bottom=aeff, color=C['treatment'], alpha=0.85,
           edgecolor='white', lw=0.5,
           label='ESS-binding', zorder=2)
    ax.bar(x, clean, w, bottom=[a + e for a, e in zip(aeff, ess)],
           color=C['safe'], alpha=0.85, edgecolor='white', lw=0.5,
           label=r'Clean ($b^*{=}0$)', zorder=2)

    # Percentage labels inside bars
    for i in range(2):
        ax.text(i, aeff[i] / 2, f'{aeff[i]:.1f}%',
                ha='center', va='center', fontsize=7.5,
                fontweight='bold', color='white')
        ax.text(i, aeff[i] + ess[i] / 2, f'{ess[i]:.1f}%',
                ha='center', va='center', fontsize=7.5,
                fontweight='bold', color='white')
        cy = aeff[i] + ess[i] + clean[i] / 2
        ax.text(i, cy, f'{clean[i]:.1f}%' if clean[i] >= 5.0 else f'{clean[i]}%',
                ha='center', va='center', fontsize=6, fontweight='bold',
                color='white')

    ax.set_ylabel('Batch proportion (%)')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 105)
    ax.legend(loc='upper center', fontsize=7, framealpha=0.92,
              edgecolor='none', borderpad=0.4)
    ax.grid(**GRID_KW)
    ax.set_axisbelow(True)
    fig.tight_layout(pad=0.3)
    _save(fig, 'constraint_regime_decomposition')


# ═══════════════════════════════════════════════════════════════════
# Figure A.2 — tau_rho_rank_preservation  (figure, \columnwidth)
# Narrative: τ=0.7 is optimal/near-optimal at both ρ levels;
#            rank order preserved
# Data: Table tau (corrected) + Appendix rho06
# IMPORTANT: τ=0.8 at ρ=0.4 uses corrected from-scratch value
#            (17.683), not resume-artifact value (17.653)
# ═══════════════════════════════════════════════════════════════════
def fig_tau_rho():
    rho04 = {0.50: 17.688,  0.60: 17.681,  0.70: 17.674,
             0.80: 17.683,  0.90: 17.712,  0.95: 17.723}
    rho06 = {0.60: 17.736, 0.70: 17.731, 0.80: 17.740}
    u04, u06 = 17.694, 17.763

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(3.25, 4.2),
        gridspec_kw={'height_ratios': [1.3, 1], 'hspace': 0.38})

    # ── Panel (a): tau-PPL curves ──
    t04, p04 = zip(*sorted(rho04.items()))
    t06, p06 = zip(*sorted(rho06.items()))

    # Safe range shading
    ax1.axvspan(0.5, 0.8, alpha=0.05, color=C['safe'], zorder=0)
    ax1.text(0.53, 17.726, 'safe range', fontsize=7,
             color=C['safe'], fontstyle='italic', alpha=0.7)

    # Curves — ρ=0.4 primary (baseline), ρ=0.6 contrast (treatment)
    ax1.plot(t04, p04, 'o-', color=C['baseline'], markersize=4,
             markeredgecolor='white', markeredgewidth=0.3,
             label=r'$\rho{=}0.4$', zorder=3)
    ax1.plot(t06, p06, 's-', color=C['treatment'], markersize=4,
             markeredgecolor='white', markeredgewidth=0.3,
             label=r'$\rho{=}0.6$', zorder=3)

    # Uniform baselines
    ax1.axhline(u04, color=C['baseline'], ls='--', lw=0.7, alpha=0.4)
    ax1.axhline(u06, color=C['treatment'], ls='--', lw=0.7, alpha=0.4)
    t_u04 = ax1.text(0.96, u04 + 0.001, f'{u04:.3f}', fontsize=7,
                     color=C['baseline'], alpha=0.6, ha='right', va='bottom')
    t_u04.set_path_effects(STROKE)
    t_u06 = ax1.text(0.96, u06 + 0.001, f'{u06:.3f}', fontsize=7,
                     color=C['treatment'], alpha=0.6, ha='right', va='bottom')
    t_u06.set_path_effects(STROKE)

    # Optimal markers — τ=0.7 is best at both ρ
    ax1.plot(0.7, rho04[0.7], '*', color=C['baseline'], markersize=9,
             markeredgecolor='white', markeredgewidth=0.3, zorder=4)
    ax1.plot(0.7, rho06[0.7], '*', color=C['treatment'], markersize=9,
             markeredgecolor='white', markeredgewidth=0.3, zorder=4)
    ax1.annotate(r'$\tau^*{=}0.7$', xy=(0.7, rho04[0.7]),
                 xytext=(0.78, 17.668), fontsize=7.5, color=C['baseline'],
                 arrowprops=dict(arrowstyle='->', color=C['baseline'], lw=0.6))

    ax1.set_xlabel(r'Quality threshold $\tau$')
    ax1.set_ylabel('Held-out PPL')
    ax1.set_title('(a)', loc='left', fontweight='bold', fontsize=9)
    ax1.set_xlim(0.45, 0.99)
    ax1.legend(loc='upper left', fontsize=7, framealpha=0.92, edgecolor='none')
    ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    ax1.grid(**GRID_KW)
    ax1.set_axisbelow(True)

    # ── Panel (b): normalized gap ──
    shared = [0.6, 0.7, 0.8]
    g04 = [(rho04[t] - u04) / u04 * 100 for t in shared]
    g06 = [(rho06[t] - u06) / u06 * 100 for t in shared]
    bw = 0.30
    xb = np.arange(len(shared))

    ax2.bar(xb - bw/2, g04, bw, color=C['baseline'], alpha=0.85,
            label=r'$\rho{=}0.4$', edgecolor='white', lw=0.3)
    ax2.bar(xb + bw/2, g06, bw, color=C['treatment'], alpha=0.85,
            label=r'$\rho{=}0.6$', edgecolor='white', lw=0.3)

    ax2.axhline(0, color='black', lw=0.5)
    ax2.set_xlabel(r'Quality threshold $\tau$')
    ax2.set_ylabel('Gap vs. uniform (%)')
    ax2.set_title('(b)', loc='left', fontweight='bold', fontsize=9)
    ax2.set_xticks(xb)
    ax2.set_xticklabels([str(t) for t in shared])
    ax2.set_xlim(-0.55, 2.55)
    ax2.legend(loc='lower left', fontsize=7, framealpha=0.92, edgecolor='none')
    ax2.grid(**GRID_KW)
    ax2.set_axisbelow(True)
    ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))

    fig.tight_layout()
    _save(fig, 'tau_rho_rank_preservation')


# ═══════════════════════════════════════════════════════════════════
# Figure A.3 — dr_dual_curve  (figure, \columnwidth)
# Narrative: The raw U-shape is a multi-epoch artifact; epoch-matched
#            PPL decreases monotonically and saturates at adaptive level
# Data: Appendix Table dr_threshold
# ═══════════════════════════════════════════════════════════════════
def fig_dr_dual():
    ret_raw = [15.0, 23, 31.5, 38, 41.4, 46, 49.8, 56, 61.6]
    ppl_raw = [17.40, 17.27, 17.250, 17.263, 17.28, 17.30,
               17.32, 17.34, 17.42]
    ret_em  = [15.0, 31.5, 41.4, 49.8, 61.6]
    ppl_em  = [18.04, 17.74, 17.65, 17.62, 17.628]
    adaptive, uniform = 17.674, 17.697

    fig, ax = plt.subplots(figsize=(3.35, 3.0))

    # Saturation region
    ax.fill_between([47, 66], 17.60, 17.65, alpha=0.08,
                    color=C['safe'], zorder=0)
    ax.text(56, 17.625, 'saturation', ha='center', va='center',
            fontsize=7, color=C['safe'], fontstyle='italic', alpha=0.7)

    # D&R multi-epoch curve
    ax.plot(ret_raw, ppl_raw, 'o-', color=C['safe'], markersize=4,
            markeredgecolor='white', markeredgewidth=0.3, lw=1.4,
            label='D&R (multi-epoch)', zorder=3)

    # D&R epoch-matched curve
    ax.plot(ret_em, ppl_em, 's--', color=C['safe'], markersize=4,
            markeredgecolor='white', markeredgewidth=0.3, lw=1.2,
            alpha=0.65, label='D&R (single epoch)', zorder=3)

    # Adaptive reference line
    ax.axhline(adaptive, color=C['baseline'], ls='-.', lw=0.9, zorder=1)
    t_ad = ax.text(11.5, adaptive - 0.025, r'Adaptive $b^*$',
                   fontsize=6, color=C['baseline'], va='top', ha='left')
    t_ad.set_path_effects(STROKE)

    # Uniform reference line
    ax.axhline(uniform, color=C['neutral'], ls=':', lw=0.9, zorder=1)
    t_un = ax.text(11.5, uniform + 0.025, 'Uniform',
                   fontsize=6, color=C['neutral'], va='bottom', ha='left')
    t_un.set_path_effects(STROKE)

    # Epoch count annotations — staggered vertically to avoid overlap
    epoch_annot = [(15.0, '10.0×', -0.050, 'top'),
                   (31.5, '3.2×', -0.045, 'top'),
                   (61.6, '1.1×', 0.025, 'bottom')]
    for ret_val, label, dy, va in epoch_annot:
        idx = ret_raw.index(ret_val)
        t = ax.text(ret_val, ppl_raw[idx] + dy, label, fontsize=6.5,
                    color=C['safe'], ha='center', va=va)
        t.set_path_effects(STROKE)

    # Best raw threshold
    ax.annotate(r'$q{>}0.3$', xy=(31.5, 17.250),
                xytext=(20, 17.18), fontsize=6.5, color=C['safe'],
                arrowprops=dict(arrowstyle='->', color=C['safe'], lw=0.6),
                ha='center')

    ax.set_xlabel('Data retained (%)')
    ax.set_ylabel('Held-out PPL')
    ax.set_xlim(10, 66)
    ax.set_ylim(17.15, 18.10)
    ax.legend(loc='upper right', fontsize=7, framealpha=0.92,
              edgecolor='none', borderpad=0.3)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    ax.grid(**GRID_KW)
    ax.set_axisbelow(True)
    fig.tight_layout(pad=0.3)
    _save(fig, 'dr_dual_curve')


# ═══════════════════════════════════════════════════════════════════
# Figure A.4 — delta_vs_rho  (figure, \columnwidth)
# Narrative: Method transitions from harmful to beneficial between
#            ρ=0.3 and ρ=0.4
# Data: Appendix rho03 + main text
# ═══════════════════════════════════════════════════════════════════
def fig_delta_vs_rho():
    rho   = [0.2,   0.3,    0.4,    0.6]
    delta = [0.046, 0.002, -0.023, -0.032]
    # SD of paired differences (computed from paper's t-stats and n)
    sd    = [None,  0.0022, 0.006,  0.0056]
    n_seeds = [1,   3,      5,      3]

    fig, ax = plt.subplots(figsize=(3.35, 2.6))

    # Transition zone
    ax.axvspan(0.28, 0.42, alpha=0.06, color=C['neutral'], zorder=0)
    ax.text(0.35, 0.052, 'transition\nzone', fontsize=7, ha='center',
            va='bottom', color=C['neutral'], fontstyle='italic',
            linespacing=0.9)

    # Zero reference
    ax.axhline(0, color='black', ls='--', lw=0.6, zorder=1)

    # Data with error bars
    for i, (r, d, s, ns) in enumerate(zip(rho, delta, sd, n_seeds)):
        if ns == 1:
            ax.plot(r, d, 'o', color=C['baseline'], markersize=6,
                    markerfacecolor='white', markeredgecolor=C['baseline'],
                    markeredgewidth=1.2, zorder=4)
        else:
            yerr = s if s else 0
            ax.errorbar(r, d, yerr=yerr, fmt='o', color=C['baseline'],
                        markersize=5, markeredgecolor='white',
                        markeredgewidth=0.4, capsize=3, capthick=0.7,
                        elinewidth=0.7, zorder=4)

    # Connect with line
    ax.plot(rho, delta, '-', color=C['baseline'], lw=1.4, zorder=3)

    # Region labels
    ax.text(0.2, 0.040, 'harmful', fontsize=7.5, color=C['collapse'],
            ha='center', va='top', fontweight='bold')
    ax.text(0.50, -0.028, 'effective', fontsize=7.5, color=C['safe'],
            ha='center', va='top', fontweight='bold')

    ax.set_xlabel(r'$\rho$ (Contamination Ratio)')
    ax.set_ylabel(r'$\Delta$ Holdout PPL (Adaptive $-$ Uniform)')
    ax.set_xlim(0.12, 0.68)
    ax.set_ylim(-0.045, 0.065)
    ax.set_xticks(rho)
    ax.set_xticklabels(['0.2', '0.3', '0.4', '0.6'])
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    ax.grid(**GRID_KW)
    ax.set_axisbelow(True)
    fig.tight_layout(pad=0.3)
    _save(fig, 'delta_vs_rho')


# ═══════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print('Generating optimized paper figures...')
    fig_dual_constraint()
    fig_grid_b_trend()
    fig_constraint_regime()
    fig_tau_rho()
    fig_dr_dual()
    fig_delta_vs_rho()
    print('All 6 figures generated.')
