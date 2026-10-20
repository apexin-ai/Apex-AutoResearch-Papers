# check 4gpu progress

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_4gpu-progress_20260514T022952_result.json`
- **Structured JSON:** [`abddd012bab9522633a6.json`](../../sessions/ab/abddd012bab9522633a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | GPU | 显存占用 | GPU利用率 | 进度 | 完成 |
|------|-----|---------|----------|------|------|
| fixed_s020_r2 | 0 | 33509 MiB | 75% | **28/50** | 否 |
| fixed_s030_r2 | 1 | 33509 MiB | 76% | **28/50** | 否 |
| random_s015 | 2 | 23885 MiB | 76% | **19/50** | 否 |
| random_s025 | 3 | 23885 MiB | 77% | **20/50** | 否 |

4 个实验均在运行中，无一完成（profiling_results.json 均不存在）。fixed 组进度约 56%，random 组约 38-40%。

---
