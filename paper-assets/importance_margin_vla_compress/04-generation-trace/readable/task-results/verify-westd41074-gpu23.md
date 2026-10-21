# verify westd41074 gpu23

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_westd41074_gpu23_20260525T061157_result.json`
- **Structured JSON:** [`34009a693387a2c78d56.json`](../../sessions/34/34009a693387a2c78d56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部4个GPU验证通过：

| GPU | Util | Memory | PID | 实验 | 状态 |
|-----|------|--------|-----|------|------|
| 0 | 87% | 15964 MiB | 5205 | eval_openvla_random_k09_goal_seed42 | ✓ 运行中 |
| 1 | 87% | 16046 MiB | 5390 | eval_openvla_random_k09_spatial_seed42 | ✓ 运行中 |
| 2 | 70% | 15980 MiB | 8731 | eval_openvla_l2norm_k05_object_seed42_v4 | ✓ 运行中 |
| 3 | 82% | 16108 MiB | 8915 | eval_openvla_prune_random_k03_seed42 | ✓ 运行中 |

GPU 2-3 新提交的实验已正常启动，正在执行 Task 1/10。PID 与预期基本一致（偏差几个数字是正常的 fork 行为）。4块 GPU 均高负载运行，无异常。

---
