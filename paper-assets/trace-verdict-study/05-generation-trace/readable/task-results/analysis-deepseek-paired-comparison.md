# analysis deepseek paired comparison

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_paired_comparison_20260516T024634_result.json`
- **Structured JSON:** [`05ff4430822ef855cb57.json`](../../sessions/05/05ff4430822ef855cb57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已生成并保存。确认 exception_only 是 seed42 版本 (99.33%)，VOTA 是 max_length=16384 版本 (84.45%)。

## DeepSeek Paired Comparisons (n=1190, seed42)

| Pair (A vs B) | Acc_A | Acc_B | Δ(A-B) | 95% CI | McNemar p | sig |
|---|---|---|---|---|---|---|
| VOTA vs exception_only | 84.45% | 99.33% | -14.87% | [-17.06, -12.77] | 6.86e-45 | *** |
| VOTA vs full_trace | 84.45% | 79.16% | +5.29% | [+2.35, +8.15] | 4.03e-04 | *** |
| VOTA vs no_trace | 84.45% | 73.36% | +11.09% | [+8.07, +14.20] | 2.50e-12 | *** |
| exception_only vs full_trace | 99.33% | 79.16% | +20.17% | [+17.82, +22.61] | 8.85e-64 | *** |
| exception_only vs no_trace | 99.33% | 73.36% | +25.97% | [+23.36, +28.66] | 8.49e-83 | *** |
| full_trace vs no_trace | 79.16% | 73.36% | +5.80% | [+3.61, +7.98] | 3.67e-07 | *** |

所有 6 对比较均高度显著 (p < 0.001)。文件已保存至：
- `/root/trace-verdict-study/analysis/deepseek_paired_comparisons.json`
- `/root/trace-verdict-study/analysis/deepseek_paired_comparisons.txt`

---
