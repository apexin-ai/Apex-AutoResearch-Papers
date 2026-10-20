# run eval 3B d000 s42 a32 batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_eval_3B_d000_s42_a32_batch_20260516T001355_result.json`
- **Structured JSON:** [`f9d7aa2f9ca36fe8b9f8.json`](../../sessions/f9/f9d7aa2f9ca36fe8b9f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:4 被占用，无法提交。**

当前 cuda:4 上正在运行 `compute_signals.py`（PID 661774，d025_s123 arc_challenge，已运行 4m40s）。

GPU 状态一览：
| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 23260/24564 MiB | 忙 |
| 1 | 13341/24564 MiB | 忙 |
| 2 | 7537/24564 MiB | 忙 |
| 3 | 8976/24564 MiB | 忙 |
| 4 | 9165/24564 MiB | 忙（compute_signals d025_s123） |
| 5 | 0/24564 MiB | **空闲** |

可选方案：
1. 改提交到 **cuda:5**（当前唯一空闲 GPU）
2. 等 cuda:4 的 signals 任务完成后再提交

需要你决定。

---
