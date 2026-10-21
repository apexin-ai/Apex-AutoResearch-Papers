# Negative Results Classification (2026-05-25)

## Summary: 7 正文讨论 / 6 Appendix / 3 省略

### 正文讨论 (7)
1. eval_a1_lora_object_v11_rerun — Claim 1 主证据 (99.6% fake safe)
2. eval_pi05_safelibero_object_v11 — Claim 2 (stronger model ≠ safer)
3. eval_pi05_safelibero_spatial_v11 — Claim 2+3 (spatial arm-body)
4. oracle_true_gt_adaptive_alpha_v11 — Oracle triplet 1/3
5. oracle_true_gt_fixed_alpha_v11 — Oracle triplet 2/3
6. oracle_true_gt_feature_v11 — Oracle triplet 3/3
7. eval_a1_lora_spatial_v11 — EE-only boundary (spatial)

### Appendix (6)
8-13: A3 diagnostics, baseline references

### 省略 (3)
14-16: Bug (M027 oracle dead code), superseded v10a

### vs D019: 3 experiments upgraded from unclassified → 正文讨论
- eval_pi05_safelibero_object_v11, eval_pi05_safelibero_spatial_v11, eval_a1_lora_spatial_v11

### Recommended narrative order
1. Fake Safety (eval_a1_lora) → 2. Stronger model fails (Pi0.5 object+spatial) → 3. Oracle upper bound (triplet) → 4. EE-only boundary (A1 spatial)
