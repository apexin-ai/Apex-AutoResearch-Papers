# verify final partA D

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_final_partA_D_20260523T191636_result.json`
- **Structured JSON:** [`95edda8ec73e3a3538d4.json`](../../sessions/95/95edda8ec73e3a3538d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。现在系统性核对所有数据点。

---

## Part A: Registry 交叉核对

### Table 1 (Main PPL, ρ=0.4, τ=0.7)

**Uniform 3-seed:**
- [Uniform seed42=17.694] 无对应 registry entry (qwen06b_uniform_seed42 仍 RUNNING) ⚠️ 无法追溯
- [Uniform seed123=17.686] exp_id=uniform_ood_seed123: 论文值=17.686, registry=17.686 ✅
- [Uniform seed456=17.702] exp_id=uniform_ood_seed456: 论文值=17.702, registry=17.702 ✅
- [Uniform mean=17.694±.008] 计算: (17.694+17.686+17.702)/3=17.694, SD=0.008 ✅

**Adaptive b* 3-seed (τ=0.7):**
- [Adaptive seed42=17.680] 无 registry entry (τ=0.7 实验未注册) ⚠️ 无法追溯
- [Adaptive seed123=17.666] 无 registry entry ⚠️
- [Adaptive seed456=17.677] 无 registry entry ⚠️
- [Adaptive mean=17.674±.007] 计算: (17.680+17.666+17.677)/3=17.6743≈17.674, SD≈0.007 ✅ 内部一致
- [Δ=-0.020] 17.674-17.694=-0.020 ✅

**Grid (b=0.3) 3-seed:**
- [Grid seed42=17.640] appendix grid table 确认 b=0.3→17.640 ✅
- [Grid seed123=17.579] exp_id=grid_b0_3_seed123: registry=17.58, 论文=17.579 ⚠️ registry 仅 2dp，差 0.001
- [Grid seed456=17.640] exp_id=grid_b0_3_seed456: registry=17.64, 论文=17.640 ✅
- [Grid mean=17.620±.033] 计算: (17.640+17.579+17.640)/3=17.620 ✅; 从 rounded 值计算 SD≈0.035，论文说 0.033 (full precision 计算) ⚠️ 无法精确验证

**ESS-only 3-seed:**
- [ESS-only seed42=17.730] 无 registry entry (ess_only_seed42 未注册) ⚠️
- [ESS-only seed123=17.720] exp_id=ess_only_seed123: RUNNING，无指标 ⚠️
- [ESS-only seed456=17.760] exp_id=ess_only_seed456: RUNNING，无指标 ⚠️
- [ESS-only mean=17.737±.021] 计算: 17.737, SD=0.021 ✅ 内部一致

**Random U(0,2) 3-seed:**
- [Random seed42=17.830] 无 Qwen3 registry entry ⚠️ (registry 中 random_reweight_baseline_seed42 是 Qwen2.5，PPL=17.958); 间接验证: random_reweight_seed123_r5 notes 称 "seed42: +0.136"，17.694+0.136=17.830 ✅ 间接一致
- [Random seed123=17.800] exp_id=random_reweight_seed123_r5: registry=17.801, 论文=17.800 ⚠️ 差 0.001 (rounding)
- [Random seed456=17.777] exp_id=random_reweight_seed456: RUNNING ⚠️ 无法验证
- [Random mean=17.802±.027] 计算: 17.802, SD=0.027 ✅ 内部一致

**Golden Ratio:**
- [Golden Ratio seed42=17.654] 无 registry entry ⚠️ 无法追溯

**Detect & Remove (q>0.3):**
- [D&R seed42=17.250, seed123=17.250, seed456=17.251, mean=17.250±.001] 无 registry entry (detect_remove_q03_seed42 标记为训练失败) ⚠️ 数据源不明

---

### Epoch-Match Table (D&R q>0.5)

**D&R full (q>0.5) 3-seed:**
- [D&R full seed42=17.285] exp_id=detect_remove_q05_v2_seed42: registry=17.2853→17.285 ✅
- [D&R full seed123=17.272] exp_id=detect_remove_q05_v2_seed123_r2: registry=17.2723→17.272 ✅
- [D&R full seed456=17.277] 无 registry entry ⚠️; memory.md 记录=17.277 ✅
- [D&R full mean=17.278±.007] memory.md=17.278±.007 ✅

**D&R epoch-matched 3-seed:**
- [Epoch-matched seed42=17.651, seed123=17.659, seed456=17.660, mean=17.657±.005] memory.md 完全一致 ✅; 无 registry entry ⚠️

---

### Table 2 / Detector Decision Summary

**N-gram:**
- [AUC=0.73] 无独立 registry 验证 ⚠️
- [ECE=0.069] appendix detector table 确认 ✅
- [Δ PPL=+0.129] 17.823-17.694=0.129 ✅; registry ngram_adaptive=17.82, vs_ngram_uniform="+0.13" ✅

**GPT-2:**
- [AUC=0.91] 无独立 registry 验证 ⚠️
- [ECE=0.131] appendix detector table 确认 ✅
- [Δ PPL=+0.098] 17.792-17.694=0.098 ✅

**TF-IDF:**
- [AUC=0.94] paper_provenance=0.939 ⚠️ 论文 round 到 0.94; appendix detector table=0.94 ✅
- [ECE=0.048] appendix detector table=0.048 ✅; experiments.tex 写 "0.05" ⚠️ 精度不一致 (Part D)
- [Δ PPL=-0.020 (τ=0.7 main)] Table 1 Δ=-0.020 ✅; detector table (τ=0.8) Δ=-0.044 ✅ (不同 τ，正确)

---

### Batch-size Amplification

**B=4:**
- [Δ=-0.020±0.008] memory.md 确认 ✅

**B=8:**
- [Δ=-0.050 (2-seed mean)] memory.md: seed42 Δ=-0.044, seed123 Δ=-0.056, mean=-0.050 ✅
- [seed42: adaptive=17.650, uniform=17.694] memory.md 确认 ✅; registry bs8_auto_nmin_r5=17.66 ⚠️ 不匹配 (不同实验 run，bs8_auto_nmin vs bs8_nmin4_adaptive)
- [seed123: adaptive=17.631, uniform=17.687] memory.md 确认 ✅; 无 registry entry

**B=16:**
- [Δ=-0.068±0.005 (3 seeds)] memory.md: adaptive=17.631±0.008, uniform=17.694±0.015, Δ=-0.068±0.005 ✅
- [seed123] exp_id=bs16_adaptive_tau07_seed123_r2: registry holdout_ppl=17.616; memory 没有 per-seed B=16 数据 ⚠️

---

### Constraint Regime (τ=0.7)

- [ρ=0.4: 50.9% α_eff / 43.3% ESS / 5.8% clean] 论文 results.tex:126 + appendix:144 一致 ✅; 来自 step_metrics 分析，无 registry 验证 ⚠️
- [ρ=0.6: 46.8% α_eff / 48.7% ESS / 4.5% clean] appendix:145 确认 ✅; 同上 ⚠️
- [Sharpening ratio 5.8×] introduction:22 引用; 需 α_eff-binding batches 的 b* 数据验证。论文说 adaptive mean b*=1.4, ESS-only=3.5-5.9。整体比例 5.9/1.4=4.2×≠5.8×。5.8× 可能是 α_eff-binding batches 子集的比例 ⚠️ 无法独立验证

---

### ρ Sensitivity

**ρ=0.2:**
- [Δ=+0.046] 论文 discussion:11 + appendix rho02:392 一致 ✅; registry rho02_adaptive_tau09_r5 给出 +0.114 但那是 τ=0.9 (不同配置) ⚠️; τ=0.8 的 rho02 实验 (rho02_adaptive_tau08_seed42) 仍 RUNNING

**ρ=0.3:**
- [Δ=+0.002 (3-seed)] appendix rho03 table + memory.md 完全一致 ✅
  - seed42: A=17.422, U=17.422, Δ=0.000 ✅
  - seed123: A=17.435, U=17.433, Δ=+0.002 ✅
  - seed456: A=17.424, U=17.419, Δ=+0.005 ✅

**ρ=0.6:**
- [Δ=-0.032, p=0.009] appendix rho06 table 确认:
  - seed42: A=17.735, U=17.766, Δ=-0.031
  - seed123: A=17.727, U=17.754, Δ=-0.027
  - seed456: A=17.732, U=17.770, Δ=-0.038
  - Mean Δ=-0.032 ✅
  - **p 值不一致**: 主文 results.tex:94 写 p=0.009; appendix rho06 caption:283 写 "3dp rounding yields t=−9.95, p=0.010" ❌ 同一计算给出不同 p 值
  - 独立验证: t=-9.95, df=2 → two-sided p=0.010, 非 0.009 ❌ 主文 p=0.009 错误

---

### 1.7B Scale

- [Adaptive 13.26, Uniform 13.28, Δ=-0.013] ❌ **严重不一致**
  - exp_id=eval_adaptive_1_7b_v2: registry=13.27 (≠论文 13.26)
  - exp_id=eval_uniform_1_7b_v3: registry=13.50 (≠论文 13.28，差 0.22!)
  - memory.md: "adaptive PPL=13.27 vs uniform PPL=13.50, Δ=-0.23"
  - 论文声称 "3 seeds" 但 report.md 显示 eval_adaptive_1_7b_seed123 / eval_uniform_1_7b_seed123 仍为 "准备中"
  - **论文 Δ=-0.013 与所有可追溯数据 (Δ=-0.23 single seed) 严重矛盾**

---

### Downstream

- [Mean accuracy=0.5414 for both] 无法从 registry 完整验证 ⚠️; registry adaptive_fix_seed42 downstream 值与 appendix per-seed 值不完全一致（可能不同 eval 配置）

---

### 统计量重算

**ρ=0.4 paired t-test:**
- 从 3dp per-seed: Δ=(-0.014, -0.020, -0.025), mean=-0.0197, SD=0.00551, t=-6.19
- 论文说 t=-7.1 (full precision 计算), p=0.019 → 对 t=-7.1, df=2: p≈0.019 ✅
- p_BH=0.078 (k=9): 无法独立验证（需全部 9 个 p 值）⚠️
- Bootstrap CI [-0.028, -0.012]: 论文已标注无法独立验证 ⚠️

**ρ=0.6 paired t-test:**
- 从 3dp per-seed: Δ=(-0.031, -0.027, -0.038), mean=-0.032, SD=0.00557, t=-9.95
- t=-9.95, df=2 → p=0.010
- 论文主文 p=0.009 ❌, appendix p=0.010 ✅

**Cohen's d = 2.86:**
- 从 paired Δ: d = |mean|/SD_paired = 0.020/0.00551 = 3.63 (rounded values)
- 若用 pooled group SD: SD_pooled ≈ 0.007, d = 0.020/0.007 = 2.86 ✅
- 注意: 2.86 用的是 pooled group SD，不是 paired difference SD；若标注为 "paired"，定义需要明确

**BH correction k=9:**
- 论文 ρ=0.4: p_BH=0.078; ρ=0.6: p_BH=0.064
- 无法验证（需全部 9 个 uncorrected p 值）⚠️

---

## Part D: 精度一致性

### PPL 值 (应统一 3dp)

- [results.tex:101] `13.26` → 应为 `13.260` ⚠️ 2dp 不一致
- [results.tex:101] `13.28` → 应为 `13.280` ⚠️ 2dp 不一致
- [appendix:199] dr_threshold 表 `17.40` → 应为 `17.400` ⚠️
- [appendix:200] `17.27` → 应为 `17.270` ⚠️
- [appendix:203] `17.28` → 应为 `17.280` ⚠️
- [appendix:204] `17.30` → 应为 `17.300` ⚠️
- [appendix:205] `17.32` → 应为 `17.320` ⚠️
- [appendix:206] `17.34` → 应为 `17.340` ⚠️
- [appendix:207] `17.42` → 应为 `17.420` ⚠️
- [appendix:199] `18.04` → 应为 `18.040` ⚠️
- [appendix:201] `17.74` → 应为 `17.740` ⚠️
- [appendix:203] `17.65` → 应为 `17.650` ⚠️
- [appendix:205] `17.62` → 应为 `17.620` ⚠️

### p 值 (应统一 3dp)

- [results.tex:94] `p=0.009` vs [appendix:283] `p=0.010` ❌ 同一统计量不一致
- 其余 p 值 (0.019, 0.009 in abstract) 均 3dp ✅

### ECE (精度不一致)

- [experiments.tex:8] `ECE=0.05` (2dp) vs [appendix detector table:349] `ECE=0.048` (3dp) ⚠️ 同一数值不同精度

### Δ PPL (应统一 3dp)

- [discussion.tex:5] `+0.26` → 应为 `+0.257` ⚠️ 2dp 不一致

### 百分比 (应统一 1dp)

- 所有百分比 (50.9%, 43.3%, 5.8%, 46.8%, 48.7%, 4.5%, 46.3%) ✅ 均为 1dp

---

## 关键问题汇总

| 严重度 | 问题 | 位置 |
|--------|------|------|
| ❌ **严重** | 1.7B 数据与 registry 严重矛盾: 论文 Δ=-0.013 (adaptive=13.26, uniform=13.28), registry/memory Δ=-0.23 (adaptive=13.27, uniform=13.50); 论文声称 3-seed 但实验尚未完成 | results.tex:100-101 |
| ❌ | ρ=0.6 p 值不一致: 主文写 p=0.009, appendix 同一计算写 p=0.010; 独立验算确认 p=0.010 | results.tex:94 vs appendix:283 |
| ⚠️ | D&R (q>0.3) Table 1 数据 (17.250±.001) 无 registry entry 可追溯 | results.tex:65 |
| ⚠️ | τ=0.7 adaptive per-seed 值 (17.680/17.666/17.677) 无 registry entry | results.tex:60 |
| ⚠️ | Random U(0,2) seed42=17.830 和 seed456=17.777 无 Qwen3 registry entry | results.tex:62 |
| ⚠️ | 1.7B PPL 2dp (13.26/13.28) 违反全文 3dp 精度约定 | results.tex:101 |
| ⚠️ | Appendix dr_threshold 表 11 个 PPL 值为 2dp，与全文 3dp 约定不一致 | appendix:199-208 |
| ⚠️ | ECE 精度不一致: experiments.tex 写 0.05, detector table 写 0.048 | experiments.tex:8 |
| ⚠️ | discussion.tex Δ=+0.26 应为 +0.257 (3dp) | discussion.tex:5 |

**最优先修复**: 1.7B 数据需要核实——如果 3-seed 实验确实未完成，论文不能声称 "3 seeds"；如果已有新数据使 Δ 从 -0.23 变为 -0.013，需要更新 registry。ρ=0.6 的 p=0.009→0.010 需要统一。

---
