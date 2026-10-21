# analysis qwen7b full trace label only seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen7b_full_trace_label_only_seed456_20260519T113830_result.json`
- **Structured JSON:** [`70660c2b56b483dfe606.json`](../../sessions/70/70660c2b56b483dfe606.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新至 DONE/success。

```
=== qwen7b_full_trace_label_only_seed456 结果 ===
accuracy: 84.70% (95% CI: [82.7%, 86.6%])
pass_f1: 0.9000
fail_f1: 0.7100
train_loss: 0.2452
eval_loss: 0.3366
conclusion: success

=== full_trace_label_only 3-seed 统计 ===
seed42: 86.22% | seed123: 86.89% | seed456: 84.70%
mean: 85.94% | σ: 1.12pp
```

seed456 略低于前两个 seed（84.7% vs 86.2%/86.9%），但在 95% CI 范围内重叠，3-seed σ=1.12pp 属于正常方差。full_trace_label_only 条件的稳定性可接受，可用于回应 N5 reviewer 关于方差的 concern。

---
