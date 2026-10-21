# analysis n32 bootstrap significance

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n32_bootstrap_significance_20260516T160827_result.json`
- **Structured JSON:** [`22067a13d5a1a35c522a.json`](../../sessions/22/22067a13d5a1a35c522a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Bootstrap Test: Signal Selection vs Greedy (N=529 instances, B=10000)

| Signal | Mean Δ (pp) | 95% CI | p-value | Significant? |
|--------|------------|--------|---------|-------------|
| **LP** | +0.95 | [-0.41, +2.34] | 0.091 | No |
| SJ | +0.36 | [-0.66, +1.38] | 0.244 | No |
| FK | +0.66 | [-0.36, +1.67] | 0.101 | No |
| EM | +0.22 | [-0.99, +1.44] | 0.355 | No |
| VC | -4.36 | [-6.26, -2.37] | 1.000 | No (significantly *worse*) |
| Oracle | +20.00 | [+17.98, +22.10] | 0.000 | Yes *** |

### Permutation Test: Signal Selection vs Random Selection

| Signal | Obs Δ (pp) | p-value | Significant? |
|--------|-----------|---------|-------------|
| **LP** | +4.56 | <0.0001 | Yes *** |
| SJ | +3.96 | <0.0001 | Yes *** |
| FK | +4.27 | <0.0001 | Yes *** |
| EM | +3.84 | 0.0002 | Yes *** |
| VC | -0.74 | 0.741 | No |

### 论文建议

**不能 claim "statistically significant improvement over greedy"**。LP 的 p=0.091 接近但未达 0.05 阈值，95% CI 跨越零。529 个 instances 上 +0.95pp 的 effect size 太小，方差太大。

**可以 claim 的**：
1. **所有信号（除 VC）都显著优于随机选择**（permutation test, p<0.001）——说明信号确实携带信息，不是随机噪声
2. **LP 是最佳信号**，但与 FK 无统计显著差异（p=0.33）
3. **Oracle gap 巨大**（+20pp, p<0.001）——说明 sample pool 中存在大量可利用的质量差异，但现有信号未能充分挖掘
4. **VC 是唯一显著低于 greedy 的信号**（95% CI 完全在零以下）

建议论文措辞：*"LP selection shows a consistent positive trend (+0.95pp, p=0.09) but does not reach statistical significance at α=0.05. However, all consistency-based signals except VC significantly outperform random selection (p<0.001), confirming that these signals carry meaningful quality information. The large oracle gap (+20pp) suggests substantial room for improved selection mechanisms."*

---
