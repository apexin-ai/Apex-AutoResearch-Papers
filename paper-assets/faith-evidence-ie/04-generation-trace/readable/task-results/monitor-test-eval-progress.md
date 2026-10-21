# monitor test eval progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_test_eval_progress_20260522T000307_result.json`
- **Structured JSON:** [`a3c9d57315e906c86b99.json`](../../sessions/a3/a3c9d57315e906c86b99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| exp_id | 进度 | 预估剩余 | 状态 |
|--------|------|----------|------|
| test_eval_14b_sft_s42 | 485/500 | ~10 min | 正常，即将完成 |
| test_eval_1_7b_sft_s42 | 178/500 | ~2h10m | 正常，~24s/it |
| test_eval_14b_sft_s42_no_evi | 75/500 | ~5h | 正常，~42s/it |

14B SFT 马上跑完，完成后 cuda:1 会释放。1.7B 预计下午3点左右完成，14B no-evi 预计晚上1点左右。

---
