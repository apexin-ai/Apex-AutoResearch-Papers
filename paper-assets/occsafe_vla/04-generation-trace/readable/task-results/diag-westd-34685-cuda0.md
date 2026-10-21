# diag westd 34685 cuda0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd-34685-cuda0_20260528T141826_result.json`
- **Structured JSON:** [`92d06cbd51fa92c3a99f.json`](../../sessions/92/92d06cbd51fa92c3a99f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 空闲。**

nvidia-smi 显示 GPU 0 (NVIDIA RTX PRO 6000 Black, 96GB) 上无任何进程运行，显存占用 0MiB。

注意到一个异常：GPU-Util 显示 100% 但无进程且显存为 0。这通常是 GPU 刚释放进程后的短暂状态，或 persistence mode 下的显示延迟，不影响使用。

---
