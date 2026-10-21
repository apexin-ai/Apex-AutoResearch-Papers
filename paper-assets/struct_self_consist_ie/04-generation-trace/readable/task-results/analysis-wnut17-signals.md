# analysis wnut17 signals

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wnut17_signals_20260515T030718_result.json`
- **Structured JSON:** [`f2b94f3ae7fb0b757bd9.json`](../../sessions/f2/f2b94f3ae7fb0b757bd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。汇总如下：

### 数据概况
| 指标 | 值 |
|------|-----|
| n_total | 1287 |
| n_gold_empty | 598 |
| n_after_filter (gold nonempty) | 689 |
| n_f1_positive (F1>0) | 334 |

### 5 信号完整分析

| Signal | Spearman ρ | p-value | AUROC | Cond ρ (F1>0) | Cond p |
|--------|-----------|---------|-------|---------------|--------|
| soft_jaccard | 0.0888 | 0.0197 | 0.5170 | 0.2884 | 8.04e-08 |
| fleiss_kappa | 0.1250 | 0.0010 | 0.5551 | 0.1686 | 0.0020 |
| exact_match | 0.0496 | 0.1935 | 0.4872 | 0.3330 | 4.33e-10 |
| logprob | -0.4095 | 3.07e-29 | 0.2189 | 0.3501 | 4.58e-11 |
| voting_conf | 0.7238 | 7.84e-113 | 0.9127 | 0.0382 | 0.4868 |

### SJ 校对结论

**论文写的 SJ ρ = 0.082 (p=0.106) 是错误的。** 从 raw data 重新计算的确切值是：

- **SJ ρ = 0.0888 (p = 0.0197)**，与 report.json 中的 0.0888 完全一致
- 与论文值差 +0.0068，且 p 值差异显著（0.0197 vs 0.106）
- registry 中 0.089 是正确的（四舍五入），0.062 和 0.082 均不正确

---
