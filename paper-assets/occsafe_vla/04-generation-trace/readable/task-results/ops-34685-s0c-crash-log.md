# ops 34685 s0c crash log

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_34685-s0c-crash-log_20260527T005105_result.json`
- **Structured JSON:** [`804265df40008cce2040.json`](../../sessions/80/804265df40008cce2040.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**崩溃原因：OOM（CUDA 显存不足）。**

具体信息：`torch.OutOfMemoryError: CUDA out of memory`，在 LlamaRMSNorm 的 `hidden_states.to(torch.float32)` 处触发。GPU 0 总共 94.97 GiB，进程已占用 60.74 GiB PyTorch 内存 + 34.15 GiB 非 PyTorch 内存，剩余仅 74.5 MiB，无法分配所需的 76 MiB。

LayerNorm 做 fp32 上转型时内存峰值超出了单卡 A100 95GB 的容量。

---
