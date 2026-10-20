# ops check 1 7b seed43 eval result

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_1_7b_seed43_eval_result_20260517T164731_result.json`
- **Structured JSON:** [`4ceb5bb9fbc2f8bb903e.json`](../../sessions/4c/4ceb5bb9fbc2f8bb903e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1.7B RSFT Seed 43 Eval 结果

| 指标 | Seed 42 | Seed 43 | Δ |
|------|---------|---------|---|
| **F1** | 0.5219 | 0.5180 | -0.39pp |
| **Ign-F1** | 0.5050 | 0.5024 | -0.26pp |
| Evi-F1 (DREEAM) | — | 0.4201 | — |
| Evi-F1 (TP) | — | 0.8341 | — |
| EDCR | — | 0.6246 | — |
| Format OK | — | 984/985 (99.9%) | — |

两个 seed 的 rel_f1 差距 0.39pp、ign_f1 差距 0.26pp，均在 ±1pp 以内，1.7B RSFT 数据点稳定。Registry 已更新，cron 已删除。

---
