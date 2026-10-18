# deploy westd41074 gpu2 random obj s43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_gpu2_random_obj_s43_20260524T202627_result.json`
- **Structured JSON:** [`ed1dc319160e936eb65b.json`](../../sessions/ed/ed1dc319160e936eb65b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

- **exp_id**: `eval_pi05_random_k09_object_seed43_postfix`
- **状态**: RUNNING (PID 797800)
- **GPU2**: 25% util, 10554 MiB
- **配置确认**: random prune, keep 230/256 tokens/image, libero_object, seed 43
- **日志**: `logs/eval_pi05_random_k09_object_seed43_postfix.log`

注意：启动时未显式设置 `CUDA_VISIBLE_DEVICES=2`（因 nohup 超时问题改用全路径 python 直接执行），但 nvidia-smi 确认进程已正确加载到 GPU2 上��

---
