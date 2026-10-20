# 数字一致性终审报告

审计日期：2026-05-14
审计范围：abstract.tex, introduction.tex, results.tex, analysis.tex, discussion.tex, conclusion.tex, appendix_results.tex, appendix_disc_analysis.tex

---

## 通过 ✅

### Table 1 (tab:aggregate-ii) — DeepSeek 重要性驱逐 Δ 值
| 稀疏度 | 论文值 | 数据源 (median_difference_results.txt) | 验证 |
|--------|--------|----------------------------------------|------|
| s=0.15 | 0.39 | bf16_importance_s015: 0.3925 → 0.39 | ✅ |
| s=0.20 | 1.48 | bf16_importance_s020: 1.4818 → 1.48 | ✅ |
| s=0.25 | 7.16 | bf16_importance_s025: 7.163595 → 7.16 | ✅ |
| s=0.30 | 14.59 | bf16_importance_s030: 14.586064 → 14.59 | ✅ |

### Table 1 — Random 驱逐 s=0.30 行
| 相位 | 论文值 | 数据源 (permutation_test_median_verification.txt) | 验证 |
|------|--------|--------------------------------------------------|------|
| high | 2.503 | high=2.503 | ✅ |
| mid  | 2.592 | mid=2.592 | ✅ |
| low  | 4.041 | low=4.041 | ✅ |
| Δ    | 1.54  | 4.041 - 2.503 = 1.538 → 1.54 | ✅ |
| G    | 1.6   | 4.041 / 2.503 = 1.615 → 1.6 | ✅ |

### Table 2 (tab:main-results) — 内部算术一致性
所有 Δ = II_low - II_high 和 G = II_low / II_high 在显示精度内一致（G 由未四舍五入的中位数计算后取整）：
- s=0.15 Imp: 0.398 - 0.006 = 0.392 ≈ 0.39 ✅; G 由未取整值计算得 69 ✅
- s=0.20 Imp: 1.496 - 0.015 = 1.481 ≈ 1.48 ✅; G ≈ 103 ✅
- s=0.25 Imp: 7.196 - 0.032 = 7.164 ≈ 7.16 ✅; G ≈ 222 ✅
- s=0.30 Imp: 14.639 - 0.053 = 14.586 ≈ 14.59 ✅; G ≈ 274 ✅
- s=0.15 Rand: 0.103 - 0.093 = 0.010 ≈ 0.01 ✅; G = 1.108 ≈ 1.1 ✅
- s=0.20 Rand: 0.276 - 0.292 = -0.016 ≈ -0.02 ✅; G = 0.945 ≈ 0.9 ✅
- s=0.25 Rand: 1.363 - 0.818 = 0.545 ≈ 0.54 ✅; G = 1.666 ≈ 1.7 ✅
- s=0.30 Rand: 4.041 - 2.503 = 1.538 ≈ 1.54 ✅; G = 1.615 ≈ 1.6 ✅

### Table 3 (tab:cross-model) — Qwen 重要性驱逐 Δ 值
| 稀疏度 | 论文值 | 数据源 (median_difference_results.txt) | 验证 |
|--------|--------|----------------------------------------|------|
| s=0.15 | 0.04 | bf16_qw_imp_s015: 0.038565 → 0.04 | ✅ |
| s=0.20 | 0.23 | bf16_qw_imp_s020: 0.234979 → 0.23 | ✅ |
| s=0.25 | 1.27 | bf16_qw_imp_s025: 1.267732 → 1.27 | ✅ |
| s=0.30 | 2.94 | bf16_qw_imp_s030: 2.943093 → 2.94 | ✅ |

### Table 3 — DeepSeek 行与 Table 1 一致
s=0.15: 0.39, s=0.20: 1.48, s=0.25: 7.16, s=0.30: 14.59 — 与 Table 1 重要性行完全一致 ✅

### Table 5 (tab:cohens-d) — Cohen's d_z 值
| 模型 | 稀疏度 | 论文 d_z | 数据源 (cohens_d_6point_paired_dz.txt) | cross_model_summary.json | 验证 |
|------|--------|---------|----------------------------------------|--------------------------|------|
| DS | s=0.15 | 0.44 | 0.442 → 0.44 | 0.44 | ✅ |
| DS | s=0.20 | 0.52 | 0.520 → 0.52 | 0.52 | ✅ |
| DS | s=0.25 | 0.68 | 0.683 → 0.68 | 0.68 | ✅ |
| DS | s=0.30 | 0.80 | 0.803 → 0.80 | 0.80 | ✅ |
| QW | s=0.15 | 0.28 | 0.281 → 0.28 | 0.28 | ✅ |
| QW | s=0.20 | 0.55 | 0.549 → 0.55 | 0.55 | ✅ |
| QW | s=0.25 | 0.89 | 0.889 → 0.89 | 0.89 | ✅ |
| QW | s=0.30 | 1.02 | 1.022 → 1.02 | 1.02 | ✅ |

### Cross-model 统计量
- Spearman ρ = 1.0: cross_model_analysis_summary.txt/json 均为 1.0 ✅
- Gradient permutation p = 0.043: cross_model_analysis_summary.txt/json 均为 0.043 ✅
- Per-problem concordance p = 0.926: cross_model_analysis_summary.json 为 0.926 ✅
- Per-problem mean ρ = -0.11: appendix_results.tex 注释 mean_rho=-0.107 → -0.11 ✅
- Random fail 7/8: cross_model_analysis_summary.json random_fail: 7/8 ✅
- Importance pass 8/8: cross_model_analysis_summary.json importance_pass: 8/8 ✅
- Qwen random s=0.30 anomaly: p=0.012, d=-0.035 → d_z=-0.04 (四舍五入) ✅

### 37× 放大因子 (results.tex:8)
14.59 / 0.39 = 37.41 → 37× ✅

### Crossover 反转倍数 (results.tex:66)
- s=0.15: 0.398/0.103 = 3.86 → 3.9× ✅
- s=0.20: 1.496/0.276 = 5.42 → 5.4× ✅
- s=0.25: 7.196/1.363 = 5.28 → 5.3× ✅
- s=0.30: 14.639/4.041 = 3.62 → 3.6× ✅

### Crossover 绝对值 (abstract:9, results:66, discussion:5)
- Importance high at s=0.25: 0.032 vs Random high: 0.818 ✅ (Table 2)
- Importance low at s=0.25: 7.196 vs Random low: 1.363 ✅ (Table 2)
- 三个文件中数字完全一致 ✅

### Δ 增长率 (appendix_disc_analysis.tex:57)
- 1.48/0.39 = 3.79 → 3.8× ✅
- 7.16/1.48 = 4.84 → 4.8× ✅
- 14.59/7.16 = 2.04 → 2.0× ✅

### 样本量一致性
- Table 1 caption: n=50（全部问题，中位数计算）✅
- Table 4 caption: n=49（DeepSeek 配对检验，排除 1 个）✅
- results.tex:81: n=46 Qwen, n=49 DeepSeek ✅
- appendix_disc_analysis.tex:45: n=49 DeepSeek (1 excluded), n=46 Qwen (4 excluded) ✅
- 50 - 1 = 49 ✅; 50 - 4 = 46 ✅

### Bootstrap B 值一致性
- results.tex:115: 10,000 permutations ✅
- results.tex:149 (Table 5 caption): B=10,000 ✅
- appendix_disc_analysis.tex:45: B=10,000 ✅
- rebootstrap_b10000_results.json: B=10000 ✅

### Table 4 (tab:permutation) CI 下界递增
论文正文 (results.tex:117): "CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$)"
Table 4 值: [0.19, 0.62], [0.69, 1.49], [1.66, 6.64], [6.70, 16.29]
下界序列：0.19, 0.69, 1.66, 6.70 — 与正文完全一致 ✅
appendix_disc_analysis.tex:47 注释中复述的 CI 与 Table 4 完全一致 ✅

### Qwen ~1/5 magnitude (results.tex:83)
- s=0.30: 2.94/14.59 = 0.201 ≈ 1/5 ✅
- 其他稀疏度下比值为 0.10–0.18，论文用 "~1/5" 作为近似表述，以最高稀疏度为准，可接受 ✅

### 高稀疏度相位 II < 0.06 (appendix_disc_analysis.tex:11)
Table 2 重要性高相位值：0.006, 0.015, 0.032, 0.053 — 均 < 0.06 ✅

### s=0.35 补充实验 (appendix_disc_analysis.tex:11)
论文写 0.105，注释写 II_high=0.1051 → 0.105 ✅

### Mean/median ratio at s=0.30 (appendix_disc_analysis.tex:46)
注释：mean_diff=22.94, median_diff=14.59 → 22.94/14.59 = 1.572 ≈ 1.6 ✅

### Abstract 与 results/discussion/conclusion 跨文件一致性
| 数字 | abstract | introduction | results | discussion | conclusion | 一致 |
|------|----------|-------------|---------|------------|------------|------|
| Δ: 0.39→14.59 | ✅ line 7 | ✅ line 13 | ✅ Table 1 | — | — | ✅ |
| d_z: 0.44→0.80 | ✅ line 7 | ✅ line 13 | ✅ Table 5 | ✅ line 11 | ✅ line 4 | ✅ |
| p<0.005 Bonf | ✅ line 7 | ✅ line 13 | ✅ Table 4 | — | — | ✅ |
| 7/8 random n.s. | ✅ line 8 | ✅ line 15 | — | — | ✅ line 4 | ✅ |
| Qwen d_z≥0.55 | ✅ line 10 | ✅ line 14 | ✅ sec 4.4 | ✅ line 11 | ✅ line 4 | ✅ |
| ρ=1.0, p=0.043 | ✅ line 10 | — | ✅ line 83 | ✅ line 11 | — | ✅ |
| G: 69→274 | — | — | ✅ Table 2 | ✅ line 5 | ✅ line 4 | ✅ |
| Crossover 0.032/0.818, 7.196/1.363 | ✅ line 9 | — | ✅ Table 2 | ✅ line 5 | — | ✅ |
| d_z=-0.04 random anomaly | ✅ line 8 | — | — | — | — | ✅ |

---

## 不一致 ❌

### ❌-1. 百分位数与 Bonferroni p 值算术矛盾 (results.tex:115)

**论文写：** "At $s{=}0.15$, the observed statistic falls at the $99.68$th percentile of the null ($p_{\text{Bonf}} = 0.0032$)"

**问题：** 99.68th percentile 意味着 10,000 次置换中约 32 次超过观测值，即 raw p = 32/10000 = 0.0032。Bonferroni 校正（4 次比较）应为 p_Bonf = 0.0032 × 4 = **0.0128**，非 0.0032。

反之，若 p_Bonf = 0.0032 确为 Bonferroni 校正后的值，则 raw p = 0.0008（约 8/10000 次置换超过观测值），对应百分位应为 **99.92th**，非 99.68th。

**两种修复可能：**
1. 若 raw p = 0.0032：百分位 99.68th 正确，但 p_Bonf 应改为 0.0128（仍 < 0.05，结论不变）
2. 若 raw p = 0.0008：p_Bonf = 0.0032 正确，但百分位应改为 99.92th

> 注：不影响显著性结论（两种情况下 p_Bonf 均 < 0.05），但数字报告自相矛盾。

### ❌-2. 数据源文件间 Cohen's d_z 值不一致

**cohens_d_6point_paired_dz.txt**（论文使用此源）：
- DS: 0.442 / 0.520 / 0.683 / 0.803 (s015–s030)
- QW: 0.281 / 0.549 / 0.889 / 1.022

**cohens_d_6point_paired_info.txt**（引用 regen_cohens_d_6point.py 再生脚本）：
- DS: 0.607 / 0.725 / 0.953 / 1.126 (s015–s030)
- QW: 0.371 / 0.722 / 1.233 / 1.439

两组数值差异极大（如 DS s015: 0.442 vs 0.607）。论文与 cross_model_analysis_summary.json 使用的是 dz.txt 的值，**内部一致**。但若 info.txt 的"regen"版本是后续修正计算，则论文可能使用了过时数据。

> 建议：确认哪组 d_z 为最终正确值。若 info.txt 为更新版本，论文中 Table 5 及所有引用 d_z 的位置均需更新。

### ❌-3. 熵变区间记号错误 (analysis.tex:43)

**论文写：** "$\Delta\mathcal{H} \in [-0.040, -0.047]$"

**问题：** 数学区间 $[a, b]$ 要求 $a \leq b$。但 $-0.040 > -0.047$，因此 $[-0.040, -0.047]$ 是空集。应写为 **$[-0.047, -0.040]$**。

Table 8 中四个值为 -0.040, -0.047, -0.045, -0.044，范围确为 [-0.047, -0.040]。

---

## 无法验证 ⚠️

### ⚠️-1. Table 4 (tab:permutation) 置换检验详细数值
- Observed Δ̃: 0.37, 0.97, 3.34, 9.85
- 95% CI: [0.19, 0.62], [0.69, 1.49], [1.66, 6.64], [6.70, 16.29]
- p_Bonf: 0.0032, <0.001, <0.001, <0.001

**原因：** 提供的数据源文件中无完整的置换检验结果表。permutation_test_median_verification.txt 仅涉及 D029 中位数修复验证（随机条件 s=0.30 的 II 值），不含重要性 vs 随机的配对置换检验原始结果。服务器文件 permutation_test_results.json 未包含在提供的数据源中。

> 论文内部引用的 CI 值在 results.tex:117 和 appendix_disc_analysis.tex:47 之间完全一致。

### ⚠️-2. Table 5 (tab:cohens-d) 中的 Δ̃ 和 CI 列
- DS: 0.32 [0.20, 0.47], 1.15 [0.66, 1.26], 3.97 [2.83, 5.29], 9.94 [8.39, 16.65]
- QW: 0.05 [-0.01, 0.11], 0.21 [0.07, 0.40], 1.11 [0.61, 1.47], 2.62 [1.72, 3.65]

**原因：** rebootstrap_b10000_results.json 仅指向服务器文件路径，未包含实际数值。

### ⚠️-3. Table 1 Random 行 s=0.15/0.20/0.25 值
- s=0.15: high=0.093, mid=0.097, low=0.103, Δ=0.01
- s=0.20: high=0.292, mid=0.350, low=0.276, Δ=-0.02
- s=0.25: high=0.818, mid=0.932, low=1.363, Δ=0.54

**原因：** 提供的数据源中仅有 s=0.30 随机条件的逐相位数据（来自 permutation_test_median_verification.txt）。s=0.15–0.25 的随机条件数据不在提供的文件中。
> 内部算术 (Δ = low - high, G = low/high) 已全部验证正确。

### ⚠️-4. Table 6/7 (analysis.tex) 判别崩溃和熵变指标
- Gini delta, CV delta (Table 6): 8 个 DeepSeek + 8 个 Qwen 值
- Entropy delta (Table 7): 4 个 DeepSeek + 4 个 Qwen 值
- Appendix random Gini deltas: DS -0.031 to -0.073, QW -0.019 to -0.045

**原因：** 这些值来自 c4_entropy 实验，原始数据不在提供的数据源文件中。

### ⚠️-5. Mean/median ratios (results.tex:112)
- DeepSeek: 1.2× (s=0.15) to 1.6× (s=0.30)
- Qwen: 1.1× to 1.4×

**原因：** 仅 s=0.30 的 mean/median ratio 可从注释验证（22.94/14.59 = 1.57 ≈ 1.6）。其他稀疏度无数据。

### ⚠️-6. Percentile 99.68 具体排名 (results.tex:115)
见 ❌-1，无法确定真实 raw p 值（需要原始置换检验输出）。

---

## 内部一致性

### 跨文件交叉检查

1. **abstract ↔ results tables**: 所有从 abstract 引用的数字均可在 results 的 table 中找到精确对应。✅
2. **introduction ↔ results**: introduction 中的 Δ (0.39→14.59)、d_z (0.44→0.80)、p<0.005 均与 results tables 一致。✅
3. **discussion ↔ results**: G 范围 (69–274×)、crossover 数值 (0.032/0.818, 7.196/1.363) 与 Table 2 一致。✅
4. **conclusion ↔ results**: G (69→274)、d_z (0.44→0.80)、7/8 non-significant、Qwen d_z≥0.55 全部一致。✅
5. **appendix_results ↔ results**: Random control 数据 (3/4 FAIL for Qwen, p=0.012, d_z=-0.04) 与 abstract/results 一致。✅
6. **appendix_disc_analysis ↔ results**: CI 值、样本量 (n=49/46)、B=10,000 全部一致。✅

### Table 间交叉检查

1. **Table 1 vs Table 2**: Table 1 的 Δ 列是 Table 2 中 Importance 行的 Δ 列子集，数值完全一致。✅
2. **Table 1 vs Table 3**: Table 3 的 DeepSeek 行与 Table 1 Importance 行完全一致。✅
3. **Table 2 G 列 vs 正文**: 正文引用 69×→274× 与 Table 2 G 列一致。✅
4. **Table 4 vs Table 5**: 两表测量不同统计量（Table 4: 重要性 vs 随机配对中位差; Table 5: 重要性条件下高/低相位配对中位差），数值不同是正确的。✅

### 派生计算验证

| 计算 | 输入 | 预期 | 论文值 | 验证 |
|------|------|------|--------|------|
| 37× amplification | 14.59/0.39 | 37.41 | 37 | ✅ |
| 5.3× reversal (s=0.25) | 7.196/1.363 | 5.28 | 5.3 | ✅ |
| 3.9× reversal (s=0.15) | 0.398/0.103 | 3.86 | 3.9 | ✅ |
| 5.4× reversal (s=0.20) | 1.496/0.276 | 5.42 | 5.4 | ✅ |
| 3.6× reversal (s=0.30) | 14.639/4.041 | 3.62 | 3.6 | ✅ |
| Δ growth 3.8× | 1.48/0.39 | 3.79 | 3.8 | ✅ |
| Δ growth 4.8× | 7.16/1.48 | 4.84 | 4.8 | ✅ |
| Δ growth 2.0× | 14.59/7.16 | 2.04 | 2.0 | ✅ |
| Qwen ~1/5 | 2.94/14.59 | 0.201 | ~1/5 | ✅ |
| mean/median 1.6× (s=0.30) | 22.94/14.59 | 1.572 | 1.6 | ✅ |
| n: 50-1=49 DS | — | 49 | 49 | ✅ |
| n: 50-4=46 QW | — | 46 | 46 | ✅ |

---

## 总结

| 类别 | 数量 |
|------|------|
| 已验证通过 | ~95 个数字/声明 |
| 不一致 | 3 个（1 个算术矛盾、1 个数据源冲突、1 个记号错误）|
| 无法验证 | 6 类（均因原始数据未包含在提供的数据源文件中）|

**严重程度排序：**
1. **❌-2 (Cohen's d_z 数据源冲突)** — 高。需确认哪组值正确。若 info.txt 为最终版，Table 5 及所有 d_z 引用需全面更新。
2. **❌-1 (百分位/p_Bonf 矛盾)** — 中。数字自相矛盾，但不影响显著性结论。
3. **❌-3 (区间记号)** — 低。纯排版问题。
