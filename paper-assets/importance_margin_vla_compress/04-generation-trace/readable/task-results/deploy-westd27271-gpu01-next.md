# deploy westd27271 gpu01 next

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_gpu01_next_20260525T123326_result.json`
- **Structured JSON:** [`f849551754671eef42fc.json`](../../sessions/f8/f849551754671eef42fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功启动，正在加载模型 checkpoint：

| GPU | 实验 | 状态 |
|-----|------|------|
| GPU 0 | `eval_openvla_random_k05_goal_seed42` | Loading checkpoint shards 25% |
| GPU 1 | `eval_openvla_random_k05_spatial_seed42` | Loading checkpoint shards 0% |

Registry 状态均为 RUNNING。模型加载完成后将自动开始 50 episodes 评估。

---
