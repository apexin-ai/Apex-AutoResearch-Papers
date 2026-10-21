# monitor eval progress check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_eval_progress_check_20260516T033014_result.json`
- **Structured JSON:** [`5a108b03b3acc43029df.json`](../../sessions/5a/5a108b03b3acc43029df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 eval 全部正常运行，无异常。

| Eval | 进度 | 速度 | 预计完成 (UTC) |
|------|------|------|----------------|
| eval_plan_014_no_evidence_r2 | 143/247 (58%) | ~27s/it | ~12:17 |
| eval_rsft_ced_s45 | 173/247 (70%) | ~42s/it | ~12:22 |
| eval_rsft_ced_s43 | 105/247 (43%) | ~44s/it | ~13:14 |
| reeval_flat_nli_s43_r2 | 35/247 (14%) | ~43s/it | ~14:02 |

GPU 利用率 48-57%，显存 ~10-11GB/32GB，headroom 充足。`plan_014_no_evidence_r2` 因无 evidence 生成更短，速度最快。报告已写入 `artifacts/eval_progress_20260516.md`。

---
