# analysis eval math500 grpo cka only 20 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_math500_grpo_cka_only_20_2048_20260519T030922_result.json`
- **Structured JSON:** [`4fadca7f02151254be49.json`](../../sessions/4f/4fadca7f02151254be49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**GRPO CKA-only 20% 在 MATH-500 @2048 的最终 accuracy: 29.2%** (146/500)

与 interim 29.7% 基本一致，最终略降 0.5pp。

关键对比：
- GRPO vs SFT for CKA-only: **+0.2pp**（几乎持平，GRPO 未给 CKA-only 带来显著提升）
- CKA-only 是所有剪枝方案中最强的：比 GRPO Standard 高 2.8pp，比 GRPO RASP 高 5.2pp
- 22% 的样本在 2048 tokens 处截断

---
