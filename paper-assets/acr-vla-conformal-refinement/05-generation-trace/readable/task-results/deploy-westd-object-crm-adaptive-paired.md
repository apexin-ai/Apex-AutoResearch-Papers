# deploy westd object crm adaptive paired

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-object-crm-adaptive-paired_20260526T132404_result.json`
- **Structured JSON:** [`cd4c75ad8114dbc810d6.json`](../../sessions/cd/cd4c75ad8114dbc810d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 不空闲：正在跑 `westd-pi05-vla-only-long-s44-r2` (VLA-only LONG s44, PID 467995, 14GB)。任务描述说"westd 6 卡全部空闲"与实际状态冲突。

我可以：
- A) 部署 5 个实验到 cuda:1-5（丢一个），报告冲突
- B) 等 GPU 0 空闲后补第 6 个（无队列机制，需手动）
- C) Kill 现有 long s44 任务，按原计划部署 6 个

请确认要走哪条路径？默认我先按 A 部署 5 个不阻塞，等你回复决定第 6 个怎么办。

---
