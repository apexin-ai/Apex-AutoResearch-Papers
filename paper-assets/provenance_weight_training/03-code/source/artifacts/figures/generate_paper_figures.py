"""Generate all 4 paper figures with unified publication-quality style.

Data sources (all verified):
  Fig 1: Appendix Table 4 (grid search, seed 42) + Table 1 cross-seed
  Fig 2: Section 4.4 + Appendix D constraint regime statistics
  Fig 3: tau_rho_rank_analysis.py authoritative data
  Fig 4: Appendix Table dr_threshold
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from pathlib import Path

OUT = Path("/home/ubuntu/.agent-ml-research-idea_gen_0509_10/"
           "projects/provenance_weight_training/artifacts/figures")

# ── Unified palette ──
C = dict(
    blue='#2166ac', red='#b2182b', orange='#e08214',
    lt_orange='#f4a582', green='#4dac26', teal='#1b7837',
    gray='#878787', lt_blue='#92c5de',
)

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
    'mathtext.fontset': 'dejavuserif',
    'font.size': 8, 'axes.labelsize': 9, 'axes.titlesize': 9,
    'xtick.labelsize': 8, 'ytick.labelsize': 8, 'legend.fontsize': 8,
    'axes.linewidth': 0.6,
    'xtick.major.width': 0.5, 'ytick.major.width': 0.5,
    'xtick.major.size': 3, 'ytick.major.size': 3,
    'lines.linewidth': 1.3, 'lines.markersize': 4.5,
    'axes.spines.top': False, 'axes.spines.right': False,
    'figure.dpi': 300, 'savefig.dpi': 300, 'savefig.bbox': 'tight',
})


def _save(fig, name):
    for ext in ('pdf', 'png'):
        fig.savefig(OUT / f'{name}.{ext}', dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f'  saved {name}.pdf/.png')


# ═══════════════════════════════════════════════════════════════
# Figure 1 — grid_b_trend_clean  (main text, \columnwidth)
# ═══════════════════════════════════════════════════════════════
def fig1_grid_b_trend():
    # Seed 42 full grid — Appendix Table 4
    b   = [0.1,   0.2,   0.3,   0.5,   1.0,   1.5,   2.0,   3.0,   5.0]
    ppl = [17.657,17.640,17.640,17.651,17.692,17.718,17.741,17.774,17.818]
    uniform = 17.694

    fig, ax = plt.subplots(figsize=(3.5, 2.6))

    # Degradation zone  b >= 2 (gray hatching for B&W)
    ax.axvspan(2.0, 5.8, alpha=0.08, color='#999999', zorder=0)
    ax.fill_between([2.0, 5.8], 17.62, 17.85, alpha=0.0, hatch='///',
                    edgecolor='#cccccc', linewidth=0.5, zorder=0)

    # ESS-only b* mean marker — black for B&W
    yb = 17.835
    ax.annotate(r'ESS-only $\bar{b}^*{\approx}3.5$',
                xy=(3.5, 17.774), xytext=(4.3, yb),
                fontsize=8, color='black', ha='center',
                arrowprops=dict(arrowstyle='->', color='black', lw=0.7))

    # Uniform baseline
    ax.axhline(uniform, color=C['gray'], ls='--', lw=0.8, zorder=1,
               label=f'Uniform ({uniform:.3f})')

    # Adaptive b* vertical indicator — black dash-dot for B&W
    ax.axvline(0.9, color='black', ls='-.', lw=0.8, alpha=0.7, zorder=1)
    ax.text(0.80, 17.72, r'Adaptive $\bar{b}^*{\approx}0.9$', fontsize=8,
            color='black', va='bottom', rotation=90)

    # Main curve — seed 42 (filled black circles)
    ax.plot(b, ppl, 'o-', color='black', markersize=4, zorder=3,
            markerfacecolor='black', markeredgecolor='black', markeredgewidth=0.3,
            label='Seed 42 (full grid)')

    # Cross-seed at b = 0.5 — distinct markers for B&W
    ax.plot(0.5, 17.638, 's', color='black', markersize=5, zorder=3,
            markerfacecolor='white', markeredgecolor='black', markeredgewidth=1.0,
            label='Seed 123')
    ax.plot(0.5, 17.650, 'D', color=C['gray'], markersize=4.5, zorder=3,
            markerfacecolor=C['gray'], markeredgecolor='black', markeredgewidth=0.5,
            label='Seed 456')

    ax.set_xlabel(r'Sharpening exponent $b$')
    ax.set_ylabel('Held-out PPL')
    ax.set_xlim(-0.2, 5.7)
    ax.set_ylim(17.62, 17.85)
    ax.legend(loc='upper left', framealpha=0.9, edgecolor='none',
              handlelength=1.5, handletextpad=0.4, borderpad=0.4)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    ax.grid(axis='y', lw=0.3, alpha=0.4, color='#ccc')
    ax.set_axisbelow(True)
    fig.tight_layout(pad=0.3)
    _save(fig, 'grid_b_trend_clean')


# ═══════════════════════════════════════════════════════════════
# Figure 2 — constraint_regime_decomposition  (appendix)
# ═══════════════════════════════════════════════════════════════
def fig2_constraint_regime():
    labels = [r'$\rho{=}0.4$', r'$\rho{=}0.6$']
    aeff   = [50.9, 46.8]          # τ=0.7, 3-seed avg
    ess    = [43.3, 48.7]
    clean  = [ 5.8,  4.5]

    fig, ax = plt.subplots(figsize=(2.8, 2.6))
    x = np.arange(len(labels))
    w = 0.52

    ax.bar(x, aeff, w, color=C['lt_orange'], edgecolor='white', lw=0.5,
           label=r'$\alpha_{\mathrm{eff}}$-binding', zorder=2)
    ax.bar(x, ess, w, bottom=aeff, color=C['lt_blue'], edgecolor='white', lw=0.5,
           label='ESS-binding', zorder=2)
    ax.bar(x, clean, w, bottom=[a+e for a, e in zip(aeff, ess)],
           color=C['green'], alpha=0.8, edgecolor='white', lw=0.5,
           label='Clean', zorder=2)

    for i in range(2):
        ax.text(i, aeff[i] / 2, f'{aeff[i]:.1f}%',
                ha='center', va='center', fontsize=8,
                fontweight='bold', color='white')
        ax.text(i, aeff[i] + ess[i] / 2, f'{ess[i]:.0f}%',
                ha='center', va='center', fontsize=8,
                fontweight='bold', color='white')

    ax.set_ylabel('Batch proportion (%)')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 108)
    ax.legend(loc='upper right', fontsize=8, framealpha=0.9, edgecolor='none')
    ax.grid(axis='y', lw=0.3, alpha=0.4, color='#ccc')
    ax.set_axisbelow(True)
    fig.tight_layout(pad=0.3)
    _save(fig, 'constraint_regime_decomposition')


# ═══════════════════════════════════════════════════════════════
# Figure 3 — tau_rho_rank_preservation  (appendix, 2-panel)
# ═══════════════════════════════════════════════════════════════
def fig3_tau_rho():
    rho04 = {0.50: 17.688,  0.60: 17.6805, 0.70: 17.6793,
             0.80: 17.6527, 0.90: 17.712,  0.95: 17.723}
    rho06 = {0.60: 17.7359, 0.70: 17.730,  0.80: 17.740}
    u04, u06 = 17.6939, 17.766

    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(6.8, 2.6),
        gridspec_kw={'width_ratios': [1.3, 1], 'wspace': 0.40})

    # ── Panel (a): tau-PPL curves ──
    t04, p04 = zip(*sorted(rho04.items()))
    t06, p06 = zip(*sorted(rho06.items()))

    ax1.axvspan(0.5, 0.8, alpha=0.07, color=C['green'], zorder=0)
    ax1.text(0.58, 17.648, 'safe range', fontsize=8,
             color=C['teal'], fontstyle='italic')

    ax1.plot(t04, p04, 'o-', color=C['blue'], markersize=4.5,
             markeredgecolor='white', markeredgewidth=0.3,
             label=r'$\rho{=}0.4$', zorder=3)
    ax1.plot(t06, p06, 's-', color=C['red'], markersize=4.5,
             markeredgecolor='white', markeredgewidth=0.3,
             label=r'$\rho{=}0.6$', zorder=3)

    # Uniform baselines
    ax1.axhline(u04, color=C['blue'], ls='--', lw=0.7, alpha=0.5)
    ax1.axhline(u06, color=C['red'],  ls='--', lw=0.7, alpha=0.5)
    ax1.text(0.96, u04 + 0.001, f'{u04:.3f}', fontsize=8,
             color=C['blue'], alpha=0.7, ha='right', va='bottom')
    ax1.text(0.96, u06 + 0.001, f'{u06:.3f}', fontsize=8,
             color=C['red'],  alpha=0.7, ha='right', va='bottom')

    # Optimal markers
    ax1.plot(0.8, rho04[0.8], '*', color=C['blue'], markersize=10,
             markeredgecolor='white', markeredgewidth=0.3, zorder=4)
    ax1.plot(0.7, rho06[0.7], '*', color=C['red'], markersize=10,
             markeredgecolor='white', markeredgewidth=0.3, zorder=4)
    ax1.annotate(r'$\tau^*{=}0.8$', xy=(0.8, rho04[0.8]),
                 xytext=(0.84, 17.646), fontsize=8, color=C['blue'],
                 arrowprops=dict(arrowstyle='->', color=C['blue'], lw=0.7))
    ax1.annotate(r'$\tau^*{=}0.7$', xy=(0.7, rho06[0.7]),
                 xytext=(0.75, 17.722), fontsize=8, color=C['red'],
                 arrowprops=dict(arrowstyle='->', color=C['red'], lw=0.7))

    ax1.set_xlabel(r'Quality threshold $\tau$')
    ax1.set_ylabel('Held-out PPL')
    ax1.set_title('(a)', loc='left', fontweight='bold')
    ax1.set_xlim(0.45, 0.99)
    ax1.legend(loc='upper left', fontsize=7, framealpha=0.9, edgecolor='none')
    ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    ax1.grid(axis='y', lw=0.3, alpha=0.4, color='#ccc')
    ax1.set_axisbelow(True)

    # ── Panel (b): normalized gap ──
    shared = [0.6, 0.7, 0.8]
    g04 = [(rho04[t] - u04) / u04 * 100 for t in shared]
    g06 = [(rho06[t] - u06) / u06 * 100 for t in shared]
    bw = 0.28
    xb = np.arange(len(shared))

    b1 = ax2.bar(xb - bw/2, g04, bw, color=C['blue'], alpha=0.85,
                 label=r'$\rho{=}0.4$')
    b2 = ax2.bar(xb + bw/2, g06, bw, color=C['red'],  alpha=0.85,
                 label=r'$\rho{=}0.6$')

    ax2.axhline(0, color='black', lw=0.5)
    ax2.set_xlabel(r'Quality threshold $\tau$')
    ax2.set_ylabel('Gap vs. uniform (%)')
    ax2.set_title('(b)', loc='left', fontweight='bold')
    ax2.set_xticks(xb)
    ax2.set_xticklabels([str(t) for t in shared])
    ax2.set_xlim(-0.5, 2.7)
    ax2.legend(loc='upper right', fontsize=8, framealpha=0.9, edgecolor='none')
    ax2.grid(axis='y', lw=0.3, alpha=0.4, color='#ccc')
    ax2.set_axisbelow(True)
    ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))

    fig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.93, wspace=0.40)
    _save(fig, 'tau_rho_rank_preservation')


# ═══════════════════════════════════════════════════════════════
# Figure 4 — dr_dual_curve  (appendix)
# ═══════════════════════════════════════════════════════════════
def fig4_dr_dual():
    # Appendix Table dr_threshold — all 9 thresholds
    ret_raw = [15.0, 23, 31.5, 38, 41.4, 46, 49.8, 56, 61.6]
    ppl_raw = [17.40, 17.27, 17.250, 17.263, 17.28, 17.30, 17.32, 17.34, 17.42]

    # Epoch-matched subset
    ret_em = [15.0, 31.5, 41.4, 49.8, 61.6]
    ppl_em = [18.04, 17.74, 17.65, 17.62, 17.628]

    adaptive, uniform = 17.674, 17.694

    fig, ax = plt.subplots(figsize=(3.5, 2.8))

    # Saturation region shading
    ax.fill_between([47, 66], 17.54, 17.64, alpha=0.10,
                    color=C['orange'], zorder=0)
    ax.text(56.5, 17.57, 'saturation', ha='center', va='center',
            fontsize=8, color=C['orange'], fontstyle='italic')

    # Raw (multi-epoch) curve
    ax.plot(ret_raw, ppl_raw, 'o-', color=C['blue'], markersize=4.5, lw=1.6,
            markeredgecolor='white', markeredgewidth=0.3,
            label='D&R (multi-epoch)', zorder=3)

    # Epoch-matched curve
    ax.plot(ret_em, ppl_em, 's--', color=C['orange'], markersize=4.5, lw=1.6,
            markeredgecolor='white', markeredgewidth=0.3,
            label='D&R (single epoch)', zorder=3)

    # Reference lines
    ax.axhline(adaptive, color=C['teal'], ls='-.', lw=1.0, zorder=1,
               label=r'Adaptive $b^*$ ' + f'({adaptive})')
    ax.axhline(uniform, color=C['gray'], ls=':', lw=1.0, zorder=1,
               label=f'Uniform ({uniform})')

    # Epoch count annotations (selected points)
    for ret_val, label in [(15.0, '6.7x'), (31.5, '3.2x'), (61.6, '1.6x')]:
        idx = ret_raw.index(ret_val)
        dy = -0.04 if ret_val == 15.0 else 0.025
        va = 'top' if ret_val == 15.0 else 'bottom'
        ax.text(ret_val, ppl_raw[idx] + dy, label, fontsize=8,
                color=C['blue'], ha='center', fontweight='bold', va=va)

    # Best raw threshold annotation
    ax.annotate(r'$q{>}0.3$', xy=(31.5, 17.250),
                xytext=(21, 17.19), fontsize=8, color=C['blue'],
                arrowprops=dict(arrowstyle='->', color=C['blue'], lw=0.7),
                ha='center')

    ax.set_xlabel('Data retained (%)')
    ax.set_ylabel('Held-out PPL')
    ax.set_xlim(10, 66)
    ax.set_ylim(17.15, 18.10)
    ax.legend(loc='upper right', fontsize=8, framealpha=0.9, edgecolor='none')
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    ax.grid(axis='y', lw=0.3, alpha=0.4, color='#ccc')
    ax.set_axisbelow(True)
    fig.tight_layout(pad=0.3)
    _save(fig, 'dr_dual_curve')


if __name__ == '__main__':
    print('Generating paper figures...')
    fig1_grid_b_trend()
    fig2_constraint_regime()
    fig3_tau_rho()
    fig4_dr_dual()
    print('All 4 figures generated.')
