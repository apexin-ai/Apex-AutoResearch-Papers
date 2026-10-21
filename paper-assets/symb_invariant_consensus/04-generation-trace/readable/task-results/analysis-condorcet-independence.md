# analysis condorcet independence

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_condorcet-independence_20260519T010903_result.json`
- **Structured JSON:** [`37ff2fe0f7e5a875b7d2.json`](../../sessions/37/37ff2fe0f7e5a875b7d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

### Cross-Model Comparison

| Model | n | SC Acc | Agreement | Expected | Kappa | Eff K |
|-------|---|--------|-----------|----------|-------|-------|
| Mistral-7B | 204 | 0.544 | 0.688 | 0.721 | **0.501** | **1.82** / 10 |
| Qwen2.5-14B | 204 | 0.750 | 0.833 | 0.847 | **0.739** | **1.31** / 12 |

### Per Entropy Bin

| Model | Bin | n | SC Acc | Kappa | Eff K |
|-------|-----|---|--------|-------|-------|
| Mistral-7B | low | 73 | 0.740 | 0.932 | 1.06 |
| Mistral-7B | medium | 65 | 0.523 | 0.422 | 2.09 |
| Mistral-7B | high | 66 | 0.349 | 0.086 | 5.65 |
| Qwen2.5-14B | low | 120 | 0.867 | 1.000 | 1.00 |
| Qwen2.5-14B | medium | 26 | 0.808 | 0.611 | 1.55 |
| Qwen2.5-14B | high | 58 | 0.483 | 0.267 | 3.05 |

### 关键结论

1. **Fleiss' Kappa 极高**：Mistral 0.50，Qwen-14B 0.74。Traces 远非独立。

2. **Effective K 极低**：Mistral 名义 K=10（有效 traces），实际等效 1.82 个独立 trace；Qwen-14B 名义 K=12，实际等效仅 1.31。更强的模型反而独立性更差。

3. **低 entropy 问题（模型确定的问题）**：Kappa 接近 1.0，Effective K ≈ 1.0。12 条 traces 等于 1 条。

4. **高 entropy 问题（模型不确定的问题）**：Kappa 明显下降（Mistral 0.086，Qwen 0.267），Effective K 回升到 3-6。但即使在最不确定的问题上，12 条 traces 也只等效 3-6 条独立 trace。

5. **Qwen-14B 有 120/204 问题 12 条 trace 完全一致**（entropy=0），这些问题完全没有从 SC 投票中获益。

Raw violation 因 finite-sample bias 始终 ≤ 0，Fleiss' Kappa 是更可靠的指标。结果已保存到 `results/condorcet_independence_analysis.json`。

---
