"""
Optimized power curve: detection probability comparison across measurement methods.
Narrative: Pairwise methods reach 80% power at n~60-114 while Likert methods require
4-206x more samples, confirming structural sensitivity gap.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np
from scipy.stats import norm, nct

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 13,
    'axes.labelsize': 13,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'lines.linewidth': 2.0,
})

# Parameters from the paper
BT_P = 0.630
SIGN_P = 0.739
BLIKERT_P = 0.606
ATE_D = 0.073
CONSISTENCY_RATE = 0.523
TIE_RATE = 0.625
ALPHA = 0.05

# Colors (semantic: pairwise = warm/active, Likert = cool/muted)
C_BT = '#4E79A7'      # baseline blue
C_SIGN = '#E15759'     # treatment coral
C_BLIK = '#59A14F'     # green
C_ATE = '#B07AA1'      # muted purple

NS = np.arange(20, 1001)


def power_prop(n, p, alpha=ALPHA):
    if n < 1:
        return 0.0
    z = norm.ppf(1 - alpha / 2)
    c_hi = n * 0.5 + z * np.sqrt(n * 0.25)
    c_lo = n * 0.5 - z * np.sqrt(n * 0.25)
    mu = n * p
    sig = np.sqrt(n * p * (1 - p))
    if sig < 1e-12:
        return 1.0
    return (1.0 - norm.cdf(c_hi, mu, sig)) + norm.cdf(c_lo, mu, sig)


def power_ttest(n, d, alpha=ALPHA):
    if n < 2:
        return 0.0
    df = n - 1
    tc = nct.ppf(1 - alpha / 2, df, 0)
    nc = d * np.sqrt(n)
    return (1.0 - nct.cdf(tc, df, nc)) + nct.cdf(-tc, df, nc)


def find_crossing(ns, pows, target=0.8):
    idx = np.where(pows >= target)[0]
    return int(ns[idx[0]]) if len(idx) > 0 else None


# Compute power curves
pow_bt = np.array([power_prop(n, BT_P) for n in NS])
pow_sign = np.array([power_prop(max(1, int(n * CONSISTENCY_RATE)), SIGN_P) for n in NS])
pow_blik = np.array([power_prop(max(1, int(n * (1 - TIE_RATE))), BLIKERT_P) for n in NS])
pow_ate = np.array([power_ttest(n, ATE_D) for n in NS])

n80_bt = find_crossing(NS, pow_bt)
n80_sign = find_crossing(NS, pow_sign)
n80_blik = find_crossing(NS, pow_blik)
n80_ate = find_crossing(NS, pow_ate)
if n80_ate is None:
    z_a = norm.ppf(1 - ALPHA / 2)
    z_b = norm.ppf(0.8)
    n80_ate_approx = int(np.ceil(((z_a + z_b) / ATE_D) ** 2))
else:
    n80_ate_approx = n80_ate

print(f"80% power crossings: BT={n80_bt}, Sign={n80_sign}, BLikert={n80_blik}, ATE={n80_ate_approx}")

fig, ax = plt.subplots(figsize=(7, 4.2))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Typical study size band
ax.axvspan(50, 200, alpha=0.06, color='#4E79A7', zorder=0)
ax.text(125, 0.03, 'typical $n$', ha='center', fontsize=8,
        color='#4E79A7', alpha=0.6, fontstyle='italic')

# 80% power line
ax.axhline(0.8, color='#999999', linestyle=':', linewidth=0.9, zorder=1)
ax.text(1010, 0.8, '80%', va='center', fontsize=9, color='#999999')

# Plot curves with sparse markers
me = 40  # marker every N points

ax.plot(NS, pow_sign, color=C_SIGN, linewidth=1.8, linestyle='--',
        marker='^', markevery=me, markersize=4.5, markeredgewidth=0,
        label=f'Pairwise Sign ($p$={SIGN_P})', zorder=3)
ax.plot(NS, pow_bt, color=C_BT, linewidth=2.0,
        marker='o', markevery=me, markersize=4.5, markeredgewidth=0,
        label=f'Pairwise BT ($p$={BT_P})', zorder=3)
ax.plot(NS, pow_blik, color=C_BLIK, linewidth=1.8,
        marker='s', markevery=me, markersize=4, markeredgewidth=0,
        label=f'Binarized Likert ($p$={BLIKERT_P})', zorder=3)
ax.plot(NS, pow_ate, color=C_ATE, linewidth=1.8, linestyle='-.',
        marker='D', markevery=me, markersize=3.5, markeredgewidth=0,
        label=f'Likert ATE ($d$={ATE_D})', zorder=3)

# 80% crossing annotations
# Sign test crossing (n≈62) - place above
if n80_sign is not None:
    ax.plot(n80_sign, 0.8, 'o', color=C_SIGN, markersize=5, zorder=5)
    t = ax.annotate(f'$n$={n80_sign}', (n80_sign, 0.8),
                    xytext=(-8, 14), textcoords='offset points',
                    fontsize=9, color=C_SIGN, fontweight='bold', ha='center')
    t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# BT crossing (n≈114) - place below to avoid overlap
if n80_bt is not None:
    ax.plot(n80_bt, 0.8, 'o', color=C_BT, markersize=5, zorder=5)
    t = ax.annotate(f'$n$={n80_bt}', (n80_bt, 0.8),
                    xytext=(8, -18), textcoords='offset points',
                    fontsize=9, color=C_BT, fontweight='bold', ha='center')
    t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Binarized Likert crossing (n≈462)
if n80_blik is not None and n80_blik <= 1000:
    ax.plot(n80_blik, 0.8, 'o', color=C_BLIK, markersize=5, zorder=5)
    t = ax.annotate(f'$n$={n80_blik}', (n80_blik, 0.8),
                    xytext=(0, 12), textcoords='offset points',
                    fontsize=9, color=C_BLIK, fontweight='bold', ha='center')
    t.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])

# Likert ATE (off-chart)
t = ax.annotate(f'$n$≈{n80_ate_approx}\n(off-chart)', (970, pow_ate[-1]),
                xytext=(-55, 18), textcoords='offset points',
                fontsize=8.5, color=C_ATE, fontweight='bold', ha='center',
                arrowprops=dict(arrowstyle='->', color=C_ATE, lw=0.8))
t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])

ax.set_xlabel('Sample Size ($n$)')
ax.set_ylabel('Statistical Power')
ax.set_xlim(20, 1010)
ax.set_ylim(-0.02, 1.04)

# Legend outside data area
leg = ax.legend(loc='lower right', fontsize=9, frameon=True,
                framealpha=0.95, edgecolor='#DDDDDD', borderpad=0.5)
leg.get_frame().set_linewidth(0.5)

plt.tight_layout()

out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/figures'
fig.savefig(f'{out_dir}/power_curve.pdf', facecolor='white', edgecolor='none')
fig.savefig(f'{out_dir}/power_curve.png', facecolor='white', edgecolor='none')
plt.close()
print('Saved: power_curve.pdf + .png')
