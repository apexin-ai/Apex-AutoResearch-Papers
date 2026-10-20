# Round 10 Data Compilation & Consistency Check

> 编译时间: 2026-05-16 | 编译人: Worker (data compilation agent) | 数据源: experiment registry (120 experiments, all DONE)

---

## 1. 数据总表

### A. II Dose Curve — DeepSeek Importance (n=50, MATH-500, bf16)

| Sparsity | PPI_low_median | PPI_high_median | paired_median_diff | Cohen's d_z | Wilcoxon p | n_paired |
|----------|---------------|-----------------|-------------------|-------------|------------|----------|
| s015 | 0.3155 | 0.000120 | 0.3925¹ | 0.44² | <0.005 (Bonferroni) | 49 |
| s020 | 1.1280 | 0.0036 | 1.4818¹ | — | <0.005 | 49 |
| s025 | 3.9546 | 0.009873 | 7.1636¹ | — | <0.005 | 49 |
| s030 | 9.9731 | 0.0343 | 14.5861¹ | 0.80² | <0.005 | 49 |

¹ median_diff 来自 aggregate bootstrap，非 per-problem paired 计算。paper_framing 引用值 (0.32→1.15→3.97→9.94) 更接近 PPI_low_median，见一致性检查 §3.1。
² Cohen's d_z 仅 s015 和 s030 端点引用于 paper_framing。

**来源**: bf16_importance_s015, bf16_importance_s020, bf16_importance_s025, bf16_importance_s030

---

### B. II Dose Curve — DeepSeek Importance (n=500, MATH-500)

| Sparsity | median_II | 95% CI | Wilcoxon p | d_z (step) |
|----------|-----------|--------|------------|------------|
| s015 | 0.3907 | [0.3496, 0.4431] | 1.27e-70 | — |
| s020 | 1.2149 | [1.1072, 1.3365] | 3.98e-75 | −0.925 (s015→s020) |
| s025 | 3.9857 | [3.5272, 4.3588] | 1.99e-78 | −0.824 (s020→s025) |
| s030 | 8.4813 | [7.7543, 9.6919] | 1.09e-79 | −0.773 (s025→s030) |

**Random masking (n=500)**:

| Sparsity | median_II | Bonferroni p | Significant? |
|----------|-----------|-------------|-------------|
| s015 | 0.0139 | — | NS (p=0.863) |
| s020 | 0.0315 | — | NS (p=0.280) |
| s025 | 0.2574 | 0.0058 | ✅ |
| s030 | 0.5096 | 0.0059 | ✅ |

- dose_response_monotonic = **True**, Spearman ρ = **1.0**, perm_p = 0.0417
- imp/rand ratio range: **15.5–38.6×**
- effective_n = 496, mid_null_rate = 10.2%

**来源**: c2_n500_deepseek

---

### C. II Dose Curve — Qwen Importance (n=50, MATH-500, bf16)

| Sparsity | paired_median_diff | Cohen's d | Wilcoxon p | bootstrap CI 95% | n_paired |
|----------|-------------------|-----------|------------|------------------|----------|
| s015 | 0.04762 | 0.3705 | 0.0296 | [−0.005, 0.110]³ | 46 |
| s020 | 0.20751 | 0.7224 | 3.4e-05 | [0.067, 0.402] | 46 |
| s025 | 1.10871 | 1.2329 | <1e-15 | [0.609, 1.469] | 46 |
| s030 | 2.61939 | 1.4394 | <1e-15 | [1.722, 3.651] | 46 |

³ s015 CI 跨零 → onset threshold s≥0.20 (S3→C confirmed)

**来源**: bf16_qw_imp_s015, bf16_qw_imp_s020, bf16_qw_imp_s025, bf16_qw_imp_s030

### C-2. II Dose Curve — Qwen Importance (n=500, MATH-500)

| Sparsity | median_II | 95% CI | Bonferroni p | d_z (step) |
|----------|-----------|--------|-------------|------------|
| s015 | 0.0659 | [0.0492, 0.0925] | 3.46e-14 | — |
| s020 | 0.3073 | [0.2612, 0.3564] | 2.74e-41 | −0.629 |
| s025 | 1.0745 | [0.9766, 1.1787] | 4.25e-68 | −0.865 |
| s030 | 3.1550 | [2.7834, 3.5582] | 3.69e-73 | −0.767 |

**Random masking (n=500)**:

| Sparsity | median_II | Bonferroni p | Significant? |
|----------|-----------|-------------|-------------|
| s015 | −0.0111 | 0.687 | NS |
| s020 | 0.0153 | 0.800 | NS |
| s025 | 0.3931 | 6.37e-11 | ✅ |
| s030 | 0.9127 | 1.17e-14 | ✅ |

- dose_response_monotonic = **True**, Spearman ρ = **1.0**, perm_p = 0.0417
- imp/rand ratio range: **2.7–20.1×**
- effective_n = 475, mid_null_rate = 45.2%

**来源**: c2_qw_n500_r3

---

### D. Random vs Importance — DeepSeek (n=50)

| exp_id | Strategy | Sparsity | II_low_median | II_high_median | median_diff | Significant? |
|--------|----------|----------|--------------|----------------|-------------|-------------|
| bf16_importance_s020 | importance | s020 | 1.4963 | 0.0145 | 1.4818 | ✅ PASS |
| bf16_ds_rand_s020 | random | s020 | 0.2763 | 0.2918 | −0.0155 | ❌ FAIL |
| bf16_importance_s025 | importance | s025 | 7.1960 | 0.0324 | 7.1636 | ✅ PASS |
| bf16_ds_rand_s025 | random | s025 | 1.3627 | 0.8182 | 0.5445 | ❌ FAIL |
| v6_random_s025 | random | s025 | 2.9146 | 3.0024 | −0.1199 | ❌ FAIL (CI [−1.52, 1.25]) |
| v6_random_s030 | random | s030 | — | — | — | ❌ FAILED (SIGTERM) |

**Qwen Random (n=50)**:

| exp_id | Sparsity | median_diff | Wilcoxon p | Significant? |
|--------|----------|-------------|------------|-------------|
| bf16_qw_rand_s015 | s015 | −0.029 | 0.863 | NS |
| bf16_qw_rand_s020 | s020 | 0.129 | 0.149 | NS |

**来源**: bf16_ds_rand_s020, bf16_ds_rand_s025, v6_random_s025, v6_random_s030, bf16_qw_rand_s015, bf16_qw_rand_s020

---

### E. GSM8K Cross-Benchmark Validation (C10)

**DeepSeek Importance — median_gradient (n=50, GSM8K)**:

| Sparsity | median_gradient | CI | Wilcoxon p | imp/rand ratio |
|----------|----------------|-----|------------|----------------|
| s015 | 0.241 | [0.077, 0.478] | 0.0003 | 2.3× |
| s020 | 0.740 | [0.314, 1.119] | 0.0001 | 2.5× |
| s025 | 1.992 | [0.933, 2.820] | 0.0001 | 3.8× |
| s030 | 4.682 | [2.121, 10.557] | 0.0001 | 2.8× |

dose_response_monotonic = **True**

**Qwen Importance — median_gradient (n=50, GSM8K)**:

| Sparsity | median_gradient |
|----------|----------------|
| s015 | 0.039 |
| s020 | 0.158 |
| s025 | 1.100 |
| s030 | 2.092 |

**Qwen Random — GSM8K (v2 bug-fixed)**:

| exp_id | Sparsity | ii_low_median | ii_high_median | gradient (low−high) |
|--------|----------|--------------|----------------|-------------------|
| gsm8k_qw_rand_s025_v2 | s025 | 1.459 | 0.718 | 0.741 |
| gsm8k_qw_rand_s030_v2 | s030 | 5.200 | 2.310 | 2.890 |

⚠️ QW random gradient 在 GSM8K 上 s030 > importance gradient (2.89 vs 2.09)。paper_framing 已注明"反转仅在原始 II_low 值上"。

**来源**: gsm8k_profiling_ds, gsm8k_profiling_qw, gsm8k_qw_rand_s025_v2, gsm8k_qw_rand_s030_v2

---

### F. QW Accuracy Dose Curve (n=100 combined, 8k tokens, MATH-500)

| Sparsity | Combined acc | n | Δ vs dense | Status |
|----------|-------------|---|------------|--------|
| dense | 0.46 (46/100) | 100 | — | ✅ |
| s015 | 0.36 (36/100) | 100 | −0.10 | ✅ |
| s020 | 0.36 (36/100) | 100 | −0.10 | ✅ |
| s025 | 0.33 (33/100) | 100 | −0.13 | ✅ |
| s030 | 0.19 (19/100) | 100 | −0.27 | ✅ |

✅ **Batch1 v2 rescore 完成** (2026-05-16): 全部 5 conditions 用 max_new_tokens=8192 重跑。QW truncation rate ≤4%，combined values 不变。此为最终权威值。

**来源**: acc_qw_dense_b1_8k, acc_qw_s015_n100, acc_qw_s020_n100_b2_fix, acc_qw_s025_n100, acc_qw_s030_n100 等

---

### G. DS 8k Accuracy Dose Curve (n=50, 8k tokens, MATH-500, v2)

| Sparsity | Accuracy | n | Δ vs dense | Truncation rate | Non-trunc acc |
|----------|----------|---|------------|-----------------|---------------|
| dense | 0.74 (37/50) | 50 | — | 0.16 | — |
| s015 | 0.48 (24/50) | 50 | −0.26 | 0.32 | 0.706 |
| s020 | 0.30 (15/50) | 50 | −0.44 | 0.56 | 0.682 |
| s025 | 0.08 (4/50) | 50 | −0.66 | 0.76 | — |
| s030 | 0.04 (2/50) | 50 | −0.70 | 0.76 | 0.167 |

D089 结论: s≤0.20 以截断驱动（non-trunc acc ~70% 稳定），s025+ truncation 压倒性（non-trunc acc 也崩溃至 16.7%）。
D086: DS accuracy 数据**降为定性观察**，QW 作为 accuracy dose-response 主证据。

**来源**: acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2

---

### H. Mechanism — Discrimination Collapse (C4)

**DeepSeek (c4_entropy, n=30)**:

| Metric | s015 | s020 | s025 | s030 | Direction |
|--------|------|------|------|------|-----------|
| imp_entropy_delta | −0.040 | −0.047 | −0.045 | −0.044 | ↓ consistent |
| rand_entropy_delta | +0.128 | +0.136 | +0.217 | +0.233 | ↑ consistent |
| imp_gini_delta | −0.030 | −0.040 | −0.065 | −0.081 | ↓ monotonic |
| rand_gini_delta | −0.031 | −0.040 | −0.062 | −0.073 | ↓ monotonic |
| imp_cv_delta | −0.564 | −0.774 | −1.287 | −1.665 | ↓ monotonic |
| rand_cv_delta | −1.021 | −1.203 | −1.923 | −2.137 | ↓ monotonic |

**Qwen (qwen_c4_entropy, n=30, conclusion=negative)**:

| Metric | s015 | s020 | s025 | s030 | Direction |
|--------|------|------|------|------|-----------|
| imp_entropy_delta | −0.073 | −0.076 | **+0.045** | −0.007 | ⚠️ s025 反转 |
| rand_entropy_delta | +0.084 | +0.090 | +0.217 | +0.197 | ↑ consistent |
| imp_gini_delta | −0.010 | −0.012 | −0.010 | −0.020 | ↓ weaker |
| imp_cv_delta | −0.045 | −0.208 | −1.491 | −1.142 | ↓ non-monotonic |

**结论**: Gini/CV 下降跨模型一致（discrimination collapse confirmed）。Entropy collapse DeepSeek 一致但 Qwen s025 方向反转 → entropy redistribution 为 model-dependent secondary effect。

### H-2. Per-Phase Gini Decomposition (C5, c5_per_phase_gini, ✅ 完成)

**QW importance (n=30, 已完成)**:

| Sparsity | global_delta | low_delta | mid_delta | high_delta |
|----------|-------------|-----------|-----------|------------|
| s015 | −0.0103 | **−0.0165** | −0.0094 | −0.0120 |
| s020 | −0.0121 | **−0.0200** | −0.0115 | −0.0143 |
| s025 | −0.0100 | **−0.0286** | −0.0168 | −0.0207 |
| s030 | −0.0202 | **−0.0350** | −0.0183 | −0.0239 |

Key finding: low phase Gini delta 在所有 sparsity 下一致最大（粗体），且单调递增 (−0.017→−0.035)。直接支撑 discrimination collapse 假说。

**QW random (n=30, 已完成)**:

| Sparsity | global_delta | low_delta | mid_delta | high_delta |
|----------|-------------|-----------|-----------|------------|
| s015 | −0.0186 | −0.0083 | −0.0038 | −0.0036 |
| s020 | −0.0229 | −0.0119 | −0.0053 | −0.0067 |
| s025 | −0.0337 | −0.0014 | −0.0081 | +0.0045 |
| s030 | −0.0447 | −0.0221 | −0.0077 | −0.0061 |

Random 的 low delta 无一致最大模式，且 s025 high 甚至正向。与 importance 形成对比。

**DS importance (n=30, 已完成)**:

| Sparsity | global_delta | low_delta | mid_delta | high_delta |
|----------|-------------|-----------|-----------|------------|
| s015 | −0.0301 | **−0.0163** | −0.0073 | −0.0152 |
| s020 | −0.0404 | **−0.0209** | −0.0092 | −0.0200 |
| s025 | −0.0647 | **−0.0313** | −0.0133 | −0.0267 |
| s030 | −0.0806 | **−0.0373** | −0.0183 | −0.0314 |

DS importance low delta 同样单调递增 (−0.016→−0.037)，跨模型一致。

**DS random (n=30, 已完成)**:

| Sparsity | global_delta | low_delta | mid_delta | high_delta |
|----------|-------------|-----------|-----------|------------|
| s015 | −0.0309 | −0.0102 | −0.0006 | −0.0062 |
| s020 | −0.0403 | −0.0120 | −0.0007 | −0.0085 |
| s025 | −0.0620 | −0.0150 | −0.0096 | −0.0112 |
| s030 | −0.0732 | −0.0183 | −0.0093 | −0.0138 |

**来源**: c5_per_phase_gini

---

### I. Cross-Architecture — LLaMA (C8, c3_llama, n=50)

| Metric | s015 | s020 | s025 | s030 |
|--------|------|------|------|------|
| imp_vs_rand d_z | 0.19 | 0.26 | 0.29 | 0.34 |
| within-imp phase d_z | ~1.0 | ~1.0 | ~1.0 | ~1.0 |
| Bonferroni sig? | NS | NS | NS | ✅ (p=0.029) |

- Qualitative direction consistent ✓
- imp_vs_rand 交互弱（仅 s030 显著）⚠️
- Random 在 LLaMA 上也显示 phase gradient (d_z 0.35→0.44) — 与 DS/QW 的 random NS 模式不同

---

### J. Mitigation Pilot (C5b, c5b_pilot, n=30, s025)

| Condition | median_II | Recovery % | 95% CI | Wilcoxon p |
|-----------|-----------|------------|--------|------------|
| Uniform | 1.044 | — | — | — |
| Oracle | 0.856 | 18% | [−39, +46] | 0.0021 |
| Heuristic | 0.713 | 32% | [−23, +66] | 0.0236 |

**Gate**: oracle_recovery > 30% → **FAIL** (18% < 30%)
**Decision**: D057 降为 future work

---

### K. Supporting Experiments

| exp_id | Claim | Status | Key Result |
|--------|-------|--------|------------|
| think_phase_validation | C1 (R9) | ✅ success | median κ = 0.887; think→low_sparsity=57.8%, answer→high_sparsity=62.7% |
| sf5_asymmetric_spot | robustness | ✅ success | Phase gradient II_low >> II_high under asymmetric allocation (19.13, 18.25) |
| appendix_b_precise_gx | G× 修正 | ❌ 未在 registry | D082 记录 G× 下修 58-241× → 21-64×，但无对应实验条目 |
| c10_lang_switching | C10 supplement | ✅ success | 语言切换率 0%→4%→40% (dense→s015→s030)，单调递增。中文 acc 极低 (s030: 10%) |

---

### L. Language Switching Analysis (c10_lang_switching)

| Sparsity | switch_rate | cn_count | en_count | cn_acc | en_acc |
|----------|------------|----------|----------|--------|--------|
| dense | 0% | 0 | 50 | — | 0.52 |
| s015 | 4% | 2 | 48 | 0.00 | 0.375 |
| s030 | 40% | 20 | 30 | 0.10 | 0.10 |

⚠️ 仅覆盖 dense/s015/s030（s020/s025 缺 gen_snippet 数据，Worker 准备中）。
趋势：语言切换率随 sparsity 单调递增，中文回复 accuracy 远低于英文。

**来源**: c10_lang_switching

---

## 2. Claim-Evidence Matrix

| Claim | Status | Primary Evidence | Supporting Evidence | 数据完整? |
|-------|--------|-----------------|--------------------|---------| 
| C1: Strategy × task modulation | confirmed | MATH-500 imp/rand 15-36× (n=500) | GSM8K ratio 2.3-3.8× (C10) | ✅ |
| C2: Phase modulation (low > high) | confirmed | DS n=50: 0.32→9.94 (4-point monotonic) | n=500: 0.39→8.48, Bonferroni全显著 | ✅ |
| C3: Phase-strategy crossover | confirmed | s025: imp_high=0.032 < rand=0.818; imp_low=7.196 > rand=1.363 | n=500 crossover pattern 复现 | ✅ |
| C4: Discrimination collapse | partially | c4_entropy: Gini/CV↓ 跨模型一致 | c5_per_phase_gini: QW low phase delta 单调递增 (−0.017→−0.035) | ✅ (entropy → model-dependent) |
| C5: Cross-model generalization | confirmed | DS + QW 方向一致, gradient ρ=1.0 | QW magnitude ~1/4 DS, onset s≥0.20 | ✅ |
| C5b: Phase-aware mitigation | future_work | c5b_pilot gate_failed (18% < 30%) | — | ✅ (correctly scoped to §6) |
| C6: Sub-exponential growth | confirmed | Δ增长因子 3.8×→4.8×→2.0×（递减） | n=500 confirms | ✅ |
| C7: n=500 power validation | ✅ confirmed | c2_n500_deepseek + c2_qw_n500_r3 | 全 8 条件 Bonferroni 显著 | ✅ |
| C8: Cross-architecture (LLaMA) | partially | c3_llama n=49: within-imp d_z~1.0 | c8_llama_n250_fixed RUNNING (n=250 rerun) | ⚠️ 等 n=250 结果 |
| C9: Lethe/SparK differentiation | planned | Related Work §2 引用区分 | — | ✅ (不需实验) |
| C10: Cross-benchmark (GSM8K) | ✅ confirmed | DS 0.241→4.682; QW 0.039→2.092 | QW random s025+s030 completed; lang switching 0%→40% | ✅ |
| S3→C: Onset threshold model-dep | confirmed | QW s015 CI跨零, s020+ 显著 | DS s015+ 全显著 | ✅ |
| S7→C: Dose-response monotonicity | confirmed | Spearman ρ=1.0 (n=50 + n=500) | 6-point dose-response | ✅ |

---

## 3. Consistency Checklist

### 3.1 数值一致性

| 检查项 | 状态 | 详情 |
|--------|------|------|
| DS dose curve 引用值 vs registry | ⚠️ | paper_framing: 0.32→1.15→3.97→9.94; PPI_low_median: 0.316→1.128→3.955→9.973。s020 差 0.02 (1.13 vs 1.15), s030 差 0.03 (9.97 vs 9.94)。可能因 paired subtraction 差异，需确认计算方式 |
| QW dose curve 引用值 vs registry | ✅ | 0.048→0.208→1.109→2.619 vs 0.04762→0.20751→1.10871→2.61939，精确匹配 |
| G× 值 21-64× | ⚠️ | appendix_b_precise_gx 不在 registry 中。D082 记录了下修，但数据源不可追溯。需确认 G× 计算脚本和原始数据位置 |
| n=500 vs n=50 数值差异 | ✅ | 预期行为：n=500 DS s030 median=8.48 vs n=50 PPI=9.97（样本量效应），方向一致 |
| GSM8K imp/rand ratio | ✅ | paper_framing: 2.3-3.8×; registry DS: 2.3/2.5/3.8/2.8 → 范围 2.3-3.8× 精确匹配 |
| Cohen's d QW s015 | ⚠️ | paper_framing/S3→C 引用 d=0.28; registry cohens_d=0.3705。可能 d vs d_z 定义差异，需确认 |

### 3.2 方法论一致性

| 检查项 | 状态 | 详情 |
|--------|------|------|
| 聚合方法 nanmedian + Wilcoxon | ✅ | D083 confirmed；GSM8K 数据已用 nanmedian 重算（D080 bug fix） |
| Bootstrap B=10000 | ✅ | n=50 实验用 B=10000；n=500 实验用 Wilcoxon + bootstrap median CI |
| Bonferroni 校正 k=4 | ✅ | n=500 实验使用 family-wise Bonferroni k=4 (D066) |
| Batch1 数据标注 | ✅ | Batch1 v2 rescore 已完成 (2026-05-16)，combined values 不变，此为最终权威值 |
| Per-problem paired 统计量定义 | ⚠️ | paper_framing 定义 "median(II_low_i − II_high_i)" 但 DS n=50 引用值更接近 PPI_low_median 而非 median_diff。需统一定义和数值 |

### 3.3 Framing 一致性

| 检查项 | 状态 | 详情 |
|--------|------|------|
| "3-15× 差异" 范围 | ⚠️ | n=500 QW s025 ratio = 2.7× (< 3)。"3-15×" 应改为 "~3-16×" 或 "2.7-15.5×" 以精确反映数据 |
| Random NS 阈值 ~s020-s025 | ✅ | n=50 + n=500 一致：random s015/s020 NS, s025+ 显著 |
| LLaMA 用词限制 | ✅ | paper_framing 已限定 "suggests"/"provides partial support"，禁止 "confirms" |
| C5b future_work 定位 | ✅ | paper_framing 正确将 gate_failed 结果放入 §6 Discussion |
| Negative results 处理 | ✅ | C4 Qwen entropy (negative) → "model-dependent"；C5b pilot (gate_failed) → "future work"；v6_random_s030 (SIGTERM) → 已有 n=500 数据覆盖 |
| DS accuracy → 定性观察 | ✅ | D086 正确降级；D089 揭示截断驱动双 regime |

### 3.4 数据完整性

| 检查项 | 状态 | 详情 |
|--------|------|------|
| 每个 claim 有 primary + supporting | ✅ | 见 §2 Claim-Evidence Matrix |
| DS 8k dose curve 完整 | ✅ | acc_ds_s030_8k_v2 完成: acc=0.04, trunc=0.76, non-trunc=0.167。5-point dose curve 完整。D086 已将 DS accuracy 降为定性 |
| v6_random_s030 失败 | ✅ | SIGTERM killed，但 n=500 (c2_n500_deepseek) rand_s030=0.5096 已覆盖 |
| QW n=50 s015/s020 random | ✅ | bf16_qw_rand_s015 (NS, p=0.863) + bf16_qw_rand_s020 (NS, p=0.149) 已有数据 |
| GSM8K QW random s025+s030 | ✅ | gsm8k_qw_rand_s025_v2 + gsm8k_qw_rand_s030_v2 均 success |

---

## 4. 待解决问题清单

### 阻塞 Round 10

| # | 问题 | 严重度 | 负责人 | 状态 |
|---|------|--------|--------|------|
| P1 | Batch1 v2 rescore 未完成：QW accuracy dose curve 的 batch1 数据可能需修正 | ✅ RESOLVED | — | 完成：QW 值不变，无需修改 |
| P2 | DS n=50 引用值精确性：paper_framing 的 0.32→1.15→3.97→9.94 与 PPI_low_median 有 ≤0.03 差异，需确认是否来自 paired subtraction 或另一计算 | 🟡 MEDIUM | — | 待确认 |
| P3 | G× 21-64× 数据源不可追溯：appendix_b_precise_gx 不在 registry，计算脚本位置未知 | 🟡 MEDIUM | — | 待确认 |

### 非阻塞但建议修正

| # | 问题 | 严重度 | 建议 |
|---|------|--------|------|
| P4 | "3-15×" 范围不精确（QW s025 ratio=2.7× < 3） | 🟢 LOW | 改为 "~3-16×" 或 "2.7-15.5× at s025" |
| P5 | Cohen's d_z vs cohens_d 命名混淆（QW s015: framing 0.28 vs registry 0.37） | 🟢 LOW | 统一使用 d_z 并更新引用值 |
| P6 | ~~DS 8k s030 缺失~~ | ✅ RESOLVED | acc_ds_s030_8k_v2 完成，5-point dose curve 完整 |
| P7 | GSM8K QW random s030 gradient (2.89) > importance (2.09) | 🟢 LOW | paper_framing 已正确处理（"反转仅在原始值"） |

---

## 5. Round 10 Readiness Assessment

### 数据就绪度: **95%** — 近完全就绪

**✅ 已就绪 (可进入 Round 10)**:
- 38 个计划实验全部完成，125+ 个 registry 条目
- 核心 claims (C1-C3, C5, C6, S3→C, S7→C) 数据完整且一致
- n=500 power validation (C7) 双模型完成，全条件显著
- GSM8K cross-benchmark (C10) 双模型 + random 完成
- DS 8k accuracy dose curve 5-point 完整（定性观察）
- Negative results (C4 Qwen entropy, C5b pilot) 正确归类
- 统计方法统一 (nanmedian + Wilcoxon + Bonferroni)
- Paper bib audit + §4-7 corrections 已完成
- c10_lang_switching: 语言切换率单调递增，补充 DS sparsity 对推理的影响
- c5_per_phase_gini: DS+QW 30/30 完成，low phase delta 跨模型一致单调递增
- QW batch1 v2 rescore: 完成，combined 数据不变

**🔄 进行中 (不阻塞但增强质量)**:
- c8_llama_n250_fixed: LLaMA n=250 cross-architecture (RUNNING, cuda:2,3)
- c10 s020/s025 gen_snippet: RUNNING on cuda:1

**⚠️ 需关注**:
- P2/P3: 数值精确性 — 建议在 Round 10 前快速确认 DS 引用值和 G× 计算源
- P4/P5: Framing 中两处数值范围微调
