# research bernoulli st pessimism design

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bernoulli_st_pessimism_design_20260514T034834_result.json`
- **Structured JSON:** [`9809d43968820deaf419.json`](../../sessions/98/9809d43968820deaf419.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计文档已写入 `artifacts/pessimism_mechanism_design.md`。

关键结论：

- **方案 A（Twin Critic）**：改 `ImagBehavior` 加第二个 critic，`_compute_target` L671 用 `min(v1,v2) - β·|v1-v2|`。稳健但开销大、新颖性低。
- **方案 B（Reward Discount）**：仅在 `_compute_target` L665-693 间加 5 行 reward 衰减。最简单但启发式、不治根因。
- **方案 C（Partial Freeze）**：冻结 `RSSM._dt_embedding.weight[1]`（dt=2 的 embedding），使 dt=2 预测天然不准确 → 结构性悲观。零超参、零开销、直接命中根因、最具论文新颖性。

推荐 **C 优先、A 备选**。

---
