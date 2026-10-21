# monitor d140 progress check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_d140_progress_check_20260521T091057_result.json`
- **Structured JSON:** [`d91732aab5f7ae027c6c.json`](../../sessions/d9/d91732aab5f7ae027c6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部存活，进度：

| 实验 | 进度 | ETA |
|------|------|-----|
| 1.7B no-evi (cuda:0) | 205/247 (83%) | ~22min |
| 4B no-evi (cuda:1) | 177/247 (72%) | ~35min |
| 8B no-evi (cuda:2) | 139/247 (56%) | ~81min |
| 4B with-evi (cuda:3) | 11/247 (4%) | ~2.5h |

4 卡全在正常工作，磁盘 108G 可用。报告已写入 `artifacts/d140_progress_check.md`。

---
