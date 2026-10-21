#!/usr/bin/env python3
"""
MVP Validation: Confounding DAG with K=3 Multiclass Annotation Error

Verifies that multiclass (K>=3) annotation error in causal inference
produces qualitatively different bias patterns than binary misclassification.

DAG: A -> T, A -> Y, T -> Y
  A in {0,1,2}: true 3-class confounder
  A*: noisy annotation via 3x3 confusion matrix C
  T: continuous treatment
  Y: continuous outcome

DGP:
  T = alpha_1*1[A=1] + alpha_2*1[A=2] + eta,  eta ~ N(0, sigma_T^2)
  Y = beta_T*T + beta_1*1[A=1] + beta_2*1[A=2] + eps,  eps ~ N(0, sigma_Y^2)
  P(A*=j|A=i) = C[j,i]  (C is column-stochastic)

Key result: plim gamma_hat = (E[Z'Z])^{-1} E[Z'X] beta
  where Z uses A* dummies, X uses true A dummies.

Pass criteria:
  1. Theory vs MC 95% CI match: 5/5
  2. >=1 non-differential C produces away-from-null bias
  3. Binary collapse bias != multiclass theory prediction

Dependencies: numpy, scipy (standard library only)
"""

import numpy as np
from scipy import stats
import time

# ============================================================
# Configuration
# ============================================================
N_SAMPLES = 10_000
M_REPS = 1_000
SEED = 42

P_A = np.array([0.4, 0.35, 0.25])
ALPHA = np.array([1.5, -1.0])        # alpha_1, alpha_2
BETA_T = 2.0                          # true causal effect
BETA_A = np.array([1.0, -0.5])       # beta_1, beta_2
SIGMA_T = 1.0
SIGMA_Y = 1.0


# ============================================================
# Confusion matrix definitions
# ============================================================
def make_confusion_matrices():
    """5 confusion matrix structures. Each column sums to 1."""
    matrices = {}

    # 1. Symmetric high accuracy: diag=0.8, off-diag=0.1
    matrices["1_sym_high"] = (np.array([
        [0.80, 0.10, 0.10],
        [0.10, 0.80, 0.10],
        [0.10, 0.10, 0.80]
    ]), False)

    # 2. Asymmetric: P(A*=1|A=0)=0.30 >> P(A*=0|A=1)=0.05
    matrices["2_asymmetric"] = (np.array([
        [0.65, 0.05, 0.10],
        [0.30, 0.85, 0.10],
        [0.05, 0.10, 0.80]
    ]), False)

    # 3. Structural: classes 1<->2 heavily confused, class 0 clean
    matrices["3_struct_12"] = (np.array([
        [0.90, 0.05, 0.05],
        [0.05, 0.65, 0.30],
        [0.05, 0.30, 0.65]
    ]), False)

    # 4. Near-random: diag~0.4
    matrices["4_near_rand"] = (np.array([
        [0.40, 0.30, 0.30],
        [0.30, 0.40, 0.30],
        [0.30, 0.30, 0.40]
    ]), False)

    # 5. Differential: base C + T-dependent error increase
    matrices["5_differen"] = (np.array([
        [0.80, 0.10, 0.10],
        [0.10, 0.80, 0.10],
        [0.10, 0.10, 0.80]
    ]), True)

    for name, (C, _) in matrices.items():
        assert np.allclose(C.sum(axis=0), 1.0), f"{name}: columns don't sum to 1"
        assert (C >= 0).all(), f"{name}: negative entries"

    return matrices


# ============================================================
# Theoretical bias (exact, for non-differential C)
# ============================================================
def theoretical_bias_exact(C, p_A, alpha, beta_T, beta_A, sigma_T):
    """
    Compute plim of OLS with misclassified A* dummies.

    plim gamma = (E[Z'Z])^{-1} E[Z'X] beta
    Z = (1, T, D*_1, D*_2),  X = (1, T, D_1, D_2)

    Returns: (bias_on_betaT, full_plim_vector)
    """
    p0, p1, p2 = p_A
    a1, a2 = alpha
    b1, b2 = beta_A
    beta = np.array([0.0, beta_T, b1, b2])

    ET = a1 * p1 + a2 * p2
    ET2 = a1**2 * p1 + a2**2 * p2 + sigma_T**2

    q = C @ p_A  # q[j] = P(A*=j)

    # E[T * D*_j] = a1*C[j,1]*p1 + a2*C[j,2]*p2
    ET_Ds = np.array([a1 * C[j, 1] * p1 + a2 * C[j, 2] * p2 for j in range(3)])

    # E[Z'Z]
    EZZ = np.array([
        [1.0,  ET,       q[1],      q[2]],
        [ET,   ET2,      ET_Ds[1],  ET_Ds[2]],
        [q[1], ET_Ds[1], q[1],      0.0],
        [q[2], ET_Ds[2], 0.0,       q[2]]
    ])

    # E[Z'X]:  E[D*_j * D_k] = C[j,k]*p_k
    EZX = np.array([
        [1.0,  ET,       p1,             p2],
        [ET,   ET2,      a1 * p1,        a2 * p2],
        [q[1], ET_Ds[1], C[1, 1] * p1,   C[1, 2] * p2],
        [q[2], ET_Ds[2], C[2, 1] * p1,   C[2, 2] * p2]
    ])

    plim = np.linalg.solve(EZZ, EZX @ beta)
    return plim[1] - beta_T, plim


def theoretical_bias_largesample(C_base, p_A, alpha, beta_T, beta_A,
                                  sigma_T, sigma_Y, N_approx=2_000_000,
                                  seed=999):
    """
    Approximate theoretical bias for differential misclassification
    via large-sample moment estimation.
    """
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
    """Vectorized non-differential A* generation."""
    probs = C[:, A]                          # (3, N)
    cum = np.cumsum(probs, axis=0)           # (3, N)
    u = rng.uniform(size=A.shape[0])
    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))


def _make_C_high(C_base, delta=0.15):
    """Reduce diagonal by delta, redistribute to off-diagonal."""
    C_high = C_base.copy()
    for col in range(3):
        reduction = min(delta, C_high[col, col] - 1.0 / 3.0)
        if reduction <= 0:
            continue
        C_high[col, col] -= reduction
        off = [j for j in range(3) if j != col]
        for j in off:
            C_high[j, col] += reduction / 2.0
    return C_high


def _generate_Astar_differential(A, T, C_base, rng):
    """T > median => higher misclassification rate."""
    N = len(A)
    C_high = _make_C_high(C_base)
    T_med = np.median(T)
    high = T > T_med

    probs_low = C_base[:, A]     # (3, N)
    probs_high = C_high[:, A]    # (3, N)
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
            differential, rng
        )
        D_true = np.column_stack([(A == 1).astype(float), (A == 2).astype(float)])
        D_star = np.column_stack([(A_star == 1).astype(float),
                                   (A_star == 2).astype(float)])
        bias_true[m] = ols_beta_T(T, Y, D_true) - beta_T
        bias_misclass[m] = ols_beta_T(T, Y, D_star) - beta_T

    return bias_true, bias_misclass


# ============================================================
# Unadjusted bias (omitted variable)
# ============================================================
def unadjusted_bias(p_A, alpha, beta_T, beta_A, sigma_T):
    """plim of OLS Y ~ 1 + T (no confounder control)."""
    p0, p1, p2 = p_A
    a1, a2 = alpha
    b1, b2 = beta_A

    ET = a1 * p1 + a2 * p2
    VarT = a1**2 * p1 + a2**2 * p2 + sigma_T**2 - ET**2
    CovD1T = a1 * p1 - p1 * ET    # Cov(1[A=1], T)
    CovD2T = a2 * p2 - p2 * ET    # Cov(1[A=2], T)
    return (b1 * CovD1T + b2 * CovD2T) / VarT


# ============================================================
# Binary collapse analysis
# ============================================================
def collapse_binary_C(C, p_A):
    """
    Derive 2x2 confusion matrix for B=1[A in {1,2}] from 3x3 C.

    C_bin[0,0] = P(B*=0|B=0) = C[0,0]
    C_bin[1,0] = P(B*=1|B=0) = C[1,0] + C[2,0]
    C_bin[0,1] = P(B*=0|B=1) = weighted avg of P(A*=0|A=1), P(A*=0|A=2)
    C_bin[1,1] = 1 - C_bin[0,1]
    """
    p1, p2 = p_A[1], p_A[2]
    pB1 = p1 + p2

    c_bin_00 = C[0, 0]
    c_bin_10 = C[1, 0] + C[2, 0]
    c_bin_01 = (C[0, 1] * p1 + C[0, 2] * p2) / pB1
    c_bin_11 = 1.0 - c_bin_01

    C_bin = np.array([[c_bin_00, c_bin_01],
                      [c_bin_10, c_bin_11]])
    return C_bin


def theoretical_bias_binary(C_bin, p_A, alpha, beta_T, beta_A, sigma_T):
    """
    Theoretical bias when collapsing to binary B=1[A in {1,2}].
    True model still has separate D1, D2 effects.

    Z_bin = (1, T, B*),  X_full = (1, T, D1, D2)
    plim = (E[Z_bin'Z_bin])^{-1} E[Z_bin'X_full] beta
    """
    p0, p1, p2 = p_A
    a1, a2 = alpha
    b1, b2 = beta_A
    beta = np.array([0.0, beta_T, b1, b2])
    pB1 = p1 + p2

    ET = a1 * p1 + a2 * p2
    ET2 = a1**2 * p1 + a2**2 * p2 + sigma_T**2

    # P(B*=1) via confusion
    q_Bs1 = C_bin[1, 0] * p0 + C_bin[1, 1] * pB1

    # E[T * B*] = E[T * 1[A* in {1,2}]]
    #   = sum_j in {1,2} E[T * D*_j]
    #   = sum_j in {1,2} (a1*C[j,1]*p1 + a2*C[j,2]*p2)
    # But we only have C_bin, so reconstruct:
    # E[T * B*] = E[T * E[B*|A,T]]
    # For non-diff: E[B*|A=0] = C_bin[1,0], E[B*|A=1,2] = C_bin[1,1]
    # E[T*B*] = C_bin[1,0]*E[T*1[A=0]] + C_bin[1,1]*E[T*1[A in {1,2}]]
    # E[T*1[A=0]] = E[T*D0] = 0*p0 = 0  (since T = a1*D1 + a2*D2 + eta, D0 uncorrelated w/ eta)
    # Wait: E[T*D0] = E[(a1*D1 + a2*D2 + eta)*D0] = 0 (D0*D1=0, D0*D2=0, E[eta*D0]=0)
    # E[T*B] = E[T*(D1+D2)] = a1*p1 + a2*p2
    ET_Bs = C_bin[1, 0] * 0.0 + C_bin[1, 1] * (a1 * p1 + a2 * p2)

    # E[B* * D_k] for k=1,2
    # E[B* * D1] = P(B*=1, A=1) = P(A* in {1,2} | A=1)*p1
    #   = (1 - C[0,1])*p1 = (1 - P(A*=0|A=1))*p1
    # Using C_bin: P(B*=1|B=1) = C_bin[1,1], but this is averaged over A=1,2.
    # More precisely: P(B*=1|A=1) = 1 - C[0,1] (from original 3x3 C)
    # We don't have the original C here, so let's pass it separately.
    # Actually, let's just compute this from the original C.
    # This function should receive the original C too, or compute directly.
    # Let me restructure...

    # For cleanliness, compute binary plim from original C directly.
    raise NotImplementedError("Use theoretical_bias_binary_from_C3 instead")


def theoretical_bias_binary_from_C3(C, p_A, alpha, beta_T, beta_A, sigma_T):
    """
    Theoretical bias when researcher collapses A to B=1[A in {1,2}]
    and uses B* = 1[A* in {1,2}].

    Z = (1, T, B*),  X = (1, T, D1, D2)
    plim = (E[Z'Z])^{-1} E[Z'X] beta
    """
    p0, p1, p2 = p_A
    a1, a2 = alpha
    b1, b2 = beta_A
    beta = np.array([0.0, beta_T, b1, b2])

    ET = a1 * p1 + a2 * p2
    ET2 = a1**2 * p1 + a2**2 * p2 + sigma_T**2

    # B* = 1[A* in {1,2}] = D*_1 + D*_2
    # P(B*=1) = sum_{j=1,2} q_j where q_j = sum_i C[j,i]*p_i
    q = C @ p_A
    q_Bs = q[1] + q[2]  # = 1 - q[0]

    # E[T * B*] = E[T*(D*1 + D*2)] = sum_{j=1,2} E[T*D*_j]
    ET_Ds = np.array([a1 * C[j, 1] * p1 + a2 * C[j, 2] * p2 for j in range(3)])
    ET_Bs = ET_Ds[1] + ET_Ds[2]

    # E[Z'Z]: Z = (1, T, B*)
    EZZ = np.array([
        [1.0,    ET,    q_Bs],
        [ET,     ET2,   ET_Bs],
        [q_Bs,   ET_Bs, q_Bs]    # B*^2 = B* (indicator)
    ])

    # E[Z'X]: X = (1, T, D1, D2)
    # E[B* * D_k] = P(B*=1, A=k) = P(A* in {1,2} | A=k) * p_k
    #             = (C[1,k] + C[2,k]) * p_k  =  (1 - C[0,k]) * p_k
    EB_D1 = (1.0 - C[0, 1]) * p1
    EB_D2 = (1.0 - C[0, 2]) * p2

    EZX = np.array([
        [1.0,    ET,     p1,       p2],
        [ET,     ET2,    a1 * p1,  a2 * p2],
        [q_Bs,   ET_Bs,  EB_D1,    EB_D2]
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
            differential, rng
        )
        B_star = ((A_star == 1) | (A_star == 2)).astype(float).reshape(-1, 1)
        bias_bin[m] = ols_beta_T(T, Y, B_star) - beta_T

    return bias_bin


# ============================================================
# Main
# ============================================================
def main():
    print("=" * 80)
    print("MVP Validation: Confounding DAG — K=3 Multiclass Annotation Error Bias")
    print("=" * 80)
    print(f"\nDGP: P(A)={list(P_A)}, alpha={list(ALPHA)}, "
          f"beta_T={BETA_T}, beta_A={list(BETA_A)}")
    print(f"     sigma_T={SIGMA_T}, sigma_Y={SIGMA_Y}")
    print(f"MC:  N={N_SAMPLES:,}, M={M_REPS:,}, seed={SEED}")

    # Unadjusted bias (omitted variable reference)
    ovb = unadjusted_bias(P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)
    print(f"\nUnadjusted OVB (no A control): {ovb:.6f}")
    print(f"  => Unadjusted plim(beta_T_hat) = {BETA_T + ovb:.6f}")
    print(f"  => Direction: {'toward null' if ovb * BETA_T < 0 else 'away from null'}")

    matrices = make_confusion_matrices()

    # ── Step 1-3: K=3 analysis ──────────────────────────────
    print("\n" + "=" * 80)
    print("PART A: K=3 Multiclass — Theory vs Monte Carlo")
    print("=" * 80)

    results_k3 = {}
    header = f"{'Config':<14} {'Theory':>10} {'MC Mean':>10} {'MC 95% CI':>22} {'Match?':>7} {'Dir':>14}"
    print(f"\n{header}")
    print("-" * len(header))

    for name, (C, is_diff) in matrices.items():
        t0 = time.time()

        # Theoretical bias
        if is_diff:
            th_bias, _ = theoretical_bias_largesample(
                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T, SIGMA_Y)
        else:
            th_bias, _ = theoretical_bias_exact(
                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)

        # Monte Carlo
        _, mc_bias = run_mc(M_REPS, N_SAMPLES, C, P_A, ALPHA, BETA_T,
                            BETA_A, SIGMA_T, SIGMA_Y, is_diff, SEED)

        mc_mean = mc_bias.mean()
        mc_se = mc_bias.std(ddof=1)
        ci_lo = mc_mean - 1.96 * mc_se / np.sqrt(M_REPS)
        ci_hi = mc_mean + 1.96 * mc_se / np.sqrt(M_REPS)
        match = ci_lo <= th_bias <= ci_hi

        # Direction relative to null
        if abs(th_bias) < 1e-6:
            direction = "~zero"
        elif th_bias * BETA_T > 0:
            direction = "AWAY from null"
        else:
            direction = "toward null"

        elapsed = time.time() - t0
        results_k3[name] = {
            "th_bias": th_bias, "mc_mean": mc_mean,
            "ci": (ci_lo, ci_hi), "match": match,
            "direction": direction, "mc_bias_arr": mc_bias,
            "is_diff": is_diff
        }

        print(f"{name:<14} {th_bias:>10.6f} {mc_mean:>10.6f} "
              f"[{ci_lo:>9.6f}, {ci_hi:>9.6f}] {'YES' if match else '**NO**':>7} "
              f"{direction:>14}  ({elapsed:.1f}s)")

    # ── Step 4: Binary collapse ──────────────────────────────
    print("\n" + "=" * 80)
    print("PART B: Binary Collapse — B=1[A in {1,2}]")
    print("=" * 80)

    header_b = (f"{'Config':<14} {'K3 Theory':>10} {'Bin Theory':>10} "
                f"{'Bin MC Mean':>11} {'Bin MC 95% CI':>22} {'K3!=Bin?':>8}")
    print(f"\n{header_b}")
    print("-" * len(header_b))

    pass_criterion_3 = False

    for name, (C, is_diff) in matrices.items():
        t0 = time.time()
        k3_bias = results_k3[name]["th_bias"]

        # Binary theoretical (from original 3x3 C, non-differential only)
        if not is_diff:
            bin_th = theoretical_bias_binary_from_C3(
                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)
        else:
            # For differential, use large-sample approx for binary too
            rng_approx = np.random.default_rng(888)
            N_ap = 2_000_000
            A_ap = rng_approx.choice(3, size=N_ap, p=P_A)
            D1_ap = (A_ap == 1).astype(np.float64)
            D2_ap = (A_ap == 2).astype(np.float64)
            T_ap = ALPHA[0] * D1_ap + ALPHA[1] * D2_ap + rng_approx.normal(0, SIGMA_T, N_ap)
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

        # Binary MC
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

        elapsed = time.time() - t0
        print(f"{name:<14} {k3_bias:>10.6f} {bin_th:>10.6f} "
              f"{bin_mean:>11.6f} [{bin_ci_lo:>9.6f}, {bin_ci_hi:>9.6f}] "
              f"{'YES' if k3_ne_bin else 'no':>8}  ({elapsed:.1f}s)")

    # ── Pass/Fail summary ────────────────────────────────────
    print("\n" + "=" * 80)
    print("PASS / FAIL SUMMARY")
    print("=" * 80)

    # Criterion 1: all 5 theory-MC matches
    n_match = sum(1 for r in results_k3.values() if r["match"])
    c1 = n_match == 5
    print(f"\n1. Theory vs MC 95% CI match: {n_match}/5  "
          f"{'PASS' if c1 else 'FAIL'}")

    # Criterion 2: >=1 non-differential C with away-from-null bias
    away_nondiff = [name for name, r in results_k3.items()
                    if not r["is_diff"] and r["direction"] == "AWAY from null"]
    c2 = len(away_nondiff) >= 1
    print(f"2. Non-diff C with away-from-null bias: {len(away_nondiff)} "
          f"({', '.join(away_nondiff) if away_nondiff else 'none'})  "
          f"{'PASS' if c2 else 'FAIL'}")

    # Criterion 3: binary collapse != multiclass
    print(f"3. Binary collapse bias != K=3 theory: "
          f"{'PASS' if pass_criterion_3 else 'FAIL'}")

    print(f"\nOVERALL: {'PASS' if (c1 and c2 and pass_criterion_3) else 'FAIL'}")

    # ── Detailed confusion matrices ──────────────────────────
    print("\n" + "=" * 80)
    print("APPENDIX: Confusion Matrices")
    print("=" * 80)
    for name, (C, is_diff) in matrices.items():
        tag = " [DIFFERENTIAL]" if is_diff else ""
        print(f"\n{name}{tag}:")
        for row in C:
            print(f"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]")


if __name__ == "__main__":
    main()
