"""
Paired bootstrap resampling test for provenance weight training experiments.
3-seed comparison (rho=0.4) + point estimates (rho=0.6).
"""
import numpy as np
from itertools import combinations

np.random.seed(2026)

# === rho=0.4 data (from registry, 3 seeds: 42, 123, 456) ===
data_rho04 = {
    "Uniform": np.array([17.6939, 17.6861, 17.7015]),
    "Adaptive (n_min=3)": np.array([17.644, 17.6308, 17.6419]),
    "Adaptive_fix (n_min=2)": np.array([17.6527, 17.6432, 17.6566]),
    "Grid-best": np.array([17.64, 17.638, 17.65]),  # seed42:b=0.3, seed123/456:b=0.5
    "ESS-only": np.array([17.73, 17.72, 17.719]),
}

# === rho=0.6 data (single seed=42) ===
data_rho06 = {
    "Uniform": 17.766,
    "Adaptive τ=0.7": 17.73,
    "Adaptive τ=0.8": 17.74,
    "Adaptive τ=0.6": 17.7359,
    "ESS-only": 17.77,
}

N_BOOTSTRAP = 10000
N_SEEDS = 3


def paired_bootstrap(a, b, n_iter=N_BOOTSTRAP):
    """Paired bootstrap test. H0: mean(a) = mean(b). Returns p-value and CI of diff."""
    observed_diff = np.mean(a) - np.mean(b)
    n = len(a)
    diffs = a - b  # paired differences

    boot_diffs = np.zeros(n_iter)
    for i in range(n_iter):
        idx = np.random.randint(0, n, size=n)
        boot_diffs[i] = np.mean(diffs[idx])

    # Two-sided p-value: proportion of bootstrap samples where sign flips
    # Under H0, center the bootstrap distribution at 0
    centered = boot_diffs - np.mean(boot_diffs)
    p_value = np.mean(np.abs(centered) >= np.abs(observed_diff))

    # 95% CI of the difference (percentile method)
    ci_lo = np.percentile(boot_diffs, 2.5)
    ci_hi = np.percentile(boot_diffs, 97.5)

    return observed_diff, ci_lo, ci_hi, p_value


def cohens_d(a, b):
    """Cohen's d for paired samples."""
    diff = a - b
    return np.mean(diff) / np.std(diff, ddof=1) if np.std(diff, ddof=1) > 0 else np.inf


# === Run comparisons for rho=0.4 ===
comparisons = [
    ("Adaptive (n_min=3)", "Uniform"),
    ("Adaptive_fix (n_min=2)", "Uniform"),
    ("Grid-best", "Uniform"),
    ("Adaptive (n_min=3)", "Grid-best"),
    ("Adaptive (n_min=3)", "ESS-only"),
    ("Adaptive_fix (n_min=2)", "ESS-only"),
    ("ESS-only", "Uniform"),
]

print("=" * 80)
print("PAIRED BOOTSTRAP TEST RESULTS (rho=0.4, 3 seeds, 10000 iterations)")
print("=" * 80)
print()

results = []
for name_a, name_b in comparisons:
    a = data_rho04[name_a]
    b = data_rho04[name_b]
    diff, ci_lo, ci_hi, p = paired_bootstrap(a, b)
    d = cohens_d(a, b)
    results.append((name_a, name_b, diff, ci_lo, ci_hi, p, d))
    print(f"{name_a} vs {name_b}:")
    print(f"  Mean diff = {diff:.4f} (negative = first is better)")
    print(f"  95% CI: [{ci_lo:.4f}, {ci_hi:.4f}]")
    print(f"  p-value = {p:.4f}")
    print(f"  Cohen's d = {d:.2f}")
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
    print(f"  Significance: {sig}")
    print()

# === rho=0.6 point estimates ===
print("=" * 80)
print("POINT ESTIMATES (rho=0.6, single seed=42, no statistical test possible)")
print("=" * 80)
print()
baseline_06 = data_rho06["Uniform"]
for method, ppl in data_rho06.items():
    if method == "Uniform":
        continue
    delta = ppl - baseline_06
    print(f"  {method}: PPL={ppl:.4f}, Δ vs Uniform = {delta:+.4f}")

# === Generate markdown report ===
report = """# Statistical Significance Tests — Provenance Weight Training

## Methodology

**Test**: Paired bootstrap resampling (10,000 iterations)
**Samples**: 3 random seeds (42, 123, 456) per method
**Metric**: eval_ppl_holdout (lower is better)
**Dataset contamination rate**: ρ=0.4

### Limitation Statement

With only N=3 seeds, bootstrap resampling has very limited statistical power.
The test can only distinguish effects that are consistent across all 3 seeds.
A non-significant p-value means **insufficient evidence to reject H0** given the
small sample size — it does NOT mean the methods are equivalent. These results
should be interpreted as directional evidence, not definitive conclusions.

## ρ=0.4 Results (3-seed Bootstrap)

### Raw Data (eval_ppl_holdout)

| Method | seed=42 | seed=123 | seed=456 | Mean |
|--------|---------|----------|----------|------|
| Uniform | 17.6939 | 17.6861 | 17.7015 | 17.6938 |
| Adaptive (n_min=3, τ=0.8) | 17.6440 | 17.6308 | 17.6419 | 17.6389 |
| Adaptive_fix (n_min=2) | 17.6527 | 17.6432 | 17.6566 | 17.6508 |
| Grid-best (b=0.3/0.5) | 17.6400 | 17.6380 | 17.6500 | 17.6427 |
| ESS-only | 17.7300 | 17.7200 | 17.7190 | 17.7230 |

*Note: Grid-best uses b=0.3 for seed42, b=0.5 for seeds 123/456 (best grid value per seed).*

### Pairwise Comparisons

| Comparison | Mean Δ | 95% CI | p-value | Cohen's d | Sig. |
|-----------|--------|--------|---------|-----------|------|
"""

for name_a, name_b, diff, ci_lo, ci_hi, p, d in results:
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
    report += f"| {name_a} vs {name_b} | {diff:+.4f} | [{ci_lo:.4f}, {ci_hi:.4f}] | {p:.4f} | {d:.2f} | {sig} |\n"

report += """
*Significance: *** p<0.001, ** p<0.01, * p<0.05, ns = not significant*
*Negative Δ means the first method has lower (better) PPL.*

### Interpretation

"""

# Add interpretations
for name_a, name_b, diff, ci_lo, ci_hi, p, d in results:
    if p < 0.05:
        direction = "lower" if diff < 0 else "higher"
        report += f"- **{name_a} vs {name_b}**: Significant (p={p:.4f}). {name_a} has {direction} PPL by {abs(diff):.4f}.\n"
    else:
        report += f"- **{name_a} vs {name_b}**: Not significant (p={p:.4f}). Cannot distinguish with 3 seeds.\n"

report += """
## ρ=0.6 Results (Single Seed, No Statistical Test)

| Method | PPL | Δ vs Uniform |
|--------|-----|-------------|
| Uniform | 17.7660 | — |
"""

for method, ppl in data_rho06.items():
    if method == "Uniform":
        continue
    delta = ppl - baseline_06
    report += f"| {method} | {ppl:.4f} | {delta:+.4f} |\n"

report += """
*Single-seed results. No statistical test is possible. Differences are point estimates only.*

## Summary

1. **Adaptive methods consistently outperform Uniform** across all 3 seeds (ρ=0.4), with the best variant (n_min=3, τ=0.8) achieving ~0.055 PPL reduction.
2. **ESS-only performs worse than Uniform**, indicating that ESS-based weighting without the adaptive component hurts performance.
3. **Grid-best is competitive with Adaptive**, suggesting the adaptive mechanism successfully finds near-optimal weighting without grid search.
4. **Statistical power is limited** with N=3. The consistency of direction across seeds provides confidence in the ranking, but precise effect sizes require more seeds.
5. **ρ=0.6 (single seed)**: Same directional pattern — adaptive methods improve over uniform, ESS-only is worst.
"""

output_path = "/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/artifacts/statistical_tests.md"
with open(output_path, "w") as f:
    f.write(report)

print(f"\nReport written to: {output_path}")
