# ops harvest plan010 nli large eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_plan010_nli_large_eval_20260520T020703_result.json`
- **Structured JSON:** [`ea3a53efdef6c345f9fb.json`](../../sessions/ea/ea3a53efdef6c345f9fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。Cron 不存在（可能已被清理）。

## plan010_nli_large_eval_r2 结果摘要

| 指标 | v3-large (本次) | v3-base baseline (s42) | Δ |
|------|----------------|----------------------|---|
| **ign_f1** | **0.4533** | 0.4423 | **+1.10pp** |
| f1 | 0.4636 | 0.4517 | +1.19pp |
| evi_f1_joint | 0.3606 | — | — |
| edcr | 0.653 | — | — |
| format | 100% | — | — |
| truncated | 180/985 | — | — |

**结论：v3-large > v3-base，ign_f1 提升 +1.1pp。** 属于第一种解读——当前 CED scorer 有提升空间，更强的 NLI 模型能产出更高质量的 reward signal，进而提升下游 RSFT 效果。提升幅度不算大但方向明确一致（f1/ign_f1 均提升）。

---
