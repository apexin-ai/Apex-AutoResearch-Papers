# ops cqa1 disk cleanup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1_disk_cleanup_20260519T162057_result.json`
- **Structured JSON:** [`40a47b7d8d27f6d6c0aa.json`](../../sessions/40/40a47b7d8d27f6d6c0aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**清理内容**：
| 目标 | 大小 | 原因 |
|------|------|------|
| `datasets/parquet/default-9082321d09ccfd80` | ~33G (实际释放 ~101G，含 hardlink) | 旧 parquet cache，无进程引用 |
| `datasets/parquet/default-134874f6610e1406` | 4.8G | 旧 parquet cache，无进程引用 |
| `checkpoints/smart_compress_m16_seed44` | 218M | failed 实验，部分文件 |
| `checkpoints/libero_acis_stage1only_k03` | 1.8G | failed 实验 |

**磁盘状态**：250G 中已用 140G，可用 **111G (56%)**，从 4MB → 111G。

**运行中训练状态**：两个任务均正常运行中
- `m128_seed43`: step 14850/100000, loss=0.097, 4.0 sps
- `m16_seed43`: step 14750/100000, loss=0.136, 4.0 sps

---
