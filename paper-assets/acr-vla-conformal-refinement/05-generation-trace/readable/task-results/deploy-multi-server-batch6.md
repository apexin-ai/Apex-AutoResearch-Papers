# deploy multi server batch6

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_multi-server-batch6_20260517T112247_result.json`
- **Structured JSON:** [`29c25a5e2ca40d1a610c.json`](../../sessions/29/29c25a5e2ca40d1a610c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**3 台服务器的目标 GPU 全部被占用，无法部署。**

| 服务器 | 目标 GPU | 占用进程 | 运行时间 | 显存 |
|---|---|---|---|---|
| bjb2-28827 | cuda:2 | `evaluate.py --mode crm_perdof --seed 46 --max_correction_norm 0.3` | 23m | 5645 MiB |
| bjb1-18228 | cuda:1 | `evaluate.py --mode crm_obs_only --seed 47 --max_correction_norm 0.3` | 23m | 5645 MiB |
| bjb2-40593 | cuda:0 | `evaluate.py --mode crm_perdof --norm 0.1 --seed 47` | 1h27m | 5609 MiB |

前两个跑了约 23 分钟，第三个已跑 1.5 小时。按照约束规则，不部署任何实验。

选项：
1. 等当前实验跑完后再部署（bjb2-40593 可能最快结束）
2. 如果这些实验可以被中断，告知我杀掉哪些

---
