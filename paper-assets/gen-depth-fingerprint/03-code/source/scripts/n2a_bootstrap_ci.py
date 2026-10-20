"""N2a: Bootstrap CI + effect size for downstream perplexity comparisons."""
import json
import itertools
import numpy as np
from pathlib import Path

np.random.seed(2026)

DATA = {
    "size_matched": [2.367, 2.367, 2.367],
    "depth01": [2.3877, 2.3869, 2.387],
    "all": [2.335, 2.335, 2.3354],
    "binary_filtered": [2.389, 2.389, 2.389],
    "depth0_only": [2.6818, 2.68, 2.6817],
}

N_BOOT = 10_000
N_PERM = 10_000


def cohens_d(a, b):
    na, nb = len(a), len(b)
    va, vb = np.var(a, ddof=1), np.var(b, ddof=1)
    pooled_std = np.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))
    if pooled_std == 0:
        return float("inf") if np.mean(a) != np.mean(b) else 0.0
    return (np.mean(a) - np.mean(b)) / pooled_std


def bootstrap_ci(a, b, n_boot=N_BOOT):
    a, b = np.array(a), np.array(b)
    obs_diff = np.mean(a) - np.mean(b)
    diffs = np.empty(n_boot)
    for i in range(n_boot):
        sa = a[np.random.randint(0, len(a), len(a))]
        sb = b[np.random.randint(0, len(b), len(b))]
        diffs[i] = np.mean(sa) - np.mean(sb)
    ci_lo, ci_hi = np.percentile(diffs, [2.5, 97.5])
    return obs_diff, ci_lo, ci_hi, diffs


def permutation_test(a, b, n_perm=N_PERM):
    a, b = np.array(a), np.array(b)
    obs_diff = abs(np.mean(a) - np.mean(b))
    combined = np.concatenate([a, b])
    n_a = len(a)
    count = 0
    for _ in range(n_perm):
        np.random.shuffle(combined)
        perm_diff = abs(np.mean(combined[:n_a]) - np.mean(combined[n_a:]))
        if perm_diff >= obs_diff:
            count += 1
    return count / n_perm


def exact_permutation_test(a, b):
    """Exact test enumerating all assignments (feasible for n=3+3=6)."""
    a, b = np.array(a), np.array(b)
    obs_diff = abs(np.mean(a) - np.mean(b))
    combined = np.concatenate([a, b])
    n = len(combined)
    n_a = len(a)
    count = 0
    total = 0
    for idx in itertools.combinations(range(n), n_a):
        grp_a = combined[list(idx)]
        perm_diff = abs(np.mean(grp_a) - np.mean(combined) * 2 + np.mean(grp_a))
        # simpler: recompute
        rest = np.delete(combined, list(idx))
        perm_diff = abs(np.mean(grp_a) - np.mean(rest))
        if perm_diff >= obs_diff - 1e-12:
            count += 1
        total += 1
    return count / total


def compare_pair(name_a, name_b):
    a, b = DATA[name_a], DATA[name_b]
    obs_diff, ci_lo, ci_hi, _ = bootstrap_ci(a, b)
    d = cohens_d(a, b)
    p_perm = permutation_test(a, b)
    p_exact = exact_permutation_test(a, b)
    return {
        "group_a": name_a,
        "group_b": name_b,
        "mean_a": round(float(np.mean(a)), 6),
        "mean_b": round(float(np.mean(b)), 6),
        "mean_diff": round(float(obs_diff), 6),
        "bootstrap_95ci": [round(float(ci_lo), 6), round(float(ci_hi), 6)],
        "cohens_d": round(float(d), 4),
        "permutation_p": round(float(p_perm), 4),
        "exact_permutation_p": round(float(p_exact), 4),
        "n_boot": N_BOOT,
        "n_perm": N_PERM,
    }


results = {"primary_comparison": {}, "pairwise": [], "caveat": ""}

# Primary: size_matched vs depth01
primary = compare_pair("size_matched", "depth01")
results["primary_comparison"] = primary

# All pairwise
names = list(DATA.keys())
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        results["pairwise"].append(compare_pair(names[i], names[j]))

results["caveat"] = (
    "n=3 per group. Bootstrap and permutation tests with such small samples "
    "have limited resolution (exact permutation test has only C(6,3)=20 distinct "
    "assignments, so minimum nonzero p=0.05). Results should be interpreted as "
    "directional evidence, not definitive hypothesis tests."
)
results["method"] = {
    "bootstrap": "nonparametric percentile bootstrap, 10000 resamples",
    "permutation": "two-sided permutation test on mean difference, 10000 random + exact enumeration",
    "effect_size": "Cohen's d with pooled SD (ddof=1)",
}

out_path = Path(
    "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint"
    "/artifacts/n2a_downstream_bootstrap.json"
)
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)

# Print summary
print("=== Primary: size_matched vs depth01 ===")
p = results["primary_comparison"]
print(f"  Mean diff: {p['mean_diff']:.6f} (size_matched - depth01)")
print(f"  95% CI: [{p['bootstrap_95ci'][0]:.6f}, {p['bootstrap_95ci'][1]:.6f}]")
print(f"  Cohen's d: {p['cohens_d']:.4f}")
print(f"  Permutation p: {p['permutation_p']:.4f} (exact: {p['exact_permutation_p']:.4f})")

print(f"\n=== All {len(results['pairwise'])} pairwise comparisons ===")
for r in results["pairwise"]:
    print(
        f"  {r['group_a']:18s} vs {r['group_b']:18s} | "
        f"diff={r['mean_diff']:+.6f} | d={r['cohens_d']:+.4f} | "
        f"p_exact={r['exact_permutation_p']:.4f}"
    )

print(f"\nResults saved to {out_path}")
