# analysis exp017 lp range

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp017_lp_range_20260515T154349_result.json`
- **Structured JSON:** [`47f79975341febbbd6ca.json`](../../sessions/47/47f79975341febbbd6ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新，artifact 已注册。

---

## 结果汇总

### Part 1: LP Range — T=0.7 vs T=1.0

| 统计量 | T=0.7 | T=1.0 |
|--------|------:|------:|
| median | 1.15e-05 | 2.28e-04 |
| IQR | [~0, 0.0181] | [~0, 0.0317] |
| mean | 0.0111 | 0.0198 |
| **tied_fraction(ε=0.05)** | **95.79%** | **86.76%** |

**T=0.7 的 LP tied fraction 比 T=1.0 高 9 个百分点**（95.8% vs 86.8%）。低温进一步压缩 LP range，强化 "LP compression is intrinsic to structured output" 的 claim — 即使在更集中的采样分布下，logprob 仍然无法区分样本。

### Part 2: 5-signal ρ + AUROC

| Signal | T=0.7 ρ | T=1.0 ρ | T=0.7 AUROC | T=1.0 AUROC |
|--------|--------:|--------:|------------:|------------:|
| SJ | 0.3934 | 0.4314 | 0.6506 | 0.7039 |
| FK | 0.3879 | 0.4277 | 0.6488 | 0.7026 |
| VC | 0.3750 | 0.4256 | 0.6551 | 0.7088 |
| EM | 0.3888 | 0.4306 | 0.6494 | 0.7046 |
| LP | 0.2951 | 0.3072 | 0.7509 | 0.7610 |

所有信号在 T=0.7 下 ρ 和 AUROC 均下降（低温减少多样性 → 信号区分力降低），但 LP 的 AUROC 仍然最高（0.7509），LP 的 ρ 仍然最低（0.2951）— correlation-AUROC dissociation 依然成立。

### Part 3: Selection F1

| Method | F1 | Δ greedy |
|--------|---:|--------:|
| Greedy | 0.9242 | — |
| Oracle | 0.9391 | +1.49 pp |
| SJ | 0.9247 | +0.05 pp |
| FK | 0.9254 | +0.12 pp |
| **VC** | **0.9264** | **+0.22 pp** |
| EM | 0.9255 | +0.13 pp |
| LP | 0.9248 | +0.06 pp |

Oracle headroom 只有 1.49 pp（T=1.0 下约 1.41 pp），所有信号的 selection gain 微弱但为正。VC 仍然表现最好。

---
