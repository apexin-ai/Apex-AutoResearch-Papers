# eval smart compress m32 libero spatial

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_smart_compress_m32_libero_spatial_20260518T230035_result.json`
- **Structured JSON:** [`05d50982b83476432e90.json`](../../sessions/05/05d50982b83476432e90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认，运行正常：

- **Checkpoint**: `checkpoints/smart_compress_m32/checkpoint.pt` (1.5GB) ✓
- **数据集**: `libero_spatial` 10 tasks 加载成功 ✓
- **模型**: `SmartCompressWrapper loaded: M=32, compressor params=22179840` ✓
- **Episode 执行**: Task 0 前 5 个 episode 已完成，4/5 SUCCESS（前 4 个 ep 全部成功，步数 82-117）

SR 已经明显 > 0%，generalization 初步得到验证。Job ID: `eval_smart_compress_m32_libero_spatial`，GPU: `cuda:2`，10 tasks × 50 episodes，预计需要一段时间跑完。

---
