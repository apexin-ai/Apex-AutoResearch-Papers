# monitor all running experiments

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_all_running_experiments_20260513T175625_result.json`
- **Structured JSON:** [`8e753dacba0c982db4a3.json`](../../sessions/8e/8e753dacba0c982db4a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### GPU 使用
| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 100% | 79986 / 97887 MiB |
| cuda:1 | 58% | 12227 / 97887 MiB |

---

### 1. random_50_seed123 (PID 250452, cuda:0) — **运行中, Gen 2/7 训练阶段**
- 运行时间: 48分45秒
- 已完成 Gen 0 和 Gen 1，当前 Gen 2 正在训练 student
- 每代约 710s，预计还需 ~59 分钟完成剩余 5 代

**已完成 metrics:**

| Gen | Perplexity | RankMe | k-NN | Rare n-gram | Rank corr | Time |
|-----|-----------|--------|------|-------------|-----------|------|
| 0 | 36.46 | 272.72 | 0.9880 | 0.02935 | -0.0114 | 713s |
| 1 | 43.44 | 287.58 | 0.9880 | 0.01968 | -0.0431 | 708s |

baseline Gen-0 RankMe: 231.08

---

### 2. random_50_seed456 (PID 250453, cuda:0) — **运行中, Gen 2/7 训练阶段**
- 运行时间: 48分45秒
- 已完成 Gen 0 和 Gen 1，当前 Gen 2 正在训练 student

**已完成 metrics:**

| Gen | Perplexity | RankMe | k-NN | Rare n-gram | Rank corr | Time |
|-----|-----------|--------|------|-------------|-----------|------|
| 0 | 36.91 | 274.42 | 0.9880 | 0.02843 | -0.0070 | 706s |
| 1 | 43.89 | 289.60 | 0.9880 | 0.01901 | -0.0316 | 709s |

baseline Gen-0 RankMe: 231.08

---

### 3. seed456_methods / uncurated_seed456 (cuda:1) — **运行中, 刚启动**
- 日志仅 6 行，刚开始第一个方法 `uncurated_seed456`
- 启动时间: Thu May 14 01:52:08 CST 2026
- 尚未产出任何 generation metrics
- 后续还有 ext_seed456 → rgds_seed456 串行等待

---

**两个 seed 的 Gen 0-1 趋势一致**: perplexity 从 ~36→~43 上升，RankMe 从 ~273→~289 上升，rare n-gram 从 ~0.029→~0.019 下降，rank corr 从 ~-0.01→~-0.04 略降。两个 random50 实验预计约 1 小时后完成。

---
