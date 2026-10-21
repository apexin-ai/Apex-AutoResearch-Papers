# code q3 bcs distribution

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_q3-bcs-distribution_20260517T075611_result.json`
- **Structured JSON:** [`b36c73b63a9847c15d90.json`](../../sessions/b3/b36c73b63a9847c15d90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果非常清晰。

## 结论

**Train-origin 和 val-origin types 的 BCS 分布没有 systematic difference。**

关键数据：

| Group | N_pairs | Mean | Std | Median |
|-------|---------|------|-----|--------|
| Train-Train | 2016 | 0.8801 | 0.0693 | 0.8996 |
| Val-Val | 120 | 0.8738 | 0.0847 | 0.9015 |
| Cross | 1024 | 0.8774 | 0.0763 | 0.8976 |

统计检验：
- Mann-Whitney U: p = 0.754 (远不显著)
- KS test: D = 0.088, p = 0.326 (不显著)
- Cohen's d = 0.081 (negligible effect size, < 0.2 threshold)
- BCS(train) = 0.880, BCS(val) = 0.874, 差异仅 0.006

**解读**：两组 types 来自同一 similarity 分布，split origin 不引入 confound。Within-pool analysis 的有效性不受 train/val 来源影响。

### 产出
- 脚本：`/root/schema-dag-extraction/scripts/q3_bcs_distribution.py`
- 图表：`/root/schema-dag-extraction/figures/paper/fig_q3_bcs_distribution.pdf`
- LaTeX 表格片段已在上方输出中

对 reviewer 的回复要点：三组 (within-train, within-val, cross) 的 pairwise SCS 分布在 mean、median、shape 上几乎相同，Mann-Whitney p=0.75，Cohen's d=0.08，说明 FewRel 的 train/val split 在 schema confusability 维度上是均匀的。

---
