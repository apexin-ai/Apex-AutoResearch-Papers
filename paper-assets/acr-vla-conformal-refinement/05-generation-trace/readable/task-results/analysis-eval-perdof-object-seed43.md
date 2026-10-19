# analysis eval perdof object seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-perdof-object-seed43_20260516T031452_result.json`
- **Structured JSON:** [`5a6ea109f0f3d6281374.json`](../../sessions/5a/5a6ea109f0f3d6281374.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

## eval-perdof-object-seed43 结果总结

**Overall SR: 12.0%** (12/100)，conclusion: **success**

### Per-task 成绩

| Task | SR |
|------|-----|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| salad_dressing | 20% |
| bbq_sauce | 30% |
| ketchup | 0% |
| tomato_sauce | 0% |
| butter | 0% |
| milk | 0% |
| chocolate_pudding | 40% |
| orange_juice | 30% |

### LIBERO Object seed=43 三方对比

| Method | seed=42 | seed=43 | 2-seed avg |
|--------|---------|---------|------------|
| **obs_only** (norm=0.1) | 19% | 12% | 15.5% |
| **argmin** | 12% | 17% | 14.5% |
| **perdof** | 11% | **12%** | 11.5% |
| VLA-only | — | 12% | — |

### 结论

perdof seed=43 = 12%，低于 argmin seed=43 的 17%，**符合预期**——perdof 在 object benchmark 上不优于 argmin。两个 seed 平均 perdof (11.5%) < argmin (14.5%) < obs_only (15.5%)，进一步确认 obs_only 是 object 上最佳 CRM 变体。

---
