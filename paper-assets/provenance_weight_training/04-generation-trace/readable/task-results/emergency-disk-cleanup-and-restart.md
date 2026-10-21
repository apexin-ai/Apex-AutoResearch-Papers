# emergency disk cleanup and restart

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_emergency_disk_cleanup_and_restart_20260521T185434_result.json`
- **Structured JSON:** [`099ff8729743cd38d4da.json`](../../sessions/09/099ff8729743cd38d4da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

### 磁盘空间对比

| | 清理前 | 清理后 |
|---|---|---|
| `/root/autodl-tmp` | 250G/250G (**100%**) | 160G/250G (**64%**) |
| 剩余空间 | 308K | **91GB** |

回收约 **90GB**（废弃目录 + 9个实验的中间 checkpoint）。磁盘安全（91GB >> 50GB 阈值）。

### 实验状态

| 实验 | PID | 状态 | 操作 |
|---|---|---|---|
| bs16_adaptive_tau07_seed123 | 643108 | **DEAD** (disk full crash at step 500) | 已清理 checkpoint，从头重启 |
| bs16_uniform_seed123 | 643185 | **ALIVE** | 无需操作 |
| detect_remove_q05_v2_seed42 | 629320 | **ALIVE** | 无需操作 |

### 重启信息

| 新 exp_id | GPU | 新 PID | parent |
|---|---|---|---|
| bs16_adaptive_tau07_seed123_r2 | cuda:0 | **645294** | bs16_adaptive_tau07_seed123 |

原 bs16_adaptive_tau07_seed123 已标记 `DONE/failed`，新条目 bs16_adaptive_tau07_seed123_r2 已在 registry 中标记为 `RUNNING`。

---
