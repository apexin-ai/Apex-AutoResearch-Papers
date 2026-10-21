# deploy cqa1 gpu012

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-cqa1-gpu012_20260523T211141_result.json`
- **Structured JSON:** [`5f0147a40fa6d9091e5d.json`](../../sessions/5f/5f0147a40fa6d9091e5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部在正确 GPU 上运行，GPU 3 保持空闲。

**部署完成：**

| GPU | exp_id | PID | tmux session | 显存 |
|-----|--------|-----|-------------|------|
| 0 | `eval_pi05_l2norm_k095_goal_seed42` | 315899 | `eval_pi05_l2norm_k095_goal_seed42` | 10310 MiB |
| 1 | `eval_pi05_random_k03_goal_seed42` | 315972 | `eval_pi05_random_k03_goal_seed42` | 10140 MiB |
| 2 | `eval_pi05_l2norm_k03_goal_seed42` | 295877 | `eval_pi05_l2norm_k03_goal_seed42` | 10104 MiB |
| 3 | (保留 - 空闲) | — | — | 1 MiB |

Registry 注意：GPU 0/1 实验被误推进到 DEPLOYED 状态（无出路），需要手动修正或重建条目。GPU 2 实验已在 RUNNING 状态（retry #1）。

---
