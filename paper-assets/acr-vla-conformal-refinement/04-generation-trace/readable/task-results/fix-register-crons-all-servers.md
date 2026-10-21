# fix register crons all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_register-crons-all-servers_20260528T003848_result.json`
- **Structured JSON:** [`55c730933ee58d33a486.json`](../../sessions/55/55c730933ee58d33a486.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 8 个 cron 注册成功。汇总：

### 已注册 cron

| exp_id | server | PID | GPU |
|--------|--------|-----|-----|
| smolvla-tau040-long-s42 | bjb1-18228 | 892511 | cuda:0 |
| smolvla-tau045-long-s42 | bjb1-18228 | 892789 | cuda:1 |
| crm-always-on-goal-s46 | bjb1-18228 | 944325 | cuda:3 |
| crm-always-on-long-s45 | bjb1-32546 | 423632 | cuda:5 |
| smolvla-tau015-long-s42 | bjb2-28827 | 4609 | cuda:0 |
| smolvla-tau020-long-s42 | bjb2-28827 | 5160 | cuda:1 |
| smolvla-tau030-long-s42 | bjb2-28827 | 5635 | cuda:2 |
| smolvla-tau035-long-s42 | bjb2-28827 | 7362 | cuda:3 |

### 需要注意

- **crm-always-on-goal-s46** 实际 PID=944325（非任务中的 944319），registry 状态为 DONE 但进程仍在跑
- **crm-always-on-object-s45** (bjb1-18228 cuda:2) — registry RUNNING 但无 GPU 进程，可能已完成
- **crm-always-on-object-s46** (bjb1-32546 cuda:2) — registry RUNNING 但无 GPU 进程，可能已完成
- bjb2 四个 tau-sweep 是重跑，registry 状态为 DONE/PREPARING，cron 已注册但 registry 状态可能需要更新为 RUNNING

---
