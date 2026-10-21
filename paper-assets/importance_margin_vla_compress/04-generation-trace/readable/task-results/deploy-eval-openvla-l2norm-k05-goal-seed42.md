# deploy eval openvla l2norm k05 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_eval_openvla_l2norm_k05_goal_seed42_20260526T144036_result.json`
- **Structured JSON:** [`f91d120b067b20cc92cc.json`](../../sessions/f9/f91d120b067b20cc92cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这个实验已经存在且状态为 **DONE**，已有结果：

- **exp_id**: eval_openvla_l2norm_k05_goal_seed42
- **status**: DONE (success)
- **overall_sr**: 43.4% (217/500)
- **server**: westd-41074 (之前的服务器)
- **elapsed**: 386.1 min
- **command**: `--mode l2norm` (注意：你的任务指定的是 `--mode l2norm_prune`)

两个差异需要确认：
1. 之前用 `--mode l2norm`，你的任务指定 `--mode l2norm_prune` — 这是不同的模式吗？还是同一个？
2. 实验已完成且有结果（43.4%），是否需要重新部署？

如果需要重跑，我需要先重置实验状态。请确认。

---
