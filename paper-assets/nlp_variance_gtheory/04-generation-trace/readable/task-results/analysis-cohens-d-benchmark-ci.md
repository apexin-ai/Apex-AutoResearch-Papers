# analysis cohens d benchmark ci

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cohens_d_benchmark_ci_20260522T084105_result.json`
- **Structured JSON:** [`fba0384c3941cb04b08d.json`](../../sessions/fb/fba0384c3941cb04b08d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存到 `artifacts/exp004/data/cohens_d_ci.json`。

关键结果：

**Benchmark-level d:**
- Cohen's d = **7.90**（MC mean 70.0% vs FF mean 36.4%，s_pooled = 4.25）
- NCT 95% CI: **[-18.26, 36.51]** — df=3 太小，CI 跨零，NCT 方法在此 n 下基本无信息量
- Bootstrap 95% CI: **[7.59, 64.73]** — 不跨零但上界极端（n=2 的 FF 组 variance 估计极不稳定，571/10000 次 resample 产生 NaN）

**Item-level propagated d:**
- d = **7.90**（同点估计）
- Parametric bootstrap 95% CI: **[4.26, 11.72]** — 比 benchmark-level bootstrap 窄很多，因为每个 benchmark 的 item-related% 不确定性通过其自身 bootstrap CI 传入，提供了额外约束
- Median = 6.57（低于点估计，分布右偏）

核心结论：MC 与 FF 的 item-related% 差异巨大（~34 个百分点），d > 4 即使在最保守估计下也远超 "large effect" 阈值。但 benchmark-level 的 NCT CI 跨零纯粹是 n=5 的统计功效不足，不应解读为差异不显著。

---
