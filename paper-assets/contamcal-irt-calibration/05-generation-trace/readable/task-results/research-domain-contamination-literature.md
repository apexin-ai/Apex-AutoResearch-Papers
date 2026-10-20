# research domain contamination literature

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_domain-contamination-literature_20260516T150810_result.json`
- **Structured JSON:** [`1fe14dccdf6d909ca035.json`](../../sessions/1f/1fe14dccdf6d909ca035.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心结论：

**我们的发现具有三重新颖性：**

1. **方向反转（γ < 0）**— 无论文报告 contamination 对特定 domain 有负面效果。现有工作一律假设 contamination 提升或无影响。

2. **IRT γ 作为效果量化器** — PSN-IRT (AAAI 2026) 用 guessing parameter (c) 做 contamination *检测*；我们用 γ 做 contamination *效果方向和幅度*的量化，这是未报告的用法。

3. **Simpson's paradox 框架** — 无论文将 Simpson's paradox 应用于 benchmark contamination 分析。Aggregate γ 掩盖了 domain 级别的反向效应。

最接近的竞争者是 Reddy & Karmakar (2026) 报告了 domain 间 contamination *率*的差异，但仍假设方向一致（正向）。我们是第一个量化 contamination 可以在某些 domain 伤害模型表现的工作。

报告保存在：`artifacts/literature_survey_domain_dependent_contamination.md`

---
