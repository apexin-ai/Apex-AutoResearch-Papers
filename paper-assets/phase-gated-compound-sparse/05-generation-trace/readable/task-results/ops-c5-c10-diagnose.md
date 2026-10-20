# ops c5 c10 diagnose

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c5_c10_diagnose_20260516T035719_result.json`
- **Structured JSON:** [`3c1ddbe70738e8826d63.json`](../../sessions/3c/3c1ddbe70738e8826d63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### c5 DS: **DONE** (30/30)
- PID 307021 已退出
- 结果文件 `results_c5_gini_ds.json` (366KB) 写入时间 May 16 11:49
- 30/30 problems 全部完成，sparsity levels: 0.15, 0.20, 0.25, 0.30

### c10 PID 313211: **ALIVE** ⚠️
两个 c10 进程都还在 GPU 1 上运行：

| PID | CMD | Elapsed | GPU Mem |
|-----|-----|---------|---------|
| 312143 | `python scripts/c10_gen_s020` | 18:56 | 15646 MiB |
| 313211 | `python scripts/gen_c10_s020` | 15:01 | 16588 MiB |

注意脚本名不同：`c10_gen_s020` vs `gen_c10_s020`。313211 **没有被 kill**，仍在运行且占用 GPU 显存。

### 全 GPU 状态

| GPU | Used/Total | Util | Process |
|-----|-----------|------|---------|
| 0 | 0 / 97887 MiB | 0% | 空闲 |
| 1 | 32248 / 97887 MiB | 95% | 312143 + 313211 (两个 c10) |
| 2 | 73273 / 97887 MiB | 98% | 310735 `pacs.profiling.r...` (37min) |
| 3 | 73273 / 97887 MiB | 100% | 310736 `pacs.profiling.r...` (37min) |

**需要处理**：GPU 1 上 PID 313211 是重复进程，需要 kill 释放 ~16.6GB 显存。是否 kill？

---
