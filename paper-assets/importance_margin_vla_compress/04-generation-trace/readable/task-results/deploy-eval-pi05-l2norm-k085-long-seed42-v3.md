# deploy eval pi05 l2norm k085 long seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_eval_pi05_l2norm_k085_long_seed42_v3_20260526T132055_result.json`
- **Structured JSON:** [`c96a83ccb77679581db0.json`](../../sessions/c9/c96a83ccb77679581db0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 被占用**：PID 384775 正在运行 `eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.85`（random k=0.85 实验），已运行 8 分钟，占用 10498 MiB。

4 张卡全部被占用（每张约 10GB）。无法在 cuda:0 上部署 l2norm k=0.85 实验。需要等当前实验完成或选择其他服务器。

---
