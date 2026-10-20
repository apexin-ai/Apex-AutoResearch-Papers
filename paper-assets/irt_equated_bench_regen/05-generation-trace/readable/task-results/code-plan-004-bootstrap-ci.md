# code plan 004 bootstrap ci

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_004_bootstrap_ci_20260521T033133_result.json`
- **Structured JSON:** [`cf81ece45cb273cadd32.json`](../../sessions/cf/cf81ece45cb273cadd32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。BCa bootstrap (n=10,000) 结果：

| Statistic | Estimate | 95% BCa CI | p |
|-----------|----------|------------|---|
| Pearson r (gap vs dif_advantage) | −0.478 | [−0.714, −0.155] | 0.005 |
| Spearman ρ (gap vs dif_advantage) | −0.403 | [−0.687, −0.031] | 0.020 |
| Partial r (controlling gsm8k_acc) | −0.385 | [−0.640, −0.058] | 0.030 |

三个 CI 均不跨零，点估计与 Step 3 报告完全一致。Spearman ρ 的 CI 上界接近零（−0.031），说明 rank-based 估计的不确定性较大，但仍显著。

产出已注册：`art_20260521_882fe3`（报告）、`art_20260521_9315bd`（脚本）。

---
