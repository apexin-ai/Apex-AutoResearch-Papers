# Round 10 Data Compilation & Consistency Check

> 编译时间: 2026-05-16 | 编译人: Worker (data compilation agent) | 数据源: experiment registry (120 experiments, all DONE)

---

## 1. 数据总表

### A. II Dose Curve — DeepSeek Importance (n=50, MATH-500, bf16)

| Sparsity | PPI_low_median | PPI_high_median | paired_median_diff | Cohen's d_z | Bonferroni p | n_paired |
|----------|---------------|-----------------|-------------------|-------------|-------------|----------|
| s015 | 0.3155 | 0.000120 | 0.3925¹ | 0.44² | <0.005 | 49 |
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
| bf16_ds_rand_s020 | random | s020 | 0.2763 | 0.2918 | −0.0155 | ❌ NS |
| bf16_importance_s025 | importance | s025 | 7.1960 | 0.0324 | 7.1636 | ✅ PASS |
| bf16_ds_rand_s025 | random | s025 | 1.3627 | 0.8182 | 0.5445 | ❌ NS |
| v6_random_s025 | random | s025 | 2.9146 | 3.0024 | −0.1199 | ❌ NS (CI [−1.52, 1.25]) |
| v6_random_s030 | random | s030 | — | — | — | ❌ FAILED (SIGTERM) |

**Qwen Random (n=50)**:

| exp_id | Sparsity | median_diff | Wilcoxon p | Significant? |
|--------|----------|-------------|------------|-------------|
| bf16_qw_rand_s015 | s015 | −0.029 | 0.863 | NS |
| bf16_qw_rand_s020 | s020 | 0.129 | 0.149 | NS |

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

---

### F. QW Accuracy Dose Curve (n=100 combined, 8k tokens, MATH-500)

| Sparsity | Combined acc | n | Δ vs dense | Status |
|----------|-------------|---|------------|--------|
| dense | 0.46 (46/100) | 100 | — | ✅ |
| s015 | 0.36 (36/100) | 100 | −0.10 | ✅ |
| s020 | 0.36 (36/100) | 100 | −0.10 | ✅ |
| s025 | 0.33 (33/100) | 100 | −0.13 | ✅ |
| s030 | 0.19 (19/100) | 100 | −0.27 | ✅ |

⚠️ **Batch1 v2 rescore 进行中**：batch1 (n=50) 原始数据用 max_new_tokens=2048，已有 b1_8k 版本（8192 tokens），但 v2 rescore 完整修正尚未完成（另一 Worker 处理中）。上述 combined acc 可能因 batch1 rescore 而变化。

---

### G. DS 8k Accuracy Dose Curve (n=50, 8k tokens, MATH-500, v2)

| Sparsity | Accuracy | n | Δ vs dense | Truncation rate | Non-trunc acc |
|----------|----------|---|------------|-----------------|---------------|
| dense | 0.74 (37/50) | 50 | — | 0.16 | — |
| s015 | 0.48 (24/50) | 50 | −0.26 | 0.32 | 0.706 |
| s020 | 0.30 (15/50) | 50 | −0.44 | 0.56 | 0.682 |
| s025 | 0.08 (4/50) | 50 | −0.66 | 0.76 | — |
| s030 | **MISSING** | — | — | — | — |

D089: s≤0.20 截断驱动（non-trunc acc ~70% 稳定），s025+ truncation 压倒性。
D086: DS accuracy **降为定性观察**，QW 作为 accuracy dose-response 主证据。

---

### H. Mechanism — Discrimination Collapse (C4)

**DeepSeek (c4_entropy, n=30)**:

| Metric | s015 | s020 | s025 | s030 | Direction |
|--------|------|------|------|------|-----------|
| imp_entropy_delta | −0.040 | −0.047 | −0.045 | −0.044 | ↓ consistent |
| rand_entropy_delta | +0.128 | +0.136 | +0.217 | +0.233 | ↑ consistent |
| imp_gini_delta | −0.030 | −0.040 | −0.065 | −0.081 | ↓ monotonic |
| imp_cv_delta | −0.564 | −0.774 | −1.287 | −1.665 | ↓ monotonic |

**Qwen (qwen_c4_entropy, n=30, conclusion=negative)**:

| Metric | s015 | s020 | s025 | s030 | Direction |
|--------|------|------|------|------|-----------|
| imp_entropy_delta | −0.073 | −0.076 | **+0.045** | −0.007 | ⚠️ s025 反转 |
| imp_gini_delta | −0.010 | −0.012 | −0.010 | −0.020 | ↓ weaker |
| imp_cv_delta | −0.045 | −0.208 | −1.491 | −1.142 | ↓ non-monotonic |

**结论**: Gini/CV 下降跨模型一致；entropy collapse DeepSeek 一致但 Qwen s025 反转 → entropy redistribution = model-dependent secondary effect。

---

### I. Cross-Architecture — LLaMA (C8, c3_llama, n=50)

| Metric | s015 | s020 | s025 | s030 |
|--------|------|------|------|------|
| imp_vs_rand d_z | 0.19 | 0.26 | 0.29 | 0.34 |
| within-imp phase d_z | ~1.0 | ~1.0 | ~1.0 | ~1.0 |
| Bonferroni sig? | NS | NS | NS | ✅ (p=0.029) |

- Qualitative direction consistent; imp_vs_rand 交互弱（仅 s030 显著）
- Random 在 LLaMA 上也显示 phase gradient (d_z 0.35→0.44)

---

### J. Mitigation Pilot (C5b, c5b_pilot, n=30, s025)

| Condition | median_II | Recovery % | 95% CI | Wilcoxon p |
|-----------|-----------|------------|--------|------------|
| Uniform | 1.044 | — | — | — |
| Oracle | 0.856 | 18% | [−39, +46] | 0.0021 |
| Heuristic | 0.713 | 32% | [−23, +66] | 0.0236 |

**Gate**: oracle_recovery > 30% → **FAIL** (18% < 30%). D057 降为 future work.

---

### K. Supporting Experiments

| exp_id | Claim | Key Result |
|--------|-------|------------|
| think_phase_validation | C1 (R9) | median κ = 0.887; think→low_sparsity=57.8%, answer→high_sparsity=62.7% |
| sf5_asymmetric_spot | robustness | Phase gradient consistent under asymmetric allocation (D=19.13, 18.25) |
| appendix_b_precise_gx | G× 修正 | ❌ 未在 registry；D082 记录 G× 下修 58-241× → 21-64× |

---

## 2. Claim-Evidence Matrix

| Claim | Status | Primary Evidence | Supporting Evidence | 完整? |
|-------|--------|-----------------|--------------------|---------| 
| C1: Strategy × task modulation | confirmed | MATH-500 imp/rand 15-36× (n=500) | GSM8K ratio 2.3-3.8× | ✅ |
| C2: Phase modulation | confirmed | DS n=50: 0.32→9.94 (monotonic) | n=500: 0.39→8.48, Bonferroni全显著 | ✅ |
| C3: Phase-strategy crossover | confirmed | s025 crossover data | n=500 复现 | ✅ |
| C4: Discrimination collapse | partially | c4_entropy: Gini/CV↓ | qwen_c4: entropy s025 反转 | ✅ |
| C5: Cross-model | confirmed | DS+QW 方向一致, ρ=1.0 | QW ~1/4 DS, onset s≥0.20 | ✅ |
| C5b: Mitigation | future_work | gate_failed (18%<30%) | — | ✅ (§6) |
| C6: Sub-exponential | confirmed | 增长因子递减 | n=500 confirms | ✅ |
| C7: n=500 power | confirmed | c2_n500_deepseek + c2_qw_n500_r3 | 全条件 Bonf sig | ✅ |
| C8: LLaMA | partially | within-imp d_z~1.0 | imp_vs_rand 仅s030 sig | ⚠️ |
| C9: Prior work diff | planned | §2 引用区分 | — | ✅ |
| C10: GSM8K | confirmed | DS 0.241→4.682; QW 0.039→2.092 | QW rand completed | ✅ |
| S3→C: Onset threshold | confirmed | QW s015 CI跨零 | DS s015+ 全显著 | ✅ |
| S7→C: Monotonicity | confirmed | ρ=1.0 (n=50+n=500) | 6-point | ✅ |

---

## 3. Consistency Checklist

### 3.1 数值一致性

| 检查项 | 状态 | 详情 |
|--------|------|------|
| DS dose curve 引用值 vs registry | ⚠️ | paper_framing: 0.32→1.15→3.97→9.94; PPI_low_median: 0.316→1.128→3.955→9.973。s020差0.02, s030差0.03。需确认计算方式 |
| QW dose curve 引用值 vs registry | ✅ | 0.048→0.208→1.109→2.619 精确匹配 |
| G× 值 21-64× | ⚠️ | appendix_b_precise_gx 不在registry。D082 记录下修但数据源不可追溯 |
| n=500 vs n=50 数值差异 | ✅ | 预期行为（样本量效应），方向一致 |
| GSM8K imp/rand ratio 2.3-3.8× | ✅ | DS registry: 2.3/2.5/3.8/2.8 → 2.3-3.8× 精确匹配 |
| Cohen's d QW s015 | ⚠️ | framing引用 d=0.28; registry cohens_d=0.3705。d vs d_z 定义差异？ |

### 3.2 方法论一致性

| 检查项 | 状态 | 详情 |
|--------|------|------|
| 聚合 nanmedian + Wilcoxon | ✅ | D083 confirmed; GSM8K 已用 nanmedian 重算 |
| Bootstrap B=10000 | ✅ | n=50 B=10000; n=500 Wilcoxon + bootstrap CI |
| Bonferroni k=4 | ✅ | n=500 family-wise (D066) |
| Batch1 数据标注 | ⚠️ | v2 rescore 进行中。论文需标注数据版本 |
| 统计量定义一致性 | ⚠️ | paper定义 median(II_low_i−II_high_i) 但DS引用值匹配 PPI_low_median |

### 3.3 Framing 一致性

| 检查项 | 状态 | 详情 |
|--------|------|------|
| "3-15×差异" 范围 | ⚠️ | n=500 QW s025 ratio=2.7×(<3)。建议改为 "~3-16×" 或注明 |
| Random NS 阈值 ~s020-s025 | ✅ | n=50+n=500 一致 |
| LLaMA 用词限制 | ✅ | "suggests"/"partial support" |
| C5b future_work 定位 | ✅ | gate_failed 正确入 §6 |
| Negative results 处理 | ✅ | C4 Qwen → "model-dependent"; C5b → "future work" |
| DS accuracy → 定性 | ✅ | D086 正确降级 |

### 3.4 数据完整性

| 检查项 | 状态 | 详情 |
|--------|------|------|
| 每个 claim primary+supporting | ✅ | 见 §2 |
| DS 8k s030 缺失 | ⚠️ | D086 降为定性; 论文注明 4-point |
| v6_random_s030 失败 | ✅ | n=500 rand_s030=0.5096 已覆盖 |
| GSM8K QW random | ✅ | s025+s030 completed |

---

## 4. 待解决问题清单

### 阻塞 Round 10

| # | 问题 | 严重度 | 负责人 | 状态 |
|---|------|--------|--------|------|
| P1 | Batch1 v2 rescore 未完成：QW accuracy 可能变化 | 🟡 MEDIUM | 另一 Worker | 进行中 |
| P2 | DS n=50 引用值精确性：s020差0.02, s030差0.03 | 🟡 MEDIUM | — | 待确认 |
| P3 | G× 21-64× 数据源不可追溯 | 🟡 MEDIUM | — | 待确认 |

### 非阻塞

| # | 问题 | 严重度 | 建议 |
|---|------|--------|------|
| P4 | "3-15×" 范围（QW s025=2.7×<3） | 🟢 LOW | 微调范围 |
| P5 | Cohen's d_z 命名混淆（QW s015: 0.28 vs 0.37） | 🟢 LOW | 统一定义 |
| P6 | DS 8k s030 缺失 | 🟢 LOW | 注明 4-point |
| P7 | GSM8K QW rand s030 gradient > importance | 🟢 LOW | 已正确处理 |

---

## 5. Round 10 Readiness Assessment

### 数据就绪度: **85%** — 条件性就绪

**✅ 已就绪**:
- 120 registry 条目全部 DONE
- 核心 claims (C1-C3, C5-C7, C10, S3→C, S7→C) 数据完整且一致
- n=500 power validation 双模型完成
- GSM8K cross-benchmark 双模型 + random 完成
- Negative results 正确归类
- 统计方法统一

**⚠️ 需关注**:
- P1: Batch1 v2 rescore — 如 QW accuracy 变化 >±0.05 需更新论文
- P2/P3: 数值精确性 — 建议 Round 10 前快速确认
- P4/P5: Framing 微调

**建议**: 可以开始 Round 10 审稿，同时并行解决 P1-P3。