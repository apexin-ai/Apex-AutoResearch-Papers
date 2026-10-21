# analysis k8 eval check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k8_eval_check_20260523T044911_result.json`
- **Structured JSON:** [`810e233d86e16e83ca2e.json`](../../sessions/81/810e233d86e16e83ca2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry already had status=DONE and conclusion=success (likely auto-updated). Metrics are now recorded.

## K=8 Eval 结果 (perlayer_kl_k8_s42_eval)

| Metric | Value |
|--------|-------|
| **wikitext2_ppl** | 8.9704 |
| **arc_challenge** (acc_norm) | 0.4104 |
| **winogrande** (acc) | 0.6740 |
| **mmlu** (acc) | 0.3980 |
| **gsm8k** (exact_match) | 0.0561 |
| **hellaswag** (acc_norm) | 0.6919 |
| **piqa** (acc_norm) | 0.7612 |

Eval 在 4328s (~72min) 内完成，registry 已更新。

---
