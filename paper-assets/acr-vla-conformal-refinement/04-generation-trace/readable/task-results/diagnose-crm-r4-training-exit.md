# diagnose crm r4 training exit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_crm-r4-training-exit_20260522T172018_result.json`
- **Structured JSON:** [`0bf528459ed1fd61b9be.json`](../../sessions/0b/0bf528459ed1fd61b9be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：CRON 误报，训练正常进行中。**

| 项目 | 值 |
|------|---|
| 状态 | RUNNING (PID 322367) |
| 进度 | epoch 14/50, batch 2700/6316 (~28%) |
| 最新 checkpoint | epoch 13 |
| train_loss | ~0.012 |
| 预估剩余 | 约 36 个 epoch，每 epoch ~23 min → ~14 小时 |

Registry 已更新，status 保持 RUNNING。无需干预。

---
