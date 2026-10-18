# deploy westd 38929 batch2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-38929-batch2_20260523T154322_result.json`
- **Structured JSON:** [`97d2b32093a03e21e44b.json`](../../sessions/97/97d2b32093a03e21e44b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**

**OpenVLA 模型不存在** — Goal 和 Long 模型均未找到。

**备选方案已在运行** — 4 张 GPU 全部被占用，正好是备选方案的 4 个实验：

| GPU | tmux session | 显存占用 |
|-----|-------------|---------|
| 0 | `eval_pi05_random_k0925_goal_seed42_w38` | 10.5 GB |
| 1 | `eval_pi05_l2norm_k0925_goal_seed42_w38` | 10.5 GB |
| 2 | `eval_e5_xvla_attn_last_goal_k03` | 4.4 GB |
| 3 | `eval_e5_xvla_attn_mean_goal_k03` | 4.8 GB |

备选方案的 4 个实验已经全部部署完成，无需额外操作。

---
