# analysis cross domain mitigation

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_domain_mitigation_20260522T160911_result.json`
- **Structured JSON:** [`1f57e9d3a29f72a92f94.json`](../../sessions/1f/1f57e9d3a29f72a92f94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个产出文件已生成：

### Part A 关键结论
- **Domain × Condition 交互不显著** (β=-0.303, p=0.187) → retail 和 airline 行为一致
- Retail Δ=+30.6pp, Airline Δ=+37.7pp, 两个 domain 都高度显著
- **模型排序跨域一致性高** (Spearman ρ=0.900, p=0.037)
- **类型排序跨域一致性低** (ρ=0.257, p=0.623) — conditional_precedence 跨域差异最大 (-22.0pp, Fisher p<0.001)

### Part B 关键结论
- **Conditional precedence 和 lexical**: 所有 5 模型一致改善，pooled Δ 分别 -8.1pp (p=0.017) 和 -8.9pp (p=0.019)
- **Auth scope**: 4/5 模型改善（Claude 为 0），pooled -18.0pp (p=0.059)
- **Incompleteness**: 4/5 改善但效应小 (pooled -3.3pp, p=0.320)
- **Model × Mitigation 交互不显著** (p=0.302)，Type × Mitigation 交互边际 (p=0.073)
- Baseline vulnerability 与 mitigation responsiveness 无显著相关 (r=-0.215, p=0.303)

产出文件：
- `artifacts/analysis_cross_domain.json`
- `artifacts/analysis_mitigation_5model.json`
- `artifacts/analysis_cross_domain_mitigation_summary.md`

---
