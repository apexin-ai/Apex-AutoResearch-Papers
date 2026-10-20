# research paper data audit

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_data_audit_20260523T191953_result.json`
- **Structured JSON:** [`56510b3416c55d5f9c3c.json`](../../sessions/56/56510b3416c55d5f9c3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是逐项核对结果。

---

## 数值一致性审计报告

### ✅ 一致 (35 项)

| # | 数值 | 论文位置 | 源 | 状态 |
|---|------|---------|-----|------|
| 1 | τ = 0.857 (G-MFRM) | abstract:2, intro:4/16, exp:37/44/52, concl:4, app:211/257/295 | exp-003b `joint_gmfrm.kendall_tau` | ✅ |
| 2 | τ = 0.786 (baseline) | abstract:2, intro:4/16, exp:29-36/40/44 | exp-003b `raw_average.kendall_tau` | ✅ |
| 3 | Δτ = +0.071 (7.1pp) | exp:40/44/50, app:295 | 0.857 - 0.786 = 0.071 | ✅ |
| 4 | ΔELPD = -55.7 | abstract:2, exp:48 | pointwise audit: 55.6924→55.7 | ✅ |
| 5 | \|Δ/dSE\| = 5.9 | abstract:2, exp:48 | pointwise audit: 5.9282→5.9 | ✅ |
| 6 | SE = 9.4 (LOO) | exp:48 | audit: dSE=9.3945→9.4 | ✅ |
| 7 | r = 0.86 (OVB) | intro:8, bg:26/36/41 | fig2生成脚本: r=0.8572→0.86 | ✅ |
| 8 | 92/176 items elevated residuals | limitations:1 | exp-008: 87 underfit + 5 overfit = 92 | ✅ |
| 9 | SBC coverage 71% | exp:52, lim:1, app:190/403 | exp-009 `part_b_cn_recovery.coverage_95`=0.71 | ✅ |
| 10 | Δτ p < 0.002 (N=8) | app:361, exp:50 | exp-015 `tau_wilcoxon_p`=0.002 | ✅ |
| 11 | Δτ p = 1.81e-4 (N=20) | app:380 | exp-018 `tau_wilcoxon_p`=0.000181 | ✅ |
| 12 | ESS_bulk ≥ 217 (model-level) | exp:52 | ess_tail_report.json: c `ess_bulk_min`=217 | ✅ |
| 13 | ESS_bulk ≥ 174 (overall) | exp:52 | exp-003b `convergence.ess_min`=174 | ✅ |
| 14 | ESS_tail ≥ 381 | exp:52 | ess_tail_report.json: b `ess_tail_min`=381 | ✅ |
| 15 | ESS_tail ≥ 437 (model-level) | exp:52 | ess_tail_report.json: c `ess_tail_min`=437 | ✅ |
| 16 | R-hat ≤ 1.03 | exp:52 | exp-003b `r_hat_max`=1.03; ess_tail max=1.0326 | ✅ |
| 17 | σ ≤ 0.2: θ 退化 5.9% | method:101, exp:76 | exp-012 `sigma_0.2.delta_theta_pct`=5.9 | ✅ |
| 18 | gpt-3.5 c_n = 5.60 [4.40, 6.80] | exp:52, app:322 | exp-003b `c_n_95ci` | ✅ |
| 19 | gpt-4o c_n = 0.88 [0.05, 2.20] | exp:52, app:315 | exp-003b `c_n_95ci` (CI 0.052→0.05 rounded) | ✅ |
| 20 | Claude Opus d_j = +0.60 [+0.43, +0.76] | exp:52, app:226 | exp-003b `d_j_95ci` | ✅ |
| 21 | Mistral d_j = -0.74 [-1.10, -0.37] | exp:52, app:234 | exp-003b `d_j_95ci` | ✅ |
| 22 | σ_c = 2.40 | exp:52 | exp-003b `sigma_c.mean`=2.4 | ✅ |
| 23 | c̄ = 2.50 | exp:52 | mean(5.6+4.2+3.0+2.5+1.7+1.2+0.93+0.88)/8=2.50 | ✅ |
| 24 | 51.2% RMSE reduction (N=50 ablation) | abstract:2, intro:4/15 | 1−0.124/0.254=51.2% (ablation: 0.2539→0.254, 0.1243→0.124) | ✅ |
| 25 | τ = 0.922 vs 0.839 (synthetic) | intro:15, app:141/144 | exp-w7-ablation: 0.9224→0.922, 0.8393→0.839 | ✅ |
| 26 | 0 divergent transitions | exp:52 | exp-003b `divergent_transitions`=0 | ✅ |
| 27 | Infit/outfit [0.63, 1.07] | exp:52 | exp-008 `model_facet.range`=[0.63,1.07] | ✅ |
| 28 | Pareto k̂ < 0.7 | exp:48 | worker log: "Pareto-k > 0.7: 0/5661 (0.0%)" | ✅ |
| 29 | Severity range 1.34 logits | app:237 | 0.60−(−0.74)=1.34 | ✅ |
| 30 | Judge count τ: .771→.800→.821→.857 | app:251-258 | exp-006 registry 完全匹配 | ✅ |
| 31 | Weight robustness ρ ≥ 0.998 | method:38, exp:11, app:281-287 | exp-013: min(0.998,1.0,0.999,0.998)=0.998 | ✅ |
| 32 | Bias absorption Δθ (all 8 models) | app:343-351 | exp-019 `delta_theta_table` 完全匹配 | ✅ |
| 33 | Spearman ρ = 1.0 (Δθ vs c_n) | app:333 | exp-019 `spearman_rho_delta_theta_cn`=1 | ✅ |
| 34 | Error propagation table (4 sigma levels) | exp:66-70, method:101 | exp-012 registry 所有均值完全匹配 | ✅ |
| 35 | Abstract ≤ 200 words | abstract.tex | 实测 ~191 words | ✅ |

### ⚠️ 轻微不一致 (2 项)

| # | 问题 | 论文值 | 正确值 | 位置 |
|---|------|--------|--------|------|
| 1 | N=8 合成 θ RMSE 改善百分比 | **-50.1%** | **-50.3%** (精确) 或 **-50.0%** (从四舍五入值) | appendix.tex:370 |
| 2 | N=20 合成 θ RMSE 改善百分比 | **-45.0%** | **-45.2%** (精确，registry exp-018) | appendix.tex:389 |

**说明**: 两处都是四舍五入路径差异。Paper 用四舍五入后的均值算百分比，得到的值与从精确值计算的百分比不完全一致。建议统一用 registry 精确值：-50.3% 和 -45.2%。

### 📝 占位符未填 (4 项)

| # | 内容 | 位置 | 应填值 |
|---|------|------|--------|
| 1 | "XX,XXX observations" | experiments.tex:7 | **5,661** (exp-003b `n_observations`) |
| 2 | "XX.X% fill rate" | experiments.tex:7 | **44.7%** (5661/(8×176×9)=44.67%) |
| 3 | "XX.X% fill rate (XX,XXX of XX,XXX potential cells)" | limitations.tex:1 | **44.7% (5,661 of 12,672)** |
| 4 | "τ = TBD" (self-eval) | experiments.tex:9 | **0.857** (appendix 确认 self-eval 排除后 τ 不变) |
| 5 | 17-model 列全部 TBD | experiments.tex:29-37 | 需 17-model 实验结果 |

### ❌ 无法追溯到 registry/artifact (7 项)

| # | 数值 | 论文位置 | 说明 |
|---|------|---------|------|
| 1 | N ≈ 17 for 80% power | exp:50, app:299 | Appendix 描述了 permutation 方法论，但无 registry 实验条目。多个 review report 引用此值。来源可能是独立 power analysis 脚本 |
| 2 | P(Δτ ≥ 0) = 0.927 | exp:44 | bootstrap 后验分析产出，无 registry 条目 |
| 3 | P(θ_mini > θ_qwen) = 0.853 | exp:44 | 后验概率计算，无 registry 条目 |
| 4 | PPC: predicted 0.593 vs observed 0.599 | app:161 | 后验预测检验结果，无 registry 条目 |
| 5 | Self-eval win rates (Qwen 1.000/42, LLaMA 0.912) | app:209 | 分析脚本产出，无 registry 条目 |
| 6 | θ CI coverage 90.1% (N=8), c_n 67.9% (N=8) | app:403 | SBC 分析产出，无 registry 条目 |
| 7 | Horseshoe vs HalfNormal r > 0.999 | exp:52 | 需从 exp-003 和 exp-003b 后验对比计算，无预计算值 |

**这些值不一定有误**，只是无法从 registry 直接验证。它们来自分析脚本或后验计算，理论上可通过重新运行对应脚本验证。

### 内部一致性检查

论文内部同一数值在不同章节的引用均一致：
- τ = 0.857 在 abstract/intro/experiments/conclusion/appendix 中 7 处引用，全部一致
- τ = 0.786 在 6 处引用，全部一致
- 71% coverage 在 4 处引用，全部一致
- r = 0.86 在 4 处引用，全部一致
- ΔELPD = -55.7 在 2 处引用，一致
- 51.2% 在 3 处引用，一致

---

## 汇总

| 类别 | 数量 |
|------|------|
| ✅ 一致 | 35 |
| ⚠️ 轻微四舍五入不一致 | 2 |
| 📝 占位符未填 | 5 |
| ❌ 无法追溯 | 7 |

**需立即修复**:
1. 填写 4 个占位符（observations、fill rate、self-eval τ）
2. 修正 appendix 两处百分比（-50.1%→-50.3%，-45.0%→-45.2%），或统一用 registry 精确值

**无数值错误发现**：所有可追溯的数值与 registry/artifact 源数据一致。

---
