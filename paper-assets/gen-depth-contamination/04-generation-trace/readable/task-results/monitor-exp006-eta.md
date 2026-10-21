# monitor exp006 eta

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp006-eta_20260514T032708_result.json`
- **Structured JSON:** [`0e78a3a538a86538bf7c.json`](../../sessions/0e/0e78a3a538a86538bf7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，整理结果。

## exp-006 真实 per-run 时间和 ETA

### 已完成 Run 的精确耗时

**Training 时间（from `train_runtime` in log）：**

| # | Run | train_runtime | 总耗时* |
|---|-----|-------------|---------|
| 1 | no-filter_s42 | 36.3 min (2178s) | ~70 min** |
| 2 | no-filter_s123 | 36.4 min (2185s) | 44.2 min |
| 3 | no-filter_s456 | 36.2 min (2175s) | 44.2 min |
| 4 | no-filter_s789 | 36.2 min (2173s) | 44.1 min |
| 5 | no-filter_s1024 | 36.2 min (2173s) | 44.1 min |
| 6 | binary-ours_s42 | 37.4 min (2243s) | 45.3 min |
| 7 | binary-ours_s123 | 37.3 min (2240s) | 45.2 min |
| 8 | binary-ours_s456 | 41.2 min (2473s) | 49.1 min |

\* 总耗时 = 连续 run 目录时间戳间隔（training + eval + overhead）
\*\* 第 1 个 run 包含 base model 评估开销，非典型

### 平均值（runs 2-8）

- **Training: 37.2 min**
- **Eval + overhead: 8.0 min**（极稳定，每个 run 都在 7.8-8.0 min）
- **总 per-run: 45.2 min**

原始估算 ~25min/run 严重偏低——只算了 training，漏了 eval。实际 per-run **≈45 min**。

### 当前进度

- **完成: 8/50 (16%)**
- **进行中: Run 9/50 (binary-ours_s789)**
  - Step 2002/2814 (71%), 26:33 elapsed, ~1.26 it/s
  - 剩余训练: ~10.7 min
  - 加 eval: ~8 min
  - Run 9 预计完成: ~**03:48 UTC** May 14

### ETA

服务器时区: UTC+8

| | |
|---|---|
| 已完成 | 8/50 |
| 当前 run 剩余 | ~19 min |
| 剩余 runs | 41 |
| 41 runs × 45.2 min | 30.9 hours |
| **总剩余时间** | **~31 hours** |
| **ETA (UTC)** | **May 15 ~10:45 UTC** |
| **ETA (服务器本地 UTC+8)** | **May 15 ~18:45** |

### 注意事项

- 所有 8 个已完成 run 的 `Samples after filtering: 30000/30000 (100%)`，步数均为 2814
- 后续 graduated/surprisal/dsir 策略如果过滤掉样本，步数会减少，per-run 可能更快——但目前无法确认，上述 ETA 按保守估计（全部 45.2 min/run）
- binary-ours_s456 的 train_runtime 异常偏高（41.2 min vs 平均 36-37 min），可能是 GPU 热降频导致的一次性波动

---
