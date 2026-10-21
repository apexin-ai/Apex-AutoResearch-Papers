# deploy westd38929 gpu0 ov random k095 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_gpu0_ov_random_k095_long_20260527T122512_result.json`
- **Structured JSON:** [`393cc6f6b86c3bb4c35e.json`](../../sessions/39/393cc6f6b86c3bb4c35e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已部署完成。

- **服务器**: westd-38929 GPU0
- **PID**: 272022
- **tmux session**: `ov_rnd_k095_long`
- **timeout**: 43200s (12h)，前次 8h 不够
- **日志**: `eval_openvla_random_k095_long_seed42_v3.log`
- **Registry**: `eval_openvla_random_k095_long_seed42_v3` → RUNNING

注意：初始部署时 tmux 内 `python` 不在 PATH，已修复为先 `conda activate base` 再运行。

---
