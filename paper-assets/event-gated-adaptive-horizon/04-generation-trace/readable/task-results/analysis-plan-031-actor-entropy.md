# analysis plan 031 actor entropy

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_031_actor_entropy_20260525T100450_result.json`
- **Structured JSON:** [`4238c7952533a13930eb.json`](../../sessions/42/4238c7952533a13930eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**Actor entropy 不是 CIVO collapse 的区分指标。** 在可比时间点（55K step），collapsed 组均值 -5.02 vs healthy 组均值 -5.05，差异仅 0.03 nats。

关键结论：
1. **Actor 在 collapse 期间保持高置信度。** fixed_dt2 的 entropy 稳定在 -5.1，但 return 从 580 崩溃到 29——actor 没有"困惑"，而是自信地执行错误策略
2. **Collapse 机制是 critic 侧的。** 非正常的 value estimates 驱动崩溃，不是 actor 的 policy 结构退化
3. **Baseline 的 entropy 回升（-5.2→-1.5）伴随最佳性能（950 return）**，说明 entropy 上升本身不是病理信号
4. **论文意义**：强化了"delusional critic"叙事——应关注 value calibration 指标而非 actor entropy 作为诊断信号

报告已注册为 artifact `art_20260525_02b121`。

---
