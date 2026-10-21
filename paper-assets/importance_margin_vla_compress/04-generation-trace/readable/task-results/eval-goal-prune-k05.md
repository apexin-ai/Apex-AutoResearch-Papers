# eval goal prune k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_goal_prune_k05_20260517T124811_result.json`
- **Structured JSON:** [`3daa1355de8186c19dd8.json`](../../sessions/3d/3daa1355de8186c19dd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果确认 cliff-edge 效应跨全部 3 个 LIBERO suite 一致。

## 结果汇总

**ACIS k=0.5 True Removal Pruning — LIBERO Goal Suite**

| 指标 | 值 |
|------|------|
| Overall SR | **0/500 (0.0%)** |
| Wilson CI 95% | [0.0, 0.76%] |
| Episodes per task | 50 |
| Total tasks | 10 |
| Max steps | 300 |

**Per-task SR（全部 0%）：**
- Task 0: open the middle drawer of the cabinet — 0%
- Task 1: put the bowl on the stove — 0%
- Task 2: put the wine bottle on top of the cabinet — 0%
- Task 3: open the top drawer and put the bowl inside — 0%
- Task 4: put the bowl on top of the cabinet — 0%
- Task 5: push the plate to the front of the stove — 0%
- Task 6: put the cream cheese in the bowl — 0%
- Task 7: turn on the stove — 0%
- Task 8: put the bowl on the plate — 0%
- Task 9: put the wine bottle on the rack — 0%

**跨 Suite 对比：**

| Suite | Baseline SR | Pruned k=0.5 SR |
|-------|------------|----------------|
| Object | 78% | **0%** |
| Spatial | 76% | **0%** |
| Goal | 63% | **0%** |

Cliff-edge 效应在全部 3 个 LIBERO suite 上完全一致：k=0.5 true removal pruning 导致所有 task 的 success rate 从正常水平直接崩溃到 0%。结果 JSON 已保存至 `eval_results/eval_goal_prune_k05.json`。

---
