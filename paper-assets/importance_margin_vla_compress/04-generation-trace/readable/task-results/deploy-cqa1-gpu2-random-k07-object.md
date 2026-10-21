# deploy cqa1 gpu2 random k07 object

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-cqa1-gpu2-random-k07-object_20260523T223920_result.json`
- **Structured JSON:** [`96cc7584cbcd55cbcb8a.json`](../../sessions/96/96cc7584cbcd55cbcb8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 2 还在加载模型（π0.5 模型较大，加载需要几分钟）。日志只有 2 行，模型仍在读取中。进程正常运行。

部署完成：

- **实验**: eval_pi05_random_k07_object_seed42_v2
- **服务器**: cqa1-33015 GPU 2
- **tmux session**: `eval_pi05_random_k07_object_seed42_v2`
- **日志**: `/tmp/eval_pi05_random_k07_object_seed42_v2.log`
- **参数**: `--prune_mode random --keep_ratio 0.7 --suite libero_object --seed 42`
- **Registry**: RUNNING，hypothesis/parent/spec 已更新
- **其他 GPU**: GPU 0/1/3 实验未受影响

---
