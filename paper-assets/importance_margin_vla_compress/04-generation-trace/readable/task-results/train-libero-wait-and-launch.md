# train libero wait and launch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_libero_wait_and_launch_20260516T141758_result.json`
- **Structured JSON:** [`7f03e347a6ff30458841.json`](../../sessions/7f/7f03e347a6ff30458841.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

| 实验 | GPU | 状态 | 首步 loss |
|------|-----|------|-----------|
| `libero_full_ft_baseline` | cuda:0 | RUNNING | 1.1827 |
| `libero_lora_baseline` | cuda:1 | RUNNING | 1.2838 |

- LIBERO 数据集已完整（273465 samples，383 blobs）
- 两个 tmux session 存活，GPU 显存正常（2.7GB / 2.1GB，还在 warmup）
- Registry 已更新至 RUNNING 状态，含 hypothesis 和 spec

---
