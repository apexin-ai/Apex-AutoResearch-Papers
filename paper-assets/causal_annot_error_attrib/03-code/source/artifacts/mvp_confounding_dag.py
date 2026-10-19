#!/usr/bin/env python3
"""
MVP Validation: Confounding DAG with K=3 Multiclass Annotation Error

== Technical Setting ==
A is an OBSERVED confounder measured with error via LLM annotation.
The researcher observes A but uses A* (LLM-annotated proxy) to control
for confounding in regression adjustment.

  DAG: A -> T, A -> Y, T -> Y, A -> A*
  Estimand: E[Y|do(T=t)] estimated via OLS adjusting for A*

This differs from Lee & Wood-Doughty (2024), who study UNOBSERVED
confounding where A is never observed and A* is the only available proxy.
Their setting involves different identifiability conditions (proxy must
satisfy relevance + exclusion). Our setting: A is observable in principle
but measured with classification error by an LLM annotator, creating a
known-structure noise process (confusion matrix C).

== DGP ==
  A in {0,1,2}: true 3-class confounder, P(A=k) configurable
  T = alpha_1*1[A=1] + alpha_2*1[A=2] + eta,  eta ~ N(0, sigma_T^2)
  Y = beta_T*T + beta_1*1[A=1] + beta_2*1[A=2] + eps,  eps ~ N(0, sigma_Y^2)
  P(A*=j|A=i) = C[j,i]  (C is column-stochastic 3x3 matrix)

== Key Result ==
  plim gamma_hat = (E[Z'Z])^{-1} E[Z'X] beta
  where Z = (1, T, D*_1, D*_2), X = (1, T, D_1, D_2)
  Theoretical bias on beta_T = gamma_hat[1] - beta_T

== Pass Criteria ==
  1. Theory vs MC 95% CI match: 6/6
  2. >=1 non-differential C produces away-from-null bias
  3. Binary collapse bias != multiclass theory prediction

Dependencies: numpy, scipy
"""

import numpy as np
from collections import OrderedDict
import time


# ============================================================
# DGP Parameters
# ============================================================
N_SAMPLES = 10_000
M_REPS = 1_000
SEED = 42

P_A = np.array([0.4, 0.35, 0.25])
ALPHA = np.array([1.5, -1.0])        # alpha_1, alpha_2
BETA_T = 2.0                          # true causal effect of T on Y
BETA_A = np.array([1.0, -0.5])       # beta_1, beta_2 (direct A->Y)
SIGMA_T = 1.0
SIGMA_Y = 1.0


# ============================================================
# Confusion Matrix Structures (named constants)
# ============================================================

# --- Non-differential (C independent of T) ---

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
C3_DESC = "Structural: classes 1<->2 heavily confused (0.30), class 0 clean (off<0.02)"

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
C5_DESC = "Near-permutation: cyclic shift 0->1, 1->2, 2->0 (p=0.90)"

# --- Differential (C depends on T) ---

C6_DIFF_BASE = np.array([
    [0.80, 0.10, 0.10],
    [0.10, 0.80, 0.10],
    [0.10, 0.10, 0.80],
])
C6_DESC = "Differential: base=C1, off-diagonal doubled when T>median"


def make_confusion_matrices():
    """6 confusion matrix structures: 5 non-differential + 1 differential."""
    matrices = OrderedDict([
        ("1_sym_high",   (C1_SYMMETRIC_HIGH, False, C1_DESC)),
        ("2_asymmetric", (C2_ASYMMETRIC,     False, C2_DESC)),
        ("3_struct_12",  (C3_STRUCTURAL_12,  False, C3_DESC)),
        ("4_weak_diag",  (C4_WEAK_DIAG,      False, C4_DESC)),
        ("5_near_perm",  (C5_NEAR_PERM,      False, C5_DESC)),
        ("6_differen",   (C6_DIFF_BASE,      True,  C6_DESC)),
    ])
    for name, (C, _, desc) in matrices.items():
        assert np.allclose(C.sum(axis=0), 1.0), f"{name}: columns don't sum to 1"
        assert (C >= 0).all(), f"{name}: negative entries"
    return matrices


# ============================================================
# Theoretical bias (exact, for non-differential C)
# ============================================================
def theoretical_bias_exact(C, p_A, alpha, beta_T, beta_A, sigma_T):
    """
    plim gamma = (E[Z'Z])^{-1} E[Z'X] beta
    Z = (1, T, D*_1, D*_2),  X = (1, T, D_1, D_2)
    """
    p0, p1, p2 = p_A
    a1, a2 = alpha
    b1, b2 = beta_A
    beta = np.array([0.0, beta_T, b1, b2])

    ET = a1 * p1 + a2 * p2
    ET2 = a1**2 * p1 + a2**2 * p2 + sigma_T**2
    q = C @ p_A
    ET_Ds = np.array([a1 * C[j, 1] * p1 + a2 * C[j, 2] * p2 for j in range(3)])

    EZZ = np.array([
        [1.0,  ET,       q[1],      q[2]],
        [ET,   ET2,      ET_Ds[1],  ET_Ds[2]],
        [q[1], ET_Ds[1], q[1],      0.0],
        [q[2], ET_Ds[2], 0.0,       q[2]],
    ])
    EZX = np.array([
        [1.0,  ET,       p1,             p2],
        [ET,   ET2,      a1 * p1,        a2 * p2],
        [q[1], ET_Ds[1], C[1, 1] * p1,   C[1, 2] * p2],
        [q[2], ET_Ds[2], C[2, 1] * p1,   C[2, 2] * p2],
    ])

    plim = np.linalg.solve(EZZ, EZX @ beta)
    return plim[1] - beta_T, plim


def theoretical_bias_largesample(C_base, p_A, alpha, beta_T, beta_A,
                                  sigma_T, sigma_Y, N_approx=2_000_000,
                                  seed=999):
    """Approximate theoretical bias for differential C via large-sample moments."""
    rng = np.random.default_rng(seed)
    a1, a2 = alpha

    A = rng.choice(3, size=N_approx, p=p_A)
    D1 = (A == 1).astype(np.float64)
    D2 = (A == 2).astype(np.float64)
    T = a1 * D1 + a2 * D2 + rng.normal(0, sigma_T, N_approx)

    A_star = _generate_Astar_differential(A, T, C_base, rng)
    D1s = (A_star == 1).astype(np.float64)
    D2s = (A_star == 2).astype(np.float64)

    beta = np.array([0.0, beta_T, beta_A[0], beta_A[1]])
    ones = np.ones(N_approx)
    Z = np.column_stack([ones, T, D1s, D2s])
    X = np.column_stack([ones, T, D1, D2])

    EZZ = (Z.T @ Z) / N_approx
    EZX = (Z.T @ X) / N_approx
    plim = np.linalg.solve(EZZ, EZX @ beta)
    return plim[1] - beta_T, plim


# ============================================================
# Data generation
# ============================================================
def _generate_Astar_nondiff(A, C, rng):
    """Vectorized: sample A* from C[:, A[i]] for each i."""
    probs = C[:, A]                          # (3, N)
    cum = np.cumsum(probs, axis=0)           # (3, N)
    u = rng.uniform(size=A.shape[0])
    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))


def _make_C_high(C_base, factor=2.0):
    """Scale off-diagonal entries by factor, renormalize columns."""
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
    return C_high


def _generate_Astar_differential(A, T, C_base, rng):
    """T > median => off-diagonal rates doubled."""
    N = len(A)
    C_high = _make_C_high(C_base, factor=2.0)
    T_med = np.median(T)
    high = T > T_med

    probs_low = C_base[:, A]
    probs_high = C_high[:, A]
    probs = np.where(high[np.newaxis, :], probs_high, probs_low)

    cum = np.cumsum(probs, axis=0)
    u = rng.uniform(size=N)
    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))


def generate_data(N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,
                  differential, rng):
    a1, a2 = alpha
    b1, b2 = beta_A

    A = rng.choice(3, size=N, p=p_A)
    D1 = (A == 1).astype(np.float64)
    D2 = (A == 2).astype(np.float64)
    T = a1 * D1 + a2 * D2 + rng.normal(0, sigma_T, N)
    Y = beta_T * T + b1 * D1 + b2 * D2 + rng.normal(0, sigma_Y, N)

    if differential:
        A_star = _generate_Astar_differential(A, T, C, rng)
    else:
        A_star = _generate_Astar_nondiff(A, C, rng)

    return A, T, Y, A_star


# ============================================================
# OLS helper
# ============================================================
def ols_beta_T(T, Y, dummies):
    """OLS Y ~ 1 + T + dummies, return coefficient on T."""
    X = np.column_stack([np.ones(len(T)), T, dummies])
    coef, _, _, _ = np.linalg.lstsq(X, Y, rcond=None)
    return coef[1]


# ============================================================
# Monte Carlo
# ============================================================
def run_mc(M, N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,
           differential, seed):
    rng = np.random.default_rng(seed)
    bias_true = np.empty(M)
    bias_misclass = np.empty(M)

    for m in range(M):
        A, T, Y, A_star = generate_data(
            N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,
            differential, rng)
        D_true = np.column_stack([(A == 1).astype(float), (A == 2).astype(float)])
        D_star = np.column_stack([(A_star == 1).astype(float),
                                   (A_star == 2).astype(float)])
        bias_true[m] = ols_beta_T(T, Y, D_true) - beta_T
        bias_misclass[m] = ols_beta_T(T, Y, D_star) - beta_T

    return bias_true, bias_misclass


# ============================================================
# Unadjusted bias (omitted variable reference)
# ============================================================
def unadjusted_bias(p_A, alpha, beta_T, beta_A, sigma_T):
    """plim of OLS Y ~ 1 + T (no confounder control)."""
    p0, p1, p2 = p_A
    a1, a2 = alpha
    b1, b2 = beta_A
    ET = a1 * p1 + a2 * p2
    VarT = a1**2 * p1 + a2**2 * p2 + sigma_T**2 - ET**2
    CovD1T = a1 * p1 - p1 * ET
    CovD2T = a2 * p2 - p2 * ET
    return (b1 * CovD1T + b2 * CovD2T) / VarT


# ============================================================
# Binary collapse analysis
# ============================================================
def theoretical_bias_binary_from_C3(C, p_A, alpha, beta_T, beta_A, sigma_T):
    """
    Theoretical bias when collapsing A to B=1[A in {1,2}], B*=1[A* in {1,2}].
    Z = (1, T, B*),  X = (1, T, D1, D2)
    plim = (E[Z'Z])^{-1} E[Z'X] beta
    """
    p0, p1, p2 = p_A
    a1, a2 = alpha
    b1, b2 = beta_A
    beta = np.array([0.0, beta_T, b1, b2])

    ET = a1 * p1 + a2 * p2
    ET2 = a1**2 * p1 + a2**2 * p2 + sigma_T**2

    q = C @ p_A
    q_Bs = q[1] + q[2]

    ET_Ds = np.array([a1 * C[j, 1] * p1 + a2 * C[j, 2] * p2 for j in range(3)])
    ET_Bs = ET_Ds[1] + ET_Ds[2]

    EZZ = np.array([
        [1.0,    ET,    q_Bs],
        [ET,     ET2,   ET_Bs],
        [q_Bs,   ET_Bs, q_Bs],
    ])

    EB_D1 = (1.0 - C[0, 1]) * p1
    EB_D2 = (1.0 - C[0, 2]) * p2

    EZX = np.array([
        [1.0,    ET,     p1,       p2],
        [ET,     ET2,    a1 * p1,  a2 * p2],
        [q_Bs,   ET_Bs,  EB_D1,    EB_D2],
    ])

    plim = np.linalg.solve(EZZ, EZX @ beta)
    return plim[1] - beta_T


def run_mc_binary_collapse(M, N, C, p_A, alpha, beta_T, beta_A,
                           sigma_T, sigma_Y, differential, seed):
    """MC with binary collapse: B=1[A in {1,2}], B*=1[A* in {1,2}]."""
    rng = np.random.default_rng(seed)
    bias_bin = np.empty(M)

    for m in range(M):
        A, T, Y, A_star = generate_data(
            N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,
            differential, rng)
        B_star = ((A_star == 1) | (A_star == 2)).astype(float).reshape(-1, 1)
        bias_bin[m] = ols_beta_T(T, Y, B_star) - beta_T

    return bias_bin


# ============================================================
# Main
# ============================================================
def main():
    print("=" * 85)
    print("MVP Validation: Confounding DAG — K=3 Multiclass Annotation Error Bias")
    print("=" * 85)
    print()
    print("Setting: A is OBSERVED confounder with noisy LLM annotation A*.")
    print("         Researcher adjusts for A* (not A) in OLS.  DAG: A->T, A->Y, T->Y, A->A*")
    print("         (cf. Lee & Wood-Doughty 2024: UNOBSERVED confounding with proxy)")
    print()
    print(f"DGP: P(A)=[{P_A[0]}, {P_A[1]}, {P_A[2]}], "
          f"alpha=[{ALPHA[0]}, {ALPHA[1]}], "
          f"beta_T={BETA_T}, beta_A=[{BETA_A[0]}, {BETA_A[1]}]")
    print(f"     sigma_T={SIGMA_T}, sigma_Y={SIGMA_Y}")
    print(f"MC:  N={N_SAMPLES:,}, M={M_REPS:,}, seed={SEED}")

    ovb = unadjusted_bias(P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)
    print(f"\nUnadjusted OVB (no A control): {ovb:.6f}")
    print(f"  => plim(beta_T_hat_unadj) = {BETA_T + ovb:.6f}")
    print(f"  => Direction: {'toward null' if ovb * BETA_T < 0 else 'away from null'}")

    matrices = make_confusion_matrices()

    # ── PART A: K=3 Theory vs MC ──────────────────────────────
    print("\n" + "=" * 85)
    print("PART A: K=3 Multiclass — Theory vs Monte Carlo  (6 structures)")
    print("=" * 85)

    results_k3 = {}
    header = (f"{'#':<2} {'Config':<14} {'Theory':>10} {'MC Mean':>10} "
              f"{'MC 95% CI':>22} {'Match?':>7} {'Direction':>14}")
    print(f"\n{header}")
    print("-" * len(header))

    for name, (C, is_diff, desc) in matrices.items():
        t0 = time.time()
        idx = name[0]

        if is_diff:
            th_bias, _ = theoretical_bias_largesample(
                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T, SIGMA_Y)
        else:
            th_bias, _ = theoretical_bias_exact(
                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)

        _, mc_bias = run_mc(M_REPS, N_SAMPLES, C, P_A, ALPHA, BETA_T,
                            BETA_A, SIGMA_T, SIGMA_Y, is_diff, SEED)

        mc_mean = mc_bias.mean()
        mc_se = mc_bias.std(ddof=1)
        ci_lo = mc_mean - 1.96 * mc_se / np.sqrt(M_REPS)
        ci_hi = mc_mean + 1.96 * mc_se / np.sqrt(M_REPS)
        match = ci_lo <= th_bias <= ci_hi

        if abs(th_bias) < 1e-6:
            direction = "~zero"
        elif th_bias * BETA_T > 0:
            direction = "AWAY from null"
        else:
            direction = "toward null"

        elapsed = time.time() - t0
        results_k3[name] = dict(
            th_bias=th_bias, mc_mean=mc_mean, ci=(ci_lo, ci_hi),
            match=match, direction=direction, mc_bias_arr=mc_bias,
            is_diff=is_diff)

        print(f"{idx:<2} {name:<14} {th_bias:>10.6f} {mc_mean:>10.6f} "
              f"[{ci_lo:>9.6f}, {ci_hi:>9.6f}] "
              f"{'YES' if match else '**NO**':>7} "
              f"{direction:>14}  ({elapsed:.1f}s)")

    # ── PART B: Binary collapse ──────────────────────────────
    print("\n" + "=" * 85)
    print("PART B: Binary Collapse — B=1[A in {1,2}]")
    print("=" * 85)

    header_b = (f"{'#':<2} {'Config':<14} {'K3 Bias':>10} {'Bin Bias':>10} "
                f"{'Bin MC':>10} {'Bin MC 95% CI':>22} {'K3!=Bin?':>8}")
    print(f"\n{header_b}")
    print("-" * len(header_b))

    pass_criterion_3 = False
    bin_results = {}

    for name, (C, is_diff, desc) in matrices.items():
        t0 = time.time()
        idx = name[0]
        k3_bias = results_k3[name]["th_bias"]

        if not is_diff:
            bin_th = theoretical_bias_binary_from_C3(
                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)
        else:
            rng_approx = np.random.default_rng(888)
            N_ap = 2_000_000
            A_ap = rng_approx.choice(3, size=N_ap, p=P_A)
            D1_ap = (A_ap == 1).astype(np.float64)
            D2_ap = (A_ap == 2).astype(np.float64)
            T_ap = (ALPHA[0] * D1_ap + ALPHA[1] * D2_ap
                    + rng_approx.normal(0, SIGMA_T, N_ap))
            As_ap = _generate_Astar_differential(A_ap, T_ap, C, rng_approx)
            Bs_ap = ((As_ap == 1) | (As_ap == 2)).astype(np.float64)
            beta_vec = np.array([0.0, BETA_T, BETA_A[0], BETA_A[1]])
            ones_ap = np.ones(N_ap)
            Z_b = np.column_stack([ones_ap, T_ap, Bs_ap])
            X_f = np.column_stack([ones_ap, T_ap, D1_ap, D2_ap])
            EZZ_b = (Z_b.T @ Z_b) / N_ap
            EZX_b = (Z_b.T @ X_f) / N_ap
            plim_b = np.linalg.solve(EZZ_b, EZX_b @ beta_vec)
            bin_th = plim_b[1] - BETA_T

        bin_mc = run_mc_binary_collapse(
            M_REPS, N_SAMPLES, C, P_A, ALPHA, BETA_T, BETA_A,
            SIGMA_T, SIGMA_Y, is_diff, SEED)

        bin_mean = bin_mc.mean()
        bin_se = bin_mc.std(ddof=1)
        bin_ci_lo = bin_mean - 1.96 * bin_se / np.sqrt(M_REPS)
        bin_ci_hi = bin_mean + 1.96 * bin_se / np.sqrt(M_REPS)

        k3_ne_bin = abs(k3_bias - bin_th) > 0.001
        if k3_ne_bin:
            pass_criterion_3 = True

        bin_results[name] = dict(bin_th=bin_th, bin_mean=bin_mean, k3_ne_bin=k3_ne_bin)

        elapsed = time.time() - t0
        print(f"{idx:<2} {name:<14} {k3_bias:>10.6f} {bin_th:>10.6f} "
              f"{bin_mean:>10.6f} [{bin_ci_lo:>9.6f}, {bin_ci_hi:>9.6f}] "
              f"{'YES' if k3_ne_bin else 'no':>8}  ({elapsed:.1f}s)")

    # ── Pass/Fail ────────────────────────────────────────────
    print("\n" + "=" * 85)
    print("PASS / FAIL SUMMARY")
    print("=" * 85)

    n_total = len(results_k3)
    n_match = sum(1 for r in results_k3.values() if r["match"])
    c1 = n_match == n_total
    print(f"\n1. Theory vs MC 95% CI match: {n_match}/{n_total}  "
          f"{'PASS' if c1 else 'FAIL'}")

    # Per-structure detail
    for name, r in results_k3.items():
        status = "OK" if r["match"] else "MISMATCH"
        print(f"   {name}: th={r['th_bias']:.6f}, "
              f"CI=[{r['ci'][0]:.6f}, {r['ci'][1]:.6f}] -> {status}")

    away_nondiff = [name for name, r in results_k3.items()
                    if not r["is_diff"] and r["direction"] == "AWAY from null"]
    c2 = len(away_nondiff) >= 1
    print(f"\n2. Non-diff C with away-from-null bias: {len(away_nondiff)}/5  "
          f"{'PASS' if c2 else 'FAIL'}")
    for name in away_nondiff:
        print(f"   {name}: bias={results_k3[name]['th_bias']:.6f}")

    c3 = pass_criterion_3
    diff_names = [n for n, r in bin_results.items() if r["k3_ne_bin"]]
    print(f"\n3. Binary collapse bias != K=3 theory: "
          f"{len(diff_names)}/{n_total}  "
          f"{'PASS' if c3 else 'FAIL'}")
    for name in diff_names:
        k3b = results_k3[name]["th_bias"]
        bb = bin_results[name]["bin_th"]
        print(f"   {name}: K3={k3b:.6f}, Bin={bb:.6f}, Delta={k3b - bb:.6f}")

    overall = c1 and c2 and c3
    print(f"\nOVERALL: {'PASS' if overall else 'FAIL'}")

    # ── Appendix ─────────────────────────────────────────────
    print("\n" + "=" * 85)
    print("APPENDIX: Confusion Matrix Definitions")
    print("=" * 85)
    for name, (C, is_diff, desc) in matrices.items():
        tag = " [DIFFERENTIAL]" if is_diff else " [NON-DIFF]"
        print(f"\n{name}{tag}")
        print(f"  {desc}")
        for row in C:
            print(f"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]")
        if is_diff:
            C_high = _make_C_high(C, factor=2.0)
            print(f"  C_high (T>median):")
            for row in C_high:
                print(f"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]")

    print("\n" + "=" * 85)
    print("TECHNICAL NOTE: Lee & Wood-Doughty (2024) Distinction")
    print("=" * 85)
    print("""
This MVP studies OBSERVED confounding with noisy measurement:
  - A is an observable confounder (e.g., sentiment, topic)
  - Researcher uses LLM to annotate A, producing A* with known error structure
  - A* substitutes for A in regression adjustment for confounding
  - Error structure: P(A*=j|A=i) = C[j,i], C is estimable from validation data

Lee & Wood-Doughty (2024) study UNOBSERVED confounding with proxy:
  - A is never observed (latent confounder)
  - A* is the only available proxy (not a noisy version of something observed)
  - Requires proxy relevance + exclusion restrictions for identification
  - Different bias structure: proxy must satisfy E[T|A,A*] = E[T|A]

Key implication: our bias formula plim = (E[Z'Z])^{-1} E[Z'X] beta assumes
the researcher COULD observe A (and does, for validation), but CHOOSES to use
A* at scale. The confusion matrix C is a design parameter, not a nuisance.
""")


if __name__ == "__main__":
    main()
