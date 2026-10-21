# analysis e1 component wise re sj

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_e1_component_wise_re_sj_20260514T091631_result.json`
- **Structured JSON:** [`c60255501359224a9c09.json`](../../sessions/c6/c60255501359224a9c09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

E1 完成。**结论：negative — 乘性惩罚假说被否定。**

关键数据：

| Component | Full ρ | Cond ρ |
|---|---|---|
| head_sj | 0.210 | 0.270 |
| tail_sj | 0.201 | 0.259 |
| type_match | 0.201 | 0.252 |
| **multiplicative** | **0.244** | **0.316** |
| additive | 0.243 | 0.306 |
| fleiss_kappa | **0.278** | **0.307** |

验证通过：multiplicative ρ=0.2441 精确匹配 pilot_004，FK ρ=0.2782 精确匹配。

核心发现：
1. **head_sj ρ=0.210 远低于 NER ρ_sj=0.383**（Δ=-0.173），假说被否定
2. **每个 component 单独都比乘性组合差** — 乘性组合实际上是在 *帮忙*（整合三个信号），不是在 *伤害*
3. **additive fix 无效** — additive ρ ≈ multiplicative ρ（差 0.001）
4. RE 的 SJ 问题不是公式问题，是更根本的：关系级别的 span soft Jaccard 本身就缺乏区分力，Fleiss' kappa 的 surface matching 反而更鲁棒

这排除了方案 B（度量分解）。问题根源不在乘法公式，而在 span-level SJ 度量本身对 RE 任务的适用性。

---
