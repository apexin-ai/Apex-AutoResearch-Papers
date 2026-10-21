# ops kill westd41074 lora v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_westd41074_lora_v2_20260519T184820_result.json`
- **Structured JSON:** [`4a66007029a3a26548b5.json`](../../sessions/4a/4a66007029a3a26548b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Kill 结果：** PID 29248 已成功终止（force_killed）。

**剩余 train_openvla 进程：**

| PID | GPU | 脚本 | 说明 |
|-----|-----|------|------|
| **26118** | GPU 0 | `train_openvla_smart_compress.py` (m128) | VTC-only go/no-go gate — **保留中** |
| 27796-27799 | GPU 0 | `train_openvla_smart_compress.py` (m128) | 26118 的子进程（dataloader workers） |
| **29854** | GPU 1 | `train_openvla_smart_compress_lora.py` (m128_lora) | 29248 被 kill 后残留的子进程，仍在运行 |

注意：PID 29248 虽被 kill，但其子进程 **29854**（实际的 LoRA 训练 python 进程）和 **29242**（bash shell）、**29249**（tee）仍存活。需要一并清理吗？

---
