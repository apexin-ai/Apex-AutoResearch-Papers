# exp capacity scaling episode eval

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_capacity-scaling-episode-eval_20260516T124153_result.json`
- **Structured JSON:** [`c1d5b15d01b331aafc7b.json`](../../sessions/c1/c1d5b15d01b331aafc7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Capacity Scaling Episode-Level Eval 完成。** 结果汇总：

| Model | Mean bal_acc | Std |
|-------|-------------|-----|
| 0.6B | 0.5067 | ±0.0262 |
| 1.7B (ref) | 0.4710 | ±0.0220 |
| 4B | **0.5896** | ±0.0194 |

趋势：容量越大 balanced_acc 越高，且 variance 越小。4B 相比 1.7B 提升约 +11.9pp，0.6B 反而略高于 1.7B 约 +3.6pp（可能因为 v4 训练配置优化）。

结果已保存到 `/root/autodl-tmp/simgate-modular-routing/results/capacity_episode_eval/summary.json`。

---
