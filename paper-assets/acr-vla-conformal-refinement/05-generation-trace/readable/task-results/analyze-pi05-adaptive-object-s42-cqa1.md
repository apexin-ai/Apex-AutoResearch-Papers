# analyze pi05 adaptive object s42 cqa1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-adaptive-object-s42-cqa1_20260526T115522_result.json`
- **Structured JSON:** [`86162bc2a4835d0b4395.json`](../../sessions/86/86162bc2a4835d0b4395.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## π0.5 Adaptive Conformal CRM — Object Suite (seed=42)

**状态**: 正常完成 (EXIT_CODE=0)

### 总体指标

| 指标 | 值 |
|------|-----|
| **SR%** | **85.5%** (171/200) |
| **trigger_rate** | 3.68% (1,250 / 33,946 steps) |
| **mean_correction_norm** | 0.200 (= max_correction_norm, clipped) |
| **mean_uncertainty** | 0.0842 |
| **conformal τ** | 0.25 |

### Per-task SR%

| Task | SR% |
|------|-----|
| alphabet_soup | 100% |
| butter | 95% |
| chocolate_pudding | 95% |
| salad_dressing | 90% |
| bbq_sauce | 90% |
| tomato_sauce | 90% |
| milk | 90% |
| orange_juice | 85% |
| cream_cheese | 70% |
| ketchup | **50%** |

correction_norm 全部被 clip 到 0.2 上限，说明 CRM 在触发时总是想施加更大的修正。trigger_rate 仅 3.68%，conformal threshold=0.25 下大部分 step 不确定性低于阈值，CRM 介入非常稀疏。ketchup 任务 SR 明显偏低（50%）。

---
