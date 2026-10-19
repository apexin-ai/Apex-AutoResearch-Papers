#!/usr/bin/env python3
"""
MVP Validation: Exposure Misclassification DAG — K=3 vs K=2

Tests whether the binary "bias toward null" guarantee for non-differential
exposure misclassification breaks in the multiclass (K>=3) setting.

== Technical Setting ==
A is the EXPOSURE/TREATMENT variable, measured with error via LLM annotation.
No confounders. Simplest possible misclassification scenario.

  DAG: A -> Y, A -> A*
  DGP: Y = beta_0 + beta_1*1[A=1] + beta_2*1[A=2] + eps
  Misclassification: P(A*=j|A=i) = C[j,i], C column-stochastic

Researcher regresses Y ~ 1 + 1[A*=1] + 1[A*=2] instead of Y ~ 1 + 1[A=1] + 1[A=2].

== Binary Guarantee (K=2) ==
Non-differential misclassification of binary exposure guarantees bias toward
null: the estimated effect is attenuated (|gamma_hat| <= |beta|). This is
a classical result in measurement error literature.

== Key Question ==
Does this guarantee extend to K=3? Or can certain confusion matrix structures
produce:
  - SIGN REVERSAL: sign(gamma_hat_k) != sign(beta_k)
  - AMPLIFICATION: |gamma_hat_k| > |beta_k|

== Distinction from Lee & Wood-Doughty (2024) ==
We study OBSERVED exposure with noisy measurement (A observable, A* used at
scale). LWD study UNOBSERVED confounding with proxy (different identifiability).

Dependencies: numpy
"""

import numpy as np
from collections import OrderedDict
import time


# ============================================================
# DGP Parameters
# ============================================================
N_SAMPLES = 10_000
M_REPS = 1_000
N_RANDOM_SEARCH = 100_000
SEED = 42

P_A = np.array([0.4, 0.35, 0.25])
BETA = np.array([0.0, 1.0, -0.5])    # beta_0, beta_1, beta_2
SIGMA_Y = 1.0


# ============================================================
# Confusion Matrix Structures (reused from confounding DAG MVP)
# ============================================================

C1_SYMMETRIC_HIGH = np.array([
    [0.80, 0.10, 0.10],
    [0.10, 0.80, 0.10],
    [0.10, 0.10, 0.80],
])
C1_DESC = "Symmetric high-accuracy: diag=0.8, uniform off-diagonal=0.1"

C2_ASYMMETRIC = np.array([
    [0.65, 0.05, 0.10],
    [0.30, 0.85, 0.10],
    [0.05, 0.10, 0.80],
])
C2_DESC = "Asymmetric: P(A*=1|A=0)=0.30 >> P(A*=0|A=1)=0.05"

C3_STRUCTURAL_12 = np.array([
    [0.96, 0.01, 0.01],
    [0.02, 0.69, 0.30],
    [0.02, 0.30, 0.69],
])
C3_DESC = "Structural: classes 1<->2 heavily confused (0.30), class 0 clean"

C4_WEAK_DIAG = np.array([
    [0.40, 0.35, 0.25],
    [0.35, 0.40, 0.35],
    [0.25, 0.25, 0.40],
])
C4_DESC = "Weak diagonal dominance: diag~0.4, non-uniform off-diagonal"

C5_NEAR_PERM = np.array([
    [0.05, 0.05, 0.90],
    [0.90, 0.05, 0.05],
    [0.05, 0.90, 0.05],
])
C5_DESC = "Near-permutation: cyclic 0->1, 1->2, 2->0 (p=0.90)"

C6_DIFF_BASE = np.array([
    [0.80, 0.10, 0.10],
    [0.10, 0.80, 0.10],
    [0.10, 0.10, 0.80],
])
C6_DESC = "Differential base (=C1 in non-diff exposure setting; Y-dependent in MC)"


def make_confusion_matrices():
    """6 confusion matrix structures."""
    matrices = OrderedDict([
        ("1_sym_high",   (C1_SYMMETRIC_HIGH, C1_DESC)),
        ("2_asymmetric", (C2_ASYMMETRIC,     C2_DESC)),
        ("3_struct_12",  (C3_STRUCTURAL_12,  C3_DESC)),
        ("4_weak_diag",  (C4_WEAK_DIAG,      C4_DESC)),
        ("5_near_perm",  (C5_NEAR_PERM,      C5_DESC)),
        ("6_diff_base",  (C6_DIFF_BASE,      C6_DESC)),
    ])
    for name, (C, _) in matrices.items():
        assert np.allclose(C.sum(axis=0), 1.0), f"{name}: columns don't sum to 1"
    return matrices


# ============================================================
# Theoretical bias (exact)
# ============================================================
def theoretical_bias_exposure(C, p_A, beta):
    """
    plim gamma = (E[Z'Z])^{-1} E[Z'X] beta
    Z = (1, D*_1, D*_2),  X = (1, D_1, D_2)

    Returns: (plim_gamma, bias_vector)
    """
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

    plim = np.linalg.solve(EZZ, EZX @ beta)
    return plim, plim - beta


# ============================================================
# Data generation & OLS
# ============================================================
def _generate_Astar(A, C, rng):
    """Vectorized A* sampling from confusion matrix."""
    probs = C[:, A]
    cum = np.cumsum(probs, axis=0)
    u = rng.uniform(size=len(A))
    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))


def _generate_Astar_diff_Y(A, Y, C_base, rng, factor=2.0):
    """Differential: Y > median => off-diagonal rates scaled by factor."""
    C_high = C_base.copy()
    for col in range(3):
        diag_val = C_high[col, col]
        off_sum = 1.0 - diag_val
        new_off_sum = min(off_sum * factor, 0.95)
        scale = new_off_sum / off_sum if off_sum > 0 else 1.0
        for row in range(3):
            if row != col:
                C_high[row, col] *= scale
        C_high[col, col] = 1.0 - sum(C_high[r, col] for r in range(3) if r != col)

    Y_med = np.median(Y)
    high = Y > Y_med
    probs_low = C_base[:, A]
    probs_high = C_high[:, A]
    probs = np.where(high[np.newaxis, :], probs_high, probs_low)
    cum = np.cumsum(probs, axis=0)
    u = rng.uniform(size=len(A))
    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))


def ols_coefs(X, Y):
    """OLS coefficients."""
    return np.linalg.lstsq(X, Y, rcond=None)[0]


# ============================================================
# Monte Carlo
# ============================================================
def run_mc_exposure(M, N, C, p_A, beta, sigma_Y, seed, differential=False):
    rng = np.random.default_rng(seed)
    bias_misclass = np.empty((M, 3))

    for m in range(M):
        A = rng.choice(3, size=N, p=p_A)
        D1 = (A == 1).astype(float)
        D2 = (A == 2).astype(float)
        Y = beta[0] + beta[1] * D1 + beta[2] * D2 + rng.normal(0, sigma_Y, N)

        if differential:
            A_star = _generate_Astar_diff_Y(A, Y, C, rng)
        else:
            A_star = _generate_Astar(A, C, rng)

        D1s = (A_star == 1).astype(float)
        D2s = (A_star == 2).astype(float)
        X_star = np.column_stack([np.ones(N), D1s, D2s])
        gamma_hat = ols_coefs(X_star, Y)
        bias_misclass[m] = gamma_hat - beta

    return bias_misclass


# ============================================================
# Binary comparison
# ============================================================
def binary_attenuation_theory(C_bin, p_bin, beta_bin):
    """
    Binary exposure misclassification: plim from 2x2 system.
    Z = (1, D*), X = (1, D), beta = (beta_0, beta_1)
    """
    p0, p1 = p_bin
    q1 = C_bin[1, 0] * p0 + C_bin[1, 1] * p1

    EZZ = np.array([[1.0, q1], [q1, q1]])
    EZX = np.array([[1.0, p1], [q1, C_bin[1, 1] * p1]])

    plim = np.linalg.solve(EZZ, EZX @ beta_bin)
    return plim[1], plim[1] / beta_bin[1] if abs(beta_bin[1]) > 1e-10 else np.nan


def collapse_to_binary(C, p_A):
    """Derive 2x2 C from 3x3 by collapsing {1,2} -> 1."""
    p0, p1, p2 = p_A
    pB1 = p1 + p2

    c00 = C[0, 0]
    c10 = C[1, 0] + C[2, 0]
    c01 = (C[0, 1] * p1 + C[0, 2] * p2) / pB1
    c11 = 1.0 - c01

    C_bin = np.array([[c00, c01], [c10, c11]])
    p_bin = np.array([p0, pB1])
    beta_bin_eff = (BETA[1] * p1 + BETA[2] * p2) / pB1
    beta_bin = np.array([BETA[0], beta_bin_eff])

    return C_bin, p_bin, beta_bin


# ============================================================
# Random search for sign reversal / amplification
# ============================================================
def classify_bias(plim_gamma, beta):
    """Classify bias type for each component (1 and 2)."""
    results = {}
    for k in [1, 2]:
        g = plim_gamma[k]
        b = beta[k]
        if abs(b) < 1e-10:
            results[k] = "zero_true"
            continue
        if g * b < 0:
            results[k] = "SIGN_REVERSAL"
        elif abs(g) > abs(b):
            results[k] = "AMPLIFICATION"
        else:
            results[k] = "toward_null"
    return results


def random_search(n_search, p_A, beta, seed=0):
    """Search random column-stochastic C for bias-toward-null violations."""
    rng = np.random.default_rng(seed)

    sign_rev_count = 0
    amp_count = 0
    either_count = 0
    worst_cases = []

    for i in range(n_search):
        C = rng.dirichlet([1, 1, 1], size=3).T
        try:
            plim, bias = theoretical_bias_exposure(C, p_A, beta)
        except np.linalg.LinAlgError:
            continue

        types = classify_bias(plim, beta)
        has_sr = any(v == "SIGN_REVERSAL" for v in types.values())
        has_amp = any(v == "AMPLIFICATION" for v in types.values())

        if has_sr:
            sign_rev_count += 1
        if has_amp:
            amp_count += 1
        if has_sr or has_amp:
            either_count += 1
            severity = max(
                abs(plim[1] / beta[1]) if abs(beta[1]) > 1e-10 else 0,
                abs(plim[2] / beta[2]) if abs(beta[2]) > 1e-10 else 0,
            )
            worst_cases.append((severity, C.copy(), plim.copy(), types.copy()))

    worst_cases.sort(key=lambda x: -x[0])
    return {
        "n_searched": n_search,
        "sign_reversal": sign_rev_count,
        "amplification": amp_count,
        "either": either_count,
        "worst_cases": worst_cases[:10],
    }


# ============================================================
# Main
# ============================================================
def main():
    t_start = time.time()

    print("=" * 85)
    print("Exposure Misclassification DAG — K=3 Bias-Toward-Null Test")
    print("=" * 85)
    print()
    print("DAG: A -> Y, A -> A*  (no confounders, exposure misclassification only)")
    print(f"DGP: P(A)=[{P_A[0]}, {P_A[1]}, {P_A[2]}], "
          f"beta=[{BETA[0]}, {BETA[1]}, {BETA[2]}], sigma_Y={SIGMA_Y}")
    print(f"MC:  N={N_SAMPLES:,}, M={M_REPS:,}, seed={SEED}")
    print(f"Random search: {N_RANDOM_SEARCH:,} matrices")
    print()
    print("Binary guarantee: non-diff misclassification => |gamma| <= |beta| (attenuation)")
    print("K=3 question: does this hold for all C? Or can we get sign reversal / amplification?")

    matrices = make_confusion_matrices()

    # ── PART A: Theory + MC for 6 structures ─────────────────
    print("\n" + "=" * 85)
    print("PART A: K=3 Exposure — Theory vs Monte Carlo  (6 structures)")
    print("=" * 85)

    results = {}
    print(f"\n{'#':<2} {'Config':<14} | {'beta_1':>6} {'g1_th':>8} {'g1_mc':>8} {'type_1':>15} "
          f"| {'beta_2':>6} {'g2_th':>8} {'g2_mc':>8} {'type_2':>15} | {'Match':>5}")
    print("-" * 115)

    for name, (C, desc) in matrices.items():
        t0 = time.time()
        idx = name[0]
        is_diff = (name == "6_diff_base")

        # Theory (exact for non-differential; C6 base = C1, so same theory)
        plim_th, bias_th = theoretical_bias_exposure(C, P_A, BETA)

        # MC
        mc_bias = run_mc_exposure(M_REPS, N_SAMPLES, C, P_A, BETA, SIGMA_Y, SEED,
                                  differential=is_diff)

        mc_mean = mc_bias.mean(axis=0)
        mc_se = mc_bias.std(axis=0, ddof=1)
        ci_lo = mc_mean - 1.96 * mc_se / np.sqrt(M_REPS)
        ci_hi = mc_mean + 1.96 * mc_se / np.sqrt(M_REPS)

        match_1 = ci_lo[1] <= bias_th[1] <= ci_hi[1]
        match_2 = ci_lo[2] <= bias_th[2] <= ci_hi[2]
        if is_diff:
            match_all = True  # no exact theory for differential
            match_str = "N/A"
        else:
            match_all = match_1 and match_2
            match_str = "YES" if match_all else "**NO**"

        types = classify_bias(plim_th, BETA)
        elapsed = time.time() - t0

        results[name] = dict(
            plim=plim_th, bias=bias_th, mc_mean=mc_mean + BETA,
            mc_bias_mean=mc_mean, ci=(ci_lo, ci_hi), match=match_all,
            types=types, is_diff=is_diff)

        g1_mc = mc_mean[1] + BETA[1]  # plim gamma_1
        g2_mc = mc_mean[2] + BETA[2]

        print(f"{idx:<2} {name:<14} | {BETA[1]:>6.2f} {plim_th[1]:>8.4f} {g1_mc:>8.4f} "
              f"{types[1]:>15} | {BETA[2]:>6.2f} {plim_th[2]:>8.4f} {g2_mc:>8.4f} "
              f"{types[2]:>15} | {match_str:>5}  ({elapsed:.1f}s)")

    # ── PART B: 100k Random Search ───────────────────────────
    print("\n" + "=" * 85)
    print(f"PART B: Random Search — {N_RANDOM_SEARCH:,} column-stochastic C matrices")
    print("=" * 85)

    t0 = time.time()
    search = random_search(N_RANDOM_SEARCH, P_A, BETA, seed=12345)
    elapsed_search = time.time() - t0

    print(f"\nSearched: {search['n_searched']:,} matrices ({elapsed_search:.1f}s)")
    print(f"Sign reversal (any component):  {search['sign_reversal']:,} "
          f"({100*search['sign_reversal']/search['n_searched']:.1f}%)")
    print(f"Amplification (any component):  {search['amplification']:,} "
          f"({100*search['amplification']/search['n_searched']:.1f}%)")
    print(f"Either violation:               {search['either']:,} "
          f"({100*search['either']/search['n_searched']:.1f}%)")

    if search['worst_cases']:
        print(f"\nTop-5 most extreme violations (by max |gamma_k/beta_k|):")
        print(f"  {'Severity':>8} {'g1':>8} {'type_1':>15} {'g2':>8} {'type_2':>15}")
        print(f"  {'-'*58}")
        for sev, C_worst, plim_worst, types_worst in search['worst_cases'][:5]:
            print(f"  {sev:>8.2f} {plim_worst[1]:>8.4f} {types_worst[1]:>15} "
                  f"{plim_worst[2]:>8.4f} {types_worst[2]:>15}")
            for row in C_worst:
                print(f"    [{row[0]:.3f}  {row[1]:.3f}  {row[2]:.3f}]")
            print()

    # ── PART C: MC validation of worst-case C ────────────────
    if search['worst_cases']:
        print("=" * 85)
        print("PART C: MC Validation of Worst-Case C from Random Search")
        print("=" * 85)

        _, C_worst, plim_worst, types_worst = search['worst_cases'][0]
        print(f"\nWorst-case C (severity={search['worst_cases'][0][0]:.2f}):")
        for row in C_worst:
            print(f"  [{row[0]:.3f}  {row[1]:.3f}  {row[2]:.3f}]")

        mc_worst = run_mc_exposure(M_REPS, N_SAMPLES, C_worst, P_A, BETA, SIGMA_Y, SEED + 1)
        mc_mean_w = mc_worst.mean(axis=0)
        mc_se_w = mc_worst.std(axis=0, ddof=1)

        print(f"\n{'Component':<10} {'beta':>8} {'Theory':>8} {'MC Mean':>8} "
              f"{'MC SE':>8} {'Type':>15}")
        print("-" * 60)
        for k in [1, 2]:
            th_g = plim_worst[k]
            mc_g = mc_mean_w[k] + BETA[k]
            print(f"{'beta_'+str(k):<10} {BETA[k]:>8.4f} {th_g:>8.4f} {mc_g:>8.4f} "
                  f"{mc_se_w[k]:>8.4f} {types_worst[k]:>15}")

    # ── PART D: Binary K=2 Comparison ────────────────────────
    print("\n" + "=" * 85)
    print("PART D: Binary (K=2) Comparison — Attenuation Guarantee")
    print("=" * 85)

    print(f"\nCollapse: B=1[A in {{1,2}}]. Binary beta_B = "
          f"E[beta_1*p1 + beta_2*p2]/(p1+p2) = "
          f"{(BETA[1]*P_A[1] + BETA[2]*P_A[2])/(P_A[1]+P_A[2]):.4f}")

    print(f"\n{'#':<2} {'Config':<14} {'C_bin diag':>10} {'beta_B':>8} "
          f"{'gamma_B':>8} {'ratio':>8} {'Toward null?':>13}")
    print("-" * 72)

    for name, (C, desc) in matrices.items():
        C_bin, p_bin, beta_bin = collapse_to_binary(C, P_A)
        gamma_B, ratio = binary_attenuation_theory(C_bin, p_bin, beta_bin)
        toward_null = abs(gamma_B) <= abs(beta_bin[1]) + 1e-10
        idx = name[0]

        print(f"{idx:<2} {name:<14} [{C_bin[0,0]:.2f},{C_bin[1,1]:.2f}] "
              f"{beta_bin[1]:>8.4f} {gamma_B:>8.4f} {ratio:>8.4f} "
              f"{'YES (|r|<=1)' if toward_null else '**NO**':>13}")

    # ── PART E: K=3 vs K=2 Direct Comparison ─────────────────
    print("\n" + "=" * 85)
    print("PART E: K=3 vs K=2 — Does Binary Guarantee Extend to Multiclass?")
    print("=" * 85)

    print(f"\n{'#':<2} {'Config':<14} | {'K3: g1':>8} {'type_1':>15} {'g2':>8} "
          f"{'type_2':>15} | {'K2: toward_null':>15}")
    print("-" * 95)

    k3_violations = 0
    for name, (C, desc) in matrices.items():
        idx = name[0]
        r = results[name]
        C_bin, p_bin, beta_bin = collapse_to_binary(C, P_A)
        gamma_B, ratio = binary_attenuation_theory(C_bin, p_bin, beta_bin)
        k2_tn = abs(ratio) <= 1.0 + 1e-10

        has_violation = any(v in ("SIGN_REVERSAL", "AMPLIFICATION")
                          for v in r['types'].values())
        if has_violation:
            k3_violations += 1

        print(f"{idx:<2} {name:<14} | {r['plim'][1]:>8.4f} {r['types'][1]:>15} "
              f"{r['plim'][2]:>8.4f} {r['types'][2]:>15} | "
              f"{'YES' if k2_tn else 'NO':>15}")

    # ── Pass/Fail ────────────────────────────────────────────
    print("\n" + "=" * 85)
    print("PASS / FAIL SUMMARY")
    print("=" * 85)

    # C1: Theory-MC match (non-differential only)
    nondiff_results = {n: r for n, r in results.items() if not r['is_diff']}
    n_match = sum(1 for r in nondiff_results.values() if r['match'])
    n_nondiff = len(nondiff_results)
    c1 = n_match == n_nondiff
    print(f"\n1. Theory vs MC match (non-diff): {n_match}/{n_nondiff}  "
          f"{'PASS' if c1 else 'FAIL'}")
    for name, r in nondiff_results.items():
        ci = r['ci']
        print(f"   {name}: th_bias=[{r['bias'][1]:.6f}, {r['bias'][2]:.6f}], "
              f"CI_1=[{ci[0][1]:.6f}, {ci[1][1]:.6f}], "
              f"CI_2=[{ci[0][2]:.6f}, {ci[1][2]:.6f}] -> "
              f"{'OK' if r['match'] else 'MISMATCH'}")

    # C2: Sign reversal or amplification found
    c2_struct = k3_violations > 0
    c2_search = search['either'] > 0
    c2 = c2_struct or c2_search
    print(f"\n2. Bias-toward-null violation found: "
          f"{'PASS' if c2 else 'FAIL'}")
    print(f"   Named structures with violation: {k3_violations}/6")
    print(f"   Random search violations: {search['either']:,}/{search['n_searched']:,}")

    # C3: Binary always toward null, K=3 sometimes not
    all_k2_tn = True
    for name, (C, desc) in matrices.items():
        C_bin, p_bin, beta_bin = collapse_to_binary(C, P_A)
        _, ratio = binary_attenuation_theory(C_bin, p_bin, beta_bin)
        if abs(ratio) > 1.0 + 1e-10:
            all_k2_tn = False
    c3 = all_k2_tn and c2
    print(f"\n3. K=2 always toward null AND K=3 sometimes not: "
          f"{'PASS' if c3 else 'FAIL'}")
    print(f"   K=2 all toward null: {'YES' if all_k2_tn else 'NO'}")
    print(f"   K=3 has violations: {'YES' if c2 else 'NO'}")

    overall = c1 and c2 and c3
    print(f"\nOVERALL: {'PASS' if overall else 'FAIL'}")

    # ── Appendix: Confusion Matrices ─────────────────────────
    print("\n" + "=" * 85)
    print("APPENDIX: Confusion Matrix Definitions")
    print("=" * 85)
    for name, (C, desc) in matrices.items():
        print(f"\n{name}: {desc}")
        for row in C:
            print(f"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]")

    elapsed_total = time.time() - t_start
    print(f"\nTotal runtime: {elapsed_total:.1f}s")


if __name__ == "__main__":
    main()
