#!/usr/bin/env python3
"""
Exp-D ε-sensitivity to τ: does the ε-approximate monotonicity bound depend
on the true effect size τ?

For each non-IV topology and τ ∈ {0.1, 0.5, 1.0, 2.0, 5.0}, sample 10,000
random Dirichlet(1,...,1) confusion matrices and compute:
  ε(C0) = (worst wrong-direction step in bias curve) / |τ_true|
where τ_true = plim of OLS at C=I (or DGP τ for collider/mbias).

The τ-related DGP parameter is set per topology:
  confounding:  beta_T = τ        (direct T→Y effect)
  mediation:    tau   = τ         (direct T→Y effect, T binary)
  collider:     tau   = τ         (DGP T→Y effect)
  mbias:        tau   = τ         (DGP T→Y effect)
  exposure:     beta *= τ         (no T; bias scales linearly => ε invariant)
  frontdoor:    beta *= τ         (M→Y effect; affine in τ)

Reports max_eps, mean_eps, p99_eps, and n_violations (where ε > 0.06).
Output: exp_d_epsilon_tau_sensitivity.json
"""

import numpy as np
import json
import time
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exp_d_conjecture_verify_v2 import (
    K_VALUES, ALL_TOPOS, NON_DECREASING,
    _COMPUTE_SS, compute_bias_curve, get_tau_true,
    SEED, DELTA_STEP,
    _ALPHA_POOL, _BETA_A_POOL, _BETA_POOL,
    _GAMMA_POOL, _DELTA_POOL, _DT_POOL, _DY_POOL,
    _MBIAS_A1_POOL, _MBIAS_A2_POOL,
    _FD_GAMMA_POOL, _FD_DELTA_POOL,
    make_p_A,
)


TAU_VALUES = [0.1, 0.5, 1.0, 2.0, 5.0]
NON_IV_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
                'mbias', 'frontdoor']
EPS_THRESHOLD = 0.06
N_RAND_SENS = 10_000
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def make_params_with_tau(K, tau):
    p_A = make_p_A(K)
    tau = float(tau)
    return dict(
        confounding=dict(p_A=p_A, alpha=np.array(_ALPHA_POOL[:K - 1]),
                         beta_A=np.array(_BETA_A_POOL[:K - 1]),
                         beta_T=tau, sigma_T=1.0),
        mediation=dict(tau=tau, gamma=np.array(_GAMMA_POOL[:K]),
                       delta=np.array(_DELTA_POOL[:K]),
                       beta=np.array(_BETA_POOL[:K])),
        collider=dict(tau=tau, g=np.zeros(K),
                      dT=np.array(_DT_POOL[:K]),
                      dY=np.array(_DY_POOL[:K])),
        exposure=dict(beta=np.array(_BETA_POOL[:K]) * tau, p_A=p_A),
        mbias=dict(tau=tau, delta_coef=1.0, lam=1.0, g=np.zeros(K),
                   a1=np.array(_MBIAS_A1_POOL[:K]),
                   a2=np.array(_MBIAS_A2_POOL[:K])),
        frontdoor=dict(alpha_U=1.0, lam_U=1.0,
                       gamma=np.array(_FD_GAMMA_POOL[:K]),
                       delta=np.array(_FD_DELTA_POOL[:K]),
                       beta=np.array(_BETA_POOL[:K]) * tau),
    )


def wrong_direction_step(bias_abs, topo):
    """Largest single-step deviation in the wrong direction (absolute units)."""
    valid = ~np.isnan(bias_abs)
    ba = bias_abs[valid]
    if len(ba) < 2:
        return 0.0
    diffs = np.diff(ba)
    if topo in NON_DECREASING:
        return float(max(0.0, -diffs.min()))
    return float(max(0.0, diffs.max()))


def run_one_setting(topo, K, tau, n_random):
    params = make_params_with_tau(K, tau)
    ss = _COMPUTE_SS[topo](K, params[topo])
    tau_true = get_tau_true(topo, K, params, ss)
    if np.isnan(tau_true) or abs(tau_true) < 1e-12:
        return None, tau_true

    rng_C = np.random.default_rng(
        SEED * 7 + K * 1_000_003 + ALL_TOPOS.index(topo) * 10_007
        + int(round(tau * 1000))
    )
    eps = np.empty(n_random)
    for i in range(n_random):
        C0 = np.empty((K, K))
        for j in range(K):
            C0[:, j] = rng_C.dirichlet(np.ones(K))
        _, bias_abs = compute_bias_curve(topo, C0, ss, tau_true)
        eps[i] = wrong_direction_step(bias_abs, topo) / abs(tau_true)
    return eps, float(tau_true)


def main():
    t_total = time.time()
    print("=" * 78)
    print("Exp-D ε(τ) sensitivity")
    print(f"  Non-IV topologies: {NON_IV_TOPOS}")
    print(f"  τ values: {TAU_VALUES}")
    print(f"  K values: {K_VALUES}")
    print(f"  N random C0 per (topo, K, τ): {N_RAND_SENS:,}")
    print(f"  ε threshold for 'violation' count: {EPS_THRESHOLD}")
    print("=" * 78)
    sys.stdout.flush()

    results = {}
    for topo in NON_IV_TOPOS:
        results[topo] = {}
        print(f"\n[{topo}]")
        print(f"  {'τ':>6}  {'τ_true':>12}  {'max_eps':>10}  {'p99_eps':>10}  "
              f"{'mean_eps':>10}  {'n_viol':>10}  {'K':>3}  {'time':>7}")
        sys.stdout.flush()
        for tau in TAU_VALUES:
            tau_key = f"tau_{tau}"
            per_K = {}
            for K in K_VALUES:
                t0 = time.time()
                eps, tau_true = run_one_setting(topo, K, tau, N_RAND_SENS)
                elapsed = time.time() - t0
                if eps is None:
                    per_K[f"K{K}"] = {
                        "tau_true": tau_true,
                        "error": "tau_true is NaN or zero",
                    }
                    print(f"  {tau:>6}  {'NaN':>12}  {'-':>10}  {'-':>10}  "
                          f"{'-':>10}  {'-':>10}  {K:>3}  {elapsed:>6.1f}s")
                    sys.stdout.flush()
                    continue
                rec = {
                    "tau_true": tau_true,
                    "max_eps": float(eps.max()),
                    "p99_eps": float(np.percentile(eps, 99)),
                    "mean_eps": float(eps.mean()),
                    "n_violations": int((eps > EPS_THRESHOLD).sum()),
                    "n_tested": N_RAND_SENS,
                }
                per_K[f"K{K}"] = rec
                print(f"  {tau:>6}  {tau_true:>12.6f}  {rec['max_eps']:>10.4f}  "
                      f"{rec['p99_eps']:>10.4f}  {rec['mean_eps']:>10.4f}  "
                      f"{rec['n_violations']:>10}  {K:>3}  {elapsed:>6.1f}s")
                sys.stdout.flush()

            agg_keys = [k for k in per_K if "error" not in per_K[k]]
            if agg_keys:
                agg = {
                    "max_eps": max(per_K[k]["max_eps"] for k in agg_keys),
                    "p99_eps": max(per_K[k]["p99_eps"] for k in agg_keys),
                    "mean_eps": float(np.mean([per_K[k]["mean_eps"]
                                                for k in agg_keys])),
                    "n_violations": sum(per_K[k]["n_violations"]
                                         for k in agg_keys),
                    "n_tested": sum(per_K[k]["n_tested"] for k in agg_keys),
                }
            else:
                agg = {"error": "no valid K"}
            results[topo][tau_key] = {
                "aggregate_over_K": agg,
                "per_K": per_K,
            }

    elapsed_total = time.time() - t_total
    out = {
        "tau_values": TAU_VALUES,
        "topologies": NON_IV_TOPOS,
        "K_values": K_VALUES,
        "n_random_per_setting": N_RAND_SENS,
        "eps_threshold": EPS_THRESHOLD,
        "seed_base": SEED,
        "delta_step": DELTA_STEP,
        "tau_param_mapping": {
            "confounding": "beta_T = tau",
            "mediation": "tau (T->Y direct)",
            "collider": "tau (T->Y direct)",
            "exposure": "beta *= tau (linear in tau; eps invariant)",
            "mbias": "tau (T->Y direct)",
            "frontdoor": "beta *= tau (affine in tau)",
        },
        "results": results,
        "elapsed_seconds": elapsed_total,
    }
    out_path = os.path.join(OUT_DIR, "exp_d_epsilon_tau_sensitivity.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=str)

    print("\n" + "=" * 78)
    print(f"Total time: {elapsed_total:.1f}s ({elapsed_total/60:.1f}min)")
    print(f"Saved -> {out_path}")
    print("=" * 78)

    # Summary table: max_eps across τ per topology
    print("\nSummary -- max ε across K, per (topology, τ):")
    print(f"  {'topology':<14}  " + "  ".join(f"τ={t:<5}" for t in TAU_VALUES))
    for topo in NON_IV_TOPOS:
        row = [topo.ljust(14)]
        for tau in TAU_VALUES:
            rec = results[topo].get(f"tau_{tau}", {}).get("aggregate_over_K", {})
            v = rec.get("max_eps", float("nan"))
            row.append(f"{v:>7.4f}")
        print("  " + "  ".join(row))

    print("\nSummary -- n_violations (ε > 0.06) across K, per (topology, τ):")
    print(f"  {'topology':<14}  " + "  ".join(f"τ={t:<5}" for t in TAU_VALUES))
    for topo in NON_IV_TOPOS:
        row = [topo.ljust(14)]
        for tau in TAU_VALUES:
            rec = results[topo].get(f"tau_{tau}", {}).get("aggregate_over_K", {})
            v = rec.get("n_violations", "-")
            row.append(f"{str(v):>7}")
        print("  " + "  ".join(row))


if __name__ == "__main__":
    main()
