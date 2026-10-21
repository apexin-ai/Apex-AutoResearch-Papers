# deploy cqa1 smolvla sweep batch2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-smolvla-sweep-batch2_20260521T212019_result.json`
- **Structured JSON:** [`1bfc8682b5e019b8ae0a.json`](../../sessions/1b/1bfc8682b5e019b8ae0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。总结：

| 实验 | GPU | tmux session | 状态 |
|------|-----|-------------|------|
| **A**: `eval_smolvla_official_random_k090_object_seed42` (random k=0.9) | GPU 0 | `eval_random_k090` | RUNNING, Task 0 开始 |
| **B**: `eval_smolvla_official_random_k050_object_seed42` (random k=0.5) | GPU 1 | `eval_random_k050` | RUNNING, Task 0 开始 |
| **C**: `eval_smolvla_official_l2norm_k050_object_seed42` (l2norm k=0.5) | — | — | 已完成 (SR=0%) |

修正了两个问题：`--mode random` → `random_prune`，补充了 `--pretrained_dir` 和 `source /etc/network_turbo`（VLM backbone 加载需要网络或本地缓存匹配）。GPU 2/3 空闲可用于后续实验。

---
