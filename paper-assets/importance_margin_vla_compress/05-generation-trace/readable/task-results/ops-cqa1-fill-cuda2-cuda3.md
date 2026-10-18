# ops cqa1 fill cuda2 cuda3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-fill-cuda2-cuda3_20260521T063337_result.json`
- **Structured JSON:** [`803abd12aa6f302c847b.json`](../../sessions/80/803abd12aa6f302c847b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已启动并注册完毕。

| 实验 | GPU | tmux session | 状态 |
|------|-----|-------------|------|
| `eval_xvla_l2norm_k07_object_seed42_v2` | cuda:2 (4540 MiB) | `eval_xvla_l2norm_k07_object_seed42_v2` | RUNNING, Task 0 评估中 |
| `eval_xvla_random_k05_object_seed43` | cuda:3 (4051 MiB) | `eval_xvla_random_k05_object_seed43` | RUNNING, Task 0 评估中 |

修复了两个问题：`--n_episodes` → `--num_episodes`，补上了 `--model_path /root/autodl-tmp/X-VLA-Libero`。

---
