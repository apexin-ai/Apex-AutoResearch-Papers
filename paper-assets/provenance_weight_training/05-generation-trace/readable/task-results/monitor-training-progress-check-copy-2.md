# monitor training progress check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-check_20260514T202630_result.json`
- **Structured JSON:** [`0ee7f37df764d1176be1.json`](../../sessions/0e/0ee7f37df764d1176be1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### adaptive_fix 训练进度

| 实验 | 当前 step | 总 step | 进度 | 速度 | 预计剩余 | 状态 |
|------|----------|---------|------|------|---------|------|
| adaptive_fix_seed42 | 5801 | 6103 | 95% | ~2.24s/it | **~11 min** | 正常 |
| adaptive_fix_seed123 | 5781 | 6103 | 95% | ~2.18s/it | **~12 min** | 正常 |
| adaptive_fix_seed456 | 5292 | 6103 | 87% | ~2.21s/it | **~30 min** | 正常 |

seed42 和 seed123 约 11-12 分钟后完成；seed456 从 checkpoint-1000 恢复所以落后，约 30 分钟后完成。无报错。

### grid_b_seed42_batch 进度

已完成 b 值：0.5 → 1.0 → 1.5 → 2.0 → 3.0（共 5 个）

**当前在跑 b=5.0**：step 3422/6103 (56%)，速度 2.12s/it，预计剩余 **~1h35min**。这是 batch 中最后一个 b 值。

### auto_eval_watcher

- 原 PID 74145 **已死**
- 新 PID 99508 **存活**，已运行 7h50m（`python auto_eval_watcher.py`），工作正常

### 异常/风险

- 无报错，无异常
- 4 GPU 全部满载（88-99% 利用率，各占 ~46GB 显存）
- seed42/seed123 即将完成，完成后 GPU 1/2 会空闲——如果有后续任务可以提前准备

---
