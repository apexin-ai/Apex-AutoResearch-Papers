# ops registry fix and monitor

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-fix-and-monitor_20260518T161554_result.json`
- **Structured JSON:** [`a0230d086d829965c1fe.json`](../../sessions/a0/a0230d086d829965c1fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## Registry 更新结果

4 个实验全部 PREPARING → QUEUED → **RUNNING** 更新成功：

| 实验 | GPU | PID |
|------|-----|-----|
| exp_023_cheetah_baseline_s2 | cuda:0 | 753786 |
| exp_008f_s2 | cuda:0 | 754063 |
| exp_001_baseline_s2 | cuda:1 | 754352 |
| exp_009c_s2 | cuda:1 | 754639 |

## 进程存活状态

**6 个 dreamer 进程全部在运行**，从 `ps aux` 确认：

| 实验 | Python PID | GPU | 状态 |
|------|-----------|-----|------|
| exp_008a_cheetah_unexposed_s0 | 748628 | cuda:0 | 运行中 (CPU 1352min) |
| exp_008a_cheetah_unexposed_s1 | 748707 | cuda:1 | 运行中 |
| exp_023_cheetah_baseline_s2 | 753791 | cuda:0 | 运行中 |
| exp_008f_s2 | 754068 | cuda:0 | 运行中 |
| exp_001_baseline_s2 | 754357 | cuda:1 | 运行中 |
| exp_009c_s2 | 754644 | cuda:1 | 运行中 |

## Cheetah Unexposed 进度

| | s0 | s1 |
|---|---|---|
| 最新 step | **72000** | **76000** |
| 日志更新 | 00:07 (~9min 前) | 00:14 (~2min 前) |
| logdir 更新 | 00:07 | 00:14 |
| train_return | 430~478 | 125~470 |

s0 日志 9 分钟未更新但进程仍在（PID 748628 确认存活），属于正常的训练 step 间隔，无异常。

## GPU 利用率

| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| GPU 0 | RTX PRO 6000 Blackwell | **98%** | 13.2G / 97.9G |
| GPU 1 | RTX PRO 6000 Blackwell | **64%** | 12.1G / 97.9G |

**无异常，所有实验正常运行。**

---
