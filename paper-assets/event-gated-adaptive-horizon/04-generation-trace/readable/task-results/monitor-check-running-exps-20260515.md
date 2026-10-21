# monitor check running exps 20260515

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_check_running_exps_20260515_20260515T011247_result.json`
- **Structured JSON:** [`5bfa69040e1337f4b636.json`](../../sessions/5b/5bfa69040e1337f4b636.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

### 1. exp_008e_v3_walker_s2 (PID 43437)

| 指标 | 值 |
|------|-----|
| 当前 step | **8,000 / 105,000** |
| 进度 | **7.6%** |
| 运行时间 | 26m20s |
| 最新 eval_return | 39.27 @ 5K（仅1个eval点） |
| value_mean @ 5K | 0.00193 |
| v/e ratio | ~0.00005（过早，无参考意义） |
| gate_dt_mean | 1.0（dt=1 占 100%，gate 尚未激活） |

刚启动不久，数据点太少，无法与 s1 对比。

---

### 2. exp_009a_baseline_walker_s2 (PID 142508)

| 指标 | 值 |
|------|-----|
| 当前 step | **368,000 / 500,000** |
| 进度 | **73.6%** |
| 运行时间 | 15h40m |
| 最新 eval_return | **943.13 @ 365K** |
| value_mean @ 365K | 664.18 |
| v/e ratio @ 365K | **0.704** |
| FPS | 3.42 |

**eval_return 轨迹（关键 checkpoint）：**

| Step | eval_return | 趋势 |
|------|-------------|-------|
| 25K | 325.3 | 快速上升 |
| 65K | 688.9 | |
| 105K | **836.5** | ← 与 s1 对比点 |
| 135K | 876.1 | |
| 185K | 907.3 | |
| 215K | **956.0** | 峰值区 |
| 245K | 950.3 | |
| 285K | **960.2** | 历史最高 |
| 345K | 816.2 | 偶发回落 |
| 365K | 943.1 | 恢复 |

**200K+ 后在 900-960 区间波动，已趋于收敛。**

---

### 与 seed 1 对比（@ 105K）

| 实验 | eval_return @ 105K | v/e ratio |
|------|-------------------|-----------|
| **008e_v3_s1** | **869.9** | **0.527** |
| **009a_baseline_s2** | 836.5 | 0.704 |
| **008e_v3_s2** | 尚未到达 | — |

Baseline s2 在 105K 时 eval_return 比 v3 s1 低约 33 分（836.5 vs 869.9），但 v/e ratio 更高（0.704 vs 0.527），说明 baseline 的 value function 相对高估。

### 异常信号
- **008e_v3_s2 的 CPU%=0.0**：PID 存活但 CPU 使用率为 0，可能处于 eval 阶段或等待 GPU。如果长时间无进展需关注。
- **009a 在 345K 处 eval 回落到 816**：单次波动，365K 已恢复到 943，非系统性退化。
- 两个进程 RSS 都很低（~3.4MB），实际计算在 GPU 上，属正常。

---
