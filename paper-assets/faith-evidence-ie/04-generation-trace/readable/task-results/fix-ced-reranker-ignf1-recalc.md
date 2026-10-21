# fix ced reranker ignf1 recalc

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_ced_reranker_ignf1_recalc_20260516T034324_result.json`
- **Structured JSON:** [`83e94feb0ad479d31e2b.json`](../../sessions/83/83e94feb0ad479d31e2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Strategy | F1 | Ign-F1 | Δ |
|---|---|---|---|
| ced_reranker | 0.486367 | 0.473634 | -0.012734 |
| oracle | 0.623746 | 0.612518 | -0.011228 |
| random | 0.453783 | 0.439677 | -0.014107 |

34610 个 train facts 被用于 Ign 过滤，gold 从 12151 降至 10821（排除了 1330 个与训练集重叠的三元组）。结果已持久化到 `metrics_v2.json`。

---
