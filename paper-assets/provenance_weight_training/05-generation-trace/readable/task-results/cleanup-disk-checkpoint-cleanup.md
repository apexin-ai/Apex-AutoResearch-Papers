# cleanup disk checkpoint cleanup

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_disk_checkpoint_cleanup_20260522T011145_result.json`
- **Structured JSON:** [`68ba7ce39da0c2fd5b63.json`](../../sessions/68/68ba7ce39da0c2fd5b63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 215G | 152G |
| 可用 | 36G (86%) | 99G (61%) |
| **释放** | — | **~63G** |

清理内容：
- 4个已完成实验的 checkpoint-5500/6000/6103（保留了 final/）
- 2个 failed 实验目录整体删除（dr_epoch_matched_seed123、detect_remove_q05_v2_seed123）
- 正在训练的 _r2 目录未触碰

---
