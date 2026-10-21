# check mse30 s456 downstream result

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mse30_s456_downstream_result_20260522T105702_result.json`
- **Structured JSON:** [`d52068ebe4667d7291ed.json`](../../sessions/d5/d52068ebe4667d7291ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MSE 30% s456 downstream eval 完成，registry 已更新为 DONE/success。Cron 不存在（可能已被清理）。

**结果汇总**：

| Benchmark | Metric | Value |
|-----------|--------|-------|
| ARC-c | acc_norm | **0.3882** |
| WinoGrande | acc | **0.6196** |
| MMLU | acc | **0.3264** |
| GSM8K | exact_match | **0.0311** |
| HellaSwag | acc_norm | **0.6129** |
| PIQA | acc_norm | **0.7383** |
| BoolQ | acc | **0.7034** |

耗时 4056s (~67min)，1.18 GPU-hours。s456 seed 数据已就绪，可与 s42/s123 合并计算 3-seed mean±std。

---
