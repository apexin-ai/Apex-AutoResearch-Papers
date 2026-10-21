# analysis test eval 8b rsft s43 no evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test_eval_8b_rsft_s43_no_evi_20260523T102332_result.json`
- **Structured JSON:** [`233c4f821ce265c13072.json`](../../sessions/23/233c4f821ce265c13072.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程 220069 已终止，eval 已完成。结果：

| Metric | s43 no-evi | s43 with-evi | s42 no-evi | s42 with-evi |
|--------|-----------|-------------|-----------|-------------|
| **Ign-F1** | **0.3224** | 0.3398 | 0.3326 | 0.3360 |
| Evi-F1 (DREEAM) | 0.0938 | — | — | — |
| Evi-F1 (TP) | 0.2301 | — | — | — |
| EDCR | 0.7218 | — | — | — |
| Format OK | 499/500 | — | — | — |
| Truncated | 43/500 | — | — | — |
| Predictions | 18972 | — | — | — |

**s43 evidence tax = 0.3224 - 0.3398 = -1.74pp**

相比 s42 的 evidence tax (-0.34pp)，s43 的 no-evi 模型掉得更多。s43 no-evi (0.3224) 也低于 s42 no-evi (0.3326)，差 1.02pp。

Registry 状态需要更新为 COMPLETED。需要我更新吗？

---
