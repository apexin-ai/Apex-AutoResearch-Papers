#!/usr/bin/env python3
"""
nondiff_structured_stress_test.py
==================================
Compare 3 types of non-differential misclassification violations across 7 topologies:
  1. Uniform: random off-diagonal perturbation (existing baseline from nondiff_stress_test.py)
  2. Outcome-conditional: systematic diagonal decrease for high-Y, increase for low-Y
  3. Label-specific: accuracy proportional to |corr(A=k, Y)| from pretraining

For each (topology, epsilon, model), run MC simulation with differential C applied to
Y-subgroups, then compare bias degradation and sign-flip rates.

Input:  plan_006_asv_empirical.py (DGP generators, plim computation)
Output: artifacts/nondiff_structured_stress_results.json
"""

import numpy as np
import json
import time
import sys
import os
import importlib.util

# Import plan_006 via importlib
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plan006_path = os.path.join(PROJECT_ROOT, "plan_006_asv_empirical.py")
spec = importlib.util.spec_from_file_location("plan_006_asv_empirical", plan006_path)
plan006 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plan006)

# Re-export needed functions
GEN_FNS = plan006.GEN_FNS
make_dgp_params = plan006.make_dgp_params
precompute_suff_stats = plan006.precompute_suff_stats
compute_plim = plan006.compute_plim
extract_tau = plan006.extract_tau

# ─── Constants ──────────────────────────────────────────────
K = 3
N_MC = 10_000          # samples per MC trial
N_MATRICES = 1000      # confusion matrices per (topology, epsilon, model)
DIAG_THRESH = 0.7
EPSILONS = [0.01, 0.02, 0.05, 0.10, 0.20]
TOPOLOGIES = ['confounding', 'exposure', 'mediation', 'collider', 'mbias', 'iv', 'frontdoor']
MODELS = ['uniform', 'outcome_conditional', 'label_specific']
SEED = 42


def sample_truncated_dirichlet(n, K, diag_thresh, rng):
    """Sample n column-stochastic KxK matrices with min(diag) >= diag_thresh."""
    C_batch = np.empty((n, K, K))
    for col in range(K):
        U = rng.uniform(size=n)
        d = 1.0 - (1.0 - diag_thresh) * np.sqrt(1.0 - U)
        rem = 1.0 - d
        off_idx = [r for r in range(K) if r != col]
        V = rng.uniform(size=n)
        C_batch[:, col, col] = d
        C_batch[:, off_idx[0], col] = rem * V
        C_batch[:, off_idx[1], col] = rem * (1.0 - V)
    return C_batch


def renormalize_col_stochastic(C):
    """Clip negatives and renormalize columns to sum to 1."""
    C = np.maximum(C, 1e-12)
    C /= C.sum(axis=0, keepdims=True)
    return C


# ─── Perturbation models ───────────────────────────────────

def perturb_uniform(C0, eps, rng):
    """Model 1: Uniform random off-diagonal perturbation.
    Each off-diagonal entry += Uniform(-eps, eps), then renormalize.
    Returns (C_high, C_low) where C_high is for Y > median, C_low = C0.
    """
    C_high = C0.copy()
    for col in range(K):
        off_idx = [r for r in range(K) if r != col]
        noise = rng.uniform(-eps, eps, size=len(off_idx))
        for j_idx, j in enumerate(off_idx):
            C_high[j, col] += noise[j_idx]
    C_high = renormalize_col_stochastic(C_high)
    return C_high, C0.copy()


def perturb_outcome_conditional(C0, eps, rng):
    """Model 2: Systematic outcome-conditional perturbation.
    High-Y group: diagonal decreases by eps (LLM worse at extreme Y).
    Low-Y group: diagonal increases by eps (LLM better at average Y).
    Both groups perturbed symmetrically.
    """
    C_high = C0.copy()
    C_low = C0.copy()
    for col in range(K):
        off_idx = [r for r in range(K) if r != col]
        # High-Y: decrease diagonal, spread mass to off-diagonal equally
        C_high[col, col] -= eps
        for j in off_idx:
            C_high[j, col] += eps / len(off_idx)
        # Low-Y: increase diagonal, reduce off-diagonal equally
        C_low[col, col] += eps * 0.5
        for j in off_idx:
            C_low[j, col] -= eps * 0.5 / len(off_idx)
    C_high = renormalize_col_stochastic(C_high)
    C_low = renormalize_col_stochastic(C_low)
    return C_high, C_low


def perturb_label_specific(C0, eps, corr_AY, rng):
    """Model 3: Label-specific perturbation based on |corr(A=k, Y)|.
    Categories with high |corr| get HIGHER accuracy (diagonal boost).
    Categories with low |corr| get LOWER accuracy (diagonal drop).
    Only applied to high-Y group; low-Y group keeps C0.

    corr_AY: array of shape (K,) with |correlation| between A=k and Y.
    """
    C_high = C0.copy()
    corr_centered = corr_AY - corr_AY.mean()
    if np.abs(corr_centered).max() < 1e-10:
        corr_centered = rng.uniform(-1, 1, K)
        corr_centered -= corr_centered.mean()
    corr_norm = corr_centered / (np.abs(corr_centered).max() + 1e-10)

    for col in range(K):
        off_idx = [r for r in range(K) if r != col]
        # Adjust diagonal: high-corr categories get accuracy boost
        delta_diag = -eps * corr_norm[col]
        C_high[col, col] += delta_diag
        for j in off_idx:
            C_high[j, col] -= delta_diag / len(off_idx)
    C_high = renormalize_col_stochastic(C_high)
    return C_high, C0.copy()


# ─── MC estimator ──────────────────────────────────────────

def mc_trial(topology, params, C_high, C_low, N, rng):
    """Single MC trial: generate data, apply differential misclassification, estimate.

    Returns the estimated treatment effect (scalar for most, array for exposure).
    """
    gen_fn = GEN_FNS[topology]
    first_var, Y, A = gen_fn(K, N, params[topology], rng)

    y_med = np.median(Y)
    high_mask = Y > y_med

    # Apply differential misclassification
    A_star = np.empty(N, dtype=int)
    for k_true in range(K):
        idx_h = np.where(high_mask & (A == k_true))[0]
        if len(idx_h) > 0:
            A_star[idx_h] = rng.choice(K, size=len(idx_h), p=C_high[:, k_true])
        idx_l = np.where(~high_mask & (A == k_true))[0]
        if len(idx_l) > 0:
            A_star[idx_l] = rng.choice(K, size=len(idx_l), p=C_low[:, k_true])

    # Build dummy matrices
    D_star = np.zeros((N, K - 1))
    for j in range(K - 1):
        D_star[:, j] = (A_star == j + 1).astype(float)

    if topology == 'iv':
        Z = first_var
        z1 = Z == 1
        z0 = Z == 0
        if z1.sum() < 10 or z0.sum() < 10:
            return np.nan
        rf = Y[z1].mean() - Y[z0].mean()
        fs = D_star[z1, 0].mean() - D_star[z0, 0].mean()
        if abs(fs) < 1e-10:
            return np.nan
        return rf / fs
    elif topology == 'exposure':
        X = np.column_stack([np.ones(N), D_star])
        coefs = np.linalg.lstsq(X, Y, rcond=None)[0]
        return coefs  # [intercept, beta1, beta2]
    else:
        T = first_var
        X = np.column_stack([np.ones(N), T, D_star])
        coefs = np.linalg.lstsq(X, Y, rcond=None)[0]
        return coefs[1]  # treatment effect coefficient


def get_true_effect(topology, params):
    """Get the true treatment effect for comparison."""
    p = params[topology]
    if topology == 'exposure':
        return p['beta']  # [beta0, beta1, beta2]
    elif topology == 'confounding':
        return p['beta_T']
    elif topology in ('mediation', 'collider', 'mbias'):
        return p['tau']
    elif topology == 'iv':
        return p['lam']  # true causal effect
    elif topology == 'frontdoor':
        return p['lambda_U'] * p['alpha_U']  # true total effect via front-door
    return None


def classify_bias_scalar(estimate, true_val):
    """Classify bias for a scalar estimate. Returns (sign_flip, amplification)."""
    if not np.isfinite(estimate) or abs(true_val) < 1e-10:
        return False, False
    sf = (estimate * true_val < 0)
    amp = (abs(estimate) > abs(true_val)) and (estimate * true_val > 0)
    return sf, amp


def classify_bias_exposure(estimate, true_beta):
    """Classify bias for exposure (vector of coefficients)."""
    sf = False
    amp = False
    for k in [1, 2]:
        if abs(true_beta[k]) < 1e-10:
            continue
        if estimate[k] * true_beta[k] < 0:
            sf = True
        if abs(estimate[k]) > abs(true_beta[k]) and estimate[k] * true_beta[k] > 0:
            amp = True
    return sf, amp


def compute_corr_AY(topology, params, N=50000, seed=999):
    """Compute |corr(A=k, Y)| for label-specific perturbation."""
    rng = np.random.default_rng(seed)
    gen_fn = GEN_FNS[topology]
    _, Y, A = gen_fn(K, N, params[topology], rng)
    corrs = np.zeros(K)
    for k in range(K):
        Dk = (A == k).astype(float)
        if Dk.std() > 1e-10:
            corrs[k] = abs(np.corrcoef(Dk, Y)[0, 1])
    return corrs


# ─── Main experiment ───────────────────────────────────────

def run_experiment():
    rng_base = np.random.default_rng(SEED)
    params = make_dgp_params(K)

    # Precompute |corr(A=k, Y)| for each topology
    corr_AY = {}
    for topo in TOPOLOGIES:
        corr_AY[topo] = compute_corr_AY(topo, params)

    # Precompute true effects
    true_effects = {}
    for topo in TOPOLOGIES:
        true_effects[topo] = get_true_effect(topo, params)

    # Compute non-differential baseline (eps=0) via analytical plim
    baseline = {}
    for topo in TOPOLOGIES:
        st = precompute_suff_stats(K, topo, params[topo], N=500_000, seed=42)
        C_batch = sample_truncated_dirichlet(N_MATRICES, K, DIAG_THRESH,
                                              np.random.default_rng(SEED + 1))
        n_sf = 0
        n_amp = 0
        n_valid = 0
        for i in range(N_MATRICES):
            C0 = C_batch[i]
            plim = compute_plim(C0, st, K)
            if topo == 'exposure':
                if isinstance(plim, np.ndarray) and np.all(np.isfinite(plim)):
                    sf, amp = classify_bias_exposure(plim, true_effects[topo])
                    n_valid += 1
                    if sf: n_sf += 1
                    if amp: n_amp += 1
            else:
                tau_hat = extract_tau(plim, topo)
                if np.isfinite(tau_hat):
                    sf, amp = classify_bias_scalar(tau_hat, true_effects[topo])
                    n_valid += 1
                    if sf: n_sf += 1
                    if amp: n_amp += 1

        baseline[topo] = {
            'sign_flip_rate': n_sf / max(n_valid, 1),
            'amplification_rate': n_amp / max(n_valid, 1),
            'n_valid': n_valid,
        }
        print(f"  Baseline {topo}: SF={100*baseline[topo]['sign_flip_rate']:.1f}%, "
              f"Amp={100*baseline[topo]['amplification_rate']:.1f}%")

    # Main MC experiment
    results = {}
    total_start = time.time()

    for topo in TOPOLOGIES:
        results[topo] = {'baseline': baseline[topo]}
        topo_start = time.time()

        for eps in EPSILONS:
            # Pre-sample confusion matrices (same across models for fair comparison)
            C_batch = sample_truncated_dirichlet(
                N_MATRICES, K, DIAG_THRESH,
                np.random.default_rng(SEED + hash(f"{topo}_{eps}") % 100000))

            for model in MODELS:
                key = f"eps_{eps}_{model}"
                n_sf = 0
                n_amp = 0
                n_valid = 0
                biases = []

                for trial in range(N_MATRICES):
                    C0 = C_batch[trial]
                    trial_rng = np.random.default_rng(
                        SEED + trial * 997 + hash(f"{topo}_{eps}_{model}") % 100000)

                    # Generate perturbation
                    if model == 'uniform':
                        C_high, C_low = perturb_uniform(C0, eps, trial_rng)
                    elif model == 'outcome_conditional':
                        C_high, C_low = perturb_outcome_conditional(C0, eps, trial_rng)
                    elif model == 'label_specific':
                        C_high, C_low = perturb_label_specific(
                            C0, eps, corr_AY[topo], trial_rng)

                    # MC trial
                    estimate = mc_trial(topo, params, C_high, C_low, N_MC, trial_rng)

                    if topo == 'exposure':
                        if isinstance(estimate, np.ndarray) and np.all(np.isfinite(estimate)):
                            sf, amp = classify_bias_exposure(estimate, true_effects[topo])
                            n_valid += 1
                            if sf: n_sf += 1
                            if amp: n_amp += 1
                            rel_bias = np.mean(np.abs(estimate[1:] - true_effects[topo][1:]) /
                                              (np.abs(true_effects[topo][1:]) + 1e-10))
                            biases.append(rel_bias)
                    else:
                        if isinstance(estimate, (int, float, np.floating)) and np.isfinite(estimate):
                            sf, amp = classify_bias_scalar(estimate, true_effects[topo])
                            n_valid += 1
                            if sf: n_sf += 1
                            if amp: n_amp += 1
                            rel_bias = abs(estimate - true_effects[topo]) / (abs(true_effects[topo]) + 1e-10)
                            biases.append(rel_bias)

                sf_rate = n_sf / max(n_valid, 1)
                amp_rate = n_amp / max(n_valid, 1)
                mean_bias = float(np.mean(biases)) if biases else None

                results[topo][key] = {
                    'epsilon': eps,
                    'model': model,
                    'n_valid': n_valid,
                    'sign_flip_rate': round(sf_rate, 6),
                    'amplification_rate': round(amp_rate, 6),
                    'mean_relative_bias': round(mean_bias, 6) if mean_bias is not None else None,
                }

            # Progress
            elapsed = time.time() - topo_start
            print(f"  {topo} eps={eps}: "
                  + " | ".join(f"{m}: SF={100*results[topo][f'eps_{eps}_{m}']['sign_flip_rate']:.1f}%"
                              for m in MODELS)
                  + f" [{elapsed:.0f}s]")

        print(f"  {topo} done in {time.time() - topo_start:.0f}s\n")

    print(f"\nTotal: {time.time() - total_start:.0f}s")
    return results, true_effects, corr_AY


def build_summary(results):
    """Build summary table comparing models across topologies and epsilons."""
    summary = {}
    for topo in TOPOLOGIES:
        topo_summary = {'baseline': results[topo]['baseline']}
        for eps in EPSILONS:
            eps_summary = {}
            for model in MODELS:
                key = f"eps_{eps}_{model}"
                r = results[topo].get(key, {})
                eps_summary[model] = {
                    'sign_flip_rate': r.get('sign_flip_rate', None),
                    'mean_relative_bias': r.get('mean_relative_bias', None),
                }
            topo_summary[f"eps_{eps}"] = eps_summary
        summary[topo] = topo_summary
    return summary


def main():
    t0 = time.time()
    print("=" * 78)
    print("Structured Non-Differential Violation Stress Test")
    print("=" * 78)
    print(f"K={K}, N_MC={N_MC:,}, N_matrices={N_MATRICES:,}")
    print(f"Topologies: {TOPOLOGIES}")
    print(f"Models: {MODELS}")
    print(f"Epsilons: {EPSILONS}")
    print()

    results, true_effects, corr_AY = run_experiment()
    summary = build_summary(results)

    # Print comparison table
    print("\n" + "=" * 78)
    print("SUMMARY: Sign-Flip Rate by Model (exposure & IV focus)")
    print("=" * 78)
    for topo in ['exposure', 'iv']:
        bl = results[topo]['baseline']['sign_flip_rate']
        print(f"\n{topo.upper()} (baseline SF: {100*bl:.1f}%)")
        print(f"  {'eps':>6}  {'Uniform':>10}  {'OutcCond':>10}  {'LabelSpec':>10}")
        print(f"  {'-'*42}")
        for eps in EPSILONS:
            vals = []
            for m in MODELS:
                r = results[topo].get(f"eps_{eps}_{m}", {})
                vals.append(f"{100*r.get('sign_flip_rate', 0):.1f}%")
            print(f"  {eps:>6.2f}  {vals[0]:>10}  {vals[1]:>10}  {vals[2]:>10}")

    # Save results
    def to_json_safe(obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, (np.floating, np.integer)):
            return float(obj)
        if isinstance(obj, dict):
            return {k: to_json_safe(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [to_json_safe(v) for v in obj]
        return obj

    output = {
        'experiment': 'nondiff_structured_stress_test',
        'K': K,
        'N_MC': N_MC,
        'N_matrices': N_MATRICES,
        'diag_threshold': DIAG_THRESH,
        'epsilons': EPSILONS,
        'topologies': TOPOLOGIES,
        'models': MODELS,
        'true_effects': to_json_safe({t: true_effects[t] for t in TOPOLOGIES}),
        'corr_AY': to_json_safe(corr_AY),
        'results': to_json_safe(results),
        'summary': to_json_safe(summary),
        'elapsed_seconds': time.time() - t0,
    }

    out_path = os.path.join(PROJECT_ROOT, "artifacts", "nondiff_structured_stress_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")
    print(f"Total time: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
