# ssh launch v73 cuda0

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_launch-v73-cuda0_20260517T195609_result.json`
- **Structured JSON:** [`3b4d7e3ffd0c7d85c4d0.json`](../../sessions/3b/3b4d7e3ffd0c7d85c4d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现 eval 结构：每个 suite 有 10 个 task，每个 task 跑 50 episodes。总计需要 10×50=500 episodes per suite。

当前进度：
- **α=0.0**: 35/40 task-batches 完成 (30 for first 3 suites + 5/10 for libero_10)，还剩 5 个 task
- **α=1.0**: 34/40 task-batches 完成，还剩 6 个 task

每个 task ~20 min → **α=0.0 还需约 100 min，α=1.0 还需约 120 min**。

这比预期久很多。要等 ~1.5-2 小时 eval 才结束。是否要：
1. 等 eval 自然结束（等待脚本会自动启动 v7.3）
2. 杀掉 α=0.0 eval 立即启动训练（已有 3 suite + 5/10 task 的 libero_10 数据，但会丢失最后 5 个 task 结果）

---
