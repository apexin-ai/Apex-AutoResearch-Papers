# analysis exp 009c 008f walker s2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_009c_008f_walker_s2_20260514T141709_result.json`
- **Structured JSON:** [`8f462f24710eb0c4e1eb.json`](../../sessions/8f/8f462f24710eb0c4e1eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。训练正常结束（EXIT_CODE=0），无报错。

**结论：NEGATIVE**

| 对比维度 | 008f seed 1 | 009c seed 2 |
|----------|-------------|-------------|
| eval_return@105K | 503 | 148 |
| peak eval_return | 503@105K（上升中）| 359@75K（之后连跌3次）|
| normalized v/e@105K | 0.30x | 1.14x |
| vs baseline@105K | -45.1% | -83.8% |
| 趋势 | zigzag recovery | rise-then-decay |

Seed 2 未复现 seed 1 的 zigzag recovery 模式。75K 后 eval_return 单调下降（359→227→191→148），value_mean 却持续上升（84→96→108→111），v/e ratio 从 0.23 升至 0.75，说明 value function 与实际表现脱节加剧。虽未达到 1.5x delusional critic 阈值，但 008f 配置的因果控制效果 **seed-dependent，不 robust**。

---
