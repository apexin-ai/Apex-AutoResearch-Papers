# 数据自查报告

**日期**: 2026-05-23
**范围**: 论文全部定量数据，覆盖 8 章节、60+ 数据点
**方法**: 逐一交叉验证 registry/artifact/plot 脚本/手动计算

---

## ✅ 已核对一致

### Abstract
- 17.2% mean OOD ← Cell D 2-seed mean: (23.88+10.45)/2=17.165→17.2% (exp029_episode_level + exp029_seed3_ood_v2)
- 6.7% SFT baseline ← 9/134=6.716%→6.7% (ood_eval_sft_baseline_v3: pass_at_1=0.067)
- ≤19.1% upper bound ← Proposition 2: 0.125/(1-0.875^8)=19.04%→19.1% (intermediate rounding)
- 73% stabilize ← 8/11=72.7%→73%
- 36% generalize ← 4/11=36.4%→36%

### Table 1 (main_results)
- SFT 12.50% ID ← 4/32=12.5% ✓
- SFT 6.72% OOD ← 9/134=6.716% (ood_eval_sft_baseline_v3) ✓
- Cell A 0%/0% ← hsweep_h2_seed1: collapsed ✓
- Cell B 18.75% ID / 5.97% OOD ← factorial_h2_episodeadv_seed1: val_step5.success=0.0597 ✓; ID=6/32 arithmetic ✓
- Cell D 34.38% ID / 17.16% OOD ← mean of 2 seeds: (28.125+40.625)/2=34.375→34.38% ✓; (23.88+10.45)/2=17.165→17.16% ✓
- Cell D range 28.1-40.6 / 10.4-23.9 ← 9/32=28.125→28.1, 13/32=40.625→40.6, 10.45→10.4, 23.88→23.9 ✓
- Dense 0%/0% ← exp013f: final_val_success=0 ✓
- REINFORCE++ 12.50%/--- ← gae_baseline_seed1: val_step5=0.125 ✓

### Table 2 (11-seed OOD)
- seed2048 step5: 8.21% = 11/134 (RAGEN built-in eval, ‡标注) ✓
- seed42 step5: 12.69% = 17/134 (RAGEN built-in eval, ‡标注) ✓
- seed8 step5: 11.94% = 16/134 ← exp029_seed8_ood_precollapse: 0.1194 ✓
- seed200 step5: 10.45% = 14/134 ← exp029_seed200_step5_ood_eval: 0.1045 ✓
- seed300 step5: 10.45% = 14/134 ← exp029_seed300_step5_ood_eval_v4: 0.1045 ✓
- seed100 step5: 11.19% = 15/134 ← exp029_seed100_step5_ood_eval: 0.1119 ✓
- seed100 step10: 12.69% = 17/134 ← exp029_seed100_step10_ood_eval: 0.1269 ✓
- seed2 step15: 15.67% = 21/134 (RAGEN built-in eval, ‡标注) ✓
- seed1 step5: 23.88% = 32/134 ← exp029_episode_level: reeval_ood.success=0.2388 ✓
- seed5 step10: 29.10% = 39/134 ← exp029_seed5_ood_eval: 0.291 ✓
- seed6 step15: 29.10% = 39/134 ← exp029_seed6_ood_eval_v2: 0.291 ✓
- seed4 step15: 30.60% = 41/134 ← exp029_seed4_ood_eval_v2: 0.306 ✓
- Wilson 95% CIs: 全部12组 ±0.1pp 内一致 (scipy.stats 重算验证)
- Fisher exact tests: 方向全部正确; seed2 p=0.03 ← Fisher two-sided=0.0317→0.03 ✓

### Table 3 (8B results)
- SFT 68.75% ID ← 8b_det_eval_full: 0.6875 ✓
- SFT 80.60% OOD ← 7b_sft_eval_ood: 0.806 ✓
- SFT h=2 31.25% ID ← 8b_det_eval_h2: 0.3125 ✓
- Cell D 96.88% ID ← 8b_cell_c_episode_v9d: val_before_train_step10=0.96875 ✓
- Cell D 90.30% OOD ← 8b_v9d_ood_eval_v5: pass_at_1=90.3 ✓

### Section 4.4 Sign Verification
- 52.07% credit agreement (penalty, h=2) ← hsweep_h2_seed2 adv_analysis: sign_outcome_agreement=0.5207 ✓
- n=3,000 windows ← adv_log_lines=3000 ✓
- p=0.025 vs 50% ← binomial test: p=0.0247→0.025 ✓
- +2.07pp effect size ← 52.07-50.00=2.07 ✓
- 100% sign-episode correlation (binary, n=157) ← binary_reward_final_analysis.md iter1: 157/157=100% ✓
- 28% credit agreement (binary, n=271) ← binary_reward_final_analysis.md aggregate: 76/271=28.0% ✓

### Theoretical Calculations
- (1-p)^K = 0.875^8 ≈ 0.344 ← exact: 0.34361 ✓
- P(correct|update) = 0.125/0.656 ≈ 19.1% ← exact: 19.04%, intermediate rounding gives 19.1% ✓
- p=50%, K=8: ≤50.2% ← exact: 128/255=50.20% ✓
- p^K < 10^-7 ← 0.125^8=5.96e-8 ✓
- 0.66×0.19≈12.5% ← exact: 0.6564×0.1904=0.1250 ✓
- K=16: (1-p)^K≈0.118, P≈14.2% ← exact: 0.1181, 14.17% ✓
- 1.32 advantage magnitude ratio ← binomial_test_results.md: weighted avg per-group ratio=1.32 ✓

### ScienceWorld
- SFT 30.1% (τ=0.4) ← scienceworld_sft_eval_v2: 0.301 ✓
- SFT 34.8% (τ=0) ← sw_info_loss_bjb1: full_context_success=0.348 ✓
- h=2 drops to 4.5% ← sw_info_loss_bjb1: h2_success=0.045 ✓
- 30.3pp info loss gap ← 34.8-4.5=30.3 ✓
- Cell A 0% ← scienceworld_grpo_cell_a: success_rate=0 ✓

### Appendix Table 7 (step5 unified)
- 所有与 Table 2 共享的 OOD 数据点一致 ✓
- ID 值 (seed8 28.13%, seed42 9.38%, seed300 25.00%, seed100 31.25%, seed6 21.88%): 算术正确 ✓

### Figure Data
- Figure 1 (overview): 概念图，无定量数据 ✓
- Figure 2 (sign misattribution): 100%/n=157 + 52.07%/n=3000 硬编码值与源数据一致 ✓
- Figure 3(a) (training dynamics): 从 W&B 提取的 ID success rates，无法从 registry 独立验证
- Figure 3(b) (h-sweep): h=2→0%, h=5→0%, h=20→15.6%(=5/32), Full→23.88%(=32/134) 与 registry 一致 ✓; 已标注 ID/OOD 区分 ✓
- Figure 4 (theory curve): 公式 P=p/(1-(1-p)^K) 的可视化 ✓

### Discussion/Conclusion
- HCAPO 91.4% (7B) ← 原论文数字，引用正确 ✓
- GiGPO 90.2% ← 原论文数字，引用正确 ✓
- 所有结论章节数字与正文交叉一致 ✓

---

## ⚠️ 发现的不一致 / 已修复

### 1. [已修复] p=5% K=8 理论计算错误
- **位置**: theoretical_analysis.tex L31
- **旧值**: "at p=5%, at most 5.1% of updates are correct"
- **正确值**: P(correct|update) = 0.05/(1-0.95^8) = 0.05/0.3366 = **14.9%**
- **修复**: 改为 "at most 14.9% of updates are correct"
- **来源**: 手动计算验证; 5.1% 不对应任何合理的 K 值

### 2. [已修复] Table 1 caption 17.2% 归属歧义
- **位置**: experiments.tex Table 1 caption
- **旧文**: "where mean OOD=17.2% with 36% generalization rate" (语法上修饰 11-seed evaluation)
- **问题**: 17.2% 是 Cell D 2-seed mean (17.16%), 11-seed best-checkpoint mean 实际为 17.71%
- **修复**: 改为 "Cell~D mean OOD (17.2\%) is consistent with the 11-seed evaluation, which shows 36\% generalization rate."

---

## ❌ 待人工确认的疑点

### 1. h=10 sweep 值: 6.25% vs SFT_baseline
- **位置**: Figure 3(b) bar chart
- **问题**: 图中 h=10 = 6.25% (2/32), 但 registry hsweep_h10_seed1 记录 "step5_val_success: SFT_baseline" (=12.5%). 6.25% 可能来自其他 step 或直接从 W&B 提取。
- **严重程度**: 中
- **建议**: 确认 h=10 使用的是哪个 step 的 val success

### 2. seed2048, seed42, seed2 的 OOD 值无独立 registry 追溯
- **位置**: Table 2 (标注 ‡)
- **问题**: 这 3 个 seed 使用 RAGEN built-in eval, registry 无独立 OOD eval 条目
- **严重程度**: 低 (已通过 ‡ 标注告知读者)
- **建议**: 无需修改，但如有条件可补做独立 OOD eval

### 3. Sign-episode 100% 基于单次迭代
- **位置**: experiments.tex Section 4.4
- **问题**: 100% (n=157) 来自 binary reward iter 0; 3-iteration 汇总为 99.6% (270/271, 1 个 edge case 由 GRPO 组内归一化引起)
- **严重程度**: 低 (100% 是该度量的理论预期，单例外是 GRPO edge case)
- **建议**: 可考虑改为 "near-perfect (99.6%)" 或在脚注注明

### 4. 19.1% vs 19.04% (中间值四舍五入)
- **位置**: theoretical_analysis.tex, appendix, 多处
- **问题**: 精确值 P=0.125/0.65639=19.04%, 论文用 0.125/0.656=19.05%→19.1%. 80.9%=1-19.1% 精确应为 80.96%
- **严重程度**: 极低 (不影响任何结论)
- **建议**: 不修改; 四舍五入在合理范围内

### 5. 8B Cell A "1.5%"
- **位置**: appendix Table 3
- **问题**: Registry 7b_cell_a_h2: step2_train_success=0.015625 = 1.5625%. 论文写 "1.5". 差 0.06pp
- **严重程度**: 极低
- **建议**: 不修改; "1.5" 是 1.5625% 的合理近似

### 6. Cell B In-Dist 18.75% 无直接 registry 记录
- **位置**: Table 1
- **问题**: factorial_h2_episodeadv_seed1 的 registry 仅记录 OOD 指标, 无 ID 32-task eval 值. 18.75% = 6/32 算术正确
- **严重程度**: 低 (值可来自 W&B)
- **建议**: 无需修改

### 7. Figure 3(a) training dynamics 值来自 W&B, 无法从 registry 独立验证
- **位置**: gen_fig_training_dynamics.py 硬编码
- **问题**: 16 步的 ID success rate 数据来自 W&B, registry 仅有部分点
- **严重程度**: 低 (W&B 是权威数据源)
- **建议**: 无需修改

### 8. SFT OOD 基准使用 v3 eval (PREPARING 状态)
- **位置**: 全文 SFT baseline 6.72%
- **问题**: ood_eval_sft_baseline_v3 在 registry 中 status=PREPARING 但 metrics 已有 pass_at_1=0.067. v2 (DONE) 给 0.0597=8/134. v3 给 9/134=6.72%
- **严重程度**: 低 (v3 使用了正确的 eval 配置 enable_response_mask=false)
- **建议**: 将 v3 registry 状态更新为 DONE

---

## 统计验证汇总

| 统计量 | 方法 | 结果 |
|--------|------|------|
| Wilson CI × 12 | scipy Wilson formula | ±0.1pp 内一致 ✅ |
| Fisher exact × 12 | scipy.stats.fisher_exact | 方向全部正确 ✅ |
| Binomial test (52.07% vs 50%) | scipy.stats.binomtest | p=0.0247 → 论文 0.025 ✅ |
| Proposition 2 公式 | 精确分数计算 | 19.04% → 论文 19.1% (中间舍入) ✅ |
| p=50% K=8 | 128/255 | 50.20% ✅ |
| p=5% K=8 | 0.05/0.3366 | **14.86% ← 论文原写 5.1% [已修复为 14.9%]** |
| Cell D mean | 算术 | (23.88+10.45)/2=17.165 → 17.16% ✅ |
| 11-seed mean (best ckpt) | 算术 | 261/(11×134)=17.71% |

---

## 已执行的修复

1. `theoretical_analysis.tex` L31: "5.1%" → "14.9%"
2. `experiments.tex` Table 1 caption: 消除 "mean OOD=17.2%" 对 11-seed evaluation 的错误归属
3. 重新编译 `latexmk -pdf main.tex` 确认无错误
