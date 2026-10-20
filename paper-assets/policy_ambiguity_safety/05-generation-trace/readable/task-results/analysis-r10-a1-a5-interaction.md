# analysis r10 a1 a5 interaction

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r10_a1_a5_interaction_20260521T192247_result.json`
- **Structured JSON:** [`635aba4a4ad18158a64f.json`](../../sessions/63/635aba4a4ad18158a64f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个分析完成。

**A1: C4 sans authorization_scope — Model×Type Interaction**
- χ²(16) = 7.13, p = .971
- LR test: statistic = 9.22, df = 16, p = .904
- **结论: not_significant** — 去除 authorization_scope 后，model×type 交互效应不显著。各模型在剩余 5 种歧义类型上的 violation 分布模式没有显著差异。

**A5: Sans-incompleteness C1 Sensitivity**
- Pooled ambiguous rate: 38.4%, unambiguous rate: 7.5%
- Δpp = 30.98pp, OR = 7.75
- χ² = 338.82, p ≈ 1.15e-75
- **结论: C1 holds without incompleteness** — 即使去掉 incompleteness（效应量最大的类型），歧义条件仍显著提高 violation rate。

---
