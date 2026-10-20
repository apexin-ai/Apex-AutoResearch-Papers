# research sigma comparison

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sigma-comparison_20260521T090350_result.json`
- **Structured JSON:** [`3503e9b79b7a2ec114fb.json`](../../sessions/35/3503e9b79b7a2ec114fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**SIGMA 共 8 个指标**，其中：
- **1 个直接可比**：我们的 SLV = ½ × SIGMA 的 log det(G)，已有全部 11 代数据，零额外成本
- **3 个可从现有 checkpoints 计算**：Track I (𝒢_KF)、Track II (𝒰_LLN,cov)、及其 drift 版本。需 ~2h 开发 + 6min GPU，基于 `compute_alternative_ews_v2.py` 的 `collect_embeddings()` 改造
- **2 个需补算生成文本指标**：Distinct-2（我们有 Distinct-4 但缺 2-gram 版）和 HHI，~1h
- **2 个不建议对比**：Overestimation Ratio ℛ（需真实分布协方差）和理论 bounds

最小可行方案：先用已有 SLV drift 做定性对比（免费），再实现 Track I/II（半天内可完成）。

---
