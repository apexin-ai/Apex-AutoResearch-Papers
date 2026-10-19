# audit deploy bjb2 40593 fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit-deploy_bjb2-40593-fill_20260520T152936_result.json`
- **Structured JSON:** [`ca1b2e97433ad0bee1e6.json`](../../sessions/ca/ca1b2e97433ad0bee1e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**审计结果：**

- **cuda:0** 被 PID 707407 占用（random-sel-object-seed43），正在运行中
- 进度：完成 3/10 个 task，当前第3个 task 刚跑完
- 无已完成的 JSON 输出（`eval_random_selection_object_seed43.json` 尚未生成）

服务器只有 1x 4090，cuda:0 被占满，无法部署 eval-random-selection-spatial-seed45。等 seed43 完成后再部署。

---
