# deploy fill idle gpus bjb1 bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_fill-idle-gpus-bjb1-bjb2_20260524T201646_result.json`
- **Structured JSON:** [`5b55c93585b4f510363b.json`](../../sessions/5b/5b55c93585b4f510363b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有计划的实验已经在运行了，有人（或另一个 agent）已经部署完毕。

**bjb1-32546**（启动于 May 25 04:18）:
| GPU | PID | 实验 |
|-----|------|------|
| 0 | 726394 | vla_only object s42 |
| 2 | 726597 | vla_only object s43 |
| 3 | 726864 | vla_only object s44 |
| 4 | 727196 | vla_only goal s42 |
| 5 | 727400 | vla_only long s43 |

**bjb2-28827**（启动于 May 25 04:18）:
| GPU | PID | 实验 |
|-----|------|------|
| 0 | 429934 | crm_obs_only spatial s48 |
| 4 | 430199 | crm_obs_only spatial s49 |
| 5 | 430467 | crm_obs_only goal s48 |
| 2 | 393794 | pi05 reconvla goal s42（已有） |
| 3 | 394198 | pi05 reconvla object s42（已有） |

命令参数与部署计划完全一致。GPU 1 在两台服务器上反而空闲了（bjb1 原来的 PID 567066 已结束）。

需要我检查这些实验是否已有 registry 条目，或者为它们补建 registry？

---
