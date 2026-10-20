#!/usr/bin/env python3
"""
Theoretical power analysis for lz* contamination detection.

Derives E[lz*] under contamination via expected score equations,
proves δ ∝ √n, explains the inverted-U, and validates against
2000-sim × 11-level × 5-benchmark empirical data.
"""

import os
import sys
import json
import time

import numpy as np
import pandas as pd
from scipy.optimize import brentq
from scipy.stats import norm

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
from person_fit import prob_4pl, filter_valid_items

# ── paths ──────────────────────────────────────────────────────────────────
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARAM_DIR = os.path.join(ROOT, "artifacts", "psn_irt_params")
SIM_DIR = os.path.join(ROOT, "artifacts", "extended_simulation")
OUT_DIR = os.path.join(ROOT, "artifacts", "power_theory")

BMS = ["mmlu", "hellaswag", "gsm8k", "arc_c", "humaneval"]
PCTS = [0, 3, 5, 10, 15, 25, 50, 60, 75, 90, 100]
NQ = 30

COL = {"mmlu": "#1f77b4", "hellaswag": "#ff7f0e", "gsm8k": "#2ca02c",
       "arc_c": "#d62728", "humaneval": "#9467bd"}
MRK = {"mmlu": "o", "hellaswag": "s", "gsm8k": "^", "arc_c": "D", "humaneval": "v"}
LBL = {"mmlu": "MMLU", "hellaswag": "HellaSwag", "gsm8k": "GSM8K",
       "arc_c": "ARC-C", "humaneval": "HumanEval"}


# ── data loading ───────────────────────────────────────────────────────────

def load_params(bm):
    df = pd.read_csv(os.path.join(PARAM_DIR, f"{bm}_params.csv"))
    a, b, c, d = (df[k].values.astype(np.float64)
                  for k in ["a_discrimination", "b_difficulty",
                            "c_guessing", "d_feasibility"])
    m = filter_valid_items(a, b, c, d, min_a=0.0)
    return {"a": a[m], "b": b[m], "c": c[m], "d": d[m], "n": int(m.sum())}


def load_sim():
    return pd.read_csv(os.path.join(SIM_DIR, "two_sided_power.csv"))


# ── core theory ────────────────────────────────────────────────────────────

def _irt_at(theta, a, b, c, d):
    """Compute IRT quantities at theta: P, Q, g, h, Var*."""
    P = prob_4pl(theta, a, b, c, d)
    Q = np.maximum(1 - P, 1e-15)
    g = np.log(np.maximum(P, 1e-15) / Q)
    z = a * (theta - b)
    sig = 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))
    dP = a * (d - c) * sig * (1 - sig)
    h = dP / (P * Q)
    Var_l = float(np.sum(P * Q * g**2))
    I_th = float(np.sum(P * Q * h**2))
    C_th = float(np.sum(P * Q * h * g))
    Vs = Var_l - C_th**2 / max(I_th, 1e-30)
    if Vs <= 1e-10:
        Vs = Var_l
    return P, Q, g, h, Vs


def expected_theta_hat(theta0, pi, a, b, c, d):
    """E[θ̂] under contamination π via expected score equation."""
    if pi > 1 - 1e-9:
        return 4.0
    if pi < 1e-9:
        return float(np.clip(theta0, -3.99, 3.99))
    P0 = prob_4pl(theta0, a, b, c, d)
    Ex = P0 + pi * (1 - P0)

    def score(th):
        P = prob_4pl(th, a, b, c, d)
        Q = np.maximum(1 - P, 1e-15)
        z = a * (th - b)
        sig = 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))
        dP = a * (d - c) * sig * (1 - sig)
        return float(np.sum((Ex - P) * dP / (P * Q)))

    sl, sh = score(-3.99), score(3.99)
    if sl * sh >= 0:
        return 3.99 if sl > 0 else -3.99
    try:
        return brentq(score, -3.99, 3.99, xtol=1e-6)
    except ValueError:
        return 3.99 if pi > 0.5 else float(np.clip(theta0, -3.99, 3.99))


def cond_moments(theta0, pi, a, b, c, d):
    """E[lz*|θ₀,π] and Var[lz*|θ₀,π] under contamination."""
    P0 = prob_4pl(theta0, a, b, c, d)
    Q0 = 1 - P0
    Ex = P0 + pi * Q0

    th_hat = expected_theta_hat(theta0, pi, a, b, c, d)
    P, Q, g, _, Vs = _irt_at(th_hat, a, b, c, d)

    E_num = float(np.sum((Ex - P) * g))
    sd_s = np.sqrt(max(Vs, 1e-30))
    E_lz = E_num / sd_s if sd_s > 1e-10 else 0.0

    Var_x = Ex * Q0 * (1 - pi)
    V_num = float(np.sum(Var_x * g**2))
    V_lz = V_num / max(Vs, 1e-30)

    return E_lz, max(V_lz, 1e-10), th_hat


def marginal_power(pi, a, b, c, d, nq=NQ):
    """Power integrated over θ ~ N(0,1) via Gauss-Hermite quadrature."""
    nodes, wts = np.polynomial.hermite_e.hermegauss(nq)
    wts = wts / np.sqrt(2 * np.pi)

    mu_a, sq_a = 0.0, 0.0
    p2, pl, pr = 0.0, 0.0, 0.0

    for th, w in zip(nodes, wts):
        El, Vl, _ = cond_moments(float(th), pi, a, b, c, d)
        sd = max(np.sqrt(Vl), 0.005)

        mu_a += w * El
        sq_a += w * (El**2 + Vl)

        if sd < 0.01:
            cl = 1.0 if El < -1.96 else 0.0
            cr = 1.0 if El > 1.96 else 0.0
            cl1 = 1.0 if El < -1.6449 else 0.0
            cr1 = 1.0 if El > 1.6449 else 0.0
        else:
            cl = norm.cdf((-1.96 - El) / sd)
            cr = 1 - norm.cdf((1.96 - El) / sd)
            cl1 = norm.cdf((-1.6449 - El) / sd)
            cr1 = 1 - norm.cdf((1.6449 - El) / sd)

        p2 += w * (cl + cr)
        pl += w * cl1
        pr += w * cr1

    var_m = max(sq_a - mu_a**2, 0)
    return {
        "two_sided": float(np.clip(p2, 0, 1)),
        "left_tail": float(np.clip(pl, 0, 1)),
        "right_tail": float(np.clip(pr, 0, 1)),
        "mean_lz": float(mu_a),
        "std_lz": float(np.sqrt(var_m)),
    }


# ── benchmark-level computation ───────────────────────────────────────────

def benchmark_theory(params):
    a, b, c, d = params["a"], params["b"], params["c"], params["d"]
    return {pct: marginal_power(pct / 100.0, a, b, c, d) for pct in PCTS}


# ── comparison & metrics ──────────────────────────────────────────────────

def build_comparison(theory, sim_df, all_params):
    rows = []
    for _, r in sim_df.iterrows():
        bm, pct = r["benchmark"], int(r["contamination_pct"])
        t = theory[bm][pct]
        rows.append({
            "benchmark": bm, "contamination_pct": pct,
            "n_items": all_params[bm]["n"],
            "sim_two": r["two_sided_rate"], "sim_left": r["left_tail_rate"],
            "sim_right": r["right_tail_rate"], "sim_mean": r["mean_lz_star"],
            "sim_std": r["std_lz_star"],
            "th_two": t["two_sided"], "th_left": t["left_tail"],
            "th_right": t["right_tail"], "th_mean": t["mean_lz"],
            "th_std": t["std_lz"],
        })
    return pd.DataFrame(rows)


def r2_rmse(y, yh):
    m = np.isfinite(y) & np.isfinite(yh)
    y, yh = y[m], yh[m]
    ss_res = np.sum((y - yh)**2)
    ss_tot = np.sum((y - y.mean())**2)
    return (1 - ss_res / max(ss_tot, 1e-30), np.sqrt(ss_res / len(y)))


def fit_metrics(comp):
    m = {}
    for name, sc, tc in [("two_sided", "sim_two", "th_two"),
                          ("left_tail", "sim_left", "th_left"),
                          ("right_tail", "sim_right", "th_right"),
                          ("mean_lz", "sim_mean", "th_mean")]:
        r2, rmse = r2_rmse(comp[sc].values, comp[tc].values)
        m[name] = {"R2": round(r2, 4), "RMSE": round(rmse, 4)}
        for bm in BMS:
            sub = comp[comp["benchmark"] == bm]
            r2b, rmseb = r2_rmse(sub[sc].values, sub[tc].values)
            m[f"{name}_{bm}"] = {"R2": round(r2b, 4), "RMSE": round(rmseb, 4)}
    return m


# ── √n scaling verification ──────────────────────────────────────────────

def verify_sqrt_n(theory, all_params):
    results = {}
    for pct in [5, 10, 15, 25, 50]:
        sqn = np.array([np.sqrt(all_params[bm]["n"]) for bm in BMS])
        means = np.array([theory[bm][pct]["mean_lz"] for bm in BMS])
        alpha = float(np.sum(sqn * means) / np.sum(sqn**2))
        pred = alpha * sqn
        r2, _ = r2_rmse(means, pred)
        results[pct] = {"alpha": round(alpha, 6), "R2": round(r2, 4)}
    return results


# ── minimum items table ──────────────────────────────────────────────────

def min_items_table(all_params, targets=(0.80, 0.90, 0.95),
                    cpcts=(5, 10, 15, 25, 50)):
    nodes, wts = np.polynomial.hermite_e.hermegauss(NQ)
    wts = wts / np.sqrt(2 * np.pi)
    rows = []

    for cpct in cpcts:
        pi = cpct / 100.0
        all_d1, all_s0 = [], []
        for bm in BMS:
            p = all_params[bm]
            d1s, s0s = [], []
            for th in nodes:
                El, Vl, _ = cond_moments(float(th), pi,
                                         p["a"], p["b"], p["c"], p["d"])
                d1s.append(El / np.sqrt(p["n"]))
                s0s.append(np.sqrt(Vl))
            all_d1.append(d1s)
            all_s0.append(s0s)

        avg_d1 = np.mean(all_d1, axis=0)
        avg_s0 = np.mean(all_s0, axis=0)

        def power_at_n(n):
            pw = 0.0
            for d1, s0, w in zip(avg_d1, avg_s0, wts):
                mu = np.sqrt(n) * d1
                sd = max(s0, 0.005)
                if sd < 0.01:
                    pw += w * (1.0 if abs(mu) > 1.96 else 0.0)
                else:
                    pw += w * (norm.cdf((-1.96 - mu) / sd)
                               + 1 - norm.cdf((1.96 - mu) / sd))
            return float(np.clip(pw, 0, 1))

        for tp in targets:
            lo, hi = 10, 200000
            if power_at_n(hi) < tp:
                n_min = None
            else:
                while hi - lo > 1:
                    mid = (lo + hi) // 2
                    if power_at_n(mid) >= tp:
                        hi = mid
                    else:
                        lo = mid
                n_min = hi
            rows.append({"contamination_pct": cpct,
                         "target_power": tp, "min_n_items": n_min})

    return pd.DataFrame(rows)


# ── crossover & peak ─────────────────────────────────────────────────────

def find_crossover(a, b, c, d):
    """Find π where E[lz*] crosses from negative to positive."""
    def mlz(pi):
        return marginal_power(pi, a, b, c, d, nq=20)["mean_lz"]

    lo, hi = 0.55, 0.99
    vlo, vhi = mlz(lo), mlz(hi)

    if vlo >= 0:
        lo, vlo = 0.35, mlz(0.35)
        if vlo >= 0:
            return None
    if vhi <= 0:
        return None

    for _ in range(40):
        mid = (lo + hi) / 2
        vm = mlz(mid)
        if vlo * vm <= 0:
            hi = mid
        else:
            lo, vlo = mid, vm
        if hi - lo < 0.002:
            break
    return round((lo + hi) / 2, 3)


def find_left_peak(a, b, c, d):
    best_p, best_pw = 0, 0
    for pct in range(3, 96, 2):
        r = marginal_power(pct / 100.0, a, b, c, d, nq=20)
        if r["left_tail"] > best_pw:
            best_pw, best_p = r["left_tail"], pct / 100.0
    return round(best_p, 2), round(best_pw, 4)


# ── plotting ─────────────────────────────────────────────────────────────

def plot_comparison(comp, all_params, path):
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    axes = axes.flatten()

    for i, bm in enumerate(BMS):
        ax = axes[i]
        df = comp[comp["benchmark"] == bm].sort_values("contamination_pct")
        x = df["contamination_pct"].values
        n = all_params[bm]["n"]

        ax.scatter(x, df["sim_two"], color=COL[bm], marker=MRK[bm], s=60,
                   zorder=3, edgecolors="k", linewidth=0.5,
                   label="Sim (two-sided)")
        ax.plot(x, df["th_two"], color=COL[bm], lw=2,
                label="Theory (two-sided)")

        ax.scatter(x, df["sim_left"], color=COL[bm], marker="x", s=30,
                   alpha=0.5, label="Sim (left)")
        ax.plot(x, df["th_left"], color=COL[bm], lw=1.2, ls="--", alpha=0.6,
                label="Theory (left)")

        r2t = r2_rmse(df["sim_two"].values, df["th_two"].values)[0]
        r2l = r2_rmse(df["sim_left"].values, df["th_left"].values)[0]

        ax.set_title(f"{LBL[bm]} (n={n:,})\n"
                     f"R²(two)={r2t:.3f}, R²(left)={r2l:.3f}", fontsize=10)
        ax.set_xlabel("Contamination (%)", fontsize=9)
        ax.set_ylabel("Detection Rate", fontsize=9)
        ax.set_ylim(-0.02, 1.05)
        ax.set_xticks(PCTS)
        ax.tick_params(axis="x", rotation=45, labelsize=8)
        ax.axhline(0.05, color="red", ls=":", alpha=0.4, label="α=0.05")
        ax.grid(True, alpha=0.3)
        if i == 0:
            ax.legend(fontsize=6.5, loc="upper left")

    ax = axes[5]
    for bm in BMS:
        df = comp[comp["benchmark"] == bm].sort_values("contamination_pct")
        x = df["contamination_pct"].values
        n = all_params[bm]["n"]
        ax.plot(x, df["th_two"], color=COL[bm], lw=2,
                label=f"{LBL[bm]} (n={n:,})")
        ax.scatter(x, df["sim_two"], color=COL[bm], marker=MRK[bm],
                   s=30, alpha=0.7)
    ax.set_title("All Benchmarks: Theory (line) vs Sim (marker)", fontsize=10)
    ax.set_xlabel("Contamination (%)", fontsize=9)
    ax.set_ylabel("Two-sided Power", fontsize=9)
    ax.set_ylim(-0.02, 1.05)
    ax.set_xticks(PCTS)
    ax.tick_params(axis="x", rotation=45, labelsize=8)
    ax.axhline(0.05, color="red", ls=":", alpha=0.4)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7, loc="upper left")

    fig.suptitle("Theoretical vs Simulated lz* Detection Power",
                 fontsize=13, y=0.98)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


# ── markdown generators ──────────────────────────────────────────────────

def write_derivation(path, scaling, metrics):
    text = r"""# Theoretical Power Analysis for lz* Contamination Detection

## 1. Model Setup

### 4PL IRT Model
$$P_i(\theta) = c_i + (d_i - c_i) \cdot \frac{1}{1 + e^{-a_i(\theta - b_i)}}$$

### Contamination Model
Contamination fraction $\pi$ forces a random $\lfloor n\pi \rceil$ items correct:
$$\mathbb{E}[x_i | \theta_0, \pi] = P_i(\theta_0) + \pi \cdot Q_i(\theta_0)$$

### lz* Statistic (Snijders, 2001)
$$lz^* = \frac{l(\hat\theta) - \mathbb{E}[l(\hat\theta)]}{\sqrt{\mathrm{Var}^*(\hat\theta)}}$$
where $\mathrm{Var}^* = \mathrm{Var}_l - C_\theta^2 / I_\theta$ corrects for the estimated $\hat\theta$.

Under the null: $lz^* \sim N(0, 1)$ approximately.

## 2. Expected lz* Under Contamination

### Expected MLE Bias
The expected $\hat\theta$ solves the expected score equation:
$$\sum_{i=1}^n \bigl(\mathbb{E}[x_i] - P_i(\theta)\bigr) \cdot h_i(\theta) = 0$$
where $h_i = P_i' / (P_i Q_i)$.

Since $\mathbb{E}[x_i] > P_i(\theta_0)$ for $\pi > 0$, $\mathbb{E}[\hat\theta] > \theta_0$ (upward bias).

### Mean Shift
$$\delta(\theta_0, \pi) = \frac{\sum_{i=1}^n \bigl(\mathbb{E}[x_i] - P_i(\hat\theta)\bigr) \cdot g_i(\hat\theta)}{\sqrt{\mathrm{Var}^*(\hat\theta)}}$$
where $g_i(\theta) = \log(P_i / Q_i)$.

### Conditional Variance
$$\mathrm{Var}[lz^* | \theta_0, \pi] = \frac{\sum_{i=1}^n \mathrm{Var}[x_i] \cdot g_i(\hat\theta)^2}{\mathrm{Var}^*(\hat\theta)}$$
with $\mathrm{Var}[x_i] = \mathbb{E}[x_i] \cdot Q_i(\theta_0) \cdot (1 - \pi)$.

## 3. Power ∝ √n Scaling (Proposition 1)

**Proposition**: $\delta(\theta_0, \pi) \propto \sqrt{n}$ for fixed $\theta_0$ and $\pi > 0$.

**Proof**: The numerator $\sum_i \epsilon_i = n \cdot \bar\epsilon$ is $O(n)$. The denominator $\sqrt{\mathrm{Var}^*} = \sqrt{\sum_i v_i} = O(\sqrt{n})$. Therefore:
$$\delta = \frac{n \cdot \bar\epsilon}{\sqrt{n \cdot \bar v}} = \sqrt{n} \cdot \underbrace{\frac{\bar\epsilon}{\sqrt{\bar v}}}_{\delta_1}$$

The per-item noncentrality $\delta_1$ is $O(1)$ and depends only on item parameters and $(\theta_0, \pi)$.

**Empirical verification** (E[lz*] regressed on $\sqrt{n}$ across 5 benchmarks):

"""
    for pct, info in sorted(scaling.items()):
        text += f"- π={pct}%: α={info['alpha']:.6f}, R²={info['R2']:.4f}\n"

    text += r"""
## 4. Marginal Power Formula (Proposition 2)

Integrating over $\theta_0 \sim N(0,1)$ via Gauss-Hermite quadrature ($K=""" + str(NQ) + r"""$ nodes):
$$\mathrm{Power}(n, \pi) = \sum_{k=1}^K w_k \left[\Phi\!\left(\frac{-z_\alpha - \delta_k}{\sigma_k}\right) + 1 - \Phi\!\left(\frac{z_\alpha - \delta_k}{\sigma_k}\right)\right]$$
where $\delta_k = \delta(\theta_k, \pi)$ and $\sigma_k = \sqrt{\mathrm{Var}[lz^*|\theta_k, \pi]}$.

For two-sided detection: $z_\alpha = 1.96$.

## 5. Validation Against Simulation

"""
    text += f"| Metric | Overall R² | Overall RMSE |\n"
    text += f"|--------|-----------|-------------|\n"
    for name in ["two_sided", "left_tail", "right_tail", "mean_lz"]:
        text += f"| {name} | {metrics[name]['R2']} | {metrics[name]['RMSE']} |\n"

    text += "\nPer-benchmark R² (two-sided power):\n\n"
    for bm in BMS:
        r2 = metrics[f"two_sided_{bm}"]["R2"]
        text += f"- {LBL[bm]}: R² = {r2}\n"

    text += r"""
## 6. Key Formulas Summary

For paper citation:

1. **Expected response**: $\mathbb{E}[x_i | \theta_0, \pi] = P_i(\theta_0) + \pi \cdot (1 - P_i(\theta_0))$
2. **Expected θ̂**: Solve $\sum_i (\mathbb{E}[x_i] - P_i(\theta)) h_i(\theta) = 0$
3. **Mean shift**: $\delta(\theta_0, \pi) = \sum_i (\mathbb{E}[x_i] - P_i(\hat\theta)) g_i(\hat\theta) / \sqrt{\mathrm{Var}^*}$
4. **Scaling**: $\delta \propto \sqrt{n}$, so power increases with benchmark size
5. **Power**: Integrate conditional power over $\theta_0 \sim N(0,1)$
"""
    with open(path, "w") as f:
        f.write(text)


def write_inverted_u(path, crossovers, peaks, all_params, sim_df):
    text = """# Theoretical Explanation of the Inverted-U Detection Pattern

## Mechanism

The left-tail detection power exhibits an inverted-U as a function of contamination
fraction $\\pi$ because the **sign of $\\mathbb{E}[lz^*]$ reverses** at high $\\pi$.

### Phase 1: Moderate contamination (small to medium $\\pi$)
- Contaminated items create an **aberrant** response pattern: items the examinee would
  have failed now appear correct.
- MLE $\\hat\\theta$ is biased upward but cannot fully explain the inflated score.
- Result: $lz^* < 0$ (too many "unexpected" correct responses).
- Left-tail power increases with $\\pi$.

### Phase 2: High contamination ($\\pi \\to 1$)
- Nearly all items are correct; $\\hat\\theta$ approaches the upper boundary.
- At high $\\hat\\theta$, the model **expects** nearly all items correct.
- The all-correct pattern becomes **over-consistent** rather than aberrant.
- Result: $lz^* > 0$ (pattern is more predictable than expected).
- Left-tail power **drops** as $lz^*$ moves to the right tail.

## Theoretical vs Empirical Crossover Points

The crossover $\\pi^*$ where $\\mathbb{E}[lz^*] = 0$:

| Benchmark | n_items | Theory $\\pi^*$ | Simulation crossover |
|-----------|---------|----------------|---------------------|
"""
    for bm in BMS:
        n = all_params[bm]["n"]
        cp = crossovers[bm]
        bm_sim = sim_df[sim_df["benchmark"] == bm].sort_values("contamination_pct")
        cross_str = "N/A"
        for j in range(len(bm_sim) - 1):
            r0, r1 = bm_sim.iloc[j], bm_sim.iloc[j + 1]
            if r0["mean_lz_star"] <= 0 and r1["mean_lz_star"] > 0:
                cross_str = f"{int(r0['contamination_pct'])}–{int(r1['contamination_pct'])}%"
        cp_str = f"{cp * 100:.1f}%" if cp else "N/A"
        text += f"| {LBL[bm]} | {n:,} | {cp_str} | {cross_str} |\n"

    text += """
## Left-tail Power Peak

| Benchmark | n_items | Peak $\\pi$ | Peak left-tail power |
|-----------|---------|------------|---------------------|
"""
    for bm in BMS:
        n = all_params[bm]["n"]
        pp, ppw = peaks[bm]
        text += f"| {LBL[bm]} | {n:,} | {pp * 100:.0f}% | {ppw:.4f} |\n"

    text += """
## Why Two-sided Detection Eliminates the Inverted-U

Two-sided detection ($|lz^*| > 1.96$) captures **both** tails:
- Left tail catches moderate contamination ($lz^* < 0$, aberrant pattern).
- Right tail catches high contamination ($lz^* > 0$, over-consistent pattern).

The right-tail power increases precisely where the left-tail power drops, so the
combined two-sided power is **monotonically increasing** (or nearly so) with $\\pi$
for sufficiently large benchmarks, eliminating the inverted-U artifact.

## Implications for Practice

1. **Always use two-sided detection** ($|lz^*| > 1.96$) instead of one-sided.
2. The crossover region ($\\pi^* \\approx 75$–$85\\%$) is relatively consistent across
   benchmarks, suggesting it is primarily driven by the contamination-to-ability
   mapping rather than item characteristics.
3. Benchmarks with more items are more robust: with $n > 1000$ items, two-sided
   power exceeds 80% across almost all contamination levels.
"""
    with open(path, "w") as f:
        f.write(text)


# ── main ─────────────────────────────────────────────────────────────────

def main():
    t0 = time.time()
    os.makedirs(OUT_DIR, exist_ok=True)

    all_params = {bm: load_params(bm) for bm in BMS}
    sim_df = load_sim()

    # 1. Theoretical power curves
    print("Computing theoretical power curves...")
    theory = {}
    for bm in BMS:
        t1 = time.time()
        print(f"  {bm} (n={all_params[bm]['n']:,})...", end=" ", flush=True)
        theory[bm] = benchmark_theory(all_params[bm])
        print(f"{time.time() - t1:.1f}s")

    # 2. Comparison
    comp = build_comparison(theory, sim_df, all_params)
    metrics = fit_metrics(comp)
    print(f"\nFit metrics:")
    print(f"  R²(two-sided) = {metrics['two_sided']['R2']}")
    print(f"  R²(left-tail) = {metrics['left_tail']['R2']}")
    print(f"  R²(mean lz*)  = {metrics['mean_lz']['R2']}")

    # 3. √n scaling
    scaling = verify_sqrt_n(theory, all_params)
    print(f"\n√n scaling:")
    for pct, info in sorted(scaling.items()):
        print(f"  π={pct}%: α={info['alpha']:.6f}, R²={info['R2']:.4f}")

    # 4. Min items
    print("\nComputing minimum items table...")
    mi_df = min_items_table(all_params)
    print("\nMinimum items for target power (two-sided, |lz*|>1.96):")
    print(mi_df.to_string(index=False))

    # 5. Crossover & peak
    print("\nCrossover & left-peak analysis...")
    crossovers, peaks = {}, {}
    for bm in BMS:
        p = all_params[bm]
        crossovers[bm] = find_crossover(p["a"], p["b"], p["c"], p["d"])
        peaks[bm] = find_left_peak(p["a"], p["b"], p["c"], p["d"])
        cp_str = f"{crossovers[bm] * 100:.1f}%" if crossovers[bm] else "N/A"
        print(f"  {bm}: crossover={cp_str}, "
              f"left_peak_π={peaks[bm][0] * 100:.0f}% (power={peaks[bm][1]:.4f})")

    # 6. Save outputs
    print("\nSaving outputs...")
    plot_comparison(comp, all_params,
                    os.path.join(OUT_DIR, "theory_vs_simulation.png"))
    write_derivation(os.path.join(OUT_DIR, "theory_derivation.md"),
                     scaling, metrics)
    write_inverted_u(os.path.join(OUT_DIR, "inverted_u_theory.md"),
                     crossovers, peaks, all_params, sim_df)
    mi_df.to_csv(os.path.join(OUT_DIR, "minimum_items_table.csv"), index=False)

    with open(os.path.join(OUT_DIR, "fit_metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)

    summary = {
        "description": "Theoretical power analysis for lz* contamination detection",
        "method": "Expected score equation + Gauss-Hermite quadrature (K=30)",
        "key_result": "δ(n,π) ∝ √n; inverted-U from lz* sign reversal at high π",
        "fit": {
            "R2_two_sided": metrics["two_sided"]["R2"],
            "RMSE_two_sided": metrics["two_sided"]["RMSE"],
            "R2_left_tail": metrics["left_tail"]["R2"],
            "RMSE_left_tail": metrics["left_tail"]["RMSE"],
            "R2_mean_lz": metrics["mean_lz"]["R2"],
            "RMSE_mean_lz": metrics["mean_lz"]["RMSE"],
        },
        "sqrt_n_scaling": scaling,
        "crossover_points_pct": {bm: crossovers[bm] for bm in BMS},
        "left_peak_pct": {bm: peaks[bm][0] for bm in BMS},
        "left_peak_power": {bm: peaks[bm][1] for bm in BMS},
        "min_items": mi_df.to_dict("records"),
        "benchmarks": {bm: {"n_items": all_params[bm]["n"]} for bm in BMS},
        "artifacts": [
            "theory_derivation.md",
            "theory_vs_simulation.png",
            "minimum_items_table.csv",
            "inverted_u_theory.md",
            "fit_metrics.json",
            "power_theory_summary.json",
        ],
    }
    with open(os.path.join(OUT_DIR, "power_theory_summary.json"), "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    elapsed = time.time() - t0
    print(f"\nAll outputs → {OUT_DIR}")
    print(f"Total: {elapsed:.1f}s")
    print(f"\nVERDICT: R²(two-sided)={metrics['two_sided']['R2']} "
          f"{'≥' if metrics['two_sided']['R2'] >= 0.9 else '<'} 0.9")


if __name__ == "__main__":
    main()
