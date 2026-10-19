# deploy bjb1 18228 pi05 redeploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-pi05-redeploy_20260526T034300_result.json`
- **Structured JSON:** [`d7d87072b30476533f9d.json`](../../sessions/d7/d7d87072b30476533f9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。bjb1-18228 4 卡满载，4 个 π0.5 评估都在跑：

| GPU | PID | exp_id | 状态 |
|-----|-----|--------|------|
| 0 | 2558 | pi05-crm-k2-long-s42-r2 | rollout 中（14.7GB, 40%） |
| 1 | 2916 | pi05-crm-k2-long-s43-r2 | 模型已加载（10.9GB） |
| 2 | 3332 | pi05-k2mean-goal-s42-r2 | 加载 PI05 中 |
| 3 | 3764 | pi05-adaptive-long-s42-r2 | 加载 PI05 中 |

Registry 4 个条目已建（QUEUED + hypothesis + parent）。错峰启动成功，未复现 cqa1 6 进程并发崩溃。

---
