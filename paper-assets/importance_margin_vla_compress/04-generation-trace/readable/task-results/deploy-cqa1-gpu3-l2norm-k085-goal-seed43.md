# deploy cqa1 gpu3 l2norm k085 goal seed43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy-cqa1-gpu3-l2norm-k085-goal-seed43_20260524T010042_result.json`
- **Structured JSON:** [`dad487d409083e9f9b8c.json`](../../sessions/da/dad487d409083e9f9b8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Model still loading (pi0.5 is large, takes a few minutes). The experiment is correctly deployed:

- **Exp ID**: `eval_pi05_l2norm_k085_goal_seed43`
- **Server**: cqa1-33015, GPU 3 (`CUDA_VISIBLE_DEVICES=3`)
- **Config**: `prune_mode=l2norm, keep_ratio=0.85, suite=libero_goal, seed=43`
- **Tmux session**: `eval_pi05_l2norm_k085_goal_seed43`
- **Log**: `/tmp/eval_pi05_l2norm_k085_goal_seed43.log`
- **Registry**: RUNNING, hypothesis and spec set
- **GPU 0/1**: untouched (existing experiments safe)

---
