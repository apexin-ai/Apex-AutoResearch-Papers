# deploy s47 remaining gpus

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_s47_remaining_gpus_20260529T022240_result.json`
- **Structured JSON:** [`c826b2a817e4a7d3de93.json`](../../sessions/c8/c826b2a817e4a7d3de93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器各只有 **1 块 GPU**（NVIDIA RTX PRO 6000 Black, 98GB），不是预期的 4 块。

- **westd-41074**: GPU 0 占用 10.8GB，正在运行 python 进程（已部署的 Attn k=0.5 seed47）
- **westd-38929**: GPU 0 占用 10.9GB，正在运行 python 进程（已部署的 Attn k=0.85 seed47）

**没有空闲 GPU（cuda:1/2/3 不存在）。** 无法在这两台服务器上部署额外的 s47 bonus 实验。需要等当前实验完成后复用 GPU 0，或使用其他服务器。

---
