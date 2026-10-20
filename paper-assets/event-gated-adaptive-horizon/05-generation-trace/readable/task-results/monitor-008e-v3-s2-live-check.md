# monitor 008e v3 s2 live check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_008e_v3_s2-live-check_20260515T042155_result.json`
- **Structured JSON:** [`8cc91556a1ccb1a4b026.json`](../../sessions/8c/8cc91556a1ccb1a4b026.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

### exp_008e_v3_walker_s2 (C6 seed=2, gate_fixed_dt=1)

| 项目 | 状态 |
|------|------|
| **进程** | ALIVE (PID 43437, 运行时间 3h35m) |
| **实际最新 step** | **72K** (registry=68K, 实际领先 4K) |
| **最新 eval** | 65K (下次 eval 预计在 75K) |
| **目标** | 105K, 完成 ~69% |
| **FPS** | ~6.4 |

**Eval trajectory:**

| Step | eval_return | value_mean |
|------|-------------|------------|
| 5K   | 39.3        | 0.002      |
| 15K  | 180.9       | 3.9        |
| 25K  | 211.8       | —          |
| 35K  | 320.4       | —          |
| 45K  | 356.9       | —          |
| 55K  | 418.3       | 172.9      |
| 65K  | **435.1**   | 220.5      |

（25K-45K 的 value_mean 被输出截断）

**趋势**: 每 10K 步稳定提升约 50-80 pts。当前 435@65K 低于 seed=1 同期（seed=1 在 65K 约 500+），但仍在上升通道。gate_dt 全部为 1（gate_dt_1_frac=1.0），gate 机制未激活。预计 ~5.5h 后完成 105K。

---

### exp_009a_baseline_walker_s2 (baseline seed=2)

| 项目 | 状态 |
|------|------|
| **进程** | ALIVE (PID 142508, 运行时间 18h49m) |
| **实际最新 step** | **448K** (registry=445K, 领先 3K) |
| **最新 eval** | 445K (eval_return = **948.4**) |
| **目标** | 500K, 完成 ~90% |
| **FPS** | ~7.3 |

**近期 eval (最后 10 个):**

| Step | eval_return |
|------|-------------|
| 355K | 932.4 |
| 365K | 943.1 |
| 375K | 952.9 |
| 385K | 942.3 |
| 395K | **966.9** (peak) |
| 405K | 948.0 |
| 415K | 957.1 |
| 425K | 939.4 |
| 435K | 963.7 |
| 445K | 948.4 |

**趋势**: 已收敛，在 930-967 范围波动。与 seed=1 final=950.9 高度一致。train_return 近期也在 840-946 范围。预计 ~2h 后完成 500K。

---

### 关键发现

1. **Registry 滞后确认**: 两个实验都比 registry 领先 3-4K steps，符合 tmux log buffering 预期
2. **008e_v3_s2 进度偏慢**: eval_return 435@65K，比 seed=1 同期低。但 train_return 已达 678@72K，说明 policy 在改善，eval 可能在 75K+ 出现跳升
3. **009a 已基本完成**: eval 稳定在 ~950，与 seed=1 (950.9) 一致，最终结果可预期在 940-960 范围

---
