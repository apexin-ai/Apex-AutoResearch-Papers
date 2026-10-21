# analysis perlayer kl k2 s456 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k2_s456_eval_20260523T112226_result.json`
- **Structured JSON:** [`06e5b3b34d49980d1eb5.json`](../../sessions/06/06e5b3b34d49980d1eb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已包含全部数据。结果如下：

## `perlayer_kl_k2_s456_eval` 结果

**配置**: TEAL global, sparsity_target=0.3, uniform allocation, bottleneck_size=128

| Metric | Value |
|--------|-------|
| **wikitext2_ppl** | **10.5826** |
| arc_challenge_acc_norm | 0.3840 |
| winogrande_acc | 0.6488 |
| mmlu_acc | 0.3542 |
| gsm8k_exact_match (flexible) | 0.0205 |
| gsm8k_exact_match (strict) | 0.0190 |
| hellaswag_acc_norm | 0.6590 |
| piqa_acc_norm | 0.7280 |

Sparsity 信息未在日志中单独记录（grep 被 pipe 阻断），但 config 中 `sparsity_target=0.3`（即 30% sparsity）。

---
