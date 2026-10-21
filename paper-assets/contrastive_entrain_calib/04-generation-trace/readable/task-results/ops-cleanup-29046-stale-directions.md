# ops cleanup 29046 stale directions

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-29046-stale-directions_20260519T094002_result.json`
- **Structured JSON:** [`7e4ff735917d04ee5e04.json`](../../sessions/7e/7e4ff735917d04ee5e04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**已删除：**
- `output/directions_STALE_DO_NOT_USE.pt` ✓

**grep 结果：**
- `directions_STALE` — 无引用 ✓
- `output/directions` — **有引用**：`run_phase5.sh:6` 仍指向 `./output/directions.pt`

**正确路径** `results/exp001/directions.pt` 已确认存在。

**需要修改：** `run_phase5.sh` 第 6 行的 `--directions ./output/directions.pt` 应改为 `--directions ./results/exp001/directions.pt`。是否现在修改？

---
