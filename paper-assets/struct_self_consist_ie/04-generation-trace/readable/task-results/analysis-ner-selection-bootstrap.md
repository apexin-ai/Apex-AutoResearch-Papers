# analysis ner selection bootstrap

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ner_selection_bootstrap_20260514T233738_result.json`
- **Structured JSON:** [`d0d49af01cfc1c2f8088.json`](../../sessions/d0/d0d49af01cfc1c2f8088.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

---

## NER Selection F1 Bootstrap 统计报告 (n=529)

### 1. Bootstrap 95% CI (B=10000)

| Method | Mean F1 | 95% CI | Width |
|--------|---------|--------|-------|
| greedy | 0.6439 | [0.6180, 0.6692] | 0.0511 |
| logprob_best | 0.6501 | [0.6246, 0.6751] | 0.0505 |
| sj_best | 0.6450 | [0.6190, 0.6712] | 0.0522 |
| voting_conf_best | 0.6337 | [0.6071, 0.6597] | 0.0527 |

**差值 vs greedy 的 95% CI：**

| Method - greedy | Diff | 95% CI | 含0? |
|-----------------|------|--------|------|
| logprob_best | +0.0061 | [-0.0300, +0.0420] | YES |
| sj_best | +0.0011 | [-0.0352, +0.0377] | YES |
| voting_conf_best | -0.0102 | [-0.0471, +0.0257] | YES |

### 2. Paired Permutation Test (10000 permutations)

| Comparison | Diff | p-value | Sig |
|------------|------|---------|-----|
| logprob_best vs greedy | +0.0061 | 0.3864 | n.s. |
| sj_best vs greedy | +0.0011 | 0.8827 | n.s. |
| voting_conf_best vs greedy | -0.0102 | 0.1868 | n.s. |

### 3. Sign Test

| Comparison | W/T/L | Win% (non-tie) | p-value |
|------------|-------|-----------------|---------|
| logprob_best vs greedy | 61W/398T/70L | 46.6% | 0.4847 |
| sj_best vs greedy | 58W/420T/51L | 53.2% | 0.5657 |
| voting_conf_best vs greedy | 66W/395T/68L | 49.3% | 0.9312 |

### 4. Effect Size (Cohen's d)

| Comparison | d |
|------------|---|
| logprob_best vs greedy | 0.0375 |
| sj_best vs greedy | 0.0066 |
| voting_conf_best vs greedy | -0.0576 |

### 结论

**logprob_best +0.61pp 不显著。** 所有统计检验一致：

- 差值 95% CI 跨越 0（[-0.030, +0.042]）
- Permutation test p=0.39，远高于 0.05
- Sign test 显示 logprob_best 甚至输多赢少（61W vs 70L，win%=46.6%）
- Cohen's d=0.038，几乎无效应

**所有三个信号（logprob、SJ、voting）vs greedy 均不显著。** 529 个实例中，75% 的实例在所有方法间得到相同 F1（ties），实际有差异的实例太少且方向不一致，无法支撑 best-of-N selection 在 NER 上优于 greedy 的结论。

---
