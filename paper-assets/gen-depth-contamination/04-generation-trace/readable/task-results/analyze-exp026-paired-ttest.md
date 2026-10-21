# analyze exp026 paired ttest

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp026-paired-ttest_20260518T114213_result.json`
- **Structured JSON:** [`dd3a740eb48febcd2379.json`](../../sessions/dd/dd3a740eb48febcd2379.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `artifacts/exp_026_ttest/results_summary.md`。

核心结论：

**graduated vs no_filter：差异不显著（null result confirmed）**
- MMLU: +0.01pp, p=0.692, d=0.19
- HellaSwag: -0.01pp, p=0.245, d=-0.61
- 两个指标的 95% CI 都包含零

**binary vs no_filter：存在显著 trade-off**
- MMLU: -0.23pp (p=0.005, survives Bonferroni)
- HellaSwag: +0.41pp (p<0.00001, survives Bonferroni)

**graduated vs binary：显著差异（与上面同一 trade-off pattern）**
- MMLU: +0.24pp (p=0.015, 不过 Bonferroni)
- HellaSwag: -0.43pp (p<0.0001, 过 Bonferroni)

graduated (alpha=0.9) 在统计上等同于 no_filter，是个 no-op。binary filtering 有真实但很小的 MMLU/HellaSwag trade-off。

---
