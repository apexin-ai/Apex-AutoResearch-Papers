# ops disk cleanup westd41074 retry

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-westd41074-retry_20260520T043457_result.json`
- **Structured JSON:** [`18216120670382a710c2.json`](../../sessions/18/18216120670382a710c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：m96 和 m64 目录已不存在，上次清理已生效。**

当前 checkpoints 目录状态：
| 目录 | 大小 |
|------|------|
| `openvla_sc_m128` | 38 GB |
| `openvla_vtc_m128_seed42` | 0 (空目录) |

- `runs/` 目录不存在
- `/tmp/` 无大文件残留（最大的是 `ViT-L-14.pt` 890MB）
- **磁盘可用：82 GB / 250 GB (32% 空闲)**

无需额外删除操作。

---
