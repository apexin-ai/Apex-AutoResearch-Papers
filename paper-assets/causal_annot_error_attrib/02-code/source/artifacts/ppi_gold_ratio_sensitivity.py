#!/usr/bin/env python3
"""
PPI++ Gold Label Ratio Sensitivity — K=3 synthetic confusion matrices.

For each (topology, gold_fraction, confusion matrix, rep):
  1. Generate synthetic data via the K=3 DGP from compute_ppi_empirical.py.
  2. Misclassify A -> A* using C.
  3. Run PPI++ correction at the given gold fraction.
  4. Accumulate (tau_hat - tau_true) for RMSE aggregation.

Outputs RMSE and RMSE reduction (vs naive plug-in / naive Wald) per
(topology x gold_fraction) to artifacts/ppi_gold_ratio_results.json.
"""

import json
import os
import sys
import time

import numpy as np

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from annot_sensitivity.correction import correct_ppi  # noqa: E402
from annot_sensitivity.utils import make_dummies, misclassify  # noqa: E402

from compute_ppi_empirical import (  # noqa: E402
    GEN_FNS,
    compute_tau_true,
    make_dgp_params,
    ppi_wald,
    wald_est,
)


K = 3
N_SAMPLES = 10_000
N_REPS = 100
GOLD_FRACTIONS = [0.05, 0.10, 0.20, 0.50, 1.00]
TOPOLOGIES = ['exposure', 'confounding', 'iv', 'mediation', 'mbias']
N_CONFUSIONS = 5
MIN_DIAG = 0.6
SEED = 20260523


def sample_confusion_matrix(K, rng, min_diag=MIN_DIAG, max_tries=200):
    """Dirichlet-sampled column-stochastic confusion matrix with diag >= min_diag.

    Each column j is drawn from Dirichlet(alpha) where alpha gives the diagonal
    entry a larger weight, then rejection-sampled to enforce C[j, j] >= min_diag.
    """
    for _ in range(max_tries):
        C = np.zeros((K, K))
        ok = True
        for j in range(K):
            alpha = np.ones(K)
            alpha[j] = 6.0
            col = rng.dirichlet(alpha)
            if col[j] < min_diag:
                ok = False
                break
            C[:, j] = col
        if ok:
            return C
    raise RuntimeError(f"Could not sample CM with diag>={min_diag} after {max_tries} tries")


def naive_estimate(topology, first_var, Y, Astar, K):
    if topology == 'iv':
        return wald_est(first_var, Y, Astar, k=1)
    if topology == 'exposure':
        N = len(Y)
        D_star = make_dummies(Astar, K)
        X = np.column_stack([np.ones(N), D_star])
        try:
            beta = np.linalg.lstsq(X, Y, rcond=None)[0]
            return float(beta[1])
        except Exception:
            return np.nan
    # confounding, mediation
    T = first_var
    N = len(Y)
    D_star = make_dummies(Astar, K)
    X = np.column_stack([np.ones(N), T, D_star])
    try:
        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
        return float(beta[1])
    except Exception:
        return np.nan


def ppi_estimate(topology, first_var, Y, A, Astar, gold_mask, rng, K):
    N = len(Y)
    if topology == 'iv':
        tau, ok = ppi_wald(first_var, Y, A, Astar, gold_mask, k=1, rng=rng)
        return (float(tau), True) if ok and np.isfinite(tau) else (np.nan, False)
    if topology == 'exposure':
        X_other = np.ones((N, 1))
        tau_idx = 1
    else:  # confounding, mediation
        T = first_var
        X_other = np.column_stack([np.ones(N), T])
        tau_idx = 1
    tau, _, ok = correct_ppi(X_other, Y, Astar, A, gold_mask, tau_idx=tau_idx, rng=rng)
    if ok and np.isfinite(tau):
        return float(tau), True
    return np.nan, False


def run_one_rep(topology, params, C, tau_true, gold_frac, rng):
    first_var, Y, A = GEN_FNS[topology](K, N_SAMPLES, params[topology], rng)
    Astar = misclassify(A, C, rng)

    N = len(Y)
    n_gold = min(N, max(int(round(N * gold_frac)), 50))
    gold_idx = rng.choice(N, size=n_gold, replace=False)
    gold_mask = np.zeros(N, dtype=bool)
    gold_mask[gold_idx] = True

    naive = naive_estimate(topology, first_var, Y, Astar, K)
    ppi, ppi_ok = ppi_estimate(topology, first_var, Y, A, Astar, gold_mask, rng, K)

    naive_err = naive - tau_true if np.isfinite(naive) else np.nan
    ppi_err = ppi - tau_true if ppi_ok else np.nan
    return naive_err, ppi_err


def main():
    t_start = time.time()
    print("=" * 72)
    print("PPI++ Gold Label Ratio Sensitivity")
    print("=" * 72)
    print(f"K={K}, N={N_SAMPLES}, n_reps={N_REPS}, n_cms={N_CONFUSIONS}")
    print(f"gold_fractions={GOLD_FRACTIONS}")
    print(f"topologies={TOPOLOGIES}")

    rng_master = np.random.default_rng(SEED)
    params = make_dgp_params(K)

    print("\nComputing tau_true for each topology (N=500k)...")
    tau_true = {}
    for topo in TOPOLOGIES:
        tau_true[topo] = float(compute_tau_true(K, topo, params))
        print(f"  {topo:12s}: tau_true = {tau_true[topo]:+.6f}")

    print("\nSampling confusion matrices...")
    confusion_matrices = []
    for ci in range(N_CONFUSIONS):
        C = sample_confusion_matrix(K, rng_master, MIN_DIAG)
        confusion_matrices.append(C)
        diag = np.diag(C)
        print(f"  CM[{ci}] diag = [{diag[0]:.3f}, {diag[1]:.3f}, {diag[2]:.3f}]")

    results = {topo: {} for topo in TOPOLOGIES}

    total_conditions = len(TOPOLOGIES) * len(GOLD_FRACTIONS)
    cond_idx = 0
    for topo in TOPOLOGIES:
        print(f"\n--- Topology: {topo} (tau_true={tau_true[topo]:+.4f}) ---")
        for gf in GOLD_FRACTIONS:
            cond_idx += 1
            naive_errs = []
            ppi_errs = []
            t_cond = time.time()
            for ci, C in enumerate(confusion_matrices):
                for rep in range(N_REPS):
                    seed_rep = int(rng_master.integers(0, 2**31))
                    rng_rep = np.random.default_rng(seed_rep)
                    naive_err, ppi_err = run_one_rep(
                        topo, params, C, tau_true[topo], gf, rng_rep
                    )
                    if np.isfinite(naive_err):
                        naive_errs.append(naive_err)
                    if np.isfinite(ppi_err):
                        ppi_errs.append(ppi_err)

            naive_arr = np.asarray(naive_errs)
            ppi_arr = np.asarray(ppi_errs)
            naive_rmse = float(np.sqrt(np.mean(naive_arr ** 2))) if naive_arr.size else None
            ppi_rmse = float(np.sqrt(np.mean(ppi_arr ** 2))) if ppi_arr.size else None
            if naive_rmse is not None and ppi_rmse is not None and naive_rmse > 1e-12:
                reduction = 1.0 - ppi_rmse / naive_rmse
            else:
                reduction = None

            results[topo][f"{gf:.2f}"] = {
                'naive_rmse': naive_rmse,
                'ppi_rmse': ppi_rmse,
                'rmse_reduction': float(reduction) if reduction is not None else None,
                'naive_mean_bias': float(naive_arr.mean()) if naive_arr.size else None,
                'ppi_mean_bias': float(ppi_arr.mean()) if ppi_arr.size else None,
                'n_naive_valid': int(naive_arr.size),
                'n_ppi_valid': int(ppi_arr.size),
            }

            elapsed = time.time() - t_cond
            red_str = f"{100 * reduction:+6.1f}%" if reduction is not None else "  N/A "
            print(f"  gold={gf:0.2f}  naive_rmse={naive_rmse:.5f}  "
                  f"ppi_rmse={ppi_rmse:.5f}  reduction={red_str}  "
                  f"[{cond_idx}/{total_conditions}, {elapsed:.1f}s]")

    output = {
        'meta': {
            'K': K,
            'N': N_SAMPLES,
            'n_reps': N_REPS,
            'n_confusion_matrices': N_CONFUSIONS,
            'min_diag': MIN_DIAG,
            'gold_fractions': GOLD_FRACTIONS,
            'topologies': TOPOLOGIES,
            'seed': SEED,
            'aggregation': 'RMSE pooled across confusion matrices and reps',
        },
        'tau_true': tau_true,
        'confusion_matrices': [C.tolist() for C in confusion_matrices],
        'results': results,
    }

    out_path = os.path.join(PROJECT_ROOT, 'artifacts', 'ppi_gold_ratio_results.json')
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)

    print("\n" + "=" * 72)
    print("SUMMARY (RMSE reduction vs naive, %)")
    print("=" * 72)
    header = f"{'topology':14s}" + "".join(
        [f"  gold={gf:0.2f}" for gf in GOLD_FRACTIONS]
    )
    print(header)
    print("-" * len(header))
    for topo in TOPOLOGIES:
        row = f"{topo:14s}"
        for gf in GOLD_FRACTIONS:
            r = results[topo][f"{gf:.2f}"]['rmse_reduction']
            row += f"  {100*r:+7.1f}%" if r is not None else "    N/A  "
        print(row)

    print(f"\nSaved to: {out_path}")
    print(f"Total runtime: {time.time() - t_start:.1f}s")


if __name__ == '__main__':
    main()
