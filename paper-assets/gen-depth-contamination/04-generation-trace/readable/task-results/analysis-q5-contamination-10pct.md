# analysis q5 contamination 10pct

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_q5_contamination_10pct_20260520T044840_result.json`
- **Structured JSON:** [`2ca6bda98242ac2d4c6a.json`](../../sessions/2c/2ca6bda98242ac2d4c6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。汇总如下：

---

## 10% contamination: binary classifier vs no-filter

| | MMLU (5-seed mean) |
|---|---|
| **no_filter** | 60.58% |
| **binary_ours** | 60.79% |
| **pp 差距** | **+0.21 pp** |
| **p-value** | **0.00103** (paired t-test, Holm-Bonferroni corrected α=0.0125, **显著**) |
| Cohen's d | 3.82 |

---

## 全部 contamination ratios 汇总 (binary_ours vs no_filter, MMLU)

| Ratio | no_filter | binary_ours | Δ (pp) | p-value | Significant? |
|-------|-----------|-------------|--------|---------|-------------|
| **10%** | 60.58 | 60.79 | **+0.21** | **0.00103** | **Yes** (α=0.0125) |
| 30% | 60.69 | 60.82 | +0.13 | 0.0739 | No (α=0.0167) |
| 50% | 60.63 | 60.88 | +0.25 | 0.0377 | No (α=0.0167) |

---

**数据来源**: `/root/autodl-tmp/gen-depth-contamination/results/exp_009_dose_response/ratio_{10,30,50}/statistical_analysis.json`

10% ratio 是唯一在 MMLU 上通过 Holm-Bonferroni 校正后仍显著的条件（p=0.00103, d=3.82）。差距虽仅 0.21 pp，但跨 5 个 seed 非常稳定（binary_ours std=0.044%, no_filter std=0.018%）。

---
