# ops harvest llama no evidence eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_llama_no_evidence_eval_20260520T005857_result.json`
- **Structured JSON:** [`edf0060157aa59036cdd.json`](../../sessions/ed/edf0060157aa59036cdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。Cron 不存在（可能已在之前的 session 中删除）。

## 结果摘要

| 指标 | LLaMA-3.1-8B no-evidence | LLaMA-3.1-8B with-evidence |
|------|--------------------------|---------------------------|
| **ign_f1** | 0.5526 | 0.5839 |
| f1 | 0.5666 | — |
| format_compliance | 99.8% | — |
| n_truncated | 190/985 | — |

**Evidence tax: -3.13pp** (0.5526 − 0.5839)

对比 Qwen3-8B evidence tax = **-0.78pp**，LLaMA 的 evidence tax 大 4 倍。去掉 evidence 输出反而严重损害 LLaMA 的关系抽取性能，说明 LLaMA 比 Qwen3 更依赖 evidence 生成作为推理的中间步骤（chain-of-thought 效应）。

---
