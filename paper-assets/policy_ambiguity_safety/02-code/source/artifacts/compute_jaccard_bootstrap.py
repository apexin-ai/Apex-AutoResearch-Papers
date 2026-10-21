"""
Bootstrap confidence intervals and permutation test for cross-family Jaccard analysis.

Computes:
1. Per-model violation sets (clause_ids with moderate/critical violations under ambiguous condition)
2. Bootstrap 95% CIs (B=10000) for within-family Jaccard, cross-family mean Jaccard, and their difference
3. Permutation test (N=10000) for H0: no family effect on Jaccard similarity

Input: artifacts/full_study/judgments/{model}/judgments.jsonl
Output: artifacts/bootstrap_jaccard_ci.json
"""

import json
import os
import numpy as np
from itertools import combinations
from pathlib import Path

# Configuration
SEED = 42
B_BOOTSTRAP = 10_000
N_PERMUTATIONS = 10_000
MODELS = ["gpt-5.4", "gpt-4.1", "claude-sonnet-4-6", "deepseek-v3", "qwen3-235b"]
# Within-family pair: GPT-5.4 and GPT-4.1 (same provider family)
WITHIN_FAMILY_PAIRS = [("gpt-5.4", "gpt-4.1")]
JUDGMENTS_DIR = Path(__file__).parent / "full_study" / "judgments"
OUTPUT_PATH = Path(__file__).parent / "bootstrap_jaccard_ci.json"


def load_violation_sets():
    """Load per-model violation sets: clause_ids with moderate/critical under ambiguous."""
    violation_sets = {}
    for model in MODELS:
        vset = set()
        jpath = JUDGMENTS_DIR / model / "judgments.jsonl"
        with open(jpath) as f:
            for line in f:
                d = json.loads(line)
                if (d["condition"] == "ambiguous" and
                        d["judgment"]["violation_level"] in ("moderate", "critical")):
                    vset.add(d["clause_id"])
        violation_sets[model] = vset
    return violation_sets


def build_clause_vectors(violation_sets, all_clauses):
    """Build binary violation vectors indexed by clause position.

    Returns dict: model -> np.array of shape (n_clauses,) with 1=violated, 0=not.
    """
    clause_list = sorted(all_clauses)
    clause_idx = {c: i for i, c in enumerate(clause_list)}
    vectors = {}
    for model, vset in violation_sets.items():
        vec = np.zeros(len(clause_list), dtype=np.int8)
        for c in vset:
            vec[clause_idx[c]] = 1
        vectors[model] = vec
    return vectors, clause_list


def jaccard_from_vectors(v1, v2):
    """Compute Jaccard index from binary vectors."""
    intersection = np.sum(v1 & v2)
    union = np.sum(v1 | v2)
    if union == 0:
        return 0.0
    return float(intersection / union)


def compute_all_pairwise(vectors, indices=None):
    """Compute all 10 pairwise Jaccard values.

    If indices is provided, use only those clause positions (for bootstrap resampling).
    """
    pairs = list(combinations(MODELS, 2))
    results = {}
    for a, b in pairs:
        v1 = vectors[a] if indices is None else vectors[a][indices]
        v2 = vectors[b] if indices is None else vectors[b][indices]
        results[(a, b)] = jaccard_from_vectors(v1, v2)
    return results


def split_within_cross(pairwise):
    """Split pairwise Jaccard dict into within-family and cross-family lists."""
    within_pairs_set = set(WITHIN_FAMILY_PAIRS)
    within = []
    cross = []
    for pair, val in pairwise.items():
        if pair in within_pairs_set or (pair[1], pair[0]) in within_pairs_set:
            within.append(val)
        else:
            cross.append(val)
    return within, cross


def bootstrap_ci(vectors, n_clauses, rng):
    """Bootstrap B=10000 resamples of clause-level vectors, compute CIs."""
    within_samples = []
    cross_samples = []
    diff_samples = []

    for _ in range(B_BOOTSTRAP):
        # Resample clause indices with replacement
        idx = rng.integers(0, n_clauses, size=n_clauses)
        pairwise = compute_all_pairwise(vectors, indices=idx)
        within, cross = split_within_cross(pairwise)
        w_mean = np.mean(within)
        c_mean = np.mean(cross)
        within_samples.append(w_mean)
        cross_samples.append(c_mean)
        diff_samples.append(w_mean - c_mean)

    within_samples = np.array(within_samples)
    cross_samples = np.array(cross_samples)
    diff_samples = np.array(diff_samples)

    return {
        "within_family": {
            "mean": float(np.mean(within_samples)),
            "ci_lower": float(np.percentile(within_samples, 2.5)),
            "ci_upper": float(np.percentile(within_samples, 97.5)),
            "std": float(np.std(within_samples))
        },
        "cross_family_mean": {
            "mean": float(np.mean(cross_samples)),
            "ci_lower": float(np.percentile(cross_samples, 2.5)),
            "ci_upper": float(np.percentile(cross_samples, 97.5)),
            "std": float(np.std(cross_samples))
        },
        "difference_within_minus_cross": {
            "mean": float(np.mean(diff_samples)),
            "ci_lower": float(np.percentile(diff_samples, 2.5)),
            "ci_upper": float(np.percentile(diff_samples, 97.5)),
            "std": float(np.std(diff_samples)),
            "prop_positive": float(np.mean(diff_samples > 0))
        }
    }


def permutation_test(vectors, observed_diff, rng):
    """Permutation test: H0 = no family effect on Jaccard.

    Strategy: randomly assign 5 models into families of size 2+3 (matching real split),
    compute within-family mean Jaccard - cross-family mean Jaccard for each permutation.
    p-value = proportion of permuted differences >= observed difference.
    """
    n_models = len(MODELS)
    all_pairs = list(combinations(range(n_models), 2))

    # Precompute observed pairwise Jaccard matrix
    pairwise_matrix = np.zeros((n_models, n_models))
    for i, j in all_pairs:
        j_val = jaccard_from_vectors(vectors[MODELS[i]], vectors[MODELS[j]])
        pairwise_matrix[i, j] = j_val
        pairwise_matrix[j, i] = j_val

    # Real family assignment: family 0 = {gpt-5.4, gpt-4.1}, family 1 = rest
    # For permutation: randomly pick 2 models as "family A", rest as "family B"
    # Within-family = pairs within same family, cross = pairs across families

    count_ge = 0
    perm_diffs = []

    for _ in range(N_PERMUTATIONS):
        # Randomly select 2 models to be "family A" (like the GPT pair)
        perm = rng.permutation(n_models)
        family_a = set(perm[:2].tolist())
        family_b = set(perm[2:].tolist())

        within_vals = []
        cross_vals = []

        for i, j in all_pairs:
            val = pairwise_matrix[i, j]
            if (i in family_a and j in family_a) or (i in family_b and j in family_b):
                within_vals.append(val)
            else:
                cross_vals.append(val)

        if within_vals and cross_vals:
            diff = np.mean(within_vals) - np.mean(cross_vals)
        else:
            diff = 0.0
        perm_diffs.append(diff)
        if diff >= observed_diff:
            count_ge += 1

    p_value = count_ge / N_PERMUTATIONS
    perm_diffs = np.array(perm_diffs)

    return {
        "observed_diff": float(observed_diff),
        "p_value": float(p_value),
        "n_permutations": N_PERMUTATIONS,
        "perm_diff_mean": float(np.mean(perm_diffs)),
        "perm_diff_std": float(np.std(perm_diffs)),
        "perm_diff_95th": float(np.percentile(perm_diffs, 95))
    }


def main():
    rng = np.random.default_rng(SEED)

    # Step 1: Load violation sets
    print("Loading violation sets...")
    violation_sets = load_violation_sets()
    for model in MODELS:
        print(f"  {model}: {len(violation_sets[model])} violations (of 300 clauses)")

    # Get all clause IDs
    all_clauses = set()
    for model in MODELS:
        jpath = JUDGMENTS_DIR / model / "judgments.jsonl"
        with open(jpath) as f:
            for line in f:
                d = json.loads(line)
                if d["condition"] == "ambiguous":
                    all_clauses.add(d["clause_id"])
    print(f"\nTotal clauses: {len(all_clauses)}")

    # Step 2: Build binary vectors
    vectors, clause_list = build_clause_vectors(violation_sets, all_clauses)
    n_clauses = len(clause_list)

    # Step 3: Compute observed pairwise Jaccard
    print("\nObserved pairwise Jaccard:")
    observed_pairwise = compute_all_pairwise(vectors)
    for pair, val in sorted(observed_pairwise.items()):
        marker = " [within-family]" if pair in WITHIN_FAMILY_PAIRS else ""
        print(f"  {pair[0]} vs {pair[1]}: {val:.3f}{marker}")

    within_obs, cross_obs = split_within_cross(observed_pairwise)
    within_mean_obs = np.mean(within_obs)
    cross_mean_obs = np.mean(cross_obs)
    observed_diff = within_mean_obs - cross_mean_obs
    print(f"\nWithin-family Jaccard: {within_mean_obs:.3f}")
    print(f"Cross-family mean Jaccard: {cross_mean_obs:.3f}")
    print(f"Difference (within - cross): {observed_diff:.3f}")

    # Step 4: Bootstrap CIs
    print(f"\nRunning bootstrap (B={B_BOOTSTRAP})...")
    boot_results = bootstrap_ci(vectors, n_clauses, rng)
    print(f"  Within-family 95% CI: [{boot_results['within_family']['ci_lower']:.3f}, {boot_results['within_family']['ci_upper']:.3f}]")
    print(f"  Cross-family 95% CI: [{boot_results['cross_family_mean']['ci_lower']:.3f}, {boot_results['cross_family_mean']['ci_upper']:.3f}]")
    print(f"  Difference 95% CI: [{boot_results['difference_within_minus_cross']['ci_lower']:.3f}, {boot_results['difference_within_minus_cross']['ci_upper']:.3f}]")
    print(f"  P(diff > 0): {boot_results['difference_within_minus_cross']['prop_positive']:.4f}")

    # Step 5: Permutation test
    print(f"\nRunning permutation test (N={N_PERMUTATIONS})...")
    perm_results = permutation_test(vectors, observed_diff, rng)
    print(f"  Observed difference: {perm_results['observed_diff']:.3f}")
    print(f"  Permutation p-value: {perm_results['p_value']:.4f}")
    print(f"  Null distribution: mean={perm_results['perm_diff_mean']:.4f}, std={perm_results['perm_diff_std']:.4f}")
    print(f"  Null 95th percentile: {perm_results['perm_diff_95th']:.4f}")

    # Step 6: Save results
    output = {
        "description": "Bootstrap CIs and permutation test for cross-family Jaccard analysis",
        "seed": SEED,
        "n_clauses": n_clauses,
        "n_models": len(MODELS),
        "models": MODELS,
        "within_family_pairs": WITHIN_FAMILY_PAIRS,
        "violation_set_sizes": {m: len(violation_sets[m]) for m in MODELS},
        "observed": {
            "within_family_jaccard": float(within_mean_obs),
            "cross_family_mean_jaccard": float(cross_mean_obs),
            "difference": float(observed_diff),
            "all_pairwise": {f"{a}_vs_{b}": round(v, 4) for (a, b), v in observed_pairwise.items()}
        },
        "bootstrap": boot_results,
        "permutation_test": perm_results
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {OUTPUT_PATH}")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    sig = "significant" if perm_results["p_value"] < 0.05 else "not significant"
    ci_excludes_zero = boot_results["difference_within_minus_cross"]["ci_lower"] > 0
    print(f"Within-family Jaccard: {within_mean_obs:.3f} (95% CI [{boot_results['within_family']['ci_lower']:.3f}, {boot_results['within_family']['ci_upper']:.3f}])")
    print(f"Cross-family mean:     {cross_mean_obs:.3f} (95% CI [{boot_results['cross_family_mean']['ci_lower']:.3f}, {boot_results['cross_family_mean']['ci_upper']:.3f}])")
    print(f"Difference:            {observed_diff:.3f} (95% CI [{boot_results['difference_within_minus_cross']['ci_lower']:.3f}, {boot_results['difference_within_minus_cross']['ci_upper']:.3f}])")
    print(f"CI excludes zero:      {ci_excludes_zero}")
    print(f"Permutation p-value:   {perm_results['p_value']:.4f} ({sig} at α=0.05)")


if __name__ == "__main__":
    main()
