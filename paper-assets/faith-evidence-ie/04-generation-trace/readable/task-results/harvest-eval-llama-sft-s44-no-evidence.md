# harvest eval llama sft s44 no evidence

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval-llama-sft-s44-no-evidence_20260520T170140_result.json`
- **Structured JSON:** [`56b1fdd8311081cdef8b.json`](../../sessions/56/56b1fdd8311081cdef8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron job（可能在之前的 session 中已清理或过期）。Registry 已更新为 DONE。

```
状态: success
Metrics: ign_f1=0.3326, f1=0.3348, format_ok=931/985 (94.5%), truncated=411/985
Fair Comparison: raw_tax=-14.76pp, fair_tax=-12.62pp, fair_subset=931 docs
  With-evi: ign_f1=0.4802 (full) / 0.4742 (fair)
  No-evi:   ign_f1=0.3326 (full) / 0.3481 (fair)
```

注意：s44 的 evidence tax 远大于 s42 的 -1.65pp，主要原因是 no-evidence 模型 format_ok 只有 94.5%（54 docs 失败，其中 52 是 truncation），recall 大幅下降（0.2648 vs 0.4915）。no-evidence 模型在没有 evidence 约束后 precision 反而没有提升（0.4346 vs 0.4695），recall 却腰斩，说明 evidence 作为结构化约束对模型输出质量有正面作用。

---
