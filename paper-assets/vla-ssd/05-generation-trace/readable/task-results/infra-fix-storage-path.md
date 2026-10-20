# infra fix storage path

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-storage-path_20260515T051232_result.json`
- **Structured JSON:** [`f26f40b445a5e51d4fe3.json`](../../sessions/f2/f26f40b445a5e51d4fe3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**修复结果：**

| 项目 | 状态 |
|------|------|
| 符号链接 | `/root/vla-ssd/features` → `/root/autodl-tmp/vla-ssd/features` |
| 数据盘可用空间 | **816GB**（XFS，`/dev/sda2`） |
| 根分区可用空间 | 23GB（不再承载 features） |
| checkpoints/data | 均为空（0 bytes），暂无需迁移 |

特征提取产生的 ~110GB hidden states 将写入数据盘，根分区不受影响。如果后续 checkpoints 或 data 目录增长，需要同样做符号链接迁移。

---
