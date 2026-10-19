# analyze eval supp adapt tau025 spatial s43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-adapt-tau025-spatial-s43_20260523T083433_result.json`
- **Structured JSON:** [`80bf645064737e43a140.json`](../../sessions/80/80bf645064737e43a140.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。总结：

## eval-supp-adapt-tau025-spatial-s43 结果

| 指标 | seed43 | seed42 | VLA-only baseline |
|------|--------|--------|-------------------|
| **SR** | **80.0%** (160/200) | 82.0% | 78.5% (3-seed mean 79.8%±1.2%) |
| **trigger_rate** | 19.4% | 19.4% | — |
| **mean_unc** | 0.1845 | — | — |

**结论：success** — SR 80.0% > VLA-only baseline 78.5%，trigger_rate 与 seed42 完全一致 (19.4%)。

### Per-task 明细

| Task | SR | 
|------|------|
| between_plate_and_ramekin | 95% |
| next_to_ramekin | 95% |
| from_table_center | 95% |
| on_cookie_box | **100%** |
| next_to_cookie_box | **100%** |
| next_to_plate | 85% |
| on_stove | 80% |
| on_wooden_cabinet | 80% |
| in_top_drawer | 70% |
| on_ramekin | **0%** |

### 与 seed42 对比

seed43 比 seed42 低 2pp (80% vs 82%)，但仍在 VLA-only 3-seed 均值 (79.8%±1.2%) 之上。trigger_rate 完全一致，说明 conformal threshold τ=0.25 的触发行为跨 seed 稳定。on_ramekin 任务两个 seed 应该都是 0%（硬任务），是 SR 的主要拖累项。

---
