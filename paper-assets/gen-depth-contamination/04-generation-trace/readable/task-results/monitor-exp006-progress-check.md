# monitor exp006 progress check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp006-progress-check_20260514T045453_result.json`
- **Structured JSON:** [`09ff7c1f6b3e76530397.json`](../../sessions/09/09ff7c1f6b3e76530397.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-006 进度报告

### 进度
- **已完成**: 10/50 runs（5 no-filter + 5 binary-ours）+ base_model baseline
- **进行中**: `binary-drayson_s42`（训练阶段，checkpoint-938，无 final_adapter）
- **剩余**: 当前 run 完成后还有 39 runs
- **无失败**: failures.log 不存在

### 实际 pace
从已完成 runs 的时间戳推算（9 个间隔）：

| 指标 | 数值 |
|------|------|
| Training | ~37.5 min |
| Eval | ~7.7 min |
| **总计/run** | **~45.2 min** |
| 范围 | 44–49 min |

**45.2 min/run 是正确的，99 min/run 的估计是错误的。**

### 修正 ETA
- 当前 run 剩余: ~23 min
- 后续 39 runs × 45.2 min = 1763 min
- **总剩余: ~29.8 小时**
- **ETA: May 15 ~10:43 UTC（18:43 +0800）**

### GPU 状态
- RTX 4090, 83% utilization, 339W/425W
- 显存 13.7GB / 24.5GB (56%)
- PID 61363 (python3)

### 当前 run
- Strategy: `binary-drayson`, seed: `42`
- 已运行 ~22 min，预计 ~13:18 +0800 完成

---
