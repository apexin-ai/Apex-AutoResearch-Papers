# diag qwen status check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen-status-check_20260514T045637_result.json`
- **Structured JSON:** [`04a8c04726ab9940e186.json`](../../sessions/04/04a8c04726ab9940e186.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验进程均存活，GPU 利用率 78-90%，ALLOCATED 状态是 registry 层面的问题，实际在正常运行。

关键问题：**进度极慢**。2.5 小时后 s015/s020 才处理到第 4/50 个 problem，s025/s030 才第 2/50 个。按当前速率估算完成需 1.5-4 天，远超 4 小时 timeout 限制。GPU 2/3 内存占用（55-58 GB）是 GPU 0/1（27 GB）的两倍，高 sparsity 的计算开销显著更大。

报告已写入 `artifacts/qwen_status_check.md`。

---
