# analysis deepseek paired bootstrap full trace

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_paired_bootstrap_full_trace_20260516T031448_result.json`
- **Structured JSON:** [`8b9761d157b7e442f961.json`](../../sessions/8b/8b9761d157b7e442f961.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。Accuracy 与预期完全匹配，3 对比较均显著（p < 0.001）。

## 结果汇总

| 比较 | Acc A | Acc B | Δ | 95% CI | p_bootstrap | p_McNemar | Sig |
|------|-------|-------|---|--------|-------------|-----------|-----|
| full_trace vs VOTA | 79.16% | 84.45% | -5.29% | [-8.15%, -2.35%] | 3.00e-04 | 4.03e-04 | *** |
| full_trace vs exception_only | 79.16% | 99.33% | -20.17% | [-22.61%, -17.82%] | 1.00e-04 | 8.85e-64 | *** |
| full_trace vs no_trace | 79.16% | 73.36% | +5.80% | [+3.61%, +7.98%] | 1.00e-04 | 3.67e-07 | *** |

所有 3 对差异均在 p < 0.001 水平显著。结果已保存到 `/root/trace-verdict-study/analysis/deepseek_full_trace_paired_bootstrap.json` 并合并到 `deepseek_paired_comparisons.json`。

---
