# analysis c3 lp range cdf n16 3seed

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c3_lp_range_cdf_n16_3seed_20260515T130825_result.json`
- **Structured JSON:** [`6607a4d337972f6ac103.json`](../../sessions/66/6607a4d337972f6ac103.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### LP Range 统计 (Within-instance, N=16)

| | Median | Q1 | Q3 | IQR |
|---|---|---|---|---|
| Seed 42 | 0.0548 | 0.0368 | 0.0990 | 0.0622 |
| Seed 123 | 0.0608 | 0.0362 | 0.1038 | 0.0676 |
| Seed 456 | 0.0591 | 0.0356 | 0.1046 | 0.0691 |
| **Pooled** | **0.0586** | **0.0361** | **0.1023** | **0.0661** |

**42.6% 的 instances 的 LP range < ε=0.05**（三种子一致：41.2%–44.6%）

### Spearman ρ (LP-F1 相关性)

| | Pooled ρ | Instance-level ρ(LP_range, F1_range) | Per-instance median ρ | Frac sig (p<0.05) |
|---|---|---|---|---|
| Seed 42 | 0.310*** | 0.438*** | 0.256 | 36.3% |
| Seed 123 | 0.312*** | 0.493*** | 0.282 | 34.6% |
| Seed 456 | 0.319*** | 0.472*** | 0.270 | 31.6% |
| **3-seed pooled** | **0.314*** | **0.467*** | — | — |

所有 p-value 极显著。Instance-level ρ≈0.47 说明 LP range 越大的 instance，F1 变异也越大——LP 是质量信号的 ε-free 连续证据。

### 产出文件
- `artifacts/analysis_lp_range_cdf_n16_3seed.json`
- `artifacts/lp_range_cdf_n16_3seed.pdf` + `.png`
- 服务器端同步保存在 `output/` 和 `output/figures/`

---
