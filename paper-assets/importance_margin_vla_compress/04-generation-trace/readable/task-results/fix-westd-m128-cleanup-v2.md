# fix westd m128 cleanup v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd_m128_cleanup_v2_20260519T045020_result.json`
- **Structured JSON:** [`3b2e1681db2b9f4e8e9d.json`](../../sessions/3b/3b2e1681db2b9f4e8e9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：无需清理。**

- `train_m128_s44` tmux session 不存在，GPU 1 上没有多余进程
- GPU 0: PID 462076 — `smart_compress_m16_seed44` 训练中
- GPU 1: PID 459645 — `smart_compress_m128_seed44` 训练中
- 保留的 m128_seed44 当前状态：**step 18950/100000，loss=0.0817，速度 5.3 steps/s**，正常运行

---
