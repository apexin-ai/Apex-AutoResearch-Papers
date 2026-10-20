# ssh scierc conll n8 mv recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scierc_conll_n8_mv_recompute_20260522T034721_result.json`
- **Structured JSON:** [`8e0bdb2e29bbe6c39ff5.json`](../../sessions/8e/8e0bdb2e29bbe6c39ff5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个数据集的 MV strict recompute 完成。

## 结果汇总

### SciERC N=8, seed=42 (autodl-5090)

| 指标 | 值 |
|------|-----|
| greedy_f1 | 0.6683 |
| mv_strict_f1 | 0.6558 |
| oracle_f1 | 0.7840 |
| mv_delta (strict) | -1.24pp |
| degeneracy_rate | 13.4% |
| alpha_crit_eff_strict | 0.3859 |

### CoNLL N=8, seed=42 (autodl-5090-c)

| 指标 | 值 |
|------|-----|
| greedy_f1 | 0.9123 |
| mv_strict_f1 | 0.9101 |
| oracle_f1 | 0.9538 |
| mv_delta (strict) | -0.22pp |
| degeneracy_rate | 60.1% |
| alpha_crit_eff_strict | 2.0903 |

注：CoNLL 的 `conll_mf4v2_seed42` 数据在 autodl-5090-c 上，不在 autodl-5090。

---
