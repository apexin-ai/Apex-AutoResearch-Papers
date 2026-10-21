# ops gpu process check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_process_check_20260514T070953_result.json`
- **Structured JSON:** [`c0381eda13da9dd30a52.json`](../../sessions/c0/c0381eda13da9dd30a52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。

## 进程状态
- **008f**: ALIVE, PID=127766, elapsed=02:18:24, state=Rl
- **008e_v3**: ALIVE, PID=126115, elapsed=02:40:48, state=Rl
- 目标 105K steps，均在运行中

## 008f 指标（no_dt_embed, subsample_on, h=8）

| step | eval_return | value_mean | v/e | normalized v/e |
|------|-------------|------------|-----|----------------|
| 5000 | 30.49 | 0.00 | 0.0% | 0.00x |
| 15000 | 182.03 | 2.99 | 1.6% | 0.05x |
| 25000 | 196.78 | 17.51 | 8.9% | 0.27x |
| 35000 | 206.67 | 36.28 | 17.6% | 0.53x |
| **45000** | **194.08** | **53.43** | **27.5%** | **0.83x** |
| 55000 | 173.45 | 67.90 | 39.2% | 1.18x |

**008f@45K: v/e=27.5% < 35% → C2 因果确认成立** (normalized 0.83x < 1.06x)

注意：eval_return 从 35K 的 206.7 开始下降到 55K 的 173.5，性能在退化。value_mean 持续上升但 eval_return 在掉——value overestimation 加剧。

## 008e_v3 指标（subsample_on, dt=1, h=15）

| step | eval_return | value_mean | v/e | normalized v/e |
|------|-------------|------------|-----|----------------|
| 5000 | 31.00 | 0.00 | 0.0% | 0.00x |
| 15000 | 131.17 | 4.00 | 3.1% | 0.09x |
| 25000 | 155.69 | 26.19 | 16.8% | 0.51x |
| 35000 | 276.47 | 62.76 | 22.7% | 0.69x |
| 45000 | 382.22 | 110.67 | 29.0% | 0.87x |
| 55000 | 486.84 | 170.09 | 34.9% | 1.06x |
| 65000 | 580.67 | 235.05 | 40.5% | 1.22x |

008e_v3 表现健康——eval_return 持续上升（580.7@65K），v/e ratio 也在合理增长。

## GPU 状态
- cuda:0: 2751 MiB used, 19% util（008f）
- cuda:1: 4167 MiB used, 20% util（008e_v3）
- **可用于下一波实验: NO**（两块 GPU 均被占用）

---
