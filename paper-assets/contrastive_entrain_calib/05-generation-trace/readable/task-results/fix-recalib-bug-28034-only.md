# fix recalib bug 28034 only

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_recalib-bug-28034-only_20260519T113847_result.json`
- **Structured JSON:** [`61077fefd3f4a6567ab7.json`](../../sessions/61/61077fefd3f4a6567ab7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。变更摘要：

- **line 190**: `step = t._reward_step` → `step = t.state.global_step`
- 这使得 recalibration 条件判断（line 192-194）和 `recalibrate_direction()` 调用（line 195）都基于 `t.state.global_step`
- `t._reward_step += 1`（line 189）保留不动
- 语法检查通过，备份已保存为 `dcgrpo_trainer.py.bak_pre_recalib_fix`
- `/root/mvp_v2_1_expanded/` 下是独立副本，未修改

---
