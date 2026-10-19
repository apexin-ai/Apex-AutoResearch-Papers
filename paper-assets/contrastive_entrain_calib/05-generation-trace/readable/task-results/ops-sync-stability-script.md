# ops sync stability script

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync-stability-script_20260519T014634_result.json`
- **Structured JSON:** [`6a350bc607cc340f3cba.json`](../../sessions/6a/6a350bc607cc340f3cba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

1. **脚本同步** — 已写入 `/root/contrastive_entrain_calib/training/measure_direction_stability.py`，语法验证通过 (OK)。

2. **Checkpoint 不可用** — `exp002v2_dcgrpo_cosine/` 目录下没有 `checkpoint-*` 子目录。当前约 step 216（基于 log 中 combined_mean 条目计数），`save_steps=500` 尚未触发首次保存。

3. **无法运行诊断** — 需等到 step 500 产生第一个 checkpoint 后再执行。按当前约 30s/step 的速度，预计还需约 **2.5 小时**（284 steps × ~30s）才会有 checkpoint。

---
