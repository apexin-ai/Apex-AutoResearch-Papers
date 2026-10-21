# ops exp013 direction bias

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp013_direction_bias_20260521T010913_result.json`
- **Structured JSON:** [`09034eae4cc207097e02.json`](../../sessions/09/09034eae4cc207097e02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 方向分布

| 子集 | formal→casual | casual→formal | f2c 比例 |
|------|:---:|:---:|:---:|
| **总体** (N=100) | 59 | 41 | 59.0% |
| **NLI-pass** (N=88) | 50 | 38 | 56.8% |
| **NLI-fail** (N=12) | 9 | 3 | 75.0% |
| **FN** (NLI-fail + LLM=YES, N=8) | 6 | 2 | 75.0% |
| **TN** (NLI-fail + LLM=NO, N=4) | 3 | 1 | 75.0% |

### 8 个 FN 的具体方向

| ID | original_formality | Direction |
|---|---|---|
| mvp_0014 | formal | formal→casual |
| mvp_0032 | formal | formal→casual |
| mvp_0043 | formal | formal→casual |
| mvp_0050 | formal | formal→casual |
| mvp_0059 | formal | formal→casual |
| mvp_0066 | formal | formal→casual |
| mvp_0029 | casual | casual→formal |
| mvp_0055 | casual | casual→formal |

### 统计检验

| 检验 | 统计量 | p-value | 显著? |
|------|--------|---------|:-----:|
| **Fisher exact**: Direction × NLI result | OR = 0.44 | p = 0.350 (two-sided) | No |
| **Fisher exact**: Direction × FN vs TN | OR = 1.00 | p = 1.000 | No |
| **Binomial**: FN f2c (6/8) vs overall 0.59 | — | p = 0.295 (one-sided) | No |
| **Binomial**: All-fail f2c (9/12) vs overall 0.59 | — | p = 0.205 (one-sided) | No |

### 结论

**方向偏差不显著。** 75% vs 59% 的差异方向上一致（formal→casual 在 NLI-fail 中偏多），但样本量太小（N=8/12），所有检验 p > 0.20。注意 FN 和 TN 子集的 f2c 比例完全相同（都是 75%），说明方向偏差不是 FN 特有的——它存在于整个 NLI-fail 群体，且 FN/TN 内部无差异 (Fisher p=1.0)。以 n=8 做 binomial test，需要 ≥7/8（87.5%）才能在 p<0.05 下拒绝 H0=0.59。

---
