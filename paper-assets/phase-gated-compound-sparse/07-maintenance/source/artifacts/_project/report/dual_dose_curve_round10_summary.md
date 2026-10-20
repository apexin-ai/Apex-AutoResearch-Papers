# Dual 5-Point Accuracy Dose Curve Summary
## Round 10 Consistency Check — 2026-05-16

### DS (DeepSeek-R1-Distill-Qwen-7B) — n=50, MATH-500 problems 1-50, max_new_tokens=8192

| Sparsity | Accuracy | Correct/Total | Trunc.Count | Trunc.Rate | Non-Trunc.Acc | Source |
|----------|----------|---------------|-------------|------------|---------------|--------|
| dense    | 0.74     | 37/50         | 8           | 0.16       | 0.881         | Reviewer-verified |
| s015     | 0.48     | 24/50         | 16          | 0.32       | 0.706         | Reviewer-verified |
| s020     | 0.30     | 15/50         | 28          | 0.56       | 0.682         | Reviewer-verified (corrected) |
| s025     | 0.08     | 4/50          | 38          | 0.76       | —             | Registry |
| s030     | 0.04     | 2/50          | 39          | 0.78       | 0.182         | Registry ⚠️ see discrepancy |

**DS s030 discrepancy flag:**
- Registry (from JSON analysis): truncated_count=39, truncation_rate=0.78, non_truncated_acc=0.182 (2/11)
- Director's Reviewer-verified: truncated_count=38, truncation_rate=0.76, non_truncated_acc=0.167
- Delta: 1 sample difference in truncation count → different denominator → 0.182 vs 0.167
- Needs Reviewer re-verification on raw JSON

### QW (Qwen2.5-7B-Instruct) — Combined n=100, MATH-500 problems 1-100, max_new_tokens=8192

| Sparsity | b1_8k (1-50) | b2 (51-100) | Combined | Acc   |
|----------|--------------|-------------|----------|-------|
| dense    | 22/50        | 24/50       | 46/100   | 0.46  |
| s015     | 23/50        | 19/50       | 42/100   | 0.42  |
| s020     | 13/50        | 23/50       | 36/100   | 0.36  |
| s025     | 16/50        | 17/50       | 33/100   | 0.33  |
| s030     | 7/50         | 12/50       | 19/100   | 0.19  |

All batches use max_new_tokens=8192 (b1_8k rerun fixed original 2048 mismatch).

### Consistency Checks

1. **Monotonicity**: Both curves strictly monotonically decreasing ✓
2. **Token budget**: All experiments unified at max_new_tokens=8192 ✓
3. **DS two-phase pattern**: dense→s020 shows truncation-driven degradation (non_trunc_acc ~68-88%), s025+ shows dual collapse ✓
4. **QW truncation**: Negligible at 8k tokens (≤4% across all sparsities) → accuracy drop is reasoning quality, not truncation ✓
5. **Cross-model**: Both models show dose-response, QW baseline lower (0.46 vs 0.74) but relative degradation pattern consistent ✓

### Registry Source IDs

DS: acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2
QW b1_8k: acc_qw_dense_b1_8k, acc_qw_s015_b1_8k, acc_qw_s020_b1_8k, acc_qw_s025_b1_8k, acc_qw_s030_b1_8k
QW b2: (from acc_qw_s015_n100, acc_qw_s020_n100_b2_fix, acc_qw_s025_n100_b2_fix, acc_qw_s030_n100, acc_qw_dense_b1_8k.batch2)
