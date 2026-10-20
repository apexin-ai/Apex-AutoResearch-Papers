# analysis gpqa s015 results

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpqa_s015_results_20260516T201157_result.json`
- **Structured JSON:** [`883883c7ecddea8eb334.json`](../../sessions/88/883883c7ecddea8eb334.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提取到所有关键数据。结果如下：

```
n_problems: 198

per_phase_ii (interaction_index @ sparsity=0.15):
  high_sparsity: {mean: 0.191363, median: 0.012758, ci: [0.047972, 0.514786], median_ci: [0.011463, 0.013936], winsorized_mean: 0.039667, skewness: 77.00, outliers: 3}
  mid_sparsity:  {mean: 0.877870, median: 0.102412, ci: [0.723150, 1.039118], median_ci: [0.092683, 0.115074], winsorized_mean: 0.532911, skewness: 7.70, outliers: 37}
  low_sparsity:  {mean: 5.991797, median: 0.960161, ci: [5.235965, 6.732278], median_ci: [0.892882, 1.033060], winsorized_mean: 3.945337, skewness: 8.88, outliers: 56}

perplexity (@ sparsity=0.15):
  high_sparsity: {dense: 1.1777, attn: 1.5205, kv: 1.7020, both: 2.2531}
  mid_sparsity:  {dense: 1.3075, attn: 1.6733, kv: 3.2369, both: 4.7222}
  low_sparsity:  {dense: 1.4216, attn: 1.9771, kv: 19.3067, both: 27.6495}

phase_stats:
  high_sparsity: {n_tokens: 479658, n_segments: 6261}
  mid_sparsity:  {n_tokens: 276409, n_segments: 2185}
  low_sparsity:  {n_tokens: 465085, n_segments: 5128}

pass_fail: PASS
  ci_overlap_test: PASS (low vs mid CI non-overlapping at 0.15)
  sign_reversal_test: FAIL (no sign reversal detected)
  overall: PASS

gradient_direction: low > mid > high (median: 0.960 > 0.102 > 0.013)
```

**Config:**
- Model: DeepSeek-R1-Distill-Qwen-7B
- Masking: importance (head=attention_frobenius_norm, kv=cumulative_attention_received)
- Segmentation: quantile
- Bootstrap: 1000 iterations

梯度方向正确（low_sparsity II >> mid >> high），且 low vs mid 的 CI 不重叠，整体判定 **PASS**。

---
