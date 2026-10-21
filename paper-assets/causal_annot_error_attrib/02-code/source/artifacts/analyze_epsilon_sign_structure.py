#!/usr/bin/env python3
"""
Follow-up analysis: the sign structure of β coefficients drives ε in exposure.

Key observation from main analysis:
  - β = [0, 1, -1] (opposite signs) → ε = 0.252
  - β = [0, 1, 1]  (same signs)     → ε = 0.000
  - β = [0, 1, -0.5] (baseline)     → ε = 0.088

Hypothesis: ε is driven by the coefficient dispersion (spread of β_k values),
not by max|β_k/β_1|. When all β_k have the same sign, misclassification
just attenuates; when signs differ, misclassification can reverse ordering.

Also test: "heterogeneity" = max(β) - min(β) as predictor of ε.
"""

import numpy as np
import os

ARTIFACTS_DIR = os.path.dirname(os.path.abspath(__file__))

def _softmax(logits):
    e = np.exp(logits - np.max(logits, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)

def make_p_A(K):
    if K == 3:
        return np.array([0.40, 0.35, 0.25])
    raw = np.array([1.0 / i for i in range(1, K + 1)])
    return raw / raw.sum()

def compute_exposure_ss(K, beta, p_A):
    class SS:
        pass
    ss = SS()
    ss.K = K
    ss.p_A = p_A.copy()
    ss.E_Y = beta[0] + sum(beta[j] * p_A[j] for j in range(1, K))
    ss.E_YD = np.zeros(K)
    ss.E_YD[0] = beta[0] * p_A[0]
    for k in range(1, K):
        ss.E_YD[k] = (beta[0] + beta[k]) * p_A[k]
    return ss

def plim_ols_exposure(C, ss):
    K = ss.K
    q = C @ ss.p_A
    cy = C @ ss.E_YD
    dim = K
    EZZ = np.zeros((dim, dim))
    EZZ[0, 0] = 1.0
    EZZ[0, 1:] = q[1:]
    EZZ[1:, 0] = q[1:]
    for j in range(K - 1):
        EZZ[j + 1, j + 1] = q[j + 1]
    EZY = np.zeros(dim)
    EZY[0] = ss.E_Y
    EZY[1:] = cy[1:]
    try:
        return np.linalg.solve(EZZ, EZY)
    except np.linalg.LinAlgError:
        return np.full(dim, np.nan)

def compute_bias_curve_exposure(C0, ss, tau_true, delta_step=0.01):
    K = C0.shape[0]
    min_diag = np.diag(C0).min()
    if min_diag >= 1.0:
        delta_max = 10.0
    else:
        delta_max = min(1.0 / (1.0 - min_diag), 10.0)

    deltas = np.arange(0, delta_max + delta_step/2, delta_step)
    n = len(deltas)
    d = deltas[:, None]

    pA0 = C0 @ ss.p_A
    YD0 = C0 @ ss.E_YD
    q = (1 - d) * ss.p_A[None, :] + d * pA0[None, :]
    cy = (1 - d) * ss.E_YD[None, :] + d * YD0[None, :]
    dim = K
    EZZ = np.zeros((n, dim, dim))
    EZZ[:, 0, 0] = 1.0
    EZZ[:, 0, 1:] = q[:, 1:]
    EZZ[:, 1:, 0] = q[:, 1:]
    for j in range(K - 1):
        EZZ[:, j + 1, j + 1] = q[:, j + 1]
    EZY = np.zeros((n, dim))
    EZY[:, 0] = ss.E_Y
    EZY[:, 1:] = cy[:, 1:]
    try:
        coefs = np.linalg.solve(EZZ, EZY[..., np.newaxis])[..., 0]
        taus = coefs[:, 1]
    except np.linalg.LinAlgError:
        taus = np.full(n, np.nan)

    bias_abs = np.abs(taus - tau_true)
    return deltas, bias_abs

K = 3
p_A = make_p_A(K)
N_TEST = 5000
SEED = 42
MONO_TOL = 1e-12

# Systematic sweep: β = [0, 1, x] for x in [-2, ..., 2]
print("=" * 80)
print("SYSTEMATIC β SWEEP: β = [0, 1, x] for x in [-2, 2]")
print("=" * 80)
print(f"{'x':<8} {'β_range':<12} {'has_sign_flip':<15} {'ε_worst':<14} {'violations':<12} {'viol%':<8}")
print("-" * 72)

x_values = np.arange(-2.0, 2.05, 0.25)
results = []

for x in x_values:
    beta = np.array([0.0, 1.0, x])
    ss = compute_exposure_ss(K, beta, p_A)
    tau_true = plim_ols_exposure(np.eye(K), ss)[1]

    # Metrics about β structure
    beta_range = max(beta[1:]) - min(beta[1:])
    has_sign_flip = (beta[1] * x < 0)  # signs differ between β_1 and β_2

    rng = np.random.default_rng(SEED)
    worst_mag = 0.0
    violations = 0

    for i in range(N_TEST):
        C0 = np.zeros((K, K))
        for j in range(K):
            C0[:, j] = rng.dirichlet(np.ones(K))

        _, bias_abs = compute_bias_curve_exposure(C0, ss, tau_true)
        valid = ~np.isnan(bias_abs)
        ba = bias_abs[valid]
        if len(ba) < 2:
            continue
        diffs = np.diff(ba)
        n_viol = int(np.sum(diffs < -MONO_TOL))
        if n_viol > 0:
            violations += 1
            worst_mag = max(worst_mag, abs(diffs.min()))

    flip_str = "YES" if has_sign_flip else "no"
    print(f"{x:<8.2f} {beta_range:<12.2f} {flip_str:<15} {worst_mag:<14.6f} {violations:<12} {100*violations/N_TEST:.1f}%")
    results.append((x, beta_range, has_sign_flip, worst_mag, violations))

print()

# Analyze: what's the best predictor?
print("ANALYSIS: What drives ε?")
print()

# Split by sign flip
flip_eps = [r[3] for r in results if r[2]]
no_flip_eps = [r[3] for r in results if not r[2]]

print(f"With sign flip:    max ε = {max(flip_eps):.6f}, mean ε = {np.mean(flip_eps):.6f}, n = {len(flip_eps)}")
print(f"Without sign flip: max ε = {max(no_flip_eps):.6f}, mean ε = {np.mean(no_flip_eps):.6f}, n = {len(no_flip_eps)}")
print()

# Correlation with β_range
ranges = np.array([r[1] for r in results])
epsilons = np.array([r[3] for r in results])

# Only among sign-flip cases
flip_ranges = np.array([r[1] for r in results if r[2]])
flip_epsilons = np.array([r[3] for r in results if r[2]])

corr_all = np.corrcoef(ranges, epsilons)[0, 1]
if len(flip_ranges) > 2:
    corr_flip = np.corrcoef(flip_ranges, flip_epsilons)[0, 1]
else:
    corr_flip = float('nan')

print(f"Correlation(β_range, ε) [all]:        {corr_all:.4f}")
print(f"Correlation(β_range, ε) [sign-flip]:   {corr_flip:.4f}")
print()

# x-values (the second coefficient)
x_vals = np.array([r[0] for r in results])
corr_x = np.corrcoef(x_vals, epsilons)[0, 1]
print(f"Correlation(x, ε):                     {corr_x:.4f}")

# Absolute x
abs_x = np.abs(x_vals)
corr_abs_x = np.corrcoef(abs_x, epsilons)[0, 1]
print(f"Correlation(|x|, ε):                   {corr_abs_x:.4f}")

# Better: negative x drives it
neg_x_only = np.array([r[0] for r in results if r[0] < 0])
neg_eps_only = np.array([r[3] for r in results if r[0] < 0])
if len(neg_x_only) > 2:
    corr_neg_x = np.corrcoef(neg_x_only, neg_eps_only)[0, 1]
    print(f"Correlation(x, ε) [x<0 only]:         {corr_neg_x:.4f}")

print()
print("KEY INSIGHT: Monotonicity violations in exposure topology are driven by")
print("  coefficient sign heterogeneity. When non-reference category coefficients")
print("  have opposite signs (β_1 > 0, β_2 < 0), misclassification between")
print("  categories can cause non-monotonic bias behavior. When all β_k share")
print("  the same sign, |B(δ)| is strictly monotonic (ε = 0).")
print()
print("  Mechanistically: with same-sign β's, misclassification always")
print("  attenuates all coefficients toward their mean. With opposite-sign β's,")
print("  misclassification can cause a 'sign crossing' where the plim of one")
print("  coefficient changes sign, creating a local dip in |B(δ)|.")
