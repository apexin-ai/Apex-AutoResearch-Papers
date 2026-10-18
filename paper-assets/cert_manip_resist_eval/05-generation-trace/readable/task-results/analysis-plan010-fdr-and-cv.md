# analysis plan010 fdr and cv

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan010-fdr-and-cv_20260522T121717_result.json`
- **Structured JSON:** [`d835f6cae1e622a3312e.json`](../../sessions/d8/d835f6cae1e622a3312e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果总结：

**FDR 校正 (48 tests 统一)**

| Method | η_max raw | η_max FDR-48 | η_max Bonf | K_eff neg raw | K_eff neg FDR | K_eff neg Bonf |
|--------|-----------|--------------|------------|---------------|---------------|----------------|
| majority_vote | 8/12 | 5/12 | 1/12 | 1/12 | 1/12 | 0/12 |
| weighted_vote | 7/12 | 6/12 | 1/12 | 1/12 | 1/12 | 0/12 |
| threshold_vote | 7/12 | 6/12 | 5/12 | 0/12 | 0/12 | 0/12 |
| bayesian | 3/12 | 2/12 | 1/12 | 0/12 | 0/12 | 0/12 |

与 plan_009 的区别：plan_009 FDR 是 12 个 test 内部做的（majority only），本次是 48 个 test 统一 FDR，更保守。majority_vote 从 plan_009 的 6/12 (FDR-12) 到这里的 5/12 (FDR-48)，差异不大。

**Bayesian 5-fold CV**

| Variant | η_max sig raw | η_max sig FDR-12 |
|---------|---------------|------------------|
| Original (300-sample weights) | 3/12 | 2/12 |
| 5-fold CV weights | 3/12 | 1/12 |

结论：**robust** — CV 版本与原始版本显著性几乎一致，无信息泄漏伪影。3 个 raw significant condition 完全相同（mmlu__sycophancy, mmlu__verbosity_bias, arc_challenge__sycophancy），p-values 变化极小。

输出已保存到 `/root/cert_manip_resist_eval/artifacts/results/results_plan010_fdr_cv.json`。

---
