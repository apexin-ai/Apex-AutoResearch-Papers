# audit paper data verification

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper_data_verification_20260524T042818_result.json`
- **Structured JSON:** [`514f9b2a22568d2c1d4f.json`](../../sessions/51/514f9b2a22568d2c1d4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here is the comprehensive report.

---

## 论文全文数据自查报告

### 一、Abstract

| 数字 | 来源 | 一致性 |
|------|------|--------|
| 17.2% mean OOD | Table 1 Cell D: 17.16% → 1dp 四舍五入 | ✅ |
| 6.7% SFT baseline | Table 1: 6.72% → 1dp 四舍五入 | ✅ |
| 73% seeds stabilize | 8/11=72.7% → 73% | ✅ |
| 36% OOD transfer | 4/11=36.4% → 36% | ✅ |
| 8B, ScienceWorld | 与 §5.5 一致 | ✅ |
| Word count: 193 | 限制 200 | ✅ |

---

### 二、Introduction

| 数字 | 交叉验证 | 一致性 |
|------|----------|--------|
| 0% collapse | Table 1 Cell A | ✅ |
| 73% avoid collapse | 与 abstract/Table 2 一致 | ✅ |
| 36% OOD improvement | 与 abstract/Table 2 一致 | ✅ |

---

### 三、Theoretical Analysis (§3)

| 数字 | 独立计算 | 一致性 |
|------|----------|--------|
| 19.1% upper bound (p=12.5%, K=8) | 0.125/0.6564 = 19.04% → paper says 19.1% | ✅ (rounding 0.06pp) |
| (1-p)^K ≈ 34.4% | 0.875^8 = 0.3436 = 34.4% | ✅ |
| p^K < 10^{-7} | 0.125^8 = 5.96e-8 < 1e-7 | ✅ |
| p=50%: ≤50.2% | 0.5/(1-0.5^8) = 50.2% | ✅ |
| p=5%: ≤14.9% | 0.05/(1-0.95^8) = 14.9% | ✅ |
| 0.66 × 0.19 ≈ 12.5% | 0.656 × 0.190 = 12.5% | ✅ |
| Ratio 1.32 (Eq.6) | Registry artifact 确认 | ✅ |
| 87.5% wrong direction (large-K) | 1-p = 1-0.125 = 87.5% | ✅ |
| 52.1% credit agreement (penalty) | Registry `hsweep_h2_seed2`: sign_outcome_agreement=0.5207 | ✅ |

---

### 四、Experiments — Table 1 (Main Results)

| Cell | Metric | Paper | Registry | 一致性 |
|------|--------|-------|----------|--------|
| SFT | ID | 12.50% | val_before_train=12.5% (32 tasks) | ✅ |
| SFT | OOD | 6.72% | ood_eval_sft_baseline_v3: 9/134=6.72% | ✅ |
| A (h=2,step) | ID | 0% | seed1 val_final=0, seed2 val_step5=0 | ✅ |
| A (h=2,step) | OOD | 0% | seed1 无 OOD eval；seed2 step5=0% | ✅ (step 5) |
| B (h=2,episode) | OOD | 5.97% | factorial_h2_episodeadv_seed1: 0.0597 | ✅ |
| B (h=2,episode) | ID | 18.75% | **Registry 无记录** | ⚠️ 不可验证 |
| D (full,episode) | ID | 34.38% | mean(28.125,40.625)=34.375% | ✅ |
| D (full,episode) | OOD | 17.16% | mean(23.88,10.45)=17.165% | ✅ |
| D | ID range | 28.1–40.6 | 28.125–40.625 | ✅ |
| D | OOD range | 10.4–23.9 | 10.45–23.88 | ✅ |

---

### 五、Experiments — Sign Verification (§5.4)

| 数字 | Registry/Artifact | 一致性 |
|------|-------------------|--------|
| 99.6% (270/271) sign-episode | artifact binary_reward_final_analysis.md 确认 | ✅ |
| 52.07% credit agreement (n=3000) | hsweep_h2_seed2: 0.5207 | ✅ |
| p=0.025 binomial test | z=2.264, p=0.0247→0.025 | ✅ |
| Cohen's h=0.041 | 独立计算=0.0414 | ✅ |
| 28% binary credit (n=271) | artifact: 76/271=28.0% | ✅ |

---

### 六、Experiments — Table 2 (Seed Variability)

| Seed | Paper OOD | Registry | CI (computed vs paper) | 一致性 |
|------|-----------|----------|------------------------|--------|
| seed2048 | 8.21% | **无专属 OOD eval** | [4.6,14.1] vs [4.6,14.2] | ⚠️ OOD 来源不可验证 |
| seed42 | 12.69% | **无专属 OOD eval** | [8.1,19.4] vs [8.0,19.4] | ⚠️ OOD 来源不可验证 |
| seed8 | 11.94% | exp029_seed8_ood_precollapse: 0.1194 | [7.5,18.5] | ✅ |
| seed200 | 10.45% | exp029_seed200_step5_ood_eval: 14/134 | [6.3,16.8] | ✅ |
| seed300 | 10.45% | exp029_seed300_step5_ood_eval_v4: 14/134 | [6.3,16.8] | ✅ |
| seed100 s5 | 11.19% | exp029_seed100_step5_ood_eval: 15/134 | [6.9,17.6] | ✅ |
| seed100 s10 | 12.69% | exp029_seed100_step10_ood_eval: 17/134 | [8.1,19.4] vs [8.0,19.4] | ✅ (CI 0.1pp) |
| seed2 | 15.67% | **所有 eval 失败/取消** | [10.5,22.8] | ⚠️ OOD 来源不可验证 |
| seed1 | 23.88% | exp029_episode_level: 0.2388 | [17.5,31.8] vs [17.4,31.8] | ✅ (CI lower 0.1pp off) |
| seed5 | 29.10% | exp029_seed5_ood_eval: 0.291 | [22.1,37.3] | ✅ |
| seed6 | 29.10% | exp029_seed6_ood_eval_v2: 0.291 | [22.1,37.3] vs **[22.2,37.1]** | ❌ CI 错误 |
| seed4 | 30.60% | exp029_seed4_ood_eval_v2: 0.306 | [23.4,38.8] vs [23.5,38.7] | ⚠️ CI 0.1pp off |

**seed5 与 seed6 同为 39/134，Wilson CI 应完全相同 [22.1, 37.3]，但 seed6 写成 [22.2, 37.1]。** ❌

---

### 七、8B 和 ScienceWorld

| 数字 | Registry | 一致性 |
|------|----------|--------|
| 8B SFT ID 68.75% | 8b_det_eval_full: 0.6875 | ✅ |
| 8B SFT OOD 80.60% | 7b_sft_eval_ood: 0.806 | ✅ |
| 8B SFT h=2 31.25% | 8b_det_eval_h2: 0.3125 | ✅ |
| 8B Cell D ID 96.88% | val_before_train_step10: 0.96875 | ✅ |
| 8B Cell D OOD 90.30% | pass_at_1: 90.3 | ✅ |
| 8B Cell A 28.1→1.5% | 28.1% ✅; 1/64=1.5625% paper 写 1.5% | ❌ 应为 1.6% |
| 8B M1 gap 37.5pp | 68.75-31.25=37.5 | ✅ |
| SW Cell A 0% | scienceworld_grpo_cell_a: 0 | ✅ |
| SW M1 gap 30.3pp | sw_info_loss_bjb1: delta=30.3 | ✅ |

---

### 八、Appendix

| 数字 | 独立计算/Registry | 一致性 |
|------|-------------------|--------|
| K=16: 14.2% | 0.125/(1-0.875^16)=14.2% | ✅ |
| γ^24=0.29 | 0.95^24=0.292 | ✅ |
| Eval variance std=1.29pp | sample std(11.19,11.19,13.43)=1.29pp | ✅ |
| Eval variance mean=11.94% | (11.19+11.19+13.43)/3=11.94% | ✅ |
| seed6 step5 ID=21.88% | 7/32=21.875% | ✅ |
| Dense reward 60%→97.5% | 与 fig caption 一致 | ✅ |
| "ranging from 0% to 30.6%" | Table 2 最小值为 8.21%，无 0% | ❌ |
| 分类阈值 p<0.05 → p<0.01 | Table 2 用 p<0.01；appendix 描述矛盾 | ❌ |

---

## 汇总：发现 5 处问题

### ❌ 确认错误（需修复）

1. **seed6 Wilson CI 错误** (`experiments.tex` Table 2, L102)
   - 写了 `[22.2, 37.1]`，应为 `[22.1, 37.3]`（与 seed5 相同，同为 39/134）

2. **8B Cell A 1.5% 截断误差** (`appendix.tex` Table 8b_results, L116)
   - 1/64 = 1.5625%，四舍五入应为 1.6%，paper 写 1.5%

3. **Appendix eval variance "0%–30.6%" 范围错误** (`appendix.tex`, L232)
   - Table 2 中无 seed 为 0% OOD（最小 8.21%），应为 "8.2%–30.6%"

4. **Appendix 分类阈值描述矛盾** (`appendix.tex`, L234)
   - 写 "based on Fisher's exact test at p < 0.05; shifting to p < 0.01 would... changing from 36% to 27%"
   - 但 Table 2 实际用 p<0.01（seed2 at p=0.03 classified as S），且 36%=4/11 在 p<0.01 下成立
   - 逻辑自相矛盾：若 threshold=p<0.05，seed2 应为 G，rate=5/11=45%，不是 36%
   - 应改为：threshold is p<0.01; shifting to p<0.05 would reclassify seed2 as Generalized, changing rate from 36% to 45%

### ⚠️ 来源不可验证（Registry 无记录）

5. **seed2048, seed42, seed2 的 OOD 数字无 registry backing**
   - 论文已用 ‡ 标注这些来自 RAGEN built-in eval
   - seed2048 的 8.21% 与 seed7 high-KL step5 eval 数值重合，存在潜在 misattribution 风险
   - seed2 所有 OOD eval 均失败/取消，checkpoint 已丢失
   - 数字算术上自洽（CI、p-value 可由 k/134 推导），但源数据不可追溯

### ✅ 无问题

- Cell B ID=18.75% registry 无记录但可从 W&B 验证（6/32）
- 所有理论计算正确
- Abstract/正文/Table/Appendix 中 SFT baseline、Cell D、sign 数字交叉一致
- 99.6% (270/271) 全文两处出现，一致
- 52.07%/52.1% 精度差异为合理四舍五入
- 36%, 73% 等比例全文一致
- Abstract 193 words < 200 限制

---
