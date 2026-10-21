# monitor training progress check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-check_20260516T012805_result.json`
- **Structured JSON:** [`021e2ac2a45641a388c0.json`](../../sessions/02/021e2ac2a45641a388c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| exp_id | GPU | Step/Total | Progress | Loss | ETA | Status |
|--------|-----|-----------|----------|------|-----|--------|
| contamination_60_seed42_r2 | cuda:0 | 5537/6103 | 90.7% | 9.82 | ~21 min | RUNNING |
| grid_b0_3_seed42 | cuda:1 | 334/6103 | 5.5% | 9.11 | ~7h 13min | RUNNING |
| contamination_60_ess_only_seed42 | cuda:2 | 3261/6103 | 53.4% | 9.77 | ~1h 40min | RUNNING |
| contamination_60_grid_b0_5_seed42 | cuda:3 | 6103/6103 | 100% | 9.26 | — | **COMPLETED** |

注意事项：
- **PID 255781 已不存在** — `contamination_60_grid_b0_5_seed42` 已完成训练，模型已保存到 `output/models/contamination_60_grid_b0_5_seed42/final`，EXIT_CODE=129（SIGHUP）
- `grid_b0_3_seed42` 速度是其他实验的 2 倍慢（4.51s/it vs ~2.2s/it），VRAM 占用接近满载（93/95.6 GB）
- GPU 3 已空闲，可用于新实验

报告已写入 `artifacts/training_progress_20260516.md`。

---
