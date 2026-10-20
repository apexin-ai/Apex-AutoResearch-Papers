# analysis gradient decomposition timeline

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient-decomposition-timeline_20260516T133312_result.json`
- **Structured JSON:** [`bbec405e2b9b76bebe2e.json`](../../sessions/bb/bbec405e2b9b76bebe2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验（exp_018 和 exp_008d）都**只有一个 `latest.pt` checkpoint**，没有中间步骤的存档。这是 DreamerV3 的默认行为——只保存最新状态，覆盖式更新。

**结论：只有最终 checkpoint，无法回溯中间步骤（25K/50K/75K/100K）的梯度分解。** 要获取训练过程中的梯度演变数据，需要在训练时配置多 checkpoint 保存策略（如每 25K step 保存一份），然后重新训练。

---
