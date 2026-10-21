# deploy westd41074 model transfer v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_model_transfer_v3_20260525T060521_result.json`
- **Structured JSON:** [`a51c6d2da9a22d0f8f2b.json`](../../sessions/a5/a51c6d2da9a22d0f8f2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四项验证全部通过：

1. **Goal 模型** — `/root/autodl-tmp/openvla-7b-finetuned-libero-goal` 存在，15GB ✓
2. **Spatial 模型** — `/root/autodl-tmp/openvla-7b-finetuned-libero-spatial` 存在，15GB ✓
3. **GPU 占用** — GPU 0: 70% util, 15964 MiB; GPU 1: 89% util, 16046 MiB ✓
4. **Python 进程** — PID 5205 (goal, GPU 0) 和 PID 5390 (spatial, GPU 1) 都在运行 ✓

模型已在 westd-41074 上（无需传输），两个 Random k=0.9 实验已成功启动并运行中。

---
