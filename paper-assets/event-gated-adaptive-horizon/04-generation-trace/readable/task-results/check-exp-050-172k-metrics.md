# check exp 050 172k metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_050_172k_metrics_20260523T053608_result.json`
- **Structured JSON:** [`2c4a671bdb1ac87a6afd.json`](../../sessions/2c/2c4a671bdb1ac87a6afd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_050 PegInsertion 指标趋势

**当前步数：172,500（update_count=85,100）**

### ve_ratio 完整趋势

| Step | ve_ratio | eval_return |
|-----:|--------:|------------:|
| 12.5K | 0.21 | 9.56 |
| 22.5K | 0.74 | 14.21 |
| 32.5K | 1.90 | 10.00 |
| 42.5K | 2.67 | 10.70 |
| 52.5K | 7.10 | 5.40 |
| 62.5K | 3.14 | 14.13 |
| 72.5K | 6.17 | 7.90 |
| **82.5K** | **10.05** | 4.53 |
| 92.5K | 9.55 | 3.65 |
| 102.5K | 4.55 | 6.23 |
| 112.5K | 4.02 | 6.67 |
| 122.5K | 2.63 | 10.43 |
| 132.5K | 3.75 | 7.20 |
| 142.5K | 3.20 | 7.72 |
| **152.5K** | **8.46** | 2.40 |
| 162.5K | 1.94 | 9.01 |
| **172.5K** | **3.13** | 4.77 |

### 分析

ve_ratio 从 152.5K 的 8.46 峰值 → 162.5K 的 1.94 → 172.5K 的 3.13，**下降趋势没有持续，出现了反弹**。整体呈锯齿形波动模式，有两个明显高峰区间：82.5K-92.5K（~10）和 152.5K（8.46），之间会回落到 2-4 区间。

eval_return 同样波动剧烈（2.40~14.21），无明显上升趋势。ve_ratio 与 eval_return 呈**负相关**：ve_ratio 高点（82.5K=10.05, 152.5K=8.46）对应 eval_return 低谷（4.53, 2.40）。

gate_dt 始终锁死在 dt=2（gate_dt_2_frac=1.0），门控没有学到自适应行为。

### exp_051 StackCube 状态

Step 174,000，train_return 在 24.8-27.0 之间，870 episodes。运行正常。

---
