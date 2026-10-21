# deploy cqa1 zeromask

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-zeromask_20260525T181140_result.json`
- **Structured JSON:** [`619e14d3e8ad9d0d4d7f.json`](../../sessions/61/619e14d3e8ad9d0d4d7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

zeromask_random 已启动，正在加载模型。

**部署状态：**

| GPU | 实验 | 状态 |
|-----|------|------|
| cuda:0 | `eval_pi05_zeromask_random_k09_object_seed42` | 已提交，模型加载中 |
| cuda:2 | `eval_pi05_zeromask_l2norm_k09_object_seed42` | **无法部署** — cuda:2 正在跑 `random k=0.7 libero_10 seed43` (PID 537176, 10207 MiB) |

**cuda:2 的问题：** 当前有 3 个 GPU 在用（cuda:1/2/3），不是预期的 2 个（cuda:1/3）。cuda:2 上跑的是 `eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 43`。

zeromask_l2norm 需要等 cuda:2 的实验完成后再部署，或者你可以指定其他空闲 GPU。

---
