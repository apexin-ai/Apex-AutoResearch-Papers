# fix verify symlink disk

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_verify_symlink_disk_20260517T034419_result.json`
- **Structured JSON:** [`5984d87cf6bd8dfdc135.json`](../../sessions/59/5984d87cf6bd8dfdc135.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**

| 目录 | 状态 | 指向 | 需要迁移 |
|------|------|------|----------|
| `checkpoints` | symlink ✓ | `/root/autodl-tmp/spectral_collapse_ews/checkpoints_410m` | 否 |
| `checkpoints_1b` | symlink ✓ | `/root/autodl-tmp/spectral_collapse_ews/checkpoints_1b` | 否 |

**磁盘状态：**
- 根分区 `/`：30G，已用 25G (84%)
- 数据盘 `/root/autodl-tmp`：250G，已用 111G (45%)
- 410m checkpoints 占用：7.6G（已在数据盘上）

symlink 正常，无需操作。

---
