# analysis loss variant eval results

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_loss-variant-eval-results_20260522T103937_result.json`
- **Structured JSON:** [`dd187ea9616658995581.json`](../../sessions/dd/dd187ea9616658995581.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部更新完毕。汇总：

## CRM Loss 变体 Eval 对比表

| Variant | Avg SR% | Successes/Episodes | Best Task (SR%) | Worst Task (SR%) | 正常完成? |
|---------|---------|-------------------|-----------------|------------------|-----------|
| **perdof** | **4.0%** | 8/200 | butter (10%) | alphabet_soup, salad_dressing, tomato_sauce (0%) | ✓ |
| **conformal** | **6.0%** | 12/200 | chocolate_pudding (20%) | alphabet_soup, salad_dressing, ketchup, butter (0%) | ✓ |
| **combined** | **9.0%** | 18/200 | chocolate_pudding (25%) | alphabet_soup, ketchup (0%) | ✓ |

### Per-task 详细 (SR%)

| Task | perdof | conformal | combined |
|------|--------|-----------|----------|
| alphabet_soup | 0 | 0 | 0 |
| cream_cheese | 5 | 5 | 10 |
| salad_dressing | 0 | 0 | 10 |
| bbq_sauce | 5 | 10 | 15 |
| ketchup | 5 | 0 | 0 |
| tomato_sauce | 0 | 5 | 5 |
| butter | 10 | 0 | 5 |
| milk | 5 | 10 | 10 |
| chocolate_pudding | 5 | 20 | 25 |
| orange_juice | 5 | 10 | 10 |

### 对比参考

| Method | Avg SR% | 结论 |
|--------|---------|------|
| MSE baseline | 7.0% | negative |
| VLA-only (无 CRM) | 10.8%±1.3% | baseline |
| Plan A (obs_only, K=2) | 18.3%±2.1% | **success** |
| **perdof** | **4.0%** | **negative** — 低于 MSE baseline |
| **conformal** | **6.0%** | **negative** — 低于 VLA-only |
| **combined** | **9.0%** | **negative** — 低于 VLA-only |

三个 loss 变体全部 negative。combined 最好但仍低于 VLA-only 10.8%，perdof 甚至低于 MSE baseline 7.0%。CRM loss 改进方向未能带来正收益。

---
