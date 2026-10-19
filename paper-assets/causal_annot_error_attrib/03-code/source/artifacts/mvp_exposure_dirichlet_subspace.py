#!/usr/bin/env python3
"""
Dirichlet Prior Subspace Analysis for Exposure Misclassification

The 85% violation rate from mvp_exposure_dag.py uses Dirichlet(1,1,1) uniform
prior over column-stochastic matrices. Actual LLM confusion matrices are far
more diagonal-dominant. This script stratifies the violation rate by minimum
diagonal value of C to assess practical relevance.

Subspaces:
  - Full space (no diagonal constraint, equiv. Dirichlet(1,1,1))
  - min(diag(C)) >= 0.5
  - min(diag(C)) >= 0.7  (realistic LLM accuracy)
  - min(diag(C)) >= 0.9  (high-accuracy LLM)

Method: direct sampling via truncated Beta(1,2) for diagonal entries +
uniform simplex split for off-diagonal. Equivalent to uniform distribution
on the constrained space, but O(n) time/memory vs rejection sampling.

For K=3, each column's diagonal entry d ~ Beta(1,2) truncated to [thresh,1],
density f(d) = 2(1-d)/(1-thresh)^2. Inverse CDF: d = 1-(1-thresh)*sqrt(1-U).

Dependencies: numpy
"""

import numpy as np
import time

P_A = np.array([0.4, 0.35, 0.25])
BETA = np.array([0.0, 1.0, -0.5])

DIAG_THRESHOLDS = [0.0, 0.5, 0.7, 0.9]
N_SAMPLES = 50_000


def theoretical_plim(C, p_A, beta):
    """plim gamma = (E[Z'Z])^{-1} E[Z'X] beta for exposure DAG."""
    p0, p1, p2 = p_A
    q = C @ p_A
    EZZ = np.array([
        [1.0,  q[1], q[2]],
        [q[1], q[1], 0.0],
        [q[2], 0.0,  q[2]],
    ])
    EZX = np.array([
        [1.0,  p1,            p2],
        [q[1], C[1, 1] * p1,  C[1, 2] * p2],
        [q[2], C[2, 1] * p1,  C[2, 2] * p2],
    ])
    return np.linalg.solve(EZZ, EZX @ beta)


def sample_and_analyze(n, diag_thresh, p_A, beta, rng):
    """
    Sample n column-stochastic 3x3 C with min(diag) >= diag_thresh,
    compute plim for each, return statistics. No large array stored.
    """
    n_sr = 0       # sign reversal (any component)
    n_amp = 0      # amplification (any component)
    n_either = 0   # any violation
    n_valid = 0

    worst_sev = 0.0
    worst_C = None
    worst_plim = None

    # Process in manageable chunks
    chunk = min(n, 5000)
    remaining = n

    while remaining > 0:
        batch = min(chunk, remaining)
        remaining -= batch

        # Direct sampling: each column independently
        C_batch = np.empty((batch, 3, 3))
        for col in range(3):
            U = rng.uniform(size=batch)
            d = 1.0 - (1.0 - diag_thresh) * np.sqrt(1.0 - U)
            V = rng.uniform(size=batch)
            rem = 1.0 - d

            off = [r for r in range(3) if r != col]
            C_batch[:, col, col] = d
            C_batch[:, off[0], col] = rem * V
            C_batch[:, off[1], col] = rem * (1.0 - V)

        # Analyze each C
        for i in range(batch):
            C = C_batch[i]
            try:
                plim = theoretical_plim(C, p_A, beta)
            except np.linalg.LinAlgError:
                continue

            n_valid += 1
            sr = False
            amp = False
            for k in [1, 2]:
                if abs(beta[k]) < 1e-10:
                    continue
                if plim[k] * beta[k] < 0:
                    sr = True
                if abs(plim[k]) > abs(beta[k]):
                    amp = True

            if sr:
                n_sr += 1
            if amp:
                n_amp += 1
            if sr or amp:
                n_either += 1
                sev = max(
                    abs(plim[1] / beta[1]) if abs(beta[1]) > 1e-10 else 0,
                    abs(plim[2] / beta[2]) if abs(beta[2]) > 1e-10 else 0,
                )
                if sev > worst_sev:
                    worst_sev = sev
                    worst_C = C.copy()
                    worst_plim = plim.copy()

    return {
        "n_valid": n_valid,
        "n_violation": n_either,
        "n_sign_rev": n_sr,
        "n_amp": n_amp,
        "violation_rate": n_either / n_valid if n_valid > 0 else 0,
        "sign_rev_rate": n_sr / n_valid if n_valid > 0 else 0,
        "amp_rate": n_amp / n_valid if n_valid > 0 else 0,
        "worst_severity": worst_sev,
        "worst_C": worst_C,
        "worst_plim": worst_plim,
    }


def main():
    t_start = time.time()
    rng = np.random.default_rng(42)

    print("=" * 85)
    print("Dirichlet Subspace Analysis: Exposure Misclassification Violation Rates")
    print("=" * 85)
    print()
    print(f"DGP: P(A)=[{P_A[0]}, {P_A[1]}, {P_A[2]}], "
          f"beta=[{BETA[0]}, {BETA[1]}, {BETA[2]}]")
    print(f"Samples per subspace: {N_SAMPLES:,}")
    print(f"Method: direct sampling (truncated Beta(1,2) diagonal + uniform split)")

    # ── Main table ───────────────────────────────────────────
    print(f"\n{'Subspace':>12} {'N':>8} {'Violation%':>11} "
          f"{'SignRev%':>10} {'Amplif%':>10} {'Worst':>8} {'Time':>7}")
    print("-" * 70)

    all_results = {}

    for thresh in DIAG_THRESHOLDS:
        t0 = time.time()
        label = f"diag>={thresh:.1f}" if thresh > 0 else "full"

        res = sample_and_analyze(N_SAMPLES, thresh, P_A, BETA, rng)
        elapsed = time.time() - t0

        all_results[thresh] = res

        print(f"{label:>12} {res['n_valid']:>8,} {100*res['violation_rate']:>10.1f}% "
              f"{100*res['sign_rev_rate']:>9.1f}% {100*res['amp_rate']:>9.1f}% "
              f"{res['worst_severity']:>8.2f} {elapsed:>6.1f}s")

    # ── Worst-case per subspace ──────────────────────────────
    print("\n" + "=" * 85)
    print("Worst-Case C per Subspace")
    print("=" * 85)

    for thresh, res in all_results.items():
        label = f"diag>={thresh:.1f}" if thresh > 0 else "full"
        if res['worst_C'] is None:
            print(f"\n{label}: no violations found")
            continue

        C_w = res['worst_C']
        p_w = res['worst_plim']
        print(f"\n{label} (severity={res['worst_severity']:.2f}, "
              f"diag=[{C_w[0,0]:.3f}, {C_w[1,1]:.3f}, {C_w[2,2]:.3f}]):")
        for row in C_w:
            print(f"  [{row[0]:.3f}  {row[1]:.3f}  {row[2]:.3f}]")

        for k in [1, 2]:
            if abs(BETA[k]) > 1e-10:
                ratio = p_w[k] / BETA[k]
                if p_w[k] * BETA[k] < 0:
                    tag = "SIGN REVERSAL"
                elif abs(p_w[k]) > abs(BETA[k]):
                    tag = "AMPLIFICATION"
                else:
                    tag = "toward null"
                print(f"  beta_{k}={BETA[k]:.2f} -> gamma_{k}={p_w[k]:.4f} "
                      f"(ratio={ratio:.2f}, {tag})")

    # ── Paper framing guidance ───────────────────────────────
    print("\n" + "=" * 85)
    print("PAPER FRAMING GUIDANCE")
    print("=" * 85)

    print(f"\n{'Subspace':<15} {'Violation':>10} {'SignRev':>10} {'Amplif':>10} {'Assessment':>25}")
    print("-" * 73)
    for thresh, res in all_results.items():
        label = f"diag>={thresh:.1f}" if thresh > 0 else "full space"
        vr = res['violation_rate']
        if vr > 0.10:
            assess = "STRONG argument"
        elif vr > 0.01:
            assess = "moderate (note scope)"
        elif vr > 0.001:
            assess = "weak (flag in paper)"
        elif vr > 0:
            assess = "rare (theoretical only)"
        else:
            assess = "no violations"
        print(f"{label:<15} {100*vr:>9.1f}% {100*res['sign_rev_rate']:>9.1f}% "
              f"{100*res['amp_rate']:>9.1f}% {assess:>25}")

    elapsed_total = time.time() - t_start
    print(f"\nTotal runtime: {elapsed_total:.1f}s")


if __name__ == "__main__":
    main()
