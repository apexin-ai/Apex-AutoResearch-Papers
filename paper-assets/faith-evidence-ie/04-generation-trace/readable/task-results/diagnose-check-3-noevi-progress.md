# diagnose check 3 noevi progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_check-3-noevi-progress_20260522T212256_result.json`
- **Structured JSON:** [`390d5f250b9397ebd443.json`](../../sessions/39/390d5f250b9397ebd443.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 eval 均在运行中，无完成项：

| GPU | 实验 | PID | 显存 | 进度 | 预计剩余 |
|-----|------|-----|------|------|----------|
| cuda:0 | 4B RSFT no-evi | 194600 | 9.6 GB | 262/500 (52%) | ~3h |
| cuda:2 | 1.7B RSFT no-evi | 189485 | 6.1 GB | 382/500 (76%) | ~1.5h |
| cuda:3 | LLaMA RSFT no-evi | 196512 | 18.9 GB | 19/500 (4%) | ~6h |

1.7B 最快完成（约 1.5h 后），4B 约 3h，LLaMA 刚开始约 6h。

---
