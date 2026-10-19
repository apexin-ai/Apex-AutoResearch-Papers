# test exp004 single gpu vram

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_test_exp004_single_gpu_vram_20260518T153642_result.json`
- **Structured JSON:** [`37747c9b451ce198dca3.json`](../../sessions/37/37747c9b451ce198dca3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**SINGLE GPU OK**，peak 24.1GB / 32GB，余量约 8GB。

细分：
- 模型加载后：16.6GB
- Forward 1 后：19.1GB
- Forward 2 后：21.6GB
- Backward peak：24.1GB

单卡 32GB RTX 5090 跑 ACT baseline（batch=1, seq=2048, LoRA r=64, gradient_checkpointing）没有问题。

---
