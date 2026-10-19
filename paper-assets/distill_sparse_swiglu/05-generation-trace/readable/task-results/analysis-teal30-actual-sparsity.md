# analysis teal30 actual sparsity

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_teal30_actual_sparsity_20260519T225206_result.json`
- **Structured JSON:** [`3f2c36a07d24653cd334.json`](../../sessions/3f/3f2c36a07d24653cd334.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到了。

**TEAL@30% uniform 的 actual sparsity = 0.293**（model-level）

来源：`~/runs/distill_sparse_swiglu/qwen14b_teal30_uniform_gsm8k.log`，48 层逐层 sparsity 范围 0.277–0.301，model-level 汇总为 **0.293**。

与 KL actual sparsity 的对比：
- KL actual sparsity: **0.296**
- TEAL actual sparsity: **0.293**
- 差值: **0.003**（TEAL 略低）

两者 actual sparsity 基本一致，差异可忽略，公平对比成立。

---
