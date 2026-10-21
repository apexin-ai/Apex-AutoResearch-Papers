# analysis fk independence test

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fk_independence_test_20260515T044252_result.json`
- **Structured JSON:** [`5bf4e6070f70211ddfdb.json`](../../sessions/5b/5bf4e6070f70211ddfdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `fk_independence_test.json`。核心发现：

### 结果汇总

| 配置 | N | Observed Agr. | Chance Agr. | Excess | ICC | Split-half Jaccard |
|------|---|---------------|-------------|--------|-----|-------------------|
| Qwen SciERC | 528 | 0.7485 | 0.7799 | **-0.0314** (-4.0%) | 0.8372 | 0.7418 |
| LLaMA SciERC | 527 | 0.7741 | 0.8023 | **-0.0282** (-3.5%) | 0.8835 | 0.7632 |
| Qwen CoNLL | 2749 | 0.8889 | 0.9028 | **-0.0139** (-1.5%) | 0.9227 | 0.8536 |
| LLaMA CoNLL | 2741 | 0.9720 | 0.9755 | **-0.0035** (-0.4%) | 0.9963 | 0.9692 |

### 结论

**Excess agreement 在所有配置上均为负值**（平均 -0.019），意味着温度采样的 pairwise agreement 实际上**低于**独立 rater 的期望水平。

原因：温度采样在 entity 边界上引入了**互补性变异**——同一文本位置的不同边界选择（如 "morphological analysis" vs "morphological analysis in Japanese text processing"）在 sample 间形成负相关（inter-entity φ 均为负值：-0.10 至 -0.54），使 sample 间的实际一致性略低于独立抽样预期。

**对 FK 的影响**：FK 假设 rater 独立。温度采样的独立性偏离方向是**保守的**——不会高估 agreement，因此 FK 值不会被虚假膨胀。独立性假设的违背程度轻微且方向安全，FK 作为 inter-rater agreement 度量在此场景下是可靠的。

高 ICC（0.84–0.996）表明 entity **数量**在 sample 间高度一致（共享 prompt 约束），但这不影响 FK 的有效性，因为 FK 衡量的是具体 entity 的一致而非数量。

---
