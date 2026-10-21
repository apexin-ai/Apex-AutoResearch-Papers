# deploy westd38929 gpu023 xvla k085 disruption

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd38929-gpu023-xvla-k085-disruption_20260524T010752_result.json`
- **Structured JSON:** [`ecbeb802cc9463aaf6b0.json`](../../sessions/ec/ecbeb802cc9463aaf6b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部正常运行：

| GPU | 实验 | 状态 | 显存 |
|-----|------|------|------|
| 0 | Object k=0.85 Random | Ep 29/50 (Task 0) | 4872 MiB |
| 2 | Goal k=0.85 Random | Ep 37/50 (Task 0) | 4856 MiB |
| 3 | Spatial k=0.85 Random | Ep 34/50 (Task 0) | 4938 MiB |

GPU 1 空闲（之前的 L2 Long seed43 已完成）。Registry 中 Goal 已更新为 RUNNING，Object 和 Spatial 因已有先前结果（63.6%/67.6%）无法重新转为 RUNNING 状态。

日志路径：
- `/tmp/eval_xvla_random_k085_object_seed42.log`
- `/tmp/eval_xvla_random_k085_goal_seed42.log`
- `/tmp/eval_xvla_random_k085_spatial_seed42.log`

预计每个实验约 80-90 分钟完成（10 tasks × 50 episodes）。

---
