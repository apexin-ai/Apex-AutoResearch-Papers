# analysis exp 032 dual critic walker

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_032_dual_critic_walker_20260521T074655_result.json`
- **Structured JSON:** [`72a9fc10235ef951fae8.json`](../../sessions/72/72a9fc10235ef951fae8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**exp_032_dual_critic_walker — conclusion: success**

| 指标 | 值 |
|------|-----|
| NVE peak | 1.1 (95K) — 远低于 1.5× 阈值 |
| NVE final | 0.1 |
| Eval peak | 787.7 (205K) |
| Eval final | 739.7 (215K) |
| v1-v2 gap | <0.1%，min 操作无 pessimism 效应 |
| Gate | dt=2 collapsed, 100% |

与 exp_032b (seed=1) 一致：两个 seed 均确认 dual-critic 抑制 CIVO。seed=0 eval 显著高于 seed=1 (787.7 vs 551.8 peak)，但 CIVO 抑制模式相同。

注意点：v1≈v2 说明 dual-critic 抑制 CIVO 的实际机制不是 min-of-two pessimism，可能是隐式的 value function 正则化。Gate 坍塌仍然存在，adaptive horizon 在 dual-critic 下未被测试。

---
