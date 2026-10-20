# analysis rebootstrap qw rand s030

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rebootstrap_qw_rand_s030_20260514T090030_result.json`
- **Structured JSON:** [`382659971764b92de408.json`](../../sessions/38/382659971764b92de408.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 完整报告

### (a) Raw Data 可用性：✅ 可用

所有 8 个实验（4 sparsity × 2 method）均含 `per_problem_ii` 字段，提供每个 problem 的 `ii_high`/`ii_mid`/`ii_low` 值。50 problems/实验，结构完全一致。

### (b) ⚠️ B=10000 Re-bootstrap Verdict: **PASS → FAIL**

| 指标 | B=1000 (原始) | B=10000 (per-problem bootstrap) |
|------|--------------|-------------------------------|
| median_high | 3.955 | 4.201 |
| median_high CI | [3.516, 5.605] | [2.576, 7.959] |
| median_low | 8.196 | 8.066 |
| median_low CI | [5.766, 10.922] | [4.136, 17.571] |
| gradient | 4.241 | 3.865 |
| gradient 95% CI | — | **[-1.538, 13.707]** |
| p-value | — | **0.1113** |
| CI overlap | No → PASS | **Yes → FAIL** |

Per-problem bootstrap 的 CI 更宽，median_high_ci 上界 (7.959) > median_low_ci 下界 (4.136)，overlap = 3.823。gradient CI 包含 0。**Reviewer 的怀疑得到确认：n=1000 的 PASS 是假阳性。**

Random vs Importance gradient CI 也重叠，无法区分两种 masking 方法在 s=0.30。

### (c) Cohen's d 表格（全 4 水平，importance vs random）

| Sparsity | Imp Grad Med | Rand Grad Med | Cohen's d | 95% CI |
|----------|-------------|--------------|-----------|--------|
| 0.15 | 0.0493 | 0.0013 | 0.125 | [-0.349, 0.429] |
| 0.20 | 0.1575 | 0.0108 | -0.164 | [-0.594, 0.237] |
| 0.25 | 1.0637 | 1.0649 | -0.221 | [-0.475, 0.269] |
| 0.30 | 2.5016 | 3.8651 | 0.224 | [-0.233, 0.472] |

**所有 4 个水平的 Cohen's d 95% CI 均包含 0。** Effect size 极小 (|d| < 0.25)，importance 和 random masking 在任何 sparsity 水平上都没有统计显著差异。

### (d) profiling_results.json 结构

**Top-level keys**: `config`, `phase_stats`, `perplexity`, `interaction_index`, `pass_fail`, `warnings`, `diagnostics`, `per_problem_ii`

**per_problem_ii 字段**: `problem_idx`, `problem_id`, `ii_high`, `n_segments_high`, `ii_mid`, `n_segments_mid`, `ii_low`, `n_segments_low`

所有 bf16 实验结构完全一致（已验证 imp_s015, imp_s030, rand_s015, rand_s030）。

### (e) ⚠️ Verdict 变更标注

**bf16_qw_rand_s030: PASS → FAIL**。原始 n_bootstrap=1000 的段级 bootstrap 给出窄 CI 导致非重叠假象。Per-problem B=10000 bootstrap 显示 CI 严重重叠，gradient 不显著 (p=0.111)。

脚本和结果已保存到 `/root/autodl-tmp/pacs/results/rebootstrap_analysis/`。

---
