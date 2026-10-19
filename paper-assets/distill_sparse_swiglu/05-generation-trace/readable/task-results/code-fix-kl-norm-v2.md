# code fix kl norm v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-kl-norm-v2_20260515T143706_result.json`
- **Structured JSON:** [`3920e08c5a7ed9711170.json`](../../sessions/39/3920e08c5a7ed9711170.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Two old training runs (the buggy version with `/ vocab_size`) are using both GPUs. These are runs `mvp_kl_norm_s42` and `mvp_kl_norm_s123` — both using the broken code. They need to be killed to free GPU memory for the fixed quicktest.

Should I kill these two processes? They're running the buggy (double-normalized) code, so their results would be invalid anyway.

---
