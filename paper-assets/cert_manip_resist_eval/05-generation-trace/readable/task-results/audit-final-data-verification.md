# audit final data verification

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_final-data-verification_20260524T042647_result.json`
- **Structured JSON:** [`8a3b7b1959a4993ab6ba.json`](../../sessions/8a/8a3b7b1959a4993ab6ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No local git repo found. The code lives on the remote server. Let me provide the complete verification report.

---

## 数据自查报告

### 检查范围
- 11 个 .tex 文件，27 个 V2 JSON 数据文件
- 系统性核对了论文中所有数值（约 200+ 个数字点）

### 已修复的问题（3 处 V1 残留）

| # | 文件:行号 | 当前值(V1) | 正确值(V2) | 数据源 |
|---|-----------|-----------|-----------|--------|
| 1 | `appendix.tex:124` tab:robustness_checks "Full bootstrap" K_eff sig | 7/12 | **10/12** | `regime_transition_corrected.json` K5.new.keff_sig=10 |
| 2 | `appendix.tex:128` tab:robustness_checks "Fractional logit" | η=5/12, K=9/12 | **η=4/12, K=11/12** | `fractional_logit_corrected.json` K5 clustered |
| 3 | `appendix.tex:78` tab:aggregation_k5 "Majority" K_eff sig | 7/12 | **10/12** | `regime_transition_corrected.json` K5.new.keff_sig=10 |

注意：#3 的修复也消除了 appendix.tex 中文本(line 69 已写 "10/12")与表格(旧 "7/12")的内部矛盾。

### 已确认的 V1→V2 修复（分析.tex，Paper Agent 已修）
- ρ=0.942 → 0.978 ✓
- |β̄|=0.194 → 0.497 ✓  
- |β̄|=0.164 → 0.430 ✓

### 需要注意但无法自动修复的问题

**1. tab:aggregation_k5 其余行可能也是 V1 数据**
- Weighted (1/12, 9/12, 0.249)、Threshold (6/12, 10/12, 0.506)、Bayesian (1/12, 0/12, 0.081) 均来自 `k5_aggregation_table_data.txt`，该文件与 V1 majority bootstrap 值一致
- R² 值（0.256 等）也可能需要 V2 重算
- **建议**：在服务器上用 V2 代码重跑 K=5 aggregation bootstrap，更新这些数字

**2. Tier 分类不一致**
- methodology.tex Table: frontier=3, mid=3, lightweight=9（gemini-3.5-flash 归 mid-tier）
- stochastic_dominance_analysis.json: frontier=4, mid=6, lightweight=5（gemini-3.5-flash 归 frontier）
- threat_model.tex 引用的 67.7%/31.1% within/cross-tier 统计是基于 JSON 的 4/6/5 分组计算的
- 按论文自己的 caption 标准（">85% on both benchmarks = frontier"），gemini-3.5-flash (MMLU .968, ARC 1.00) 应为 frontier
- **建议**：统一 tier 定义，或在 threat_model 中注明 within/cross-tier 分析使用了不同的 tier 划分

### 验证通过的数字（核心清单）

| 位置 | 数字 | 数据源 | 状态 |
|------|------|--------|------|
| Abstract | 78% (28/36) | Sensitivity table checkmarks | ✓ |
| Abstract | frac logit 9/12, 11/12, 12/12 | fractional_logit_corrected.json K3/K5/K7 clustered | ✓ |
| Abstract | R²: 0.83, 0.09 | aggregation_r2_bootstrap.json | ✓ |
| Intro | 88.9–100% GAM positive rate | gam_bootstrap_ci_k3.json min=0.8895 | ✓ |
| Intro | bootstrap 3/12 η, 4/12 K at K=3 | regime_transition_corrected.json | ✓ |
| Intro | 10/12 K=5, 9/12 K=7, 0/12 η | regime_transition_corrected.json | ✓ |
| Intro | concordance 98.6% (71/72) | fractional_logit_corrected.json | ✓ |
| Threat model | 58% (61/105) dominant pairs | stochastic_dominance_analysis.json | ✓ |
| Threat model | 67.7% within, 31.1% cross | stochastic_dominance_analysis.json | ✓ |
| Tab:dominance | η 10/12, K 12/12, Co:10 K:2 | table1_corrected.json | ✓ |
| Tab:aggregation | threshold-bayesian gradient | table2_corrected.json | ✓ |
| Tab:method_comparison | all 5 rows | Multiple V2 JSONs | ✓ |
| MDE | 0.144, 0.048, 0.036 | power_analysis_all_K.json | ✓ |
| K_eff dist | 2.18, 3.35, 4.53 | keff_distribution_corrected.json | ✓ |
| Alt diversity | Q/Disagree/κ/K_eff table | alt_diversity_corrected.json | ✓ |
| Kappa regime | 8→7→6, 4→10→9 | kappa_diversity_regime_transition.json | ✓ |
| Sensitivity | RV 1/12→3/12→4/12 | Appendix table checkmarks verified | ✓ |
| Pool A | 2/12 K=3, 10/12 K=5 | sensitivity_analysis_poolA_corrected.json | ✓ |
| Pool A | "two failures are both sycophancy" | sensitivity_analysis_poolA_corrected.json | ✓ |
| Attacked K_eff | ρ values, stable 4/6, 6/8 K=5 | keff_stability_split_corrected.json | ✓ |
| RF contrast | R²=0.73–0.81 (K=3) | random_fault_contrast_corrected.json K3 | ✓ |
| RF contrast | adaptive R²=0.275, gap=0.43 (K=5) | random_fault_contrast_corrected.json | ✓ |
| Epsilon | Δβ=0.10 K=3, 0.073 K=5 | appendix text, consistent | ✓ |
| Limitations | OLS 12/12, bootstrap 4/12, frac 9/12 | Multiple V2 JSONs | ✓ |

### 汇总
- 检查数字点：~200+
- 发现并修复 V1 残留：**3 处**（全在 appendix 表格）
- 需要后续处理的问题：**2 个**（K=5 aggregation 重算；tier 定义统一）
- 无法追溯的数字：Kruskal-Wallis p=0.200 和 p=0.423（多处引用一致，但不在任何 JSON 文件中）

---
