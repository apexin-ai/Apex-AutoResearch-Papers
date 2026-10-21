# code exp45 monitor setup

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp45_monitor_setup_20260522T063124_result.json`
- **Structured JSON:** [`ca327150de29208c2675.json`](../../sessions/ca/ca327150de29208c2675.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告如下：

## exp45 训练状态

| 项目 | 值 |
|------|-----|
| **主进程 PID** | **40296** (python scripts/exp45_benign_adaptation_curve.py) |
| **子进程 PID** | 45369 (train_deberta.py, N=25 的 Stage 1 DeBERTa DAPT) |
| **启动时间** | 14:26 CST，已运行 ~6 分钟 |
| **GPU** | cuda:0 (CUDA_VISIBLE_DEVICES=0) |
| **当前进度** | **N=25** 的 Stage 1 (DeBERTa DAPT) 正在训练 |

### 已完成

| N 值 | 耗时 |
|------|------|
| N=0 | 1.7 min |
| N=5 | 1.7 min |
| N=10 | 1.7 min |

### 待完成

N=25（进行中）→ N=50 → N=100 → N=150

### 预估剩余时间

每个 N 值约 1.7 min（前 3 个一致）。N 越大训练数据越多，后面的可能稍慢，但数据量增幅不大（350 Qwen 固定，只加 WildChat）。保守估计：

- 剩余 4 个 N 值（含当前 N=25）× ~2 min ≈ **8 分钟**
- 总运行时间约 **13-15 分钟**，预计 ~14:40 CST 完成

---
