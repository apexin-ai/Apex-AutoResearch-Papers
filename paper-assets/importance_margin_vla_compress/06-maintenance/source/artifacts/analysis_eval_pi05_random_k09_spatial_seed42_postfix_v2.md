# Analysis: eval_pi05_random_k09_spatial_seed42_postfix_v2

## Overview
- **Model**: π0.5
- **Suite**: libero_spatial
- **Prune mode**: random, keep_ratio=0.9 (10% token removal)
- **Seed**: 42
- **Post-fix**: CPU RNG bug fixed
- **Overall SR**: **53.4%** (267/500)
- **Wall time**: 171.9 min

## Per-task Success Rates

| Task | Description | SR |
|------|-------------|-----|
| T0 | pick up the black bowl between the plate | 90% |
| T1 | pick up the black bowl next to the ramekin | 52% |
| T2 | pick up the black bowl from table center | 80% |
| T3 | pick up the black bowl on the cookie box | 24% |
| T4 | pick up the black bowl in the top drawer | 18% |
| T5 | pick up the black bowl on the ramekin | 40% |
| T6 | pick up the black bowl next to the cookie box | 58% |
| T7 | pick up the black bowl on the stove | 54% |
| T8 | pick up the black bowl next to the plate | 90% |
| T9 | pick up the black bowl on the wooden cabinet | 28% |

## Comparison: π0.5 Spatial Random Post-fix Series

| keep_ratio | SR | Δ vs baseline | Source |
|------------|------|---------------|--------|
| k=1.0 (baseline) | 78.0% | — | registry metadata |
| k=0.925 | 58.2–60.4% | -17.6 to -19.8pp | unreg / pre-fix |
| **k=0.9** | **53.4%** | **-24.6pp** | **this experiment** |
| k=0.85 | 60.8% | -17.2pp | postfix_v2 |
| k=0.5 | 71.8% | -6.2pp | postfix_v3 |

## Key Findings

1. **Disruption peak confirmed on Spatial**: k=0.9 (53.4%) is worse than both k=0.85 (60.8%) and k=0.5 (71.8%), confirming the non-monotonic degradation pattern.

2. **k=0.9 is the deepest point** in the available Spatial curve — 10% token removal causes -24.6pp drop, worse than 50% removal (-6.2pp).

3. **Cross-suite consistency**: Object suite also shows a severe disruption at k=0.9 (SR=9%), though far more extreme. Spatial disruption is milder but follows the same pattern.

4. **Task variance**: T0/T2/T8 remain robust (80–90%), while T3/T4/T9 collapse to 18–28%. The disruption is task-selective.

## Conclusion

**negative** — 10% random token removal at k=0.9 causes disproportionate -24.6pp degradation on Spatial suite, confirming the disruption peak extends to Spatial. The non-monotonic curve (k=0.9 < k=0.85 < k=0.5) is consistent with the RoPE positional encoding disruption hypothesis.
