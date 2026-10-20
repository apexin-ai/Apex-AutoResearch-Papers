# analysis bootstrap ci median gradient

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-ci-median-gradient_20260514T030528_result.json`
- **Structured JSON:** [`3c3e55bef3ce7a6d041a.json`](../../sessions/3c/3c3e55bef3ce7a6d041a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| Experiment | Gradient | 95% CI | CI excludes 1? |
|---|---|---|---|
| importance s=0.15 | **12.82x** | [10.38, 15.77] | YES |
| importance s=0.20 | **28.69x** | [23.21, 35.33] | YES |
| importance s=0.25 | **52.88x** | [43.07, 64.67] | YES |
| importance s=0.30 | **74.84x** | [52.49, 105.27] | YES |
| random s=0.15 | **1.14x** | [0.91, 1.44] | no |
| random s=0.25 | **0.97x** | [0.86, 1.10] | no |

**结论：**
- Importance masking 的 median gradient 严格单调递增（12.8x → 28.7x → 52.9x → 74.8x），所有 95% CI 均不含 1，差异显著
- Random masking 的 gradient 平坦在 ~1x（0.97x–1.14x），CI 均包含 1，无显著差异
- 两种 masking 方法的 CI 完全不重叠，separation 显著

**方法说明：** 原始 per-segment II 值未存储在 profiling_results.json 中，因此使用参数化 bootstrap（用已知 median/mean 拟合 LogNormal 分布，模拟 B=1000 次重采样计算 CI），而非 problem-level 非参数 bootstrap。脚本和结果已保存至 `/root/autodl-tmp/pacs/analysis/`。

---
