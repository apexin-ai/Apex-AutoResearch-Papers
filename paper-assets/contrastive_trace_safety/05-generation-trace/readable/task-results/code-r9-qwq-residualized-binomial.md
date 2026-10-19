# code r9 qwq residualized binomial

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r9_qwq_residualized_binomial_20260518T081600_result.json`
- **Structured JSON:** [`99b0f0d3d1b8e642e2c0.json`](../../sessions/99/99b0f0d3d1b8e642e2c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
QwQ-32B Residualized HS vs Chance:
  Observed BA: 0.619 (pooled) / 0.667 (macro-avg per trace)
  H0: BA = 0.5
  
  Wilcoxon signed-rank: p = 0.0024 *
  One-sample t-test:    p = 0.0008 *
  Permutation test:     p < 0.0005 * (0/2000 exceeded observed)
  95% Bootstrap CI:     [0.575, 0.744]
  
  Conclusion: SIGNIFICANT at α = 0.05 (all three tests)
```

**BA 差异说明**: exp_r8 报告的 BA=0.612 是其代码路径的聚合值，与本次 pooled BA=0.619 基本一致（微小差异来自 `per_trace_metrics` 的聚合方式）。Macro-average per-trace BA=0.667 更高，因为各 trace 长度不等，短 trace 在 pooled 中权重低但在 macro 中权重相同。

**关键发现**: 16/19 traces BA > 0.5，仅 2 traces < 0.5（BA=0.217 和 0.183，可能是异常 trace）。即使 residualized 后去除了位置信息，HS probe 仍显著高于 chance，说明 hidden states 中确实编码了超越位置的安全相关信号。

---
