# analysis exp hopper frozen s0 ext

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_hopper_frozen_s0_ext_20260527T105310_result.json`
- **Structured JSON:** [`608230730f76784b988d.json`](../../sessions/60/608230730f76784b988d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE (negative)，报告已注册。

**结论：假设被否定。**

| 指标 | trained_s0_ext | frozen_s0_ext |
|------|---------------|---------------|
| eval_return | 3.26 → 81.58 (恢复) | 0 → 0.56 (无恢复) |
| ve_ratio | 0.897 → 0.44 (下降) | 4.3M → 15.08 (持续高) |
| value_mean | 2.93 → 35.81 (跟踪真实表现) | 4.34 → 8.46 (phantom value) |

frozen_s0 的近零表现不是暂态不稳定——是**结构性学习失败**。frozen embedding 无法适应，价值函数学到的是与实际回报完全脱节的幻影价值。这与 trained_s0_ext 的恢复模式根本不同。

---
