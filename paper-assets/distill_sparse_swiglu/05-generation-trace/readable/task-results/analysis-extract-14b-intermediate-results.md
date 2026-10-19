# analysis extract 14b intermediate results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_extract_14b_intermediate_results_20260517T215553_result.json`
- **Structured JSON:** [`ca0dfa294bf8e9f4643e.json`](../../sessions/ca/ca0dfa294bf8e9f4643e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果写入 `artifacts/qwen14b_intermediate_results.md`。

**核心发现：ARC/WinoGrande/MMLU 分数目前不可提取。** 原因：eval 脚本用 lm-eval-harness 将 4 个 task 打包一次性跑，结果只在全部完成后才写入 log/JSON。GSM8K 是最慢的（generate_until），3 个实验都还在跑。

**目前可用数据：**

| Experiment | PPL | GSM8K 进度 |
|------------|-----|-----------|
| qwen14b_dense_baseline | 5.1854 | 81% (~50 min remaining) |
| qwen14b_teal30_eval | 8.7332 | 87% (~49 min remaining) |
| qwen14b_bce30_s42_eval | 8.7634 | 86% (~46 min remaining) |

预计 30-50 分钟后 GSM8K 跑完，所有指标才会一次性输出。需要到时再提取。

---
