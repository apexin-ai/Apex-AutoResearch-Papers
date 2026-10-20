# ops harvest llama rsft s43 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_llama_rsft_s43_eval_20260519T223453_result.json`
- **Structured JSON:** [`d5be0bc83e7472c77edf.json`](../../sessions/d5/d5be0bc83e7472c77edf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron job，无需删除。

---

## eval_llama_rsft_k1_s43 结果摘要

| 指标 | 值 |
|---|---|
| **Ign-F1** | **0.5662** |
| F1 | 0.5780 |
| Evi-F1 (DREEAM) | 0.4644 |
| Evi-F1 (TP) | 0.8287 |
| EDCR | 0.5783 |
| Format compliance | 985/985 (100%) |
| Truncated | 173/985 |

### Baseline 对比

| 对比 | ign_f1 | delta |
|---|---|---|
| SFT baseline | 0.5514 | — |
| RSFT s42 | 0.5839 | — |
| **RSFT s43** | **0.5662** | — |
| RSFT gain (s43 vs SFT) | — | **+0.0148** |
| Seed variance (s43 vs s42) | — | **0.0177** |

s43 相比 SFT 有 +1.48 的提升，但比 s42 低 1.77 个点，seed 间方差较大。

---
