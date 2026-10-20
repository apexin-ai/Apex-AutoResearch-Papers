# analysis reeval flat nli s43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reeval_flat_nli_s43_20260515T235848_result.json`
- **Structured JSON:** [`7fa3c4cd7eee7fb86b13.json`](../../sessions/7f/7fa3c4cd7eee7fb86b13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

## reeval_flat_nli_s43 结论

| 指标 | s43 (本次) | s42 | Δ |
|------|-----------|-----|---|
| **rel_f1** | **0.4523** | 0.4539 | -0.16pp |
| ign_f1 | 0.4523 | — | — |
| evi_f1 | 0.8158 | — | — |
| edcr | 0.6505 | — | — |

**结论: success.** flat-NLI RSFT s43 的 rel_f1=0.4523 与 s42 (0.4539) 仅差 0.16pp，确认 seed 稳定性。D064 bug 修复有效（原无效结果 0.0022 → 修复后 0.4523）。flat-NLI 两 seed 均值 0.4531，略低于 CED RSFT 均值 0.4596（差 0.65pp）。

---
