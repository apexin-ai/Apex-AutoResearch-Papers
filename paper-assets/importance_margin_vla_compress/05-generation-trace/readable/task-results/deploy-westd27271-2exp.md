# deploy westd27271 2exp

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_2exp_20260526T034055_result.json`
- **Structured JSON:** [`6fe1b6a050590237880e.json`](../../sessions/6f/6fe1b6a050590237880e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功启动并占用显存。

| 实验 | GPU | PID | 显存占用 |
|------|-----|-----|---------|
| `eval_openvla_l2norm_k09_goal_seed43_v2` (L2norm k=0.9 Goal seed43) | GPU0 | 3897 | 15946 MiB |
| `eval_openvla_random_k07_goal_seed42_v2` (Random k=0.7 Goal seed42) | GPU1 | 4360 | 15946 MiB |

两块 NVIDIA RTX PRO 6000 Blackwell (98GB) 各占用约 16GB，模型加载正常。100% utilization 是 Blackwell 驱动已知行为，不影响运行。

---
