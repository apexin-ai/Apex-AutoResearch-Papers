# analysis bootstrap ci decoupling

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-ci-decoupling_20260520T011928_result.json`
- **Structured JSON:** [`0c93bc37bd80914638b1.json`](../../sessions/0c/0c93bc37bd80914638b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### σ (architecture std) — 95% Bootstrap CI

| Ratio | Point | 95% CI |
|-------|-------|--------|
| pure | 0.02431 | [0.01930, 0.02955] |
| h24-1 | 0.01647 | [0.01162, 0.02172] |
| h12-1 | 0.01462 | [0.00969, 0.02019] |
| h6-1 | 0.00643 | [0.00240, 0.01165] |
| h3-1 | 0.00537 | [0.00180, 0.01057] |

### J_helped (mean pairwise Jaccard) — 95% CI

| Ratio | Point | 95% CI |
|-------|-------|--------|
| h24-1 | 0.0945 | [0.0826, 0.1066] |
| h12-1 | 0.0954 | [0.0834, 0.1075] |
| h6-1 | 0.0904 | [0.0790, 0.1023] |
| h3-1 | 0.0964 | [0.0844, 0.1088] |

### J_hurt (mean pairwise Jaccard) — 95% CI

| Ratio | Point | 95% CI |
|-------|-------|--------|
| h24-1 | 0.0860 | [0.0745, 0.0978] |
| h12-1 | 0.0775 | [0.0667, 0.0891] |
| h6-1 | 0.0980 | [0.0857, 0.1105] |
| h3-1 | 0.0932 | [0.0814, 0.1057] |

### Key Finding

**σ CIs non-overlapping between pure and h3-1** (pure lower bound 0.01930 > h3-1 upper bound 0.01057) **→ 显著下降**。同时 **J CIs 在所有 ratio 间完全重叠 → Jaccard 保持 flat**。

统计证据支持 decoupling：attention 增加时 accuracy variance 显著收敛，但 example-level 帮助/伤害的架构间 overlap 模式不变。

结果已保存到 `/root/entrainment_gated_ft/bootstrap_ci_results.json`。

---
