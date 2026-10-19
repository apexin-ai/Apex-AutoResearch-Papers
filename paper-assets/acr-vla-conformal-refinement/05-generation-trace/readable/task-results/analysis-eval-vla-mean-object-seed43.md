# analysis eval vla mean object seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-vla-mean-object-seed43_20260516T045020_result.json`
- **Structured JSON:** [`1e4fda53d24b1b7b6f10.json`](../../sessions/1e/1e4fda53d24b1b7b6f10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 结果完整，10/10 tasks 已完成。

## seed=43 结果

- **overall_sr**: 15%
- **total_success**: 15
- **total_rollouts**: 100 (10 tasks × 10 rollouts)
- **per_task**:

| Task | seed=43 | seed=42 | Diff |
|------|---------|---------|------|
| alphabet_soup | 0% | 0% | — |
| cream_cheese | 0% | 0% | — |
| salad_dressing | 20% | 10% | +10 |
| bbq_sauce | 30% | 30% | — |
| ketchup | 10% | 10% | — |
| tomato_sauce | 10% | 10% | — |
| butter | 10% | 0% | +10 |
| milk | 30% | 20% | +10 |
| chocolate_pudding | 30% | 30% | — |
| orange_juice | 10% | 10% | — |

## 对比分析

- **Overall SR**: seed=43 (15%) vs seed=42 (12%), +3pp
- seed=43 在 salad_dressing、butter、milk 三个 task 上各高 10pp，其余 task 完全一致
- 两个 seed 的 hard tasks（alphabet_soup, cream_cheese）均为 0%，easy tasks（bbq_sauce, chocolate_pudding）均为 30%，分布一致
- 方差合理，两 seed 平均 overall SR ≈ 13.5%

## Conclusion: **success**

结果完整、合理，seed 间差异在正常波动范围内。VLA-mean baseline 在 object benchmark 上 overall SR 约 12-15%。

---
