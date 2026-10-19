# monitoring check oldest evals

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitoring_check-oldest-evals_20260517T225815_result.json`
- **Structured JSON:** [`f7f14e38448dd1240e51.json`](../../sessions/f7/f7f14e38448dd1240e51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 1. eval-perdof-object-norm02-seed46 (bjb2-28827, PID 389051)
- **PID 存活**: ✅ 运行 12h22m
- **进度**: ~75/100 episodes（完成 7 个 task，正在第 8 个 "milk" rollout 5/10）
- **预估剩余**: ~25 episodes × ~5min = ~2h
- **异常**: 无，正常推进中

### 2. eval-perdof-object-norm01-seed47 (bjb1-32546, PID 414817)
- **PID 存活**: ❌ 已结束
- **状态**: ✅ **已完成**
- **结果**: Overall success rate = **14.0% (14/100)**
- **输出**: `logs/eval_object_perdof_norm01_seed47_r2.json`

### 3. eval-obs-only-object-norm03-seed46 (bjb1-32546, PID 416568)
- **PID 存活**: ✅ 运行 12h31m
- **进度**: ~96/100 episodes（正在最后一个 task "orange_juice" rollout 6/10）
- **预估剩余**: ~4 episodes × ~5min = ~20min
- **异常**: 无，即将完成

---

三个实验都正常：2 号已完成（14%），3 号约 20 分钟内完成，1 号约 2 小时后完成。无卡住或异常。

---
