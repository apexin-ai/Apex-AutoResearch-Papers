# deploy westd 41074 object zeromask

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-41074-object-zeromask_20260525T181624_result.json`
- **Structured JSON:** [`c6bea76dd766656c407f.json`](../../sessions/c6/c6bea76dd766656c407f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 GPU 全部已占用（~16GB each），模型加载成功。

| GPU | exp_id | 模式 | 状态 |
|-----|--------|------|------|
| cuda:0 | `eval_openvla_random_k05_object_seed42_v2` | random_prune k=0.5 | 运行中 (15980 MiB) |
| cuda:1 | `eval_openvla_l2norm_k05_object_seed42_v2` | l2norm_prune k=0.5 | 运行中 (15980 MiB) |
| cuda:2 | `eval_openvla_zeromask_random_k09_object_seed42` | zero_mask + random k=0.9 | 运行中 (16016 MiB) |
| cuda:3 | `eval_openvla_zeromask_l2norm_k09_object_seed42` | zero_mask + l2norm k=0.9 | 运行中 (16016 MiB) |

timeout 8h，预计 4-5 小时完成（500 episodes each）。

---
