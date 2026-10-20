# ops 008e v3 fresh metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_008e_v3_fresh_metrics_20260514T071355_result.json`
- **Structured JSON:** [`0e5b8248719be6987ab3.json`](../../sessions/0e/0e5b8248719be6987ab3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。趋势判断：

**eval_return**：单调递增，65K 达到 580.7，学习曲线健康。对 walker_walk 来说这个进度正常。

**normalized v/e**：从 25K 的 1.93x 快速下降到 65K 的 **0.72x**，远低于 1.2x 阈值。value function 相对 baseline 更保守，说明 subsample ON（含 dt=2 transitions）并未导致 value 过估——反而偏保守。

**关键结论**：exp_008e_v3 表现接近 baseline，subsample ON + dt=1 imagination 的组合没有造成明显性能下降。gate_dt 全程锁定 1.0（符合 fixed_dt=1 设定）。剩余 ~37K steps，预估还需 ~1.5h 完成。

---
