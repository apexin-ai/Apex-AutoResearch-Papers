#!/usr/bin/env python3
"""
Exp: Primary Coefficient Sign Reversal Analysis for Exposure Topology

For the exposure topology with K=3, the OLS regression is:
    Y = β₀ + β₁·1[A*=1] + β₂·1[A*=2] + ε

The paper claims "the primary coefficient never reverses sign" based on
empirical LLM confusion matrices.  This script verifies that claim
systematically by:

1. Varying the β₁/β₂ ratio (from equal to highly imbalanced)
2. For each ratio, sampling 100,000 Dirichlet(1,1,1) confusion matrices
3. Computing the analytical probability limit of each coefficient
4. Checking sign reversal for the PRIMARY coefficient (the largest |βₖ|)
   vs SECONDARY coefficients
5. Also checking with a "realistic" filter: diagonal ≥ 0.7

Output: artifacts/exp_primary_coeff_breakdown_results.json

Key imports from plan_006_asv_empirical.py:
  - make_dgp_params(K): generates DGP parameters
  - precompute_suff_stats(K, topo, params): precomputes sufficient statistics
  - compute_plim(C, suff_stats, K): analytical probability limit given C
"""

import numpy as np
import json
import time
import sys
import os

# Add project root to path so we can import from plan_006
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from plan_006_asv_empirical import (
    make_dgp_params,
    precompute_suff_stats,
    compute_plim,
    make_p_A,
)

# ============================================================================
# Configuration
# ============================================================================

K = 3
N_MATRICES = 100_000
BETA_RATIOS = [1.0, 1.5, 2.0, 5.0, 10.0, 50.0]
DIAG_THRESHOLD = 0.7  # "realistic" confusion matrix filter
N_PRECOMP = 2_000_000
SEED = 2026


# ============================================================================
# Core Analysis
# ============================================================================

def make_exposure_params_custom(K, beta_vec, p_A):
    """Create exposure DGP params with a custom beta vector."""
    return {
        'beta': np.array(beta_vec),
        'p_A': p_A,
    }


def sample_dirichlet_confusion_matrices(K, n_matrices, rng):
    """
    Sample n_matrices confusion matrices where each column is drawn
    independently from Dirichlet(1,1,...,1) (uniform over the simplex).

    Returns: array of shape (n_matrices, K, K)
    """
    # Each column j of C is drawn from Dirichlet(alpha=[1]*K)
    # Shape: (n_matrices, K, K) where C[:, :, j] are the columns
    alpha = np.ones(K)
    matrices = np.zeros((n_matrices, K, K))
    for j in range(K):
        # Draw n_matrices columns from Dirichlet
        matrices[:, :, j] = rng.dirichlet(alpha, size=n_matrices)
    return matrices


def analyze_single_ratio(ratio, rng, verbose=True):
    """
    For a given β₁/β₂ ratio, compute sign-flip statistics.

    β = [0.0, β₁, β₂] where β₁ = 1.0 and β₂ = 1.0/ratio.
    The primary coefficient is β₁ (index 1 in the plim vector).
    The secondary coefficient is β₂ (index 2 in the plim vector).

    Returns a dict with sign-flip counts and rates.
    """
    beta_1 = 1.0
    beta_2 = 1.0 / ratio
    beta_vec = [0.0, beta_1, beta_2]
    p_A = make_p_A(K)

    # Create custom exposure params
    exp_params = make_exposure_params_custom(K, beta_vec, p_A)

    # Precompute sufficient statistics with these params
    suff_stats = precompute_suff_stats(
        K, 'exposure', exp_params, N=N_PRECOMP, seed=int(ratio * 1000) % 99999
    )

    # Verify: plim with identity C should recover true beta
    plim_identity = compute_plim(np.eye(K), suff_stats, K)
    if verbose:
        print(f"  True β = {beta_vec}")
        print(f"  Plim(I) = {plim_identity}")

    # Sample confusion matrices
    C_all = sample_dirichlet_confusion_matrices(K, N_MATRICES, rng)

    # Counters
    primary_sign_flip_all = 0
    secondary_sign_flip_all = 0
    any_sign_flip_all = 0
    primary_sign_flip_diag = 0
    secondary_sign_flip_diag = 0
    any_sign_flip_diag = 0
    n_valid_all = 0
    n_valid_diag = 0
    n_diag_pass = 0

    # Track worst-case (most negative primary plim)
    worst_primary_plim = float('inf')
    worst_primary_C = None
    worst_secondary_plim = float('inf')
    worst_secondary_C = None

    # Collect plim values for summary stats
    primary_plims = []
    secondary_plims = []

    for i in range(N_MATRICES):
        C = C_all[i]

        # Compute plim: returns [intercept, coeff_1, coeff_2] for exposure
        plim_vec = compute_plim(C, suff_stats, K)

        if isinstance(plim_vec, float) or not np.all(np.isfinite(plim_vec)):
            continue

        n_valid_all += 1

        # plim_vec layout for exposure: [β₀_hat, β₁_hat, β₂_hat]
        # True signs: β₁ = 1.0 > 0, β₂ = 1.0/ratio > 0
        beta1_hat = plim_vec[1]  # primary coefficient
        beta2_hat = plim_vec[2]  # secondary coefficient

        primary_plims.append(beta1_hat)
        secondary_plims.append(beta2_hat)

        # Check sign reversal (true signs are both positive)
        primary_flipped = (beta1_hat < 0)
        secondary_flipped = (beta2_hat < 0)

        if primary_flipped:
            primary_sign_flip_all += 1
            if beta1_hat < worst_primary_plim:
                worst_primary_plim = beta1_hat
                worst_primary_C = C.copy()
        if secondary_flipped:
            secondary_sign_flip_all += 1
            if beta2_hat < worst_secondary_plim:
                worst_secondary_plim = beta2_hat
                worst_secondary_C = C.copy()
        if primary_flipped or secondary_flipped:
            any_sign_flip_all += 1

        # Check with diagonal threshold
        min_diag = np.min(np.diag(C))
        if min_diag >= DIAG_THRESHOLD:
            n_diag_pass += 1
            n_valid_diag += 1
            if primary_flipped:
                primary_sign_flip_diag += 1
            if secondary_flipped:
                secondary_sign_flip_diag += 1
            if primary_flipped or secondary_flipped:
                any_sign_flip_diag += 1

    primary_plims = np.array(primary_plims)
    secondary_plims = np.array(secondary_plims)

    result = {
        'ratio': ratio,
        'beta': beta_vec,
        'n_matrices': N_MATRICES,
        'n_valid_all': n_valid_all,
        'n_diag_pass': n_diag_pass,
        # All matrices
        'primary_sign_flip_all': primary_sign_flip_all,
        'primary_sign_flip_rate_all': primary_sign_flip_all / max(n_valid_all, 1),
        'secondary_sign_flip_all': secondary_sign_flip_all,
        'secondary_sign_flip_rate_all': secondary_sign_flip_all / max(n_valid_all, 1),
        'any_sign_flip_all': any_sign_flip_all,
        'any_sign_flip_rate_all': any_sign_flip_all / max(n_valid_all, 1),
        # Diagonal >= 0.7
        'primary_sign_flip_diag': primary_sign_flip_diag,
        'primary_sign_flip_rate_diag': (
            primary_sign_flip_diag / max(n_valid_diag, 1) if n_valid_diag > 0 else None
        ),
        'secondary_sign_flip_diag': secondary_sign_flip_diag,
        'secondary_sign_flip_rate_diag': (
            secondary_sign_flip_diag / max(n_valid_diag, 1) if n_valid_diag > 0 else None
        ),
        'any_sign_flip_diag': any_sign_flip_diag,
        'any_sign_flip_rate_diag': (
            any_sign_flip_diag / max(n_valid_diag, 1) if n_valid_diag > 0 else None
        ),
        # Summary statistics on plim values
        'primary_plim_stats': {
            'mean': float(np.mean(primary_plims)) if len(primary_plims) > 0 else None,
            'std': float(np.std(primary_plims)) if len(primary_plims) > 0 else None,
            'min': float(np.min(primary_plims)) if len(primary_plims) > 0 else None,
            'p5': float(np.percentile(primary_plims, 5)) if len(primary_plims) > 0 else None,
            'p25': float(np.percentile(primary_plims, 25)) if len(primary_plims) > 0 else None,
            'median': float(np.median(primary_plims)) if len(primary_plims) > 0 else None,
            'p75': float(np.percentile(primary_plims, 75)) if len(primary_plims) > 0 else None,
            'p95': float(np.percentile(primary_plims, 95)) if len(primary_plims) > 0 else None,
            'max': float(np.max(primary_plims)) if len(primary_plims) > 0 else None,
        },
        'secondary_plim_stats': {
            'mean': float(np.mean(secondary_plims)) if len(secondary_plims) > 0 else None,
            'std': float(np.std(secondary_plims)) if len(secondary_plims) > 0 else None,
            'min': float(np.min(secondary_plims)) if len(secondary_plims) > 0 else None,
            'p5': float(np.percentile(secondary_plims, 5)) if len(secondary_plims) > 0 else None,
            'p25': float(np.percentile(secondary_plims, 25)) if len(secondary_plims) > 0 else None,
            'median': float(np.median(secondary_plims)) if len(secondary_plims) > 0 else None,
            'p75': float(np.percentile(secondary_plims, 75)) if len(secondary_plims) > 0 else None,
            'p95': float(np.percentile(secondary_plims, 95)) if len(secondary_plims) > 0 else None,
            'max': float(np.max(secondary_plims)) if len(secondary_plims) > 0 else None,
        },
        # Worst cases
        'worst_primary_plim': (
            float(worst_primary_plim) if worst_primary_plim != float('inf') else None
        ),
        'worst_primary_C': (
            worst_primary_C.tolist() if worst_primary_C is not None else None
        ),
        'worst_secondary_plim': (
            float(worst_secondary_plim) if worst_secondary_plim != float('inf') else None
        ),
        'worst_secondary_C': (
            worst_secondary_C.tolist() if worst_secondary_C is not None else None
        ),
    }

    return result


# ============================================================================
# Main
# ============================================================================

def main():
    t_start = time.time()
    print("=" * 70)
    print("Primary Coefficient Sign Reversal Analysis — Exposure Topology K=3")
    print(f"  N_MATRICES = {N_MATRICES:,}")
    print(f"  β₁/β₂ ratios = {BETA_RATIOS}")
    print(f"  Diagonal threshold = {DIAG_THRESHOLD}")
    print("=" * 70)

    rng = np.random.default_rng(SEED)
    results = []

    for ratio in BETA_RATIOS:
        t_ratio = time.time()
        print(f"\n--- Ratio β₁/β₂ = {ratio} ---")
        res = analyze_single_ratio(ratio, rng, verbose=True)
        elapsed = time.time() - t_ratio
        print(f"  Valid matrices: {res['n_valid_all']:,} / {N_MATRICES:,}")
        print(f"  Diagonal >= {DIAG_THRESHOLD}: {res['n_diag_pass']:,}")
        print(f"  [ALL]  Primary sign-flip:   {res['primary_sign_flip_all']:>6,} "
              f"({res['primary_sign_flip_rate_all']:.4%})")
        print(f"  [ALL]  Secondary sign-flip:  {res['secondary_sign_flip_all']:>6,} "
              f"({res['secondary_sign_flip_rate_all']:.4%})")
        print(f"  [ALL]  Any sign-flip:        {res['any_sign_flip_all']:>6,} "
              f"({res['any_sign_flip_rate_all']:.4%})")
        if res['n_diag_pass'] > 0:
            print(f"  [DIAG] Primary sign-flip:   {res['primary_sign_flip_diag']:>6,} "
                  f"({res['primary_sign_flip_rate_diag']:.4%})")
            print(f"  [DIAG] Secondary sign-flip:  {res['secondary_sign_flip_diag']:>6,} "
                  f"({res['secondary_sign_flip_rate_diag']:.4%})")
        print(f"  Primary plim:  mean={res['primary_plim_stats']['mean']:.4f}, "
              f"min={res['primary_plim_stats']['min']:.4f}, "
              f"p5={res['primary_plim_stats']['p5']:.4f}")
        print(f"  Secondary plim: mean={res['secondary_plim_stats']['mean']:.4f}, "
              f"min={res['secondary_plim_stats']['min']:.4f}, "
              f"p5={res['secondary_plim_stats']['p5']:.4f}")
        print(f"  Time: {elapsed:.1f}s")
        results.append(res)

    # ========================================================================
    # Summary table
    # ========================================================================
    print("\n" + "=" * 70)
    print("SUMMARY TABLE")
    print("=" * 70)
    header = (f"{'Ratio':>6} | {'β':>18} | "
              f"{'Pri flip (all)':>14} | {'Sec flip (all)':>14} | "
              f"{'Pri flip (diag)':>15} | {'Sec flip (diag)':>15}")
    print(header)
    print("-" * len(header))
    for res in results:
        beta_str = f"[0, 1.0, {1.0/res['ratio']:.3f}]"
        pri_all = f"{res['primary_sign_flip_rate_all']:.4%}"
        sec_all = f"{res['secondary_sign_flip_rate_all']:.4%}"
        pri_diag = (f"{res['primary_sign_flip_rate_diag']:.4%}"
                    if res['primary_sign_flip_rate_diag'] is not None else "N/A")
        sec_diag = (f"{res['secondary_sign_flip_rate_diag']:.4%}"
                    if res['secondary_sign_flip_rate_diag'] is not None else "N/A")
        print(f"{res['ratio']:>6.1f} | {beta_str:>18} | "
              f"{pri_all:>14} | {sec_all:>14} | "
              f"{pri_diag:>15} | {sec_diag:>15}")

    # ========================================================================
    # Key finding
    # ========================================================================
    print("\n" + "=" * 70)
    print("KEY FINDINGS")
    print("=" * 70)

    any_primary_flip_all = any(r['primary_sign_flip_all'] > 0 for r in results)
    any_primary_flip_diag = any(
        r['primary_sign_flip_diag'] > 0 for r in results
        if r['n_diag_pass'] > 0
    )
    any_secondary_flip_all = any(r['secondary_sign_flip_all'] > 0 for r in results)

    if not any_primary_flip_all:
        print("  [CONFIRMED] Primary coefficient NEVER reverses sign across ALL matrices")
    else:
        max_rate = max(r['primary_sign_flip_rate_all'] for r in results)
        print(f"  [VIOLATED] Primary coefficient CAN reverse sign (max rate: {max_rate:.4%})")

    if not any_primary_flip_diag:
        print("  [CONFIRMED] Primary coefficient NEVER reverses sign for diag >= 0.7")
    else:
        max_rate = max(
            r['primary_sign_flip_rate_diag'] for r in results
            if r['primary_sign_flip_rate_diag'] is not None
        )
        print(f"  [VIOLATED] Primary coefficient CAN reverse sign at diag >= 0.7 "
              f"(max rate: {max_rate:.4%})")

    if any_secondary_flip_all:
        max_rate = max(r['secondary_sign_flip_rate_all'] for r in results)
        max_ratio = max(results, key=lambda r: r['secondary_sign_flip_rate_all'])['ratio']
        print(f"  Secondary coefficient DOES reverse sign (max rate: {max_rate:.4%} "
              f"at ratio={max_ratio})")
    else:
        print("  Secondary coefficient also never reverses sign")

    # ========================================================================
    # Save results
    # ========================================================================
    output_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'exp_primary_coeff_breakdown_results.json'
    )

    # Clean results for JSON serialization
    def clean_for_json(obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            v = float(obj)
            return None if (np.isnan(v) or np.isinf(v)) else v
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {str(k): clean_for_json(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [clean_for_json(v) for v in obj]
        elif isinstance(obj, (bool, np.bool_)):
            return bool(obj)
        elif isinstance(obj, float):
            return None if (np.isnan(obj) or np.isinf(obj)) else obj
        return obj

    output_data = clean_for_json({
        'config': {
            'K': K,
            'n_matrices': N_MATRICES,
            'beta_ratios': BETA_RATIOS,
            'diag_threshold': DIAG_THRESHOLD,
            'n_precomp': N_PRECOMP,
            'seed': SEED,
        },
        'results': results,
        'summary': {
            'primary_ever_flips_all': any_primary_flip_all,
            'primary_ever_flips_diag': any_primary_flip_diag,
            'secondary_ever_flips_all': any_secondary_flip_all,
        },
    })

    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=2)
    print(f"\nResults saved to {output_path}")

    total_time = time.time() - t_start
    print(f"Total time: {total_time:.1f}s ({total_time / 60:.1f}min)")


if __name__ == '__main__':
    main()
