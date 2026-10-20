# research q1q6 answer prep d105

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_q1q6_answer_prep_d105_20260516T045413_result.json`
- **Structured JSON:** [`fe4709d91c19ec43b7eb.json`](../../sessions/fe/fe4709d91c19ec43b7eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已写入 `artifacts/q1q6_answer_prep/answers.md` 并注册。

每个 Q 的核心策略：

- **Q1 (RE scope)**: 不加 TACRED（结构不兼容），改 title/scope 限定为 NER-focused + RE exploratory。12 configurations 一致的 binary dominance pattern 是防守点。
- **Q2 (ε circularity)**: 删除 "data-driven justification"，ε-free 连续指标 (median range 0.041, pooled ρ=0.248) 作主呈现，ε sweep 标 post-hoc。主结论 (Table 2) 完全不依赖 ε。
- **Q3 (Contribution 1 trivial)**: Reframe 为 empirical dissociation（ρ/AUROC/selection F1 三指标解耦），instance-level/per-sample 分类移入 §3 作前提。EM "best filter worst ranker" 悖论是 key evidence。
- **Q4 (signal combination)**: LR ensemble 已做且 negative (AUROC 0.666 < EM 0.749)。VC quartile 分层分析代替 binary threshold cascade。
- **Q5 (scale + seeds)**: 所有 scale claims 限定 "within 3B-8B"，删除 Kendall W=1.000 强结论，改为 descriptive consistency。
- **Q6 (RE reversal)**: Binary dominance mechanism——RE LP full ρ=0.266 vs cond ρ=0.011 (p=0.86)，LP 的 RE 信号完全来自 zero/nonzero split。

三个 MF 全部是写作/framing 调整，无需新实验，关键路径在 Paper Agent。

---
