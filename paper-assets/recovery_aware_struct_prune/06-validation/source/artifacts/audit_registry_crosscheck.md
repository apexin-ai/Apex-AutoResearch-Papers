# Registry 交叉验证

审计日期: 2026-05-25
数据源: registry.yaml 完整导出 (277 experiments)

---

## Table 2 数据溯源 (GSM8K Decoupling, 20% sparsity)

### GRPO Accuracy

| 论文值 | Registry exp_id | Registry metric | 匹配? |
|--------|----------------|-----------------|-------|
| CKA-only 64.39% (σ=0.19) | eval_gsm8k_grpo_cka_only_20_v2 (seed42: 64.37%), eval_gsm8k_grpo_cka_only_20_seed123 (64.22%), eval_gsm8k_grpo_cka_only_20_seed456_full (64.59%) | mean=64.39% | ✅ 精确匹配 |
| Standard 59.84% (σ=0.38) | eval_gsm8k_grpo_standard_20_fair_v2 (seed42: 59.44%), eval_gsm8k_grpo_standard_20_seed123_full (59.89%), eval_gsm8k_grpo_standard_20_seed456_full (60.20%) | mean=59.84% | ✅ 精确匹配 |
| RASP 60.88% | eval_gsm8k_grpo_rasp_20_fair | accuracy=0.6088 = 60.88% | ✅ 精确匹配 |
| Random 50.72% (σ=0.15) | eval_gsm8k_grpo_random_20_v2 (50.57%), eval_gsm8k_grpo_random_20_seed123_v2 (50.72%), eval_gsm8k_grpo_random_20_seed456 (50.87%) | mean=50.72% | ✅ 精确匹配 |
| ShortGPT 43.37% | eval_gsm8k_grpo_shortgpt_20 | gsm8k_accuracy=43.37 | ✅ 精确匹配 |

### SFT Accuracy

| 论文值 | Registry exp_id | Registry metric | 匹配? |
|--------|----------------|-----------------|-------|
| CKA-only 63.91% | eval_gsm8k_sft_cka_only_20 | gsm8k_accuracy=0.6391 = 63.91% | ✅ 精确匹配 |
| Standard 59.29% | eval_sft_standard_full_westd | accuracy=0.5929 = 59.29% | ✅ 匹配 (westd eval) |
| Standard 59.29% | eval_gsm8k_sft_standard_20 | gsm8k_accuracy=0.5921 = 59.21% | ⚠ 0.08pp 差异 (不同服务器) |
| RASP 61.49% | eval_gsm8k_sft_rasp_20 | gsm8k_accuracy=0.6149 = 61.49% | ✅ 精确匹配 |
| Random 51.25% | eval_gsm8k_sft_random_20 | gsm8k_accuracy=0.5125 = 51.25% | ✅ 精确匹配 |
| ShortGPT 44.73% | eval_gsm8k_sft_shortgpt_20 | gsm8k_accuracy=44.73 | ✅ 精确匹配 |

### Peak Rewards

| 论文值 | Registry exp_id | Registry metric | 匹配? |
|--------|----------------|-----------------|-------|
| CKA 0.354 | grpo_cka_only_20 | peak_reward=0.3544 | ✅ (0.3544 → 0.354 四舍五入) |
| Standard 0.081 | grpo_standard_20_fair | peak_reward=0.081 | ✅ 精确匹配 |
| RASP 0.061 | grpo_rasp_20_fair | peak_reward=0.061 | ✅ 精确匹配 |
| Random 0.190 | grpo_random_20 | reward_peak=0.19 | ✅ 精确匹配 |

---

## Table 3 数据溯源 (Alpha ablation, GSM8K 20%)

| α | 论文 SFT | 论文 GRPO | Registry exp_id(s) | Registry SFT | Registry GRPO | 匹配? |
|---|---------|----------|-------------------|-------------|--------------|-------|
| 0.5 | 60.73 | 61.18 | eval_gsm8k_sft_alpha0p5_20 / eval_gsm8k_grpo_alpha0p5_20 | 60.73% | 61.18% | ✅✅ |
| 1.0 | 61.49 | 60.88 | eval_gsm8k_sft_rasp_20 / eval_gsm8k_grpo_rasp_20_fair | 61.49% | 60.88% | ✅✅ |
| 2.0 | 64.97 | 66.11 | eval_gsm8k_sft_alpha2p0_20 / eval_gsm8k_grpo_alpha2p0_20 | 64.97% | 66.11% | ✅✅ |
| 3.0 | 64.14 | 63.46 | eval_gsm8k_sft_alpha3p0_20 / eval_gsm8k_grpo_alpha3p0_20 | 64.14% | 63.45% | ✅⚠ GRPO off by 0.01pp (rounding 0.6345→63.46) |
| 4.0 | 61.94 | 62.77 | eval_gsm8k_sft_alpha4_20_v5 / eval_gsm8k_grpo_alpha4_20_v3 | 61.94% | 62.77% | ✅✅ |

**结论**: Table 3 所有值与 registry 精确匹配（α=3.0 GRPO 仅 0.01pp 舍入差异）。

---

## MATH-500 数据溯源 (tab_math500)

### 主方法对比 (20%)

| 方法 | 论文 SFT | 论文 GRPO | Registry exp_id(s) | Registry SFT | Registry GRPO | 匹配? |
|------|---------|----------|-------------------|-------------|--------------|-------|
| CKA-only | 27.4 | 27.6 | eval_math500_sft_cka_only_20_fixed_v2 / eval_math500_grpo_cka_only_20_fixed | 27.4% | 27.6% | ✅✅ |
| Standard | 25.6 | 27.0 | eval_math500_sft_standard_20_fixed_v4 / eval_math500_grpo_standard_20_fixed | 25.6% | 27.0% | ✅✅ |
| RASP α=1.0 | 21.6 | 23.0 | eval_math500_sft_rasp_alpha1p0_20_fixed / eval_math500_grpo_rasp_alpha1p0_20_fixed | 21.6% | 23.0% | ✅✅ |
| Random | 16.6 | 15.0 | eval_math500_sft_random_20_fixed_v3 / eval_math500_grpo_random_20_fixed | 16.6% | 15.0% | ✅✅ |

### Alpha 消融 (20%)

| α | 论文 SFT | 论文 GRPO | Registry exp_id(s) | Registry SFT | Registry GRPO | 匹配? |
|---|---------|----------|-------------------|-------------|--------------|-------|
| 0.5 | 26.8 | 26.8 | eval_math500_sft_rasp_alpha0p5_20_fixed / eval_math500_grpo_rasp_alpha0p5_20_fixed | 26.8% | 26.8% | ✅✅ |
| 2.0 | 25.6 | 27.4 | eval_math500_sft_rasp_alpha2p0_20_fixed / eval_math500_grpo_rasp_alpha2p0_20_fixed | 25.6% | 27.4% | ✅✅ |
| 3.0 | 23.6 | -- | eval_math500_sft_rasp_alpha3p0_20_fixed_v2 (空metrics) / eval_math500_grpo_rasp_alpha3p0_20 | **无记录** | 22.8% | ⚠ SFT fixed_v2无metrics; 非fixed=23.2%; 论文23.6% |
| 4.0 | 27.8 | 27.2 | eval_math500_sft_rasp_alpha4p0_20_fixed / eval_math500_grpo_rasp_alpha4p0_20_fixed (空metrics) | 27.8% | **无记录** | ⚠ GRPO fixed无metrics; 非fixed=26.2%; 论文27.2% |

### 25% sparsity

| 方法 | 论文 SFT | 论文 GRPO | Registry SFT | Registry GRPO | 匹配? |
|------|---------|----------|-------------|--------------|-------|
| CKA-only | 18.8 | 17.6 | 18.8% (eval_math500_sft_cka_only_25_fixed) | 17.6% (eval_math500_grpo_cka_only_25_fixed) | ✅✅ |
| Standard | 15.4 | -- | 15.4% (eval_math500_sft_standard_25_fixed_v2) | -- | ✅ |

### Dense baseline

| 论文值 | Registry | 匹配? |
|--------|---------|-------|
| 53.0% (2048 tokens) | eval_math500_dense_2048: 53.0% | ✅ |
| 73.6% (4096 tokens) | eval_math500_dense_unpruned: 73.6% | ✅ |

---

## MBPP 数据溯源 (tab_mbpp)

| 方法 | 论文 SFT | 论文 GRPO | Registry SFT | Registry GRPO | 匹配? |
|------|---------|----------|-------------|--------------|-------|
| Dense | 53.48 | -- | 53.48% (eval_mbpp_dense_unpruned) | -- | ✅ |
| CKA-only | 12.83 | 14.17 | 12.83% (eval_mbpp_sft_cka_only_20) | 14.17% (eval_mbpp_grpo_cka_only_20) | ✅✅ |
| Standard | 12.03 | 13.10 | 12.03% (eval_mbpp_sft_standard_20_v4) | 13.10% (eval_mbpp_grpo_standard_20_v4) | ✅✅ |
| RASP | 11.76 | 13.10 | 11.76% (eval_mbpp_sft_rasp_20) | 13.10% (eval_mbpp_grpo_rasp_20) | ✅✅ |
| ShortGPT | 10.43 | 14.44 | 10.43% (eval_mbpp_sft_shortgpt_20_v2) | 14.44% (eval_mbpp_grpo_shortgpt_20_v2) | ✅✅ |

**结论**: MBPP 所有 8 个数值与 registry 精确匹配。

---

## Cross-Scale 1.5B 数据溯源 (tab5_cross_scale)

| 方法 | 论文 Reward | 论文 GSM8K | Registry Reward | Registry GSM8K | 匹配? |
|------|-----------|----------|----------------|---------------|-------|
| CKA-only | 0.238 | 35.48 | 0.2375 (grpo_cka_only_20_1p5b) | 35.48% (eval_gsm8k_grpo_cka_only_20_1p5b) | ⚠✅ reward 0.2375→0.238 |
| Standard | 0.084 | 22.29 | 0.0844 (grpo_standard_20_1p5b) | 22.29% (eval_gsm8k_grpo_standard_20_1p5b) | ⚠✅ reward 0.0844→0.084 |
| RASP | 0.099 | 26.16 | 0.099 (grpo_rasp_20_1p5b) | 26.16% (eval_gsm8k_grpo_rasp_20_1p5b) | ✅✅ |

**注**: 1.5B CKA/Standard reward 的 registry 值分别是 0.2375/0.0844，论文四舍五入到 0.238/0.084，合理。

---

## Floor 消融数据溯源

| τ | 论文值 | Registry exp_id | Registry 值 | 匹配? |
|---|--------|----------------|------------|-------|
| 0.3 | 65.05% | floor_ablation_0p3_cka_only_20_v2 | 65.05% | ✅ |
| 0.4 | 64.37% | eval_gsm8k_grpo_cka_only_20_v2 (default) | 64.37% | ✅ |
| 0.5 | 61.71% | floor_ablation_0p5_cka_only_20_v2 | 61.71% | ✅ |
| 0.6 | 62.02% | floor_ablation_0p6_cka_only_20_v2 | 62.02% | ✅ |

---

## Issue #1 验证 (Fig 1 vs Table 3)

### Registry 判定

**α=0.5**:
- Registry `eval_gsm8k_sft_alpha0p5_20`: gsm8k_accuracy = **0.6073 = 60.73%**
- Registry `eval_gsm8k_grpo_alpha0p5_20`: gsm8k_accuracy = **0.6118 = 61.18%**
- **Table 3 值 (60.73/61.18) 与 registry 精确匹配**
- **Fig 1 值 (64.52/65.05) 与 registry 不匹配**

**α=3.0**:
- Registry `eval_gsm8k_sft_alpha3p0_20`: **0.6414 = 64.14%**
- Registry `eval_gsm8k_grpo_alpha3p0_20`: **0.6345 ≈ 63.46%**
- **Table 3 值 (64.14/63.46) 与 registry 匹配**
- **Fig 1 值 (64.06/64.59) 与 registry 不匹配**

**α=4.0**:
- Registry SFT: **0.6194 = 61.94%** → Table 3 匹配; Fig 1 写 62.02% (差 0.08pp)
- Registry GRPO: **0.6277 = 62.77%** → 两者均匹配

### 污染源追踪

**关键发现**: Fig 1 中的错误值可追溯到其他实验的 registry 数据——这是**数据复制污染**：

| Fig 1 错误值 | 实际来源 (registry) | 污染类型 |
|-------------|-------------------|---------|
| α=0.5 GRPO = **65.05%** | floor_ablation_0p3_cka_only_20_v2 (τ=0.3 floor) = **65.05%** | 精确匹配：floor 消融数据误入 alpha 消融数组 |
| α=4.0 SFT = **62.02%** | floor_ablation_0p6_cka_only_20_v2 (τ=0.6 floor) = **62.02%** | 精确匹配：floor 消融数据误入 alpha 消融数组 |
| α=3.0 GRPO = **64.59%** | eval_gsm8k_grpo_cka_only_20_seed456_full (CKA seed 456) = **64.59%** | 精确匹配：CKA multi-seed 数据误入 |
| α=3.0 SFT = **64.06%** | 接近 eval_gsm8k_grpo_cka_only_20_verify = **64.06%** | 近似匹配：CKA verify 运行数据误入 |
| α=0.5 SFT = **64.52%** | 无精确匹配（最近: CKA seed456=64.59, CKA v2=64.37） | 来源不确定 |

**结论**: gen_fig1_dose_response.py 的硬编码数据有多个值来自 floor 消融或 CKA multi-seed 实验而非 alpha 消融实验。**Table 3 的数据是正确的**，Fig 1 的硬编码数据需要用 Table 3 值更新。

---

## Issue #5 验证 (4× cross-seed σ)

### 3-seed 实验值

**CKA-only GRPO 20%:**
| Seed | exp_id | Accuracy |
|------|--------|----------|
| 42 | eval_gsm8k_grpo_cka_only_20_v2 | 64.37% |
| 123 | eval_gsm8k_grpo_cka_only_20_seed123 | 64.22% |
| 456 | eval_gsm8k_grpo_cka_only_20_seed456_full | 64.59% |

- Mean = 64.39% ✅ 与论文匹配
- Range = 64.59 - 64.22 = 0.37 pp ✅ 与论文匹配
- Population σ (÷n) = **0.152 pp**
- Sample σ (÷(n-1)) = **0.186 pp**
- 论文 σ = **0.19 pp**

**论文使用的是 sample σ (n-1=2)**: 0.186 → 四舍五入 0.19 ✅

### "4×" 推导验证

论文原文 (exp.tex:78, app.tex:374):
> "$\varepsilon = 2$ pp because it is approximately $4\times$ the observed cross-seed standard deviation ($\sigma{=}0.19$ pp for CKA-only)"

计算:
- 2 / 0.19 = **10.5×** ← 不是 4×
- 2 / 0.38 (Standard σ) = **5.3×** ← 也不是 4×
- 2 / max(所有 sample σ) = 2 / 0.38 = **5.2×** ← 仍不是 4×

**结论: "4×" 数字找不到任何合理的推导路径。**

可能的解释：
1. 早期版本使用了不同的 σ 值（如 σ≈0.5 → 2/0.5 = 4×）
2. 计算错误：作者可能误用了 range (0.37) 而非 σ，但 2/0.37 ≈ 5.4×，仍不是 4×
3. 编辑遗留：ε 从其他值修改为 2pp 后未更新 "4×" 倍数

**此问题需要修正：要么改 "4×" 为 "~10×"（基于 CKA σ=0.19），要么改为 "~5×"（基于 Standard σ=0.38），或删除倍数声称直接说 "substantially exceeds"。**

---

## 新发现的问题

### MATH-500 两个值 registry 数据缺失

| 位置 | 论文值 | Registry exp_id | 问题 |
|------|--------|----------------|------|
| tab_math500 α=3.0 SFT | 23.6% | eval_math500_sft_rasp_alpha3p0_20_fixed_v2 | **metrics 为空**；非 fixed 版本 = 23.2% |
| tab_math500 α=4.0 GRPO | 27.2% | eval_math500_grpo_rasp_alpha4p0_20_fixed | **metrics 为空**；非 fixed 版本 = 26.2% |

这两个实验的 "fixed" 版本在 registry 中标记为 `conclusion: success` 但 metrics 为空（可能是 Worker 完成后未将 metrics 写回 registry）。论文值（23.6/27.2）与非 fixed 版本（23.2/26.2）存在 0.4-1.0pp 差异。

**影响**: 论文用了 "fixed" 评估脚本的结果，但该结果未入 registry。无法从 registry 交叉验证这两个数字。需要从服务器日志或 W&B 找回 fixed 版本的实际输出。

### Standard SFT 基线不一致

论文主表使用 Standard SFT = **59.29%** (来自 eval_sft_standard_full_westd)，但 TOST 表的 Δ 值推算出的 SFT 基线是 **59.21%** (来自 eval_gsm8k_sft_standard_20，不同服务器)。

- TOST seed456 Δ = +0.99 pp → 59.21 + 0.99 = 60.20% = registry GRPO seed456 值 ✅
- 如果用 SFT=59.29%: Δ应为 60.20-59.29 = 0.91 pp ≠ 0.99 pp

**影响**: TOST 分析内部一致（使用 59.21% 作为 SFT 基线），但与主文 SFT=59.29% 不一致。差异仅 0.08pp，不改变 TOST 结论，但严格来说 TOST 表和主表使用了不同的 SFT 基线值。

---

## 问题汇总

### 已确认需修复 (从 registry 交叉验证发现)

| # | 严重度 | 问题 | 状态 |
|---|--------|------|------|
| 1 | **HIGH** | Fig 1 (gen_fig1_dose_response.py) 中 α=0.5, 3.0 的数据与 Table 3 / registry 不一致。污染源追溯到 floor 消融和 CKA multi-seed 数据。**Table 3 是正确的。** | 需更新 Fig 1 脚本 |
| 2 | **MEDIUM** | "4× cross-seed σ" 声明：2/0.19=10.5×，不是 4×。无合理推导路径。 | 需修正文字 |
| 3 | **LOW** | MATH-500 α=3.0 SFT (23.6%) 和 α=4.0 GRPO (27.2%) 的 "fixed" 实验 registry metrics 缺失，无法交叉验证 | 需找回原始数据 |
| 4 | **LOW** | Standard SFT 基线: 主表 59.29% vs TOST 表推算 59.21% (差 0.08pp) | 应统一 |

### 已确认无误

- Table 2 全部 14 个值（6 GRPO + 6 SFT + α=2.0 pair）✅
- Table 3 全部 10 个值 ✅ (α=3.0 GRPO 0.01pp 舍入)
- MATH-500 主方法对比 8/8 ✅
- MATH-500 alpha 消融 4/6 ✅ (2 个 fixed 版本 metrics 缺失)
- MBPP 全部 8 个值 ✅
- Cross-scale 1.5B 全部 6 个值 ✅
- Peak rewards 全部 4 个值 ✅
- Floor 消融全部 4 个值 ✅
- Dense baselines ✅

**总计**: ~54 个论文关键数值中，50 个与 registry 精确匹配或合理四舍五入，2 个因 registry 数据缺失无法验证，2 个发现问题（Fig 1 污染 + 4× σ）。
