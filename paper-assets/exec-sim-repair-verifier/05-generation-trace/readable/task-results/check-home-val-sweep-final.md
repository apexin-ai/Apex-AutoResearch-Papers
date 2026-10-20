# check home val sweep final

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-val-sweep-final_20260514T083021_result.json`
- **Structured JSON:** [`186df0943b3a9720b5d4.json`](../../sessions/18/186df0943b3a9720b5d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Sweep 状态：正在运行，即将完成

**GPU 0**: 占用中 — RTX 5090, 100% utilization, 81°C, 12336MiB/32607MiB

**进度**: 5 个 checkpoint 中已完成 4 个，第 5 个 (checkpoint-1000) 正在跑 (5440/9335, ~58%)。不是 13 个 checkpoint — 目录里只有 5 个 (200/400/600/800/1000)。

**ETA**: checkpoint-1000 约 01:15 开始，按当前速度 ~01:42 完成（约 12 分钟后）。

### 已完成 checkpoint 的 val 指标

| Checkpoint | Accuracy | F1 macro | fail F1 | fail Recall | pass F1 | Unparseable |
|-----------|----------|----------|---------|-------------|---------|-------------|
| 200 | 62.51% | 55.54% | 37.94% | 47.51% | 73.14% | 1883 |
| 400 | 80.72% | 67.03% | 45.78% | 33.75% | 88.27% | 1883 |
| 600 | 76.78% | 66.81% | 48.63% | 45.56% | 85.00% | 1883 |
| **800** | **81.81%** | **69.14%** | **49.37%** | 36.77% | **88.91%** | 1883 |
| 1000 | running... | — | — | — | — | — |

**checkpoint-800 目前最优**（accuracy 81.81%, f1_macro 69.14%, fail_f1 49.37%）。checkpoint-1000 running_acc 暂时 81.8%，与 800 持平。

所有 checkpoint unparseable 数量一致 (1883/9335 = 20.2%)，说明这是数据问题而非模型问题。

Majority baseline 75.88%，checkpoint-800 超出 +5.9pp。主要瓶颈在 fail recall（36.77%），precision 很高 (75.14%) 但漏检严重。

---
