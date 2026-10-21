# ops kill westd41074 pid30737

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_westd41074_pid30737_20260519T190731_result.json`
- **Structured JSON:** [`bbde6889894a8b8e5a8c.json`](../../sessions/bb/bbde6889894a8b8e5a8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

- **PID 30737（目标）**：已不存在，无需 kill
- **PID 26118（受保护）**：已不存在（服务器可能重启过）
- **GPU 0**：PID 841334 占用 32276 MiB，正在跑 `train_openvla_smart_compress.py --config openvla_smart_compress_m128.yaml`（tmux session `train_openvla_sc_m128_v2`）
- **GPU 1**：完全空闲（3 MiB），可直接用于 C5 RoboFlamingo fine-tune

原来的两个进程都已不在了，当前 GPU 0 上跑的是一个新的 smart compress m128 v2 训练。这个进程我没有动。

---
