# ops cuda5 conflict fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda5-conflict-fix_20260514T000250_result.json`
- **Structured JSON:** [`697e42d5331dc5cbdad1.json`](../../sessions/69/697e42d5331dc5cbdad1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完毕，**无需执行任何 kill 操作**。

## GPU 状态报告

| GPU | PID | 显存占用 | 利用率 | 对应实验 |
|-----|-----|---------|--------|---------|
| 0 | 235248 | 21986 / 24564 MiB | 100% | 未知实验 |
| 1 | 229375 | 3658 / 24564 MiB | 34% | 未知实验 |
| 2 | 229521 | 3658 / 24564 MiB | 33% | 未知实验 |
| 3 | 216254 | 17318 / 24564 MiB | 60% | 未知实验 |
| 4 | 221376 | 5820 / 24564 MiB | 44% | 未知实验 |
| 5 | 239734 | 21988 / 24564 MiB | 77% | **exp_001_sft_d005_05B_v3** |

## cuda:5 冲突处理结果

**无冲突。** 实际情况：

- **exp_001_sft_d005_05B_v3** (PID 239729→子进程 239734): **存活**，已运行 5h13m，GPU 5 上占 21988 MiB，利用率 77%，正常训练中。保留。
- **exp_001_sft_d005_05B_r3** (PID 240163): **已死**，ps 中无此进程，GPU 上也无对应 PID。无需 kill。
- **exp_001_eval_3B_d000_s42_v2** (PID 237865): **已死**，ps 中无此进程，GPU 上也无对应 PID。

## cuda:5 残留检查

cuda:5 上仅有 PID 239734（v3 的 python 子进程），无其他残留进程。

## 异常发现

无异常。6 块 GPU 各跑 1 个进程，无 GPU 空闲，无多进程冲突。GPU 0 利用率 100% 但这属于正常满载训练。

---
