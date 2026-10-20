# d066 Beam Width Sweep — SciERC Analysis

**Model**: Qwen3-8B LoRA (merged), SciERC test set (551 samples)
**Date**: 2026-05-20
**Server**: westd-21461 GPU1
**Status**: 7/8 configs complete, k=8 constrained in progress (~12%, ETA 11:50 CST)

## Full Results Table

| Config | #Ent | #Rel | ET% | RV% | DR% | CF% | E-P | E-R | E-F1 | R-P | R-R | R-F1 | Avg Time(s) | Total Time(s) |
|--------|------|------|-----|-----|-----|-----|-----|-----|------|-----|-----|------|-------------|----------------|
| k=1 unc | 1785 | 1140 | 0.0 | 0.0 | 2.11 | 0.0 | 65.01 | 68.86 | 66.88 | 39.82 | 46.61 | 42.95 | 2.494 | 1374.0 |
| k=1 con | 1785 | 1140 | 0.0 | 0.0 | 0.0 | 0.5 | 65.01 | 68.86 | 66.88 | 39.82 | 46.61 | 42.95 | 2.932 | 1615.8 |
| k=2 unc | 1775 | 1167 | 0.0 | 0.0 | 1.54 | 0.0 | 66.04 | 69.64 | **67.79** | 41.05 | 49.18 | **44.75** | 2.954 | 1627.8 |
| k=2 con | 1775 | 1165 | 0.0 | 0.0 | 0.0 | 0.11 | 65.95 | 69.58 | 67.71 | 40.94 | 48.97 | 44.60 | 3.463 | 1908.3 |
| k=4 unc | 1814 | 1272 | 0.0 | 0.0 | 1.89 | 0.0 | 65.06 | 70.11 | 67.49 | 38.60 | 50.41 | 43.72 | 3.485 | 1920.1 |
| k=4 con | 1814 | 1269 | 0.0 | 0.0 | 0.0 | 0.0 | 64.82 | 69.81 | 67.22 | 38.53 | 50.21 | 43.60 | 4.069 | 2242.0 |
| k=8 unc | 1833 | 1297 | 0.0 | 0.0 | 1.77 | 0.0 | 63.75 | 69.28 | 66.40 | 37.81 | 50.31 | 43.17 | 4.194 | 2311.2 |
| k=8 con | — | — | — | — | — | — | — | — | — | — | — | — | — | IN PROGRESS |

## Key Findings

### 1. Schema Compliance
- **ET% = 0, RV% = 0** across all configs — entity types and relation vocabulary fully internalized by LoRA fine-tuning
- **DR% = 1.54–2.11% unconstrained → 0% constrained** — constrained decoding eliminates all domain restriction violations
- **CF%**: k=1 con (0.5%) > k=2 con (0.11%) > k=4 con (0.0%) — higher beam width resolves entity type conflicts

### 2. F1 vs Beam Width (Inverted-U Shape)
```
E-F1:  k=1 (66.88) → k=2 (67.79 ★) → k=4 (67.49) → k=8 (66.40)   Δ peak→k8 = -1.39pp
R-F1:  k=1 (42.95) → k=2 (44.75 ★) → k=4 (43.72) → k=8 (43.17)   Δ peak→k8 = -1.58pp
```
**k=2 is the sweet spot.** Higher beam widths increase recall (more entities/relations predicted) but hurt precision disproportionately:
- Recall trend (E-R): 68.86 → 69.64 → 70.11 → 69.28 (peaks at k=4)
- Precision trend (E-P): 65.01 → 66.04 → 65.06 → 63.75 (peaks at k=2, then drops)

### 3. Constrained Decoding Cost
| Beam k | E-F1 Δ(con-unc) | R-F1 Δ(con-unc) | Latency Overhead |
|--------|-----------------|-----------------|------------------|
| k=1 | 0.00 | 0.00 | +17.6% |
| k=2 | -0.08 | -0.15 | +17.2% |
| k=4 | -0.27 | -0.12 | +16.8% |
| k=8 | TBD | TBD | TBD |

**Constrained decoding F1 cost ≤ 0.27pp** with consistent ~17% latency overhead.

### 4. Latency Scaling
```
Avg time (unc): k=1 (2.494s) → k=2 (2.954s) → k=4 (3.485s) → k=8 (4.194s)
Avg time (con): k=1 (2.932s) → k=2 (3.463s) → k=4 (4.069s) → k=8 (TBD, est ~4.9s)
```
Roughly linear scaling: +0.24s per doubling of beam width (unc).

### 5. Prediction Volume
Higher beam width increases entity/relation count modestly:
- Entities: 1785 → 1775 → 1814 → 1833
- Relations: 1140 → 1167 → 1272 → 1297

## Pareto Analysis

### F1 Frontier
- **k=2 unconstrained**: Best raw F1 (E=67.79, R=44.75), 2.954s/sample
- **k=2 constrained**: Near-best F1 (E=67.71, R=44.60), 0% DR, 3.463s/sample

### Compliance Frontier
- **k=4 constrained**: Perfect compliance (ET=0, RV=0, DR=0, CF=0), -0.57pp E-F1 vs best, 4.069s/sample
- **k=2 constrained**: Near-perfect (only CF=0.11%), -0.08pp E-F1 vs best, 3.463s/sample

### Recommended Operating Point
**k=2 constrained** — best F1/compliance/latency tradeoff:
- Only -0.08pp E-F1, -0.15pp R-F1 vs unconstrained best
- 0% DR violations (vs 1.54% unconstrained)
- 17% latency overhead (3.46s vs 2.95s)
- Residual CF% (0.11%) is negligible (2 instances out of 1775)

## Conclusion
Beam search k=2 is Pareto optimal for SciERC on Qwen3-8B. Higher beam widths (k=4, k=8) increase recall but damage precision, yielding net F1 decline. Constrained decoding cost is negligible (≤0.27pp F1, ~17% latency). The LoRA model has fully internalized schema constraints (ET%=0, RV%=0), with only domain restriction violations (DR 1.5-2.1%) remaining for constrained decoding to correct.

**Pending**: k=8 constrained results (ETA ~11:50 CST 2026-05-20). Expected to confirm the trend but unlikely to change conclusions.
