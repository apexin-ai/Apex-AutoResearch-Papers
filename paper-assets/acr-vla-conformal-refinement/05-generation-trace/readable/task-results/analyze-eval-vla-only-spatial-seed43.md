# analyze eval vla only spatial seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-vla-only-spatial-seed43_20260519T144237_result.json`
- **Structured JSON:** [`f2631fc486d11323a495.json`](../../sessions/f2/f2631fc486d11323a495.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。汇总：

## eval-vla-only-spatial-seed43 结果

**Overall: 29% (29/100)**

### Per-task 对比 (seed42 → seed43)

| Task | seed42 | seed43 | Δ |
|------|--------|--------|---|
| between_plate_and_ramekin | 0.6 | 0.7 | +0.1 |
| next_to_ramekin | 1.0 | 0.8 | -0.2 |
| from_table_center | 0.0 | 0.1 | +0.1 |
| on_cookie_box | 0.2 | 0.3 | +0.1 |
| in_top_drawer | 0.0 | 0.0 | — |
| on_ramekin | 0.0 | 0.0 | — |
| next_to_cookie_box | 0.9 | 0.9 | — |
| on_stove | 0.0 | 0.0 | — |
| next_to_plate | 0.3 | 0.1 | -0.2 |
| on_wooden_cabinet | 0.0 | 0.0 | — |
| **Overall** | **30%** | **29%** | **-1%** |

两个 seed 非常一致（29% vs 30%），跨 seed 方差极小。同样的 task 难度梯度：next_to_cookie_box / next_to_ramekin / between_plate_and_ramekin 容易，in_top_drawer / on_ramekin / on_stove / on_wooden_cabinet 全部 0%。

### CRM 配对

CRM obs_only spatial seed43 结果 **pending**（seed43 CRM = 32% 按 hypothesis 记录，待实验完成确认）。

---
