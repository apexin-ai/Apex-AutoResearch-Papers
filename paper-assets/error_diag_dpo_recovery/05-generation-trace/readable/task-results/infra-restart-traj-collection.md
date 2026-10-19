# infra restart traj collection

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_restart-traj-collection_20260512T124014_result.json`
- **Structured JSON:** [`7bb4d16146ada5cc929f.json`](../../sessions/7b/7bb4d16146ada5cc929f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

轨迹收集已稳定运行：

| 指标 | Part 0 | Part 1 |
|------|--------|--------|
| Screen | `traj_p0` (Detached) | `traj_p1` (Detached) |
| 进度 | 1/500, task=0 | 1/500, task=0 |
| 速度 | ~55s/轨迹 | ~64s/轨迹 |
| 文件 | 1 行 | 1 行 |

两个进程都在 screen 中稳定收集。每条轨迹约 55-64 秒，500 条预计 ~7-9 小时完成。

**额外处理**：根分区从 100% 降到 31%（移了 `/root/structfuse` 21G 到数据盘并建了 symlink），解决了之前 `No space left on device` 的根本原因。

---
