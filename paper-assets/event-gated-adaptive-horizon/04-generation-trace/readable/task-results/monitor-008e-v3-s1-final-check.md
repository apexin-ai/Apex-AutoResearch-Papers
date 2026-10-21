# monitor 008e v3 s1 final check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_008e_v3_s1_final_check_20260514T223908_result.json`
- **Structured JSON:** [`fdc19250c8c63e4dd5d3.json`](../../sessions/fd/fdc19250c8c63e4dd5d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_008e_v3_walker_s1 状态汇总

**进程状态**: RUNNING (PID 898127)
**当前进度**: ~85K+ / 105K（metrics.jsonl 最后 eval 在 85K，训练继续中）

### Eval 指标表

| Step | eval_return | value_mean | v/e ratio | baseline v/e | normalized |
|------|------------|------------|-----------|-------------|------------|
| 5K   | 31.00      | 0.00       | 0.000     | —           | —          |
| 15K  | 131.17     | 4.00       | 0.031     | —           | —          |
| 25K  | 155.69     | 26.19      | 0.168     | 0.087       | **1.931**  |
| 35K  | 276.47     | 62.76      | 0.227     | 0.241       | 0.942      |
| 45K  | 382.22     | 110.67     | 0.290     | 0.331       | 0.876      |
| 55K  | 486.84     | 170.09     | 0.349     | 0.404       | 0.864      |
| 65K  | 580.67     | 235.05     | 0.405     | 0.563       | 0.719      |
| 75K  | 574.09     | 300.51     | 0.523     | 0.719       | 0.728      |
| 85K  | 657.31     | 351.33     | 0.534     | 0.701       | 0.762      |

### Gate 统计

**gate_dt_mean = 1.0, gate_dt_1_frac = 1.0** （所有步骤一致）

门控完全锁死在 dt=1，从未学会使用自适应时间步长。gate_empirical_entropy = 0.0，gate_entropy_ratio = 0.0。

### 分析

- **eval_return** 稳步上升，85K 时达到 657.3（表现不错）
- **v/e ratio** 持续低于 baseline（除 25K 外），且差距在 65K-85K 阶段稳定在 ~0.72-0.76x baseline
- **核心问题**：gate 完全不工作，始终输出 dt=1，等价于标准 DreamerV3（无自适应行为）。v/e ratio 低于 baseline 说明 value function 校准略差于纯 baseline
- 预计还需 ~50 分钟到达 105K（按 6.5 fps 估算）

---
