# deploy westd 27271 goal

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-27271-goal_20260525T180935_result.json`
- **Structured JSON:** [`99ae5f64b982f8851d5d.json`](../../sessions/99/99ae5f64b982f8851d5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已启动并正在运行：

| GPU | exp_id | 状态 |
|-----|--------|------|
| cuda:0 | `eval_openvla_baseline_goal_seed43` | 模型加载完成，Task 1/10 开始 |
| cuda:1 | `eval_openvla_random_k09_goal_seed43` | 模型加载完成（Random pruning k=0.9），10 tasks x 50 episodes 就绪 |

脚本：`eval_openvla_l2norm_libero.py`，模型：`openvla-7b-finetuned-libero-goal`，unnorm_key=`libero_goal`，seed=43。预计每个实验约 4h 完成。

---
