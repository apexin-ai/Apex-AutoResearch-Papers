# analysis 016e midrun nve

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_016e_midrun_nve_20260515T221945_result.json`
- **Structured JSON:** [`eb8e6633ef181b3fe450.json`](../../sessions/eb/eb8e6633ef181b3fe450.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：016e CIVO 已确认，NVE = 6.59x。**

关键数据：
- eval_return：326.67 (75K peak) → 256.21 (85K) → **31.73 (95K)**，并非回落而是崩溃
- Critic 估计 value_mean ≈ 209，几乎未动，与实际 return 31.73 严重脱节
- Actor entropy -3.83 → -4.65，策略已坍缩到过确定化
- 比 008d (NVE 4.12x) 更严重，不可能在剩余 ~10K steps 内恢复

Registry notes 和诊断报告 (`art_20260515_27c8c8`) 已更新。

---
