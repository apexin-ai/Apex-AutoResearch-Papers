# analysis recency s025

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_recency_s025_20260517T005601_result.json`
- **Structured JSON:** [`caf281286ef2498a9d83.json`](../../sessions/ca/caf281286ef2498a9d83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE/success。

## 结果总结

**recency_s025** 对照实验结论：**SUCCESS（nuanced）**

关键发现：
- recency s=0.25 确实有显著 phase gradient（p=0.009），但方向与 importance-based **完全相反**
- **Importance**: high_sparsity phases 受损更重（dz=-0.78）
- **Recency**: low_sparsity phases 受损更重（dz=+0.22，效应量小 3.5 倍）

这比 recency_s015 的 NS 结果（p=0.77）提供了更强的证据：不仅梯度方向相反，而且机制不同。Recency 损伤集中注意力阶段（那里模型依赖被驱逐的旧 token），importance 损伤稀疏注意力阶段（那里剩余注意力已经很薄）。PACS 现象确认是 attention-score-specific 的，不是 positional artifact。

---
