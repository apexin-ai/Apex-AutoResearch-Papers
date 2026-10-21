# deploy westd41074 4gpu pi05 batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-westd41074-4gpu-pi05-batch_20260524T005749_result.json`
- **Structured JSON:** [`6b2c62cf4aa26ec2502d.json`](../../sessions/6b/6b2c62cf4aa26ec2502d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 GPU 全部加载成功：

| GPU | 显存 | 实验 |
|-----|------|------|
| 0 | 9709 MiB | eval_pi05_random_k09_object_seed43 |
| 1 | 9709 MiB | eval_pi05_random_k09_spatial_seed42_postfix |
| 2 | 9709 MiB | eval_pi05_random_k05_spatial_seed42_postfix_v2 |
| 3 | 10532 MiB | eval_pi05_random_k085_goal_seed43（已在运行） |

3 个新实验模型已加载（4143.4M params），正在初始化 LIBERO 环境。

**注意**：Registry 显示 `eval_pi05_random_k085_goal_seed43` 和 `eval_pi05_random_k09_object_seed43` 之前已有完成结果（goal=53.4%, object=9.6%）。GPU 3 上的 goal_seed43 和 GPU 0 上的 object_seed43 是重新运行。

---
