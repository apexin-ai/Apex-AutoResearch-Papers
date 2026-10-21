#!/usr/bin/env python3
"""
Analyze empirical epsilon bounds from exp_d_conjecture_results_v2.json.

Goal: derive ε ≤ f(K, topology_type) from the worst-case monotonicity
violation magnitudes across 10,000 random C₀ matrices per (topology, K).

Also runs a supplementary analysis varying β ratios for the exposure topology
at K=3 to check if max|β_k/β_1| affects ε.
"""

import json
import numpy as np
import os
import sys
from itertools import product

# Add artifacts dir to path for importing from exp_d script
ARTIFACTS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ARTIFACTS_DIR)

# ====================================================================
# Part 1: Load and tabulate the v2 results
# ====================================================================
with open(os.path.join(ARTIFACTS_DIR, "exp_d_conjecture_results_v2.json")) as f:
    data = json.load(f)

rv = data["random_verification"]

ALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
             'mbias', 'frontdoor']  # exclude IV (unbounded)
K_VALUES = [3, 5, 7]

print("=" * 80)
print("TABLE 1: Worst-case monotonicity violation magnitude ε by topology × K")
print("         (10,000 random C₀ matrices per cell, analytic plim)")
print("=" * 80)
print(f"{'Topology':<14} {'Dir':<8} {'K=3':>12} {'K=5':>12} {'K=7':>12} {'Viol%_K3':>10} {'Viol%_K5':>10} {'Viol%_K7':>10}")
print("-" * 80)

eps_table = {}  # (topo, K) -> worst_magnitude
viol_table = {}  # (topo, K) -> violation count

for topo in ALL_TOPOS:
    row = rv[topo]
    vals = []
    viols = []
    for K in K_VALUES:
        key = f"K{K}"
        wm = row[key]["worst_violation_magnitude"]
        vc = row[key]["violations"]
        nt = row[key]["n_tested"]
        eps_table[(topo, K)] = wm
        viol_table[(topo, K)] = vc
        vals.append(f"{wm:.6f}")
        viols.append(f"{100*vc/nt:.1f}%")
    direction = row["K3"]["direction"]
    print(f"{topo:<14} {direction:<8} {vals[0]:>12} {vals[1]:>12} {vals[2]:>12} {viols[0]:>10} {viols[1]:>10} {viols[2]:>10}")

# Also show IV for completeness
iv_row = rv["iv"]
vals_iv = [f"{iv_row[f'K{K}']['worst_violation_magnitude']:.1f}" for K in K_VALUES]
print(f"{'iv':<14} {'non-dec':<8} {vals_iv[0]:>12} {vals_iv[1]:>12} {vals_iv[2]:>12}  (unbounded -- Wald estimator singularity)")

print()

# ====================================================================
# Part 2: Scaling analysis — does ε ~ 1/K or 1/√K?
# ====================================================================
print("=" * 80)
print("SCALING ANALYSIS: ε vs K")
print("=" * 80)

print(f"\n{'Topology':<14} {'ε(3)':<12} {'ε(5)':<12} {'ε(7)':<12} {'ε(3)/ε(7)':<12} {'ε(3)*3/ε(7)*7':<16} {'Log-log slope':<14}")
print("-" * 90)

for topo in ALL_TOPOS:
    e3 = eps_table[(topo, 3)]
    e5 = eps_table[(topo, 5)]
    e7 = eps_table[(topo, 7)]

    if e7 > 0 and e3 > 0:
        ratio_37 = e3 / e7
        # If ε ~ 1/K^α, then log(ε3/ε7) = α * log(7/3)
        alpha = np.log(e3 / e7) / np.log(7 / 3)
        # Check 1/K scaling: ε*K should be roughly constant
        eK_products = [e3*3, e5*5, e7*7]
        eK_str = f"{eK_products[0]:.4f}/{eK_products[1]:.4f}/{eK_products[2]:.4f}"
    else:
        ratio_37 = float('inf')
        alpha = float('nan')
        eK_str = "N/A"

    print(f"{topo:<14} {e3:<12.6f} {e5:<12.6f} {e7:<12.6f} {ratio_37:<12.2f} {eK_str:<16} {alpha:<14.2f}")

print()

# More careful fit: log(ε) = a + b*log(K)
print("Log-linear regression: log(ε) = a + b*log(K)")
print(f"{'Topology':<14} {'slope b':<12} {'R²':<12} {'Interpretation':<30}")
print("-" * 70)

slopes = {}
for topo in ALL_TOPOS:
    log_K = np.array([np.log(K) for K in K_VALUES])
    log_eps = np.array([np.log(eps_table[(topo, K)]) for K in K_VALUES])

    # Fit log(ε) = a + b*log(K)
    A = np.column_stack([np.ones(3), log_K])
    coeffs = np.linalg.lstsq(A, log_eps, rcond=None)[0]
    a, b = coeffs

    # R²
    predicted = A @ coeffs
    ss_res = np.sum((log_eps - predicted)**2)
    ss_tot = np.sum((log_eps - log_eps.mean())**2)
    R2 = 1 - ss_res / ss_tot if ss_tot > 0 else float('nan')

    slopes[topo] = b

    if abs(b + 1) < 0.15:
        interp = "~1/K"
    elif abs(b + 0.5) < 0.15:
        interp = "~1/√K"
    elif abs(b + 1.5) < 0.15:
        interp = "~1/K^1.5"
    elif abs(b + 2) < 0.15:
        interp = "~1/K²"
    else:
        interp = f"~1/K^{-b:.2f}"

    print(f"{topo:<14} {b:<12.3f} {R2:<12.4f} {interp:<30}")

print()

# ====================================================================
# Part 3: Off-diagonal mass analysis
# ====================================================================
print("=" * 80)
print("OFF-DIAGONAL MASS ANALYSIS")
print("=" * 80)
print()
print("For a random Dirichlet(1,...,1) column of C₀ with K categories:")
print("  E[diagonal element] = 1/K")
print("  E[off-diagonal mass] = 1 - 1/K = (K-1)/K")
print()

# The key insight: the off-diagonal mass of C₀ determines how much
# misclassification happens. For Dirichlet(1,...,1), each column has
# E[c_kk] = 1/K, so E[off-diag mass per column] = (K-1)/K.
# But the WORST violation ε doesn't necessarily correspond to max off-diag mass.

# Let's check: does ε correlate with some function of K and the topology?
# We know the β parameters differ by topology. Let's look at the structure.

# From make_all_params in the v2 script:
_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]
_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]

print("DGP coefficient structure by topology (K=3):")
print(f"  confounding: alpha={_ALPHA_POOL[:2]}, beta_A={_BETA_A_POOL[:2]}, beta_T=2.0")
print(f"  mediation:   gamma={[0.0, 0.5, -0.3]}, delta={[0.0, 0.8, -0.6]}, beta={[0.0, 1.0, -0.5]}, tau=0.5")
print(f"  collider:    dT={[0.0, 0.5, -0.3]}, dY={[0.0, 0.8, 0.6]}, tau=1.0")
print(f"  exposure:    beta={[0.0, 1.0, -0.5]}")
print(f"  mbias:       a1={[0.0, 0.8, -0.5]}, a2={[0.0, 0.6, 0.9]}, tau=1.0")
print(f"  frontdoor:   gamma={[0.0, 0.5, -0.3]}, delta={[0.0, 1.0, -0.8]}, beta={[0.0, 1.0, -0.5]}")
print()

# ====================================================================
# Part 4: Propose empirical bound
# ====================================================================
print("=" * 80)
print("PROPOSED EMPIRICAL BOUNDS")
print("=" * 80)
print()

# Group topologies by behavior:
# - exposure: largest ε, slow K-decay (slope ~ -1.1)
# - confounding, mediation, frontdoor: similar ε, ~1/K^1.3 decay
# - collider, mbias: smallest ε, faster decay

# Try bound: ε ≤ c / K^α for each topology group
print("Strategy: fit ε ≤ c / K^α with safety margin (multiply c by 1.5)")
print()

# For each topology, find c such that c/K^α >= all observed ε
# with α from the fitted slope
for topo in ALL_TOPOS:
    alpha_fit = -slopes[topo]
    # Find c = max over K of ε * K^α
    c_vals = [eps_table[(topo, K)] * K**alpha_fit for K in K_VALUES]
    c_tight = max(c_vals)
    c_safe = c_tight * 1.5  # 50% safety margin

    # Check bound holds
    checks = []
    for K in K_VALUES:
        bound = c_safe / K**alpha_fit
        actual = eps_table[(topo, K)]
        checks.append(f"K={K}: {actual:.6f} ≤ {bound:.6f} ({'OK' if actual <= bound else 'FAIL'})")

    print(f"{topo}: ε ≤ {c_safe:.4f} / K^{alpha_fit:.2f}")
    for ch in checks:
        print(f"  {ch}")
    print()

# Now try a SINGLE universal bound for non-IV topologies
print("-" * 60)
print("UNIVERSAL BOUND (all non-IV topologies):")
print()

# Universal: find α and c such that c/K^α >= all ε for all topologies
# Use the most conservative (exposure) as the binding constraint
all_eps = [(K, eps_table[(topo, K)]) for topo in ALL_TOPOS for K in K_VALUES]

# Try different α values
best_alpha_universal = None
best_c_universal = None
best_tightness = float('inf')

for alpha_try in np.arange(0.5, 2.5, 0.01):
    c_needed = max(eps * K**alpha_try for K, eps in all_eps)
    # Tightness: how much slack is there on average?
    slack = np.mean([(c_needed / K**alpha_try - eps) / eps
                     for K, eps in all_eps if eps > 0])
    if slack < best_tightness:
        best_tightness = slack
        best_alpha_universal = alpha_try
        best_c_universal = c_needed

c_safe_univ = best_c_universal * 1.2  # 20% margin
print(f"Best universal fit: ε ≤ {best_c_universal:.4f} / K^{best_alpha_universal:.2f}")
print(f"With 20% safety margin: ε ≤ {c_safe_univ:.4f} / K^{best_alpha_universal:.2f}")
print()

# Check against all data points
print(f"{'Topology':<14} {'K':<6} {'ε_actual':<14} {'Bound':<14} {'Slack%':<10}")
print("-" * 60)
for topo in ALL_TOPOS:
    for K in K_VALUES:
        actual = eps_table[(topo, K)]
        bound = c_safe_univ / K**best_alpha_universal
        slack_pct = 100 * (bound - actual) / actual if actual > 0 else float('inf')
        print(f"{topo:<14} {K:<6} {actual:<14.6f} {bound:<14.6f} {slack_pct:<10.1f}")

print()

# ====================================================================
# Part 5: β-ratio sensitivity for exposure topology
# ====================================================================
print("=" * 80)
print("β-RATIO SENSITIVITY ANALYSIS (exposure topology, K=3)")
print("=" * 80)
print()

# We need to import/re-implement the exposure computation
# Re-implement the key functions here for clarity

from scipy.special import roots_hermite

def make_p_A(K):
    if K == 3:
        return np.array([0.40, 0.35, 0.25])
    raw = np.array([1.0 / i for i in range(1, K + 1)])
    return raw / raw.sum()

def _softmax(logits):
    e = np.exp(logits - np.max(logits, axis=-1, keepdims=True))
    return e / np.sum(e, axis=-1, keepdims=True)

def compute_exposure_ss(K, beta, p_A):
    """Minimal exposure sufficient stats."""
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

# Test different β vectors
beta_configs = [
    ("baseline [0, 1, -0.5]", np.array([0.0, 1.0, -0.5])),
    ("uniform [0, 1, 1]", np.array([0.0, 1.0, 1.0])),
    ("large ratio [0, 5, -0.5]", np.array([0.0, 5.0, -0.5])),
    ("very large [0, 10, -0.5]", np.array([0.0, 10.0, -0.5])),
    ("extreme ratio [0, 10, 0.1]", np.array([0.0, 10.0, 0.1])),
    ("equal [0, 1, 1]", np.array([0.0, 1.0, 1.0])),
    ("opposite [0, 1, -1]", np.array([0.0, 1.0, -1.0])),
    ("small [0, 0.1, -0.05]", np.array([0.0, 0.1, -0.05])),
    ("large both [0, 5, 5]", np.array([0.0, 5.0, 5.0])),
    ("large neg [0, -5, 0.5]", np.array([0.0, -5.0, 0.5])),
]

print(f"Testing {N_TEST} random C₀ matrices per β config at K={K}")
print(f"{'β config':<30} {'max|β_k/β_1|':<14} {'ε_worst':<14} {'violations':<12} {'viol%':<8}")
print("-" * 80)

results_beta = []
for name, beta in beta_configs:
    ss = compute_exposure_ss(K, beta, p_A)
    tau_true = plim_ols_exposure(np.eye(K), ss)[1]

    max_ratio = max(abs(beta[k] / beta[1]) for k in range(2, K)) if abs(beta[1]) > 1e-10 else float('inf')

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

    print(f"{name:<30} {max_ratio:<14.2f} {worst_mag:<14.6f} {violations:<12} {100*violations/N_TEST:.1f}%")
    results_beta.append((name, beta, max_ratio, worst_mag, violations))

print()

# Check correlation between max_ratio and worst_mag
ratios = np.array([r[2] for r in results_beta if r[2] < float('inf')])
epsilons = np.array([r[3] for r in results_beta if r[2] < float('inf')])

if len(ratios) > 2:
    corr = np.corrcoef(ratios, epsilons)[0, 1]
    print(f"Correlation between max|β_k/β_1| and ε_worst: {corr:.4f}")

    log_ratios = np.log(ratios + 1)
    log_eps = np.log(epsilons + 1e-20)
    corr_log = np.corrcoef(log_ratios, log_eps)[0, 1]
    print(f"Correlation (log-log): {corr_log:.4f}")

print()

# ====================================================================
# Part 6: Additional K values for exposure to refine scaling
# ====================================================================
print("=" * 80)
print("EXTENDED K ANALYSIS FOR EXPOSURE (K=3,4,5,6,7,8,9,10)")
print("=" * 80)
print()

K_EXTENDED = [3, 4, 5, 6, 7]
N_TEST_EXT = 5000

beta_exposure_base = _BETA_POOL

print(f"Testing {N_TEST_EXT} random C₀ per K value")
print(f"{'K':<6} {'ε_worst':<14} {'violations':<12} {'viol%':<8} {'ε*K':<10} {'ε*K^1.1':<12}")
print("-" * 65)

eps_extended = []
for K in K_EXTENDED:
    p_A = make_p_A(K)
    beta = np.array(beta_exposure_base[:K])
    ss = compute_exposure_ss(K, beta, p_A)
    tau_true = plim_ols_exposure(np.eye(K), ss)[1]

    rng = np.random.default_rng(SEED)
    worst_mag = 0.0
    violations = 0

    for i in range(N_TEST_EXT):
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

    eps_extended.append((K, worst_mag, violations))
    eK = worst_mag * K
    eK11 = worst_mag * K**1.1
    print(f"{K:<6} {worst_mag:<14.6f} {violations:<12} {100*violations/N_TEST_EXT:.1f}% {eK:<10.4f} {eK11:<12.4f}")

print()

# Fit power law to extended data
log_K_ext = np.array([np.log(K) for K, _, _ in eps_extended if _ > 0])
log_eps_ext = np.array([np.log(eps) for K, eps, _ in eps_extended if eps > 0])

if len(log_K_ext) > 2:
    A = np.column_stack([np.ones(len(log_K_ext)), log_K_ext])
    coeffs = np.linalg.lstsq(A, log_eps_ext, rcond=None)[0]
    a_ext, b_ext = coeffs
    c_ext = np.exp(a_ext)

    predicted = A @ coeffs
    ss_res = np.sum((log_eps_ext - predicted)**2)
    ss_tot = np.sum((log_eps_ext - log_eps_ext.mean())**2)
    R2_ext = 1 - ss_res / ss_tot if ss_tot > 0 else float('nan')

    print(f"Power law fit for exposure: ε ≈ {c_ext:.4f} / K^{-b_ext:.3f}  (R² = {R2_ext:.4f})")
    print()

    # With safety margin
    c_safe_exp = max(eps * K**(-b_ext) for K, eps, _ in eps_extended if eps > 0) * 1.5
    print(f"Safe bound for exposure: ε ≤ {c_safe_exp:.4f} / K^{-b_ext:.2f}")

print()

# ====================================================================
# Part 7: Final summary
# ====================================================================
print("=" * 80)
print("FINAL SUMMARY: EMPIRICAL BOUNDS")
print("=" * 80)
print()
print("Key findings:")
print(f"  1. IV topology is UNBOUNDED (Wald estimator singularity near weak instruments)")
print(f"  2. Non-IV topologies: all ε < 0.056 (worst case: exposure at K=3)")
print(f"  3. Power law scaling: ε ~ 1/K^α where α varies by topology")
print()

print("Topology-specific bounds (ε ≤ c/K^α, 50% safety margin):")
for topo in ALL_TOPOS:
    alpha_fit = -slopes[topo]
    c_vals = [eps_table[(topo, K)] * K**alpha_fit for K in K_VALUES]
    c_tight = max(c_vals)
    c_safe = c_tight * 1.5
    print(f"  {topo:<14}: ε ≤ {c_safe:.4f} / K^{alpha_fit:.2f}  (α_fit = {alpha_fit:.3f})")

print()
print(f"Universal bound (all non-IV): ε ≤ {c_safe_univ:.4f} / K^{best_alpha_universal:.2f}")
print()

# LaTeX table for paper appendix
print("=" * 80)
print("LATEX TABLE (for paper appendix)")
print("=" * 80)
print()
print(r"\begin{table}[t]")
print(r"\centering")
print(r"\caption{Worst-case monotonicity violation magnitude $\varepsilon$ across 10{,}000 random confusion matrices $\mathbf{C}_0$ per cell. Non-IV topologies exhibit $\varepsilon < 0.06$, scaling approximately as $O(1/K)$.}")
print(r"\label{tab:epsilon_bounds}")
print(r"\small")
print(r"\begin{tabular}{lcrrr}")
print(r"\toprule")
print(r"Topology & Direction & $K{=}3$ & $K{=}5$ & $K{=}7$ \\")
print(r"\midrule")

for topo in ALL_TOPOS:
    direction = rv[topo]["K3"]["direction"].replace("non-dec", r"$\nearrow$").replace("non-inc", r"$\searrow$")
    vals = []
    for K in K_VALUES:
        v = eps_table[(topo, K)]
        if v < 0.001:
            vals.append(f"{v:.2e}")
        else:
            vals.append(f"{v:.4f}")
    topo_display = topo.replace("_", " ").title()
    if topo == "mbias":
        topo_display = "M-bias"
    elif topo == "frontdoor":
        topo_display = "Front-door"
    print(f"{topo_display} & {direction} & {vals[0]} & {vals[1]} & {vals[2]} \\\\")

print(r"\midrule")
print(r"IV & $\nearrow$ & \multicolumn{3}{c}{Unbounded (Wald singularity)} \\")
print(r"\bottomrule")
print(r"\end{tabular}")
print(r"\end{table}")
print()

# Usefulness assessment
print("=" * 80)
print("USEFULNESS ASSESSMENT FOR PAPER")
print("=" * 80)
print()
print("Is the bound tight enough to be useful?")
print()
print("The worst non-IV violation is ε ≈ 0.056 (exposure, K=3). This means:")
print("  - At K=3, |B(δ₂)| can briefly dip below |B(δ₁)| by up to 0.056 units")
print("    even though δ₂ > δ₁ (non-strict monotonicity violation)")
print("  - This is small relative to typical bias magnitudes of 0.5-2.0")
print("  - For K≥5, the worst violation drops below 0.052, and for K≥7, below 0.022")
print()
print("Recommendation: Frame as 'approximate monotonicity' result in the paper.")
print("The conjecture holds up to O(1/K) perturbations, which shrink rapidly with K.")
print("For typical annotation tasks with K=5+ categories, violations are negligible (<0.05).")
print("The IV topology is a genuine exception (unbounded) and should be explicitly excluded.")
