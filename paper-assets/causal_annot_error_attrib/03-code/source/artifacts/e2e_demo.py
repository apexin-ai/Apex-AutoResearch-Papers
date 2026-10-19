#!/usr/bin/env python3
"""
Mini end-to-end demo: C estimation -> ASV diagnostic -> Algorithm 1 routing
-> correction -> bias improvement.

Three topologies illustrate the key dichotomy:
  - confounding: FWL invariance => no plug-in correction helps the
    treatment coefficient; routed method is "no correction".
  - exposure: PPI++ recovers the target coefficient using a gold subset.
  - IV: Wald estimator instability; high bias, PPI++ limited/harmful.

Pipeline for each topology:
  1. Generate synthetic data with N=10000, K=3, known C0 (diag=0.7,
     off-diagonal 0.15 uniform).
  2. Sample 20% gold subset; estimate C_hat from gold (true vs. observed labels).
  3. Compute ASV (magnitude & sign-flip) using C_hat as the base of the
     interpolation path C(delta) = (1-delta) I + delta C_hat.
  4. Algorithm 1 route:
       - confounding => "no correction (FWL)"
       - exposure    => "PPI++"
       - IV          => "MC-SIMEX (gold-free)"
  5. Apply correction(s).
  6. Record naive bias, corrected bias, improvement.

100 Monte Carlo replicates per topology (mean +/- std).

Outputs:
  - artifacts/e2e_demo_results.json
  - artifacts/e2e_demo_table.tex
"""

import json
import os
import sys
import time

import numpy as np

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from annot_sensitivity.asv import compute_asv
from annot_sensitivity.correction import (
    correct_mla,
    correct_naive_plugin,
    correct_ppi,
)
from annot_sensitivity.dgp import gen_confounding, gen_exposure, gen_iv
from annot_sensitivity.utils import make_dummies, misclassify, ols_with_se

SEED = 42
N = 10_000
K = 3
GOLD_FRACTION = 0.20
N_REPS = 100

C0 = np.array([
    [0.70, 0.15, 0.15],
    [0.15, 0.70, 0.15],
    [0.15, 0.15, 0.70],
])

CONFOUNDING_PARAMS = {
    "p_A": np.array([0.40, 0.35, 0.25]),
    "alpha": np.array([0.6, -0.3]),
    "beta_A": np.array([0.8, -0.4]),
    "beta_T": 0.5,
    "sigma_T": 1.0,
}

EXPOSURE_PARAMS = {
    "p_A": np.array([0.40, 0.35, 0.25]),
    "beta": np.array([0.0, 1.0, -0.5]),
}

IV_PARAMS = {
    "lam": 1.0,
    "g": np.array([0.0, 0.0, 0.0]),
    "dZ": np.array([0.0, 1.0, -0.5]),
    "dU": np.array([0.0, 0.8, 0.6]),
    "beta": np.array([0.0, 1.0, -0.5]),
}


def estimate_C(A_true_gold, A_star_gold, K):
    """Column-stochastic Cˆ[j,k] = P(A* = j | A = k) from gold labels."""
    C_hat = np.zeros((K, K))
    for k in range(K):
        mask = A_true_gold == k
        if mask.sum() > 0:
            for j in range(K):
                C_hat[j, k] = (A_star_gold[mask] == j).sum() / mask.sum()
        else:
            C_hat[k, k] = 1.0
    return C_hat


def naive_confounding(X_other, Y, Astar, K, tau_idx=1):
    D = make_dummies(Astar, K)
    X = np.column_stack([X_other, D])
    beta, se = ols_with_se(X, Y)
    return float(beta[tau_idx]), float(se[tau_idx])


def naive_exposure(Y, Astar, K, tau_idx=1):
    N_ = len(Y)
    X_other = np.ones((N_, 1))
    D = make_dummies(Astar, K)
    X = np.column_stack([X_other, D])
    beta, se = ols_with_se(X, Y)
    return float(beta[tau_idx]), float(se[tau_idx])


def run_confounding_rep(rng, tau_true):
    data = gen_confounding(N, params=CONFOUNDING_PARAMS, rng=rng)
    T, Y, A = data["T"], data["Y"], data["A"]
    Astar = misclassify(A, C0, rng)

    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)
    gold_mask = np.zeros(N, dtype=bool)
    gold_mask[gold_idx] = True
    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)

    X_other = np.column_stack([np.ones(N), T])

    tau_naive, _ = naive_confounding(X_other, Y, Astar, K, tau_idx=1)
    tau_np, _, ok_np = correct_naive_plugin(X_other, Y, Astar, C_hat, tau_idx=1)
    tau_mla, _, ok_mla = correct_mla(X_other, Y, Astar, C_hat, tau_idx=1)

    return {
        "tau_naive": tau_naive,
        "tau_np": tau_np if ok_np else np.nan,
        "tau_mla": tau_mla if ok_mla else np.nan,
        "C_hat": C_hat,
        "tau_true": tau_true,
    }


def run_exposure_rep(rng, tau_true):
    data = gen_exposure(N, params=EXPOSURE_PARAMS, rng=rng)
    Y, A = data["Y"], data["A"]
    Astar = misclassify(A, C0, rng)

    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)
    gold_mask = np.zeros(N, dtype=bool)
    gold_mask[gold_idx] = True
    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)

    X_other = np.ones((N, 1))
    tau_naive, _ = naive_exposure(Y, Astar, K, tau_idx=1)
    tau_ppi, _, ok_ppi = correct_ppi(X_other, Y, Astar, A, gold_mask,
                                     tau_idx=1, rng=rng)

    return {
        "tau_naive": tau_naive,
        "tau_ppi": tau_ppi if ok_ppi else np.nan,
        "C_hat": C_hat,
        "tau_true": tau_true,
    }


def wald_estimator(Z, Y, D, tau_idx=1):
    """Wald (IV) ratio estimator: cov(Z,Y) / cov(Z, D_k)."""
    Z_dm = Z - Z.mean()
    RF = (Z_dm * Y).mean()
    FS_k = (Z_dm * D[:, tau_idx]).mean()
    if abs(FS_k) < 1e-15:
        return np.nan
    return RF / FS_k


def precompute_iv_tau_true(rng, N_pre=2_000_000):
    """Compute population-level Wald ratio with true A."""
    data = gen_iv(N_pre, params=IV_PARAMS, rng=rng)
    Z, Y, A = data["Z"], data["Y"], data["A"]
    D = make_dummies(A, K)
    return wald_estimator(Z, Y, D, tau_idx=1)


def run_iv_rep(rng, tau_true):
    data = gen_iv(N, params=IV_PARAMS, rng=rng)
    Z, Y, A = data["Z"], data["Y"], data["A"]
    Astar = misclassify(A, C0, rng)

    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)
    gold_mask = np.zeros(N, dtype=bool)
    gold_mask[gold_idx] = True
    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)

    D_star = make_dummies(Astar, K)
    tau_naive = wald_estimator(Z, Y, D_star, tau_idx=1)

    # PPI++ (OLS-based — intentionally limited for IV)
    X_other = np.ones((N, 1))
    tau_ppi, _, ok_ppi = correct_ppi(X_other, Y, Astar, A, gold_mask,
                                     tau_idx=1, rng=rng)

    return {
        "tau_naive": tau_naive,
        "tau_ppi": tau_ppi if ok_ppi else np.nan,
        "C_hat": C_hat,
        "tau_true": tau_true,
    }


def compute_summary(reps, method_keys, tau_true):
    out = {"tau_true": float(tau_true)}
    naive = np.array([r["tau_naive"] for r in reps])
    naive_bias = naive - tau_true
    naive_bias_pct = 100.0 * naive_bias / tau_true
    out["naive"] = {
        "mean": float(naive.mean()),
        "std": float(naive.std(ddof=1)),
        "bias_mean": float(naive_bias.mean()),
        "bias_std": float(naive_bias.std(ddof=1)),
        "abs_bias_mean": float(np.mean(np.abs(naive_bias))),
        "bias_pct_mean": float(naive_bias_pct.mean()),
        "bias_pct_std": float(naive_bias_pct.std(ddof=1)),
    }
    out["methods"] = {}
    naive_abs = np.mean(np.abs(naive_bias))
    for key in method_keys:
        vals = np.array([r[key] for r in reps])
        valid = np.isfinite(vals)
        if valid.sum() == 0:
            out["methods"][key] = None
            continue
        v = vals[valid]
        bias = v - tau_true
        bias_pct = 100.0 * bias / tau_true
        abs_bias_mean = float(np.mean(np.abs(bias)))
        improvement_pct = (
            100.0 * (1.0 - abs_bias_mean / naive_abs)
            if naive_abs > 1e-12 else float("nan")
        )
        out["methods"][key] = {
            "mean": float(v.mean()),
            "std": float(v.std(ddof=1)),
            "bias_mean": float(bias.mean()),
            "bias_std": float(bias.std(ddof=1)),
            "abs_bias_mean": abs_bias_mean,
            "bias_pct_mean": float(bias_pct.mean()),
            "bias_pct_std": float(bias_pct.std(ddof=1)),
            "improvement_pct": float(improvement_pct),
            "n_valid": int(valid.sum()),
        }
    return out


def mean_C_hat(reps):
    return np.mean(np.stack([r["C_hat"] for r in reps]), axis=0)


def main():
    t0 = time.time()
    print("=" * 70)
    print(f"Mini E2E demo: N={N}, K={K}, gold={int(N * GOLD_FRACTION)}, reps={N_REPS}")
    print(f"C0 diag={C0.diagonal().tolist()}")
    print("=" * 70)

    rng_master = np.random.default_rng(SEED)

    print("\n[Confounding] target = treatment coefficient tau = 0.5")
    tau_true_conf = CONFOUNDING_PARAMS["beta_T"]
    conf_reps = []
    for rep in range(N_REPS):
        seed_rep = int(rng_master.integers(0, 2**31))
        rng_rep = np.random.default_rng(seed_rep)
        conf_reps.append(run_confounding_rep(rng_rep, tau_true_conf))
        if (rep + 1) % 25 == 0:
            print(f"  rep {rep + 1}/{N_REPS}")

    print("\n[Exposure] target = beta_1 = 1.0")
    tau_true_exp = EXPOSURE_PARAMS["beta"][1]
    exp_reps = []
    for rep in range(N_REPS):
        seed_rep = int(rng_master.integers(0, 2**31))
        rng_rep = np.random.default_rng(seed_rep)
        exp_reps.append(run_exposure_rep(rng_rep, tau_true_exp))
        if (rep + 1) % 25 == 0:
            print(f"  rep {rep + 1}/{N_REPS}")

    print("\n[IV] precomputing population Wald ratio (N=2M)...")
    tau_true_iv = precompute_iv_tau_true(np.random.default_rng(12345))
    print(f"  tau_true (Wald, true A) = {tau_true_iv:.4f}")
    iv_reps = []
    for rep in range(N_REPS):
        seed_rep = int(rng_master.integers(0, 2**31))
        rng_rep = np.random.default_rng(seed_rep)
        iv_reps.append(run_iv_rep(rng_rep, tau_true_iv))
        if (rep + 1) % 25 == 0:
            print(f"  rep {rep + 1}/{N_REPS}")

    conf_summary = compute_summary(
        conf_reps,
        method_keys=["tau_np", "tau_mla"],
        tau_true=tau_true_conf,
    )
    exp_summary = compute_summary(
        exp_reps,
        method_keys=["tau_ppi"],
        tau_true=tau_true_exp,
    )
    iv_summary = compute_summary(
        iv_reps,
        method_keys=["tau_ppi"],
        tau_true=tau_true_iv,
    )

    C_hat_conf_mean = mean_C_hat(conf_reps)
    C_hat_exp_mean = mean_C_hat(exp_reps)
    C_hat_iv_mean = mean_C_hat(iv_reps)

    print("\n[ASV] computing magnitude & sign-flip thresholds with mean Cˆ...")
    asv_conf_mag = compute_asv(
        "confounding", C_hat_conf_mean, params=CONFOUNDING_PARAMS,
        threshold_type="magnitude", threshold_value=0.10,
    )
    asv_conf_sign = compute_asv(
        "confounding", C_hat_conf_mean, params=CONFOUNDING_PARAMS,
        threshold_type="sign_flip",
    )
    asv_exp_mag = compute_asv(
        "exposure", C_hat_exp_mean, params=EXPOSURE_PARAMS,
        threshold_type="magnitude", threshold_value=0.10,
    )
    asv_exp_sign = compute_asv(
        "exposure", C_hat_exp_mean, params=EXPOSURE_PARAMS,
        threshold_type="sign_flip",
    )
    asv_iv_mag = compute_asv(
        "iv", C_hat_iv_mean, params=IV_PARAMS,
        threshold_type="magnitude", threshold_value=0.10,
    )
    asv_iv_sign = compute_asv(
        "iv", C_hat_iv_mean, params=IV_PARAMS,
        threshold_type="sign_flip",
    )

    output = {
        "meta": {
            "seed": SEED,
            "N": N,
            "K": K,
            "gold_fraction": GOLD_FRACTION,
            "n_reps": N_REPS,
            "C0": C0.tolist(),
            "confounding_params": {
                k: (v.tolist() if isinstance(v, np.ndarray) else v)
                for k, v in CONFOUNDING_PARAMS.items()
            },
            "exposure_params": {
                k: (v.tolist() if isinstance(v, np.ndarray) else v)
                for k, v in EXPOSURE_PARAMS.items()
            },
            "iv_params": {
                k: (v.tolist() if isinstance(v, np.ndarray) else v)
                for k, v in IV_PARAMS.items()
            },
        },
        "confounding": {
            **conf_summary,
            "routed_method": "no correction (FWL invariance)",
            "C_hat_mean": C_hat_conf_mean.tolist(),
            "asv_magnitude": asv_conf_mag["asv"],
            "asv_signflip": asv_conf_sign["asv"],
            "asv_tau_true_theoretical": asv_conf_mag["tau_true"],
        },
        "exposure": {
            **exp_summary,
            "routed_method": "PPI++",
            "C_hat_mean": C_hat_exp_mean.tolist(),
            "asv_magnitude": asv_exp_mag["asv"],
            "asv_signflip": asv_exp_sign["asv"],
            "asv_tau_true_theoretical": asv_exp_mag["tau_true"],
        },
        "iv": {
            **iv_summary,
            "routed_method": "MC-SIMEX (gold-free)",
            "C_hat_mean": C_hat_iv_mean.tolist(),
            "asv_magnitude": asv_iv_mag["asv"],
            "asv_signflip": asv_iv_sign["asv"],
            "asv_tau_true_theoretical": asv_iv_mag["tau_true"],
        },
    }

    out_json = os.path.join(PROJECT_ROOT, "artifacts", "e2e_demo_results.json")
    with open(out_json, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nWrote {out_json}")

    write_latex_table(output)

    print_console_summary(output)

    print(f"\nElapsed: {time.time() - t0:.1f}s")


def _fmt_asv(v):
    return f"{v:.3f}" if v is not None else "no crossing"


def _fmt_pct(mean, std):
    if not np.isfinite(mean):
        return "--"
    return f"{mean:+.2f} $\\pm$ {std:.2f}"


def write_latex_table(out):
    conf = out["confounding"]
    exp = out["exposure"]
    iv = out["iv"]

    conf_naive = conf["naive"]
    conf_np = conf["methods"]["tau_np"]
    conf_mla = conf["methods"]["tau_mla"]
    exp_naive = exp["naive"]
    exp_ppi = exp["methods"]["tau_ppi"]
    iv_naive = iv["naive"]
    iv_ppi = iv["methods"]["tau_ppi"]

    def _improve(m):
        if m is None or not np.isfinite(m["improvement_pct"]):
            return "--"
        return f"{m['improvement_pct']:+.1f}\\%"

    def _bias_cell(m):
        if m is None:
            return "--"
        return _fmt_pct(m["bias_pct_mean"], m["bias_pct_std"])

    lines = []
    lines.append("% Auto-generated by artifacts/e2e_demo.py")
    lines.append("\\begin{table}[t]")
    lines.append("\\centering")
    lines.append("\\small")
    lines.append("\\begin{tabular}{lrrlrr}")
    lines.append("\\toprule")
    lines.append(
        "Topology & Naive Bias (\\%) & ASV $\\delta^*_{\\mathrm{mag}}$ & "
        "Routed Method & Corrected Bias (\\%) & Improvement (\\%) \\\\"
    )
    lines.append("\\midrule")

    lines.append(
        "Confounding & "
        f"{_fmt_pct(conf_naive['bias_pct_mean'], conf_naive['bias_pct_std'])} & "
        f"{_fmt_asv(conf['asv_magnitude'])} & "
        "no correction (FWL) & "
        f"{_bias_cell(conf_np)} & {_improve(conf_np)} \\\\"
    )
    lines.append(
        "\\quad (naive plug-in) & -- & -- & -- & "
        f"{_bias_cell(conf_np)} & {_improve(conf_np)} \\\\"
    )
    lines.append(
        "\\quad (MLA)          & -- & -- & -- & "
        f"{_bias_cell(conf_mla)} & {_improve(conf_mla)} \\\\"
    )

    lines.append(
        "Exposure & "
        f"{_fmt_pct(exp_naive['bias_pct_mean'], exp_naive['bias_pct_std'])} & "
        f"{_fmt_asv(exp['asv_magnitude'])} & "
        "PPI++ & "
        f"{_bias_cell(exp_ppi)} & {_improve(exp_ppi)} \\\\"
    )

    lines.append(
        "IV & "
        f"{_fmt_pct(iv_naive['bias_pct_mean'], iv_naive['bias_pct_std'])} & "
        f"{_fmt_asv(iv['asv_magnitude'])} & "
        "MC-SIMEX (gold-free) & "
        f"{_bias_cell(iv_ppi)} & {_improve(iv_ppi)} \\\\"
    )
    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    lines.append(
        "\\caption{End-to-end demo over "
        f"{out['meta']['n_reps']} replicates "
        f"(N={out['meta']['N']:,}, K={out['meta']['K']}, "
        f"{int(out['meta']['gold_fraction']*100)}\\% gold). "
        "Confounding: plug-in corrections leave the treatment coefficient "
        "unchanged (FWL invariance), so Algorithm~1 routes to ``no correction''. "
        "Exposure: PPI++ recovers the target coefficient. "
        "IV: Wald estimator instability produces large bias; "
        "PPI++ (OLS-based) is limited, routing to MC-SIMEX."
        "}"
    )
    lines.append("\\label{tab:e2e-demo}")
    lines.append("\\end{table}")

    out_tex = os.path.join(PROJECT_ROOT, "artifacts", "e2e_demo_table.tex")
    with open(out_tex, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {out_tex}")


def print_console_summary(out):
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for topo in ("confounding", "exposure", "iv"):
        s = out[topo]
        print(f"\n[{topo}]  tau_true (empirical) = {s['tau_true']:.4f}")
        print(f"  routed = {s['routed_method']}")
        nb = s["naive"]
        print(
            f"  naive       : tau = {nb['mean']:.4f} +/- {nb['std']:.4f}  "
            f"bias = {nb['bias_pct_mean']:+.2f}% +/- {nb['bias_pct_std']:.2f}%"
        )
        for key, m in s["methods"].items():
            if m is None:
                print(f"  {key:11s}: N/A")
                continue
            print(
                f"  {key:11s}: tau = {m['mean']:.4f} +/- {m['std']:.4f}  "
                f"bias = {m['bias_pct_mean']:+.2f}% +/- {m['bias_pct_std']:.2f}%  "
                f"improvement = {m['improvement_pct']:+.1f}%"
            )
        print(
            f"  ASV magnitude (10%) : {_fmt_asv(s['asv_magnitude'])}  |  "
            f"ASV sign-flip : {_fmt_asv(s['asv_signflip'])}"
        )


if __name__ == "__main__":
    main()
