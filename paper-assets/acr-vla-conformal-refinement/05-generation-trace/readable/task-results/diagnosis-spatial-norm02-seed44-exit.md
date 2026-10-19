# diagnosis spatial norm02 seed44 exit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_spatial-norm02-seed44-exit_20260519T142459_result.json`
- **Structured JSON:** [`f1f7b032c59fcc255730.json`](../../sessions/f1/f1f7b032c59fcc255730.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能之前已自动清除）。

**诊断结果：实验成功完成。**

- **状态**: SUCCESS
- **Overall SR**: 0.36 (36/100)
- **退出原因**: 正常完成，cron 误判为 failed（进程退出时未检测到 sentinel/W&B，但 JSON 输出完整）
- **Per-task SR**:
  - next_to_cookie_box: 1.0, next_to_ramekin: 1.0
  - between_plate_and_ramekin: 0.9
  - on_cookie_box: 0.4
  - next_to_plate: 0.2, in_top_drawer: 0.1
  - from_table_center / on_ramekin / on_stove / on_wooden_cabinet: 0.0

Registry 已更新为 conclusion=success，metrics 已写入。

---
