# monitor running experiments progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_running-experiments-progress_20260521T032142_result.json`
- **Structured JSON:** [`11bcce6c59d7f68c2215.json`](../../sessions/11/11bcce6c59d7f68c2215.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**8 个实验全部存活，无异常退出。** 报告已写入 `artifacts/running_experiments_progress_20260521.md`。

关键发现：

| 实验 | 进度 | Running Avg | ETA |
|------|------|-------------|-----|
| adaptive-k-spatial-seed44 | 2/10 tasks | 90% | ~1h16m |
| pi05-baseline-object-seed42 | 2/10 tasks | **0%** ⚠️ | ~6h24m |
| norm003-seed66 (20r) | 5/10 tasks | 10.0% | ~1h51m |
| norm005-seed66 (20r) | 5.25/10 tasks | 8.0% | ~1h40m |
| norm01-seed66 (20r) | 5.25/10 tasks | 12.0% | ~1h40m |
| norm003-seed67 (10r) | 3/10 tasks | 6.7% | ~1h26m |
| norm005-seed67 (10r) | 3.5/10 tasks | 3.3% | ~1h26m |
| norm01-seed67 (10r) | 3/10 tasks | 6.7% | ~1h26m |

**⚠️ pi05-baseline 0/40 rollouts 全失败**，但 norm sweep 在相同的 alphabet_soup/cream_cheese task 上也是 0-10%，object benchmark 本身难度高，建议等更多 task 完成后再判断是否是模型问题。pi05 推理很慢（~48min/task），预计还需 ~6h。

---
