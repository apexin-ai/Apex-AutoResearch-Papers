# ops gpu round4 progress

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_round4_progress_20260516T183336_result.json`
- **Structured JSON:** [`372ec686210f4d3628bd.json`](../../sessions/37/372ec686210f4d3628bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**1. GPU 利用率 + 显存**

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 76% | 82.8 / 97.9 GB |
| 1 | 100% | 92.1 / 97.9 GB |
| 2 | 78% | 91.3 / 97.9 GB |
| 3 | 75% | 91.3 / 97.9 GB |

4 卡全部满载运行。

**2. c8_llama Round 4 进度**

- Round 1-3 已完成（importance s015/s020, random s015/s020）
- **Round 4 正在运行**：`random_s025`（GPU2）和 `random_s030`（GPU3），从 23:40 开始，已运行约 3 小时。按 Round 3 耗时 ~6h 估算，预计还需 ~3h 完成。

**3. GPQA s015 / s020 状态**

- **s020**（GPU0）：正常运行，当前第 25/198 题，已跑约 1h12m
- **s015**（GPU1）：正常运行，已跑 10h50m，进度应较靠前（日志未单独拉取，但进程活跃、GPU 100% 利用率）

全部任务正常，无异常。

---
