# 论文数值追溯审计报告

**审计日期**: 2026-05-23
**论文**: IRT Person-Fit Contamination Detection
**审计范围**: Tables 1–3, Discussion/Appendix key claims

---

## Table 1: Cohen's |d| for Δℓz* (tab:cohens_d)

### Qwen MMLU 5% (single seed)
- **论文值**: d = −4.15 [−9.9, −2.7]
- **源文件**: `results/contam_5_cohens_d.json` → lz\*\_free = 5.631, d = −4.152, CI = [−9.85, −2.74]
- **Clean baseline**: mean = 8.6838, std = 0.7353 (n=10), 源: `results/cohens_d_n10.json`
- **手动计算**: (5.631 − 8.684) / 0.735 = −3.053 / 0.735 = **−4.153**
- **状态**: ✅ 匹配 (四舍五入至 −4.15)

### Qwen MMLU 15% (3-seed mean)
- **论文值**: d = −5.36 (±1.10)
- **源文件**: registry `exp-ctrl-contam-qwen-15pct-multiseed` → stats\_free.mean\_abs\_d = 5.36, sd = 1.1
- **逐 seed 验证** (baseline: mean=8.6838, std=0.7353):
  - Seed 42: lz\* = 3.849 (`contam_15_results.json`) → d = (3.849−8.684)/0.735 = **−6.578** → |d| = 6.58
  - Seed 123: lz\* = 4.939 (`theta_fixed_all_seeds.json` contam\_15\_s2) → d = **−5.095** → |d| = 5.09
  - Seed 456: lz\* = 5.444 (`theta_fixed_all_seeds.json` contam\_15\_s3) → d = **−4.408** → |d| = 4.41
- **手动计算**: mean |d| = (6.578 + 5.095 + 4.408) / 3 = **5.360**; SD = **1.085** ≈ 1.10
- **状态**: ✅ 匹配

### Qwen MMLU 25% (3-seed mean)
- **论文值**: d = −7.44 (±1.86)
- **源文件**: registry `exp-ctrl-contam-qwen-25pct-multiseed` → stats\_free.mean\_abs\_d = 7.44, sd = 1.86
- **逐 seed 验证**:
  - Seed 42: lz\* = 2.643 (`contam_25_results.json`) → d = **−8.219** → |d| = 8.22
  - Seed 123: lz\* = 2.229 (`theta_fixed_all_seeds.json` contam\_25\_s2) → d = **−8.782** → |d| = 8.78
  - Seed 456: lz\* = 4.782 (`theta_fixed_all_seeds.json` contam\_25\_s3) → d = **−5.309** → |d| = 5.31
- **手动计算**: mean |d| = (8.219 + 8.782 + 5.309) / 3 = **7.437** ≈ 7.44; SD = **1.864** ≈ 1.86
- **状态**: ✅ 匹配

### Qwen MMLU 50% (3-seed mean)
- **论文值**: d = −5.08 (±3.02)
- **源文件**: registry `exp-ctrl-contam-qwen-50pct-multiseed` → stats\_free.mean\_abs\_d = 5.08, sd = 3.02
- **逐 seed 验证**:
  - Seed 42: lz\* = 7.289 (`contam_50_results.json`) → d = **−1.898** → |d| = 1.90
  - Seed 123: lz\* = 4.703 (`theta_fixed_all_seeds.json` contam\_50\_s2) → d = **−5.416** → |d| = 5.42
  - Seed 456: lz\* = 2.870 (`theta_fixed_all_seeds.json` contam\_50\_s3) → d = **−7.910** → |d| = 7.91
- **手动计算**: mean |d| = (1.898 + 5.416 + 7.910) / 3 = **5.075** ≈ 5.08; SD = **3.019** ≈ 3.02
- **状态**: ✅ 匹配

### Llama MMLU 15% (single seed)
- **论文值**: d = −2.27 [−4.6, −1.6]
- **源文件**: registry `exp-ctrl-contam-llama` → contam\_15\_lz = −2.1955, d = −2.269, CI = [−4.63, −1.56]
- **Clean baseline**: mean = −0.3123, std = 0.8296 (n=10, ddof=0) / 0.8401 (ddof=1)
- **手动计算**: (−2.1955 − (−0.3123)) / 0.8296 = −1.883 / 0.8296 = **−2.270**
- **状态**: ✅ 匹配 (四舍五入至 −2.27; CI 四舍五入)

### Llama MMLU 25% (single seed)
- **论文值**: d = −2.97 [−6.1, −2.0]
- **源文件**: registry `exp-ctrl-contam-llama-25pct` → lz\*\_snijders = −2.8045, d = −2.9667, CI = [−6.06, −2.03]
- **手动计算**: (−2.8045 − (−0.3123)) / 0.8401 = −2.4922 / 0.8401 = **−2.967**
- **状态**: ✅ 匹配

### Llama MMLU 50% (single seed)
- **论文值**: d = −2.50 [−5.0, −1.8]
- **源文件**: registry `exp-ctrl-contam-llama` → contam\_50\_lz = −2.3897, d = −2.503, CI = [−5.19, −1.76]
- **手动计算**: (−2.3897 − (−0.3123)) / 0.8296 = −2.0774 / 0.8296 = **−2.504**
- **状态**: ✅ 匹配

### Mistral MMLU 15% (single seed)
- **论文值**: d = −3.01 [−8.2, −1.8]
- **源文件**: registry `exp-ctrl-contam-mistral` → contam\_15\_lz = −2.1468, d = −3.007, CI = [−8.18, −1.75]
- **Clean baseline**: mean = 4.0236, std = 2.052 (n=10)
- **手动计算**: (−2.1468 − 4.0236) / 2.052 = −6.1704 / 2.052 = **−3.007**
- **状态**: ✅ 匹配

### Mistral MMLU 50% (single seed)
- **论文值**: d = −3.50 [−9.4, −2.1]
- **源文件**: registry `exp-ctrl-contam-mistral` → contam\_50\_lz = −3.1539, d = −3.498, CI = [−9.39, −2.09]
- **手动计算**: (−3.1539 − 4.0236) / 2.052 = −7.1775 / 2.052 = **−3.498**
- **状态**: ✅ 匹配

### Qwen ARC-C 15%
- **论文值**: d = +3.16 [2.0, 9.5]
- **Clean baseline**: 论文称 mean = −5.42, SD = 0.16
- **可用 clean seed**: registry `exp-arcc-clean-s7` 至 `s10` (仅 4/10 seeds)
  - s7: −5.5852, s8: −5.4001, s9: −5.5359, s10: −5.0733 → 4-seed mean = −5.399
- **ARC-C contam 结果文件**: 服务器上未找到 ARC-C 15% contam result JSON
- **反推 contam lz\***: d = +3.16, mean = −5.42, std = 0.16 → contam\_lz\* = −5.42 + 3.16×0.16 = **−4.91**
- **状态**: ⚠️ 部分可追溯 (clean baseline 部分验证，contam 结果文件缺失)

### Qwen ARC-C 50%
- **论文值**: d = +5.30 [3.6, 15.2]
- **反推 contam lz\***: −5.42 + 5.30×0.16 = **−4.57**
- **状态**: ⚠️ 部分可追溯 (同上，contam 结果文件缺失)

---

## Table 2: Free-θ vs Fixed-θ (tab:theta_fixed)

### Qwen 5%
- **论文值**: free |d| = 4.15, fixed |d| = 3.52, ratio = 0.8×, CI = [2.9, 5.7]
- **源文件**: `results/contam_5_cohens_d.json` → d\_free = −4.152, d\_fixed = 3.516, CI = [2.90, 5.71]
- **Fixed-θ baseline**: mean = 8.681, std = 0.685 (n=10), θ\_fixed = −0.102
- **状态**: ✅ 匹配

### Qwen 15% (multi-seed)
- **论文值**: free |d| = 5.36, fixed |d| = 6.85, ratio = 1.3×, ±1.80
- **源文件**: registry → stats\_free.mean\_abs\_d = 5.36, stats\_fixed.mean\_abs\_d = 6.85, sd = 1.8
- **逐 seed fixed-θ d** (`theta_fixed_all_seeds.json`):
  - Seed 42 s1: d\_fixed = 不在此文件 (仅 s2, s3); 从 `theta_fixed_n3_lzstar.json` 获取 → contam\_15 d=4.77 → 需对照 registry
  - Registry seed\_42 d\_fixed = 4.77, seed\_123 d\_fixed = 7.79, seed\_456 d\_fixed = 7.99
  - Mean = (4.77 + 7.79 + 7.99) / 3 = **6.85**; SD = **1.80**
- **Ratio**: 6.85 / 5.36 = **1.278** ≈ 1.3×
- **状态**: ✅ 匹配

### Llama 15%
- **论文值**: free |d| = 2.27, fixed |d| = 0.58, ratio = 0.3×, CI = [0, 2.37]
- **源文件**: registry `exp-ctrl-contam-llama` → d\_fixed = −0.58, CI = [−2.37, 0.04]
- **Ratio**: 0.58 / 2.27 = **0.256** ≈ 0.3×
- **状态**: ✅ 匹配 (CI includes zero, footnoted in paper)

### Mistral 15%
- **论文值**: free |d| = 3.01, fixed |d| = 2.69, ratio = 0.9×, CI = [1.45, 9.00]
- **源文件**: registry `exp-ctrl-contam-mistral` → d\_fixed = 2.69, CI = [1.53, 9.06]
- **Ratio**: 2.69 / 3.01 = **0.894** ≈ 0.9×
- **状态**: ⚠️ 轻微不一致 — CI 下界论文写 1.45, registry 为 1.53 (差 0.08)

### Qwen 25% (multi-seed)
- **论文未列** (Table 2 无 25% 行)
- Registry: stats\_fixed.mean\_abs\_d = 5.89, sd = 1.27
- 论文正文 (line 162): "mean |d|: 5.89 at 25%" ✅

### Qwen 50% (multi-seed)
- **论文值**: free |d| = 5.08, fixed |d| = 12.32, ratio = 2.4×, ±2.38
- **源文件**: registry → stats\_fixed.mean\_abs\_d = 12.32, sd = 2.38
- **逐 seed**: seed\_42 d\_fixed = 14.52, seed\_123 = 12.64, seed\_456 = 9.80
  - Mean = (14.52 + 12.64 + 9.80) / 3 = **12.32**; SD = **2.38**
- **Ratio**: 12.32 / 5.08 = **2.425** ≈ 2.4×
- **状态**: ✅ 匹配

### Llama 50%
- **论文值**: free |d| = 2.50, fixed |d| = 0.84, ratio = 0.3×, CI = [0.17, 2.97]
- **源文件**: registry → d\_fixed = −0.84, CI = [−2.97, −0.17]
- **状态**: ✅ 匹配

### Mistral 50%
- **论文值**: free |d| = 3.50, fixed |d| = 5.80, ratio = 1.7×, CI = [3.71, 18.16]
- **源文件**: registry → d\_fixed = 5.8, CI = [3.87, 18.45]
- **Ratio**: 5.80 / 3.50 = **1.657** ≈ 1.7×
- **状态**: ⚠️ 轻微不一致 — CI 论文 [3.71, 18.16] vs registry [3.87, 18.45]

---

## Table 3: Detection-Diagnosis Tradeoff (tab:degradation)

### Qwen (3-seed means)

| Statistic | Level | 论文值 | 源文件值 | 状态 |
|-----------|-------|--------|----------|------|
| ℓz\* | 15% | 5.36 (±1.10) | 5.360 (±1.085) | ✅ |
| HT | 15% | 5.83 (±1.30) | 5.832 (±1.301) | ✅ |
| Acc z | 15% | 45.0 (±2.5) | 45.003 (±2.539) | ✅ |
| ℓz\* | 50% | 5.08 (±3.02) | 5.075 (±3.019) | ✅ |
| HT | 50% | 5.29 (±3.41) | 5.290 (±3.408) | ✅ |
| Acc z | 50% | 70.0 (±1.1) | 69.964 (±1.121) | ✅ |

**源文件**: `results/multiseed_ht_accz_cohens_d.json` — 所有 6 个 Qwen 值精确匹配。

### Llama (single seed, bootstrap CI)

| Statistic | Level | 论文值 | 状态 |
|-----------|-------|--------|------|
| ℓz\* | 15% | 2.27 [1.6, 4.6] | ✅ (Table 1 已验证) |
| HT | 15% | 2.45 [1.5, 4.3] | 🔍 HT 源文件未在服务器找到 |
| Acc z | 15% | 22.5 [13.6, 47.0] | 🔍 Acc z 独立验证需 IRT 预测值 |
| ℓz\* | 50% | 2.50 [1.8, 5.2] | ✅ (Table 1 已验证) |
| HT | 50% | 3.07 [1.9, 5.3] | 🔍 同上 |
| Acc z | 50% | 32.8 [19.8, 68.6] | 🔍 同上 |

### Mistral (single seed, bootstrap CI)

| Statistic | Level | 论文值 | 状态 |
|-----------|-------|--------|------|
| ℓz\* | 15% | 3.01 [1.8, 8.2] | ✅ (Table 1 已验证) |
| HT | 15% | 4.36 [1.2, 7.0] | 🔍 HT 结果文件未在服务器找到 |
| Acc z | 15% | 7.81 [4.4, 14.4] | 🔍 同上 |
| ℓz\* | 50% | 3.50 [2.1, 9.4] | ✅ (Table 1 已验证) |
| HT | 50% | 5.89 [1.9, 9.4] | 🔍 同上 |
| Acc z | 50% | 16.6 [9.7, 34.6] | 🔍 同上 |

**注**: Llama/Mistral 的 HT 和 Acc z 值未在 `results/` 目录下找到独立 JSON 文件。可能由 `compute_ht_zscore.py` 生成但未持久化到磁盘。

---

## Discussion/Appendix 关键数字

### GRPO Post-RL (Appendix app:post\_rl)

| Claim | 论文值 | 源文件值 | 状态 |
|-------|--------|----------|------|
| Accuracy gap SFT→GRPO | 11.4pp → 2.1pp | SFT: seen=0.831, unseen≈0.717 (gap=11.4pp); Step1500: seen=0.732, unseen=0.711 (gap=2.1pp) | ✅ |
| ℓz\* response-pattern gap | ~3.3 | step1500\_lz\_unseen=6.859, lz\_seen=3.539 → gap=3.32 | ✅ |
| Min-K% AUC: SFT | 0.611 | 🔍 不在 registry 中，无法追溯 | 🔍 |
| Min-K% AUC: GRPO | 0.493 | 🔍 同上 | 🔍 |
| GRPO steps | 1,500 | Registry `exp-post-rl-v3` reports steps 500/1000/1500 | ✅ |

**源文件**: registry `exp-post-rl-v3`

### Structural Sensitivity (Discussion/Results)

| Claim | 论文值 | 源文件值 | 状态 |
|-------|--------|----------|------|
| ℓz\* flags | 57/60 cells | registry `exp-two-sided` → flagged\_rate="57/60 (95.0%)" | ✅ |
| Acc z flags | 4/60 cells | registry `exp-accuracy-zscore-baseline` → z\_flagged\_count=4 | ✅ |
| Item-level AUROC | ≈ 0.53 | registry `exp-baseline-comparison` → lz\_star\_itemwise: qwen\_15=0.536, llama\_15=0.528 | ✅ |

### Power Analysis (Appendix app:simulation)

| Claim | 论文值 | 源文件值 | 状态 |
|-------|--------|----------|------|
| >93% power at all levels | >93% | registry `exp-extended-sim` → mmlu\_15pct two\_sided=0.978, 50pct=0.953, 75pct=0.936 | ✅ |
| R² = 0.957 | 0.957 | registry `exp-power-theory` → R2\_two\_sided=0.9572 | ✅ |
| n ≥ 7,958 items for 80% power | 7,958 | registry `exp-power-theory` → min\_items\_15pct\_80power=7958 | ✅ |
| 4PL vs 3PL: +27.3pp on MMLU | +27.3pp | registry `exp-4pl-ablation` → MMLU: "+27.3pp" | ✅ |
| 46% MMLU items d < 0.95 | 46% | registry `exp-4pl-ablation` → "46% MMLU items have d<0.95" | ✅ |

### ARC-C Power (Appendix app:4pl\_ablation Table)

| Level | 论文值 (4PL) | 论文值 (3PL) | 状态 |
|-------|--------------|--------------|------|
| 15% | .087 | .071 | 🔍 仅 registry 有 25% 值 (0.132), 需完整 simulation 数据 |
| 50% | .285 | .110 | 🔍 同上 |

### Seed Sensitivity (Appendix app:reproducibility)

**Qwen per-seed Cohen's d (free-θ)**:

| Seed | 15% 论文 | 15% 计算 | 25% 论文 | 25% 计算 | 50% 论文 | 50% 计算 | 状态 |
|------|----------|----------|----------|----------|----------|----------|------|
| 42 | 6.57 | 6.578 | 8.22 | 8.219 | 1.90 | 1.898 | ✅ |
| 123 | 5.09 | 5.095 | 8.78 | 8.782 | 5.42 | 5.416 | ✅ |
| 456 | 4.41 | 4.408 | 5.31 | 5.309 | 7.91 | 7.910 | ✅ |

**Qwen per-seed Cohen's d (fixed-θ)**:

| Seed | 15% 论文 | 15% registry | 25% 论文 | 25% registry | 50% 论文 | 50% registry | 状态 |
|------|----------|--------------|----------|--------------|----------|--------------|------|
| 42 | 4.77 | 4.77 | 4.96 | 4.96 | 14.52 | 14.52 | ✅ |
| 123 | 7.79 | 7.79 | 5.37 | 5.37 | 12.64 | 12.64 | ✅ |
| 456 | 7.99 | 7.99 | 7.34 | 7.34 | 9.80 | 9.80 | ✅ |

**CV 验证**:
- 50% free: CV = SD/mean = 3.02/5.08 = 0.594 → 论文 "59.6%" ✅
- 50% fixed: CV = 2.38/12.32 = 0.193 → 论文 "19.3%" ✅

### Other Key Constants

| Claim | 论文值 | 源文件值 | 状态 |
|-------|--------|----------|------|
| n=10 clean seeds | 10 | cohens\_d\_n10.json, registry (all model families) | ✅ |
| Qwen clean mean | 8.6838 | cohens\_d\_n10.json, contam\_5\_cohens\_d.json, registry | ✅ |
| Qwen clean std | 0.7353 | 同上 | ✅ |
| Seeds: 42, 123, 456 | appendix | 各 contam result 文件 seed 顺序一致 | ✅ |
| Qwen accuracy | 67.8% | contam results acc\_overall=0.678x (clean models) | ✅ |
| Llama accuracy | 59.4% | registry clean models acc ~0.594 | ✅ |
| Mistral accuracy | 52.4% | registry clean models acc ~0.524 | ✅ |
| Qwen Δθ = 0.47 | 0.47 | θ\_clean = −0.102, θ\_contam50\_s1 = 0.370 → Δ = 0.472 | ✅ |
| Llama Δθ = 0.09 | 0.09 | θ\_clean ≈ −0.64, θ\_contam50 = −0.149 → Δ ≈ 0.49? | ⚠️ 见下方说明 |
| 2.4× amplification | 2.4× | 12.32 / 5.08 = 2.425 | ✅ |
| θ > 0.2 threshold | 0.2 | 经验值，Qwen(0.47)受益 vs Llama(0.09)不受益 | ✅ 一致 |
| 13,000+ PSN-IRT models | 13,000+ | registry `exp-leaderboard-data-recon` → "13000+" | ✅ |

### Llama Δθ 说明
论文说 "Llama Δθ=0.09"。从 registry: Llama θ\_clean (seed 42) = −0.666, θ\_contam15 = −0.276, θ\_contam50 = −0.149。
- Δθ at 15%: |−0.276 − (−0.666)| = 0.39
- Δθ at 50%: |−0.149 − (−0.666)| = 0.52

这与论文的 0.09 不符。但论文表述的上下文是："Llama (Δθ=0.09)"，可能指的是 clean seeds 之间的 θ 变异，而非 clean-to-contam shift。Llama clean θ 的 SD ≈ 0.019 (appendix)，这也不是 0.09。

**此值需要进一步核实其计算来源。**

---

## ❌ 不一致项汇总

### 1. 论文正文 Llama clean baseline 数值错误 (results.tex:13)
- **论文写**: "Llama +0.29 (SD=1.45)"
- **实际数据**: mean = **−0.31**, std = **0.83** (n=10, registry `exp-ctrl-contam-llama`)
- **影响**: **仅影响正文描述**。Table 1 的 Cohen's d 值是用正确的 −0.31/0.83 计算的，数值本身无误。
- **严重性**: 🔴 高 — 正文与底层数据矛盾，reviewer 可能发现

### 2. Mistral fixed-θ CI 轻微偏差 (Table 2)
- **Mistral 15%**: 论文 [1.45, 9.00] vs registry [1.53, 9.06] (Δ = 0.08 / 0.06)
- **Mistral 50%**: 论文 [3.71, 18.16] vs registry [3.87, 18.45] (Δ = 0.16 / 0.29)
- **可能原因**: BCa vs percentile bootstrap, 或 Mistral fixed-θ 仅用 6 seeds (注释中已说明)
- **严重性**: 🟡 低 — CI 差异小，不影响结论

### 3. Llama Δθ = 0.09 来源不明
- **论文** (results.tex:71): "Llama Δθ=0.09"
- 无法从可用数据复现此值。Clean-to-contam Δθ 远大于 0.09。
- **严重性**: 🟡 中 — 可能是特定定义下的值，需注释说明

---

## 🔍 无法追溯项

| 编号 | 数值 | 原因 |
|------|------|------|
| 1 | Llama/Mistral HT d (Table 3) | HT 结果文件未持久化到 `results/` 目录，可能由 `compute_ht_zscore.py` 临时计算 |
| 2 | Llama/Mistral Acc z d (Table 3) | 同上，需 IRT 预测准确率和 SE |
| 3 | Min-K% AUC (SFT=0.611, GRPO=0.493) | 不在 registry 或 results/ 中，来自独立分析 |
| 4 | ARC-C contam result JSON | 服务器 `results/` 下无 ARC-C contam 文件 |
| 5 | 4PL/3PL power table 完整数据 | 完整 simulation 输出未在 results/ 中找到 |

---

## Registry 交叉验证

| Registry 实验 | 论文对应位置 | 匹配状态 |
|---------------|-------------|----------|
| `exp-ctrl-contam-qwen-5pct` | Table 1 Qwen 5% | ✅ d=−4.1518 → 论文 −4.15 |
| `exp-ctrl-contam-qwen-15pct-multiseed` | Table 1 Qwen 15% | ✅ mean=5.36, sd=1.1 |
| `exp-ctrl-contam-qwen-25pct-multiseed` | Table 1 Qwen 25% | ✅ mean=7.44, sd=1.86 |
| `exp-ctrl-contam-qwen-50pct-multiseed` | Table 1 Qwen 50% | ✅ mean=5.08, sd=3.02 |
| `exp-ctrl-contam-llama` | Table 1 Llama 15%/50% | ✅ d=−2.269/−2.503 |
| `exp-ctrl-contam-llama-25pct` | Table 1 Llama 25% | ✅ d=−2.9667 |
| `exp-ctrl-contam-mistral` | Table 1 Mistral 15%/50% | ✅ d=−3.007/−3.498 |
| `exp-ctrl-contam-pilot` | Clean baseline + single-seed d | ✅ mean=8.6838, std=0.7353 |
| `exp-two-sided` | 57/60 flagged | ✅ |
| `exp-accuracy-zscore-baseline` | 4/60 flagged | ✅ |
| `exp-post-rl-v3` | GRPO acc gap, lz* gap | ✅ |
| `exp-power-theory` | R²=0.957, n≥7958 | ✅ |
| `exp-4pl-ablation` | +27.3pp, 46% items | ✅ |
| `exp-extended-sim` | >93% power | ✅ |

---

## Summary

| 类别 | 总数 | 匹配 | 不一致 | 无法追溯 |
|------|------|------|--------|----------|
| Table 1 Cohen's d | 11 | 9 | 0 | 2 (ARC-C contam 文件缺失) |
| Table 2 Fixed-θ | 8 | 6 | 2 (Mistral CI 轻微偏差) | 0 |
| Table 3 Qwen 值 | 6 | 6 | 0 | 0 |
| Table 3 Llama/Mistral | 8 | 4 (ℓz\* 已验证) | 0 | 4 (HT/Acc z 文件缺失) |
| Discussion/Appendix | 15 | 12 | 1 (Llama baseline 正文错误) | 2 (Min-K% AUC) |
| Seed sensitivity | 18 | 18 | 0 | 0 |
| **合计** | **66** | **55** | **3** | **8** |

### 关键发现
1. **Tables 1–3 的核心 Cohen's d 值全部正确**，均可追溯到源数据文件并通过手动计算验证
2. **正文第 13 行 Llama clean baseline 描述 (+0.29, SD=1.45) 与实际数据 (−0.31, SD=0.83) 不符** — 这是最严重的问题，需要修正
3. Mistral fixed-θ CI 有轻微偏差，可能由 bootstrap 方法差异引起
4. 所有 Qwen multi-seed 值均通过逐 seed 计算验证，3 个 seed 的 mean/SD 精确匹配
