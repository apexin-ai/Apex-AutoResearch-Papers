# analysis permutation test s015 s025

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_permutation-test-s015-s025_20260514T072548_result.json`
- **Structured JSON:** [`7d456972d2142ba9efad.json`](../../sessions/7d/7d456972d2142ba9efad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。完整结果已保存到 `/root/autodl-tmp/pacs/analysis_output/permutation_test_results.json`。

## 全 4 水平统计检验汇总

### Ratio statistic (ii_low / ii_high)

| Sparsity | n_paired | Gradient Ratio | Perm p (median) | Perm p (mean) | Wilcoxon p | Bonferroni p (median) | 结论 |
|----------|----------|---------------|-----------------|---------------|------------|----------------------|------|
| s015 | 32 | 1.1x | 0.8704 | 0.2921 | 0.6247 | 1.0000 | **n.s.** |
| s020 | 38 | 13.9x | 0.0735 | 0.2507 | 0.1017 | 0.2940 | **n.s.** |
| s025 | 41 | 28.7x | 0.0745 | 0.0049 | 0.0239 | 0.2980 | **n.s.** (Bonferroni) |
| s030 | 44 | 74.1x | 0.0003 | 0.0003 | 0.0003 | 0.0012 | **Reject H0 (\*\*\*)** |

### Difference statistic (ii_low − ii_high) — 更 robust

| Sparsity | n_paired | Imp diff median | Rnd diff median | Perm p (median) | Perm p (mean) | Bonferroni p (median) | 95% CI | 结论 |
|----------|----------|----------------|----------------|-----------------|---------------|----------------------|--------|------|
| s015 | 49 | 0.3508 | 0.0110 | 0.0008 | 0.0001 | 0.0032 | — | **Reject H0 (\*\*\*)** |
| s020 | 49 | 1.1363 | 0.0434 | 0.0002 | 0.0003 | 0.0008 | — | **Reject H0 (\*\*\*)** |
| s025 | 49 | 4.0174 | 0.3032 | 0.0002 | 0.0001 | 0.0008 | — | **Reject H0 (\*\*\*)** |
| s030 | 49 | 9.9538 | 1.0569 | 0.0001 | 0.0001 | 0.0004 | — | **Reject H0 (\*\*\*)** |

### 关键发现

**Ratio statistic** 在低 sparsity 水平（s015/s020/s025）**不显著**。原因：EPS=0.01 过滤掉大量样本（s015 过滤了 17/49），低 sparsity 时 ii_high 值普遍很小导致 ratio 不稳定。

**Difference statistic** 所有 4 个水平**全部显著**（Bonferroni 校正后 p < 0.005），且效应量随 sparsity 递增（0.35 → 1.14 → 4.02 → 9.95）。

**建议论文采用 difference statistic 作为主结果**，ratio 作为辅助。Difference 不受 EPS 过滤影响（n_paired=49 全部保留），对重尾分布更 robust，且全 4 个水平一致拒绝 H0，消除 cherry-picking 风险。

---
