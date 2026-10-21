# fetch paired constrained perbatch

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fetch_paired_constrained_perbatch_20260520T041146_result.json`
- **Structured JSON:** [`ac6eb122150b066a3999.json`](../../sessions/ac/ac6eb122150b066a3999.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/exp_paired_constrained/data/per_batch_results.json`。

关键发现：
- 25 个 batch 中，23 个 constrained 和 unconstrained accuracy 完全相同
- 仅 high_5 和 high_11 各差 1 个样本（1/96 ≈ 1.04pp）
- 整体 acc 差异仅 -0.08pp（constrained 0.7950 vs unconstrained 0.7958）
- Pearson r 几乎一致：constrained -0.4479 vs unconstrained -0.4393（均 p<0.03）
- Spearman rho 也一致：constrained -0.1566 vs unconstrained -0.1442（均不显著）

---
