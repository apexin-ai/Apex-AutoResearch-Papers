# paper related work additions

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_related_work_additions_20260516T092241_result.json`
- **Structured JSON:** [`d043bb403097f7070379.json`](../../sessions/d0/d043bb403097f7070379.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。新增内容：

1. **QAQ** — `related_work.tex` KV Cache Quantization 段落末尾，区分 attention-score-based 动态方法 vs 我们的 offline profiling + cardinality constraint。bib 条目 `dong2024qaq` 已添加。

2. **AQLM/QuIP#** — Mixed-Precision Quantization (Weights) 段落，作为 non-additive error 的 conceptual parallel。bib 条目 `egiazarian2024aqlm` 和 `tseng2024quipsharp` 已添加。

3. **KVTuner** — Mixed-Precision Rate-Distortion Allocation 段落，区分 layer-level vs head-level granularity，cardinality constraint 使更大搜索空间可控。已有 bib 条目 `li2025kvtuner`。

---
