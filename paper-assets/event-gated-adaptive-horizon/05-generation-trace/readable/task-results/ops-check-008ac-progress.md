# ops check 008ac progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_008ac_progress_20260514T022152_result.json`
- **Structured JSON:** [`a11dd92e7ff5f8290947.json`](../../sessions/a1/a11dd92e7ff5f8290947.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个都返回 0（无匹配，grep exit code 1 是正常的"未找到"）。汇总如下：

---

## GPU 状态

| GPU | 型号 | Compute Util | Memory | 功耗 | 温度 |
|-----|------|-------------|--------|------|------|
| 0 | RTX PRO 6000 Blackwell | **19%** | 4165 / 97887 MiB (4.3%) | 145W/600W | 39°C |
| 1 | RTX PRO 6000 Blackwell | **22%** | 2751 / 97887 MiB (2.8%) | 112W/600W | 41°C |

GPU 0 跑 exp_008a (PID 106947)，GPU 1 跑 exp_008c (PID 107026)。利用率偏低（19-22%），显存占用极小。

## 训练进度

| 实验 | 当前 step | dataset_size | train_return (最新) | train_length |
|------|----------|-------------|-------------------|-------------|
| **exp_008a** | 20,000 | 10,000 | **147.82** | 500 |
| **exp_008c** | 24,000 | 12,000 | **200.85** | 500 |

exp_008c 领先 4k steps，train_return 也明显更高（~201 vs ~148）。

两个 metrics 文件中均无 `eval_return`、`model_loss`、`fps` 字段，只有 step/dataset_size/train_return/train_length/train_episodes。

## NaN 检查

008a: **0**，008c: **0**。无 NaN/inf。

## 进程状态

| PID | 运行时间 | CPU% | MEM% |
|-----|---------|------|------|
| 106942 | 44min 34s | 0.0% | 0.0% |
| 107021 | 44min 33s | 0.0% | 0.0% |

这两个 PID（106942/107021）是 wrapper 进程，CPU/MEM 接近 0；实际干活的是子进程 106947 和 107026（nvidia-smi 中可见）。

---
