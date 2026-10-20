# analysis qw rand permutation s015 s025

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qw_rand_permutation_s015_s025_20260514T084256_result.json`
- **Structured JSON:** [`7bc45d02cea4ca3f9861.json`](../../sessions/7b/7bc45d02cea4ca3f9861.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

## Qwen Random Masking 统计检验结果

| Experiment | Sparsity | Med.Diff | Perm. p | Cohen's d | Bootstrap 95% CI | Wilcoxon p | Verdict |
|---|---|---|---|---|---|---|---|
| bf16_qw_rand_s015 | 0.15 | -0.029 | **0.766** | -0.051 (negligible) | [-0.211, 0.212] ∋ 0 | 0.863 | **FAIL** |
| bf16_qw_rand_s020 | 0.20 | 0.058 | **0.352** | 0.247 (small) | [-0.139, 0.215] ∋ 0 | 0.149 | **FAIL** |
| bf16_qw_rand_s025 | 0.25 | 1.144 | **0.168** | 0.157 (negligible) | [-0.317, 4.165] ∋ 0 | 0.010 | **FAIL** |

三个 sparsity level 全部 FAIL，与预期一致。s025 的 Wilcoxon p=0.01 名义上显著，但 permutation test (p=0.17) 和 bootstrap CI 包含零否决了它——这是 Wilcoxon 对 outlier 敏感的已知行为（s025 的 II 绝对值更大、方差更大）。

已更新 registry metrics 字段（permutation_test, cohens_d, bootstrap_ci_95, wilcoxon_p, phase_median_ii）并注册 artifact。分析结果保存在服务器 `/root/autodl-tmp/pacs/analysis_output/bf16_qw_rand_s0{15,25}/analysis_results.json`。

---
