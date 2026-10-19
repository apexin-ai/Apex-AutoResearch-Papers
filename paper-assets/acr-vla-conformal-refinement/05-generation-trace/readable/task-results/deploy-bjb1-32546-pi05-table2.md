# deploy bjb1 32546 pi05 table2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-pi05-table2_20260526T052256_result.json`
- **Structured JSON:** [`78ac6badc5e676a18553.json`](../../sessions/78/78ac6badc5e676a18553.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**6 个实验全部已在运行中，无需重新部署。**

Registry 中 6 个条目全部为 RUNNING 状态，命令完全匹配：

| exp_id | GPU | benchmark | seed | 状态 | 启动时间 |
|--------|-----|-----------|------|------|---------|
| `pi05-crm-k2-goal-s42-bjb1` | 0 | goal | 42 | RUNNING | 13:43 |
| `pi05-crm-k2-goal-s43-bjb1` | 1 | goal | 43 | RUNNING | 13:43 |
| `pi05-crm-k2-goal-s44-bjb1` | 2 | goal | 44 | RUNNING | 13:43 |
| `pi05-crm-k2-object-s42-bjb1` | 3 | object | 42 | RUNNING | 13:46 |
| `pi05-crm-k2-object-s43-bjb1` | 4 | object | 43 | RUNNING | 13:46 |
| `pi05-crm-k2-object-s44-bjb1` | 5 | object | 44 | RUNNING | 13:46 |

GPU 利用率 21-60%，显存占用 ~14GB/24GB，进程运行正常（goal 组已跑 ~21 分钟，object 组 ~15 分钟）。所有 tmux session 均存活。

---
