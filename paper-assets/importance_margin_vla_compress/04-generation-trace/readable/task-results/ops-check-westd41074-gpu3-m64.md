# ops check westd41074 gpu3 m64

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd41074-gpu3-m64_20260520T202624_result.json`
- **Structured JSON:** [`8285b5812863a44cc08e.json`](../../sessions/82/8285b5812863a44cc08e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程存活，无需干预。**

| 指标 | 值 |
|------|-----|
| PID | 68852 — 状态 `Rl`（running） |
| 运行时间 | 16h 45m 51s |
| GPU 3 显存 | 27,535 MiB / 97,887 MiB |
| GPU 3 利用率 | 98%（nvidia-smi -i 3）；批量查询瞬时采样到 0% |
| 命令 | `python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m64.yaml` |

两次 nvidia-smi 调用间隔不到 1 秒，一次读到 98%、一次读到 0%——这是 checkpointing 或 dataloader 加载期间的正常瞬时波动，不是崩溃。进程状态 `Rl` 确认仍在正常运行。

---
