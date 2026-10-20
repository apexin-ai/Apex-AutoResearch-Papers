# QW Importance Masking — Accuracy Dose Curve v2

**Model**: Qwen2.5-7B-Instruct  
**Dataset**: MATH (n=100, split into batch1=problems 1-50, batch2=problems 51-100)  
**Date**: 2026-05-16  

## Summary Table

| Sparsity | Batch1_v2 (8k) | Batch2 | Combined n=100 | Old Combined (2k b1) | Δ vs Old |
|----------|----------------|--------|----------------|---------------------|----------|
| dense    | 0.44 (22/50)   | 0.48 (24/50)          | **0.46 (46/100)** | 0.40 (40/100) | +0.06 |
| s015     | 0.46 (23/50)   | 0.38 (19/50) †        | **0.42 (42/100)** | 0.36 (36/100) | +0.06 |
| s020     | 0.26 (13/50)   | 0.46 (23/50, b2_fix)  | **0.36 (36/100)** | 0.35 (35/100) | +0.01 |
| s025     | 0.32 (16/50)   | 0.34 (17/50, b2_fix)  | **0.33 (33/100)** | 0.33 (33/100) | 0.00  |
| s030     | 0.14 (7/50)    | 0.24 (12/50) †        | **0.19 (19/100)** | 0.19 (19/100) | 0.00  |

## Token Budget Notes

- **Batch1_v2**: All run with max_new_tokens=8192 (corrected)
- **Batch2 (b2_fix)**: s020, s025 re-run with 8192 tokens
- **† Batch2 (original)**: dense, s015, s030 batch2 from original n100 run — likely used max_new_tokens=2048
- Actual truncation rates at 8192 are very low (2%, ~1 problem per batch), confirming 2048 was rarely the binding constraint for s025/s030

## Key Finding

**The 2048→8192 token fix had zero impact on s025 and s030.** Both batch1_v2 results are identical to the old batch1 values:
- s025: 0.32 → 0.32 (unchanged)
- s030: 0.14 → 0.14 (unchanged)

This confirms that token truncation was NOT causing accuracy loss at higher sparsity levels. The degradation is purely from the pruning/eviction itself.

For dense and s015, the batch1_v2 (8k) shows meaningful improvement over old batch1 (dense: 0.44 vs 0.36 old_b1; s015: 0.46 vs 0.34 old_b1), but these were already re-run earlier.

## Degradation Pattern (Combined n=100)

```
dense  ████████████████████████████████████████████████  0.46
s015   ██████████████████████████████████████████        0.42  (-8.7% rel)
s020   ████████████████████████████████████              0.36  (-21.7% rel)
s025   █████████████████████████████████                 0.33  (-28.3% rel)
s030   ███████████████████                              0.19  (-58.7% rel)
```

**Cliff between s025 (0.33) and s030 (0.19)** — 42% relative drop in a single 5pp step.

## Experiment IDs

| Sparsity | Batch1_v2 exp_id | Batch2 exp_id |
|----------|------------------|---------------|
| dense    | acc_qw_dense_b1_8k | acc_qw_dense_n100 (b2 portion) |
| s015     | acc_qw_s015_b1_8k | acc_qw_s015_n100 (b2 portion) |
| s020     | acc_qw_s020_b1_8k | acc_qw_s020_n100_b2_fix |
| s025     | acc_qw_s025_b1_8k | acc_qw_s025_n100_b2_fix |
| s030     | acc_qw_s030_b1_8k | acc_qw_s030_n100 (b2 portion) |
