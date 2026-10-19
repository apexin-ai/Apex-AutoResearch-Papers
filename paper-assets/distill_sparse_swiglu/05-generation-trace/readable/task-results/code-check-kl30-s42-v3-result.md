# code check kl30 s42 v3 result

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_kl30_s42_v3_result_20260519T155540_result.json`
- **Structured JSON:** [`84f3da9786cf6fdde1aa.json`](../../sessions/84/84f3da9786cf6fdde1aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。Cron job 不存在（可能已被清除）。

**结果汇报：**

- **Conclusion**: success
- **耗时**: 5192.4s (~86 min)
- **Log**: `~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_eval_uniform_v3.log`
- **Results**: `/root/distill_sparse_swiglu/results/benchmark/qwen14b_kl30_s42_eval_uniform_v3/results.json`

**Metrics (Qwen2.5-14B, KL predictor, 30% sparsity, uniform allocation, sigmoid fix):**

| Task | Metric | Value |
|------|--------|-------|
| WikiText-2 | PPL | **7.8715** |
| ARC-Challenge | acc_norm | **0.5495** |
| WinoGrande | acc | **0.7127** |
| HellaSwag | acc_norm | **0.7268** |
| PIQA | acc_norm | **0.7476** |
| MMLU | acc | **0.6480** |

---
