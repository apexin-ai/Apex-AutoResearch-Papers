#!/usr/bin/env python3
"""
exp_proportional_real_matrices.py
=================================

Evaluate the proportional effects hypothesis (f = lambda * g) in the mediation
topology using 23 real LLM confusion matrices.

Mediation DGP:
  T ~ Bernoulli(0.5)
  A | T ~ softmax(gamma + delta * T)    # delta = g (treatment -> mediator)
  Y = beta[0] + sum_j beta[j]*D_j + tau*T + noise   # beta = f (mediator -> outcome)

Proportionality: f_j - f_0 = lambda * (g_j - g_0)

lambda(C) is extracted from the plim formula:
  plim(tau_hat | C) = tau_direct + (1 - lambda(C)) * tau_indirect
  => lambda(C) = 1 - (plim(tau|C) - tau_direct) / tau_indirect

Four DGP parameter groups, each with 23 real matrices x 100 random seeds:
  (a) proportional: f_j - f_0 = lambda*(g_j - g_0), lambda in {0.5, 1.0, 2.0}
  (b) near-proportional: f = lambda*g + eps, eps ~ N(0, 0.1)
  (c) non-proportional: f ~ N(0, 1) independent of g
  (d) sparse: f has 1-2 categories with effect=0, rest ~ N(0, 1)

Metrics per configuration:
  1. lambda(C) distribution (mean, median, Q05, Q95, min, max)
  2. Proportion of lambda(C) in [0, 1]
  3. Coefficient of variation between f and g (proportionality departure)
  4. Sign preservation rate (sign(tau_direct) == sign(tau_total))

Dependencies: numpy, plan_006_asv_empirical (imported via importlib)
Input:  artifacts/updated_empirical_results.json
Output: artifacts/exp_proportional_real_matrices_results.json
"""

import numpy as np
import json
import os
import sys
import time
import importlib.util

# ---------------------------------------------------------------------------
# Import plan_006 via importlib
# ---------------------------------------------------------------------------
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plan006_path = os.path.join(PROJECT_ROOT, "plan_006_asv_empirical.py")
spec = importlib.util.spec_from_file_location("plan_006_asv_empirical", plan006_path)
plan006 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plan006)

precompute_suff_stats = plan006.precompute_suff_stats
compute_plim = plan006.compute_plim
extract_tau = plan006.extract_tau

# ---------------------------------------------------------------------------
# Load real confusion matrices
# ---------------------------------------------------------------------------
def load_real_confusion_matrices():
    """Load 23 real LLM confusion matrices from artifacts."""
    ppi_path = os.path.join(PROJECT_ROOT, "artifacts", "ppi_empirical_validation.json")
    updated_path = os.path.join(PROJECT_ROOT, "artifacts", "updated_empirical_results.json")

    data = None
    for path in [ppi_path, updated_path]:
        if os.path.exists(path):
            with open(path) as f:
                d = json.load(f)
            if "confusion_matrices" in d:
                data = d
                print(f"  Loaded confusion matrices from {os.path.basename(path)}")
                break

    if data is None:
        raise FileNotFoundError("No confusion_matrices found in either JSON file")

    cm_raw = data["confusion_matrices"]
    matrices = {}
    for name, mat in cm_raw.items():
        matrices[name] = np.array(mat)
    return matrices


# ---------------------------------------------------------------------------
# Generate mediation DGP params with custom f/g structures
# ---------------------------------------------------------------------------
def make_mediation_params(K, f_vec, g_vec, tau=0.5, gamma=None):
    """
    Create mediation DGP parameters.

    Args:
        K: number of categories
        f_vec: beta coefficients (mediator -> outcome), length K
        g_vec: delta coefficients (treatment -> mediator), length K
        tau: direct treatment effect
        gamma: baseline mediator logits, length K (default: linspace)
    """
    if gamma is None:
        gamma = np.linspace(0, -0.3, K)
    return {
        "tau": tau,
        "gamma": gamma,
        "delta": g_vec,
        "beta": f_vec,
    }


def generate_proportional_params(K, lam, rng):
    """(a) Proportional: f_j - f_0 = lambda*(g_j - g_0). g from N(0,1) clipped."""
    g = rng.normal(0, 1, K)
    g = np.clip(g, -2, 2)
    g[0] = 0.0
    f = np.zeros(K)
    for j in range(1, K):
        f[j] = lam * g[j]  # f[0]=g[0]=0 so f_j - f_0 = lam*(g_j - g_0)
    return make_mediation_params(K, f, g), f, g


def generate_near_proportional_params(K, lam, rng, noise_std=0.1):
    """(b) Near-proportional: f = lambda*g + eps, eps ~ N(0, noise_std)."""
    g = rng.normal(0, 1, K)
    g = np.clip(g, -2, 2)
    g[0] = 0.0
    eps = rng.normal(0, noise_std, K)
    eps[0] = 0.0
    f = np.zeros(K)
    for j in range(1, K):
        f[j] = lam * g[j] + eps[j]
    return make_mediation_params(K, f, g), f, g


def generate_non_proportional_params(K, rng):
    """(c) Non-proportional: f ~ N(0,1) independent of g."""
    g = rng.normal(0, 1, K)
    g = np.clip(g, -2, 2)
    g[0] = 0.0
    f = rng.normal(0, 1, K)
    f[0] = 0.0
    return make_mediation_params(K, f, g), f, g


def generate_sparse_params(K, rng):
    """(d) Sparse: f has 1-2 categories with effect=0, rest from N(0,1)."""
    g = rng.normal(0, 1, K)
    g = np.clip(g, -2, 2)
    g[0] = 0.0
    f = rng.normal(0, 1, K)
    f[0] = 0.0
    non_ref = list(range(1, K))
    n_zero = min(rng.choice([1, 2]), len(non_ref))
    zero_cats = rng.choice(non_ref, size=n_zero, replace=False)
    for c in zero_cats:
        f[c] = 0.0
    return make_mediation_params(K, f, g), f, g


# ---------------------------------------------------------------------------
# Core computation: compute lambda(C) for multiple matrices given suff stats
# ---------------------------------------------------------------------------
def compute_lambda_from_suff_stats(C, K, st, tau_direct, tau_indirect):
    """
    Given precomputed suff stats (for a specific DGP), compute lambda(C).

    Args:
        C: confusion matrix (K x K)
        st: sufficient statistics from precompute_suff_stats
        tau_direct: plim(tau | I)
        tau_indirect: plim(tau | uniform) - plim(tau | I)

    Returns:
        lambda_C, tau_C
    """
    plim_C = compute_plim(C, st, K)
    tau_C = extract_tau(plim_C, "mediation")

    if not np.isfinite(tau_C) or abs(tau_indirect) < 1e-10:
        return np.nan, tau_C

    lambda_C = 1.0 - (tau_C - tau_direct) / tau_indirect
    return lambda_C, tau_C


def compute_proportionality_cv(f, g):
    """
    Coefficient of variation of f/g ratios (proportionality departure metric).
    Only for non-reference categories where |g_j| > 1e-10.
    """
    ratios = []
    for j in range(1, len(f)):
        if abs(g[j]) > 1e-10:
            ratios.append(f[j] / g[j])
    if len(ratios) < 2:
        return np.nan, ratios
    ratios = np.array(ratios)
    mean_ratio = np.mean(ratios)
    if abs(mean_ratio) < 1e-10:
        return np.nan, ratios.tolist()
    cv = np.std(ratios) / abs(mean_ratio)
    return float(cv), ratios.tolist()


def summarize_lambda_list(all_lambda_C, all_sign_preserved, all_cv, n_in_01, n_total):
    """Create summary dict from collected lambda(C) values."""
    arr = np.array(all_lambda_C) if all_lambda_C else np.array([])
    return {
        "n_samples": n_total,
        "lambda_C_stats": {
            "mean": float(np.mean(arr)) if len(arr) > 0 else None,
            "median": float(np.median(arr)) if len(arr) > 0 else None,
            "Q05": float(np.percentile(arr, 5)) if len(arr) > 0 else None,
            "Q95": float(np.percentile(arr, 95)) if len(arr) > 0 else None,
            "min": float(np.min(arr)) if len(arr) > 0 else None,
            "max": float(np.max(arr)) if len(arr) > 0 else None,
            "std": float(np.std(arr)) if len(arr) > 0 else None,
        },
        "prop_in_01": n_in_01 / max(n_total, 1),
        "proportionality_cv": {
            "mean": float(np.mean(all_cv)) if all_cv else None,
            "std": float(np.std(all_cv)) if all_cv else None,
        },
        "sign_preservation_rate": (
            float(np.mean(all_sign_preserved)) if all_sign_preserved else None
        ),
    }


# ---------------------------------------------------------------------------
# Optimized experiment loop: precompute suff_stats once per (seed, K, group),
# then evaluate across all matrices of that K.
# ---------------------------------------------------------------------------
def run_group(group_name, param_generator_fn, matrices_by_K, n_seeds, N_precomp):
    """
    Run experiment for one group.

    param_generator_fn(K, rng) -> (params_dict, f_vec, g_vec)
    """
    all_lambda_C = []
    all_sign_preserved = []
    all_cv = []
    n_total = 0
    n_in_01 = 0
    t_start = time.time()

    for K, mat_list in sorted(matrices_by_K.items()):
        for seed in range(n_seeds):
            rng = np.random.default_rng(seed * 31337 + K * 7 + hash(group_name) % 9973)
            params, f_vec, g_vec = param_generator_fn(K, rng)

            # Precompute suff stats ONCE for this (seed, K, params)
            precomp_seed = seed * 997 + K * 13
            st = precompute_suff_stats(K, "mediation", params, N=N_precomp, seed=precomp_seed)

            # Compute tau_direct and tau_total once
            plim_I = compute_plim(np.eye(K), st, K)
            tau_direct = extract_tau(plim_I, "mediation")
            C_uniform = np.ones((K, K)) / K
            plim_unif = compute_plim(C_uniform, st, K)
            tau_total = extract_tau(plim_unif, "mediation")
            tau_indirect = tau_total - tau_direct

            # CV for this f/g pair
            cv, _ = compute_proportionality_cv(f_vec, g_vec)
            cv_valid = np.isfinite(cv)

            # Evaluate across ALL matrices of this K
            for mat_name, C in mat_list:
                lam_C, tau_C = compute_lambda_from_suff_stats(
                    C, K, st, tau_direct, tau_indirect
                )
                if np.isfinite(lam_C):
                    all_lambda_C.append(lam_C)
                    n_total += 1
                    if 0 <= lam_C <= 1:
                        n_in_01 += 1
                    sign_ok = (
                        (np.sign(tau_direct) == np.sign(tau_total))
                        if (abs(tau_direct) > 1e-10 and abs(tau_total) > 1e-10)
                        else True
                    )
                    all_sign_preserved.append(sign_ok)
                    if cv_valid:
                        all_cv.append(cv)

        if (seed + 1) % 25 == 0 or seed == n_seeds - 1:
            elapsed = time.time() - t_start
            print(f"      K={K}: seed {seed+1}/{n_seeds} done ({elapsed:.1f}s)")

    summary = summarize_lambda_list(all_lambda_C, all_sign_preserved, all_cv, n_in_01, n_total)

    arr = np.array(all_lambda_C)
    print(f"    {group_name}: n={n_total}, mean={np.mean(arr):.4f}, "
          f"in[0,1]={n_in_01/max(n_total,1):.3f}, "
          f"sign={np.mean(all_sign_preserved):.3f} ({time.time()-t_start:.1f}s)")
    return summary


def run_experiment(matrices, n_seeds=100, N_precomp=500_000):
    """Run the full experiment across 4 DGP groups."""
    results = {}

    # Group matrices by K
    matrices_by_K = {}
    for name, C in matrices.items():
        K = C.shape[0]
        if K not in matrices_by_K:
            matrices_by_K[K] = []
        matrices_by_K[K].append((name, C))

    print(f"\n  Matrices by K: "
          + ", ".join(f"K={k}: {len(v)}" for k, v in sorted(matrices_by_K.items())))

    lambda_values = [0.5, 1.0, 2.0]

    # (a) Proportional
    print("\n  [a] Proportional group...")
    group_a = {}
    for lam in lambda_values:
        lam_key = f"lambda_{lam}"
        gen_fn = lambda K, rng, _lam=lam: generate_proportional_params(K, _lam, rng)
        group_a[lam_key] = run_group(
            f"prop/lam={lam}", gen_fn, matrices_by_K, n_seeds, N_precomp
        )
    results["proportional"] = group_a

    # (b) Near-proportional
    print("\n  [b] Near-proportional group...")
    group_b = {}
    for lam in lambda_values:
        lam_key = f"lambda_{lam}"
        gen_fn = lambda K, rng, _lam=lam: generate_near_proportional_params(K, _lam, rng)
        group_b[lam_key] = run_group(
            f"near/lam={lam}", gen_fn, matrices_by_K, n_seeds, N_precomp
        )
    results["near_proportional"] = group_b

    # (c) Non-proportional
    print("\n  [c] Non-proportional group...")
    gen_fn_c = lambda K, rng: generate_non_proportional_params(K, rng)
    results["non_proportional"] = run_group(
        "non-prop", gen_fn_c, matrices_by_K, n_seeds, N_precomp
    )

    # (d) Sparse
    print("\n  [d] Sparse group...")
    gen_fn_d = lambda K, rng: generate_sparse_params(K, rng)
    results["sparse"] = run_group(
        "sparse", gen_fn_d, matrices_by_K, n_seeds, N_precomp
    )

    return results


# ---------------------------------------------------------------------------
# Per-K breakdown analysis
# ---------------------------------------------------------------------------
def run_per_K_breakdown(matrices, n_seeds=100, N_precomp=500_000):
    """Per-K analysis with proportional lambda=1.0 to see dimension effects."""
    matrices_by_K = {}
    for name, C in matrices.items():
        K = C.shape[0]
        if K not in matrices_by_K:
            matrices_by_K[K] = []
        matrices_by_K[K].append((name, C))

    breakdown = {}
    for K, mat_list in sorted(matrices_by_K.items()):
        print(f"\n  K={K} ({len(mat_list)} matrices)...")
        single_K = {K: mat_list}
        gen_fn = lambda K_, rng: generate_proportional_params(K_, 1.0, rng)
        summary = run_group(f"perK/K={K}", gen_fn, single_K, n_seeds, N_precomp)
        summary["n_matrices"] = len(mat_list)
        breakdown[f"K={K}"] = summary
    return breakdown


# ---------------------------------------------------------------------------
# Per-matrix analysis: show lambda(C) by individual confusion matrix
# ---------------------------------------------------------------------------
def run_per_matrix_analysis(matrices, n_seeds=50, N_precomp=500_000):
    """For each real matrix, compute mean lambda(C) under proportional lambda=1.0."""
    per_mat = {}
    for name, C in sorted(matrices.items()):
        K = C.shape[0]
        lambdas = []
        for seed in range(n_seeds):
            rng = np.random.default_rng(seed * 31337 + K * 7 + 42)
            params, f_vec, g_vec = generate_proportional_params(K, 1.0, rng)
            precomp_seed = seed * 997 + K * 13
            st = precompute_suff_stats(K, "mediation", params, N=N_precomp, seed=precomp_seed)
            plim_I = compute_plim(np.eye(K), st, K)
            tau_direct = extract_tau(plim_I, "mediation")
            C_uniform = np.ones((K, K)) / K
            plim_unif = compute_plim(C_uniform, st, K)
            tau_total = extract_tau(plim_unif, "mediation")
            tau_indirect = tau_total - tau_direct
            lam_C, _ = compute_lambda_from_suff_stats(C, K, st, tau_direct, tau_indirect)
            if np.isfinite(lam_C):
                lambdas.append(lam_C)

        arr = np.array(lambdas)
        diag_mean = float(np.diag(C).mean())
        per_mat[name] = {
            "K": K,
            "diag_mean": diag_mean,
            "n_samples": len(arr),
            "mean_lambda_C": float(np.mean(arr)) if len(arr) > 0 else None,
            "std_lambda_C": float(np.std(arr)) if len(arr) > 0 else None,
            "median_lambda_C": float(np.median(arr)) if len(arr) > 0 else None,
        }
        print(f"    {name}: K={K}, diag={diag_mean:.3f}, "
              f"mean_lam(C)={np.mean(arr):.4f} +/- {np.std(arr):.4f}")
    return per_mat


# ---------------------------------------------------------------------------
# JSON-safe serialization
# ---------------------------------------------------------------------------
def to_json_safe(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        v = float(obj)
        return None if (np.isnan(v) or np.isinf(v)) else v
    elif isinstance(obj, np.ndarray):
        return to_json_safe(obj.tolist())
    elif isinstance(obj, (np.bool_, bool)):
        return bool(obj)
    elif isinstance(obj, dict):
        return {str(k): to_json_safe(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [to_json_safe(v) for v in obj]
    elif isinstance(obj, float):
        return None if (np.isnan(obj) or np.isinf(obj)) else obj
    return obj


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()
    print("=" * 70)
    print("exp_proportional_real_matrices: Proportional effects evaluation")
    print("=" * 70)

    # Load confusion matrices
    print("\n[1/5] Loading real LLM confusion matrices...")
    matrices = load_real_confusion_matrices()
    print(f"  {len(matrices)} matrices loaded")
    for name, C in sorted(matrices.items()):
        K = C.shape[0]
        print(f"    {name}: K={K}, diag_mean={np.diag(C).mean():.3f}")

    N_PRECOMP = 100_000
    N_SEEDS = 50

    # Main experiment
    print(f"\n[2/5] Main experiment (N_precomp={N_PRECOMP}, n_seeds={N_SEEDS})...")
    results = run_experiment(matrices, n_seeds=N_SEEDS, N_precomp=N_PRECOMP)

    # Per-K breakdown
    print(f"\n[3/5] Per-K breakdown (proportional lambda=1.0)...")
    per_K = run_per_K_breakdown(matrices, n_seeds=N_SEEDS, N_precomp=N_PRECOMP)
    results["per_K_breakdown"] = per_K

    # Per-matrix analysis
    print(f"\n[4/5] Per-matrix analysis (proportional lambda=1.0, n_seeds=50)...")
    per_mat = run_per_matrix_analysis(matrices, n_seeds=50, N_precomp=N_PRECOMP)
    results["per_matrix"] = per_mat

    # Summary table
    print(f"\n[5/5] Summary")
    print("-" * 90)
    fmt = f"{'Group':<30} {'Mean':>8} {'Median':>8} {'Q05':>8} {'Q95':>8} {'In[0,1]':>8} {'SignPres':>8}"
    print(fmt)
    print("-" * 90)

    for group_name in ["proportional", "near_proportional", "non_proportional", "sparse"]:
        group_data = results[group_name]
        if isinstance(group_data, dict) and "lambda_C_stats" in group_data:
            s = group_data["lambda_C_stats"]
            print(f"  {group_name:<28} {s['mean']:>8.4f} {s['median']:>8.4f} "
                  f"{s['Q05']:>8.4f} {s['Q95']:>8.4f} "
                  f"{group_data['prop_in_01']:>8.3f} "
                  f"{group_data['sign_preservation_rate']:>8.3f}")
        else:
            for lam_key, entry in group_data.items():
                s = entry["lambda_C_stats"]
                label = f"{group_name}/{lam_key}"
                print(f"  {label:<28} {s['mean']:>8.4f} {s['median']:>8.4f} "
                      f"{s['Q05']:>8.4f} {s['Q95']:>8.4f} "
                      f"{entry['prop_in_01']:>8.3f} "
                      f"{entry['sign_preservation_rate']:>8.3f}")

    print("-" * 90)

    print("\n  Per-K breakdown (proportional, lambda=1.0):")
    for k_label, k_data in per_K.items():
        s = k_data["lambda_C_stats"]
        print(f"    {k_label}: mean={s['mean']:.4f}, median={s['median']:.4f}, "
              f"[Q05,Q95]=[{s['Q05']:.4f}, {s['Q95']:.4f}], "
              f"in[0,1]={k_data['prop_in_01']:.3f}")

    # Metadata
    results["meta"] = {
        "n_matrices": len(matrices),
        "n_seeds": N_SEEDS,
        "N_precomp": N_PRECOMP,
        "topology": "mediation",
        "matrix_names": sorted(matrices.keys()),
        "elapsed_seconds": time.time() - t0,
    }

    # Save
    out_path = os.path.join(PROJECT_ROOT, "artifacts",
                            "exp_proportional_real_matrices_results.json")
    with open(out_path, "w") as f:
        json.dump(to_json_safe(results), f, indent=2)
    print(f"\nResults saved to {out_path}")
    print(f"Total time: {time.time() - t0:.1f}s ({(time.time() - t0) / 60:.1f}min)")
    print("=" * 70)


if __name__ == "__main__":
    main()
