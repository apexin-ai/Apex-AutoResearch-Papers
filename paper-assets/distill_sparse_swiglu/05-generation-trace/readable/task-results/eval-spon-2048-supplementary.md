# eval spon 2048 supplementary

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_spon_2048_supplementary_20260515T193220_result.json`
- **Structured JSON:** [`a8ac33e7cbcba0d7066a.json`](../../sessions/a8/a8ac33e7cbcba0d7066a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。全部指标：

```
=== SPON 2048 Supplementary Evaluation ===

true_dense_ppl:            6.1173
dense_with_spon_ppl:       6.1823
dense_ppl_degradation:     +0.0651
teal_sparse_no_spon_ppl:   12.0776
teal_sparse_with_spon_ppl: 11.7907
spon_recovery_teal:        4.8%
teal_sparsity:             0.4979
```

**已有指标（predictor hard mask 模式）对比：**
- True Dense PPL: 6.12 → 确认一致（6.1173）
- Sparse PPL (no SPON): 9.22
- SPON Sparse PPL: 8.99 (recovery 7.3%)

**本次补充指标：**

| 指标 | 值 |
|------|-----|
| dense_with_spon_ppl | 6.1823 |
| dense_ppl_degradation | +0.065（seq128 为 +0.08，2048 反而更小） |
| teal_sparse_no_spon_ppl | 12.0776 |
| teal_sparse_with_spon_ppl | 11.7907 |
| spon_recovery_teal | 4.8%（seq128 的对应值需对比，teal_with_spon_ppl=11.93 vs 这里 11.79） |

注意事项：
- TEAL 使用的是 predictor-based 全局分配（不是 vanilla activation-magnitude TEAL，后者在 LLaMA 上分层极度不均导致 PPL 爆炸）
- SPON biases 来自 spon_2048_s42 checkpoint（mean_norm=0.053, 确认为 2048 版本）
- Dense degradation +0.065 比预期（seq128 的 +0.08）更小，说明 2048 版 bias 虽然 mean_norm 更大（0.053 vs 0.041），但 fold 到 down_proj 后的影响反而更收敛
- TEAL 模式下 SPON recovery 仅 4.8%，远低于 predictor hard mask 的 7.3%——这在预期内，因为全局静态 mask 无法利用 per-token 自适应分配

---
