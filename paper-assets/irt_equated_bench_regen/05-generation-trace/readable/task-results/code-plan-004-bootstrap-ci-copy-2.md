# code plan 004 bootstrap ci

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_004_bootstrap_ci_20260521T035222_result.json`
- **Structured JSON:** [`d9a586b8004f1a5be512.json`](../../sessions/d9/d9a586b8004f1a5be512.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。四个统计量的 BCa bootstrap 95% CI：

| Statistic | Estimate | 95% CI | Boot. SE |
|-----------|----------|--------|----------|
| Pearson *r* (gap vs DIF adv) | −0.478 | [−0.714, −0.155] | 0.148 |
| Spearman *ρ* (gap vs DIF adv) | −0.403 | [−0.687, −0.031] | 0.168 |
| Partial *r* (| GSM8K acc) | −0.385 | [−0.640, −0.058] | 0.152 |
| Domain *ρ* (C% vs acc_change) | 0.307 | [0.025, 0.550] | 0.133 |

所有 CI 均不包含零，point estimates 与已知值精确匹配。报告和脚本已注册。

---
