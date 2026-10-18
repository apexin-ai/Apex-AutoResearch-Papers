# code greedy cardinality ablation

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_greedy_cardinality_ablation_20260514T062233_result.json`
- **Structured JSON:** [`fe1bb172664181c110ba.json`](../../sessions/fe/fe1bb172664181c110ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan_016 已完成。Artifact 也已存在。

**结果汇总：**

| Method | PPL | 2-bit | 4-bit | 8-bit | 16-bit |
|--------|-----|-------|-------|-------|--------|
| Greedy unconstrained | 32.45 | 68 | 30 | 4 | 10 |
| Greedy + max_2bit=8 | 11.23 | 8 | 100 | 4 | 0 |
| MCKP constrained k=8 | 11.23 | 8 | 100 | 4 | 0 |

**结论：** Greedy + cardinality constraint 与 MCKP constrained 产出**完全相同的 bit 分配**，PPL 差异仅 0.0012。这说明贡献来自 cardinality constraint 本身，而非 MCKP solver。MCKP 在此约束下的优化间隙可忽略不计。

Registry 已更新为 DONE/success，metrics 已写入。

---
