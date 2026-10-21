# analysis jt trend test

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_jt-trend-test_20260517T042500_result.json`
- **Structured JSON:** [`270e479dc8d93677e2d3.json`](../../sessions/27/270e479dc8d93677e2d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
Seed  42: J = 12227.5, z = 14.8007, p < 1e-48
Seed 123: J = 12144.0, z = 14.5847, p < 1e-48
Seed 456: J = 12138.5, z = 14.5701, p < 1e-48
Pooled:   J = 109707.0, z = 25.4964, p < 1e-48
```

所有 p-value 远小于 0.001（scipy 报告为 0.00e+00，即超出 float64 精度下限）。单调递减趋势极其显著。

建议论文句子：

> "Formal trend analysis confirms monotonic decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$, pooled across three seeds)."

---
