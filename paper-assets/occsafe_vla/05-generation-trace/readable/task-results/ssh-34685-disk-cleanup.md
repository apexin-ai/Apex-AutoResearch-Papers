# ssh 34685 disk cleanup

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_34685_disk_cleanup_20260525T201320_result.json`
- **Structured JSON:** [`9391362c226dff296c10.json`](../../sessions/93/9391362c226dff296c10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 34685 磁盘诊断

清理前: 96% used (16G available)
清理后: 71% used (105G available)

删除的内容:
- `cutoff_25k_s2`: 45G（已被 `cutoff_25k_s2_v3` 取代）
- `reverse_cutoff_s2`: 45G（已被 `reverse_cutoff_s2_v3` 取代）
- pip cache: 74.5MB
- conda cache: 153.6MB

当前 D051 checkpoint 存储安全: ✅（105G 剩余空间足够 4 个实验的 checkpoint 写入）

---
