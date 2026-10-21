# analysis plan 001 fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan-001-fix_20260514T185246_result.json`
- **Structured JSON:** [`6d00937a4186c6ac41f7.json`](../../sessions/6d/6d00937a4186c6ac41f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/plan-001-fix/analysis_report.md`。核心结论：

**Part A — Feature Ablation:**
- full (0.8204) >> surface_only (0.7628) >> reference_only (0.7187)，三者两两差异显著 (p<0.001 / p=0.031)
- 两类特征独立有效，组合有显著增益 (+5.8 ~ +10.2 pts)

**Part B — H1/H2 趋势:**
- H2 (单调漂移) 确认：ttr (rho=-0.63)、hapax_ratio (rho=-0.66) 随 depth 单调下降
- H1 (近平稳) 部分确认：entropy_std/max/tail_decay 平稳，但 **entropy_mean 例外** (rho=-0.68，强漂移)

**Part C — Perplexity:**
- Clean median PPL 单调下降：13.50 → 4.95 → 2.98 → 2.06 → 1.72，Kruskal-Wallis p=0.0

**Claim 2 评估：** 互补性假设成立——full 显著优于任一子集。但 "dual dynamics" 叙事需要修正：entropy_mean 是 reference 特征却呈 H2 漂移，不符合 "reference=stationary" 框架。更精确的表述应区分 reference *shape* features (std/max/tail_decay, 近平稳) 和 reference *level* feature (entropy_mean, 漂移)。

**注意事项：** 结果 JSON 文件未落盘（日志数据完整无损）；depth≥3 特征区分度饱和；gen-1 始终是最难分类的类别。

---
