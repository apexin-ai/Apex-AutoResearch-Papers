# analyze eval obs only object norm005 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-obs-only-object-norm005-seed44_20260520T103648_result.json`
- **Structured JSON:** [`60c2898eefe5f22f9800.json`](../../sessions/60/60c2898eefe5f22f9800.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果摘要

**eval-obs-only-object-norm005-seed44** — CRM obs_only ε=0.05, LIBERO-Object, seed=44

### Overall SR: **12%** (12/100)

### Per-task 分布

| Task | SR |
|---|---|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 0% (0/10) |
| salad_dressing | 0% (0/10) |
| **bbq_sauce** | **30%** (3/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 10% (1/10) |
| butter | 10% (1/10) |
| milk | 20% (2/10) |
| chocolate_pudding | 20% (2/10) |
| **orange_juice** | **30%** (3/10) |

无错误，EXIT_CODE=0，100 episodes 全部完成。

### 对比

| Seed | SR | 来源 |
|---|---|---|
| seed44 (前次) | 16% | previous_failure 记录 |
| **seed44 (本次)** | **12%** | 本次重试 |
| seed45 | 14% | 已有数据 |
| seed47 | 14% | 已有数据 |

本次 seed44 SR=12%，比前次 16% 低 4pp，但与其他 norm005 seed（14%、14%）在同一量级。ε=0.05 修正幅度极小，三个 seed 的 SR 范围 12%-14%，方差合理，可用于 Figure 2 error bars。

---
