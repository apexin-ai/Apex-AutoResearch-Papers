# Multiplicative vs Additive Null Model Comparison

## Background

- **Additive null**: II_add = R_b - R_h - R_k + 1  (expects R_b = R_h + R_k - 1)
- **Multiplicative null**: II_mul = R_b - R_h x R_k  (expects R_b = R_h x R_k)
- **Relationship**: II_mul = II_add - (R_h - 1)(R_k - 1)
- Since R_h >= 1 and R_k >= 1, multiplicative residual <= additive II always.
- Both positive iff R_b exceeds the respective null prediction.

## Table 1: Aggregate PPL-Based Comparison (mean PPL across segments)

| Sparsity | Phase | PPL_dense | PPL_attn | PPL_kv | PPL_both | R_h | R_k | R_b | Add. II | Mul. Resid. | Correction |
|----------|-------|-----------|----------|--------|----------|-----|-----|-----|---------|-------------|------------|
| 0.15 | high | 1.1462 | 1.8077 | 1.2147 | 2.2835 | 1.5771 | 1.0598 | 1.9922 | +0.3553 | +0.3209 | 0.0345 |
| 0.15 | mid | 1.1226 | 1.6033 | 2.1276 | 3.9408 | 1.4282 | 1.8952 | 3.5104 | +1.1870 | +0.8036 | 0.3833 |
| 0.15 | low | 1.1105 | 1.5982 | 6.7451 | 16.9987 | 1.4392 | 6.0739 | 15.3072 | +8.7941 | +6.5658 | 2.2283 |
| 0.20 | high | 1.1462 | 1.8835 | 1.2357 | 2.6982 | 1.6433 | 1.0781 | 2.3540 | +0.6327 | +0.5825 | 0.0502 |
| 0.20 | mid | 1.1226 | 1.7212 | 3.6511 | 8.1284 | 1.5332 | 3.2524 | 7.2407 | +3.4551 | +2.2541 | 1.2010 |
| 0.20 | low | 1.1105 | 1.6499 | 14.1083 | 42.6350 | 1.4857 | 12.7045 | 38.3926 | +25.2024 | +19.5173 | 5.6852 |
| 0.25 | high | 1.1462 | 2.0845 | 1.3108 | 3.4623 | 1.8186 | 1.1436 | 3.0207 | +1.0585 | +0.9409 | 0.1176 |
| 0.25 | mid | 1.1226 | 2.0249 | 6.1778 | 16.4148 | 1.8038 | 5.5031 | 14.6221 | +8.3153 | +4.6958 | 3.6194 |
| 0.25 | low | 1.1105 | 1.8101 | 23.8919 | 104.1749 | 1.6300 | 21.5145 | 93.8090 | +71.6645 | +58.7406 | 12.9239 |
| 0.30 | high | 1.1462 | 3.1123 | 1.3958 | 5.7149 | 2.7153 | 1.2178 | 4.9860 | +2.0529 | +1.6793 | 0.3735 |
| 0.30 | mid | 1.1226 | 6.3783 | 15.1094 | 137.6109 | 5.6817 | 13.4593 | 122.5823 | +104.4413 | +46.1104 | 58.3309 |
| 0.30 | low | 1.1105 | 7.1194 | 40.7878 | 963.1979 | 6.4110 | 36.7292 | 867.3552 | +825.2149 | +631.8846 | 193.3303 |

## Table 2: Per-Problem Median Additive II vs Aggregate Multiplicative Residual

| Sparsity | Phase | Per-Problem Median Add. II | Aggregate Add. II | Aggregate Mul. Residual | N_problems | Both Positive? |
|----------|-------|---------------------------|-------------------|------------------------|------------|----------------|
| 0.15 | high | +0.2266 | +0.3553 | +0.3209 | 43 | Yes |
| 0.15 | mid | +0.7432 | +1.1870 | +0.8036 | 32 | Yes |
| 0.15 | low | +2.8762 | +8.7941 | +6.5658 | 24 | Yes |
| 0.20 | high | +0.3353 | +0.6327 | +0.5825 | 42 | Yes |
| 0.20 | mid | +1.6733 | +3.4551 | +2.2541 | 28 | Yes |
| 0.20 | low | +9.2538 | +25.2024 | +19.5173 | 21 | Yes |
| 0.25 | high | +0.6641 | +1.0585 | +0.9409 | 42 | Yes |
| 0.25 | mid | +5.3067 | +8.3153 | +4.6958 | 23 | Yes |
| 0.25 | low | +24.1619 | +71.6645 | +58.7406 | 21 | Yes |
| 0.30 | high | +0.8833 | +2.0529 | +1.6793 | 40 | Yes |
| 0.30 | mid | +7.2706 | +104.4413 | +46.1104 | 22 | Yes |
| 0.30 | low | +34.6937 | +825.2149 | +631.8846 | 20 | Yes |

## Table 3: Gradient Comparison (low/high ratio)

| Sparsity | Add. Gradient | Mul. Gradient | Direction Match? | Add. Sign(low,high) | Mul. Sign(low,high) |
|----------|--------------|--------------|-----------------|--------------------|--------------------|
| 0.15 | 24.75 | 20.46 | Yes | (+,+) | (+,+) |
| 0.20 | 39.83 | 33.51 | Yes | (+,+) | (+,+) |
| 0.25 | 67.71 | 62.43 | Yes | (+,+) | (+,+) |
| 0.30 | 401.98 | 376.27 | Yes | (+,+) | (+,+) |

## Table 4: Per-Problem Median Gradient (additive, from stored data)

| Sparsity | Median II(high) | Median II(mid) | Median II(low) | Gradient (low/high) |
|----------|----------------|----------------|----------------|---------------------|
| 0.15 | 0.2266 | 0.7432 | 2.8762 | 12.69 |
| 0.20 | 0.3353 | 1.6733 | 9.2538 | 27.60 |
| 0.25 | 0.6641 | 5.3067 | 24.1619 | 36.38 |
| 0.30 | 0.8833 | 7.2706 | 34.6937 | 39.28 |

## Analysis and Conclusion

1. **Gradient direction**: All match between additive and multiplicative null.
2. **Sign consistency**: All (sparsity, phase) same sign under both nulls.

3. **Magnitude**: Multiplicative residual is systematically smaller by (R_h-1)(R_k-1).
   This correction grows with sparsity:
   - s=0.15: mean correction = 0.8821 (range 0.0345 to 2.2283)
   - s=0.20: mean correction = 2.3121 (range 0.0502 to 5.6852)
   - s=0.25: mean correction = 5.5536 (range 0.1176 to 12.9239)
   - s=0.30: mean correction = 84.0116 (range 0.3735 to 193.3303)

4. **Verdict**: The core claim -- compound sparsity is super-additive and
   interaction escalates high->low -- holds under both null models.
   Multiplicative null yields smaller residuals but preserves the
   monotonic phase gradient across all four sparsity levels.