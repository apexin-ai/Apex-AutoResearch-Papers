# audit c2 c4 c5 batch

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_c2-c4-c5-batch_20260523T105604_result.json`
- **Structured JSON:** [`d396c5ad1bd081afc8f2.json`](../../sessions/d3/d396c5ad1bd081afc8f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全，汇总审计结果。

---

## [C2] Attacked K_eff Spearman ρ 完整表格

| Attack | MMLU ρ | ARC ρ |
|--------|--------|-------|
| prompt_injection | 0.6283 | 0.6003 |
| sycophancy | 0.9142 | 0.9235 |
| score_manipulation | 0.9775 | **0.9860** |
| verbosity_bias | 0.9146 | 0.9200 |
| position_bias | **0.6038** | **0.0773** |
| authority_bias | 0.9493 | 0.9713 |

**与论文错误值对比：**

| 条件 | 论文写的 | JSON 实际值 | 偏差 |
|------|----------|-------------|------|
| position_bias MMLU | 0.42 | **0.6038** | 论文偏低 0.18 |
| position_bias ARC | 0.65 | **0.0773** | 论文偏高 0.57（严重错误，方向性差异） |
| score_manipulation ARC | 0.93 | **0.9860** | 论文偏低 0.06 |

**确认：** position_bias ARC 的 ρ = 0.0773，四舍五入即 0.08，与 analysis.tex 中 "ρ=0.08 on ARC" 的说法一致。但论文正文/表格中写 0.65 是严重错误——实际值表明 position_bias 在 ARC 上几乎完全破坏了 K_eff 排序（p=0.0997，甚至不显著）。

---

## [C4] Random Subsample 峰值位置

**Clustered SE K_eff dominance rate by n_local：**

| n_local | n_trials | cl_keff_dominant_rate | ols_keff_dominant_rate |
|---------|----------|-----------------------|------------------------|
| 1 | 8 | 0.000 | 0.500 |
| 2 | 117 | 0.325 | 0.581 |
| **3** | **334** | **0.602** | 0.737 |
| 4 | 363 | 0.587 | **0.752** |
| 5 | 169 | 0.367 | 0.669 |
| 6 | 9 | 0.000 | 0.333 |

**结论：**
- Clustered SE 标准下：**n_local=3 是最高峰**（dom_rate=0.602），n_local=4 紧随其后（0.587），n_local=5 大幅下降（0.367）
- OLS 标准下：n_local=4 是最高峰（0.752），n_local=3 次之（0.737）
- **论文写 "n_local=4-5" 不准确。** 若用 clustered SE，峰值在 n_local=3；若用 OLS，峰值在 n_local=3-4。n_local=5 在两种标准下都明显低于峰值，不应包含在峰值范围内。

---

## [C5] Table 1 η_max 显著性

**mmlu × score_manipulation 条件：**
- η_max OLS p = **0.3142**（不显著）
- η_max Bonferroni p = **1.0**（不显著）
- η_max FDR p = **0.3428**（不显著）

**全部 12 个条件的 η_max 显著性（FDR < 0.05）：**

| 条件 | OLS p | FDR p | 显著？ |
|------|-------|-------|--------|
| mmlu × prompt_injection | 1.53e-07 | 4.60e-07 | **Yes** |
| mmlu × sycophancy | 8.96e-12 | 3.58e-11 | **Yes** |
| mmlu × score_manipulation | 0.314 | 0.343 | **No** |
| mmlu × verbosity_bias | 3.98e-24 | 4.78e-23 | **Yes** |
| mmlu × position_bias | 7.62e-06 | 1.31e-05 | **Yes** |
| mmlu × authority_bias | 3.35e-03 | 4.46e-03 | **Yes** |
| arc × prompt_injection | 3.33e-04 | 5.00e-04 | **Yes** |
| arc × sycophancy | 2.65e-15 | 1.59e-14 | **Yes** |
| arc × score_manipulation | 0.212 | 0.255 | **No** |
| arc × verbosity_bias | 3.49e-06 | 6.97e-06 | **Yes** |
| arc × position_bias | 0.445 | 0.445 | **No** |
| arc × authority_bias | 3.14e-07 | 7.53e-07 | **Yes** |

**结论：** η_max 在 **9/12** 条件下显著（FDR < 0.05），**不是** 11/12 也不是 10/12。三个不显著条件为：
1. mmlu × score_manipulation（p=0.314）
2. arc × score_manipulation（p=0.212）
3. arc × position_bias（p=0.445）

如果论文 Table 1 声称 η_max 在 11/12 条件显著，需修正为 9/12。score_manipulation 在**两个**数据集上 η_max 都不显著（这也符合直觉——score_manipulation 的 ASR 几乎完全由 K_eff 驱动，η_max 贡献极小）。

---
