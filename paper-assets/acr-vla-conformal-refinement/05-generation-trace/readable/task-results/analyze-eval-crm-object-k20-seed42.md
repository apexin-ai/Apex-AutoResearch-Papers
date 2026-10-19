# analyze eval crm object k20 seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-crm-object-k20-seed42_20260520T103247_result.json`
- **Structured JSON:** [`b69c87c4aa352af114c1.json`](../../sessions/b6/b69c87c4aa352af114c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：eval-crm-object-k20-seed42

**Overall SR: 20.0%** (20/100)

### Per-task 明细

| Task | SR |
|------|-----|
| alphabet_soup | 0% |
| cream_cheese | 10% |
| salad_dressing | 30% |
| bbq_sauce | 40% |
| ketchup | 10% |
| tomato_sauce | 10% |
| butter | 10% |
| milk | 10% |
| chocolate_pudding | 50% |
| orange_juice | 30% |

### 与 K=10 baseline 对比

| 配置 | SR | 备注 |
|------|-----|------|
| VLA-only | ~10.9% | baseline |
| **CRM K=10** | **16.8±1.8%** | n=6 seeds, D080 |
| **CRM K=20** | **20.0%** | 本次, seed42 |

- K=20 vs K=10: **+3.2pp** 绝对提升（16.8% → 20.0%），~19% 相对提升
- 代价：推理计算量翻倍（K 从 10 到 20）

### Conclusion: **success**

K=20 相比 K=10 仅提升 3.2pp，而推理计算量翻倍。边际收益递减明显——K=10 已接近饱和区间，是 compute-efficient choice。注意这是单 seed 结果，3.2pp 在 K=10 的 ±1.8% std 范围边缘（~1.8σ），不构成显著突破。

Registry 已更新：metrics、conclusion=success、status=DONE。

---
