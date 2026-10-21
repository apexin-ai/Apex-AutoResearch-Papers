"""Power curves: Pairwise vs Likert sensitivity comparison.

Bug fixes applied:
  1. Binarized Likert: n_eff = n * (1 - tie_rate) to account for 62.5% ties
  2. Pairwise: BT curve uses full n (no filtering); sign-test curve uses
     consistency-filtered n_eff = n * retention_rate

Four curves:
  1. Pairwise BT         — p = 63.0%, n_eff = n
  2. Pairwise Sign Test   — p = 73.9%, n_eff = n * 0.523
  3. Binarized Likert     — p = 60.6%, n_eff = n * 0.375  (tie-adjusted)
  4. Likert ATE           — paired t-test, Cohen's d = 0.073
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, nct

OUTPATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "docs", "paper", "figures", "power_curve.pdf",
)

BT_P = 0.630
SIGN_P = 0.739
BLIKERT_P = 0.606
ATE_D = 0.073

CONSISTENCY_RATE = 0.523
TIE_RATE = 0.625

ALPHA = 0.05
NS = np.arange(50, 1001)


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


def main():
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

    print("80% power crossings:")
    print(f"  Pairwise BT (p={BT_P}):                n = {n80_bt}")
    print(f"  Pairwise Sign (p={SIGN_P}, r={CONSISTENCY_RATE}):  n = {n80_sign}")
    print(f"  Binarized Likert (p={BLIKERT_P}, tie={TIE_RATE}): n = {n80_blik}")
    print(f"  Likert ATE (d={ATE_D}):                n = {n80_ate_approx}")

    fig, ax = plt.subplots(figsize=(7, 4.5))

    colors = ["#2166ac", "#d6604d", "#4daf4a", "#984ea3"]
    markers = ["o", "^", "s", "D"]  # circle, triangle, square, diamond
    markevery = 25  # place a marker every 25 data points

    ax.plot(NS, pow_bt, color=colors[0], linewidth=1.5,
            marker=markers[0], markevery=markevery, markersize=4,
            label=f"Pairwise BT ($p$={BT_P})")
    ax.plot(NS, pow_sign, color=colors[1], linewidth=1.5, linestyle="--",
            marker=markers[1], markevery=markevery, markersize=4,
            label=f"Pairwise Sign ($p$={SIGN_P}, filtered)")
    ax.plot(NS, pow_blik, color=colors[2], linewidth=1.5,
            marker=markers[2], markevery=markevery, markersize=4,
            label=f"Binarized Likert ($p$={BLIKERT_P}, tie-adj.)")
    ax.plot(NS, pow_ate, color=colors[3], linewidth=1.5, linestyle="-.",
            marker=markers[3], markevery=markevery, markersize=4,
            label=f"Likert ATE ($d$={ATE_D})")

    ax.axhline(0.8, color="grey", linestyle=":", linewidth=1, alpha=0.7)
    ax.text(1005, 0.8, "80%", va="center", fontsize=9, color="grey")

    for n80, color in [
        (n80_bt, colors[0]),
        (n80_sign, colors[1]),
        (n80_blik, colors[2]),
    ]:
        if n80 is not None and n80 <= 1000:
            ax.plot(n80, 0.8, "o", color=color, markersize=5, zorder=5)
            ax.annotate(f"$n$={n80}", (n80, 0.8), textcoords="offset points",
                        xytext=(5, 10), fontsize=8, color=color, fontweight="bold")

    ax.annotate(f"$n$≈{n80_ate_approx}\n(off-chart)", (980, pow_ate[-1]),
                textcoords="offset points", xytext=(-50, 15),
                fontsize=8, color=colors[3], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=colors[3], lw=0.8))

    ax.set_xlabel("Sample Size ($n$)", fontsize=11)
    ax.set_ylabel("Statistical Power", fontsize=11)
    ax.set_xlim(50, 1000)
    ax.set_ylim(0, 1.02)
    ax.legend(loc="lower right", fontsize=8.5, framealpha=0.9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)

    plt.tight_layout()
    os.makedirs(os.path.dirname(OUTPATH), exist_ok=True)
    fig.savefig(OUTPATH, bbox_inches="tight", dpi=300)
    plt.close()
    print(f"\nSaved: {OUTPATH}")


if __name__ == "__main__":
    main()
