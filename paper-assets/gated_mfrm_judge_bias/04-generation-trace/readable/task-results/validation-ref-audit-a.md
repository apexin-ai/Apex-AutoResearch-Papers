# validation ref audit A

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validation_ref-audit-A_20260526T104707_result.json`
- **Structured JSON:** [`a691870cf4702a4d6702.json`](../../sessions/a6/a691870cf4702a4d6702.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 批次验证完成。以下是汇总结果。

---

```
总条数: 45
全部论文真实存在: ✅（无 hallucinated paper）
严重错误: 1 条
标题/元信息需修正: ~14 条
```

## 严重错误（必须修）

| # | cite_key | 错误 |
|---|----------|------|
| 44 | `ye2024justice` | **❌ Venue 错误**: 实际是 **ICLR 2025**，非 EMNLP 2024 |

## 标题显著改写（建议修正）

| # | cite_key | 问题 |
|---|----------|------|
| 10 | `uto2020generalized` | 标题大幅缩写：实际 "A generalized many-facet Rasch model and its Bayesian estimation using Hamiltonian Monte Carlo"，bib 用了 MFRM/HMC 缩写 |
| 4 | `shu2013dgirt` | 缺副标题 "due to Item Compromise"，且 "IRT" 应为 "Item Response Theory" |

## 标题截断/缺词（视 bib 实际内容决定是否修）

以下条目在 bib 摘要中存在标题不完整，需对照实际 .bib 文件确认：

| # | cite_key | 缺失部分 |
|---|----------|----------|
| 6 | `zhou2025psnirt` | "LLM"→"Large Language Model", "IRT"→"Item Response Theory" |
| 12 | `rodriguez2021irt` | 缺副标题 "How should that change NLP Leaderboards?" |
| 17 | `bavaresco2025judgebench` | 缺副标题 "A Large Scale Empirical Study across 20 NLP Evaluation Tasks" |
| 18 | `cyclicjudge2026` | 缺 "Efficiently in LLM-based Evaluation" |
| 19 | `uda2026` | 缺 "for Pair-wise LLM-as-a-Judge" |
| 20 | `fiedler2026bias_uncertainty` | 缺末尾 "Estimation" |
| 24 | `sainz2023contamination` | 缺副标题 "On the Need to Measure LLM Data Contamination for each Benchmark" |
| 29 | `preference_leakage2026` | 缺冠词 "A" → "A Contamination Problem..." |
| 30 | `li2024arenahard` | 缺 "and BenchBuilder Pipeline" |
| 39 | `vehtari2021rhat` | 缺副标题 "for Assessing Convergence of MCMC" |
| 41 | `truce2024` | 缺 "and Improve Comparative Evaluation of LLMs" |
| 42 | `choi2026irt_judge` | 缺 "the"，"IRT"→"Item Response Theory" |

## 完全通过 ✅ (30 条)

`piironen2017horseshoe`, `linacre1989mfrm`, `linacre1994mfrm`, `jiao2025mfrm_llm`, `rothenberg1971`, `sanmartin2016`, `betancourt2015`, `lalor2019irt`, `vania2021irt`, `wang2024positionbias`, `li2024splitmerge`, `koo2024cobbler`, `golchin2024timetravel`, `oren2024proving`, `deng2024contamination`, `constat2024`, `dcr2025`, `mink2024`, `zheng2023mtbench`, `talts2018sbc`, `angrist2009mostly`, `murphy1985`, `pagan1984`, `wooldridge2010`, `vehtari2017loo`, `gelman2013bda`, `livebench2025`, `polo2024tinybenchmarks`, `panickssery2024selffavor`, `gelman2013bda`

---

**结论**: 无 hallucinated paper。唯一必须立即修复的是 `ye2024justice` 的 venue（EMNLP 2024 → ICLR 2025）。标题截断问题需对照实际 .bib 文件确认——上面列出的是基于摘要信息的比对，实际 bib 中可能已有完整标题。

---
