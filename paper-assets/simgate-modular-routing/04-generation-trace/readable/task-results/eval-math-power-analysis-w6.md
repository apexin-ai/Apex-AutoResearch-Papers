# eval math power analysis w6

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_math-power-analysis-w6_20260516T192329_result.json`
- **Structured JSON:** [`6d0548747f2f4c1017f4.json`](../../sessions/6d/6d0548747f2f4c1017f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
=== MATH Post-hoc Power Analysis ===

Setup:
  N = 300 paired samples
  Effect: 4.3pp (81.0% vs 76.7%)
  Test: McNemar (chi-squared)
  Observed: chi2 = 3.073, p = 0.0796
  Discordant pairs: 55 (b=34, c=21)

Results:
  Post-hoc power: 0.4181 (41.8%)
  Required N for 80% power: 770
  Required N for 90% power: 1030

Interpretation:
  Severely underpowered — the study had little chance of detecting a true 4.3pp effect
```

N=300 时 power 仅 41.8%，远低于 80% 门槛。达到 80% power 需 N=770，90% 需 N=1030。p=0.079 的非显著结果是 power 不足导致的，不能解读为"无效果"。结果已存入 `guided_router/math_power_results.json`。

---
