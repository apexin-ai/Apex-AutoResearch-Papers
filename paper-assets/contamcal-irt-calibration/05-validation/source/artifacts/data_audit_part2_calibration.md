# Data Audit Part 2 — Calibration, S1-only, DIF, Domain, Signals

**审计时间**: 2026-05-23
**审计人**: Automated audit agent

---

## A. Table 3 — Calibration Quality (results.tex line 100–117)

**源文件**: `cqa1:/root/autodl-tmp/exp006/unified_baselines_n16/mmlu/baseline_results.json`

| 位置 | 论文数字 | 源文件 | 源文件数字 | 一致？ | 备注 |
|------|---------|--------|-----------|--------|------|
| B0 MAE | 0.006 | baseline_results.json → B0_Raw.mae | 0.0056 | ✅ | 0.0056→0.006 (3dp rounding) |
| B0 τ | 0.767 | baseline_results.json → B0_Raw.tau_gt | 0.7669 | ✅ | 0.7669→0.767 |
| B1b MAE | 0.026 | baseline_results.json → B1b_RemoveRescore.mae | 0.0258 | ✅ | 0.0258→0.026 |
| B1b τ | 0.783 | baseline_results.json → B1b_RemoveRescore.tau_gt | 0.7834 | ✅ | 0.7834→0.783 |
| B3 MAE | 0.008 | baseline_results.json → B3_Vanilla2PL.mae | 0.0080 | ✅ | 精确匹配 |
| B3 τ | 0.731 | baseline_results.json → B3_Vanilla2PL.tau_gt | 0.7313 | ✅ | 0.7313→0.731 |
| B4 MAE | 0.010 | baseline_results.json → B4_LinearReg.mae | 0.0096 | ✅ | 0.0096→0.010 |
| B4 τ | 0.751 | baseline_results.json → B4_LinearReg.tau_gt | 0.7506 | ✅ | 0.7506→0.751 |
| B5b MAE | 0.006 | baseline_results.json → B5b_Emperor.mae | 0.0060 | ✅ | 精确匹配 |
| B5b τ | 0.789 | baseline_results.json → B5b_Emperor.tau_gt | 0.7890 | ✅ | 精确匹配 |
| B6 MAE | 0.108 | baseline_results.json → B6_DCR.mae | 0.1081 | ✅ | 0.1081→0.108 |
| B6 τ | 0.654 | baseline_results.json → B6_DCR.tau_gt | 0.6543 | ✅ | 0.6543→0.654 |
| ContamCal MAE | 0.009 | baseline_results.json → ContamCal.mae | 0.0091 | ✅ | 0.0091→0.009 |
| ContamCal τ | 0.731 | baseline_results.json → ContamCal.tau_gt | 0.7313 | ✅ | 0.7313→0.731 |

**结论**: Table 3 全部 14 个数字与源文件一致。

---

## B. §5.5 / Appendix G — S1-only vs RRF comparison

**源文件 (RRF)**: `cqa1:/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16_fixed/pooled_rrf_irt_results.json` → per_benchmark.mmlu
**源文件 (S1-only)**: `cqa1:/root/autodl-tmp/exp006/s1only_minkpp_ablation/mmlu/s1only_minkpp_results.json`
**论文位置**: appendix.tex line 197–198 (Table 8)

| 位置 | 论文数字 | 源文件 | 源文件数字 | 一致？ | 备注 |
|------|---------|--------|-----------|--------|------|
| RRF γ | 0.698 | pooled_rrf → gamma.mean | 0.6979 | ✅ | 0.6979→0.698 |
| RRF PPP | 0.193 | pooled_rrf → posterior_predictive.overall_ppp | 0.193 | ✅ | 精确匹配 |
| RRF τ | 0.73 | baseline_results.json → ContamCal.tau_gt | 0.7313 | ✅ | 0.7313→0.73 (2dp) |
| RRF MAE | 0.007 | pooled_rrf → posterior_predictive.residual_mae | 0.0072 | ✅ | 0.0072→0.007 |
| RRF ESS | 1708 | pooled_rrf → diagnostics.min_ess | 1707.5 | ✅ | 1707.5→1708 |
| S1-only γ | 1.754 | s1only → gamma.mean | 1.7535 | ✅ | 1.7535→1.754 |
| S1-only PPP | 0.0003 | s1only → ppc.overall_ppp | 0.0003 | ✅ | 精确匹配 |
| S1-only τ | 0.63 | s1only → tau | 0.6281 | ✅ | 0.6281→0.63 (2dp) |
| S1-only MAE | 0.076 | s1only → ppc.residual_mae | 0.0762 | ✅ | 0.0762→0.076 |
| S1-only ESS | 261 | s1only → diagnostics.min_ess | 261.0 | ✅ | 精确匹配 |

**注**: 论文 Table 3 中的 ContamCal MAE=0.009 使用 `baseline_results.json` 的 cal_mae=0.0091（对比 ground truth）；Appendix Table 8 的 RRF MAE=0.007 使用 `pooled_rrf_irt_results.json` 的 residual_mae=0.0072（posterior predictive residual）。两者是不同的 MAE 定义，均与对应源文件一致。

**结论**: Appendix Table 8 全部 10 个数字与源文件一致。

---

## C. DIF Parameterization Comparison (Appendix H)

**源文件**: `cqa1:/root/contamcal-irt-calibration/analysis/dif_comparison/results.json`
**论文位置**: appendix.tex line 239–240 (Table 9)

| 位置 | 论文数字 | 源文件 | 源文件数字 | 一致？ | 备注 |
|------|---------|--------|-----------|--------|------|
| Non-uniform γ mean | 0.245 | results.json → **uniform_dif**.gamma_mean | 0.245223 | ✅⚠️ | 数值匹配；JSON key 名称与论文标签互换 |
| Non-uniform γ SD | 0.197 | results.json → **uniform_dif**.gamma_sd | 0.197019 | ✅⚠️ | 同上 |
| Non-uniform PPP | 0.763 | results.json → **uniform_dif**.ppp | 0.763 | ✅⚠️ | 同上 |
| Non-uniform LOO ELPD | −2124.3 | results.json → **uniform_dif**.loo_elpd | −2124.3089 | ✅⚠️ | 同上 |
| Non-uniform ESS | 1468 | results.json → **uniform_dif**.gamma_ess_bulk | 1467.95 | ✅⚠️ | 同上 |
| Uniform γ mean | −0.458 | results.json → **nonuniform_dif**.gamma_mean | −0.4583 | ✅⚠️ | 数值匹配；JSON key 名称与论文标签互换 |
| Uniform γ SD | 0.453 | results.json → **nonuniform_dif**.gamma_sd | 0.45306 | ✅⚠️ | 同上 |
| Uniform PPP | 0.743 | results.json → **nonuniform_dif**.ppp | 0.74325 | ✅⚠️ | 0.74325→0.743 |
| Uniform LOO ELPD | −2123.4 | results.json → **nonuniform_dif**.loo_elpd | −2123.4382 | ✅⚠️ | 同上 |
| Uniform ESS | 981 | results.json → **nonuniform_dif**.gamma_ess_bulk | 980.963 | ✅⚠️ | 同上 |

**⚠️ JSON key 名称互换**: 源文件中 `uniform_dif` 的数据对应论文的 "Non-uniform (current)"，`nonuniform_dif` 的数据对应论文的 "Uniform (inside a_i)"。所有 10 个数值本身均正确匹配。论文的命名基于 DIF 理论（γ 在 a_i 括号外 = 效应不随 discrimination 缩放 = non-uniform DIF），JSON key 的命名约定相反。这不影响论文正确性，但可能在后续复现时造成混淆。

**结论**: 数值全部一致；建议修复 JSON key 命名以匹配论文。

---

## D. §5.6 Domain-Level Analysis

**源文件**: `cqa1:/root/autodl-tmp/exp006/mmlu_domain_irt_j16_qwen/all_domain_results.json` → Social_Sciences
**论文位置**: results.tex line 98 和 128

| 位置 | 论文数字 | 源文件 | 源文件数字 | 一致？ | 备注 |
|------|---------|--------|-----------|--------|------|
| Social Sciences γ_d | −0.63 | all_domain_results → Social_Sciences.gamma.mean | −0.6274 | ✅ | −0.6274→−0.63 (2dp) |
| 95% CI lower | −1.07 | all_domain_results → Social_Sciences.gamma.q025 | −1.0729 | ✅ | −1.0729→−1.07 |
| 95% CI upper | −0.19 | all_domain_results → Social_Sciences.gamma.q975 | −0.1923 | ✅ | −0.1923→−0.19 |
| P(γ_d<0) | 99.7% | all_domain_results → Social_Sciences.gamma.p_neg | 0.99675 | ✅ | 99.675%→99.7% (1dp rounding) |
| PPP | 0.722 | all_domain_results → Social_Sciences.ppp.overall_ppp | 0.7215 | ✅ | 0.7215→0.722 (3dp rounding) |

**结论**: 全部 5 个数字与源文件一致。

---

## E. §5.5 Signal Failure Modes

**源文件**: `artifacts/dream_reports/dream_20260515T052337/best/experiment_data.json` (signal_survival_analysis)
**论文位置**: results.tex line 123

| 位置 | 论文数字 | 源文件 | 源文件数字 | 一致？ | 备注 |
|------|---------|--------|-----------|--------|------|
| Min-K%++ d=−1.98 at d100 (0.5B) | −1.98 | experiment_data → S2_minkpp_d100_cohens_d_05B | −1.98 | ✅ | 精确匹配 |
| Cohen's d detail (MMLU) | — | experiment_data → signal_survival_analysis table, 0.5B MMLU | −1.22 | ✅ | 仅验证源存在 |
| Cohen's d detail (GSM8K) | — | experiment_data → signal_survival_analysis table, 0.5B GSM8K | −2.67 | ✅ | mean(−1.22,−2.67,−2.05)=−1.98 |
| Cohen's d detail (ARC) | — | experiment_data → signal_survival_analysis table, 0.5B ARC | −2.05 | ✅ | |
| S1 AUC > 0.95 at all scales | >0.95 | experiment_data → S1_embedding_d005_auc_{05B,15B,3B} | 0.975, 0.98, 0.99 | ✅ | 全部 >0.95 |
| S1 MMLU 0.5B AUC | >0.95 | experiment_data → Signal AUC table, S1 MMLU 0.5B | 0.953 | ✅ | 0.953 > 0.95 |
| \|d\| > 1.4 at d005 | >1.4 | — | — | ❓ | d005 Cohen's d 未在找到的源文件中存储，仅有 d100 数据 |

**注**: 论文中 "paired Cohen's d = −1.98 at d100" 的 −1.98 是 MMLU/GSM8K/ARC 三个 benchmark 在 0.5B scale 上的均值：(−1.22 + −2.67 + −2.05)/3 = −1.98。figure 代码 (`gen_fig_signal_heatmap.py` line 33) 中的对应值完全一致。

**⚠️ 源文件存在性问题**: 论文声称 "|d| > 1.4 at d005"，但此数值未在已找到的 JSON 产出中存储。可能来自分析脚本的临时输出或 experiment_data.json 中未包含的中间结果。建议补充 d005 Cohen's d 的持久化产出。

**结论**: 5/6 个可核对数字与源文件一致；1 个 (d005 Cohen's d) 源文件未找到。

---

## 审计总结

| 检查项 | 核对数 | 一致 | 不一致 | 源缺失 | 备注 |
|--------|--------|------|--------|--------|------|
| A. Table 3 Baselines | 14 | 14 | 0 | 0 | 全部通过 |
| B. S1-only vs RRF | 10 | 10 | 0 | 0 | 全部通过 |
| C. DIF comparison | 10 | 10 | 0 | 0 | ⚠️ JSON key 名称与论文标签互换 |
| D. Domain analysis | 5 | 5 | 0 | 0 | 全部通过 |
| E. Signal failure | 6 | 5 | 0 | 1 | d005 Cohen's d 源文件未找到 |
| **合计** | **45** | **44** | **0** | **1** | |

### 发现的问题

1. **⚠️ DIF JSON key 名称互换** (C 节): `results.json` 中 `uniform_dif` / `nonuniform_dif` 的 key 名称与论文中 "Non-uniform" / "Uniform" 标签反转。数值正确，但复现时可能导致混淆。建议修复 JSON 或添加注释。

2. **❓ d005 Cohen's d 源缺失** (E 节): 论文声称 "|d| > 1.4 at d005"，该数值在已检索的产出文件中未找到持久化存储。
