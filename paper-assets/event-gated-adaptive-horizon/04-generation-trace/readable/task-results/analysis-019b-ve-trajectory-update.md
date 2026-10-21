# analysis 019b ve trajectory update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_019b-ve-trajectory-update_20260517T104423_result.json`
- **Structured JSON:** [`def0f70f0d48bd25761c.json`](../../sessions/de/def0f70f0d48bd25761c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 写入完成。

## Summary

**exp_019b PickCube CIVO Trigger V/E 轨迹** (14 eval points, step 2500-132500):

| 指标 | 值 |
|---|---|
| **Peak NVE** | **3.78x** @ step 52500 |
| **Final NVE** | **0.079x** @ step 132500 |
| **Pattern** | **spike-then-deflation** |

关键观察：
- NVE 在 step 52500 达到峰值 3.78x（此时 eval_return 仅 3.69，但 value_mean 高达 20.85，value 严重高估）
- 之后 NVE 持续下降至 0.079x，value_mean 从 27.17 降至 4.35，而 eval_return 在最后一个 step 回升到 26.87
- **Gate 完全锁死**：全程 gate_dt_2_frac=1.0，gate_empirical_entropy=0.0，gate 未发生任何切换
- Baseline（019a_v2）的 value_mean 持续单调上升至 144.57，V/E ratio 稳定在 2.0-2.8x 区间

核心问题：CIVO trigger 的 gate 从未被激活（entropy=0, dt 始终固定为 2），value function 出现先过估后崩溃的 spike-then-deflation 模式。

---
