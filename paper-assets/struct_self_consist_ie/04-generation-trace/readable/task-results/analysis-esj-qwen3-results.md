# analysis esj qwen3 results

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_esj-qwen3-results_20260522T181930_result.json`
- **Structured JSON:** [`d3bcd8417377ed1575e5.json`](../../sessions/d3/d3bcd8417377ed1575e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

---

## exp_esj_qwen3_all 结果：**Negative**

### 核心数据

| Metric | SciERC | CoNLL | FewNERD |
|--------|--------|-------|---------|
| **Greedy F1** | 0.650 | 0.909 | 0.772 |
| **Best MV F1** | 0.647 | 0.907 | 0.764 |
| **Best ESJ F1** | 0.576 | 0.824 | 0.682 |
| **ESJ vs Greedy** | **-0.074** | **-0.085** | **-0.090** |
| ESJ entity ρ | 0.020 | 0.087 | -0.008 |
| ESJ entity AUROC | 0.512 | 0.553 | 0.495 |
| Agreement ρ | 0.515 | 0.777 | 0.673 |
| Agreement AUROC | 0.792 | 0.941 | 0.881 |
| Within-inst ESJ ρ | 0.056 | -0.008 | 0.332 |
| Within-inst LP ρ | 0.188 | 0.280 | 0.543 |

### 结论

**ESJ 在 Qwen3-8B finetuned 模型上完全失败，不支持 self-calibration claim。**

1. **Entity-level AUROC ≈ 随机** (0.495–0.553)，ρ 近零。P(yes) 与实体正确性无相关性。
2. **ESJ filtering 一致性地降低 F1**——在三个数据集上比 greedy 低 7–9 个点，比 MV 低 7–8 个点。
3. **ESJ 在 agreement 各分组内均无区分力**：disputed/mid/consensus 三组的 ESJ mean 几乎相同（FewNERD: 0.655/0.650/0.650），AUROC 均 ~0.49。
4. **Agreement 信号远优于 ESJ**：AUROC 0.79–0.94 vs 0.50–0.55。
5. **LP（log-probability）也一致优于 ESJ** 做 within-instance sample ranking。

模型无法通过 entailment verification 可靠地自我校准——P(yes) 分布不编码实体质量信息。

---
