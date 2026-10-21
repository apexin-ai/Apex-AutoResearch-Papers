# ops 30476 disk cleanup emergency

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_30476_disk_cleanup_emergency_20260519T011212_result.json`
- **Structured JSON:** [`71d7c9d61e4cec0f7c29.json`](../../sessions/71/71d7c9d61e4cec0f7c29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Step 6: 汇报

### 1. 磁盘使用量
| | 使用 | 可用 | 占比 |
|---|---|---|---|
| 清理前 | ~250GB | 0GB | 100% |
| 清理后 | 133GB | 118GB | 54% |

释放约 117GB。

### 2. 实验存活状态
| 实验 | GPU | 状态 |
|---|---|---|
| detect_remove_q03_seed123 | GPU 0 | **运行中** (PID 76719) |
| detect_remove_q03_seed456 | GPU 1 | **运行中** (PID 76796) |
| detect_remove_q09_epoch_matched_seed42 | GPU 3 | **运行中** (PID 89876) |
| detect_remove_q07_epoch_matched_seed42 | GPU 2 | **已死**，已重启 |

### 3. q07 重启状态
- PID: 93812
- 已开始训练，进度 3/3047 steps，预计约 2 小时完成
- 正常运行中

### 4. 其他 crash
无。q03_seed123、q03_seed456、q09_epoch_matched 三个实验均正常存活，磁盘清理及时，未发生连锁 crash。

---
