#!/usr/bin/env python3
"""
exp_proportional_effects.py — Proportional Effects Failure Rate Analysis

Analyzes how sign-preservation and λ(C) behavior in the mediation topology
depend on the degree of proportionality between treatment-mediator effects (f)
and mediator-outcome effects (g).

Key theory: In mediation, misclassification bias is:
    plim τ̂(A*) = τ_direct + (1 - λ(C)) * τ_indirect
When the proportional effects condition holds (f_j - f_0 = λ·g_j for all j),
λ(C) is guaranteed to stay in [0,1], preventing sign reversals from this term.
Under arbitrary (f,g), λ(C) can escape [0,1].

This script quantifies how failure rates change across:
  (a) Exact proportionality: f_j - f_0 = λ·g_j
  (b) Near-proportional: f_j - f_0 = λ·g_j + noise(σ)
  (c) Independent: f, g drawn independently

Method: Constructs synthetic sufficient statistics (no sampling noise) to
isolate the effect of the proportionality degree from Monte Carlo variance.

Inputs:  plan_006_asv_empirical.py (plim computation)
Outputs: artifacts/exp_proportional_effects_results.json
"""

import numpy as np
import json
import time
import sys
import argparse
import importlib.util
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent

# Import plan_006 module for compute_plim and extract_tau
spec = importlib.util.spec_from_file_location("plan_006", str(PROJ / "plan_006_asv_empirical.py"))
plan_006 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plan_006)


# ============================================================================
# Configuration
# ============================================================================

K = 3
N_CONFIGS = 100_000
SIGMA_VALUES = [0.1, 0.3, 0.5]
SEED = 42


# ============================================================================
# Helper: generate random confusion matrix from Dirichlet prior
# ============================================================================

def random_confusion_matrix(K, rng):
    """Generate a K×K confusion matrix where each column ~ Dirichlet(1,...,1)."""
    C = np.zeros((K, K))
    for j in range(K):
        C[:, j] = rng.dirichlet(np.ones(K))
    return C


# ============================================================================
# Synthetic sufficient statistics construction
# ============================================================================

def build_suff_stats(K, tau_direct, beta_0, g, f, p_A):
    """Build population-level sufficient statistics from structural parameters.

    In the mediation DGP:
        T ~ Bernoulli(0.5)
        A | T ~ Multinomial with E[T|A=k] = f[k]
        Y = beta_0 + sum_{j>=1} g[j-1] * D_j + tau_direct * T + eps

    Args:
        K: number of categories
        tau_direct: direct treatment effect
        beta_0: intercept
        g: (K-1)-vector of mediator→outcome coefficients (for dummies D_1,...,D_{K-1})
        f: K-vector of E[T|A=k] (conditional treatment probabilities)
        p_A: K-vector of P(A=k)

    Returns:
        dict of sufficient statistics compatible with plan_006.compute_plim
    """
    E_T = 0.5
    E_T2 = 0.5  # T is Bernoulli(0.5)

    E_TD = f * p_A  # E[T * I(A=k)] = E[T|A=k] * P(A=k)

    # E[Y * I(A=k)] = E[Y|A=k] * P(A=k)
    # E[Y|A=k] = beta_0 + g[k-1]*I(k>=1) + tau_direct * E[T|A=k]
    E_YD = np.zeros(K)
    E_YD[0] = beta_0 * p_A[0] + tau_direct * E_TD[0]
    for j in range(1, K):
        E_YD[j] = (beta_0 + g[j - 1]) * p_A[j] + tau_direct * E_TD[j]

    E_Y = beta_0 + sum(g[j - 1] * p_A[j] for j in range(1, K)) + tau_direct * E_T
    E_TY = beta_0 * E_T + sum(g[j - 1] * E_TD[j] for j in range(1, K)) + tau_direct * E_T2

    return {
        'p_A': p_A.copy(),
        'E_T': E_T,
        'E_T2': E_T2,
        'E_Y': E_Y,
        'E_TY': E_TY,
        'E_TD': E_TD.copy(),
        'E_YD': E_YD.copy(),
        'topology': 'mediation',
    }


# ============================================================================
# f-vector generators for different proportionality degrees
# ============================================================================

def make_f_exact_proportional(K, g, p_A, lambda_prop, E_T=0.5):
    """f_j - f_0 = lambda_prop * g_j for j=1,...,K-1.

    f_0 is determined by the constraint sum_k p_k f_k = E[T].
    """
    # f_j = c + lambda_prop * g[j-1] for j >= 1, f_0 = c
    # sum_k p_k f_k = c + lambda_prop * sum_{j>=1} p_j * g[j-1] = E[T]
    c = E_T - lambda_prop * sum(p_A[j] * g[j - 1] for j in range(1, K))
    f = np.zeros(K)
    f[0] = c
    for j in range(1, K):
        f[j] = c + lambda_prop * g[j - 1]
    return f


def make_f_near_proportional(K, g, p_A, lambda_prop, sigma, rng, E_T=0.5):
    """f_j - f_0 = lambda_prop * g_j + noise_j, noise ~ N(0, sigma^2).

    f_0 is determined by the constraint sum_k p_k f_k = E[T].
    """
    noise = rng.normal(0, sigma, K - 1)
    # f_j = c + lambda_prop * g[j-1] + noise[j-1] for j >= 1, f_0 = c
    c = E_T - sum(p_A[j] * (lambda_prop * g[j - 1] + noise[j - 1]) for j in range(1, K))
    f = np.zeros(K)
    f[0] = c
    for j in range(1, K):
        f[j] = c + lambda_prop * g[j - 1] + noise[j - 1]
    return f


def make_f_independent(K, p_A, rng, E_T=0.5):
    """f drawn to be consistent with E[T]=0.5 but otherwise random.

    Draw f[1:] ~ N(0.5, scale^2), then set f[0] from constraint.
    """
    scale = 0.15  # reasonable variation in E[T|A=k]
    f = np.zeros(K)
    f[1:] = rng.normal(E_T, scale, K - 1)
    # Clip to valid probability range
    f[1:] = np.clip(f[1:], 0.05, 0.95)
    # Determine f[0] from constraint
    f[0] = (E_T - sum(p_A[j] * f[j] for j in range(1, K))) / p_A[0]
    f[0] = np.clip(f[0], 0.01, 0.99)
    return f


# ============================================================================
# Core evaluation
# ============================================================================

def evaluate_configs(degree_name, n_configs, K, rng, f_generator,
                     g_generator, tau_range=(0.3, 1.0)):
    """Evaluate lambda(C) for many random configurations.

    For each configuration:
      1. Generate random g (outcome coefficients)
      2. Generate f according to the specified degree
      3. Build synthetic sufficient statistics (exact, no MC noise)
      4. Generate random C ~ Dirichlet
      5. Compute lambda(C) and check sign preservation

    Args:
        degree_name: label for this degree
        n_configs: number of configurations to evaluate
        K: number of categories
        rng: numpy random generator
        f_generator: callable(K, g, p_A, rng) -> f vector
        g_generator: callable(K, rng) -> g vector
        tau_range: range for random tau_direct

    Returns:
        dict with summary statistics
    """
    p_A = np.array([0.40, 0.35, 0.25])
    beta_0 = 1.0

    lambdas = []
    sign_failures = 0
    lambda_oob = 0
    valid = 0
    skipped = 0

    report_interval = max(1, n_configs // 10)

    for i in range(n_configs):
        if i > 0 and i % report_interval == 0:
            pct = lambda_oob / max(valid, 1) * 100
            sf_pct = sign_failures / max(valid, 1) * 100
            print(f"    [{degree_name}] {i}/{n_configs} "
                  f"(lambda OOB: {pct:.1f}%, sign fail: {sf_pct:.1f}%)")

        # Random structural parameters
        g = g_generator(K, rng)
        tau_direct = rng.uniform(tau_range[0], tau_range[1]) * rng.choice([-1, 1])

        # Generate f according to proportionality degree
        f = f_generator(K, g, p_A, rng)

        # Validate f (all elements should be valid probabilities for binary T)
        if np.any(f < 0.01) or np.any(f > 0.99):
            skipped += 1
            continue

        # Build exact sufficient statistics
        st = build_suff_stats(K, tau_direct, beta_0, g, f, p_A)

        # Verify tau_true recovery
        plim_I = plan_006.compute_plim(np.eye(K), st, K)
        tau_true = plan_006.extract_tau(plim_I, 'mediation')
        if np.isnan(tau_true) or abs(tau_true - tau_direct) > 1e-8:
            skipped += 1
            continue

        # Compute indirect effect
        var_T = st['E_T2'] - st['E_T'] ** 2
        if abs(var_T) < 1e-12:
            skipped += 1
            continue
        tau_total = (st['E_TY'] - st['E_T'] * st['E_Y']) / var_T
        tau_indirect = tau_total - tau_true

        # Generate random confusion matrix
        C = random_confusion_matrix(K, rng)

        # Compute biased plim
        plim_C = plan_006.compute_plim(C, st, K)
        tau_biased = plan_006.extract_tau(plim_C, 'mediation')

        if np.isnan(tau_biased):
            skipped += 1
            continue

        valid += 1
        bias = tau_biased - tau_true

        # Compute lambda(C)
        if abs(tau_indirect) < 1e-10:
            lambda_val = np.nan
        else:
            lambda_val = 1.0 - bias / tau_indirect
            if not (0.0 <= lambda_val <= 1.0):
                lambda_oob += 1

        if np.isfinite(lambda_val):
            lambdas.append(lambda_val)

        # Sign preservation
        if abs(tau_true) > 1e-12:
            if np.sign(tau_biased) != np.sign(tau_true):
                sign_failures += 1

    lambda_arr = np.array(lambdas) if lambdas else np.array([])

    return {
        'degree': degree_name,
        'n_configs': n_configs,
        'valid': valid,
        'skipped': skipped,
        'lambda_oob_count': lambda_oob,
        'lambda_oob_rate': lambda_oob / max(valid, 1),
        'sign_failure_count': sign_failures,
        'sign_failure_rate': sign_failures / max(valid, 1),
        'lambda_mean': float(np.mean(lambda_arr)) if len(lambda_arr) > 0 else None,
        'lambda_std': float(np.std(lambda_arr)) if len(lambda_arr) > 0 else None,
        'lambda_median': float(np.median(lambda_arr)) if len(lambda_arr) > 0 else None,
        'lambda_q05': float(np.percentile(lambda_arr, 5)) if len(lambda_arr) > 0 else None,
        'lambda_q95': float(np.percentile(lambda_arr, 95)) if len(lambda_arr) > 0 else None,
        'lambda_min': float(np.min(lambda_arr)) if len(lambda_arr) > 0 else None,
        'lambda_max': float(np.max(lambda_arr)) if len(lambda_arr) > 0 else None,
        'n_lambda_finite': len(lambda_arr),
    }


# ============================================================================
# Main
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='Proportional effects failure rate analysis')
    parser.add_argument('--n-configs', type=int, default=N_CONFIGS,
                        help='Number of random configurations per degree')
    parser.add_argument('--seed', type=int, default=SEED)
    args = parser.parse_args()

    n_configs = args.n_configs
    seed = args.seed
    t0 = time.time()
    rng = np.random.default_rng(seed)

    print("=" * 80)
    print("Proportional Effects Failure Rate Analysis")
    print(f"  K={K}, N_configs={n_configs:,}, seed={seed}")
    print(f"  Method: synthetic sufficient statistics (zero MC noise)")
    print("=" * 80)

    # g generator: random outcome coefficients
    def g_gen(K, rng):
        return rng.normal(0, 0.5, K - 1)

    all_results = []

    # -----------------------------------------------------------------------
    # (a) Exact proportional: f_j - f_0 = lambda * g_j
    # -----------------------------------------------------------------------
    print("\n" + "-" * 80)
    print("[1/6] Exact proportional: f_j - f_0 = lambda * g_j")
    t1 = time.time()

    def f_gen_exact(K, g, p_A, rng):
        lam = rng.uniform(0.1, 0.5)
        return make_f_exact_proportional(K, g, p_A, lam)

    r = evaluate_configs("exact_proportional", n_configs, K, rng, f_gen_exact, g_gen)
    r['description'] = "f_j - f_0 = lambda * g_j, lambda ~ U(0.1, 0.5)"
    all_results.append(r)
    print(f"  Done in {time.time()-t1:.1f}s")
    print(f"  lambda OOB rate: {r['lambda_oob_rate']:.6f} ({r['lambda_oob_count']}/{r['valid']})")
    print(f"  Sign fail rate:  {r['sign_failure_rate']:.6f} ({r['sign_failure_count']}/{r['valid']})")
    if r['lambda_mean'] is not None:
        print(f"  lambda mean +/- std: {r['lambda_mean']:.4f} +/- {r['lambda_std']:.4f}")

    # -----------------------------------------------------------------------
    # (b) Near-proportional with varying sigma
    # -----------------------------------------------------------------------
    for sigma in SIGMA_VALUES:
        idx = SIGMA_VALUES.index(sigma) + 2
        print("\n" + "-" * 80)
        print(f"[{idx}/6] Near-proportional: f_j - f_0 = lambda*g_j + N(0, {sigma}^2)")
        t1 = time.time()

        def f_gen_near(K, g, p_A, rng, s=sigma):
            lam = rng.uniform(0.1, 0.5)
            return make_f_near_proportional(K, g, p_A, lam, s, rng)

        r = evaluate_configs(f"near_proportional_sigma_{sigma}", n_configs, K, rng,
                             f_gen_near, g_gen)
        r['description'] = f"f_j - f_0 = lambda*g_j + eps, eps ~ N(0, {sigma}^2)"
        r['sigma'] = sigma
        all_results.append(r)
        print(f"  Done in {time.time()-t1:.1f}s")
        print(f"  lambda OOB rate: {r['lambda_oob_rate']:.6f} ({r['lambda_oob_count']}/{r['valid']})")
        print(f"  Sign fail rate:  {r['sign_failure_rate']:.6f} ({r['sign_failure_count']}/{r['valid']})")
        if r['lambda_mean'] is not None:
            print(f"  lambda mean +/- std: {r['lambda_mean']:.4f} +/- {r['lambda_std']:.4f}")

    # -----------------------------------------------------------------------
    # (c) Independent: f and g unrelated
    # -----------------------------------------------------------------------
    print("\n" + "-" * 80)
    print("[5/6] Independent: f and g drawn independently")
    t1 = time.time()

    def f_gen_independent(K, g, p_A, rng):
        return make_f_independent(K, p_A, rng)

    r = evaluate_configs("independent", n_configs, K, rng, f_gen_independent, g_gen)
    r['description'] = "f independent of g, f[k] ~ N(0.5, 0.15^2)"
    all_results.append(r)
    print(f"  Done in {time.time()-t1:.1f}s")
    print(f"  lambda OOB rate: {r['lambda_oob_rate']:.6f} ({r['lambda_oob_count']}/{r['valid']})")
    print(f"  Sign fail rate:  {r['sign_failure_rate']:.6f} ({r['sign_failure_count']}/{r['valid']})")
    if r['lambda_mean'] is not None:
        print(f"  lambda mean +/- std: {r['lambda_mean']:.4f} +/- {r['lambda_std']:.4f}")

    # -----------------------------------------------------------------------
    # (d) Default plan_006 params (simulation-based, for reference)
    # -----------------------------------------------------------------------
    print("\n" + "-" * 80)
    print("[6/6] Default plan_006 DGP (simulation-based reference)")
    t1 = time.time()

    default_params = plan_006.make_dgp_params(K)['mediation']
    st_sim = plan_006.precompute_suff_stats(K, 'mediation', default_params,
                                             N=2_000_000, seed=seed + 999)
    plim_I = plan_006.compute_plim(np.eye(K), st_sim, K)
    tau_true = plan_006.extract_tau(plim_I, 'mediation')
    var_T = st_sim['E_T2'] - st_sim['E_T'] ** 2
    tau_total = (st_sim['E_TY'] - st_sim['E_T'] * st_sim['E_Y']) / var_T
    tau_indirect = tau_total - tau_true

    oob = 0
    sfail = 0
    lambdas_default = []
    for i in range(n_configs):
        C = random_confusion_matrix(K, rng)
        plim_C = plan_006.compute_plim(C, st_sim, K)
        tau_biased = plan_006.extract_tau(plim_C, 'mediation')
        if np.isnan(tau_biased):
            continue
        bias = tau_biased - tau_true
        if abs(tau_indirect) > 1e-10:
            lv = 1.0 - bias / tau_indirect
            lambdas_default.append(lv)
            if not (0.0 <= lv <= 1.0):
                oob += 1
        if abs(tau_true) > 1e-12 and np.sign(tau_biased) != np.sign(tau_true):
            sfail += 1

    n_valid = len(lambdas_default)
    lam_arr = np.array(lambdas_default)
    default_result = {
        'degree': 'default_plan006',
        'description': (f"Fixed plan_006 params: delta={default_params['delta'].tolist()}, "
                        f"beta={default_params['beta'].tolist()}"),
        'n_configs': n_configs,
        'valid': n_valid,
        'skipped': n_configs - n_valid,
        'lambda_oob_count': oob,
        'lambda_oob_rate': oob / max(n_valid, 1),
        'sign_failure_count': sfail,
        'sign_failure_rate': sfail / max(n_valid, 1),
        'lambda_mean': float(np.mean(lam_arr)) if len(lam_arr) > 0 else None,
        'lambda_std': float(np.std(lam_arr)) if len(lam_arr) > 0 else None,
        'lambda_median': float(np.median(lam_arr)) if len(lam_arr) > 0 else None,
        'lambda_q05': float(np.percentile(lam_arr, 5)) if len(lam_arr) > 0 else None,
        'lambda_q95': float(np.percentile(lam_arr, 95)) if len(lam_arr) > 0 else None,
        'lambda_min': float(np.min(lam_arr)) if len(lam_arr) > 0 else None,
        'lambda_max': float(np.max(lam_arr)) if len(lam_arr) > 0 else None,
        'n_lambda_finite': len(lam_arr),
        'tau_true': float(tau_true),
        'tau_total': float(tau_total),
        'tau_indirect': float(tau_indirect),
    }
    all_results.append(default_result)
    print(f"  Done in {time.time()-t1:.1f}s")
    print(f"  tau_true={tau_true:.6f}, tau_indirect={tau_indirect:.6f}")
    print(f"  lambda OOB rate: {default_result['lambda_oob_rate']:.6f} ({oob}/{n_valid})")
    print(f"  Sign fail rate:  {default_result['sign_failure_rate']:.6f} ({sfail}/{n_valid})")
    if default_result['lambda_mean'] is not None:
        print(f"  lambda mean +/- std: {default_result['lambda_mean']:.4f} +/- {default_result['lambda_std']:.4f}")

    # ========================================================================
    # Summary table
    # ========================================================================
    print("\n" + "=" * 80)
    print("SUMMARY TABLE")
    print("=" * 80)
    header = (f"{'Degree':<35} {'lambda OOB%':>11} {'Sign Fail%':>11} "
              f"{'lambda mean':>11} {'lambda std':>11} {'lambda [5%,95%]':>18}")
    print(header)
    print("-" * len(header))

    for r in all_results:
        name = r['degree']
        oob_pct = f"{r['lambda_oob_rate'] * 100:.2f}%"
        sf_pct = f"{r['sign_failure_rate'] * 100:.2f}%"
        lm = f"{r['lambda_mean']:.4f}" if r['lambda_mean'] is not None else "N/A"
        ls = f"{r['lambda_std']:.4f}" if r['lambda_std'] is not None else "N/A"
        q5 = f"{r['lambda_q05']:.3f}" if r.get('lambda_q05') is not None else "?"
        q95 = f"{r['lambda_q95']:.3f}" if r.get('lambda_q95') is not None else "?"
        interval = f"[{q5}, {q95}]"
        print(f"{name:<35} {oob_pct:>11} {sf_pct:>11} {lm:>11} {ls:>11} {interval:>18}")

    # ========================================================================
    # Save results
    # ========================================================================
    output_path = PROJ / "artifacts" / "exp_proportional_effects_results.json"

    output = {
        'metadata': {
            'K': K,
            'n_configs': n_configs,
            'seed': seed,
            'sigma_values': SIGMA_VALUES,
            'method': 'synthetic_suff_stats',
            'proportionality_condition': 'f_j - f_0 = lambda * g_j for j=1,...,K-1',
            'p_A': [0.40, 0.35, 0.25],
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        },
        'results': all_results,
    }

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nResults saved to {output_path}")

    elapsed = time.time() - t0
    print(f"Total time: {elapsed:.1f}s ({elapsed / 60:.1f}min)")


if __name__ == "__main__":
    main()
