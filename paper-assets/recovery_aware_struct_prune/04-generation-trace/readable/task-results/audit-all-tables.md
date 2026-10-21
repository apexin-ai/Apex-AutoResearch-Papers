# audit all tables

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_all_tables_20260524T045119_result.json`
- **Structured JSON:** [`dc6dd7617b13f8734263.json`](../../sessions/dc/dc6dd7617b13f8734263.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Found it — `eval_sft_standard_full_westd` has accuracy 0.5929 (782/1319), matching the table's 59.29%. The Standard SFT uses the retrained westd checkpoint. Now I have all the data for the complete audit.

---

## 全量 Table 数据审计报告

---

### tab1_recovery_gradient.tex (4 methods × 3 metrics = 12 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| CKA-only Peak Rew | 0.354 | `grpo_cka_only_20` | peak_reward: 0.3544 → 0.354 | ✅ |
| CKA-only Mean Rew | 0.285 | `grpo_cka_only_20` | 无 mean_reward 字段 (final_reward=0.3444) | ⚠️ W&B |
| CKA-only Min f₀ | 0.125 | `grpo_cka_only_20` | 无 min_frac_zero_std 字段 (final=0.2) | ⚠️ W&B |
| Random Peak Rew | 0.190 | `grpo_random_20` | reward_peak: 0.19 | ✅ |
| Random Mean Rew | 0.164 | `grpo_random_20` | reward_mean: 0.164 | ✅ |
| Random Min f₀ | 0.300 | `grpo_random_20` | frac_zero_std_mean: 0.333 (非 min) | ⚠️ W&B |
| Standard Peak Rew | 0.081 | `grpo_standard_20_fair` | peak_reward: 0.081 | ✅ |
| Standard Mean Rew | 0.050 | `grpo_standard_20_fair` | 无 mean 字段 (final_reward=0.054) | ⚠️ W&B |
| Standard Min f₀ | 0.500 | `grpo_standard_20_fair` | final_frac_zero_std: 0.55 (非 min) | ⚠️ W&B |
| RASP Peak Rew | 0.061 | `grpo_rasp_20_fair` | peak_reward: 0.061 | ✅ |
| RASP Mean Rew | 0.031 | `grpo_rasp_20_fair` | 无 mean 字段 (final_reward=0.01) | ⚠️ W&B |
| RASP Min f₀ | 0.675 | `grpo_rasp_20_fair` | min_frac_zero_std: 0.675 | ✅ |

**小结**: 6/12 ✅ 直接验证, 6/12 ⚠️ 需 W&B 训练曲线验证 (Mean Rew 和 Min f₀ 是 step-level 聚合值, registry 仅记录 peak/final)。数值精度统一 3 位小数 ✓。Bold 标记正确 ✓。

---

### tab2_decoupling.tex (23 numerical cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Unpruned SFT | 81.27% | `eval_sft_unpruned_full` | accuracy: 81.27 | ✅ |
| Unpruned GRPO | 81.27% | `eval_grpo_unpruned_v2_step100` | accuracy: 81.27 (1072/1319) | ✅ |
| Unpruned Δ | 0.00 | computed | 81.27 − 81.27 = 0.00 | ✅ |
| Unpruned Peak Rew | 0.669 | `grpo_unpruned_v2` | peak_reward: 0.669 | ✅ |
| CKA-only SFT | 63.91% | `eval_gsm8k_sft_cka_only_20` | gsm8k_accuracy: 0.6391 (843/1319) | ✅ |
| CKA-only GRPO mean | 64.39% | seeds 42/123/456 | (64.37+64.22+64.59)/3 = 64.39 | ✅ |
| CKA-only GRPO std | ±0.19 | seeds 42/123/456 | std(64.37,64.22,64.59) = 0.186 → 0.19 | ✅ |
| CKA-only Δ | +0.48 | computed | 64.39 − 63.91 = 0.48 | ✅ |
| CKA-only Peak Rew | 0.354 | `grpo_cka_only_20` | peak_reward: 0.3544 → 0.354 | ✅ |
| Standard SFT | 59.29% | `eval_sft_standard_full_westd` | accuracy: 0.5929 (782/1319) | ✅ |
| Standard GRPO mean | 59.84% | seeds 42/123/456 | (59.44+59.89+60.20)/3 = 59.84 | ✅ |
| Standard GRPO std | ±0.38 | seeds 42/123/456 | std = 0.382 → 0.38 | ✅ |
| Standard Δ | +0.55 | computed | 59.84 − 59.29 = 0.55 | ✅ |
| Standard Peak Rew | 0.081 | `grpo_standard_20_fair` | peak_reward: 0.081 | ✅ |
| RASP SFT | 61.49% | `eval_gsm8k_sft_rasp_20` | gsm8k_accuracy: 0.6149 (811/1319) | ✅ |
| RASP GRPO | 60.88% | `eval_gsm8k_grpo_rasp_20_fair` | accuracy: 0.6088 (803/1319) | ✅ |
| RASP Δ | −0.61 | computed | 60.88 − 61.49 = −0.61 | ✅ |
| RASP Peak Rew | 0.061 | `grpo_rasp_20_fair` | peak_reward: 0.061 | ✅ |
| Random SFT | 51.25% | `eval_gsm8k_sft_random_20` | gsm8k_accuracy: 0.5125 (676/1319) | ✅ |
| Random GRPO mean | 50.72% | seeds 42/123/456 | (50.57+50.72+50.87)/3 = 50.72 | ✅ |
| Random GRPO std | ±0.15 | seeds 42/123/456 | std = 0.15 | ✅ |
| Random Δ | −0.53 | computed | 50.72 − 51.25 = −0.53 | ✅ |
| Random Peak Rew | 0.190 | `grpo_random_20` | reward_peak: 0.19 | ✅ |
| ShortGPT SFT | 44.73% | `eval_gsm8k_sft_shortgpt_20` | gsm8k_accuracy: 44.73 | ✅ |
| ShortGPT GRPO | 43.37% | `eval_gsm8k_grpo_shortgpt_20` | gsm8k_accuracy: 43.37 | ✅ |
| ShortGPT Δ | −1.36 | computed | 43.37 − 44.73 = −1.36 | ✅ |
| ShortGPT Peak Rew | -- | N/A | 无 ShortGPT GRPO 训练实验 | ✅ (正确标注为 --) |

**Multi-seed source exp_ids**:
- CKA-only: `eval_gsm8k_grpo_cka_only_20_v2` (seed42, 0.6437), `eval_gsm8k_grpo_cka_only_20_seed123` (0.6422), `eval_gsm8k_grpo_cka_only_20_seed456_full` (0.6459)
- Standard: `eval_gsm8k_grpo_standard_20_fair_v2` (seed42, 59.44%), `eval_gsm8k_grpo_standard_20_seed123_full` (0.5989), `eval_gsm8k_grpo_standard_20_seed456_full` (0.602)
- Random: `eval_gsm8k_grpo_random_20_v2` (seed42, 0.5057), `eval_gsm8k_grpo_random_20_seed123_v2` (0.5072), `eval_gsm8k_grpo_random_20_seed456` (0.5087)

**小结**: 27/27 ✅。精度统一 (GSM8K 2dp, Reward 3dp) ✓。Bold 正确 ✓。Footnote 脚注 ($N{=}1$ for RASP, 3 seeds for others) 与数据一致 ✓。

---

### table3_alpha.tex (5 α × 3 columns = 15 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| α=0.5 SFT | 60.73% | `eval_gsm8k_sft_alpha0p5_20` | 0.6073 | ✅ |
| α=0.5 GRPO | 61.18% | `eval_gsm8k_grpo_alpha0p5_20` | 0.6118 | ✅ |
| α=0.5 Δ | +0.45 | computed | 61.18−60.73=0.45 | ✅ |
| α=1.0 SFT | 61.49% | `eval_gsm8k_sft_rasp_20` | 0.6149 | ✅ |
| α=1.0 GRPO | 60.88% | `eval_gsm8k_grpo_rasp_20_fair` | 0.6088 | ✅ |
| α=1.0 Δ | −0.61 | computed | 60.88−61.49=−0.61 | ✅ |
| α=2.0 SFT | 64.97% | `eval_gsm8k_sft_alpha2p0_20` | 0.6497 | ✅ |
| α=2.0 GRPO | 66.11% | `eval_gsm8k_grpo_alpha2p0_20` | 0.6611 | ✅ |
| α=2.0 Δ | +1.14 | computed | 66.11−64.97=1.14 | ✅ |
| α=3.0 SFT | 64.14% | `eval_gsm8k_sft_alpha3p0_20` | 0.6414 (846/1319) | ✅ |
| α=3.0 GRPO | 63.46% | `eval_gsm8k_grpo_alpha3p0_20` | 0.6345 → 837/1319=63.46% | ✅ |
| α=3.0 Δ | −0.68 | computed | 63.46−64.14=−0.68 | ✅ |
| α=4.0 SFT | 61.94% | `eval_gsm8k_sft_alpha4_20_v5` | 0.6194 (817/1319) | ✅ |
| α=4.0 GRPO | 62.77% | `eval_gsm8k_grpo_alpha4_20_v3` | 0.6277 (828/1319) | ✅ |
| α=4.0 Δ | +0.83 | computed | 62.77−61.94=0.83 | ✅ |

**注**: α=3.0 GRPO registry 存储值 0.6345 是 4dp 截断, 实际 837/1319=0.63457→63.46%。表格值正确。

**小结**: 15/15 ✅。精度 2dp 统一 ✓。Bold (α=2.0) 正确 ✓。

---

### table4_sparsity_cliff.tex (8 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Standard N | 200 | `eval_postprune_standard_30` | total: 200 | ✅ |
| Standard Acc | 4% | `eval_postprune_standard_30` | gsm8k_accuracy: 0.04 → 4% | ✅ |
| Standard EOS Rate | 5.5% | `eval_postprune_standard_30` | eos_rate: 0.055 → 5.5% | ✅ |
| RASP N | 200 | `eval_postprune_rasp_30` | n_total: 200 | ✅ |
| RASP Acc | 0% | `eval_postprune_rasp_30` | accuracy: 0 | ✅ |
| RASP EOS Rate | 3.0% | `eval_postprune_rasp_30` | eos_rate: 0.03 → 3.0% | ✅ |
| CKA-only N | 500† | `prune_eval_cka_only_30` | n_evaluated: 500 | ✅ |
| CKA-only Acc | 1.6% | `prune_eval_cka_only_30` | accuracy: 1.6 | ✅ |

**Footnote 验证**: "8/500 correct" → 8/500=1.6% ✓。CKA-only EOS Rate = "--†" (terminated early, 正确标注) ✓。

**小结**: 8/8 ✅。

---

### tab5_cross_scale.tex (13 numerical cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| CKA-only 7B Peak Rew | 0.354 | `grpo_cka_only_20` | 0.3544 → 0.354 | ✅ |
| CKA-only 7B GSM8K | 64.39% | multi-seed mean (Tab2) | 64.39 | ✅ |
| Standard 7B Peak Rew | 0.081 | `grpo_standard_20_fair` | 0.081 | ✅ |
| Standard 7B GSM8K | 59.84% | multi-seed mean (Tab2) | 59.84 | ✅ |
| RASP 7B Peak Rew | 0.061 | `grpo_rasp_20_fair` | 0.061 | ✅ |
| RASP 7B GSM8K | 60.88% | `eval_gsm8k_grpo_rasp_20_fair` | 0.6088 | ✅ |
| Random 7B Peak Rew | 0.190 | `grpo_random_20` | 0.19 | ✅ |
| Random 7B GSM8K | -- | N/A | 实际可用 (50.72%) 但未填 | ⚠️ 有意省略 |
| CKA-only 1.5B Rew | 0.238 | `grpo_cka_only_20_1p5b` | reward_mean: 0.2375 → 0.238 | ✅ |
| CKA-only 1.5B GSM8K | 35.48% | `eval_gsm8k_grpo_cka_only_20_1p5b` | 0.3548 | ✅ |
| Standard 1.5B Rew | 0.084 | `grpo_standard_20_1p5b` | reward_mean: 0.0844 → 0.084 | ✅ |
| Standard 1.5B GSM8K | 22.29% | `eval_gsm8k_grpo_standard_20_1p5b` | 0.2229 | ✅ |
| RASP 1.5B Rew | 0.099 | `grpo_rasp_20_1p5b` | final_reward: 0.099 | ✅ |
| RASP 1.5B GSM8K | 26.16% | `eval_gsm8k_grpo_rasp_20_1p5b` | 0.2616 | ✅ |

**注**: Random 7B GSM8K 为 "--"。该值在 Tab2 中可用 (50.72%), 但因 Random 无 1.5B 实验, 省略以保持 cross-scale 对比的完整性。语义合理。

**Caption 验证**: "7B reward = peak" — 7B 列确实用 peak_reward ✓; "1.5B reward = mean" — 1.5B 列用 reward_mean ✓。

**小结**: 13/13 ✅ (Random GSM8K "--" 为有意省略)。Bold 正确 ✓。

---

### tab_cka_stability.tex (2 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Spearman ρ (min) | 0.964 | `cka_scoring_stability_ablation` | min_combined_rho: 0.964 | ✅ |
| Spearman ρ (mean) | 0.979 | `cka_scoring_stability_ablation` | mean_combined_rho: 0.979 | ✅ |

**Caption 验证**: "High correlation (ρ ≥ 0.964)" — 正确引用 min 值 ✓。

**小结**: 2/2 ✅。

---

### tab_math500.tex (docs/paper/tables — 31 cells incl. Δ)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Dense | 53.0%† | `eval_math500_dense_2048` | 0.53 | ✅ |
| **20% method comparison** | | | | |
| CKA-only SFT | 27.4% | `eval_math500_sft_cka_only_20_fixed_v2` | 0.274 | ✅ fixed |
| CKA-only GRPO | 27.6% | `eval_math500_grpo_cka_only_20_fixed` | 0.276 | ✅ fixed |
| CKA-only Δ | +0.2 | computed | 27.6−27.4=0.2 | ✅ |
| Standard SFT | 23.4% | `eval_math500_sft_standard_20_2048_v3` | 0.234 | ✅ 非 fixed |
| Standard GRPO | 27.0% | `eval_math500_grpo_standard_20_fixed` | 0.27 | ✅ fixed |
| Standard Δ | +3.6 | computed | 27.0−23.4=3.6 | ✅ |
| RASP SFT | 21.6% | `eval_math500_sft_rasp_alpha1p0_20_fixed` | 0.216 | ✅ fixed |
| RASP GRPO | 23.0% | `eval_math500_grpo_rasp_alpha1p0_20_fixed` | 0.23 | ✅ fixed |
| RASP Δ | +1.4 | computed | 23.0−21.6=1.4 | ✅ |
| Random SFT | 14.4% | `eval_math500_sft_random_20_v3` | 0.144 | ✅ 非 fixed |
| Random GRPO | 13.4% | `eval_math500_grpo_random_20_v3` | 0.134 | ✅ 非 fixed |
| Random Δ | −1.0 | computed | 13.4−14.4=−1.0 | ✅ |
| **α dose-response** | | | | |
| α=0.5 SFT | 25.4% | `eval_math500_sft_rasp_alpha0p5_20` | 0.254 | ✅ 非 fixed |
| α=0.5 GRPO | 24.8% | `eval_math500_grpo_rasp_alpha0p5_20` | 0.248 | ✅ 非 fixed |
| α=0.5 Δ | −0.6 | computed | 24.8−25.4=−0.6 | ✅ |
| α=2.0 SFT | 25.6% | `eval_math500_sft_rasp_alpha2p0_20_fixed` | 0.256 | ✅ fixed |
| α=2.0 GRPO | 27.4% | `eval_math500_grpo_rasp_alpha2p0_20_fixed` | 0.274 | ✅ fixed |
| α=2.0 Δ | +1.8 | computed | 27.4−25.6=1.8 | ✅ |
| α=3.0 SFT | 23.2% | `eval_math500_sft_rasp_alpha3p0_20` | 0.232 | ✅ 非 fixed |
| α=3.0 GRPO | 22.8% | `eval_math500_grpo_rasp_alpha3p0_20` | 0.228 | ✅ 非 fixed |
| α=3.0 Δ | −0.4 | computed | 22.8−23.2=−0.4 | ✅ |
| α=4.0 SFT | 26.6% | `eval_math500_sft_rasp_alpha4p0_20` | 0.266 | ✅ 非 fixed |
| α=4.0 GRPO | 26.2% | `eval_math500_grpo_rasp_alpha4p0_20` | 0.262 | ✅ 非 fixed |
| α=4.0 Δ | −0.4 | computed | 26.2−26.6=−0.4 | ✅ |
| **25% sparsity** | | | | |
| CKA-only 25% SFT | 19.2% | `eval_math500_sft_cka_only_25_v2` | 0.192 | ✅ 非 fixed |
| CKA-only 25% GRPO | 18.4% | `eval_math500_grpo_cka_only_25_v2` | 0.184 | ⚠️ 非 fixed; fixed 版本=17.6% |
| CKA-only 25% Δ | −0.8 | computed | 18.4−19.2=−0.8 | ✅ |
| Standard 25% SFT | 14.0% | `eval_math500_sft_standard_25` | 0.14 | ✅ 非 fixed |
| Standard 25% GRPO | 12.8% | ❌ **无 registry 实验** | — | ❌ 无法追溯 |
| Standard 25% Δ | −1.2 | computed | 12.8−14.0=−1.2 | ✅ (算术正确, 但 GRPO 源不明) |

**Caption 验证**:
- "CKA-only–Standard GRPO gap is 0.6 pp" → 27.6−27.0=0.6 ✓
- "vs. 4.6 pp on GSM8K" → 64.39−59.84=4.55 → 4.6 ✓ (四舍五入)
- "73.6% at 4096" → eval_math500_dense_unpruned=0.736 ✓

**⚠️ Fixed vs 非 fixed 混用问题**:

已使用 fixed eval 的 cell (8个): CKA-only 20% SFT/GRPO, Standard 20% GRPO, RASP 20% SFT/GRPO, α=2.0 SFT/GRPO

仍在使用旧 eval 的 cell (10个):
1. Standard 20% SFT — 无 fixed 版本
2. Random 20% SFT/GRPO — 无 fixed 版本
3. α=0.5 SFT/GRPO — 无 fixed 版本
4. α=3.0 SFT/GRPO — 无 fixed 版本
5. α=4.0 SFT/GRPO — 无 fixed 版本
6. CKA-only 25% SFT — 无 fixed 版本
7. CKA-only 25% GRPO — fixed 版本已有 (17.6%) 但表格仍用旧值 (18.4%)
8. Standard 25% SFT — 无 fixed 版本

**小结**: 29/31 ✅, 1 ⚠️ (CKA-only 25% GRPO 应更新为 fixed 值 17.6%), 1 ❌ (Standard 25% GRPO 12.8% 无 registry 来源)。精度 1dp 统一 ✓。Bold 正确 ✓。

---

### tab_mbpp.tex (13 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Dense GRPO | 53.48% | `eval_mbpp_dense_unpruned` | pass_at_1: 0.5348 | ✅ |
| CKA-only SFT | 12.83% | `eval_mbpp_sft_cka_only_20` | pass_at_1: 0.1283 | ✅ |
| CKA-only GRPO | 14.17% | `eval_mbpp_grpo_cka_only_20` | pass_at_1: 0.1417 | ✅ |
| CKA-only Δ | +1.34 | computed | 14.17−12.83=1.34 | ✅ |
| Standard SFT | 12.03% | `eval_mbpp_sft_standard_20_v4` | pass_at_1: 0.1203 | ✅ |
| Standard GRPO | 13.10% | `eval_mbpp_grpo_standard_20_v4` | pass_at_1: 0.131 | ✅ |
| Standard Δ | +1.07 | computed | 13.10−12.03=1.07 | ✅ |
| RASP SFT | 11.76% | `eval_mbpp_sft_rasp_20` | pass_at_1: 0.1176 | ✅ |
| RASP GRPO | 13.10% | `eval_mbpp_grpo_rasp_20` | pass_at_1: 0.131 | ✅ |
| RASP Δ | +1.34 | computed | 13.10−11.76=1.34 | ✅ |
| ShortGPT SFT | 10.43% | `eval_mbpp_sft_shortgpt_20_v2` | pass_at_1: 0.1043 | ✅ |
| ShortGPT GRPO | 14.44% | `eval_mbpp_grpo_shortgpt_20_v2` | pass_at_1: 0.1444 | ✅ |
| ShortGPT Δ | +4.01 | computed | 14.44−10.43=4.01 | ✅ |

**小结**: 13/13 ✅。精度 2dp 统一 ✓。

---

### paper/tables/tab_math500.tex (更新版, 含 truncation rate)

此版本结构不同 (Post-SFT / Post-GRPO 各有 Acc + Trunc 列), 大量 "--" 待填。仅审计有值 cell:

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Dense SFT Acc | 73.6% | `eval_math500_dense_unpruned` | 0.736 | ✅ |
| Dense SFT Trunc | 24.8% | `eval_math500_dense_unpruned` | 1−natural_eos_pct(0.752)=0.248 | ✅ |
| Dense GRPO Acc | 69.0% | ❌ **无 registry 实验** | — | ❌ 无法追溯 |
| Dense GRPO Trunc | 17.2% | ❌ **无 registry 实验** | — | ❌ 无法追溯 |
| Standard GRPO Acc | 27.0% | `eval_math500_grpo_standard_20_fixed` | 0.27 | ✅ |
| CKA-only SFT Acc | 27.4% | `eval_math500_sft_cka_only_20_fixed_v2` | 0.274 | ✅ |
| CKA-only SFT Trunc | 23.2% | `eval_math500_sft_cka_only_20_fixed_v2` | truncated_pct: 0.232 | ✅ |
| CKA-only GRPO Acc | 27.6% | `eval_math500_grpo_cka_only_20_fixed` | 0.276 | ✅ |
| RASP SFT Acc | 21.6% | `eval_math500_sft_rasp_alpha1p0_20_fixed` | 0.216 | ✅ |
| RASP GRPO Acc | 23.0% | `eval_math500_grpo_rasp_alpha1p0_20_fixed` | 0.23 | ✅ |
| RASP GRPO Trunc | 36.0% | `eval_math500_grpo_rasp_alpha1p0_20_fixed` | 180/500=0.36 | ✅ |
| α=2.0 SFT Acc | 25.6% | `eval_math500_sft_rasp_alpha2p0_20_fixed` | 0.256 | ✅ |
| α=2.0 SFT Trunc | 31.0% | `eval_math500_sft_rasp_alpha2p0_20_fixed` | truncated_pct: 0.31 | ✅ |
| α=2.0 GRPO Acc | 27.4% | `eval_math500_grpo_rasp_alpha2p0_20_fixed` | 0.274 | ✅ |
| α=2.0 GRPO Trunc | 30.2% | `eval_math500_grpo_rasp_alpha2p0_20_fixed` | truncated_pct: 0.302 | ✅ |
| CKA-only 25% GRPO Acc | 17.6% | `eval_math500_grpo_cka_only_25_fixed` | 0.176 | ✅ fixed |
| CKA-only 25% GRPO Trunc | 26.6% | `eval_math500_grpo_cka_only_25_fixed` | truncated_pct: 0.266 | ✅ |

**注**: 此版本 CKA-only 25% GRPO 已更新为 fixed 值 17.6% (docs 版仍用 18.4%)。

**小结**: 15/17 有值 cell ✅, 2 ❌ (Dense GRPO Acc 69.0% 和 Trunc 17.2% 无 registry 来源)。`\label{tab:math500}` 与 docs 版重复, 编译时会冲突。

---

## 总结

| Table | 总 cell 数 | ✅ 已验证 | ⚠️ 需确认 | ❌ 问题 |
|-------|-----------|----------|----------|--------|
| tab1_recovery_gradient | 12 | 6 | 6 (W&B) | 0 |
| tab2_decoupling | 27 | 27 | 0 | 0 |
| table3_alpha | 15 | 15 | 0 | 0 |
| table4_sparsity_cliff | 8 | 8 | 0 | 0 |
| tab5_cross_scale | 13 | 13 | 0 | 0 |
| tab_cka_stability | 2 | 2 | 0 | 0 |
| tab_math500 (docs) | 31 | 29 | 1 | 1 |
| tab_mbpp | 13 | 13 | 0 | 0 |
| tab_math500 (paper/) | 17 | 15 | 0 | 2 |
| **合计** | **138** | **128** | **7** | **3** |

### 必须修复的问题 (❌)

1. **tab_math500 docs: Standard 25% GRPO = 12.8%** — 无 registry 实验可追溯。需确认来源或补跑 `eval_math500_grpo_standard_25_fixed`。

2. **tab_math500 paper/: Dense GRPO Acc = 69.0%, Trunc = 17.2%** — 无 registry 实验。需补跑 unpruned GRPO 模型的 MATH-500 评估并注册。

### 需要决策的问题 (⚠️)

3. **tab1 Mean Rew / Min f₀ (6 cells)** — 来自 W&B 训练曲线聚合, registry 仅有 peak/final 值。建议从 W&B 提取并注册为 metrics (或在 caption 注明来源)。

4. **tab_math500 docs: CKA-only 25% GRPO** — 旧值 18.4% vs fixed 值 17.6%。paper/ 版本已更新, docs 版本需同步更新为 17.6%。

5. **tab_math500 fixed/非 fixed 混用** — 10 个 cell 仍用旧 eval (α=0.5/3.0/4.0 全部, Standard SFT, Random SFT/GRPO, 25% sparsity 部分)。如果 fixed eval 是最终协议, 这些需要补跑。

---
