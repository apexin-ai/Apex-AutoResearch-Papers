# research r14 rho computation

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r14_rho_computation_20260522T135212_result.json`
- **Structured JSON:** [`367322107dae6fcc894c.json`](../../sessions/36/367322107dae6fcc894c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

- **6 types (all)**: Spearman ρ = 0.09, p = 0.87 — 近乎无相关
- **5 types (excl. auth scope)**: Spearman ρ = 0.90, p = 0.037 — 强正相关且显著

排除 auth scope 后，两个 judge group 的 type 排序高度一致。近零相关几乎完全由 auth scope 这一个 type 驱动（该 type 在 GPT-5.4-judged 组排最低 28%，在 GPT-4.1-judged 组排最高 62%）。

结果已写入 `artifacts/r14_rho_computation.md`。

---
