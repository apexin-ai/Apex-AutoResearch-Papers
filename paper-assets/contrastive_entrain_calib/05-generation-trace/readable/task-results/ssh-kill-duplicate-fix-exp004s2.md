# ssh kill duplicate fix exp004s2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-duplicate-fix-exp004s2_20260522T155341_result.json`
- **Structured JSON:** [`f9ca9f717ac09e1d2bc9.json`](../../sessions/f9/f9ca9f717ac09e1d2bc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 1. Kill 结果
PID 502516 已成功终止（SIGTERM 即退出）。

### 2. PID 494017 状态
运行中，当前 **step 4000/8000**，刚保存了 checkpoint-4000。运行时间 ~5h，在 GPU1（CUDA_VISIBLE_DEVICES=1）上。

### 3. Checkpoint 完整性（按 adapter_model.safetensors mtime）

| Checkpoint | mtime | 可信？ | 说明 |
|---|---|---|---|
| checkpoint-2000 | 20:24:52 | **可信** | 初始恢复点 |
| checkpoint-2500 | 21:41:14 | **不确定** | 两个进程都经过此 step，可能被覆盖 |
| checkpoint-3000 | **22:56:41** | **被污染** | 时间晚于 3500，是 PID 502516（已 kill）写的覆盖 |
| checkpoint-3500 | 22:36:45 | **可信** | 只有 PID 494017 能到 3500 |
| checkpoint-4000 | 刚保存 | **可信** | PID 502516 已死，只有 494017 写入 |

关键问题：**checkpoint-3000 被 PID 502516 覆盖了**（mtime 22:56 比 checkpoint-3500 的 22:36 晚 20 分钟，说明是慢进程后写入的）。

### 4. 日志污染
**严重**。585 条记录，仅 399 个 unique step：
- Step 2010-2500：每个出现 **3 次**（原始训练 + 两次恢复都写入）
- Step 2510-3360：每个出现 **2 次**（两个恢复进程同时写入）
- `train_log.jsonl` 需要清洗后才能用于分析

### 5. GPU 状态
GPU0: 100% / 55GB，GPU1: 97% / 40GB。只剩 PID 494017 一个 exp-004-s2 进程。

**建议后续操作**：如果需要日志分析，需按时间戳或 PID 过滤 `train_log.jsonl` 去重。checkpoint-3000 不可信，可以删掉。

---
