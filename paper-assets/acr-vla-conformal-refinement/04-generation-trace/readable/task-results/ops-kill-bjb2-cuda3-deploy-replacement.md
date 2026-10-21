# ops kill bjb2 cuda3 deploy replacement

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-bjb2-cuda3-deploy-replacement_20260515T193342_result.json`
- **Structured JSON:** [`1719640de1fa670fd164.json`](../../sessions/17/1719640de1fa670fd164.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**结果汇总：**

| 操作 | 结果 |
|------|------|
| Kill PID 141024 (重复 obs_only) | 已 force kill |
| cuda:3 释放 | 确认空闲 (1 MiB / 24564 MiB) |
| 注册 eval-mag-perdof-norm02-seed43-object-r3 | PREPARING → PENDING → QUEUED → ALLOCATED |
| 提交任务 | PID 144504, tmux session 启动 |
| GPU 验证 | cuda:3 进程 144513 占用 3132 MiB，正在加载 LIBERO 环境 |

新实验已在 bjb2-28827:cuda:3 上运行，CRM checkpoint 和 VLM 已加载成功。

---
