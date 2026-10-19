# eval-supp-k2mean-spatial-s42 Analysis

## Result
**Overall SR: 81.5% (163/200)** — K=2 mean baseline, vla_only mode, Spatial benchmark, seed 42

## Per-task Breakdown

| Task | SR | Count |
|------|-----|-------|
| bowl between plate & ramekin → plate | 95.0% | 19/20 |
| bowl next to ramekin → plate | 95.0% | 19/20 |
| bowl from table center → plate | 100.0% | 20/20 |
| bowl on cookie box → plate | 100.0% | 20/20 |
| bowl in top drawer → plate | 70.0% | 14/20 |
| bowl on ramekin → plate | 0.0% | 0/20 |
| bowl next to cookie box → plate | 95.0% | 19/20 |
| bowl on stove → plate | 80.0% | 16/20 |
| bowl next to plate → plate | 85.0% | 17/20 |
| bowl on wooden cabinet → plate | 95.0% | 19/20 |

## Hypothesis Verification

**Hypothesis**: K=2 mean ≈ VLA-only (78.5%) → CRM is the source of improvement, not sampling diversity.

**Result: REJECTED (negative)**

K=2 mean achieves 81.5%, which is **+3pp above VLA-only baseline (78.5%)**. Multi-sample averaging alone provides meaningful improvement without any CRM correction.

## Improvement Decomposition

| Method | SR | Delta vs VLA-only |
|--------|-----|-------------------|
| VLA-only (K=1, seed42) | 78.5% | — |
| **K=2 mean (this exp)** | **81.5%** | **+3.0pp** |
| CRM always-on (norm=0.05) | 80.0% | +1.5pp |
| Reconvla K=10 | 79.0% | +0.5pp |
| Adaptive CRM τ=0.25 | 82.0% | +3.5pp |

## Key Takeaways

1. **Averaging is the dominant contributor**: ~3pp of the adaptive CRM's 3.5pp gain comes from multi-sample averaging, not CRM correction itself.
2. **CRM adds marginal value**: Adaptive CRM (82.0%) vs K=2 mean (81.5%) = only +0.5pp attributable to CRM correction.
3. **Implication for paper narrative**: Cannot claim CRM correction as the primary mechanism. The story needs to acknowledge that sampling diversity / averaging is the main driver, with CRM providing incremental refinement.
4. **bowl on ramekin remains unsolvable** (0%) across all methods — a fundamental VLA limitation, not addressable by post-hoc correction.
