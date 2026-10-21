# train p0 batchsize 16

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_p0_batchsize_16_20260524T155653_result.json`
- **Structured JSON:** [`ffb1a1c3fd660500c28d.json`](../../sessions/ff/ffb1a1c3fd660500c28d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OOM 了——B=16 在 Qwen3-0.6B 上直接跑 forward 需要一次性分配 18.55 GiB logits tensor，超出 GPU 剩余显存。

进程已退出。可能的解决方案：
1. **降低 batch_size 到 8，gradient_accumulation_steps 改为 2**（effective batch 仍为 16，显存减半）
2. 加 `PYTORCH_ALLOC_CONF=expandable_segments:True` 尝试减少碎片（但 free 只有 15 GiB，大概率不够）

建议用方案 1：`batch_size=8, gradient_accumulation_steps=2, n_min=4`（8//2=4）。是否按此调整重新提交？

---
