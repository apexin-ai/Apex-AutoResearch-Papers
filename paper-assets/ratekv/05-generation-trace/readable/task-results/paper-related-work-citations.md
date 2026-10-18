# paper related work citations

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_related-work-citations_20260514T191436_result.json`
- **Structured JSON:** [`90213bc851f392953900.json`](../../sessions/90/90213bc851f392953900.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。变更总结：

**references.bib** — 添加 3 个 `@inproceedings` 条目：`fu2025headkv`、`feng2025adakv`、`li2025kvtuner`

**related_work.tex** — 两处修改：
- **KV Cache Eviction 段**（第 9 行）：新增一句引用 HeadKV 和 Ada-KV，说明 per-head eviction 验证了 head-level heterogeneity 可利用，并衔接到本文的 quantization 视角
- **Mixed-Precision 段**（第 15 行）：将 KVTuner 插入 layer-level 引用组，与 KVmix 并列，注明其 Pareto search 方法

第 10 行有一个多余空行，如需去除告诉我。

---
