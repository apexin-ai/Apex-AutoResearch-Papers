#!/usr/bin/env python3
"""
Exp: FWL Nonlinear Scaling Test

Tests whether FWL invariance breakdown under logistic regression scales with N.

Under linear OLS, FWL invariance means matrix-based corrections (naive plug-in)
achieve exactly 0% bias reduction for "covariate" topologies (confounding,
mediation, collider, M-bias). Under logistic regression this invariance breaks,
but the paper claims the breakdown is negligible (< 0.1%).

This script tests whether the breakdown magnitude changes with sample size N,
across 7 topologies, 3 error levels, and N in {1000, 5000, 10000, 50000}.

For each (topology, N, error_level), we run 200 MC replications:
  1. Generate data from the DGP (logistic link for binary Y)
  2. Misclassify A -> A* using a synthetic confusion matrix
  3. Fit logistic regression with and without naive plug-in correction
  4. Compute bias reduction % = 1 - |bias_corrected| / |bias_uncorrected|

Output: artifacts/exp_fwl_nonlinear_scaling_results.json

Dependencies: numpy, sklearn (LogisticRegression)
"""

import sys
import json
import time
import os
import numpy as np
from pathlib import Path
from sklearn.linear_model import LogisticRegression

# Force unbuffered output
import functools
print = functools.partial(print, flush=True)

# ============================================================================
# Import DGP generators from plan_006
# ============================================================================

PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
sys.path.insert(0, str(PROJ))
import importlib.util
spec = importlib.util.spec_from_file_location("plan_006", str(PROJ / "plan_006_asv_empirical.py"))
plan_006 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plan_006)

# ============================================================================
# Constants
# ============================================================================

K = 3
N_VALUES = [1000, 5000, 10000, 50000]
N_REPS = 200
SEED = 20260523

# All 7 topologies; IV is skipped (Wald estimator has no FWL structure)
TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
              'mbias', 'frontdoor', 'iv']

# Topologies where A enters as covariate (T+D regression form)
COVARIATE_TOPOS = {'confounding', 'mediation', 'collider', 'mbias', 'frontdoor'}

ERROR_LEVELS = {
    'low':    0.9,   # diag=0.9, off-diag uniform
    'medium': 0.7,   # diag=0.7
    'high':   0.5,   # diag=0.5
}


# ============================================================================
# Confusion matrix construction
# ============================================================================

def make_cm(K, diag_val):
    """Build a K×K column-stochastic confusion matrix with given diagonal."""
    C = np.full((K, K), (1 - diag_val) / (K - 1))
    np.fill_diagonal(C, diag_val)
    return C


# ============================================================================
# DGP generators (logistic link — binary Y)
# Reuse plan_006 structure but produce binary Y via logistic link
# ============================================================================

# DGP parameters from plan_006
DGP_PARAMS = plan_006.make_dgp_params(K)

# Shared parameters
TAU = 0.5
BETA = np.array([0.0, 1.0, -0.5])
P_A = plan_006.make_p_A(K)


def dummy_encode(A, K=3):
    N = len(A)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    return D


def misclassify(A, C, rng):
    """Misclassify true labels A using confusion matrix C."""
    probs = C[:, A]
    cum = np.cumsum(probs, axis=0)
    u = rng.uniform(size=len(A))
    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)


def _softmax_sample(logits, rng):
    logits = logits - logits.max(axis=1, keepdims=True)
    probs = np.exp(logits)
    probs /= probs.sum(axis=1, keepdims=True)
    cum = np.cumsum(probs, axis=1)
    u = rng.uniform(size=logits.shape[0])[:, None]
    return (u >= cum[:, :-1]).sum(axis=1).astype(int)


def gen_confounding_logistic(N, rng):
    """Confounding: A -> T, A -> Y, T -> Y. Y is binary via logistic link."""
    A = rng.choice(K, size=N, p=P_A)
    D = dummy_encode(A)
    alpha = np.array([0.5, -0.3])  # A -> T
    T = D @ alpha + rng.normal(0, 1, N)
    eta = TAU * T + D @ BETA[1:] + rng.normal(0, 1, N)
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return T, Y, A


def gen_mediation_logistic(N, rng):
    """Mediation: T -> A -> Y (with direct T -> Y). Y binary."""
    T = rng.binomial(1, 0.5, N).astype(float)
    logits = np.array([0.0, 0.5, -0.3])[None, :] + np.array([0.0, 0.8, -0.6])[None, :] * T[:, None]
    A = _softmax_sample(logits, rng)
    D = dummy_encode(A)
    eta = TAU * T + D @ BETA[1:] + BETA[0] + rng.normal(0, 1, N)
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return T, Y, A


def gen_collider_logistic(N, rng):
    """Collider: T -> A <- Y. Y binary."""
    T = rng.normal(0, 1, N)
    eta_y = TAU * T + rng.normal(0, 1, N)
    prob_y = 1.0 / (1.0 + np.exp(-eta_y))
    Y = rng.binomial(1, prob_y, N).astype(float)
    logits = (np.zeros((N, K))
              + np.array([0.0, 0.5, -0.3])[None, :] * T[:, None]
              + np.array([0.0, 0.8, 0.6])[None, :] * Y[:, None])
    A = _softmax_sample(logits, rng)
    return T, Y, A


def gen_exposure_logistic(N, rng):
    """Exposure: A -> Y (no treatment T). Y binary."""
    A = rng.choice(K, size=N, p=P_A)
    D = dummy_encode(A)
    eta = D @ BETA[1:] + BETA[0] + rng.normal(0, 1, N)
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return None, Y, A


def gen_mbias_logistic(N, rng):
    """M-bias: U1->T, U1->A, U2->A, U2->Y, T->Y. Y binary."""
    U1 = rng.normal(0, 1, N)
    U2 = rng.normal(0, 1, N)
    T = U1 + rng.normal(0, 1, N)
    logits = (np.zeros((N, K))
              + np.array([0.0, 0.8, -0.5])[None, :] * U1[:, None]
              + np.array([0.0, 0.6, 0.9])[None, :] * U2[:, None])
    A = _softmax_sample(logits, rng)
    eta = TAU * T + U2 + rng.normal(0, 1, N)
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return T, Y, A


def gen_frontdoor_logistic(N, rng):
    """Front-door: T -> A -> Y with U -> T, U -> Y. Y binary."""
    U = rng.normal(0, 1, N)
    T = U + rng.normal(0, 1, N)
    logits = np.array([0.0, 0.5, -0.3])[None, :] + np.array([0.0, 1.0, -0.8])[None, :] * T[:, None]
    A = _softmax_sample(logits, rng)
    D = dummy_encode(A)
    eta = D @ BETA[1:] + U + rng.normal(0, 1, N)
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return T, Y, A


def gen_iv_logistic(N, rng):
    """IV: Z -> A -> Y with U -> A, U -> Y. Y binary."""
    Z = rng.binomial(1, 0.5, N).astype(float)
    U = rng.normal(0, 1, N)
    logits = (np.zeros((N, K))
              + np.array([0.0, 1.0, -0.5])[None, :] * Z[:, None]
              + np.array([0.0, 0.8, 0.6])[None, :] * U[:, None])
    A = _softmax_sample(logits, rng)
    D = dummy_encode(A)
    eta = D @ BETA[1:] + U + rng.normal(0, 1, N)
    prob = 1.0 / (1.0 + np.exp(-eta))
    Y = rng.binomial(1, prob, N).astype(float)
    return Z, Y, A


GEN_LOGISTIC = {
    'confounding': gen_confounding_logistic,
    'mediation': gen_mediation_logistic,
    'collider': gen_collider_logistic,
    'exposure': gen_exposure_logistic,
    'mbias': gen_mbias_logistic,
    'frontdoor': gen_frontdoor_logistic,
    'iv': gen_iv_logistic,
}

# Also reuse plan_006 generators for the linear DGP comparison
GEN_LINEAR = plan_006.GEN_FNS


# ============================================================================
# Estimators
# ============================================================================

def fit_logistic_with_dummies(Y, T, D_star):
    """Fit logistic: Y ~ T + D_star. Returns tau_hat (coef on T)."""
    X = np.column_stack([T, D_star])
    try:
        lr = LogisticRegression(C=1e10, max_iter=2000, solver='lbfgs')
        lr.fit(X, Y.astype(int))
        return lr.coef_[0][0]  # coefficient on T
    except Exception:
        return np.nan


def fit_logistic_exposure(Y, D_star):
    """Fit logistic: Y ~ D_star. Returns coefs on dummies."""
    try:
        lr = LogisticRegression(C=1e10, max_iter=2000, solver='lbfgs')
        lr.fit(D_star, Y.astype(int))
        return lr.coef_[0]  # coefficients on dummies
    except Exception:
        return np.full(D_star.shape[1], np.nan)


def fit_linear_with_dummies(Y, T, D_star):
    """Fit OLS: Y ~ 1 + T + D_star. Returns tau_hat (coef on T)."""
    N = len(Y)
    X = np.column_stack([np.ones(N), T, D_star])
    try:
        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
        return beta[1]  # coefficient on T
    except np.linalg.LinAlgError:
        return np.nan


def fit_linear_exposure(Y, D_star):
    """Fit OLS: Y ~ 1 + D_star. Returns coefs on dummies."""
    N = len(Y)
    X = np.column_stack([np.ones(N), D_star])
    try:
        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
        return beta[1:]  # coefficients on dummies
    except np.linalg.LinAlgError:
        return np.full(D_star.shape[1], np.nan)


# ============================================================================
# Correction: naive plug-in (multiply dummies by C_inv)
# ============================================================================

def apply_naive_correction(D_star, C):
    """
    Naive plug-in correction: replace D*(A*) with D*(A*) @ C_inv_block.

    For K categories with K-1 dummies (dropping category 0):
    The correction transforms the dummy matrix by the inverse of the
    relevant subblock of C, attempting to undo misclassification.

    More precisely: if D* are dummies for A*, the corrected dummies are
    D_corr = D* @ M where M = C_sub^{-1} and C_sub captures how the
    K-1 dummy means change under misclassification.

    We use the full C inverse approach: map dummy indicators through C^{-1}.
    """
    K = C.shape[0]
    try:
        C_inv = np.linalg.inv(C)
    except np.linalg.LinAlgError:
        return D_star  # fallback: no correction

    N = D_star.shape[0]
    # Reconstruct full one-hot from dummies (category 0 is the omitted one)
    D_full = np.zeros((N, K))
    D_full[:, 0] = 1.0  # start with category 0
    for j in range(K - 1):
        D_full[:, j + 1] = D_star[:, j]
        D_full[:, 0] -= D_star[:, j]

    # Apply C_inv: corrected_full = D_full @ C_inv^T
    # Each row of D_full is a one-hot; C_inv maps misclassified -> true
    corrected_full = D_full @ C_inv.T

    # Extract corrected dummies (drop category 0)
    D_corrected = corrected_full[:, 1:]
    return D_corrected


# ============================================================================
# Oracle true parameters (large N)
# ============================================================================

def compute_oracle_params(N_oracle=200_000):
    """Compute true parameters using large N for each topology under logistic DGP."""
    rng = np.random.default_rng(99999)
    true_params = {}

    for topo in TOPOLOGIES:
        if topo == 'iv':
            continue  # skip IV

        gen_fn = GEN_LOGISTIC[topo]
        first_var, Y, A = gen_fn(N_oracle, rng)
        D = dummy_encode(A)

        if topo == 'exposure':
            coefs = fit_logistic_exposure(Y, D)
            true_params[topo] = {'type': 'exposure', 'coefs': coefs.tolist() if isinstance(coefs, np.ndarray) else [coefs]}
        else:
            tau = fit_logistic_with_dummies(Y, first_var, D)
            true_params[topo] = {'type': 'covariate', 'tau': float(tau)}

    return true_params


# ============================================================================
# MC simulation for one configuration
# ============================================================================

def run_one_config(topo, N, C, n_reps, base_seed, true_params):
    """
    Run MC simulation for one (topology, N, confusion_matrix) configuration.

    Returns dict with:
      - logistic_bias_reduction_pcts: list of per-rep bias reduction %
      - linear_bias_reduction_pcts: list of per-rep bias reduction %
      - mean logistic/linear bias reduction
    """
    rng = np.random.default_rng(base_seed)
    gen_fn = GEN_LOGISTIC[topo]

    logistic_br_list = []  # bias reduction % for logistic
    linear_br_list = []    # bias reduction % for linear

    for rep in range(n_reps):
        # Generate data
        first_var, Y, A = gen_fn(N, rng)

        # Misclassify
        A_star = misclassify(A, C, rng)
        D_star = dummy_encode(A_star)

        # Apply correction
        D_corrected = apply_naive_correction(D_star, C)

        if topo == 'exposure':
            # Logistic: Y ~ D_star vs Y ~ D_corrected
            coefs_uncorr = fit_logistic_exposure(Y, D_star)
            coefs_corr = fit_logistic_exposure(Y, D_corrected)

            true_coefs = np.array(true_params[topo]['coefs'])

            if np.all(np.isfinite(coefs_uncorr)) and np.all(np.isfinite(coefs_corr)):
                bias_uncorr = np.mean(np.abs(coefs_uncorr - true_coefs))
                bias_corr = np.mean(np.abs(coefs_corr - true_coefs))
                if bias_uncorr > 1e-10:
                    br = 1.0 - bias_corr / bias_uncorr
                    logistic_br_list.append(br)

            # Linear comparison
            coefs_uncorr_lin = fit_linear_exposure(Y, D_star)
            coefs_corr_lin = fit_linear_exposure(Y, D_corrected)

            if np.all(np.isfinite(coefs_uncorr_lin)) and np.all(np.isfinite(coefs_corr_lin)):
                bias_uncorr_lin = np.mean(np.abs(coefs_uncorr_lin - true_coefs))
                bias_corr_lin = np.mean(np.abs(coefs_corr_lin - true_coefs))
                if bias_uncorr_lin > 1e-10:
                    br_lin = 1.0 - bias_corr_lin / bias_uncorr_lin
                    linear_br_list.append(br_lin)
        else:
            # Covariate topologies: Y ~ T + D_star
            T = first_var
            tau_true = true_params[topo]['tau']

            # Logistic
            tau_uncorr = fit_logistic_with_dummies(Y, T, D_star)
            tau_corr = fit_logistic_with_dummies(Y, T, D_corrected)

            if np.isfinite(tau_uncorr) and np.isfinite(tau_corr):
                bias_uncorr = abs(tau_uncorr - tau_true)
                bias_corr = abs(tau_corr - tau_true)
                if bias_uncorr > 1e-10:
                    br = 1.0 - bias_corr / bias_uncorr
                    logistic_br_list.append(br)

            # Linear (for comparison — should be ~0% for covariate topos)
            # Binarize Y for linear too (same data)
            tau_uncorr_lin = fit_linear_with_dummies(Y, T, D_star)
            tau_corr_lin = fit_linear_with_dummies(Y, T, D_corrected)

            if np.isfinite(tau_uncorr_lin) and np.isfinite(tau_corr_lin):
                bias_uncorr_lin = abs(tau_uncorr_lin - tau_true)
                bias_corr_lin = abs(tau_corr_lin - tau_true)
                if bias_uncorr_lin > 1e-10:
                    br_lin = 1.0 - bias_corr_lin / bias_uncorr_lin
                    linear_br_list.append(br_lin)

    def safe_mean(lst):
        return float(np.mean(lst)) if lst else None

    def safe_std(lst):
        return float(np.std(lst)) if lst else None

    def safe_median(lst):
        return float(np.median(lst)) if lst else None

    return {
        'logistic_mean_bias_reduction_pct': safe_mean(logistic_br_list),
        'logistic_std_bias_reduction_pct': safe_std(logistic_br_list),
        'logistic_median_bias_reduction_pct': safe_median(logistic_br_list),
        'linear_mean_bias_reduction_pct': safe_mean(linear_br_list),
        'linear_std_bias_reduction_pct': safe_std(linear_br_list),
        'linear_median_bias_reduction_pct': safe_median(linear_br_list),
        'logistic_n_valid': len(logistic_br_list),
        'linear_n_valid': len(linear_br_list),
    }


# ============================================================================
# Main
# ============================================================================

def clean_json(obj):
    """Make object JSON-serializable."""
    if isinstance(obj, (float, np.floating)):
        v = float(obj)
        return None if (np.isnan(v) or np.isinf(v)) else v
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return clean_json(obj.tolist())
    if isinstance(obj, dict):
        return {str(k): clean_json(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [clean_json(v) for v in obj]
    return obj


def main():
    t0 = time.time()
    out_dir = os.path.dirname(os.path.abspath(__file__))

    print("=" * 70)
    print("FWL Nonlinear Scaling Test")
    print(f"  K={K}, N_values={N_VALUES}, n_reps={N_REPS}")
    print(f"  Error levels: {list(ERROR_LEVELS.keys())}")
    print(f"  Topologies: {TOPOLOGIES}")
    print("=" * 70)

    # Build confusion matrices
    cms = {}
    for level_name, diag_val in ERROR_LEVELS.items():
        cms[level_name] = make_cm(K, diag_val)
        print(f"\n  CM ({level_name}, diag={diag_val}):")
        print(f"    {cms[level_name]}")

    # Compute oracle parameters
    print("\n[1/2] Computing oracle true parameters (N=200k)...")
    true_params = compute_oracle_params(N_oracle=200_000)
    for topo, tp in true_params.items():
        if tp['type'] == 'covariate':
            print(f"  {topo}: tau_true = {tp['tau']:.6f}")
        else:
            print(f"  {topo}: coefs = {tp['coefs']}")

    # Run MC simulations
    print(f"\n[2/2] Running MC simulations ({N_REPS} reps each)...")
    results = []
    active_topos = [t for t in TOPOLOGIES if t != 'iv']  # skip IV
    n_configs = len(active_topos) * len(N_VALUES) * len(ERROR_LEVELS)
    idx = 0

    for topo in active_topos:
        for N in N_VALUES:
            for level_name, diag_val in ERROR_LEVELS.items():
                idx += 1
                C = cms[level_name]
                base_seed = SEED + hash((topo, N, level_name)) % 100000

                t1 = time.time()
                r = run_one_config(topo, N, C, N_REPS, base_seed, true_params)
                elapsed = time.time() - t1

                log_br = r['logistic_mean_bias_reduction_pct']
                lin_br = r['linear_mean_bias_reduction_pct']
                log_s = f"{log_br*100:.2f}%" if log_br is not None else "N/A"
                lin_s = f"{lin_br*100:.2f}%" if lin_br is not None else "N/A"

                print(f"  [{idx}/{n_configs}] {topo:<13} N={N:>6} err={level_name:<6} "
                      f"logistic_BR={log_s:>8} linear_BR={lin_s:>8} "
                      f"({elapsed:.1f}s)")

                results.append({
                    'topology': topo,
                    'N': N,
                    'error_level': level_name,
                    'diag_val': diag_val,
                    **r,
                })

    # Summary table
    print("\n" + "=" * 70)
    print("SUMMARY: Mean Bias Reduction % (logistic | linear)")
    print("=" * 70)

    header = f"{'Topology':<13} {'Error':>6}"
    for N in N_VALUES:
        header += f" | N={N:>5}"
    print(header)
    print("-" * len(header))

    for topo in active_topos:
        for level_name in ERROR_LEVELS:
            row = f"{topo:<13} {level_name:>6}"
            for N in N_VALUES:
                r = next((x for x in results
                         if x['topology'] == topo and x['N'] == N
                         and x['error_level'] == level_name), None)
                if r and r['logistic_mean_bias_reduction_pct'] is not None:
                    log_br = r['logistic_mean_bias_reduction_pct'] * 100
                    lin_br = (r['linear_mean_bias_reduction_pct'] or 0) * 100
                    row += f" | {log_br:>5.2f}/{lin_br:>5.2f}"
                else:
                    row += " |    N/A"
            print(row)

    # Check scaling trend
    print("\n" + "=" * 70)
    print("SCALING ANALYSIS: Does logistic bias reduction grow with N?")
    print("=" * 70)

    for topo in active_topos:
        for level_name in ERROR_LEVELS:
            brs = []
            for N in N_VALUES:
                r = next((x for x in results
                         if x['topology'] == topo and x['N'] == N
                         and x['error_level'] == level_name), None)
                if r and r['logistic_mean_bias_reduction_pct'] is not None:
                    brs.append((N, r['logistic_mean_bias_reduction_pct'] * 100))

            if len(brs) >= 2:
                ns = [b[0] for b in brs]
                vals = [b[1] for b in brs]
                # Simple slope via log-linear regression
                log_ns = np.log10(ns)
                slope = np.polyfit(log_ns, vals, 1)[0]
                trend = "INCREASING" if slope > 0.5 else "DECREASING" if slope < -0.5 else "STABLE"
                print(f"  {topo:<13} {level_name:>6}: "
                      f"range [{min(vals):.2f}%, {max(vals):.2f}%] "
                      f"slope={slope:.3f}pp/decade -> {trend}")

    # Save results
    output = clean_json({
        'config': {
            'K': K,
            'N_values': N_VALUES,
            'n_reps': N_REPS,
            'seed': SEED,
            'error_levels': ERROR_LEVELS,
            'topologies': [t for t in TOPOLOGIES if t != 'iv'],
        },
        'true_params': true_params,
        'confusion_matrices': {name: C.tolist() for name, C in cms.items()},
        'results': results,
    })

    out_path = os.path.join(out_dir, 'exp_fwl_nonlinear_scaling_results.json')
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")

    total = time.time() - t0
    print(f"Total time: {total:.0f}s ({total/60:.1f}min)")


if __name__ == '__main__':
    main()
