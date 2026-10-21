"""
Numerical verification that the mediation leakage coefficient

    lambda(C) := Var(E[g(A) | A*]) / Var(g(A))

lies in [0, 1] for any column-stochastic confusion matrix C and any
non-degenerate marginal distribution pi over A and any non-constant g.

The bound is the law-of-total-variance identity
    Var(g) = Var(E[g|A*]) + E[Var(g|A*)]
applied to the random variable g(A) under the joint law P(A,A*) = pi(A)*C(A*|A).

This script samples random (C, pi, g) triples for K in {3, 5, 7} and checks
that lambda(C) lies in [0, 1] in every case. It also verifies the two
extremal cases analytically:
  - C = I (perfect classification):    lambda = 1
  - C = (1/K) * 1 1^T (rank-one row):  lambda = 0
"""

import json
import os
from pathlib import Path

import numpy as np


RNG = np.random.default_rng(20260522)
N_TRIALS_PER_K = 10_000
KS = (3, 5, 7)
ATOL = 1e-12


def sample_column_stochastic(K, rng):
    """Each column ~ Dirichlet(1,...,1) on the K-simplex."""
    M = rng.dirichlet(np.ones(K), size=K).T  # rows: a*, cols: a
    return M


def lambda_of(C, pi, g):
    """
    lambda(C) := Var(E[g|A*]) / Var(g)
    where the joint law is P(A=k) = pi[k], P(A*=j|A=k) = C[j,k].
    """
    K = pi.size
    # Joint P(A*=j, A=k) = C[j,k] * pi[k]
    joint = C * pi[None, :]              # shape (K, K), rows j, cols k
    p_astar = joint.sum(axis=1)          # P(A*=j)
    # Conditional P(A=k | A*=j) = joint[j,k] / p_astar[j]
    # Handle degenerate columns (p_astar=0) by skipping their contribution.
    cond_mean = np.zeros(K)
    safe = p_astar > 0
    cond_mean[safe] = (joint[safe] @ g) / p_astar[safe]
    mean_g = pi @ g
    V_B = np.sum(p_astar * (cond_mean - mean_g) ** 2)
    V = float(np.sum(pi * (g - mean_g) ** 2))
    if V <= 0:
        return None  # g is constant on the support; lambda undefined
    return float(V_B / V)


def run():
    results = {"per_K": {}}
    overall_min = np.inf
    overall_max = -np.inf
    n_total = 0
    n_oob = 0

    for K in KS:
        mins = []
        maxs = []
        lambdas = []
        for _ in range(N_TRIALS_PER_K):
            C = sample_column_stochastic(K, RNG)
            pi = RNG.dirichlet(np.ones(K))
            g = RNG.normal(size=K)
            lam = lambda_of(C, pi, g)
            if lam is None:
                continue
            lambdas.append(lam)
            if lam < -ATOL or lam > 1.0 + ATOL:
                n_oob += 1
            mins.append(lam)
            maxs.append(lam)
        arr = np.array(lambdas)
        results["per_K"][K] = {
            "n_trials": int(arr.size),
            "min": float(arr.min()),
            "max": float(arr.max()),
            "mean": float(arr.mean()),
            "median": float(np.median(arr)),
            "n_out_of_bounds": int(((arr < -ATOL) | (arr > 1.0 + ATOL)).sum()),
        }
        overall_min = min(overall_min, float(arr.min()))
        overall_max = max(overall_max, float(arr.max()))
        n_total += int(arr.size)

    # Analytic extremes
    K_ref = 3
    pi_ref = np.array([0.4, 0.35, 0.25])
    g_ref = np.array([-0.7, 0.2, 1.1])
    lam_I = lambda_of(np.eye(K_ref), pi_ref, g_ref)
    lam_unif = lambda_of(np.full((K_ref, K_ref), 1.0 / K_ref), pi_ref, g_ref)

    results["extremes_K3"] = {
        "lambda_at_identity":    lam_I,
        "lambda_at_uniform_C":   lam_unif,
    }
    results["overall"] = {
        "n_total": n_total,
        "min": overall_min,
        "max": overall_max,
        "n_out_of_bounds": n_oob,
        "atol": ATOL,
    }

    out_path = Path(__file__).with_name("verify_lambda_bound_results.json")
    out_path.write_text(json.dumps(results, indent=2))

    print(f"K values tested: {KS}")
    for K, r in results["per_K"].items():
        print(f"  K={K}: n={r['n_trials']}, lambda in [{r['min']:.6f}, {r['max']:.6f}], OOB={r['n_out_of_bounds']}")
    print(f"Overall: n={n_total}, lambda in [{overall_min:.6f}, {overall_max:.6f}], OOB={n_oob}")
    print(f"Identity check (K=3):  lambda(I)       = {lam_I:.12f}  (expect 1.0)")
    print(f"Uniform-C check (K=3): lambda(1 1^T/K) = {lam_unif:.12e}  (expect 0.0)")
    print(f"Results written to {out_path}")

    assert overall_min >= -ATOL and overall_max <= 1.0 + ATOL, (
        f"BOUND VIOLATION: lambda outside [0,1] in {n_oob} of {n_total} trials"
    )
    assert abs(lam_I - 1.0) < 1e-12
    assert abs(lam_unif) < 1e-12


if __name__ == "__main__":
    run()
