# analysis k5 aggregation reinvestigate

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-aggregation-reinvestigate_20260524T070032_result.json`
- **Structured JSON:** [`3738790e0204cde4b60d.json`](../../sessions/37/3738790e0204cde4b60d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部收集完毕。以下是完整报告。

---

## 文件清单

| # | 路径 | 大小 | 修改时间 | 备注 |
|---|------|------|----------|------|
| A | `_project/data/k5_aggregation_bootstrap.json` | 71,279 | May 23 14:33 | 原始 |
| B | `results/plan001/k5_aggregation_bootstrap.json` | 71,140 | **May 24 14:13** | 重跑版 |
| C | `server_backup/results/plan001/k5_aggregation_bootstrap.json` | 71,279 | May 23 14:32 | 原始备份 |

文件 A 和 C 大小一致（71,279），是同一份数据。文件 B 是 May 24 重新生成的，大小不同（71,140），内容不同。

---

## 文件 A（原始，May 23）—— K_eff = **7/9/10/0**（differentiated）

| Method | K_eff sig | η_max sig |
|--------|-----------|-----------|
| majority_vote | **7/12** | 0/12 |
| weighted_vote | **9/12** | 1/12 |
| threshold_supermajority | **10/12** | 6/12 |
| bayesian | **0/12** | 1/12 |

### majority_vote keff_fdr_p（7/12 sig）

| Condition | keff_fdr_p | Sig |
|-----------|------------|-----|
| mmlu×prompt_injection | 0.0162 | *** |
| mmlu×sycophancy | 0.0247 | *** |
| mmlu×score_manipulation | 0.0162 | *** |
| mmlu×verbosity_bias | 0.0162 | *** |
| mmlu×position_bias | 0.1151 | |
| mmlu×authority_bias | 0.3136 | |
| arc×prompt_injection | 0.0315 | *** |
| arc×sycophancy | 0.1880 | |
| arc×score_manipulation | 0.0162 | *** |
| arc×verbosity_bias | 0.1327 | |
| arc×position_bias | 0.0315 | *** |
| arc×authority_bias | 0.1817 | |

### weighted_vote keff_fdr_p（9/12 sig）

| Condition | keff_fdr_p | Sig |
|-----------|------------|-----|
| mmlu×prompt_injection | 0.0124 | *** |
| mmlu×sycophancy | 0.0204 | *** |
| mmlu×score_manipulation | 0.0144 | *** |
| mmlu×verbosity_bias | 0.0124 | *** |
| mmlu×position_bias | 0.0238 | *** |
| mmlu×authority_bias | 0.0574 | |
| arc×prompt_injection | 0.0275 | *** |
| arc×sycophancy | 0.7911 | |
| arc×score_manipulation | 0.0124 | *** |
| arc×verbosity_bias | 0.0332 | *** |
| arc×position_bias | 0.0234 | *** |
| arc×authority_bias | 0.0657 | |

### threshold_supermajority keff_fdr_p（10/12 sig）

| Condition | keff_fdr_p | Sig |
|-----------|------------|-----|
| mmlu×prompt_injection | 0.0032 | *** |
| mmlu×sycophancy | 0.0099 | *** |
| mmlu×score_manipulation | 0.0032 | *** |
| mmlu×verbosity_bias | 0.0164 | *** |
| mmlu×position_bias | 0.0032 | *** |
| mmlu×authority_bias | 0.0032 | *** |
| arc×prompt_injection | 0.0496 | *** |
| arc×sycophancy | 0.5843 | |
| arc×score_manipulation | 0.0012 | *** |
| arc×verbosity_bias | 0.0159 | *** |
| arc×position_bias | 0.0032 | *** |
| arc×authority_bias | 0.9903 | |

### bayesian keff_fdr_p（0/12 sig）

| Condition | keff_fdr_p | Sig |
|-----------|------------|-----|
| mmlu×prompt_injection | 0.7278 | |
| mmlu×sycophancy | 0.1839 | |
| mmlu×score_manipulation | 0.7712 | |
| mmlu×verbosity_bias | 0.6525 | |
| mmlu×position_bias | 0.1820 | |
| mmlu×authority_bias | 0.7986 | |
| arc×prompt_injection | 0.5338 | |
| arc×sycophancy | 0.5952 | |
| arc×score_manipulation | 0.1820 | |
| arc×verbosity_bias | 0.5338 | |
| arc×position_bias | 0.1820 | |
| arc×authority_bias | 0.3583 | |

---

## 文件 B（重跑版，May 24）—— K_eff = **7/7/7/7**（uniform）

| Method | K_eff sig | η_max sig |
|--------|-----------|-----------|
| majority_vote | **7/12** | 2/12 |
| weighted_vote | **7/12** | 2/12 |
| threshold_supermajority | **7/12** | 3/12 |
| bayesian | **7/12** | 2/12 |

### majority_vote keff_fdr_p（7/12 sig）

| Condition | keff_fdr_p | Sig |
|-----------|------------|-----|
| mmlu×prompt_injection | 0.0108 | *** |
| mmlu×sycophancy | 0.0108 | *** |
| mmlu×score_manipulation | 0.0134 | *** |
| mmlu×verbosity_bias | 0.0148 | *** |
| mmlu×position_bias | 0.1527 | |
| mmlu×authority_bias | 0.0108 | *** |
| arc×prompt_injection | 0.0944 | |
| arc×sycophancy | 0.6132 | |
| arc×score_manipulation | 0.0108 | *** |
| arc×verbosity_bias | 0.0262 | *** |
| arc×position_bias | 0.9790 | |
| arc×authority_bias | 0.1799 | |

### weighted_vote keff_fdr_p（7/12 sig）

| Condition | keff_fdr_p | Sig |
|-----------|------------|-----|
| mmlu×prompt_injection | 0.0090 | *** |
| mmlu×sycophancy | 0.0090 | *** |
| mmlu×score_manipulation | 0.0152 | *** |
| mmlu×verbosity_bias | 0.0152 | *** |
| mmlu×position_bias | 0.0657 | |
| mmlu×authority_bias | 0.0090 | *** |
| arc×prompt_injection | 0.0657 | |
| arc×sycophancy | 0.6127 | |
| arc×score_manipulation | 0.0090 | *** |
| arc×verbosity_bias | 0.0369 | *** |
| arc×position_bias | 0.9786 | |
| arc×authority_bias | 0.1486 | |

### threshold_supermajority keff_fdr_p（7/12 sig）

| Condition | keff_fdr_p | Sig |
|-----------|------------|-----|
| mmlu×prompt_injection | 0.0064 | *** |
| mmlu×sycophancy | 0.0072 | *** |
| mmlu×score_manipulation | 0.0072 | *** |
| mmlu×verbosity_bias | 0.0122 | *** |
| mmlu×position_bias | 0.1555 | |
| mmlu×authority_bias | 0.0064 | *** |
| arc×prompt_injection | 0.0923 | |
| arc×sycophancy | 0.3294 | |
| arc×score_manipulation | 0.0012 | *** |
| arc×verbosity_bias | 0.0142 | *** |
| arc×position_bias | 0.4249 | |
| arc×authority_bias | 0.4290 | |

### bayesian keff_fdr_p（7/12 sig）

| Condition | keff_fdr_p | Sig |
|-----------|------------|-----|
| mmlu×prompt_injection | 0.0096 | *** |
| mmlu×sycophancy | 0.0076 | *** |
| mmlu×score_manipulation | 0.0076 | *** |
| mmlu×verbosity_bias | 0.0118 | *** |
| mmlu×position_bias | 0.0908 | |
| mmlu×authority_bias | 0.0096 | *** |
| arc×prompt_injection | 0.2907 | |
| arc×sycophancy | 0.0783 | |
| arc×score_manipulation | 0.0076 | *** |
| arc×verbosity_bias | 0.0362 | *** |
| arc×position_bias | 0.5692 | |
| arc×authority_bias | 0.0832 | |

---

## 差异分析

**两个文件完全不同**，是两次独立运行的结果：

1. **原始文件（A/C, May 23）= differentiated**：K_eff = 7/9/10/0，Reviewer 报告的版本
2. **重跑文件（B, May 24 14:13）= uniform**：K_eff = 7/7/7/7，Worker 报告的版本

关键差异：
- **Bayesian 翻转最剧烈**：原始 0/12 → 重跑 7/12（所有 p 值从 >0.18 降到 <0.05 区间）
- **Threshold 从 10/12 降到 7/12**：原始有 arc×prompt_injection (0.0496) 刚好显著，重跑变为 0.0923 不显著
- **Validation 项符号反转**：原始 `arc_sycophancy_majority_keff_std_beta = -0.157`（negative=true），重跑 `= +0.065`（negative=false）
- **重跑的显著条件高度一致**：4 种方法几乎在相同的 7 个条件上显著（6 个 mmlu 条件中的 5 个 + arc×score_manipulation + arc×verbosity_bias），暗示底层数据处理可能发生了变化

**结论**：`results/plan001/k5_aggregation_bootstrap.json` 在 May 24 被重新生成覆盖了，使用的代码或数据与原始版本不同。原始 differentiated 结果（7/9/10/0）保存在 `_project/data/` 和 `server_backup/` 中。

---
