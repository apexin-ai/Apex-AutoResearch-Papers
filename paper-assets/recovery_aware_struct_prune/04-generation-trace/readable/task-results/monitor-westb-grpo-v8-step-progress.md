# monitor westb grpo v8 step progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westb-grpo-v8-step-progress_20260515T172014_result.json`
- **Structured JSON:** [`4f3fbd105d16283ea411.json`](../../sessions/4f/4f3fbd105d16283ea411.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据到手。

---

## GRPO v8 实验状态报告

### 进程状态

| | RASP (cuda:0) | Standard (cuda:1) |
|---|---|---|
| PID | 532861 ✅ 运行中 | 534667 ✅ 运行中 |
| 运行时长 | 2h 47m | 2h 38m |
| **当前 step** | **23/100** | **22/100** |
| 平均 step 耗时 | ~403s (6m43s) | ~415s (6m55s) |

### Step 30 预估到达时间

- **RASP**: step 23 → step 30 = 7 steps × ~410s ≈ 48 min → **~18:03 UTC (May 15)**
- **Standard**: step 22 → step 30 = 8 steps × ~415s ≈ 55 min → **~18:14 UTC (May 15)**

（当前 UTC 约 17:20，即 RASP ~43min 后、Standard ~54min 后到达 step 30）

### 关键指标

**RASP** (step 10 → step 20):

| 指标 | step 10 | step 20 | 判断 |
|------|---------|---------|------|
| grad_norm | 0.0134 | 0.0109 | 极低，几乎无梯度 |
| reward_mean | 0.009 | 0.026 | 微弱 |
| frac_zero_std | **0.90** | **0.90** | 锁死在 0.9，无恢复迹象 |
| entropy | 0.060 | 0.065 | 极低 |
| loss | 0.009 | -0.005 | 趋零 |

**结论：RASP 模型已严重坍塌。** 90% batch 无差异化 reward 信号，grad_norm 比 Standard 低 100x+，无任何恢复迹象。

**Standard** (step 10 → step 20):

| 指标 | step 10 | step 20 | 判断 |
|------|---------|---------|------|
| grad_norm | 2.906 | 1.586 | 正常范围，下降中 |
| reward_mean | 0.058 | 0.061 | 稳定 |
| frac_zero_std | **0.50** | **0.675** | ⚠️ 上升中，趋近 0.75 预警线 |
| entropy | 0.148 | 0.145 | 稳定 |
| loss | 0.060 | 0.056 | 缓降 |

**结论：Standard 尚存活但 frac_zero_std 从 0.5→0.675 线性上升，按此趋势 step 30 附近将触及 0.75 预警线。** 需要在 step 30 checkpoint 时评估是否干预。

### GPU 状态

| GPU | 利用率 | 显存 | 温度 |
|-----|--------|------|------|
| cuda:0 | 100% | 71.7 / 97.9 GB | 84°C |
| cuda:1 | 100% | 71.7 / 97.9 GB | 84°C |

### 磁盘

`/root/autodl-tmp`: 88GB 可用 (65%)，checkpoint 写入无问题。

---
