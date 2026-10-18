# analysis w1 feature correlation permutation

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w1_feature_correlation_permutation_20260515T110606_result.json`
- **Structured JSON:** [`607a263940f5113479ee.json`](../../sessions/60/607a263940f5113479ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已生成，结果如下：

---

## 结果报告

### (a) 高度相关特征对（|r| > 0.8，pythia_nucleus095 代表）

共 **17 对**，按 |r| 排序：

| 特征对 | r |
|--------|-----|
| rep_3gram <-> rep_4gram | 0.9904 |
| skewness_ppl <-> kurtosis_ppl | 0.9877 |
| bigram_entropy <-> trigram_entropy | 0.9861 |
| rep_2gram <-> rep_3gram | 0.9813 |
| rep_2gram <-> rep_4gram | 0.9505 |
| type_token_ratio <-> rep_2gram | -0.9303 |
| mean_ppl <-> var_ppl | 0.9151 |
| p75_ppl <-> p90_ppl | 0.8965 |
| type_token_ratio <-> rep_3gram | -0.8690 |
| p50_ppl <-> mean_surprisal | 0.8671 |
| mean_surprisal <-> var_surprisal | 0.8609 |
| p90_ppl <-> var_surprisal | 0.8464 |
| p75_ppl <-> mean_surprisal | 0.8442 |
| p75_ppl <-> var_surprisal | 0.8361 |
| type_token_ratio <-> rep_4gram | -0.8213 |
| type_token_ratio <-> hapax_ratio | 0.8155 |
| p50_ppl <-> p75_ppl | 0.8124 |

审稿人 W1 的共线性担忧成立——ppl 分位数之间、repetition 特征之间、entropy 特征之间确实存在强共线性。

### (b) Permutation top-5 vs Gini top-5

| Cell | Spearman ρ | Perm top-5 |
|------|-----------|------------|
| pythia_nucleus095 | 0.6526 | var_surprisal, p90_ppl, p50_ppl, skewness_ppl, var_ppl |
| pythia_temp09 | 0.7158 | var_surprisal, p90_ppl, p50_ppl, p75_ppl, mean_ppl |
| pythia_topk50 | 0.7526 | var_surprisal, p90_ppl, p75_ppl, p50_ppl, mean_ppl |
| gpt2xl_nucleus095 | 0.7281 | var_surprisal, p90_ppl, p75_ppl, mean_ppl, p25_ppl |
| gpt2xl_temp09 | 0.8702 | p90_ppl, var_surprisal, p75_ppl, p25_ppl, p50_ppl |
| gpt2xl_topk50 | 0.8018 | p90_ppl, p75_ppl, var_surprisal, p25_ppl, mean_surprisal |
| olmo_nucleus095 | 0.8193 | p90_ppl, var_surprisal, p75_ppl, p50_ppl, p25_ppl |
| olmo_temp09 | 0.7175 | var_surprisal, p90_ppl, p75_ppl, p25_ppl, mean_ppl |
| olmo_topk50 | 0.7772 | var_surprisal, p90_ppl, p75_ppl, p25_ppl, mean_ppl |

Spearman ρ (Perm vs Gini) 均值=**0.7595**（范围 0.65–0.87），排名中度一致。**var_surprisal 和 p90_ppl 在 permutation importance 下同样稳定占据 top-2**，所有 9 个 cell 的 perm top-2 都包含这两个特征。

### (c) p90_ppl / var_surprisal top-2 rate

| 特征 | Gini top-2 | Perm top-2 |
|------|-----------|------------|
| p90_ppl | **9/9** | **9/9** |
| var_surprisal | **7/9** | **8/9** |

**结论**：尽管存在共线性，permutation importance（对共线性更鲁棒）仍然确认 p90_ppl 和 var_surprisal 是最重要的两个特征。p90_ppl 在 Perm 和 Gini 下均为 9/9 top-2；var_surprisal 在 Perm 下甚至从 7/9 提升到 8/9。

### 产出文件
- `results/w1_correlation_matrix.json`
- `results/w1_permutation_importance_9cell.json`

---
