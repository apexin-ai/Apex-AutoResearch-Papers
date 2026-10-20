# ssh b3 results collection

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_b3-results-collection_20260520T130911_result.json`
- **Structured JSON:** [`fa1056052a3c5644315e.json`](../../sessions/fa/fa1056052a3c5644315e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved to `artifacts/b3_prompted_diversity/`.

## B3 Prompted Diversity — 结果汇总

**结论：负结果。Multi-template 采样在所有指标上都不如 single-template。**

### Construction F1

| Method | Single | Multi | Δ | p (bootstrap) |
|--------|--------|-------|---|---------------|
| greedy | 0.7441 | 0.7441 | 0.0000 | — |
| majority_vote | 0.7209 | 0.7102 | **-0.0107** | 0.991 |
| theta2n | 0.7618 | 0.7269 | **-0.0349** | 1.000 |
| lp_weighted | 0.7665 | 0.7308 | **-0.0356** | 1.000 |
| vc_weighted | 0.7723 | 0.7311 | **-0.0412** | 1.000 |

所有 construction 方法 multi-template 都显著更差（p ≥ 0.99）。vc_weighted 退化最严重（-4.1 F1）。

### Diversity（反直觉）

| Metric | Single | Multi |
|--------|--------|-------|
| unique_entities | **5.29** | 4.06 |
| pairwise_jaccard | **0.581** | 0.642 |

Multi-template 反而产生**更少**的 unique entities 和**更高**的 Jaccard（更相似/更低 diversity）。

Within-template Jaccard (0.474) < Cross-template Jaccard (0.670)：不同模板间的样本比同模板内的样本更相似——说明模板差异引入的是系统性偏移而非真正的多样性。

### Per-template Quality

C_descriptive 最弱（mean F1=0.575），A_standard 和 B_expert 最强（mean F1≈0.618）。Best-sample F1 在模板间差异不大（0.752–0.764）。

### Cross-template Agreement

模板对之间 agreement rate 在 0.855–0.916，说明模板设计差异有限，产出高度重叠。

### 解读

模型经过 fine-tuning 后对 prompt 变化不敏感——不同模板收敛到相似的 entity set，但非标准模板（C、D）引入了噪声（mean F1 下降），导致 construction 时信号被稀释。温度采样在单模板下已提供充分 diversity，多模板无额外增益。

---
