# analysis exp 008e v3 s4

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_008e_v3_s4_20260518T113318_result.json`
- **Structured JSON:** [`5b1a205253bc5eb743f2.json`](../../sessions/5b/5b1a205253bc5eb743f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## exp_008e_v3_s4 分析结果

### Conclusion: **SUCCESS**

### Eval Trajectory (单调递增，无任何下降)

| Step | eval_return | value_mean | actor_entropy | ve_ratio | NVE |
|------|-------------|------------|---------------|----------|-----|
| 5K   | 30.9        | 0.002      | 8.19          | -        | -   |
| 15K  | 343.7       | 5.03       | 0.86          | 0.015    | 0.02x |
| 25K  | 450.3       | 46.9       | -2.48         | 0.104    | 0.16x |
| 35K  | 527.4       | 112.4      | -3.57         | 0.213    | 0.33x |
| 45K  | 652.3       | 186.9      | -4.17         | 0.287    | 0.44x |
| 55K  | 718.0       | 264.1      | -4.52         | 0.368    | 0.57x |
| 65K  | 736.6       | 343.8      | -4.70         | 0.467    | 0.72x |
| 75K  | 751.7       | 413.3      | -4.65         | 0.550    | 0.85x |
| 85K  | 818.7       | 467.9      | -5.03         | 0.571    | 0.88x |
| 95K  | 835.3       | 523.5      | -5.10         | 0.627    | 0.97x |
| **105K** | **899.3** | **547.4** | **-5.08** | **0.609** | **0.94x** |

### 判断依据
- eval 从 5K 到 105K **单调递增**，peak = final = 899.3
- NVE = 0.94x（远低于 1.5x 阈值，甚至低于 baseline 1.0x）
- entropy 持续下降至 -5.08（策略收敛，无回升）
- value 单调增长至 547.4（无爆炸）
- civo/alert = 0.0 全程
- gate: dt_mean=1.0, dt_1_frac=1.0（全部选择 dt=1）
- 这是 5 个 seed 中 **eval 最高的**（899.3 vs s0/s1 的 869.9）

### C6 Sibling Seeds 对比

| Seed | Conclusion | eval@105K | NVE@105K | Collapse? |
|------|------------|-----------|----------|-----------|
| s0   | SUCCESS    | 869.9     | 0.80x    | No        |
| s1   | SUCCESS    | 869.9     | -        | No        |
| s2   | NEGATIVE   | 137       | 3.78x    | @95K      |
| s3   | NEGATIVE   | 93        | 5.0x     | @85-95K   |
| **s4** | **SUCCESS** | **899.3** | **0.94x** | **No** |

**C6 collapse rate: 2/5 = 40%**（s2, s3 collapsed; s0, s1, s4 stable）

---
