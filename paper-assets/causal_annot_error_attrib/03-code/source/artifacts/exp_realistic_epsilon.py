#!/usr/bin/env python3
"""
exp_realistic_epsilon.py — Estimate realistic differential misclassification
ε thresholds for 23 LLM configurations.

For each empirical confusion matrix C (from updated_empirical_results.json),
we sweep ε ∈ [0, 0.50] and run Monte Carlo trials to estimate the sign
reversal rate under Y-stratified differential misclassification:
    C_high = renormalize(C + ε * Δ)   (applied to Y > median stratum)
    C_low  = renormalize(C - ε * Δ)   (applied to Y ≤ median stratum)
where Δ is a random off-diagonal perturbation matrix.

The "safe ε threshold" is the max ε where sign reversal rate < 5%.

Input:  artifacts/updated_empirical_results.json  (23 confusion matrices)
Output: artifacts/exp_realistic_epsilon_results.json

Dependencies: numpy, plan_006_asv_empirical.py (for DGP + plim functions)
"""

import numpy as np
import json
import time
import sys
import importlib.util
from pathlib import Path

# ---------------------------------------------------------------------------
# Import plan_006 for DGP / plim infrastructure
# ---------------------------------------------------------------------------
PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
sys.path.insert(0, str(PROJ))
spec = importlib.util.spec_from_file_location("plan_006", str(PROJ / "plan_006_asv_empirical.py"))
plan_006 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plan_006)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
N_EPSILON = 51                 # ε grid points
EPSILON_MAX = 0.50             # max ε
N_MC = 500                     # Monte Carlo trials per ε
SIGN_REVERSAL_THRESHOLD = 0.05 # 5% threshold
TOPOLOGY = "exposure"          # use exposure topology
N_PRECOMP = 2_000_000          # samples for sufficient statistics


def renormalize_columns(M):
    """Renormalize columns of M to be non-negative and sum to 1 (column-stochastic)."""
    M = np.maximum(M, 0.0)
    col_sums = M.sum(axis=0)
    col_sums = np.where(col_sums < 1e-12, 1.0, col_sums)
    return M / col_sums


def generate_delta(K, rng):
    """Generate a random off-diagonal perturbation matrix Δ.

    Off-diagonal entries are drawn from Uniform(-1, 1).
    Diagonal entries are set so each column sums to 0.
    Then the whole matrix is normalized to have unit Frobenius norm.
    """
    Delta = rng.uniform(-1, 1, size=(K, K))
    # Zero out diagonal, then set diagonal so columns sum to 0
    np.fill_diagonal(Delta, 0.0)
    for j in range(K):
        Delta[j, j] = -Delta[:, j].sum()
    # Normalize to unit Frobenius norm for consistent scaling
    norm = np.linalg.norm(Delta, 'fro')
    if norm > 1e-12:
        Delta /= norm
    return Delta


def is_valid_stochastic(M):
    """Check if M is a valid column-stochastic matrix (non-negative, cols sum to ~1)."""
    return np.all(M >= -1e-10) and np.allclose(M.sum(axis=0), 1.0, atol=1e-6)


def check_sign_reversal(plim_perturbed, plim_identity, K):
    """Check if any exposure coefficient has a sign reversal.

    For exposure topology, plim returns [intercept, beta_1, ..., beta_{K-1}].
    We check indices 1..K-1 (the exposure coefficients, excluding intercept).
    """
    if plim_perturbed is None or plim_identity is None:
        return False
    if not isinstance(plim_perturbed, np.ndarray) or not isinstance(plim_identity, np.ndarray):
        return False
    if np.any(~np.isfinite(plim_perturbed)) or np.any(~np.isfinite(plim_identity)):
        return False

    # Check coefficients at indices 1..K-1
    for idx in range(1, K):
        true_val = plim_identity[idx]
        pert_val = plim_perturbed[idx]
        # Only count reversal if the true coefficient is meaningfully non-zero
        if abs(true_val) > 1e-8 and np.sign(true_val) != np.sign(pert_val):
            return True
    return False


def run_epsilon_sweep_for_config(C, K, suff_stats, plim_identity, epsilons, n_mc, rng):
    """Sweep ε values for a single confusion matrix.

    For each ε, run n_mc Monte Carlo trials:
      1. Generate random Δ
      2. Construct C_high = renormalize(C + ε*Δ), C_low = renormalize(C - ε*Δ)
      3. Check validity
      4. Compute plim under each, average them
      5. Check for sign reversal vs identity plim

    Returns: dict of {ε: sign_reversal_rate}
    """
    results = {}
    for eps in epsilons:
        if eps < 1e-12:
            results[float(eps)] = 0.0
            continue

        n_reversal = 0
        n_valid = 0

        for _ in range(n_mc):
            Delta = generate_delta(K, rng)

            C_high_raw = C + eps * Delta
            C_low_raw = C - eps * Delta

            # Renormalize to valid stochastic matrices
            C_high = renormalize_columns(C_high_raw)
            C_low = renormalize_columns(C_low_raw)

            # Skip if either matrix has substantial negative entries before clipping
            # (renormalize_columns clips to 0, but if too many entries were negative,
            # the matrix is unrealistic)
            if np.any(C_high_raw < -0.1) or np.any(C_low_raw < -0.1):
                continue

            n_valid += 1

            # Compute plim under each confusion matrix
            plim_high = plan_006.compute_plim(C_high, suff_stats, K)
            plim_low = plan_006.compute_plim(C_low, suff_stats, K)

            if plim_high is None or plim_low is None:
                continue
            if not isinstance(plim_high, np.ndarray) or not isinstance(plim_low, np.ndarray):
                continue
            if np.any(~np.isfinite(plim_high)) or np.any(~np.isfinite(plim_low)):
                continue

            # Average plim across the two strata
            plim_avg = 0.5 * plim_high + 0.5 * plim_low

            if check_sign_reversal(plim_avg, plim_identity, K):
                n_reversal += 1

        rate = n_reversal / max(n_valid, 1) if n_valid > 0 else 0.0
        results[float(eps)] = rate

    return results


def find_safe_threshold(reversal_rates, epsilons):
    """Find max ε where sign reversal rate < threshold (5%).

    Returns the safe threshold, or the max ε if always safe.
    """
    safe_eps = 0.0
    for eps in epsilons:
        rate = reversal_rates.get(float(eps), 0.0)
        if rate < SIGN_REVERSAL_THRESHOLD:
            safe_eps = float(eps)
        else:
            break  # once it exceeds threshold, stop
    return safe_eps


def main():
    t_start = time.time()

    # ---- Load confusion matrices ----
    data_path = PROJ / "artifacts" / "updated_empirical_results.json"
    print(f"Loading confusion matrices from {data_path}")
    with open(data_path) as f:
        data = json.load(f)

    cm_dict = data["confusion_matrices"]
    config_meta = data.get("config_meta", {})
    print(f"  {len(cm_dict)} configurations loaded")

    # ---- Parse configs ----
    configs = {}
    for name, mat in cm_dict.items():
        C = np.array(mat)
        K = C.shape[0]
        configs[name] = {"C": C, "K": K}
        # Infer dataset from name
        if name.startswith("civil_comments"):
            configs[name]["dataset"] = "civil_comments"
        elif name.startswith("humaid"):
            configs[name]["dataset"] = "humaid"
        elif name.startswith("vast"):
            configs[name]["dataset"] = "vast"

    # ---- Precompute sufficient statistics for each K ----
    K_values = sorted(set(cfg["K"] for cfg in configs.values()))
    print(f"  K values: {K_values}")

    suff_stats_by_K = {}
    plim_identity_by_K = {}
    for K in K_values:
        print(f"  Precomputing suff stats for K={K}...")
        params = plan_006.make_dgp_params(K)
        seed = K * 1000 + 42
        st = plan_006.precompute_suff_stats(
            K, TOPOLOGY, params[TOPOLOGY], N=N_PRECOMP, seed=seed
        )
        suff_stats_by_K[K] = st

        plim_I = plan_006.compute_plim(np.eye(K), st, K)
        plim_identity_by_K[K] = plim_I
        print(f"    plim(I) = {plim_I}")

    # ---- Epsilon grid ----
    epsilons = np.linspace(0, EPSILON_MAX, N_EPSILON)
    print(f"\nε grid: {N_EPSILON} points in [0, {EPSILON_MAX}]")
    print(f"Monte Carlo trials per ε: {N_MC}")
    print(f"Sign reversal threshold: {SIGN_REVERSAL_THRESHOLD * 100:.0f}%")

    # ---- Run sweep for each config ----
    all_results = {}
    safe_thresholds = {}
    rng = np.random.default_rng(seed=2026)

    for i, (name, cfg) in enumerate(configs.items()):
        C = cfg["C"]
        K = cfg["K"]
        st = suff_stats_by_K[K]
        plim_I = plim_identity_by_K[K]

        t0 = time.time()
        reversal_rates = run_epsilon_sweep_for_config(
            C, K, st, plim_I, epsilons, N_MC, rng
        )
        safe_eps = find_safe_threshold(reversal_rates, epsilons)
        elapsed = time.time() - t0

        all_results[name] = {
            "K": K,
            "dataset": cfg.get("dataset", "unknown"),
            "diag_mean": float(np.diag(C).mean()),
            "reversal_rates": {f"{e:.4f}": r for e, r in reversal_rates.items()},
            "safe_epsilon_threshold": safe_eps,
        }
        safe_thresholds[name] = safe_eps

        # Print progress
        print(f"  [{i+1:2d}/{len(configs)}] {name:<45s} K={K:>2d}  "
              f"diag={np.diag(C).mean():.3f}  safe_ε={safe_eps:.4f}  ({elapsed:.1f}s)")

    # ---- Summary statistics ----
    thresholds = list(safe_thresholds.values())
    thresholds_arr = np.array(thresholds)

    summary = {
        "n_configs": len(thresholds),
        "mean": float(np.mean(thresholds_arr)),
        "median": float(np.median(thresholds_arr)),
        "min": float(np.min(thresholds_arr)),
        "max": float(np.max(thresholds_arr)),
        "Q05": float(np.percentile(thresholds_arr, 5)),
        "Q95": float(np.percentile(thresholds_arr, 95)),
        "std": float(np.std(thresholds_arr)),
    }

    # Per-dataset summary
    per_dataset = {}
    for dataset in ["civil_comments", "vast", "humaid"]:
        ds_thresholds = [
            v for name, v in safe_thresholds.items()
            if configs[name].get("dataset") == dataset
        ]
        if ds_thresholds:
            ds_arr = np.array(ds_thresholds)
            per_dataset[dataset] = {
                "n_configs": len(ds_thresholds),
                "mean": float(np.mean(ds_arr)),
                "median": float(np.median(ds_arr)),
                "min": float(np.min(ds_arr)),
                "max": float(np.max(ds_arr)),
            }

    # Per-K summary
    per_K = {}
    for K in K_values:
        k_thresholds = [
            v for name, v in safe_thresholds.items()
            if configs[name]["K"] == K
        ]
        if k_thresholds:
            k_arr = np.array(k_thresholds)
            per_K[str(K)] = {
                "n_configs": len(k_thresholds),
                "mean": float(np.mean(k_arr)),
                "median": float(np.median(k_arr)),
                "min": float(np.min(k_arr)),
                "max": float(np.max(k_arr)),
            }

    # ---- Print summary ----
    print("\n" + "=" * 70)
    print("SUMMARY: Safe ε thresholds (sign reversal < 5%)")
    print("=" * 70)
    print(f"  N configs:  {summary['n_configs']}")
    print(f"  Mean:       {summary['mean']:.4f}")
    print(f"  Median:     {summary['median']:.4f}")
    print(f"  Min:        {summary['min']:.4f}")
    print(f"  Max:        {summary['max']:.4f}")
    print(f"  Q05:        {summary['Q05']:.4f}")
    print(f"  Q95:        {summary['Q95']:.4f}")
    print(f"  Std:        {summary['std']:.4f}")

    print("\nPer-dataset:")
    for ds, s in per_dataset.items():
        print(f"  {ds:<20s} n={s['n_configs']:2d}  "
              f"mean={s['mean']:.4f}  median={s['median']:.4f}  "
              f"min={s['min']:.4f}  max={s['max']:.4f}")

    print("\nPer-K:")
    for k, s in per_K.items():
        print(f"  K={k:<3s}  n={s['n_configs']:2d}  "
              f"mean={s['mean']:.4f}  median={s['median']:.4f}  "
              f"min={s['min']:.4f}  max={s['max']:.4f}")

    # ---- All configs sorted by safe threshold ----
    print("\nAll configs (sorted by safe ε):")
    sorted_configs = sorted(safe_thresholds.items(), key=lambda x: x[1])
    for name, eps in sorted_configs:
        K = configs[name]["K"]
        diag = np.diag(configs[name]["C"]).mean()
        print(f"  {name:<45s} K={K:>2d}  diag={diag:.3f}  safe_ε={eps:.4f}")

    # ---- Save results ----
    output = {
        "meta": {
            "description": "Realistic differential misclassification ε thresholds",
            "topology": TOPOLOGY,
            "n_epsilon": N_EPSILON,
            "epsilon_max": EPSILON_MAX,
            "n_mc": N_MC,
            "sign_reversal_threshold": SIGN_REVERSAL_THRESHOLD,
            "n_precomp": N_PRECOMP,
            "seed": 2026,
        },
        "per_config": all_results,
        "summary": summary,
        "per_dataset": per_dataset,
        "per_K": per_K,
    }

    out_path = PROJ / "artifacts" / "exp_realistic_epsilon_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")

    elapsed_total = time.time() - t_start
    print(f"Total time: {elapsed_total:.1f}s ({elapsed_total / 60:.1f}min)")


if __name__ == "__main__":
    main()
