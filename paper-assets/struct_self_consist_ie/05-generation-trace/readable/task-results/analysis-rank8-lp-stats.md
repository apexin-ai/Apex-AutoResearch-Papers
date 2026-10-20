# analysis rank8 lp stats

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rank8_lp_stats_20260518T005609_result.json`
- **Structured JSON:** [`2180226ea3883c3b522b.json`](../../sessions/21/2180226ea3883c3b522b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| Metric | Rank=8 (exp-023) | Rank=32 (exp-012) |
|--------|------------------|-------------------|
| LP median range | **0.0569** | 0.0429 |
| LP mean range | **0.0758** | 0.0598 |
| LP tied fraction | 0/551 (0.00%) | 1/551 (0.18%) |
| Within-inst ρ(LP,F1) mean | **0.2395** | 0.1532 |
| Within-inst ρ(LP,F1) median | **0.3164** | 0.2474 |
| ρ valid instances | 506/551 (91.8%) | 451/551 (81.9%) |

Rank=8 在所有 LP 指标上优于 rank=32：更大的 within-instance range（+33%）、更强的 LP-F1 alignment（median ρ +28%）、更多 valid instances（+10pp）。低 rank adapter 的 under-parameterization 反而产生了更有区分性的 logprob 分布，对 W2 的 "LoRA rank sensitivity" 问题是正面回应。

---
