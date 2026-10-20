# analysis multiseed flip overlap

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multiseed_flip_overlap_20260515T113411_result.json`
- **Structured JSON:** [`01f006122dc021cb2f0a.json`](../../sessions/01/01f006122dc021cb2f0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Jaccard ~0.42** — 中等稳定性，LP failure pattern 部分 systematic 但不够 robust。

关键数据点：
- 3-seed stable failures: 34/551 instances（排除 0-gold-rel 后 24 个）
- Gold relation 数与 failure rate 强正相关（1 rel → 4.3%, 6 rels → 26.2%）
- Flip instances 仅 5-6 个，太少做独立论点
- LP 在 sample 级别极不稳定（1.5% 三种子一致），但 instance 级别中等稳定
- Constrained vs free-form LP delta 相关 r=0.52

**Section 5 建议**: 用中等措辞——"LP failures are partially systematic, driven by instance complexity"。Flip instances 只适合作为 illustrative example 提及，不适合作为独立 subsection。完整 Jaccard 矩阵和 stable failure 列表放 appendix。

报告已写到 `artifacts/multiseed_flip_overlap_analysis.md` 并注册。

---
