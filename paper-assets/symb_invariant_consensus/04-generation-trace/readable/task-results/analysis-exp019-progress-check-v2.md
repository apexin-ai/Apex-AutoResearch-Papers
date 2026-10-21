# analysis exp019 progress check v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp019-progress-check-v2_20260517T084055_result.json`
- **Structured JSON:** [`e3f72655496d69f9da04.json`](../../sessions/e3/e3f72655496d69f9da04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
STATUS: RUNNING
PROGRESS: 101/200
GPU_STATUS: ACTIVE (RTX PRO 6000 Black, 100% util, 88.3/97.9 GiB VRAM)
ETA: ~22 min (avg 13.6s/problem, 99 remaining)

INTERIM METRICS (101 problems):
- sica_accuracy: 72.3% (73/101)
- sc_accuracy:   70.3% (71/101)
- delta_pp:      +2.0pp
- avg_wall_time: 13.58s/problem
- constraints:   avg 10 extracted, 4 unique after dedup (example)
- maxsat:        avg solve ~3ms

实验正常推进，预计约 17:03 CST 完成全部 200 题。结果文件实时更新中。JSON 无 `num_candidates` / `truncated` 字段，需完成后从日志统计或确认 schema。

---
