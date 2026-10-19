# ssh check seed45 seed46 progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-seed45-seed46-progress_20260516T171058_result.json`
- **Structured JSON:** [`a41ab21d972385a7d550.json`](../../sessions/a4/a41ab21d972385a7d550.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

---

## 实验进度报告

### 1. eval-argmin-object-seed45 (bjb2-28827, PID 215932) — Fisher test 关键
- **状态**: 运行中，已 9h27m
- **进度**: 5/10 tasks 完成 + task 6 进行中 (rollout 5/10) → **~55/100 rollouts (55%)**
- 已完成 tasks 成功率:
  - alphabet_soup: 0/10, cream_cheese: 0/10, salad_dressing: 1/10, bbq_sauce: 4/10, ketchup: 0/10
  - 当前累计: 5/50 = 10%
- **预估剩余**: ~7-8h

### 2. eval-obs-only-object-norm02-seed45 (bjb2-28827, PID 233544) — Fisher test 关键
- **状态**: ⚠️ **进程不存在**。PID 233544 未找到，也没有 exit file
- bjb2-28827 上没有 `norm02 seed45` 的实验在运行
- 相近实验:
  - PID 242264: `obs_only default (无norm限制) seed45` — 6h28m, 2/10 tasks done (n_rollouts=20), ~20%
  - PID 272762: `obs_only norm03 seed45 r2` — 1h48m, 1/10 tasks done, ~10%

### 3. eval-obs-only-object-norm02-seed46 (bjb1-18228, PID 510896)
- **状态**: 运行中，已 1h10m
- **进度**: task 1 进行中 (rollout 5/10) → **~5/100 rollouts (5%)**
- 尚无 task 完成
- **预估剩余**: ~20-22h

---

**关键问题**: `eval-obs-only-object-norm02-seed45` 实验未在运行，需要启动。

---
