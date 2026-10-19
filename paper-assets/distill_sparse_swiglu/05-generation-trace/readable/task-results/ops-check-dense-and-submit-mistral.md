# ops check dense and submit mistral

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_dense_and_submit_mistral_20260515T233249_result.json`
- **Structured JSON:** [`84cc0fe86de51d81301a.json`](../../sessions/84/84cc0fe86de51d81301a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**汇总：**

- **Dense eval**：已完成 (PID 163723)
  - arc_challenge: **0.5819**, winogrande: **0.7814**, mmlu: **0.6532**, gsm8k: **0.5004**
- **Mistral eval**：已提交 (PID 174840, cuda:1, tmux session `lm_eval_mistral_downstream`)
  - 先跑 `mistral_kl_s42`，再跑 `mistral_dense`，结果输出到 `results/plan_009_mistral/`

---
