# analysis crossover all sparsity

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_crossover_all_sparsity_20260515T111801_result.json`
- **Structured JSON:** [`a613e1bb1e09e7f9bf10.json`](../../sessions/a6/a613e1bb1e09e7f9bf10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果非常清晰。

## 结果

**Crossover 在全部 4 个 sparsity level 都确认成立**，所有 p < 0.001。

### CSV (`crossover_all_sparsity.csv`)

```
model,sparsity,phase,imp_median,imp_ci_lo,imp_ci_hi,rand_median,rand_ci_lo,rand_ci_hi,diff_median,diff_ci_lo,diff_ci_hi,wilcoxon_p,significant,n
deepseek,s015,high,0.002946,0.001192,0.005001,0.083326,0.065059,0.098782,0.087300,0.063454,0.107986,0.000000,yes,496
deepseek,s015,low,0.352830,0.318855,0.391251,0.088911,0.072531,0.114714,0.260726,0.212264,0.316819,0.000000,yes,500
deepseek,s020,high,0.007754,0.003370,0.011420,0.270200,0.241218,0.324652,0.258850,0.226714,0.316763,0.000000,yes,496
deepseek,s020,low,1.198240,1.089282,1.303709,0.349124,0.302835,0.440463,0.733340,0.598388,0.868002,0.000000,yes,500
deepseek,s025,high,0.021203,0.016759,0.026641,1.113415,1.020394,1.292353,1.037503,0.909390,1.140881,0.000000,yes,496
deepseek,s025,low,3.970990,3.476264,4.405446,1.498281,1.229960,1.709960,2.213629,1.590189,2.883303,0.000000,yes,500
deepseek,s030,high,0.037857,0.032560,0.047639,3.112067,2.697992,3.607944,2.856017,2.403335,3.572314,0.000000,yes,496
deepseek,s030,low,8.456054,7.779761,9.762422,3.839887,3.224448,4.425942,4.735251,3.260817,6.004473,0.000000,yes,500
```

### 关键发现

| Sparsity | Crossover | Reversal Magnitude | High Diff | Low Diff |
|----------|-----------|-------------------|-----------|----------|
| s015 | YES *** | 2.99x | 0.087 | 0.261 |
| s020 | YES *** | 2.83x | 0.259 | 0.733 |
| s025 | YES *** | 2.13x | 1.038 | 2.214 |
| s030 | YES *** | 1.66x | 2.856 | 4.735 |

**s015 的担忧没有成真**——虽然绝对值很小（high diff=0.087, low diff=0.261），但 Wilcoxon p=1.35e-21 和 p=2.59e-17，crossover 仍然高度显著。

**Reversal magnitude 随 sparsity 递减**：s015 (2.99x) → s030 (1.66x)。低 sparsity 时 low-phase dominance 相对更强；高 sparsity 时 high-phase diff 增长更快（拉近比例）。

**论文可以写 "across all sparsity levels"。**

CSV 和 MD 已保存到服务器 `/root/autodl-tmp/pacs_analysis/sf5_asymmetric/crossover_all_sparsity.{csv,md}`。

---
