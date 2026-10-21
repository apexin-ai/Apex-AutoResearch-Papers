# Data Provenance & Correctness Audit

**Date**: 2026-05-23  
**Scope**: All quantitative claims in the paper (8 areas, 60+ data points)  
**Method**: Cross-reference each number against experiment registry, recompute derived statistics (Wilson CI, Fisher exact, binomial test, Proposition 2)

---

## 区域 1: Table 1 (main_results)

| 论文数字 | 来源 exp_id | Registry 值 | 匹配? | 备注 |
|----------|------------|------------|-------|------|
| SFT 12.50% ID | standard (4/32) | 4/32 = 12.5% | ✅ | |
| SFT 6.72% OOD | ood_eval_sft_baseline_v3 | pass_at_1=0.067 → 9/134=6.72% | ✅ | v2 gave 5.97% (8/134); paper uses v3 |
| Cell A 0% ID | hsweep_h2_seed1 | val_final.success=0 | ✅ | Post-collapse value |
| Cell A 0% OOD | hsweep_h2_seed1 | collapsed to 0% | ✅ | Post-collapse |
| Cell B 18.75% ID | factorial_h2_episodeadv_seed1 | 未记录 ID 指标 | ⚠️ | ID 值(6/32=18.75%)算术正确但 registry 无直接 ID 记录 |
| Cell B 5.97% OOD | factorial_h2_episodeadv_seed1 | val_step5.success=0.0597 | ✅ | 8/134=5.97% |
| Cell D 34.38% ID | exp029_episode_level + exp029_seed3_v2 | (9+13)/2/32=34.375% | ✅ | Mean of 2 seeds: 28.125% + 40.625% |
| Cell D 17.16% OOD | exp029_episode_level + exp029_seed3_ood_v2 | (0.2388+0.1045)/2=0.1717 | ✅ | (23.88%+10.45%)/2=17.165%→17.16% |
| Cell D range 28.1-40.6 ID | same | 9/32=28.125%, 13/32=40.625% | ✅ | |
| Cell D range 10.4-23.9 OOD | same | 10.45%, 23.88% | ✅ | 10.45→10.4, 23.88→23.9 rounded |
| Dense 0% ID | exp013f | final_val_pass_at1=0 | ✅ | |
| Dense 0% OOD | exp013f | final_val_success=0 | ✅ | |
| REINFORCE++ 12.50% ID | gae_baseline_seed1 | val_step5.success=0.125, val_step10.success=0.125 | ✅ | |
| REINFORCE++ --- OOD | gae_baseline_seed1 | 未做 OOD eval | ✅ | Correctly marked --- |

---

## 区域 2: Table 2 (seed_variability — 11 seeds)

### OOD Success Rate 验证

| Seed/Step | 论文值 | k/134 | Registry exp_id | Registry 值 | 匹配? | 备注 |
|-----------|--------|-------|-----------------|------------|-------|------|
| seed2048 step5 | 8.21% | 11/134 | (无直接 OOD eval) | — | ❌ | 无可追溯的 OOD eval 条目 |
| seed42 step5 | 12.69% | 17/134 | (无直接 OOD eval) | — | ❌ | 无可追溯的 OOD eval 条目 |
| seed8 step5 | 13.43% | 18/134 | exp029_seed8_ood_precollapse | 0.1194 (16/134) | ⚠️ | Registry=16/134=11.94%, 论文=18/134=13.43%, 差 2 tasks |
| seed200 step5 | 10.45% | 14/134 | exp029_seed200_step5_ood_eval | 0.1045 (14/134) | ✅ | |
| seed300 step5 | 10.45% | 14/134 | exp029_seed300_step5_ood_eval_v4 | 0.1045 (14/134) | ✅ | |
| seed100 step5 | 11.19% | 15/134 | exp029_seed100_step5_ood_eval | 0.1119 (15/134) | ✅ | |
| seed100 step10 | 12.69% | 17/134 | exp029_seed100_step10_ood_eval | 0.1269 (17/134) | ✅ | |
| seed2 step15 | 15.67% | 21/134 | (exp029_seed2_ood_step15: killed) | — | ❌ | Eval 被 kill，无可用结果 |
| seed1 step5 | 23.88% | 32/134 | exp029_episode_level | reeval_ood.success=0.2388 | ✅ | |
| seed5 step10 | 25.37% | 34/134 | exp029_seed5_ood_eval | 0.291 (39/134=29.10%) | ❌ | **严重差异**: 论文34/134 vs registry 39/134，差5 tasks |
| seed6 step15 | 29.10% | 39/134 | exp029_seed6_ood_eval_v2 | 0.291 (39/134) | ✅ | |
| seed4 step15 | 30.60% | 41/134 | exp029_seed4_ood_eval_v2 | 0.306 (41/134) | ✅ | |

### Wilson 95% CI 验证 (全部用 Python scipy 重新计算)

| Seed | 论文 CI | 计算 CI | 匹配? |
|------|---------|---------|-------|
| seed2048 (11/134) | [4.6, 14.2] | [4.6, 14.1] | ✅ |
| seed42 (17/134) | [8.0, 19.4] | [8.1, 19.4] | ✅ |
| seed8 (18/134) | [8.6, 20.3] | [8.7, 20.2] | ✅ |
| seed200 (14/134) | [6.3, 16.8] | [6.3, 16.8] | ✅ |
| seed300 (14/134) | [6.3, 16.8] | [6.3, 16.8] | ✅ |
| seed100 step5 (15/134) | [6.9, 17.6] | [6.9, 17.6] | ✅ |
| seed100 step10 (17/134) | [8.0, 19.4] | [8.1, 19.4] | ✅ |
| seed2 (21/134) | [10.5, 22.8] | [10.5, 22.8] | ✅ |
| seed1 (32/134) | [17.4, 31.8] | [17.4, 31.8] | ✅ |
| seed5 (34/134) | [18.8, 33.3] | [18.8, 33.4] | ✅ |
| seed6 (39/134) | [22.2, 37.1] | [22.1, 37.3] | ✅ |
| seed4 (41/134) | [23.5, 38.7] | [23.4, 38.8] | ✅ |

所有 Wilson CI 均在 ±0.2pp 内一致（正常的四舍五入差异）。

### Fisher Exact Test 验证 (vs SFT 9/134)

| Seed | 论文 | Fisher two-sided | Fisher one-sided | 匹配? | 备注 |
|------|------|-----------------|-----------------|-------|------|
| seed2048 (11) | NS | p=0.817 | — | ✅ | |
| seed42 (17) | NS | p=0.147 | — | ✅ | |
| seed8 (18) | NS | p=0.103 | — | ✅ | |
| seed200 (14) | NS | p=0.384 | — | ✅ | |
| seed300 (14) | NS | p=0.384 | — | ✅ | |
| seed100 step5 (15) | NS | p=0.285 | — | ✅ | |
| seed100 step10 (17) | NS | p=0.147 | — | ✅ | |
| seed2 (21) | p=0.02 | p=0.032 | p=0.016 | ⚠️ | Fisher exact 不给 0.02; chi-squared(无Yates)=0.020 吻合。论文声称 Fisher 但值更接近 chi-squared |
| seed1 (32) | p<0.001 | p=0.0001 | — | ✅ | |
| seed5 (34) | p<0.001 | p<0.0001 | — | ✅ | |
| seed6 (39) | p<0.001 | p<0.0001 | — | ✅ | |
| seed4 (41) | p<0.001 | p<0.0001 | — | ✅ | |

**注意**: 论文称对 seed2 "Fisher exact p=0.02"。Fisher two-sided 给 p=0.032，one-sided 给 p=0.016。chi-squared(无 Yates 校正)给 p=0.020。论文声称使用 Fisher exact test 但报告的 p 值与 chi-squared 吻合。结论不受影响（seed2 在 p<0.01 阈值下仍为 NS），但检验方法标注不准确。

---

## 区域 3: Table 3 (8b_results)

| 论文数字 | 来源 exp_id | Registry 值 | 匹配? | 备注 |
|----------|------------|------------|-------|------|
| SFT 68.75% ID | 8b_det_eval_full | success_rate=0.6875 (T=0, 32 tasks) | ✅ | 22/32 |
| SFT 80.60% OOD | 7b_sft_eval_ood | success_rate=0.806 (134 tasks) | ✅ | 命名含"7b"但实为8B eval(见hypothesis) |
| SFT h=2 31.25% ID | 8b_det_eval_h2 | success_rate=0.3125 (T=0, 32 tasks) | ✅ | 10/32 |
| Cell A 28.1→1.5 | 7b_cell_a_h2 | val_before_train=0.281, step2_train=0.015625 | ⚠️ | 28.1%✓; 1.5625%→论文写1.5%，差0.0625pp (1/64≠1.5%) |
| Cell D 96.88% ID | 8b_cell_c_episode_v9d | val_before_train_step10=0.96875 | ✅ | 31/32 |
| Cell D 90.30% OOD | 8b_v9d_ood_eval_v5 | pass_at_1=90.3 | ✅ | |

---

## 区域 4: Section 4.4 Sign Verification

| 论文数字 | 来源 | 验证值 | 匹配? | 备注 |
|----------|------|--------|-------|------|
| 52.07% credit agreement | hsweep_h2_seed2 adv_analysis | sign_outcome_agreement=0.5207 | ✅ | |
| n=3000 windows | same | total_records=3000 | ✅ | |
| 1562/3000 | binomial_test_results.md | k=1562 | ✅ | 1562/3000=0.52067=52.07% |
| 95% CI [50.3%, 53.9%] | Wilson CI recompute | [50.3%, 53.8%] | ✅ | 上界差 0.1pp（四舍五入） |
| p=0.025 vs 50% | binomial test recompute | p=0.0247 | ✅ | 0.0247 → 0.025 rounded |
| +2.07pp effect size | arithmetic | 52.07-50.00=2.07 | ✅ | |
| point-biserial r=0.068 | adv_analysis_v2_summary | point_biserial_r=0.068 | ✅ | |
| r>0.99 episode outcome correlation | hsweep_h2_seed2 | 未直接记录在registry | ⚠️ | 仅声明未可追溯验证 |

---

## 区域 5: Window-size Sweep

| 论文数字 | 来源 exp_id | Registry 值 | 匹配? | 备注 |
|----------|------------|------------|-------|------|
| h=2: 0% | hsweep_h2_seed1 | val_final.success=0 | ✅ | |
| h=5: 0% | gsweep_g095_h5_seed1 | val_success_step5=0 | ✅ | |
| h=10: 6.25% | hsweep_h10_seed1 | step5_val_success="SFT_baseline" | ⚠️ | Registry 记录为 "SFT_baseline"，论文报 6.25%=2/32。来源不明 |
| h=20: 15.6% | hsweep_h20_seed1 | val_step5_success=0.15625 | ✅ | 5/32=15.625%→15.6% |
| episode: 23.88% | exp029_episode_level | reeval_ood.success=0.2388 | ✅ | 32/134 |

**严重问题**: 图表标题写 "OOD success"，但 h=10 和 h=20 的数字（6.25%=2/32, 15.6%=5/32）明确来自 32-task **ID** 评估集；episode 的 23.88%=32/134 来自 134-task **OOD** 评估集。**同一图中混用了不同评估集的指标**。

---

## 区域 6: ScienceWorld

| 论文数字 | 来源 exp_id | Registry 值 | 匹配? | 备注 |
|----------|------------|------------|-------|------|
| SFT 30.1% (τ=0.4) | scienceworld_sft_eval_v2 | overall_success_rate=0.301 | ✅ | 540/1796 |
| SFT 34.8% (τ=0) | sw_info_loss_bjb1 | full_context_success=0.348 | ✅ | |
| h=2 drops to 4.5% | sw_info_loss_bjb1 | h2_success=0.045 | ✅ | |
| 30.3pp gap | arithmetic | 34.8-4.5=30.3 | ✅ | |
| Cell A 0% | scienceworld_grpo_cell_a | success_rate=0 | ✅ | |

---

## 区域 7: Appendix Table 7 (step5 unified)

与 Table 2 交叉验证——所有共享数据点一致：

| Seed | Table 7 OOD | Table 2 OOD | 匹配? |
|------|-------------|-------------|-------|
| seed2048 | 8.21% | 8.21% (step5) | ✅ |
| seed8 | 13.43% | 13.43% (step5) | ✅ |
| seed42 | 12.69% | 12.69% (step5) | ✅ |
| seed200 | 10.45% | 10.45% (step5) | ✅ |
| seed300 | 10.45% | 10.45% (step5) | ✅ |
| seed100 | 11.19% | 11.19% (step5) | ✅ |
| seed1 | 23.88% | 23.88% (step5) | ✅ |

Table 7 ID 值（有数据的）：
- seed8 ID 28.13% → 9/32 ✓ (exp029_seed8: val_success_step5=0.2813)
- seed42 ID 9.38% → 3/32 ✓
- seed300 ID 25.00% → 8/32 ✓
- seed100 ID 31.25% → 10/32 ✓ (exp029_seed100_episode: val_pass_at_1_final=0.1875 是step5 final, 但seed100_step5_ood_eval 显示此为正确checkpoint)
- seed6 ID 21.88% → 7/32 ✓ (注释称 registry 21.9% = 7/32 rounded)

Tables 2 和 7 **内部一致**。但 seed8 和 seed5 的 registry 差异同样影响 Table 7。

---

## 区域 8: Abstract / Introduction / Conclusion

| 论文数字 | 出处 | 验证 | 匹配? |
|----------|------|------|-------|
| "17.2% mean OOD" (Abstract) | Table 1 Cell D | (23.88+10.45)/2=17.165→17.2% | ✅ |
| "90.3% OOD at 8B" (Abstract) | Table 3 Cell D | 8b_v9d_ood_eval_v5: 90.3 | ✅ |
| "1.5% collapse" (Abstract) | Table 3 Cell A | 7b_cell_a_h2: 0.015625→1.5625% | ⚠️ |
| "80.9% incorrect sign" (Abstract, Intro, Conclusion) | Proposition 2 | p/(1-(1-p)^K)=19.04%→80.96%≈80.9% | ✅ |
| "52% credit agreement" (Abstract, Intro) | Section 4.4 | 1562/3000=52.07% | ✅ |
| "p=0.025 vs 50%" (Abstract) | Section 4.4 | binomial p=0.0247→0.025 | ✅ |
| "+2pp effect size" (Abstract) | Section 4.4 | 52.07-50=2.07≈2pp | ✅ |
| "73% avoid collapse" (Abstract, Intro, Conclusion) | 11-seed study | 8/11=72.7%→73% | ✅ |
| "36% generalize" (Abstract, Intro, Conclusion) | 11-seed study | 4/11=36.4%→36% | ✅ |
| "24-31% OOD" (Abstract) | G seeds range | 23.88-30.60%→24-31% rounded | ✅ |
| "6.7% SFT baseline" (Abstract) | Table 1 | 9/134=6.716%→6.7% | ✅ |
| "19.1% correct" (Theory section) | Proposition 2 | 0.125/0.6564=19.04%→19.1% | ✅ |
| "$\sim$34.4% all-fail" (Theory) | (1-p)^K | 0.875^8=0.3436→34.4% | ✅ |
| "0.66 × 0.19 ≈ 12.5% effective" (Theory) | arithmetic | 0.6564×0.1904=0.1250 | ✅ |
| Conclusion 所有数字 | 同 Abstract | 交叉验证一致 | ✅ |

---

## 汇总

### ✅ 已验证匹配: 52 个数字

所有 Table 1 核心数字、Wilson CI (12/12)、Fisher significance 方向 (12/12)、Proposition 2 预测值、binomial test 统计量、ScienceWorld 全部数字、Abstract/Intro/Conclusion 引用数字、Table 3 大部分数字、Table 7 与 Table 2 交叉一致性。

### ⚠️ 有差异但不影响结论: 5 个

| # | 差异 | 详情 | 影响 |
|---|------|------|------|
| 1 | Cell B 18.75% ID | Registry 无直接 ID 记录，但 6/32=18.75% 算术正确 | 低 |
| 2 | 8B Cell A "1.5%" | 实际值 1.5625% (1/64)，论文写 1.5% | 极低 |
| 3 | seed2 p=0.02 | Fisher exact 给 p=0.032 或 0.016；chi-squared 无Yates 给 0.020。检验方法标注不准确 | 低 |
| 4 | r>0.99 episode correlation | 声明存在但 registry 无可追溯验证数据 | 中 |
| 5 | h=10 sweep: 6.25% | Registry 记录 "SFT_baseline"，与 6.25% 不一致 | 中 |

### ❌ 有差异或无法追溯: 6 个

| # | 问题 | 详情 | 严重程度 |
|---|------|------|---------|
| 1 | **seed5 step10: 25.37% vs 29.10%** | 论文报 34/134=25.37%，exp029_seed5_ood_eval 记录 39/134=29.10%。差 5 tasks。Registry 有 verification note 确认 29.10% 正确。无其他 eval 给出 34/134。 | **高** |
| 2 | **seed8 step5: 13.43% vs 11.94%** | 论文报 18/134=13.43%，exp029_seed8_ood_precollapse 记录 16/134=11.94%。差 2 tasks。可能因不同 eval 配置导致。 | **中** |
| 3 | **seed2048 step5: 8.21% 无追溯** | exp029_new_seed_2048 无 OOD eval 条目。8.21%=11/134 的来源不明。 | **中** |
| 4 | **seed42 step5: 12.69% 无追溯** | exp029_seed42_episode 无 OOD eval 条目。12.69%=17/134 的来源不明。 | **中** |
| 5 | **seed2 step15: 15.67% 无追溯** | exp029_seed2_ood_step15 状态为 killed。21/134=15.67% 的最终结果来源不明。 | **中** |
| 6 | **Window sweep 混用评估集** | 图表标题写 "OOD success"，但 h=10 (6.25%=2/32) 和 h=20 (15.6%=5/32) 来自 32-task ID 集，episode (23.88%=32/134) 来自 134-task OOD 集。 | **高** |

### 统计验证总结

| 统计量 | 方法 | 结果 |
|--------|------|------|
| Wilson CI × 12 | scipy Wilson formula | 全部在 ±0.2pp 内一致 ✅ |
| Fisher exact × 12 | scipy.stats.fisher_exact | 方向全部一致；seed2 具体 p 值有差异 ⚠️ |
| Binomial test | scipy.stats.binomtest | p=0.0247 → 论文0.025 ✅ |
| Proposition 2 | 公式计算 | 19.04%/80.96% → 论文19.1%/80.9% ✅ |
| Cell D mean | 算术 | (23.88+10.45)/2=17.165 → 17.16% ✅ |

---

## 建议修复优先级

1. **P0 — seed5 数据**: 核实 seed5 step10 OOD 到底是 34/134 还是 39/134。若 registry 的 39/134 正确，需更新 Table 2 及其 Wilson CI 和所有引用。
2. **P0 — Window sweep 评估集**: 修正图表标题（"OOD success" → "success rate"），或在文本中明确说明 h=10/h=20 为 ID 指标、episode 为 OOD 指标，或补做 h=10/h=20 的 OOD eval。
3. **P1 — seed8 数据**: 核实 step5 OOD 是 16/134 还是 18/134，记录使用的 eval 配置。
4. **P1 — 无追溯数据点 (seed2048, seed42, seed2)**: 补充这 3 个 seed 的 OOD eval registry 条目，或标注数据来源（如来自 RAGEN 内置 eval 需注明）。
5. **P2 — seed2 p-value**: 如实际使用 chi-squared 非 Fisher exact，修改描述；或重新用 Fisher exact 计算并更新 p 值。
6. **P2 — 1.5% rounding**: 改为 1.6% 或标注 "≈1.5%"。
