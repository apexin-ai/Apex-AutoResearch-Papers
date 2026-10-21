# ssh alpha crit conll s42 gemini

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_alpha_crit_conll_s42_gemini_20260521T111401_result.json`
- **Structured JSON:** [`7d0de1f0a0ef4bee627e.json`](../../sessions/7d/7d0de1f0a0ef4bee627e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两组数据提取完毕。汇总如下：

---

### CoNLL MF4v2 seed=42 α_crit 数据

| 指标 | 值 |
|---|---|
| greedy_f1 | 0.9075 |
| mv_f1 (≥4/8) | 0.9090 |
| oracle_f1 | 0.9495 |
| Δ_SC | +0.15 pp |
| degen | 65.7% (2270/3453) |
| fleiss_kappa | 0.7729 |
| soft_jaccard | 0.8949 |
| α_crit | 0.8332 (= π_MV / (2 − π_MV)) |
| α_crit_eff | 2.4321 (= α_crit / (1 − δ)) |

**注意**：α_crit_eff > 1.0，说明 65.7% 的高 degeneracy 使得有效阈值不可达。模型已经在大多数实例上是确定性的，MV 几乎没有余地改进。Oracle headroom +4.20 pp 全部来自非退化实例。

---

### Gemini Frontier SC 详细 (FewNERD, n=200)

| 指标 | 值 |
|---|---|
| greedy_f1 | 0.6301 |
| mv_f1 | 0.6446 |
| oracle_f1 | 0.7575 |
| Δ_SC | +1.45 pp |
| degen | 28.5% (57/200) |
| α_crit | 0.4756 |
| α_crit_eff | 0.6651 |
| agreement_rho (vs F1) | 0.3887 |
| fleiss_kappa (mean) | 0.5185 |
| soft_jaccard (mean) | 0.8023 |
| parse_failure_rate | 11.9% (191/1600) |

**Per-instance F1 分布**：
- Greedy: mean=0.6301, median=0.6667, std=0.3661
- MV: mean=0.6446, median=0.6905, std=0.3606
- Oracle: mean=0.7575, median=1.0000, std=0.3268

**MV gain 模式**：
- MV > Greedy: 33 (16.5%)
- MV == Greedy: 144 (72.0%)
- MV < Greedy: 23 (10.5%) — SC hurts
- rho(agreement, mv_gain) = −0.0905 (p=0.20, 不显著)

**Failure mode**：
- F3_both_good: 125 (62.5%)
- F4_both_bad: 43 (21.5%)
- F1_sc_hurts: 21 (10.5%)
- F2_sc_helps: 11 (5.5%)

**Selection gap**: oracle − MV = 11.29 pp，表明 MV 只捕获了 oracle headroom 的 ~11% (1.45/12.74)，大量改进空间在 smarter aggregation。

---
