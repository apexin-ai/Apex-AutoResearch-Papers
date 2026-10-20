# ops execute disk cleanup 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_execute_disk_cleanup_10894_20260525T012117_result.json`
- **Structured JSON:** [`4c43516a80d92ce54a9b.json`](../../sessions/4c/4c43516a80d92ce54a9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果**：
- 可用空间：**125GB**（之前 ~35GB），释放约 90GB，达到目标
- `full_occ_ln_s0` 的 30K/40K checkpoint 本身不存在（只有 50K），所以实际删除了 4 个目录
- 剩余 checkpoints 总计 104GB（各实验保留的 final + 关键 checkpoint）

---
