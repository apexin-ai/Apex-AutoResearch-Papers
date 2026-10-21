# analysis gemma L17 steering results

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma-L17-steering-results_20260522T163015_result.json`
- **Structured JSON:** [`b7fa3044de4dbad341a6.json`](../../sessions/b7/b7fa3044de4dbad341a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

## Gemma L17 Steering — **NEGATIVE**

| Alpha | Steering Flips | Control Flips | Fisher p | p2c | c2p |
|-------|---------------|---------------|----------|-----|-----|
| -20 | 2 (1.3%) | 8 (5.1%) | 0.104 | 0 | 0 |
| -10 | 2 (1.3%) | 2 (1.3%) | 1.000 | 0 | 0 |
| -5 | 2 (1.3%) | 1 (0.6%) | 1.000 | 0 | 0 |
| +5 | 1 (0.6%) | 3 (1.9%) | 0.623 | 0 | 0 |
| +10 | 2 (1.3%) | 2 (1.3%) | 1.000 | 0 | 0 |
| +20 | 1 (0.6%) | 4 (2.5%) | 0.371 | 0 | 0 |

- **probe_accuracy**: 75.3%（探针本身可以检测冲突，但方向不具有因果意义）
- **零方向性 flip**：所有 alpha 的 p2c 和 c2p 都是 0
- **无显著 alpha**：最低 Fisher p = 0.104

## Steering 全局结论

| 模型 | 层 | 结果 |
|------|-----|------|
| **Llama L13** | 41% depth | **SUCCESS** (p<0.001, 双向) |
| Llama L18 | 56% depth | negative |
| Llama L28 | 88% depth | negative |
| Qwen L14 | 39% depth | negative |
| Qwen L23 | 64% depth | negative |
| **Gemma L17** | **40% depth** | **negative** |

Steering 因果效应是 **Llama-specific**（1/3 模型）。L21 实验仍在运行中，但预期也是 negative。

---
