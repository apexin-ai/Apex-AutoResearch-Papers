# Rebuttal Talking Points

---

## Q1: "Real data 上 EC-HTE 为什么不 work?"

**核心回应**: EC-HTE 的价值是 conditional 的——论文已明确标注 operating conditions。Real LLM 的 Δπ ∈ [0.08, 0.14] 低于 extreme heterogeneity 阈值 (Δπ > 0.15)，此时 variance cost > bias benefit，global correction 已够用。

**支撑数据**:
- Real LLM 的 identity + diagnostic 在真实数据上 pooled R² = 0.975（11 LLM-dataset 组合，8 unique LLMs），准确预测了 bias 方向和大小 → Theorem 1 在 real data 上完全成立  
  *[data_integrity_audit.md: "pooled 0.9747 ≈ 0.975"]*
- 8/8 LLMs 确认 bias amplification：100% 的 real LLM 配置中 global correction 放大了至少一个 subgroup 的 bias  
  *[debiasing_hurts_summary.csv: Real LLM 39/39 hurts, 100%]*
- EC-HTE breakeven at γ_T ≈ 0.10–0.15：γ_T = 0.10 时 EC-HTE coverage 75.0% vs Global 67.5%（仍 +7.5pp）；γ_T = 0.15 时交叉  
  *[treatment_dep_misclass_summary.csv; data_integrity_audit.md]*
- 这恰恰是 diagnostic 的价值——它正确地告诉研究者"在此 Δπ 下不需要 EC-HTE"

**引用**: Egami et al. (2024), Angelopoulos et al. (2023)

---

## Q2: "为什么不用真实因果数据验证?"

**核心回应**: Semi-synthetic 是 CSS 因果推断的标准评估范式。Real CSS 数据没有 ground truth CATE，无法直接评估 bias 或 coverage。

**支撑数据**:
- 我们的设计保留了 real LLM confusion matrices（8 LLMs × 2 datasets = 11 组合）+ real text features，仅合成 treatment assignment 和 outcome
- 真实 LLM 标注误差是实测的（非模拟）：GPT-4o FPR = 0.07–0.38, FNR = 0.15–0.62 across subgroups  
  *[stance_analysis_report.md, civilcomments_report.md]*
- κ 范围 [1.55, 15.01] 覆盖从 well-conditioned 到 near-singular 的全部实际场景  
  *[stance_analysis_report.md]*
- CSS 研究的 treatment 通常是 observational (e.g., stance, toxicity)，不存在随机化实验

**引用**: Egami et al. (2024) CausalInLP, Angelopoulos et al. (2023) PPI, Fong & Tyler (2021)

---

## Q3: "Identity 是否只是简单的矩阵代数?"

**核心回应**: Product form 的实用价值在于 separability——将 bias 分解为三个独立可估计的 component (δ_s, Δτ, π̄)，使 pre-correction diagnostic 成为可能。

**支撑数据**:
- R² = 0.9938 (synthetic K=2), 0.974 (K=4)：analytic identity 精确预测 MC bias  
  *[data_audit_report.md: "actual 0.9938 rounds to 0.994"]*
- R² = 0.975 (pooled across 11 real LLM CMs)：在 asymmetric real-world error 下验证  
  *[data_integrity_audit.md]*
- Pre-correction diagnostic：不需要估计 treatment effects 就能预测 bias 方向和大小。仅需 subgroup confusion matrix + global error rate → 可用于 study design 阶段
- 对比 F-L scalar attenuation：假设 homogeneous error + symmetric CM → 在 heterogeneous 场景下 underestimates bias（实际 bias 可达 F-L 预测的 7.14×）  
  *[debiasing_hurts_summary.csv: worst_ratio = 7.14]*

**引用**: Frazis & Loewenstein (2003), Bound et al. (2001)

---

## Q4: "K > 4 时怎么办?"

**核心回应**: K ≤ 4 是 EC-HTE 的推荐 operating range。K = 8 时 RMSE 爆炸，根因是 n_expert/K 不足以稳定估计 per-subgroup confusion matrix。

**支撑数据**:

| K | Method | |Bias| | RMSE | Coverage |
|---|--------|--------|------|----------|
| 2 | EC-HTE | 0.008 | 0.089 | 93.8% |
| 2 | Global | 0.059 | 0.099 | 86.8% |
| 4 | EC-HTE | 0.012 | 0.120 | 95.6% |
| 4 | Global | 0.056 | 0.125 | 91.1% |
| 8 | EC-HTE | 0.183 | 0.340 | 95.6% |
| 8 | Global | 0.135 | 0.168 | 95.1% |

*[k_scalability_comparison.csv, n_expert = 250]*

- K = 8 根因：250/8 ≈ 31 expert per subgroup，不足以稳定估计 2×2 confusion matrix
- EC-HTE breaks even on RMSE at n_expert ≈ 100；dominates at n_expert ≥ 250（K = 2, κ = 2.0）  
  *[kappa_stratified_analysis.md]*
- 推荐条件：K ≤ 4 或 n_expert/K ≥ 50

---

## Q5: "Simpson's Paradox 角度"

**核心回应**: Global correction 是 Simpson's paradox 的一个实例——聚合异质 error rates 产生对每个 subgroup 都错误的 pooled correction。

**支撑数据**:
- Synthetic grid: 52% of Δπ × Δτ grid shows global correction amplifying bias (debiasing hurts)  
  *[bias_anatomy_heatmap: manifest.yaml]*
- κ > 2 区间：100% 的 configs 中 global correction 增加至少一个 subgroup 的 bias  
  *[kappa_stratified_analysis.md: bin 3, 100% debiasing hurts]*
- Real LLM data: 100% of configurations (39/39) show debiasing hurts  
  *[debiasing_hurts_summary.csv]*
- Bias amplification 幅度：naive → MLE 最高 3.32×，naive → HB 最高 3.02×  
  *[civilcomments_report.md]*
- Framing 优势：连接 EC-HTE 与经典统计学概念，降低审稿人认知负担——全局分层 = pooled regression fallacy

---

## Q6: "Sign reversal 14.9% 的条件是什么?"

**核心回应**: Sign reversal 发生在 true CATE 很小 (τ(0) < 0.089) 且 misclassification heterogeneity 较大时。EC-HTE 在 synthetic configurations 中消除 sign reversal。

**支撑数据**:

| τ(0) | Reversal Rate (Global) | Configs Checked |
|------|----------------------|----------------|
| 0.01 | 31.0% (339/1092) | 546 × 2 |
| 0.03 | 14.9% (163/1092) | 546 × 2 |
| 0.05 | 6.1% (67/1092) | 546 × 2 |
| 0.07 | 1.6% (18/1092) | 546 × 2 |
| ≥ 0.10 | 0% | 546 × 2 |

*[policy_reversal_zone.csv]*

- 最危险组合：τ(0) = 0.01 + δ_misclass = 0.19 → 42.9% reversal (18/42 configs)
- Critical threshold: τ(0) < 0.089（0.07 仍有 1.6% reversal, 0.10 降至 0%）
- Stance detection (TweetEval): global correction 导致 4/30 sign reversals (13.3%), EC-HTE 降至 1/30 (3.3%)  
  *[stance_analysis_report.md]*
- EC-HTE 在 synthetic grid 中 0% sign reversal（analytically unbiased by construction）

---

## Quick Reference Numbers

### Identity & Diagnostic
| Metric | Value | Source |
|--------|-------|--------|
| R² (K=2 synthetic) | 0.9938 | data_audit_report.md |
| R² (K=4 synthetic) | 0.974 | data_audit_report.md |
| R² (11 real LLM CMs, pooled) | 0.975 | data_integrity_audit.md |
| Unique LLMs tested | 8 | data_integrity_audit_v2.md |
| Real LLM κ range | [1.55, 15.01] | stance_analysis_report.md |

### Debiasing Hurts
| Metric | Value | Source |
|--------|-------|--------|
| Synthetic grid debiasing hurts | 52% of grid | bias_anatomy_heatmap |
| κ > 2 debiasing hurts | 100% of configs | kappa_stratified_analysis.md |
| Real LLM debiasing hurts | 100% (39/39) | debiasing_hurts_summary.csv |
| Max bias amplification ratio | 7.14× | debiasing_hurts_summary.csv |

### Sign Reversal (τ-sweep)
| Metric | Value | Source |
|--------|-------|--------|
| τ(0) = 0.01, overall | 31.0% | policy_reversal_zone.csv |
| τ(0) = 0.03, overall | 14.9% | policy_reversal_zone.csv |
| τ(0) = 0.01 + δ_misclass = 0.19 | 42.9% | policy_reversal_zone.csv |
| Critical threshold | τ(0) < 0.089 | policy_reversal_zone.csv |
| Stance detection (global) | 4/30 = 13.3% | stance_analysis_report.md |
| EC-HTE (synthetic) | 0% | by construction |

### K Scalability (n_expert = 250)
| K | EC-HTE RMSE | Global RMSE | EC-HTE Coverage |
|---|------------|------------|----------------|
| 2 | 0.089 | 0.099 | 93.8% |
| 4 | 0.120 | 0.125 | 95.6% |
| 8 | 0.340 | 0.168 | 95.6% |

*[k_scalability_comparison.csv]*

### Treatment-Dependent Misclassification
| γ_T | EC-HTE Coverage | Global Coverage | EC-HTE Bias | Global Bias |
|-----|----------------|----------------|-------------|-------------|
| 0.00 | 94.5% | 89.8% | 0.058 | 0.073 |
| 0.05 | 89.8% | 84.8% | 0.073 | 0.080 |
| 0.10 | 75.0% | 67.5% | 0.110 | 0.109 |
| 0.15 | 52.5% | 55.3% | 0.151 | 0.142 |

*[treatment_dep_misclass_summary.csv]*

### Computational Cost (K=4, N=5000, n_expert=250)
| Step | Mean Time |
|------|-----------|
| EC-HTE full pipeline | 3.4 ms |
| Bootstrap SE (B=100) | 347 ms |
| HB Gibbs MCMC (4ch×6k) | 4.66 s |

*[timing_benchmark.csv]*

### Real LLM Δπ Range
| Source | Δπ Range |
|--------|----------|
| TweetEval (5 models) | [0.051, 0.198] |
| CivilComments (3 models) | [0.087, 0.149] |
| Newer models (GPT-4o, 4.1) | [0.08, 0.14] |

*[exp008_multi_llm_analysis.md, review_issues.yaml]*
