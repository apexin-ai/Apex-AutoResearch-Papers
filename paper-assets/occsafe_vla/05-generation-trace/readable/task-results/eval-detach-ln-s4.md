# eval detach ln s4

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_detach_ln_s4_20260527T132154_result.json`
- **Structured JSON:** [`0a8962a610fecf78fe29.json`](../../sessions/0a/0a8962a610fecf78fe29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已成功提交。

- **服务器**: westd-34685, cuda:1
- **tmux session**: `detach_ln_s4_eval`
- **PID**: 796385
- **Checkpoint**: `/root/autodl-tmp/checkpoints/detach_ln_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s4`
- **日志**: `/root/autodl-tmp/logs/detach_ln_s4_eval.log`
- **修复**: 首次启动因 `MUJOCO_EGL_DEVICE_ID=0` 与 `CUDA_VISIBLE_DEVICES=1` 不匹配导致 AssertionError，已改为 `MUJOCO_EGL_DEVICE_ID=1`。

---
