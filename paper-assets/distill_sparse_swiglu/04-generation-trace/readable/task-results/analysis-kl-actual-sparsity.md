# analysis kl actual sparsity

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl_actual_sparsity_20260519T203819_result.json`
- **Structured JSON:** [`fc232910de49cf220619.json`](../../sessions/fc/fc232910de49cf220619.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**Qwen-14B KL 30% actual achieved sparsity：**

| Seed | Experiment | Actual Sparsity |
|---|---|---|
| 42 | qwen14b_kl30_s42_eval_uniform_v3 | **0.296** |
| 123 | qwen14b_kl30_s123_eval_v5 | **0.296** |
| 456 | qwen14b_kl30_s456_eval_v3 | **0.297** |

3-seed 均值 ≈ **0.2963**（target 0.30，接近但略低，与 TEAL@27.5% actual=0.268 的模式一致）。

Registry 已更新，三个实验的 metrics 中均补充了 `actual_sparsity` 字段。

---
