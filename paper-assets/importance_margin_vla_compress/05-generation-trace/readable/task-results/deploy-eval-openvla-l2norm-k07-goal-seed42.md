# deploy eval openvla l2norm k07 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_eval_openvla_l2norm_k07_goal_seed42_20260526T132032_result.json`
- **Structured JSON:** [`908b308167ccbbe27e30.json`](../../sessions/90/908b308167ccbbe27e30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:2 被占用**，正在运行 `attention_prune k=0.7 Goal seed42`（PID 601124，已运行约 8 分钟）。

4 张 GPU 占用情况：
| GPU | PID | 实验 | 运行时间 |
|-----|-----|------|----------|
| 0 | 467961 | (未显示在 ps 中，可能是监控进程) | — |
| 1 | 279274 | random_prune k=0.5 Long seed42 | 8h17m |
| 2 | 601124 | attention_prune k=0.7 Goal seed42 | ~8min |
| 3 | 514356 | attention_prune k=0.85 Long seed42 | 2h11m |

cuda:2 刚启动了 attention_prune k=0.7 Goal 实验，无法部署 L2norm k=0.7 Goal。所有 GPU 均被占用，无空闲卡可用。需等待现有实验完成后再部署。

---
