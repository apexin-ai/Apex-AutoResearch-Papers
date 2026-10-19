# Adaptive K Threshold Calibration Results

**Config**: LIBERO Spatial benchmark, K=10, 200 steps, 9000 pairwise L2 distances (C(10,2)=45 per step)
**Server**: bjb1-18228
**JSON**: logs/calibrate_spatial_K10.json

## L2 Distance Distribution

| Statistic | Value |
|-----------|-------|
| Mean | 0.0581 |
| Std | 0.0283 |
| Min | 0.0275 |
| Max | 0.2789 |
| P10 | 0.0359 |
| P25 | 0.0395 |
| P50 | 0.0457 |
| P75 | 0.0702 |
| P90 | 0.0970 |
| P95 | 0.1149 |

## Recommended Thresholds

| Strategy | Percentile | Threshold | Expected behavior |
|----------|-----------|-----------|-------------------|
| Conservative | P25 | 0.0395 | ~75% full path (K=5) |
| Balanced | P50 | 0.0457 | ~50% fast / 50% full |
| Aggressive | P75 | 0.0702 | ~75% fast path (K=2) |

## Notes
- Distribution is right-skewed (mean 0.058 > median 0.046)
- Most steps show low disagreement, few steps show high disagreement (max 0.279)
- Calibrated on Spatial benchmark; Object benchmark may differ slightly
