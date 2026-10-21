# analysis qwen L14 results urgent

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen-L14-results-urgent_20260522T150412_result.json`
- **Structured JSON:** [`8ad5b5e0ac20cc4fd4c8.json`](../../sessions/8a/8ad5b5e0ac20cc4fd4c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

## Qwen L14 Steering 结果

| α | Steering flips | Control flips | p→c | c→p | Fisher p |
|---|---|---|---|---|---|
| -20 | 4/84 | 6/84 | 0 | 0 | 0.746 |
| -10 | 2/84 | 4/84 | 0 | 0 | 0.682 |
| -5 | 2/84 | 3/84 | 0 | 0 | 1.000 |
| +5 | 1/84 | 1/84 | 0 | 0 | 1.000 |
| +10 | 3/84 | 2/84 | 0 | 0 | 1.000 |
| +20 | 5/84 | 3/84 | 0 | 0 | 0.720 |

**结论：NEGATIVE**

- 所有 alpha 的 Fisher p 均远大于 0.05（最低 0.682），无显著因果效应
- p→c 和 c→p 全部为 0，完全没有方向性翻转
- Steering flips 与 control flips 处于同一噪声水平

**与 Llama L13 对比：截然不同**

| | Llama L13 | Qwen L14 |
|---|---|---|
| α=-20 Fisher p | **0.0009** | 0.746 |
| α=+5 Fisher p | **0.002** | 1.000 |
| 方向性分离 | 有（p→c / c→p 分离） | 无（全部为 0） |

Qwen L14 的 probe accuracy (70.2%) 虽然合理，但 probe 方向不具因果效应。mid-layer causal node 在 Qwen 上不成立，至少不在 L14。可能原因：Qwen 的知识冲突解决机制分布在不同层，或 probe 捕获的是相关性而非因果方向。

cuda:1 已释放（3 MiB），GPU 0/1 空闲可用。

---
