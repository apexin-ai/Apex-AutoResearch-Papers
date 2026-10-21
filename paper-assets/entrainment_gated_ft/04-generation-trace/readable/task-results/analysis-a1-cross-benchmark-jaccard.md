# analysis a1 cross benchmark jaccard

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a1_cross_benchmark_jaccard_20260522T075546_result.json`
- **Structured JSON:** [`92e839c0a07541df125a.json`](../../sessions/92/92e839c0a07541df125a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A1 分析完成。

## 结果摘要

### σ 轨迹（cross-architecture std of accuracy）
| Benchmark | σ_pure | σ_h3-1 | Reduction | ρ | p |
|-----------|--------|--------|-----------|---|---|
| LAMBADA | 0.0240 | 0.0049 | 79.4% | **-1.00** | **0.017** |
| HellaSwag | 0.0117 | 0.0118 | -1.2% | 0.30 | 0.683 |
| PIQA | 0.0046 | 0.0039 | 16.2% | -0.50 | 0.450 |
| ARC-Easy | 0.0004 | 0.0100 | -2411% | 0.30 | 0.683 |

→ σ convergence 是 LAMBADA 特有的（p=0.017），其他三个 benchmark 均不显著。

### Jaccard 轨迹（mean pairwise J across 3 arch pairs）
| Benchmark | h24-1 | h12-1 | h6-1 | h3-1 | ρ | p |
|-----------|-------|-------|------|------|---|---|
| LAMBADA | 0.091 | 0.088 | 0.096 | 0.097 | 0.80 | 0.333 |
| HellaSwag | 0.084 | 0.081 | 0.091 | 0.086 | 0.60 | 0.417 |
| PIQA | 0.089 | 0.096 | 0.089 | 0.095 | 0.00 | 1.000 |
| ARC-Easy | 0.084 | 0.099 | 0.091 | 0.109 | 0.80 | 0.333 |

→ **所有 4 个 benchmark 的 Jaccard 均无显著趋势**（全部 p>0.33）。Jaccard 在 4% attention 即饱和，不随 attention 增加而变化——这是跨 benchmark 的普遍现象。

### Decoupling 确认
Jaccard 饱和（平坦轨迹）vs σ（仅 LAMBADA 下降）：两个量在不同 timescale 上运作，decoupling 不仅限于 LAMBADA。

### 产出文件
- **JSON**: `/root/entrainment_gated_ft/results/a1_cross_benchmark_jaccard/cross_benchmark_jaccard_trajectories.json`
- **Figure**: `/root/entrainment_gated_ft/results/a1_cross_benchmark_jaccard/fig_cross_benchmark_decoupling.pdf`
- LAMBADA σ 验证通过（与 decoupling_data.csv 完全一致）

---
