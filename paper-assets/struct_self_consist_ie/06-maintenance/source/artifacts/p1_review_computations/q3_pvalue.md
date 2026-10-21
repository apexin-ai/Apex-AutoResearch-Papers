# Q3: Per-Entity-Type ρ=-0.881 P-Value Verification

## Background

The paper reports per-entity-type Spearman ρ=-0.881 (degeneracy vs oracle headroom within Few-NERD) with p=0.004. The claim notes "effective degrees of freedom may be lower than 6" because entity types share model, tokenizer, and temperature. Few-NERD INTRA coarse has 8 entity types.

## Method

1. **t-distribution approximation**: t = ρ * sqrt((n-2)/(1-ρ²)), two-sided p from t-distribution with df=n-2
2. **Exact permutation test**: enumerate all n! permutations, count fraction with |ρ| >= 0.881

## Results

| n (types) | df | t-approx p | Exact permutation p | Total permutations |
|-----------|-----|------------|---------------------|-------------------|
| 5 | 3 | 0.0484 | 0.0833 | 120 |
| 6 | 4 | 0.0204 | 0.0333 | 720 |
| 7 | 5 | 0.0088 | 0.0123 | 5,040 |
| **8** | **6** | **0.0038** | **0.0046** | **40,320** |

## Comparison with Paper

Paper reports: ρ=-0.881, p=0.004, n=8 entity types.

- At n=8, t-approximation gives p=0.00385, which rounds to **0.004** (matches paper exactly).
- Exact permutation p=0.00456, which rounds to **0.005** (slightly larger than reported).

The paper used the t-distribution approximation. This is standard practice but slightly liberal for small n. The exact permutation p is marginally more conservative.

## Effective df Concern

If effective df=4 (due to shared model/tokenizer/temperature across types), this corresponds to n=6 in the Spearman test:
- t-approx p=0.020, exact p=0.033

Both remain significant at α=0.05 but **not** at the p=0.004 level reported. The paper correctly flags this caveat: "effective degrees of freedom may be lower than 6."

## Summary

| Scenario | p-value | Significant at α=0.05? | Significant at α=0.01? |
|----------|---------|----------------------|----------------------|
| n=8 (nominal, t-approx) | 0.0038 | Yes | Yes |
| n=8 (nominal, exact) | 0.0046 | Yes | Yes |
| n=6 (conservative, t-approx) | 0.0204 | Yes | No |
| n=6 (conservative, exact) | 0.0333 | Yes | No |
| n=5 (very conservative, exact) | 0.0833 | No | No |

## Conclusion

The paper's p=0.004 is correct for n=8 under t-approximation. The exact permutation p (0.005) is marginally higher but the conclusion is unchanged. Under reduced effective df (n=6), the correlation remains significant at α=0.05 (p=0.033 exact) but not at α=0.01. The paper's caveat about effective df is appropriate and should be retained.
