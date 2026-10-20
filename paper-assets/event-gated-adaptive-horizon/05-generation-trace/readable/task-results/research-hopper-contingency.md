# research hopper contingency

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_hopper-contingency_20260529T082428_result.json`
- **Structured JSON:** [`9c41463a413c4a9aa7f2.json`](../../sessions/9c/9c41463a413c4a9aa7f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已产出并注册。核心结论：

1. **Hopper 代码完全可用**，task string 是 `dmc_hopper_hop`（注意：DMC 没有 "hopper_walk"，只有 stand 和 hop）
2. **历史 kill 全是设计决策**（批次替换/结论已出），无技术障碍
3. **已有完整 baseline 数据**可复用：`exp_hopper_baseline` eval_return=96.43, NVE 稳定
4. **关键风险**：Hopper + gate 的 failure mode 是 severe learning delay，不是标准 CIVO。如果目的是做 "clean CIVO isolation"，baseline NVE 确实干净，但 gate 实验不会复现 Walker/Cheetah 式的 value overestimation pattern。

---
