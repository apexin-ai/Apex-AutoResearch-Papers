# diag exp b k095 health

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp_b_k095_health_20260518T123622_result.json`
- **Structured JSON:** [`8f087083ba1a98155b3c.json`](../../sessions/8f/8f087083ba1a98155b3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

| 指标 | 值 |
|------|-----|
| **GPU 1 利用率** | 0% (显存 3090MiB/24564MiB，P2 状态，54W) |
| **进程 92881** | 活着，R 状态，CPU 251% |
| **tmux session** | `eval_random_k095` 存在 |
| **当前进度** | Task 3 Ep 11/50（已完成 161/500 episodes，**32%**） |
| **已完成 tasks** | T0: 0% SR, T1: 0% SR, T2: 0% SR（全部 FAIL，每个 episode 跑满 280 steps） |

### 关键发现：实验并非跑了 6 小时

日志第一条时间戳是 `2026-05-18 20:17:15`，当前服务器时间 `20:36:41`，**实际只跑了约 19 分钟**。可能之前有一个同名实验已结束/崩溃，当前是重新启动的。

### 是否卡住？

**没有卡住。** 进程活跃运行中，日志持续输出。GPU 利用率 0% 是正常的，因为 robosuite 环境模拟是 CPU 密集型，GPU 只在推理时短暂使用。

### 预计剩余时间

- 19 分钟完成 161 episodes → ~7 秒/episode
- 剩余 339 episodes → **约 40 分钟**
- 预计总耗时 ~1 小时

### 注意

所有 episode 全部 FAIL（0% SR），k_ratio=0.95 的 random pruning 效果完全不行。如果这是预期内的 baseline 对照实验则正常，否则需要检查实验配置。

---
