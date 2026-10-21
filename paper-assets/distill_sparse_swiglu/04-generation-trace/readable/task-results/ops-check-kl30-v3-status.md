# ops check kl30 v3 status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-kl30-v3-status_20260518T211601_result.json`
- **Structured JSON:** [`bf79901a5aff4081545e.json`](../../sessions/bf/bf79901a5aff4081545e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

**两个实验均已完成** (EXIT_CODE=0)，无活跃进程，GPU 空闲 (0%/0MiB)。

### kl30_s123_uniform_v3
| Metric | Value |
|---|---|
| WikiText-2 PPL | **8.8308** |
| ARC-Challenge acc / acc_norm | 0.4096 / 0.4531 |
| WinoGrande acc | 0.6938 |
| MMLU acc | 0.3944 |
| GSM8K exact_match | 0.0751 |
| 耗时 | 2157.6s (~36min) |
| 完成时间 | 2026-05-19 04:30:04 |

### kl30_s456_uniform_v3
| Metric | Value |
|---|---|
| WikiText-2 PPL | **8.7947** |
| ARC-Challenge acc / acc_norm | 0.4070 / 0.4505 |
| WinoGrande acc | 0.6875 |
| MMLU acc | 0.4198 |
| GSM8K exact_match | 0.0758 |
| 耗时 | 2325.3s (~39min) |
| 完成时间 | 2026-05-19 04:30:05 |

两个 seed 的结果非常接近，s456 的 MMLU 略高 (+2.54pp)，PPL 略优；其余指标差异在 1pp 以内。

---
