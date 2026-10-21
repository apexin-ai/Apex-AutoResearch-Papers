# analysis obsonly norm02 seed42 vs seed43 partial

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_obsonly-norm02-seed42-vs-seed43-partial_20260516T060813_result.json`
- **Structured JSON:** [`c4b4d7814c316975fe65.json`](../../sessions/c4/c4b4d7814c316975fe65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到所有数据了。以下是分析。

## Seed42 obs_only norm=0.2 逐 task 累计

| # | Task | SR | 累计 SR |
|---|------|----|---------|
| 1 | alphabet_soup | 0% | 0.0% |
| 2 | cream_cheese | 0% | 0.0% |
| 3 | salad_dressing | 30% | 10.0% |
| 4 | bbq_sauce | 40% | 17.5% |
| 5 | ketchup | 20% | 18.0% |
| 6 | tomato_sauce | 10% | 16.7% |
| 7 | **butter** | **10%** | **15.7%** |
| 8 | milk | 20% | 16.25% |
| 9 | chocolate_pudding | **60%** | **21.1%** |
| 10 | orange_juice | 30% | **22.0%** |

## 对比 seed43 前 7 task

| | seed42 | seed43 | Δ |
|---|--------|--------|---|
| 7-task partial | **15.7%** | **12.9%** | -2.9pp |
| 7-task sum (成功数) | 11/70 | 9/70 | -2 |

差距来自：
- ketchup: seed42=20%, seed43=0% (-2 successes)
- cream_cheese: seed42=0%, seed43=10% (+1)
- salad_dressing: seed42=30%, seed43=20% (-1)

## Seed43 翻盘分析

Seed42 的最后 3 个 task (milk/choc_pudding/OJ) 拿了 **20+60+30 = 110**，平均 **36.7%**，把 partial 从 15.7% 拉到 22.0%（+6.3pp）。

Seed43 当前 7-task sum = 9 (90/1000). 各目标需要的剩余 3 task 均值：

| 目标 | 需 3 task 总和 | 需均值 | 可能性 |
|------|--------------|--------|--------|
| 追平 22% | 130 | 43.3% | **困难** — seed42 同样 3 task 只拿了 36.7% |
| 追平 19% (norm=0.1) | 100 | 33.3% | **有希望** — 如果 choc_pudding≥50% + OJ≥30% |
| 达到 17% | 80 | 26.7% | **大概率** — choc_pudding 是全局最易 task |

## 结论

1. **Seed42 前 7 task 也只有 15.7%**，后 3 task 拉了 +6.3pp。所以后段翻盘是真实现象，主要靠 chocolate_pudding (60%)。

2. **Seed43 翻盘空间有限但存在。** 最可能落在 **17-20%** 区间。追平 22% 需要 3 task 均值 43.3%，比 seed42 同 3 task 的 36.7% 还高，不太现实。

3. **chocolate_pudding 是关键变量。** 如果 seed43 也能拿到 50-60%，最终大概率 18-20%；如果掉到 30% 以下，可能只有 15-16%。

---
